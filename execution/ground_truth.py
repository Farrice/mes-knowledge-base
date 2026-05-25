#!/usr/bin/env python3
"""
Ground Truth — Expert benchmark calibration system for Antigravity.

The missing piece: comparing AI output against REAL expert output.
Without this, the quality gate is self-referential (AI grading AI).

What this does:
    1. Manages a library of real expert output samples per domain
    2. Runs blind comparison scoring (AI output vs expert output, unlabeled)
    3. Calculates the "expert gap" — how far AI output is from the real thing
    4. Feeds gap data into the feedback ratchet for targeted improvement

Directory structure:
    knowledge/expert-benchmarks/
        {domain}/
            samples.json          — metadata index for all samples
            sample-001.md         — actual expert output
            sample-002.md         — actual expert output
            ...

Usage:
    from execution.ground_truth import (
        add_sample, list_samples, blind_compare, gap_report
    )

CLI:
    python execution/ground_truth.py add <domain> <file_path> --expert <name> --source <url> --type <type>
    python execution/ground_truth.py list [domain]
    python execution/ground_truth.py compare <domain> <ai_output_path>
    python execution/ground_truth.py gap-report [domain]
    python execution/ground_truth.py domains
"""

import os
import json
import argparse
import hashlib
from datetime import date, datetime
from typing import Optional, Dict, List, Any
from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent.parent / 'knowledge' / 'expert-benchmarks'

# Domain definitions — maps to skills and experts
DOMAINS = {
    "copywriting": {
        "experts": ["luke-iha", "cardinal-mason", "stefan-georgi"],
        "skills": ["luke-iha-creative-strategy", "luke-iha-proof-mechanisms", "luke-iha-insight-vectors"],
        "output_types": ["sales-page", "vsl-lead", "ad-copy", "email-sequence", "hook"],
        "description": "Direct response copywriting, VSLs, ads, hooks"
    },
    "linkedin": {
        "experts": ["lara-acosta", "nicolas-cole"],
        "skills": ["lara-acosta-linkedin-ghostwriting", "nicolas-cole-ghostwriting"],
        "output_types": ["post", "headline", "about-section", "carousel", "newsletter"],
        "description": "LinkedIn content, ghostwriting, personal brand"
    },
    "brand-strategy": {
        "experts": ["oren-john", "grace-beverley", "david-placek"],
        "skills": ["storybrand", "oren-john-brand-strategy", "grace-beverley-brand"],
        "output_types": ["positioning", "brandscript", "naming", "identity"],
        "description": "Brand positioning, naming, identity, StoryBrand"
    },
    "seo": {
        "experts": ["nathan-gotch", "ethan-smith"],
        "skills": ["nathan-gotch-seo"],
        "output_types": ["meta-titles", "content-strategy", "technical-audit", "keyword-research"],
        "description": "SEO strategy, technical SEO, content optimization"
    },
    "screenwriting": {
        "experts": ["steven-pressfield", "michael-connelly"],
        "skills": ["pressfield-screenplay", "connelly-rewrite"],
        "output_types": ["pitch", "logline", "cold-open", "dialogue", "character-bible"],
        "description": "TV/film writing, pitch bibles, screenplays"
    },
    "sales-psychology": {
        "experts": ["dai-media", "kallaway"],
        "skills": ["consumer-posture-profile", "kallaway-content-psychology"],
        "output_types": ["icp-profile", "objection-handling", "awareness-ladder", "funnel-copy"],
        "description": "Consumer psychology, persuasion, sales frameworks"
    },
    "content-strategy": {
        "experts": ["kieran-flanagan", "nate-b-jones"],
        "skills": ["kieran-flanagan-content-engine", "nate-b-jones-orchestration"],
        "output_types": ["content-calendar", "distribution-strategy", "content-audit", "growth-plan"],
        "description": "Content strategy, distribution, growth"
    },
}


# Phase C (2026-05-25) — Runtime-registered verticals merged at module load.
# /verticalize and `ground_truth.py init-domain <slug>` write here. The
# hardcoded DOMAINS dict above stays the source of truth for the 7 seed
# domains; this file holds everything added at runtime.
_REGISTERED_DOMAINS_FILE = BENCHMARKS_DIR / '_registered_domains.json'


def _load_registered_domains() -> Dict[str, Any]:
    """Load runtime-registered domains (verticals bootstrapped via init-domain)."""
    if not _REGISTERED_DOMAINS_FILE.exists():
        return {}
    try:
        return json.loads(_REGISTERED_DOMAINS_FILE.read_text())
    except Exception:
        return {}


def _save_registered_domains(data: Dict[str, Any]) -> None:
    _REGISTERED_DOMAINS_FILE.parent.mkdir(parents=True, exist_ok=True)
    _REGISTERED_DOMAINS_FILE.write_text(json.dumps(data, indent=2))


# Merge runtime registry into the hardcoded DOMAINS at import time.
# Hardcoded entries win on collision (defensive — don't let runtime override seed).
_REGISTERED = _load_registered_domains()
for _k, _v in _REGISTERED.items():
    if _k not in DOMAINS:
        DOMAINS[_k] = _v


def init_domain(
    slug: str,
    description: str,
    experts: List[str],
    output_types: List[str],
    skills: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Register a new vertical domain for ground-truth calibration.

    Called by /verticalize Phase 4 to bootstrap calibration for a new
    domain (e.g., "real-estate-sfv", "ai-construction-consulting").

    Args:
        slug: Hyphenated slug, alphanumeric + hyphens only (no spaces/underscores)
        description: One-line description of the domain
        experts: List of expert agent identifiers (or [] if none known yet)
        output_types: Domain-native output categories (e.g., ["listing-post", "neighborhood-deep-dive"])
        skills: Optional pre-registered skill IDs (empty by default — verticalize fills this)

    Returns:
        The registered domain dict.
    """
    # Validate slug
    import re
    if not re.match(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", slug):
        raise ValueError(
            f"slug must be lowercase, alphanumeric + hyphens, no leading/trailing dash. Got: {slug!r}"
        )

    if slug in DOMAINS:
        raise ValueError(f"Domain {slug!r} is already registered.")

    if not description.strip():
        raise ValueError("description is required.")

    entry = {
        "experts": list(experts),
        "skills": list(skills or []),
        "output_types": list(output_types),
        "description": description.strip(),
        "registered_at": date.today().isoformat(),
        "registered_via": "init_domain",
    }

    # Write to the runtime registry
    registered = _load_registered_domains()
    registered[slug] = entry
    _save_registered_domains(registered)

    # Mutate in-process DOMAINS so subsequent calls in the same process work
    DOMAINS[slug] = entry

    # Create the benchmark dir + empty samples index
    _ensure_domain_dir(slug)

    return entry


def _ensure_domain_dir(domain: str) -> Path:
    """Create domain directory and samples.json if they don't exist."""
    domain_dir = BENCHMARKS_DIR / domain
    domain_dir.mkdir(parents=True, exist_ok=True)
    samples_file = domain_dir / 'samples.json'
    if not samples_file.exists():
        samples_file.write_text(json.dumps({"domain": domain, "samples": []}, indent=2))
    return domain_dir


def _load_samples(domain: str) -> Dict[str, Any]:
    """Load the samples index for a domain."""
    samples_file = BENCHMARKS_DIR / domain / 'samples.json'
    if not samples_file.exists():
        return {"domain": domain, "samples": []}
    return json.loads(samples_file.read_text())


def _save_samples(domain: str, data: Dict[str, Any]):
    """Save the samples index for a domain."""
    samples_file = BENCHMARKS_DIR / domain / 'samples.json'
    samples_file.write_text(json.dumps(data, indent=2))


def add_sample(
    domain: str,
    content: str,
    expert: str,
    source: str = "",
    output_type: str = "",
    notes: str = "",
    title: str = "",
) -> Dict[str, Any]:
    """
    Add a real expert output sample to the benchmark library.

    Args:
        domain: Domain category (copywriting, linkedin, etc.)
        content: The actual expert output text
        expert: Name of the expert who produced it
        source: URL or reference for where it came from
        output_type: Type of output (sales-page, post, pitch, etc.)
        notes: What makes this sample expert-level
        title: Optional title for the sample

    Returns:
        Dict with sample metadata and file path
    """
    if domain not in DOMAINS:
        raise ValueError(f"Unknown domain '{domain}'. Valid: {', '.join(DOMAINS.keys())}")

    domain_dir = _ensure_domain_dir(domain)
    data = _load_samples(domain)

    # Generate sample ID
    sample_num = len(data["samples"]) + 1
    sample_id = f"sample-{sample_num:03d}"
    sample_file = domain_dir / f"{sample_id}.md"

    # Write the sample content
    header = f"# Expert Benchmark: {expert}\n"
    header += f"> Source: {source}\n" if source else ""
    header += f"> Type: {output_type}\n" if output_type else ""
    header += f"> Added: {date.today().isoformat()}\n\n---\n\n"
    sample_file.write_text(header + content)

    # Update the index
    sample_meta = {
        "id": sample_id,
        "expert": expert,
        "source": source,
        "output_type": output_type,
        "title": title or f"{expert} {output_type}",
        "notes": notes,
        "added": date.today().isoformat(),
        "file": sample_file.name,
        "word_count": len(content.split()),
        "content_hash": hashlib.md5(content.encode()).hexdigest()[:8],
    }
    data["samples"].append(sample_meta)
    _save_samples(domain, data)

    print(f"  Added {sample_id} to {domain}/")
    print(f"  Expert: {expert}")
    print(f"  Words: {sample_meta['word_count']}")
    print(f"  File: {sample_file}")
    return sample_meta


def list_samples(domain: str = "") -> List[Dict[str, Any]]:
    """List all samples, optionally filtered by domain."""
    all_samples = []

    domains_to_check = [domain] if domain else list(DOMAINS.keys())

    for d in domains_to_check:
        data = _load_samples(d)
        for sample in data.get("samples", []):
            sample["domain"] = d
            all_samples.append(sample)

    return all_samples


def blind_compare(domain: str, ai_output_path: str) -> Dict[str, Any]:
    """
    Run a blind comparison between AI output and expert samples.

    Produces a comparison report with both outputs unlabeled (Output A / Output B)
    so the scorer can't be biased by knowing which is AI vs expert.

    Args:
        domain: The domain to compare against
        ai_output_path: Path to the AI-generated output file

    Returns:
        Dict with comparison data ready for manual scoring
    """
    import random

    ai_output = Path(ai_output_path).read_text()
    data = _load_samples(domain)

    if not data["samples"]:
        return {"error": f"No expert samples in domain '{domain}'. Add samples first."}

    # Pick a random expert sample of similar type
    sample = random.choice(data["samples"])
    expert_file = BENCHMARKS_DIR / domain / sample["file"]
    expert_output = expert_file.read_text()

    # Strip the header from expert output (everything before ---)
    if "---\n\n" in expert_output:
        expert_output = expert_output.split("---\n\n", 1)[1]

    # Randomize order so scorer can't guess
    if random.random() > 0.5:
        output_a, output_b = ai_output, expert_output
        key = {"A": "ai", "B": "expert"}
    else:
        output_a, output_b = expert_output, ai_output
        key = {"A": "expert", "B": "ai"}

    comparison = {
        "domain": domain,
        "expert_sample": sample["id"],
        "expert_name": sample["expert"],
        "timestamp": datetime.now().isoformat(),
        "key": key,  # Reveal after scoring
        "instructions": (
            "Score each output 1-10 on: (1) Craft Quality, (2) Persuasion Power, "
            "(3) Voice Authenticity, (4) Would-Buy/Would-Hire Factor. "
            "Do NOT try to guess which is AI. Score on quality alone."
        ),
    }

    # Write comparison file for manual review
    comp_dir = BENCHMARKS_DIR / "_comparisons"
    comp_dir.mkdir(exist_ok=True)
    comp_file = comp_dir / f"compare-{domain}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

    comp_content = f"""# Blind Comparison — {domain.title()}

> **Instructions**: Score each output 1-10 on the dimensions below.
> Do NOT try to guess which is AI. Score on quality alone.
> After scoring, run `python execution/ground_truth.py reveal {comp_file.name}` to see the key.

## Scoring Dimensions
1. **Craft Quality** (1-10): Writing quality, structure, flow
2. **Persuasion Power** (1-10): Does it move the reader to action?
3. **Voice Authenticity** (1-10): Does it sound like a real expert, not a template?
4. **Would-Buy Factor** (1-10): If you were the target audience, would you act?

---

## OUTPUT A

{output_a}

---

## OUTPUT B

{output_b}

---

## Your Scores

| Dimension | Output A | Output B |
|-----------|----------|----------|
| Craft Quality | /10 | /10 |
| Persuasion Power | /10 | /10 |
| Voice Authenticity | /10 | /10 |
| Would-Buy Factor | /10 | /10 |
| **TOTAL** | /40 | /40 |

## Notes
[What made one better than the other?]
"""
    comp_file.write_text(comp_content)

    # Save key separately (don't peek until scored!)
    key_file = comp_dir / f".key-{comp_file.stem}.json"
    key_file.write_text(json.dumps(comparison, indent=2))

    print(f"\n{'='*60}")
    print(f"  BLIND COMPARISON READY — {domain.title()}")
    print(f"{'='*60}")
    print(f"  File: {comp_file}")
    print(f"  Expert sample: {sample['id']} by {sample['expert']}")
    print(f"  Instructions: Score both outputs without knowing which is AI")
    print(f"  Reveal key: python execution/ground_truth.py reveal {comp_file.name}")
    print(f"{'='*60}\n")

    return comparison


def gap_report(domain: str = "") -> Dict[str, Any]:
    """
    Generate a gap report showing expert benchmark coverage.

    Returns:
        Dict with coverage stats per domain
    """
    report = {"generated": date.today().isoformat(), "domains": {}}

    for d, config in DOMAINS.items():
        if domain and d != domain:
            continue

        data = _load_samples(d)
        samples = data.get("samples", [])

        # Coverage analysis
        experts_covered = set(s["expert"] for s in samples)
        types_covered = set(s["output_type"] for s in samples if s.get("output_type"))

        report["domains"][d] = {
            "description": config["description"],
            "total_samples": len(samples),
            "experts_known": config["experts"],
            "experts_with_samples": list(experts_covered),
            "experts_missing": [e for e in config["experts"] if e not in experts_covered],
            "output_types_covered": list(types_covered),
            "output_types_missing": [t for t in config["output_types"] if t not in types_covered],
            "coverage_pct": round(len(experts_covered) / len(config["experts"]) * 100) if config["experts"] else 0,
            "ready_for_blind_test": len(samples) >= 3,
        }

    # Print report
    print(f"\n{'='*60}")
    print(f"  GROUND TRUTH GAP REPORT")
    print(f"  Generated: {report['generated']}")
    print(f"{'='*60}\n")

    total_samples = 0
    total_gaps = 0

    for d, stats in report["domains"].items():
        status = "READY" if stats["ready_for_blind_test"] else "NEEDS SAMPLES"
        print(f"  {d.upper()} [{status}]")
        print(f"    Samples: {stats['total_samples']}")
        print(f"    Coverage: {stats['coverage_pct']}% ({len(stats['experts_with_samples'])}/{len(stats['experts_known'])} experts)")
        if stats["experts_missing"]:
            print(f"    Missing experts: {', '.join(stats['experts_missing'])}")
        if stats["output_types_missing"]:
            print(f"    Missing types: {', '.join(stats['output_types_missing'])}")
        print()
        total_samples += stats["total_samples"]
        total_gaps += len(stats["experts_missing"])

    print(f"  TOTAL: {total_samples} samples across {len(report['domains'])} domains")
    print(f"  GAPS: {total_gaps} experts without benchmark samples")
    print(f"{'='*60}\n")

    return report


def reveal_comparison(comp_filename: str):
    """Reveal the key for a blind comparison after scoring."""
    comp_dir = BENCHMARKS_DIR / "_comparisons"
    key_file = comp_dir / f".key-{Path(comp_filename).stem}.json"

    if not key_file.exists():
        print(f"  No key found for {comp_filename}")
        return

    data = json.loads(key_file.read_text())
    key = data["key"]

    print(f"\n{'='*60}")
    print(f"  COMPARISON KEY REVEALED")
    print(f"{'='*60}")
    print(f"  Output A = {key['A'].upper()}")
    print(f"  Output B = {key['B'].upper()}")
    print(f"  Expert: {data['expert_name']} (sample {data['expert_sample']})")
    print(f"{'='*60}\n")
    print("  If the expert scored higher → your AI has a real gap to close.")
    print("  If the AI scored higher → your skill is calibrated well for this domain.")
    print("  If they're close → you're in the range. Focus on voice authenticity.\n")


def list_domains():
    """Print all registered domains and their experts."""
    print(f"\n{'='*60}")
    print(f"  GROUND TRUTH DOMAINS")
    print(f"{'='*60}\n")

    for d, config in DOMAINS.items():
        data = _load_samples(d)
        count = len(data.get("samples", []))
        print(f"  {d}")
        print(f"    {config['description']}")
        print(f"    Experts: {', '.join(config['experts'])}")
        print(f"    Output types: {', '.join(config['output_types'])}")
        print(f"    Samples: {count}")
        print()


# ── CLI ─────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Ground Truth — Expert benchmark calibration")
    sub = parser.add_subparsers(dest="command")

    # add
    add_cmd = sub.add_parser("add", help="Add an expert sample")
    add_cmd.add_argument("domain", help="Domain (copywriting, linkedin, etc.)")
    add_cmd.add_argument("file_path", help="Path to the expert output file")
    add_cmd.add_argument("--expert", required=True, help="Expert name")
    add_cmd.add_argument("--source", default="", help="Source URL")
    add_cmd.add_argument("--type", default="", help="Output type")
    add_cmd.add_argument("--notes", default="", help="What makes this expert-level")
    add_cmd.add_argument("--title", default="", help="Sample title")

    # list
    list_cmd = sub.add_parser("list", help="List samples")
    list_cmd.add_argument("domain", nargs="?", default="", help="Filter by domain")

    # compare
    comp_cmd = sub.add_parser("compare", help="Run blind comparison")
    comp_cmd.add_argument("domain", help="Domain to compare against")
    comp_cmd.add_argument("ai_output", help="Path to AI output file")

    # gap-report
    gap_cmd = sub.add_parser("gap-report", help="Show coverage gaps")
    gap_cmd.add_argument("domain", nargs="?", default="", help="Filter by domain")

    # reveal
    rev_cmd = sub.add_parser("reveal", help="Reveal blind comparison key")
    rev_cmd.add_argument("filename", help="Comparison filename")

    # domains
    sub.add_parser("domains", help="List all domains")

    # init-domain (Phase C — vertical bootstrap)
    init_cmd = sub.add_parser(
        "init-domain",
        help="Register a new vertical for ground-truth calibration (used by /verticalize)",
    )
    init_cmd.add_argument("slug", help="Domain slug (lowercase, hyphens, e.g. real-estate-sfv)")
    init_cmd.add_argument("--description", required=True, help="One-line domain description")
    init_cmd.add_argument(
        "--expert", action="append", default=[],
        help="Expert identifier (repeatable; pass --expert N times)",
    )
    init_cmd.add_argument(
        "--output-type", action="append", default=[], dest="output_types",
        help="Output type (repeatable; e.g. listing-post, neighborhood-deep-dive)",
    )
    init_cmd.add_argument(
        "--skill", action="append", default=[], dest="skills",
        help="Optional skill ID (repeatable)",
    )

    args = parser.parse_args()

    if args.command == "add":
        content = Path(args.file_path).read_text()
        add_sample(args.domain, content, args.expert, args.source, args.type, args.notes, args.title)
    elif args.command == "list":
        samples = list_samples(args.domain)
        for s in samples:
            print(f"  [{s.get('domain', '?')}] {s['id']} — {s['expert']} ({s.get('output_type', '?')}) — {s['word_count']} words")
    elif args.command == "compare":
        blind_compare(args.domain, args.ai_output)
    elif args.command == "gap-report":
        gap_report(args.domain)
    elif args.command == "reveal":
        reveal_comparison(args.filename)
    elif args.command == "domains":
        list_domains()
    elif args.command == "init-domain":
        try:
            entry = init_domain(
                slug=args.slug,
                description=args.description,
                experts=args.expert,
                output_types=args.output_types,
                skills=args.skills,
            )
        except ValueError as e:
            import sys
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(2)
        print(f"Registered new domain: {args.slug}")
        print(f"  Description:  {entry['description']}")
        print(f"  Experts:      {', '.join(entry['experts']) or '(none yet)'}")
        print(f"  Output types: {', '.join(entry['output_types']) or '(none yet)'}")
        print(f"  Benchmark dir: knowledge/expert-benchmarks/{args.slug}/")
        print(f"  Next step: add 5 PASS-marked sample outputs via `ground_truth.py add {args.slug} ...`")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
