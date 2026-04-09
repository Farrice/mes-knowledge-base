#!/usr/bin/env python3
"""
Knowledge Compiler — Self-healing knowledge base for Antigravity.

Inspired by Karpathy's LLM Knowledge Base architecture:
    Raw data → Compiler (organize + interlink) → Validator → Briefings

What this does:
    1. Inventories all knowledge sources (knowledge/, extractions/, research_outputs/)
    2. Generates a structured manifest with metadata (domain, expert, word count, age)
    3. Detects stale content (not referenced in recent work)
    4. Flags overlapping topics for deduplication/consolidation
    5. Generates a session briefing (knowledge/briefing.md) — recent learnings, key entities
    6. Produces compilation reports for the agent to act on

The agent (Claude) IS the compiler — this script provides the scaffolding.
The agent reads the manifest and briefing, then actively maintains the wiki.

Directory structure after compilation:
    knowledge/
        compiled/
            manifest.json       — full inventory of all knowledge sources
            briefing.md         — session start briefing (recent learnings, entities)
            stale-report.md     — files not referenced in 30+ days
            overlap-report.md   — files covering similar topics

Usage:
    python execution/knowledge_compiler.py inventory          # Generate manifest
    python execution/knowledge_compiler.py briefing           # Generate session briefing
    python execution/knowledge_compiler.py stale              # Find stale content
    python execution/knowledge_compiler.py overlap            # Find overlapping content
    python execution/knowledge_compiler.py full               # Run all stages
    python execution/knowledge_compiler.py stats              # Quick stats overview
"""

import os
import json
import argparse
import hashlib
from datetime import date, datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent

KNOWLEDGE_DIRS = [
    PROJECT_ROOT / 'knowledge',
    PROJECT_ROOT / 'extractions',
    PROJECT_ROOT / 'research_outputs',
]

COMPILED_DIR = PROJECT_ROOT / 'knowledge' / 'compiled'

# Domain keywords for auto-classification
DOMAIN_MAP = {
    'copywriting': ['copy', 'sales', 'vsl', 'headline', 'hook', 'proof', 'cta', 'direct-response', 'email-sequence'],
    'content': ['content', 'viral', 'social', 'tiktok', 'youtube', 'linkedin', 'newsletter', 'substack'],
    'strategy': ['strategy', 'positioning', 'market', 'competitive', 'business', 'go-to-market'],
    'brand': ['brand', 'identity', 'storybrand', 'voice', 'personal-brand', 'naming'],
    'seo': ['seo', 'keyword', 'search', 'ranking', 'backlink', 'serp'],
    'sales': ['sales', 'objection', 'closing', 'persuasion', 'funnel', 'conversion'],
    'screenwriting': ['screenplay', 'script', 'dialogue', 'character', 'narrative', 'story'],
    'research': ['research', 'analysis', 'consumer', 'persona', 'behavioral', 'psychology'],
    'systems': ['automation', 'agent', 'workflow', 'orchestration', 'pipeline', 'ai-brain'],
}

# Expert name patterns for auto-attribution
EXPERT_PATTERNS = {
    'luke-iha': ['luke', 'iha', 'proof-mechanism', 'insight-vector'],
    'lara-acosta': ['lara', 'acosta', 'linkedin-ghostwriting'],
    'nicolas-cole': ['cole', 'ghostwriting', 'ship-30'],
    'cardinal-mason': ['cardinal', 'mason'],
    'nathan-gotch': ['gotch', 'seo'],
    'kallaway': ['kallaway', 'content-psychology'],
    'dai-media': ['dai', 'consumer-posture'],
    'nick-saraev': ['saraev', 'agentic'],
    'oren-john': ['oren', 'brand-strategy'],
    'pressfield': ['pressfield', 'war-of-art', 'resistance'],
    'connelly': ['connelly', 'rewrite', 'dialogue'],
    'stefan-georgi': ['georgi', 'vsl'],
    'grace-beverley': ['grace', 'beverley'],
    'jason-fladlien': ['fladlien', 'webinar'],
    'april-dunford': ['dunford', 'positioning'],
    'kieran-flanagan': ['flanagan', 'content-engine'],
}


def _classify_domain(filepath: Path, content: str) -> str:
    """Auto-classify a file into a domain based on path and content."""
    search_text = (filepath.stem + ' ' + filepath.parent.name + ' ' + content[:500]).lower()
    scores = {}
    for domain, keywords in DOMAIN_MAP.items():
        score = sum(1 for kw in keywords if kw in search_text)
        if score > 0:
            scores[domain] = score
    return max(scores, key=scores.get) if scores else 'general'


def _detect_expert(filepath: Path, content: str) -> Optional[str]:
    """Detect which expert a file is associated with."""
    search_text = (filepath.stem + ' ' + str(filepath.parent) + ' ' + content[:500]).lower()
    for expert, patterns in EXPERT_PATTERNS.items():
        if any(p in search_text for p in patterns):
            return expert
    return None


def _file_metadata(filepath: Path) -> Dict[str, Any]:
    """Extract metadata from a single file."""
    try:
        content = filepath.read_text(errors='ignore')
    except Exception:
        return None

    word_count = len(content.split())
    stat = filepath.stat()
    modified = datetime.fromtimestamp(stat.st_mtime)
    age_days = (datetime.now() - modified).days

    return {
        'path': str(filepath.relative_to(PROJECT_ROOT)),
        'name': filepath.stem,
        'parent': filepath.parent.name,
        'domain': _classify_domain(filepath, content),
        'expert': _detect_expert(filepath, content),
        'word_count': word_count,
        'modified': modified.isoformat(),
        'age_days': age_days,
        'size_bytes': stat.st_size,
        'content_hash': hashlib.md5(content[:1000].encode()).hexdigest()[:8],
        'has_frontmatter': content.startswith('---'),
    }


def generate_inventory() -> Dict[str, Any]:
    """
    Generate a full inventory of all knowledge sources.

    Returns manifest with per-file metadata and aggregate stats.
    """
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)

    files = []
    for knowledge_dir in KNOWLEDGE_DIRS:
        if not knowledge_dir.exists():
            continue
        for md_file in sorted(knowledge_dir.rglob('*.md')):
            # Skip compiled output and hidden files
            if 'compiled' in str(md_file) or md_file.name.startswith('.'):
                continue
            meta = _file_metadata(md_file)
            if meta and meta['word_count'] > 10:  # Skip near-empty files
                files.append(meta)

    # Aggregate stats
    domain_counts = defaultdict(int)
    expert_counts = defaultdict(int)
    total_words = 0
    stale_count = 0

    for f in files:
        domain_counts[f['domain']] += 1
        if f['expert']:
            expert_counts[f['expert']] += 1
        total_words += f['word_count']
        if f['age_days'] > 30:
            stale_count += 1

    manifest = {
        'generated': datetime.now().isoformat(),
        'total_files': len(files),
        'total_words': total_words,
        'total_tokens_est': int(total_words * 1.33),  # ~1.33 tokens per word
        'stale_files_30d': stale_count,
        'domains': dict(sorted(domain_counts.items(), key=lambda x: -x[1])),
        'experts': dict(sorted(expert_counts.items(), key=lambda x: -x[1])),
        'files': files,
    }

    # Write manifest
    manifest_path = COMPILED_DIR / 'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2))

    print(f"\n{'='*60}")
    print(f"  KNOWLEDGE INVENTORY")
    print(f"  Generated: {manifest['generated'][:10]}")
    print(f"{'='*60}")
    print(f"  Total files: {manifest['total_files']}")
    print(f"  Total words: {manifest['total_words']:,}")
    print(f"  Est. tokens: {manifest['total_tokens_est']:,}")
    print(f"  Stale (>30d): {manifest['stale_files_30d']}")
    print()
    print("  DOMAINS:")
    for d, c in manifest['domains'].items():
        print(f"    {d}: {c} files")
    print()
    print("  EXPERTS:")
    for e, c in list(manifest['experts'].items())[:10]:
        print(f"    {e}: {c} files")
    if len(manifest['experts']) > 10:
        print(f"    ... and {len(manifest['experts']) - 10} more")
    print(f"{'='*60}\n")

    return manifest


def generate_briefing(manifest: Dict[str, Any] = None) -> str:
    """
    Generate a session-start briefing from the knowledge base.

    This is the Karpathy compound loop: agents read the briefing
    at session start so they don't "wake up blank."
    """
    if manifest is None:
        manifest_path = COMPILED_DIR / 'manifest.json'
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        else:
            manifest = generate_inventory()

    # Find recently modified files (last 7 days)
    recent_files = [f for f in manifest['files'] if f['age_days'] <= 7]
    recent_files.sort(key=lambda x: x['age_days'])

    # Find high-value files (largest, most likely to contain deep knowledge)
    top_files = sorted(manifest['files'], key=lambda x: -x['word_count'])[:20]

    # Build briefing
    lines = [
        "# Knowledge Briefing",
        f"*Generated: {date.today().isoformat()} | {manifest['total_files']} sources | {manifest['total_words']:,} words*",
        "",
        "---",
        "",
        "## Recent Activity (Last 7 Days)",
        "",
    ]

    if recent_files:
        for f in recent_files[:10]:
            expert_tag = f" [{f['expert']}]" if f['expert'] else ""
            lines.append(f"- **{f['name']}** ({f['domain']}{expert_tag}) — {f['word_count']:,} words — `{f['path']}`")
    else:
        lines.append("*No files modified in the last 7 days.*")

    lines.extend([
        "",
        "## Domain Coverage",
        "",
        "| Domain | Files | Top Expert |",
        "|--------|-------|------------|",
    ])

    # Domain coverage with top expert per domain
    domain_experts = defaultdict(lambda: defaultdict(int))
    for f in manifest['files']:
        if f['expert']:
            domain_experts[f['domain']][f['expert']] += 1

    for domain, count in manifest['domains'].items():
        experts = domain_experts.get(domain, {})
        top_expert = max(experts, key=experts.get) if experts else "—"
        lines.append(f"| {domain} | {count} | {top_expert} |")

    lines.extend([
        "",
        "## Deepest Knowledge Sources (by word count)",
        "",
    ])

    for f in top_files[:10]:
        expert_tag = f" [{f['expert']}]" if f['expert'] else ""
        lines.append(f"1. **{f['name']}** ({f['domain']}{expert_tag}) — {f['word_count']:,} words — `{f['path']}`")

    lines.extend([
        "",
        "## Knowledge Gaps",
        "",
        "Domains with < 3 files (may need enrichment):",
        "",
    ])

    thin_domains = [(d, c) for d, c in manifest['domains'].items() if c < 3]
    if thin_domains:
        for d, c in thin_domains:
            lines.append(f"- **{d}**: {c} file{'s' if c != 1 else ''}")
    else:
        lines.append("*All domains have 3+ files.*")

    lines.extend([
        "",
        "---",
        "",
        "*This briefing is auto-generated by `execution/knowledge_compiler.py`. Run `python execution/knowledge_compiler.py briefing` to refresh.*",
    ])

    briefing_content = "\n".join(lines)
    briefing_path = COMPILED_DIR / 'briefing.md'
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    briefing_path.write_text(briefing_content)

    print(f"  Briefing written to: {briefing_path}")
    print(f"  Recent files: {len(recent_files)}")
    print(f"  Total sources: {manifest['total_files']}")
    return briefing_content


def find_stale_content(manifest: Dict[str, Any] = None, threshold_days: int = 30) -> List[Dict]:
    """Find files not modified in threshold_days."""
    if manifest is None:
        manifest_path = COMPILED_DIR / 'manifest.json'
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        else:
            manifest = generate_inventory()

    stale = [f for f in manifest['files'] if f['age_days'] > threshold_days]
    stale.sort(key=lambda x: -x['age_days'])

    # Write stale report
    lines = [
        "# Stale Content Report",
        f"*Generated: {date.today().isoformat()} | Threshold: {threshold_days} days*",
        "",
        f"**{len(stale)} files** not modified in {threshold_days}+ days.",
        "",
        "| Age (days) | Domain | Expert | File | Words |",
        "|-----------|--------|--------|------|-------|",
    ]

    for f in stale[:50]:
        expert = f['expert'] or '—'
        lines.append(f"| {f['age_days']} | {f['domain']} | {expert} | `{f['path']}` | {f['word_count']:,} |")

    if len(stale) > 50:
        lines.append(f"\n*... and {len(stale) - 50} more.*")

    lines.extend([
        "",
        "## Recommended Actions",
        "",
        "- **Review**: Check if stale files contain outdated information",
        "- **Consolidate**: Merge overlapping stale files into updated summaries",
        "- **Archive**: Move truly obsolete content to `knowledge/archive/`",
        "- **Refresh**: Update key files with recent learnings from extractions",
    ])

    report_content = "\n".join(lines)
    report_path = COMPILED_DIR / 'stale-report.md'
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content)

    print(f"\n  Stale content report: {report_path}")
    print(f"  Files > {threshold_days} days old: {len(stale)}")
    return stale


def find_overlaps(manifest: Dict[str, Any] = None) -> List[Dict]:
    """Find files covering similar topics that might need consolidation."""
    if manifest is None:
        manifest_path = COMPILED_DIR / 'manifest.json'
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        else:
            manifest = generate_inventory()

    # Group by domain + expert
    groups = defaultdict(list)
    for f in manifest['files']:
        key = f"{f['domain']}:{f['expert'] or 'no-expert'}"
        groups[key].append(f)

    overlaps = []
    for key, files in groups.items():
        if len(files) > 1:
            # Check for name similarity within the group
            names = [f['name'].lower() for f in files]
            for i, f1 in enumerate(files):
                for f2 in files[i+1:]:
                    # Simple overlap detection: shared words in filename
                    words1 = set(f1['name'].lower().replace('-', ' ').replace('_', ' ').split())
                    words2 = set(f2['name'].lower().replace('-', ' ').replace('_', ' ').split())
                    shared = words1 & words2 - {'the', 'a', 'an', 'and', 'or', 'of', 'in', 'to', 'for'}
                    if len(shared) >= 2:
                        overlaps.append({
                            'file_a': f1['path'],
                            'file_b': f2['path'],
                            'shared_words': list(shared),
                            'domain': f1['domain'],
                            'expert': f1['expert'],
                        })

    # Write overlap report
    lines = [
        "# Overlap Report",
        f"*Generated: {date.today().isoformat()}*",
        "",
        f"**{len(overlaps)} potential overlaps** detected.",
        "",
        "These file pairs share domain, expert, and significant naming overlap. Consider consolidating.",
        "",
    ]

    for i, overlap in enumerate(overlaps[:30], 1):
        lines.extend([
            f"### Overlap {i}",
            f"- **A**: `{overlap['file_a']}`",
            f"- **B**: `{overlap['file_b']}`",
            f"- **Shared**: {', '.join(overlap['shared_words'])}",
            f"- **Domain**: {overlap['domain']}",
            "",
        ])

    report_content = "\n".join(lines)
    report_path = COMPILED_DIR / 'overlap-report.md'
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content)

    print(f"\n  Overlap report: {report_path}")
    print(f"  Potential overlaps: {len(overlaps)}")
    return overlaps


def quick_stats():
    """Print quick stats without generating full manifest."""
    total_files = 0
    total_words = 0
    dir_counts = {}

    for knowledge_dir in KNOWLEDGE_DIRS:
        if not knowledge_dir.exists():
            continue
        count = 0
        for md_file in knowledge_dir.rglob('*.md'):
            if 'compiled' in str(md_file) or md_file.name.startswith('.'):
                continue
            try:
                content = md_file.read_text(errors='ignore')
                wc = len(content.split())
                if wc > 10:
                    total_files += 1
                    total_words += wc
                    count += 1
            except Exception:
                pass
        dir_counts[knowledge_dir.name] = count

    print(f"\n{'='*60}")
    print(f"  KNOWLEDGE BASE STATS")
    print(f"{'='*60}")
    print(f"  Total files: {total_files}")
    print(f"  Total words: {total_words:,}")
    print(f"  Est. tokens: {int(total_words * 1.33):,}")
    for d, c in dir_counts.items():
        print(f"    {d}/: {c} files")
    print(f"{'='*60}\n")


def full_compilation():
    """Run all compilation stages."""
    print("\n  Stage 1: Inventory...")
    manifest = generate_inventory()

    print("\n  Stage 2: Briefing...")
    generate_briefing(manifest)

    print("\n  Stage 3: Stale content detection...")
    stale = find_stale_content(manifest)

    print("\n  Stage 4: Overlap detection...")
    overlaps = find_overlaps(manifest)

    print(f"\n{'='*60}")
    print(f"  FULL COMPILATION COMPLETE")
    print(f"{'='*60}")
    print(f"  Manifest: knowledge/compiled/manifest.json")
    print(f"  Briefing: knowledge/compiled/briefing.md")
    print(f"  Stale report: knowledge/compiled/stale-report.md")
    print(f"  Overlap report: knowledge/compiled/overlap-report.md")
    print(f"{'='*60}\n")


# ── CLI ─────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Knowledge Compiler — Self-healing knowledge base")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("inventory", help="Generate full knowledge inventory")
    sub.add_parser("briefing", help="Generate session-start briefing")

    stale_cmd = sub.add_parser("stale", help="Find stale content")
    stale_cmd.add_argument("--days", type=int, default=30, help="Staleness threshold (default: 30)")

    sub.add_parser("overlap", help="Find overlapping content")
    sub.add_parser("full", help="Run all compilation stages")
    sub.add_parser("stats", help="Quick stats overview")

    args = parser.parse_args()

    if args.command == "inventory":
        generate_inventory()
    elif args.command == "briefing":
        generate_briefing()
    elif args.command == "stale":
        find_stale_content(threshold_days=args.days)
    elif args.command == "overlap":
        find_overlaps()
    elif args.command == "full":
        full_compilation()
    elif args.command == "stats":
        quick_stats()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
