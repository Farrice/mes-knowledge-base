#!/usr/bin/env python3
"""
Skill Converter — Transforms prompt-library skills into completion-engine workflows.

Converts expert skills from the old format (15-45 atomic prompts) to the new format
(3-5 end-to-end workflows that carry full genius context).

Usage:
    # Convert a single skill
    python execution/skill_converter.py --skill "skills/april-dunford-positioning"

    # Convert all expert skills
    python execution/skill_converter.py --all

    # Preview what would happen (no writes, no API calls)
    python execution/skill_converter.py --all --plan-only

    # Convert but don't call API (just do deterministic merge of genius files)
    python execution/skill_converter.py --all --merge-only
"""

import asyncio
import argparse
import json
import os
import re
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# --------------------------------------------------------------------------
# Environment Setup
# --------------------------------------------------------------------------
WORKSPACE = Path("/Users/farricecain/Google Antigravity")
ENV_PATH = WORKSPACE / ".env"

if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")
MAX_RETRIES = 2
BATCH_SIZE = 8  # skills processed in parallel per batch
MAX_CONCURRENT_API = 15  # max concurrent Gemini calls

from google import genai
from google.genai import types

# Semaphore for API concurrency control
api_semaphore = asyncio.Semaphore(MAX_CONCURRENT_API)

# --------------------------------------------------------------------------
# Tool Skills and Meta Skills (skip these)
# --------------------------------------------------------------------------
SKIP_SKILLS = {
    "canvas-design", "docx", "frontend-design", "gemini-api-dev",
    "internal-comms", "mcp-builder", "pdf", "pptx", "react-components",
    "remotion-video-creation", "slack-gif-creator", "theme-factory",
    "web-artifacts-builder", "webapp-testing", "xlsx", "design-md",
    "algorithmic-art", "asset_generator", "brand-guidelines",
    "consumer-posture-research", "creative-assembly", "doc-coauthoring",
    "market_intelligence", "seena_rez_early_adopter", "skill-creator",
    "stitch-loop", "swarm-commander",
}

# --------------------------------------------------------------------------
# Data Classes
# --------------------------------------------------------------------------

@dataclass
class SkillInfo:
    """Metadata about an existing skill."""
    name: str
    path: Path
    skill_md: str
    genius_patterns: str
    hidden_knowledge: str
    prompts: Dict[str, str]  # filename -> content
    prompt_count: int
    has_extraction: bool
    extraction_path: Optional[Path]
    expert_name: str
    expert_domain: str

@dataclass
class WorkflowPlan:
    """Plan for converting a skill into workflows."""
    skill_name: str
    workflows: List[Dict]  # [{name, slug, produces, prompts_consolidated, description}]

@dataclass
class ConversionResult:
    """Result of converting a single skill."""
    skill_name: str
    status: str  # success, failed, skipped
    workflows_created: int
    tokens_used: int
    duration_seconds: float
    error: Optional[str] = None


# --------------------------------------------------------------------------
# Gemini API
# --------------------------------------------------------------------------

async def call_gemini(prompt: str, system_instruction: str = "",
                      retries: int = MAX_RETRIES, temperature: float = 0.5) -> Tuple[str, int]:
    """Make a single Gemini API call. Returns (response_text, tokens_used)."""
    async with api_semaphore:
        client = genai.Client(api_key=API_KEY)
        config = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=16384,
        )
        if system_instruction:
            config.system_instruction = system_instruction

        for attempt in range(retries + 1):
            try:
                response = await client.aio.models.generate_content(
                    model=MODEL, contents=prompt, config=config
                )
                tokens = 0
                if response.usage_metadata:
                    tokens = response.usage_metadata.total_token_count
                return response.text, tokens
            except Exception as e:
                if attempt < retries:
                    wait = 2 ** (attempt + 1)
                    print(f"    ⚠️  Retry {attempt + 1}/{retries} ({wait}s): {e}")
                    await asyncio.sleep(wait)
                else:
                    raise


# --------------------------------------------------------------------------
# Skill Discovery & Loading
# --------------------------------------------------------------------------

def discover_expert_skills() -> List[Path]:
    """Find all expert skill directories."""
    skills_dir = WORKSPACE / "skills"
    expert_skills = []
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir():
            continue
        if d.name in SKIP_SKILLS:
            continue
        if d.name.startswith("_") or d.name.startswith("."):
            continue
        # Must have SKILL.md to be a real skill
        if not (d / "SKILL.md").exists():
            continue
        expert_skills.append(d)
    return expert_skills


def load_skill(skill_path: Path) -> SkillInfo:
    """Load all content from an existing skill."""
    skill_md = ""
    if (skill_path / "SKILL.md").exists():
        skill_md = (skill_path / "SKILL.md").read_text()

    genius_patterns = ""
    gp_path = skill_path / "references" / "genius-patterns.md"
    if gp_path.exists():
        genius_patterns = gp_path.read_text()

    hidden_knowledge = ""
    hk_path = skill_path / "references" / "hidden-knowledge.md"
    if hk_path.exists():
        hidden_knowledge = hk_path.read_text()

    # Load all prompt files
    prompts = {}
    prompts_dir = skill_path / "references" / "prompts"
    if prompts_dir.exists():
        for f in sorted(prompts_dir.iterdir()):
            if f.suffix == ".md" and f.is_file():
                try:
                    prompts[f.name] = f.read_text()
                except Exception:
                    prompts[f.name] = ""

    # Extract expert name and domain from SKILL.md
    expert_name = ""
    expert_domain = ""
    for line in skill_md.splitlines():
        if line.startswith("# ") and not expert_name:
            parts = line.replace("# ", "").split("—")
            if not parts:
                parts = line.replace("# ", "").split(":")
            if parts:
                expert_name = parts[0].strip()
                if len(parts) > 1:
                    expert_domain = parts[1].strip()
            break
    # Fallback: derive from directory name
    if not expert_name:
        expert_name = skill_path.name.replace("-", " ").title()

    # Check for extraction report
    extraction_path = None
    has_extraction = False
    # Try common extraction paths
    slug = expert_name.lower().replace(" ", "-")
    for candidate in [
        WORKSPACE / "extractions" / slug,
        WORKSPACE / "extractions" / skill_path.name.split("-")[0],
        WORKSPACE / "extractions" / "-".join(skill_path.name.split("-")[:2]),
    ]:
        if candidate.exists() and (candidate / "extraction-report.md").exists():
            extraction_path = candidate / "extraction-report.md"
            has_extraction = True
            break

    return SkillInfo(
        name=skill_path.name,
        path=skill_path,
        skill_md=skill_md,
        genius_patterns=genius_patterns,
        hidden_knowledge=hidden_knowledge,
        prompts=prompts,
        prompt_count=len(prompts),
        has_extraction=has_extraction,
        extraction_path=extraction_path,
        expert_name=expert_name,
        expert_domain=expert_domain,
    )


# --------------------------------------------------------------------------
# Phase 1: Deterministic Merge (genius.md creation)
# --------------------------------------------------------------------------

def merge_genius_file(skill: SkillInfo) -> str:
    """Merge genius-patterns.md + hidden-knowledge.md into genius.md."""
    sections = []
    sections.append(f"# {skill.expert_name} — Genius Context\n")
    sections.append("> Load this file before executing any workflow. It contains the full")
    sections.append("> extraction intelligence — patterns, tacit knowledge, and operating")
    sections.append("> principles that make this expert's output actually work.\n")

    if skill.genius_patterns:
        # Extract just the pattern content (skip any redundant title)
        content = skill.genius_patterns
        # Remove leading "# Genius Patterns — ..." header if present
        lines = content.splitlines()
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        content = "\n".join(lines).strip()
        sections.append("## Genius Patterns\n")
        sections.append(content)
        sections.append("")

    if skill.hidden_knowledge:
        content = skill.hidden_knowledge
        lines = content.splitlines()
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        content = "\n".join(lines).strip()
        sections.append("## Hidden Knowledge\n")
        sections.append(content)
        sections.append("")

    if not skill.genius_patterns and not skill.hidden_knowledge:
        sections.append("## Genius Patterns\n")
        sections.append("*No genius patterns extracted yet. Run extraction to populate.*\n")

    return "\n".join(sections) + "\n"


def execute_deterministic_merge(skill: SkillInfo, dry_run: bool = False) -> bool:
    """Phase 1: Create genius.md, workflows dir, archive old prompts."""
    skill_path = skill.path

    # 1. Create genius.md
    genius_content = merge_genius_file(skill)
    genius_path = skill_path / "genius.md"
    if not dry_run:
        genius_path.write_text(genius_content)

    # 2. Create workflows directory
    workflows_dir = skill_path / "workflows"
    if not dry_run:
        workflows_dir.mkdir(exist_ok=True)

    # 3. Archive old prompts (move to _legacy-prompts)
    prompts_dir = skill_path / "references" / "prompts"
    legacy_dir = skill_path / "references" / "_legacy-prompts"
    if prompts_dir.exists() and any(prompts_dir.iterdir()):
        if not dry_run:
            legacy_dir.mkdir(exist_ok=True)
            for f in prompts_dir.iterdir():
                if f.is_file() and f.suffix == ".md":
                    shutil.copy2(f, legacy_dir / f.name)

    return True


# --------------------------------------------------------------------------
# Phase 2: Intelligent Conversion (Gemini-powered)
# --------------------------------------------------------------------------

PLANNER_SYSTEM = """You are a skill architect converting expert knowledge from atomic prompts into end-to-end completion workflows.

Your task: Given an expert's full skill context (SKILL.md, genius patterns, hidden knowledge, and all prompt files), identify 3-5 natural end-to-end workflows that consolidate the prompts.

Rules:
1. Each workflow MUST produce a specific, named deliverable (not "insights" — a document, plan, audit, etc.)
2. Each workflow should consolidate 2-8 related prompts into one integrated flow
3. Every prompt must be assigned to exactly one workflow — nothing lost
4. Workflows should mirror how the expert actually thinks, not how prompts were originally organized
5. Maximum 5 workflows per skill. If there are only 1-3 prompts, create 1-2 workflows.

Output ONLY valid JSON, no markdown fences, no explanation:
{
  "expert_name": "...",
  "expert_domain": "...",
  "workflows": [
    {
      "slug": "01-kebab-case-name",
      "name": "Human Readable Name",
      "produces": "Specific deliverable description",
      "use_when": "Trigger condition for this workflow",
      "prompts_consolidated": ["filename1.md", "filename2.md"],
      "description": "2-3 sentence description of what this workflow does end-to-end"
    }
  ]
}"""

WORKFLOW_SYSTEM = """You are a world-class prompt engineer rewriting expert knowledge into end-to-end completion workflows for the Antigravity AI system.

## Your Task
Generate a single, complete workflow file that consolidates multiple atomic prompts into ONE integrated, end-to-end execution flow.

## Critical Rules
1. The workflow carries the expert's FULL genius — not a fragment. Every genius pattern and hidden knowledge item that's relevant should be embedded inline where it applies.
2. The workflow produces a SPECIFIC, COMPLETE deliverable — not a partial step.
3. Mirror how the expert actually thinks — continuous flow, not disconnected steps.
4. Each phase should build on the previous phase's output — the integration IS the value.
5. Include an Output Contract specifying exactly what the user receives.
6. Include a Quality Gate with expert-specific criteria.

## VIRTUOSO MANDATE
- Information density over length. Every word earns its keep.
- Anti-Pattern Lock: Extract mechanics, discard narrative skin. Don't lazily mimic.
- Gravedigger Safeguard: Density cannot mean sterile — embed concrete emotional resonance.

## Output Rules
- Output ONLY the workflow content — no preamble, no markdown fences wrapping the output
- The output must be a complete, standalone .md file ready to save
- Use the expert's actual terminology and frameworks, not generic business language
"""


async def plan_workflows(skill: SkillInfo) -> WorkflowPlan:
    """Use Gemini to identify 3-5 natural workflows from the prompt collection."""
    # Build prompt inventory (names + descriptions, not full content — saves tokens)
    prompt_inventory = []
    for fname, content in skill.prompts.items():
        # Extract name and description from frontmatter or first heading
        desc = fname
        lines = content.splitlines()
        for line in lines:
            if line.startswith("description:"):
                desc = line.replace("description:", "").strip().strip('"').strip("'")
                break
            if line.startswith("# ") and not line.startswith("# Role"):
                desc = line.replace("# ", "").strip()
                break
        prompt_inventory.append(f"- `{fname}`: {desc}")

    prompt_list = "\n".join(prompt_inventory) if prompt_inventory else "No prompts found."

    # Build context
    prompt = f"""## SKILL TO CONVERT
**Expert**: {skill.expert_name}
**Domain**: {skill.expert_domain}
**Current Prompt Count**: {skill.prompt_count}

## CURRENT SKILL.md
{skill.skill_md[:3000]}

## PROMPT INVENTORY
{prompt_list}

## GENIUS PATTERNS (summary)
{skill.genius_patterns[:2000] if skill.genius_patterns else "Not available"}

## HIDDEN KNOWLEDGE (summary)
{skill.hidden_knowledge[:1500] if skill.hidden_knowledge else "Not available"}

## INSTRUCTIONS
Analyze this expert's prompt collection and identify 3-5 natural end-to-end workflows that consolidate ALL prompts. Each workflow should produce a specific deliverable. Assign every prompt to exactly one workflow.

If there are 3 or fewer prompts, create 1-2 workflows.
If there are 4-10 prompts, create 2-3 workflows.
If there are 11-25 prompts, create 3-4 workflows.
If there are 26+ prompts, create 4-5 workflows.

Output ONLY valid JSON."""

    response, tokens = await call_gemini(prompt, PLANNER_SYSTEM)

    # Parse JSON response (strip markdown fences if present)
    cleaned = response.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned = "\n".join(lines)

    try:
        plan_data = json.loads(cleaned)
    except json.JSONDecodeError:
        # Try to extract JSON from response
        match = re.search(r'\{[\s\S]*\}', cleaned)
        if match:
            plan_data = json.loads(match.group())
        else:
            raise ValueError(f"Could not parse workflow plan JSON for {skill.name}")

    return WorkflowPlan(
        skill_name=skill.name,
        workflows=plan_data.get("workflows", []),
    )


async def generate_workflow(skill: SkillInfo, workflow: Dict, genius_content: str) -> Tuple[str, int]:
    """Generate a single workflow file by consolidating relevant prompts."""
    # Gather the full content of prompts being consolidated
    consolidated_prompts = []
    for fname in workflow.get("prompts_consolidated", []):
        if fname in skill.prompts:
            consolidated_prompts.append(f"### Source: {fname}\n{skill.prompts[fname]}")
        else:
            # Try matching without number prefix
            for actual_fname, content in skill.prompts.items():
                if fname.replace(".md", "") in actual_fname:
                    consolidated_prompts.append(f"### Source: {actual_fname}\n{content}")
                    break

    prompts_content = "\n\n---\n\n".join(consolidated_prompts) if consolidated_prompts else "No source prompts available."

    # Truncate if too long (keep under ~30K tokens input)
    if len(prompts_content) > 60000:
        prompts_content = prompts_content[:60000] + "\n\n[... truncated for token budget ...]"

    prompt = f"""## WORK ORDER: Generate Completion Engine Workflow

### WORKFLOW TO CREATE
- **Slug**: `{workflow.get('slug', '01-workflow')}`
- **Name**: {workflow.get('name', 'Workflow')}
- **Produces**: {workflow.get('produces', 'Deliverable')}
- **Description**: {workflow.get('description', '')}

### EXPERT CONTEXT
- **Expert**: {skill.expert_name}
- **Domain**: {skill.expert_domain}

### GENIUS CONTEXT (load into workflow)
{genius_content[:4000]}

### SOURCE PROMPTS TO CONSOLIDATE
These atomic prompts must be merged into ONE integrated end-to-end workflow:

{prompts_content}

### INSTRUCTIONS
Create a complete workflow file in this exact format:

---
name: "{workflow.get('name', 'Workflow')}"
produces: "{workflow.get('produces', 'Deliverable')}"
expert: "{skill.expert_name}"
load_context: "genius.md"
---

# {skill.expert_name} — {workflow.get('name', 'Workflow')}

## Role
[Expert identity with credibility markers — 2-3 sentences]

**Before executing**: Read genius.md for full extraction intelligence.

## Input Required
[3-6 essential inputs the user must provide]

## Workflow
[Integrated end-to-end flow consolidating ALL source prompts above.
Key requirements:
- Mirror how the expert thinks, not how prompts were organized
- Embed relevant genius patterns INLINE where they apply
- Each phase builds on the previous — the integration is the value
- Be specific: include exact framework names, column headers, evaluation criteria
- This is a COMPLETION engine: the output is a finished deliverable, not advice]

## Output Contract
[Exact specification of what the user receives — components, format, scope]

## Quality Gate
[3-5 expert-specific criteria — "Would {skill.expert_name} approve this?"]

Generate the complete workflow file now. Output ONLY the file content."""

    response, tokens = await call_gemini(prompt, WORKFLOW_SYSTEM)

    # Clean output
    output = response.strip()
    if output.startswith("```"):
        lines = output.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        output = "\n".join(lines)

    return output.strip() + "\n", tokens


def generate_new_skill_md(skill: SkillInfo, plan: WorkflowPlan) -> str:
    """Generate new SKILL.md in completion engine format."""
    workflows_table = []
    for i, w in enumerate(plan.workflows):
        slug = w.get("slug", f"0{i+1}-workflow")
        name = w.get("name", "Workflow")
        produces = w.get("produces", "Deliverable")
        use_when = w.get("use_when", "")
        workflows_table.append(f"| {slug.split('-')[0]} | [{name}](workflows/{slug}.md) | {produces} | {use_when} |")

    workflows_str = "\n".join(workflows_table)
    wf_count = len(plan.workflows)

    # Extract description from old SKILL.md frontmatter
    description = ""
    for line in skill.skill_md.splitlines():
        if line.strip().startswith("description:"):
            description = line.split(":", 1)[1].strip().strip('"').strip("'")
            break

    # Extract overview paragraph from old SKILL.md
    overview = ""
    in_overview = False
    for line in skill.skill_md.splitlines():
        if line.startswith("## Overview") or (line.startswith("# ") and not overview):
            in_overview = True
            continue
        if in_overview and line.startswith("## "):
            break
        if in_overview and line.strip():
            overview += line + "\n"
    overview = overview.strip()
    if not overview:
        overview = f"{skill.expert_name}'s core methodology, extracted and deployed as end-to-end completion workflows."

    # Build title: include domain only if present
    title = skill.expert_name
    if skill.expert_domain:
        title = f"{skill.expert_name} — {skill.expert_domain}"

    # Keep it dense
    content = f"""---
name: "{title}"
description: "{description}"
version: "2.0"
format: "completion-engine"
workflows: {wf_count}
---

# {title}

{overview[:500]}

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
{workflows_str}

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
"""

    return content


# --------------------------------------------------------------------------
# Full Conversion Pipeline
# --------------------------------------------------------------------------

async def convert_skill(skill: SkillInfo, dry_run: bool = False, merge_only: bool = False) -> ConversionResult:
    """Convert a single skill from prompt-library to completion-engine format."""
    start_time = time.time()
    total_tokens = 0
    skill_name = skill.name

    print(f"\n  📦 {skill_name} ({skill.prompt_count} prompts)")

    try:
        # Phase 1: Deterministic merge
        genius_content = merge_genius_file(skill)
        execute_deterministic_merge(skill, dry_run=dry_run)
        print(f"    ✅ genius.md merged")

        if merge_only:
            if not dry_run:
                (skill.path / "genius.md").write_text(genius_content)
            duration = time.time() - start_time
            return ConversionResult(skill_name, "success", 0, 0, duration)

        # Phase 2: Plan workflows
        plan = await plan_workflows(skill)
        wf_count = len(plan.workflows)
        print(f"    📋 Planned {wf_count} workflows")

        # Phase 3: Generate workflow files in parallel
        tasks = []
        for w in plan.workflows:
            tasks.append(generate_workflow(skill, w, genius_content))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Write files
        workflows_created = 0
        for w, result in zip(plan.workflows, results):
            if isinstance(result, Exception):
                print(f"    ❌ Failed: {w.get('slug')}: {result}")
                continue

            content, tokens = result
            total_tokens += tokens
            slug = w.get("slug", f"0{workflows_created + 1}-workflow")

            if not dry_run:
                wf_path = skill.path / "workflows" / f"{slug}.md"
                wf_path.parent.mkdir(parents=True, exist_ok=True)
                wf_path.write_text(content)

            workflows_created += 1
            print(f"    ✅ {slug}")

        # Write new SKILL.md
        new_skill_md = generate_new_skill_md(skill, plan)
        if not dry_run:
            # Backup old SKILL.md
            old_path = skill.path / "SKILL.md.old"
            if not old_path.exists():
                shutil.copy2(skill.path / "SKILL.md", old_path)
            (skill.path / "SKILL.md").write_text(new_skill_md)
        print(f"    ✅ SKILL.md rewritten")

        duration = time.time() - start_time
        print(f"    ⚡ Done in {duration:.1f}s ({total_tokens:,} tokens)")

        return ConversionResult(skill_name, "success", workflows_created, total_tokens, duration)

    except Exception as e:
        duration = time.time() - start_time
        print(f"    ❌ FAILED: {e}")
        return ConversionResult(skill_name, "failed", 0, total_tokens, duration, str(e))


async def convert_batch(skills: List[SkillInfo], dry_run: bool = False, merge_only: bool = False) -> List[ConversionResult]:
    """Convert a batch of skills in parallel."""
    tasks = [convert_skill(s, dry_run=dry_run, merge_only=merge_only) for s in skills]
    return await asyncio.gather(*tasks)


async def run_full_conversion(
    target_skill: Optional[str] = None,
    plan_only: bool = False,
    dry_run: bool = False,
    merge_only: bool = False,
):
    """Run the full conversion pipeline."""
    print(f"\n{'='*60}")
    print(f"  SKILL CONVERTER — Completion Engine Migration")
    print(f"  Model: {MODEL}")
    print(f"  Mode: {'plan-only' if plan_only else 'dry-run' if dry_run else 'merge-only' if merge_only else 'LIVE'}")
    print(f"{'='*60}\n")

    # Discover skills
    if target_skill:
        skill_path = WORKSPACE / target_skill if not Path(target_skill).is_absolute() else Path(target_skill)
        if not skill_path.exists():
            print(f"❌ Skill not found: {skill_path}")
            sys.exit(1)
        skill_paths = [skill_path]
    else:
        skill_paths = discover_expert_skills()

    print(f"📂 Found {len(skill_paths)} expert skills to convert\n")

    # Load all skills
    skills = []
    for p in skill_paths:
        skill = load_skill(p)
        if skill.prompt_count == 0 and not skill.genius_patterns:
            print(f"  ⏭️  Skipping {skill.name} (no prompts or genius patterns)")
            continue
        skills.append(skill)

    print(f"\n📊 Skills to convert: {len(skills)}")
    print(f"   Total prompts to consolidate: {sum(s.prompt_count for s in skills)}")
    print(f"   Skills with extractions: {sum(1 for s in skills if s.has_extraction)}")

    if plan_only:
        print(f"\n🔍 Plan-only mode — listing skills that would be converted:")
        for s in skills:
            print(f"   → {s.name}: {s.prompt_count} prompts, extraction: {'✅' if s.has_extraction else '❌'}")
        est_calls = sum(1 + min(5, max(1, s.prompt_count // 5)) for s in skills)
        est_cost = est_calls * 0.008
        print(f"\n   Estimated API calls: {est_calls}")
        print(f"   Estimated cost: ${est_cost:.2f}")
        return

    # Process in batches
    all_results = []
    start_time = time.time()

    for i in range(0, len(skills), BATCH_SIZE):
        batch = skills[i:i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (len(skills) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"\n{'─'*40}")
        print(f"  BATCH {batch_num}/{total_batches}")
        print(f"{'─'*40}")

        results = await convert_batch(batch, dry_run=dry_run, merge_only=merge_only)
        all_results.extend(results)

        # Brief pause between batches to avoid rate limits
        if i + BATCH_SIZE < len(skills):
            await asyncio.sleep(2)

    # Summary
    total_time = time.time() - start_time
    successful = [r for r in all_results if r.status == "success"]
    failed = [r for r in all_results if r.status == "failed"]
    total_tokens = sum(r.tokens_used for r in all_results)
    total_workflows = sum(r.workflows_created for r in all_results)

    # Cost estimate
    cost_per_1m_input = 0.10
    cost_per_1m_output = 0.40
    estimated_cost = (total_tokens * 0.6 * cost_per_1m_input / 1_000_000) + \
                     (total_tokens * 0.4 * cost_per_1m_output / 1_000_000)

    print(f"\n{'='*60}")
    print(f"  CONVERSION COMPLETE")
    print(f"{'='*60}")
    print(f"  ✅ Successful: {len(successful)}/{len(all_results)}")
    if failed:
        print(f"  ❌ Failed: {len(failed)}")
        for r in failed:
            print(f"     → {r.skill_name}: {r.error}")
    print(f"  📦 Workflows created: {total_workflows}")
    print(f"  📊 Total tokens: {total_tokens:,}")
    print(f"  💰 Estimated cost: ${estimated_cost:.4f}")
    print(f"  ⏱️  Total time: {total_time:.1f}s ({total_time/60:.1f}min)")
    print(f"{'='*60}\n")

    # Write conversion log
    log = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "model": MODEL,
        "skills_converted": len(successful),
        "skills_failed": len(failed),
        "workflows_created": total_workflows,
        "total_tokens": total_tokens,
        "estimated_cost": estimated_cost,
        "duration_seconds": total_time,
        "results": [
            {
                "skill": r.skill_name,
                "status": r.status,
                "workflows": r.workflows_created,
                "tokens": r.tokens_used,
                "error": r.error,
            }
            for r in all_results
        ],
    }

    log_path = WORKSPACE / "execution" / "conversion-log.json"
    if not dry_run:
        log_path.write_text(json.dumps(log, indent=2))
        print(f"📝 Conversion log: {log_path}")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Skill Converter — Transform prompt libraries into completion engines",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--skill", "-s", help="Convert a single skill (path relative to workspace)")
    parser.add_argument("--all", action="store_true", help="Convert all expert skills")
    parser.add_argument("--plan-only", action="store_true", help="Preview what would be converted")
    parser.add_argument("--dry-run", action="store_true", help="Generate but don't write files")
    parser.add_argument("--merge-only", action="store_true", help="Only merge genius files (no API calls)")
    parser.add_argument("--model", default=None, help=f"Override model (default: {MODEL})")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help=f"Skills per batch (default: {BATCH_SIZE})")

    args = parser.parse_args()

    if args.model:
        globals()["MODEL"] = args.model
    if args.batch_size:
        globals()["BATCH_SIZE"] = args.batch_size

    if not args.skill and not args.all:
        print("❌ Specify --skill <path> or --all")
        sys.exit(1)

    if not API_KEY and not args.merge_only and not args.plan_only:
        print("❌ GEMINI_API_KEY not found in .env or environment")
        sys.exit(1)

    asyncio.run(run_full_conversion(
        target_skill=args.skill,
        plan_only=args.plan_only,
        dry_run=args.dry_run,
        merge_only=args.merge_only,
    ))


if __name__ == "__main__":
    main()
