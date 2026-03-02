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
import os
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
MAX_RETRIES = int(os.environ.get("SWARM_MAX_RETRIES", "1"))
TOKEN_BUDGET = int(os.environ.get("SWARM_TOKEN_BUDGET", "500000"))

from google import genai
from google.genai import types

if not API_KEY:
    print("❌ GEMINI_API_KEY not found in .env or environment")
    sys.exit(1)

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
    extraction_context: str  # relevant genius patterns + hidden knowledge
    skill_context: str       # SKILL.md content for framework consistency
    output_path: Path

@dataclass
class PromptResult:
    """Result from generating a single prompt."""
    prompt_slug: str
    status: str  # success, failed, skipped
    output: str
    tokens_used: int
    duration_seconds: float
    output_path: Optional[Path] = None
    error: Optional[str] = None


# --------------------------------------------------------------------------
# Gemini API
# --------------------------------------------------------------------------

async def call_gemini(prompt: str, system_instruction: str = "",
                      retries: int = MAX_RETRIES) -> Tuple[str, int]:
    """Make a single Gemini API call via async SDK. Returns (response_text, tokens_used)."""
    client = genai.Client(api_key=API_KEY)
    
    config = types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=16384,
    )
    if system_instruction:
        config.system_instruction = system_instruction
        
    for attempt in range(retries + 1):
        try:
            response = await client.aio.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=config
            )
            # Extract token usage if available; otherwise use 0
            tokens = 0
            if response.usage_metadata:
                tokens = response.usage_metadata.total_token_count
            return response.text, tokens

        except Exception as e:
            if attempt < retries:
                wait = 2 ** attempt
                print(f"  ⚠️  Retry {attempt + 1}/{retries} for API call (waiting {wait}s): {e}")
                await asyncio.sleep(wait)
            else:
                raise


# --------------------------------------------------------------------------
# Context Loading
# --------------------------------------------------------------------------

def load_extraction_report(extraction_path: str) -> str:
    """Load the extraction report content."""
    path = WORKSPACE / extraction_path if not Path(extraction_path).is_absolute() else Path(extraction_path)
    if not path.exists():
        print(f"❌ Extraction report not found: {path}")
        sys.exit(1)
    return path.read_text()


def load_skill_md(skill_path: str) -> str:
    """Load the SKILL.md for framework context."""
    path = WORKSPACE / skill_path / "SKILL.md" if not Path(skill_path).is_absolute() else Path(skill_path) / "SKILL.md"
    if not path.exists():
        raise FileNotFoundError(f"CRITICAL: Required SKILL.md not found at {path}. Halting to prevent generic extraction.")
    return path.read_text()


def load_genius_patterns(skill_path: str) -> str:
    """Load genius patterns for additional context."""
    path = WORKSPACE / skill_path / "references" / "genius-patterns.md" if not Path(skill_path).is_absolute() else Path(skill_path) / "references" / "genius-patterns.md"
    if not path.exists():
        print(f"⚠️  genius-patterns.md not found at {path}, proceeding without it")
        return ""
    return path.read_text()


def load_hidden_knowledge(skill_path: str) -> str:
    """Load hidden knowledge for additional context."""
    path = WORKSPACE / skill_path / "references" / "hidden-knowledge.md" if not Path(skill_path).is_absolute() else Path(skill_path) / "references" / "hidden-knowledge.md"
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

    # Parse prompt descriptions from SKILL.md if available
    prompt_descriptions = {}
    if skill_md:
        for line in skill_md.splitlines():
            if "|" in line and "`" in line:
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if len(parts) >= 2 and parts[0].startswith("`"):
                    slug = parts[0].strip("`").strip()
                    desc = parts[1].strip()
                    prompt_descriptions[slug] = desc

    # Build combined context (Gemini 3.1 Pro High context uncapped)
    combined_context = f"""## EXTRACTION REPORT
{extraction_report}

## GENIUS PATTERNS
{genius_patterns}

## HIDDEN KNOWLEDGE
{hidden_knowledge}
"""

    # Resolve output directory
    base = WORKSPACE / skill_path if not Path(skill_path).is_absolute() else Path(skill_path)
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

async def generate_prompt(work_order: PromptWorkOrder, token_tracker: dict) -> PromptResult:
    """Generate a single crown jewel prompt via Gemini API."""
    start_time = time.time()
    slug = work_order.prompt_slug

    # Check token budget
    if token_tracker["used"] >= TOKEN_BUDGET:
        return PromptResult(
            prompt_slug=slug,
            status="skipped",
            output="",
            tokens_used=0,
            duration_seconds=0,
            error=f"Token budget exceeded ({token_tracker['used']}/{TOKEN_BUDGET})"
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
        response, tokens = await call_gemini(prompt, SYSTEM_INSTRUCTION)
        token_tracker["used"] += tokens

        duration = time.time() - start_time
        print(f"  ✅ {slug} complete ({tokens:,} tokens, {duration:.1f}s)")

        return PromptResult(
            prompt_slug=slug,
            status="success",
            output=response,
            tokens_used=tokens,
            duration_seconds=duration,
            output_path=work_order.output_path,
        )

    except Exception as e:
        duration = time.time() - start_time
        print(f"  ❌ {slug} failed: {e}")

        return PromptResult(
            prompt_slug=slug,
            status="failed",
            output="",
            tokens_used=0,
            duration_seconds=duration,
            error=str(e),
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

    print(f"\n{'='*60}")
    print(f"  EXTRACTION SWARM — {len(prompts)} prompts")
    print(f"  Model: {MODEL}")
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
        prompts=prompts,
        expert_name=expert_name,
        expert_domain=expert_domain,
        extraction_report=extraction_report,
        skill_md=skill_md,
        genius_patterns=genius_patterns,
        hidden_knowledge=hidden_knowledge,
        skill_path=skill_path,
    )

    print(f"\n📋 Work Orders ({len(orders)}):")
    for o in orders:
        print(f"   → {o.prompt_slug}: {o.prompt_description[:60]}...")
        print(f"     Output: {o.output_path}")

    if plan_only:
        print(f"\n🔍 Plan-only mode — no API calls made.")
        estimated_cost = len(orders) * 0.006  # ~$0.006 per prompt on Flash
        print(f"   Estimated cost: ${estimated_cost:.3f}")
        return []

    # Execute all in parallel
    print(f"\n⚡ Firing {len(orders)} parallel API calls...\n")
    token_tracker = {"used": 0}
    start_time = time.time()

    tasks = [generate_prompt(order, token_tracker) for order in orders]
    results = await asyncio.gather(*tasks)

    total_duration = time.time() - start_time
    total_tokens = sum(r.tokens_used for r in results)

    # Cost calculation (Gemini 3 Flash approximate)
    cost_per_1m_input = 0.10
    cost_per_1m_output = 0.40
    # Rough split: ~60% input, 40% output
    estimated_cost = (total_tokens * 0.6 * cost_per_1m_input / 1_000_000) + \
                     (total_tokens * 0.4 * cost_per_1m_output / 1_000_000)

    # Write files (unless dry-run)
    successful = [r for r in results if r.status == "success"]
    failed = [r for r in results if r.status == "failed"]
    skipped = [r for r in results if r.status == "skipped"]

    if not dry_run and successful:
        print(f"\n💾 Writing {len(successful)} prompt files...")
        for r in successful:
            if r.output_path:
                r.output_path.parent.mkdir(parents=True, exist_ok=True)
                # Clean output — strip markdown fences if present
                output = r.output
                if output.startswith("```"):
                    lines = output.splitlines()
                    # Remove first and last line if they're code fences
                    if lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].strip() == "```":
                        lines = lines[:-1]
                    output = "\n".join(lines)

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
    print(f"  📊 Total tokens: {total_tokens:,}")
    print(f"  💰 Estimated cost: ${estimated_cost:.4f}")
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
    parser.add_argument(
        "--extraction", "-e",
        required=True,
        help="Path to extraction report (relative to workspace or absolute)",
    )
    parser.add_argument(
        "--skill", "-s",
        required=True,
        help="Path to skill directory (relative to workspace or absolute)",
    )
    parser.add_argument(
        "--prompts", "-p",
        required=True,
        help="Comma-separated prompt slugs to generate",
    )
    parser.add_argument(
        "--expert-name",
        default="",
        help="Expert name (auto-detected from SKILL.md if not provided)",
    )
    parser.add_argument(
        "--expert-domain",
        default="",
        help="Expert domain (auto-detected from SKILL.md if not provided)",
    )
    parser.add_argument(
        "--plan-only",
        action="store_true",
        help="Show work orders without executing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Generate prompts but don't write files",
    )
    parser.add_argument(
        "--model",
        default=None,
        help=f"Override model (default: {MODEL})",
    )

    args = parser.parse_args()

    # Override model if specified
    if args.model:
        globals()["MODEL"] = args.model

    prompts = [p.strip() for p in args.prompts.split(",") if p.strip()]

    if not prompts:
        print("❌ No prompts specified")
        sys.exit(1)

    results = asyncio.run(execute_extraction_swarm(
        prompts=prompts,
        extraction_path=args.extraction,
        skill_path=args.skill,
        expert_name=args.expert_name,
        expert_domain=args.expert_domain,
        plan_only=args.plan_only,
        dry_run=args.dry_run,
    ))

    # Exit code based on results
    if any(r.status == "failed" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
