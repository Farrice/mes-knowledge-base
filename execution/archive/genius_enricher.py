#!/usr/bin/env python3
"""
Genius Enricher — Retrofit existing genius.md files with savant-level context.

Adds 3 new sections to genius.md files that are missing them:
  - Hall of Fame Exemplars
  - Signature Moves
  - Expert-Specific Quality Rubric

Usage:
    # Preview enrichment plan (no API calls)
    python execution/genius_enricher.py --plan-only

    # Enrich a single expert (dry run — generate but don't write)
    python execution/genius_enricher.py --skill skills/kallaway-word-mastery --dry-run

    # Enrich a single expert (live)
    python execution/genius_enricher.py --skill skills/kallaway-word-mastery

    # Enrich all experts
    python execution/genius_enricher.py --all

    # Enrich all experts, skip DF/AP/VD cleanup
    python execution/genius_enricher.py --all --no-clean
"""

import asyncio
import argparse
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env

load_env()

BASE_PATH = Path(__file__).parent.parent
TOKEN_BUDGET = int(__import__('os').environ.get("ENRICHER_TOKEN_BUDGET", "1000000"))

# Sections we're adding
NEW_SECTIONS = ["Hall of Fame Exemplars", "Signature Moves", "Expert-Specific Quality Rubric"]

# Auto-generated template sections to clean up (corrupted/generic)
TEMPLATE_SECTIONS = ["Decision Framework", "Anti-Patterns", "Voice DNA"]


# --------------------------------------------------------------------------
# Data Classes
# --------------------------------------------------------------------------

@dataclass
class EnrichmentTarget:
    """A genius.md file that needs enrichment."""
    skill_name: str
    skill_path: Path
    genius_path: Path
    genius_content: str
    extraction_content: str  # may be empty
    expert_name: str
    missing_sections: List[str] = field(default_factory=list)
    has_template_sections: bool = False


@dataclass
class EnrichmentResult:
    """Result from enriching a single genius.md."""
    skill_name: str
    status: str  # success, failed, skipped, up-to-date
    sections_added: int
    tokens_used: int
    estimated_cost: float
    duration_seconds: float
    output: str = ""
    error: Optional[str] = None


# --------------------------------------------------------------------------
# Discovery & Assessment
# --------------------------------------------------------------------------

def discover_genius_files() -> List[Path]:
    """Find all skills that have a genius.md file."""
    skills_dir = BASE_PATH / "skills"
    results = []
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("_") or d.name.startswith("."):
            continue
        genius_path = d / "genius.md"
        if genius_path.exists():
            results.append(d)
    return results


def assess_genius_file(skill_path: Path) -> EnrichmentTarget:
    """Assess a genius.md file to determine what enrichment it needs."""
    genius_path = skill_path / "genius.md"
    genius_content = genius_path.read_text() if genius_path.exists() else ""

    # Find missing sections
    missing = []
    for section in NEW_SECTIONS:
        if f"## {section}" not in genius_content:
            missing.append(section)

    # Check for template sections (auto-generated DF/AP/VD)
    has_template = False
    for section in TEMPLATE_SECTIONS:
        if f"## {section}" in genius_content:
            has_template = True
            break

    # Extract expert name from SKILL.md
    expert_name = ""
    skill_md_path = skill_path / "SKILL.md"
    if skill_md_path.exists():
        for line in skill_md_path.read_text().splitlines():
            if line.startswith("# "):
                parts = line.replace("# ", "").split("—")
                if not parts:
                    parts = line.replace("# ", "").split(":")
                if parts:
                    expert_name = parts[0].strip()
                break
    if not expert_name:
        expert_name = skill_path.name.replace("-", " ").title()

    # Look for extraction report
    extraction_content = ""
    slug = expert_name.lower().replace(" ", "-")
    for candidate in [
        BASE_PATH / "extractions" / slug,
        BASE_PATH / "extractions" / skill_path.name.split("-")[0],
        BASE_PATH / "extractions" / "-".join(skill_path.name.split("-")[:2]),
    ]:
        report = candidate / "extraction-report.md"
        if report.exists():
            extraction_content = report.read_text()
            break

    return EnrichmentTarget(
        skill_name=skill_path.name,
        skill_path=skill_path,
        genius_path=genius_path,
        genius_content=genius_content,
        extraction_content=extraction_content,
        expert_name=expert_name,
        missing_sections=missing,
        has_template_sections=has_template,
    )


# --------------------------------------------------------------------------
# Template Section Cleanup
# --------------------------------------------------------------------------

def clean_template_sections(content: str) -> str:
    """Remove auto-generated DF/AP/VD template sections from genius.md content."""
    lines = content.splitlines()
    cleaned = []
    skip = False

    for i, line in enumerate(lines):
        # Check if this line starts a template section
        is_template_header = False
        for section in TEMPLATE_SECTIONS:
            if line.strip().startswith(f"## {section}"):
                is_template_header = True
                break

        if is_template_header:
            skip = True
            continue

        if skip:
            # Stop skipping when we hit the next ## header or end of file
            if line.strip().startswith("## ") and not any(
                line.strip().startswith(f"## {s}") for s in TEMPLATE_SECTIONS
            ):
                skip = False
                cleaned.append(line)
            # Also stop at # headers
            elif line.strip().startswith("# ") and not line.strip().startswith("## "):
                skip = False
                cleaned.append(line)
            # Otherwise keep skipping
            continue

        cleaned.append(line)

    result = "\n".join(cleaned)
    # Clean up excessive blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    return result.rstrip() + "\n"


# --------------------------------------------------------------------------
# Enrichment Prompt
# --------------------------------------------------------------------------

SYSTEM_INSTRUCTION = """You are a world-class expert extraction analyst for the Antigravity AI system.

Your task is to generate 3 specific sections for a genius.md file — the calibration context that makes an AI agent perform at savant level when embodying a specific expert.

## Output Rules
1. Output ONLY the 3 sections — no preamble, no explanations, no markdown fences wrapping the output.
2. Use ## headers for each section (## Hall of Fame Exemplars, ## Signature Moves, ## Expert-Specific Quality Rubric).
3. Content MUST be expert-specific — never generic. If the material comes from a copywriting expert, the exemplars must be copywriting exemplars. If from a screenwriting expert, screenwriting exemplars.
4. Exemplars should be verbatim or reconstructed from source material when available. If no source material, generate the most realistic possible exemplar BASED ON the genius patterns and hidden knowledge.
5. Signature moves must be BEHAVIORAL — actions, not concepts. "Always starts by X" not "Believes in X".
6. Quality rubric criteria must reflect THIS expert's standards, not generic quality standards.

## Anti-Pattern Lock
- Do NOT produce generic sections like "Quality of Writing" or "Clarity of Communication" — those apply to everyone.
- DO produce specific criteria like "Subtext Density: Score 4 = dialogue states feelings directly | Score 10 = every line means something other than what's said" (for a screenwriting expert).
- Signature moves should feel like trade secrets, not textbook advice.
"""


def build_enrichment_prompt(target: EnrichmentTarget) -> str:
    """Build the enrichment prompt for a single genius.md."""
    context_parts = []

    context_parts.append(f"## EXPERT: {target.expert_name}")
    context_parts.append(f"## SKILL: {target.skill_name}\n")

    context_parts.append("## EXISTING GENIUS.MD CONTENT")
    context_parts.append(target.genius_content[:12000])  # Cap to avoid token overflow

    if target.extraction_content:
        context_parts.append("\n## EXTRACTION REPORT (Source Material)")
        context_parts.append(target.extraction_content[:15000])  # Cap

    context = "\n".join(context_parts)

    missing_str = ", ".join(target.missing_sections)

    return f"""{context}

## TASK
Generate the following missing sections for {target.expert_name}'s genius.md:
Missing: {missing_str}

For each section, mine the existing genius patterns, hidden knowledge, and extraction report (if available) to produce:

### Hall of Fame Exemplars
- Extract or reconstruct 2-3 concrete examples demonstrating this expert's methodology at its best
- Include "What makes this excellent" for each
- Include 1 anti-exemplar showing mediocre work in this domain
- If no source examples exist, generate realistic exemplars from the methodology

### Signature Moves
- 3-5 behavioral moves (not concepts) — actions this expert takes reflexively
- Format: **[Move Name]**: [action description] → **Deploy when**: [trigger]

### Expert-Specific Quality Rubric
- 5-7 criteria specific to THIS expert's domain (not generic)
- Format as markdown table: Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant)

Generate all 3 sections now. Output ONLY the section content starting with ## headers.
"""


# --------------------------------------------------------------------------
# Enrichment Engine
# --------------------------------------------------------------------------

async def enrich_single(
    target: EnrichmentTarget,
    client: GeminiClient,
    dry_run: bool = False,
    no_clean: bool = False,
) -> EnrichmentResult:
    """Enrich a single genius.md file."""
    start = time.time()

    if not target.missing_sections:
        return EnrichmentResult(
            skill_name=target.skill_name, status="up-to-date",
            sections_added=0, tokens_used=0, estimated_cost=0,
            duration_seconds=0,
        )

    # Check token budget
    if client.total_tokens_used >= TOKEN_BUDGET:
        return EnrichmentResult(
            skill_name=target.skill_name, status="skipped",
            sections_added=0, tokens_used=0, estimated_cost=0,
            duration_seconds=0,
            error=f"Token budget exceeded ({client.total_tokens_used}/{TOKEN_BUDGET})",
        )

    print(f"  🚀 Enriching {target.skill_name} ({len(target.missing_sections)} sections)...")

    prompt = build_enrichment_prompt(target)

    try:
        text, meta = await client.generate(
            prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7,
            max_output_tokens=8192,
        )

        duration = time.time() - start

        if not text.strip():
            print(f"  ❌ {target.skill_name}: Empty response")
            return EnrichmentResult(
                skill_name=target.skill_name, status="failed",
                sections_added=0, tokens_used=meta.total_tokens,
                estimated_cost=meta.estimated_cost_usd,
                duration_seconds=duration, error="Empty response",
            )

        # Strip code fences if present
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        new_sections = "\n".join(lines).strip()

        if not dry_run:
            # Read current content
            current = target.genius_content

            # Clean template sections if requested
            if not no_clean and target.has_template_sections:
                current = clean_template_sections(current)
                print(f"    🧹 Cleaned template DF/AP/VD sections")

            # Append new sections
            enriched = current.rstrip() + "\n\n" + new_sections + "\n"

            # Write back
            target.genius_path.write_text(enriched)
            print(f"  ✅ {target.skill_name} enriched ({meta.total_tokens:,} tokens, ${meta.estimated_cost_usd:.4f})")
        else:
            print(f"  🔍 {target.skill_name} dry-run ({meta.total_tokens:,} tokens, ${meta.estimated_cost_usd:.4f})")
            print(f"    Preview ({len(new_sections)} chars):")
            for line in new_sections.splitlines()[:5]:
                print(f"      {line}")

        return EnrichmentResult(
            skill_name=target.skill_name, status="success",
            sections_added=len(target.missing_sections),
            tokens_used=meta.total_tokens,
            estimated_cost=meta.estimated_cost_usd,
            duration_seconds=duration, output=new_sections,
        )

    except Exception as e:
        duration = time.time() - start
        print(f"  ❌ {target.skill_name} failed: {e}")
        return EnrichmentResult(
            skill_name=target.skill_name, status="failed",
            sections_added=0, tokens_used=0, estimated_cost=0,
            duration_seconds=duration, error=str(e),
        )


async def run_enrichment(
    targets: List[EnrichmentTarget],
    dry_run: bool = False,
    no_clean: bool = False,
    max_parallel: int = 5,
) -> List[EnrichmentResult]:
    """Run enrichment on multiple targets in parallel."""
    client = GeminiClient()

    print(f"\n{'='*60}")
    print(f"  GENIUS ENRICHER — {len(targets)} targets")
    print(f"  Model: {client.default_model}")
    print(f"  Max parallel: {max_parallel}")
    print(f"{'='*60}\n")

    # Use semaphore for controlled parallelism
    semaphore = asyncio.Semaphore(max_parallel)
    results = []
    start = time.time()

    async def _enrich(target):
        async with semaphore:
            return await enrich_single(target, client, dry_run, no_clean)

    tasks = [_enrich(t) for t in targets]
    results = await asyncio.gather(*tasks)

    total_duration = time.time() - start
    usage = client.usage_summary()

    # Summary
    successful = [r for r in results if r.status == "success"]
    up_to_date = [r for r in results if r.status == "up-to-date"]
    failed = [r for r in results if r.status == "failed"]
    skipped = [r for r in results if r.status == "skipped"]

    print(f"\n{'='*60}")
    print(f"  GENIUS ENRICHER COMPLETE")
    print(f"{'='*60}")
    print(f"  ✅ Enriched: {len(successful)}")
    print(f"  ✓  Already up-to-date: {len(up_to_date)}")
    if failed:
        print(f"  ❌ Failed: {len(failed)}")
        for r in failed:
            print(f"     → {r.skill_name}: {r.error}")
    if skipped:
        print(f"  ⏭️  Skipped: {len(skipped)}")
    print(f"  📊 Total tokens: {usage['total_tokens']:,}")
    print(f"  💰 Estimated cost: ${usage['total_cost_usd']:.4f}")
    print(f"  ⏱️  Total time: {total_duration:.1f}s")
    print(f"{'='*60}\n")

    return results


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Genius Enricher — Retrofit genius.md files with savant-level context",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--skill", "-s",
                        help="Path to a single skill directory (relative or absolute)")
    parser.add_argument("--all", "-a", action="store_true",
                        help="Enrich all skills that have genius.md files")
    parser.add_argument("--plan-only", action="store_true",
                        help="Show enrichment plan without making API calls")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate enrichments but don't write files")
    parser.add_argument("--no-clean", action="store_true",
                        help="Skip cleaning auto-generated DF/AP/VD sections")
    parser.add_argument("--max-parallel", type=int, default=5,
                        help="Max parallel API calls (default: 5)")

    args = parser.parse_args()

    if not args.skill and not args.all:
        print("❌ Specify --skill <path> or --all")
        sys.exit(1)

    # Discover targets
    if args.skill:
        skill_path = BASE_PATH / args.skill if not Path(args.skill).is_absolute() else Path(args.skill)
        if not skill_path.exists():
            print(f"❌ Skill not found: {skill_path}")
            sys.exit(1)
        skill_dirs = [skill_path]
    else:
        skill_dirs = discover_genius_files()

    print(f"\n📂 Discovered {len(skill_dirs)} skill(s) with genius.md\n")

    # Assess each
    targets = []
    for d in skill_dirs:
        target = assess_genius_file(d)
        targets.append(target)

    # Filter to only those needing enrichment
    needs_enrichment = [t for t in targets if t.missing_sections]
    already_complete = [t for t in targets if not t.missing_sections]
    has_template = [t for t in targets if t.has_template_sections]

    print(f"📋 Assessment:")
    print(f"   Need enrichment: {len(needs_enrichment)}")
    print(f"   Already complete: {len(already_complete)}")
    print(f"   Have template DF/AP/VD sections: {len(has_template)}")

    if needs_enrichment:
        print(f"\n📋 Enrichment targets:")
        for t in needs_enrichment:
            missing_str = ", ".join(t.missing_sections)
            extraction = "✅ has extraction" if t.extraction_content else "⚠️  no extraction"
            template = " 🧹 has DF/AP/VD" if t.has_template_sections else ""
            print(f"   → {t.skill_name}: missing [{missing_str}] ({extraction}){template}")

    if args.plan_only:
        estimated_cost = len(needs_enrichment) * 0.004  # ~4k tokens per call at flash rates
        print(f"\n🔍 Plan-only mode — no API calls made.")
        print(f"   Estimated cost: ${estimated_cost:.3f}")
        return

    if not needs_enrichment:
        print(f"\n✅ All genius.md files are already enriched!")
        return

    results = asyncio.run(run_enrichment(
        needs_enrichment,
        dry_run=args.dry_run,
        no_clean=args.no_clean,
        max_parallel=args.max_parallel,
    ))

    if any(r.status == "failed" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
