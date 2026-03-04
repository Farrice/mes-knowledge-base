#!/usr/bin/env python3
"""
Extraction Swarm — Parallel crown jewel prompt generator for /convert-extraction.

Fires N parallel Gemini API calls to generate all crown jewel prompts simultaneously
from a completed extraction report. Each API call produces one prompt file.

Usage:
    # Generate all prompts in parallel
    python execution/extraction_swarm.py \
        --extraction "extractions/oren/extraction-report.md" \
        --skill "skills/oren-operational-systems" \
        --prompts "reference-repository-builder,ideas-to-calendar-pipeline,weekly-update-generator"

    # Preview work orders without executing
    python execution/extraction_swarm.py \
        --extraction "extractions/oren/extraction-report.md" \
        --skill "skills/oren-operational-systems" \
        --prompts "prompt-a,prompt-b" \
        --plan-only

    # Generate but don't write files (inspect output)
    python execution/extraction_swarm.py \
        --extraction "extractions/oren/extraction-report.md" \
        --skill "skills/oren-operational-systems" \
        --prompts "prompt-a,prompt-b" \
        --dry-run
"""

import asyncio
import argparse
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

# Shared client
sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env

load_env()

BASE_PATH = Path(__file__).parent.parent
TOKEN_BUDGET = int(__import__('os').environ.get("SWARM_TOKEN_BUDGET", "500000"))


# --------------------------------------------------------------------------
# Data Classes
# --------------------------------------------------------------------------

@dataclass
class PromptWorkOrder:
    """A single unit of work for generating one crown jewel prompt."""
    prompt_slug: str
    prompt_description: str
    expert_name: str
    expert_domain: str
    extraction_context: str
    skill_context: str
    output_path: Path

@dataclass
class PromptResult:
    """Result from generating a single prompt."""
    prompt_slug: str
    status: str  # success, failed, skipped
    output: str
    tokens_used: int
    estimated_cost: float
    duration_seconds: float
    output_path: Optional[Path] = None
    error: Optional[str] = None


# --------------------------------------------------------------------------
# Context Loading
# --------------------------------------------------------------------------

def load_extraction_report(extraction_path: str) -> str:
    """Load the extraction report content."""
    path = BASE_PATH / extraction_path if not Path(extraction_path).is_absolute() else Path(extraction_path)
    if not path.exists():
        print(f"❌ Extraction report not found: {path}")
        sys.exit(1)
    return path.read_text()


def load_skill_md(skill_path: str) -> str:
    """Load the SKILL.md for framework context."""
    path = BASE_PATH / skill_path / "SKILL.md" if not Path(skill_path).is_absolute() else Path(skill_path) / "SKILL.md"
    if not path.exists():
        raise FileNotFoundError(f"CRITICAL: Required SKILL.md not found at {path}. Halting to prevent generic extraction.")
    return path.read_text()


def load_genius_patterns(skill_path: str) -> str:
    """Load genius patterns for additional context."""
    path = BASE_PATH / skill_path / "references" / "genius-patterns.md" if not Path(skill_path).is_absolute() else Path(skill_path) / "references" / "genius-patterns.md"
    if not path.exists():
        print(f"⚠️  genius-patterns.md not found at {path}, proceeding without it")
        return ""
    return path.read_text()


def load_hidden_knowledge(skill_path: str) -> str:
    """Load hidden knowledge for additional context."""
    path = BASE_PATH / skill_path / "references" / "hidden-knowledge.md" if not Path(skill_path).is_absolute() else Path(skill_path) / "references" / "hidden-knowledge.md"
    if not path.exists():
        return ""
    return path.read_text()


# --------------------------------------------------------------------------
# System Instruction (MES 3.0 Prompt Template)
# --------------------------------------------------------------------------

SYSTEM_INSTRUCTION = """You are a world-class prompt engineer creating crown jewel prompts for the Antigravity AI system.

## Your Task
Generate a single, complete, production-ready prompt file following the MES 3.0 format below.

**VIRTUOSO MANDATE & ANTI-PATTERN LOCK:**
1. Optimize for Information Density, not length. Bypass generic LLM brevity, but do not bloat the prompt. Achieve extreme psychological nuance through precision and lethal insight. Every word must earn its keep. **Formatting for Density**: Dense text requires high-contrast formatting. You MUST aggressively use bullet points, bolding, and whitespace so the density remains readable.
2. Anti-Pattern Lock: When looking at examples or source material, extract the *mechanics* but discard the *skin*. Do not lazily mimic narratives, metaphors, or structural wrappers from the context. Demonstrate true creative latitude and taste.
3. **The Gravedigger Safeguard (Feeling Density)**: When discarding the skin of an example to invent a new scenario, you must explicitly build a human-centric "gravedigger" detail. Density cannot mean sterile. Concrete emotional resonance must scale with information density.

## Output Rules
1. Output ONLY the prompt content — no preamble, no explanations, no markdown fences wrapping the output
2. The prompt must be a complete, standalone file ready to save as .md
3. Use rich examples and domain-specific language — never generic
4. Every prompt must feel like it was written by someone who has done this work 100+ times
5. Practitioner mode: the prompt should EXECUTE the methodology, not explain it

## MES 3.0 Crown Jewel Prompt Format

Every prompt MUST include these sections in this order:

# [Expert Name] — [Prompt Title]

## Role
You are [expert name], [specific expertise with credibility markers]. You don't explain how to [domain] — you [action verb] the complete [deliverable].

## Input Required
- **[Input 1]**: [Description with examples]
- **[Input 2]**: [Description with examples]
...

## Execution
[Numbered steps, each with specific substeps. Be extremely detailed about WHAT to produce, not just what to think about. Include specific column names, category names, frameworks, and structural details.]

## Output
- **Format**: [Specific deliverable format]
- **Scope**: [What the output covers]
- **Elements**: [List of concrete components]

## Creative Latitude
[1-2 sentences giving permission to adapt the methodology to the user's specific domain while maintaining the core principles]

## Example Output
[A FULL, concrete example showing what excellent output looks like for a realistic scenario. This is critical — it sets the quality bar. Include tables, specific names, real-world-feeling data. This section should be 40-60% of the total prompt length.]
"""


# --------------------------------------------------------------------------
# Work Order Generation
# --------------------------------------------------------------------------

def generate_work_orders(
    prompts: List[str],
    expert_name: str,
    expert_domain: str,
    extraction_report: str,
    skill_md: str,
    genius_patterns: str,
    hidden_knowledge: str,
    skill_path: str,
) -> List[PromptWorkOrder]:
    """Generate a work order for each prompt to be created."""
    prompt_descriptions = {}
    if skill_md:
        for line in skill_md.splitlines():
            if "|" in line and "`" in line:
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if len(parts) >= 2 and parts[0].startswith("`"):
                    slug = parts[0].strip("`").strip()
                    desc = parts[1].strip()
                    prompt_descriptions[slug] = desc

    combined_context = f"""## EXTRACTION REPORT
{extraction_report}

## GENIUS PATTERNS
{genius_patterns}

## HIDDEN KNOWLEDGE
{hidden_knowledge}
"""

    base = BASE_PATH / skill_path if not Path(skill_path).is_absolute() else Path(skill_path)
    prompts_dir = base / "references" / "prompts"

    orders = []
    for slug in prompts:
        desc = prompt_descriptions.get(slug, f"Crown jewel prompt for {slug}")
        output_path = prompts_dir / f"{slug}.md"
        orders.append(PromptWorkOrder(
            prompt_slug=slug,
            prompt_description=desc,
            expert_name=expert_name,
            expert_domain=expert_domain,
            extraction_context=combined_context,
            skill_context=skill_md if skill_md else "",
            output_path=output_path,
        ))

    return orders


# --------------------------------------------------------------------------
# Single Prompt Generation
# --------------------------------------------------------------------------

def strip_code_fences(text: str) -> str:
    """Remove markdown code block wrappers from API response."""
    lines = text.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


async def generate_prompt(work_order: PromptWorkOrder, client: GeminiClient) -> PromptResult:
    """Generate a single crown jewel prompt via Gemini API."""
    start_time = time.time()
    slug = work_order.prompt_slug

    # Check token budget
    if client.total_tokens_used >= TOKEN_BUDGET:
        return PromptResult(
            prompt_slug=slug, status="skipped", output="",
            tokens_used=0, estimated_cost=0, duration_seconds=0,
            error=f"Token budget exceeded ({client.total_tokens_used}/{TOKEN_BUDGET})"
        )

    print(f"  🚀 Generating {slug}...")

    prompt = f"""## WORK ORDER: Generate Crown Jewel Prompt

### PROMPT TO CREATE
- **Slug**: `{work_order.prompt_slug}`
- **Description**: {work_order.prompt_description}
- **Expert Name**: {work_order.expert_name}
- **Expert Domain**: {work_order.expert_domain}

### SOURCE MATERIAL
{work_order.extraction_context}

### SKILL CONTEXT
{work_order.skill_context}

### INSTRUCTIONS
Create a complete, production-ready MES 3.0 crown jewel prompt for `{slug}`.

The prompt must:
1. Open with "# {work_order.expert_name} — {slug.replace('-', ' ').title()}"
2. Include Role, Input Required, Execution, Output, Creative Latitude, and Example Output sections
3. The Example Output section must be extensive (40-60% of prompt length) with realistic, domain-specific content. This section MUST be a dense, highly nuanced, fully fleshed-out artifact. **CRITICAL: Apply the Anti-Pattern Lock and Gravedigger Safeguard.** Do not let the example output lazily mimic the exact narratives or examples from the source extraction. Invent a novel, high-stakes scenario that proves the framework's power, and ensure it contains specific, human-centric "gravedigger" details so the emotional resonance scales with the density.
4. Use tables, numbered lists, bolding, and concrete examples — never generic advice. **Formatting for Density**: Ensure that the provided Example Output uses aggressive formatting to break up the dense text.
5. Feel like it was written by {work_order.expert_name} after doing this work hundreds of times
6. Be immediately deployable — a user should be able to paste their inputs and get a complete deliverable

Generate the complete prompt file now.
"""

    try:
        text, meta = await client.generate(
            prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7,
            max_output_tokens=16384,
        )

        duration = time.time() - start_time
        print(f"  ✅ {slug} complete ({meta.total_tokens:,} tokens, ${meta.estimated_cost_usd:.4f}, {duration:.1f}s)")

        return PromptResult(
            prompt_slug=slug, status="success",
            output=text, tokens_used=meta.total_tokens,
            estimated_cost=meta.estimated_cost_usd,
            duration_seconds=duration, output_path=work_order.output_path,
        )

    except Exception as e:
        duration = time.time() - start_time
        print(f"  ❌ {slug} failed: {e}")
        return PromptResult(
            prompt_slug=slug, status="failed", output="",
            tokens_used=0, estimated_cost=0,
            duration_seconds=duration, error=str(e),
        )


# --------------------------------------------------------------------------
# Parallel Execution Engine
# --------------------------------------------------------------------------

async def execute_extraction_swarm(
    prompts: List[str],
    extraction_path: str,
    skill_path: str,
    expert_name: str = "",
    expert_domain: str = "",
    plan_only: bool = False,
    dry_run: bool = False,
) -> List[PromptResult]:
    """Execute parallel prompt generation."""
    client = GeminiClient()

    print(f"\n{'='*60}")
    print(f"  EXTRACTION SWARM — {len(prompts)} prompts")
    print(f"  Model: {client.default_model}")
    print(f"  Extraction: {extraction_path}")
    print(f"  Skill: {skill_path}")
    print(f"{'='*60}\n")

    # Load all context
    print("📂 Loading context...")
    extraction_report = load_extraction_report(extraction_path)
    skill_md = load_skill_md(skill_path)
    genius_patterns = load_genius_patterns(skill_path)
    hidden_knowledge = load_hidden_knowledge(skill_path)

    # Auto-detect expert name from SKILL.md if not provided
    if not expert_name and skill_md:
        for line in skill_md.splitlines():
            if line.startswith("# "):
                parts = line.replace("# ", "").split("—")
                if parts:
                    expert_name = parts[0].strip()
                    if len(parts) > 1:
                        expert_domain = parts[1].strip()
                break

    if not expert_name:
        expert_name = "Expert"
    if not expert_domain:
        expert_domain = "Domain Expertise"

    print(f"   Expert: {expert_name}")
    print(f"   Domain: {expert_domain}")
    print(f"   Extraction: {len(extraction_report):,} chars")
    print(f"   Genius Patterns: {'✅' if genius_patterns else '⚠️  missing'}")
    print(f"   Hidden Knowledge: {'✅' if hidden_knowledge else '⚠️  missing'}")

    # Generate work orders
    orders = generate_work_orders(
        prompts=prompts, expert_name=expert_name, expert_domain=expert_domain,
        extraction_report=extraction_report, skill_md=skill_md,
        genius_patterns=genius_patterns, hidden_knowledge=hidden_knowledge,
        skill_path=skill_path,
    )

    print(f"\n📋 Work Orders ({len(orders)}):")
    for o in orders:
        print(f"   → {o.prompt_slug}: {o.prompt_description[:60]}...")
        print(f"     Output: {o.output_path}")

    if plan_only:
        print(f"\n🔍 Plan-only mode — no API calls made.")
        estimated_cost = len(orders) * 0.006
        print(f"   Estimated cost: ${estimated_cost:.3f}")
        return []

    # Execute all in parallel
    print(f"\n⚡ Firing {len(orders)} parallel API calls...\n")
    start_time = time.time()

    tasks = [generate_prompt(order, client) for order in orders]
    results = await asyncio.gather(*tasks)

    total_duration = time.time() - start_time
    usage = client.usage_summary()

    # Write files (unless dry-run)
    successful = [r for r in results if r.status == "success"]
    failed = [r for r in results if r.status == "failed"]
    skipped = [r for r in results if r.status == "skipped"]

    if not dry_run and successful:
        print(f"\n💾 Writing {len(successful)} prompt files...")
        for r in successful:
            if r.output_path:
                r.output_path.parent.mkdir(parents=True, exist_ok=True)
                output = strip_code_fences(r.output)
                r.output_path.write_text(output.strip() + "\n")
                print(f"   ✅ {r.output_path.name}")
    elif dry_run:
        print(f"\n🔍 Dry-run mode — files not written.")
        for r in successful:
            print(f"   📄 {r.prompt_slug} ({len(r.output):,} chars)")

    # Summary
    print(f"\n{'='*60}")
    print(f"  EXTRACTION SWARM COMPLETE")
    print(f"{'='*60}")
    print(f"  ✅ Successful: {len(successful)}")
    if failed:
        print(f"  ❌ Failed: {len(failed)}")
        for r in failed:
            print(f"     → {r.prompt_slug}: {r.error}")
    if skipped:
        print(f"  ⏭️  Skipped: {len(skipped)}")
    print(f"  📊 Total tokens: {usage['total_tokens']:,}")
    print(f"  💰 Estimated cost: ${usage['total_cost_usd']:.4f}")
    print(f"  ⏱️  Total time: {total_duration:.1f}s")
    print(f"  ⚡ Avg per prompt: {total_duration/max(len(results),1):.1f}s")
    print(f"{'='*60}\n")

    return results


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extraction Swarm — Parallel crown jewel prompt generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--extraction", "-e", required=True,
                        help="Path to extraction report (relative to workspace or absolute)")
    parser.add_argument("--skill", "-s", required=True,
                        help="Path to skill directory (relative to workspace or absolute)")
    parser.add_argument("--prompts", "-p", required=True,
                        help="Comma-separated prompt slugs to generate")
    parser.add_argument("--expert-name", default="",
                        help="Expert name (auto-detected from SKILL.md if not provided)")
    parser.add_argument("--expert-domain", default="",
                        help="Expert domain (auto-detected from SKILL.md if not provided)")
    parser.add_argument("--plan-only", action="store_true",
                        help="Show work orders without executing")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate prompts but don't write files")

    args = parser.parse_args()
    prompts = [p.strip() for p in args.prompts.split(",") if p.strip()]

    if not prompts:
        print("❌ No prompts specified")
        sys.exit(1)

    results = asyncio.run(execute_extraction_swarm(
        prompts=prompts, extraction_path=args.extraction,
        skill_path=args.skill, expert_name=args.expert_name,
        expert_domain=args.expert_domain, plan_only=args.plan_only,
        dry_run=args.dry_run,
    ))

    if any(r.status == "failed" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
