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
import re
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
SOLUTIONS_DIR = PROJECT_ROOT / 'docs' / 'solutions'

SOLUTION_STOPWORDS = {
    'about', 'above', 'after', 'again', 'against', 'also', 'and', 'any',
    'are', 'because', 'before', 'being', 'between', 'but', 'can', 'codex',
    'for', 'from', 'has', 'have', 'into', 'its', 'mission', 'not', 'that',
    'the', 'their', 'then', 'there', 'this', 'use', 'when', 'with', 'without',
    'work', 'works', 'would', 'your',
}

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


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9][a-z0-9\-]{2,}", text.lower())
        if token not in SOLUTION_STOPWORDS
    }


def _first_heading(content: str, fallback: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback.replace("-", " ").replace("_", " ").title()


def _first_body_snippet(content: str, limit: int = 220) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    in_code = False

    for raw_line in content.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.startswith("#") or line.startswith("-") or line.startswith("|"):
            continue
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line)

    if current:
        paragraphs.append(" ".join(current))

    snippet = paragraphs[0] if paragraphs else ""
    if len(snippet) > limit:
        snippet = snippet[: limit - 1].rstrip() + "..."
    return snippet


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

    # Auto-update living index when inventory regenerates
    update_index(manifest)

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


def full_lint(manifest: Dict[str, Any] = None) -> Dict[str, List]:
    """
    Full wiki health check — Karpathy lint operation.

    Detects: contradictions, orphaned files, dead internal links,
    missing cross-references, stale claims, and structural issues.
    Generates severity-tiered report at knowledge/compiled/lint-report.md.
    """
    import re

    if manifest is None:
        manifest_path = COMPILED_DIR / 'manifest.json'
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        else:
            manifest = generate_inventory()

    issues = {
        'error': [],      # Must fix — broken references, data integrity
        'warning': [],    # Should fix — orphans, potential contradictions
        'info': [],       # Consider — stale content, optimization opportunities
    }

    all_paths = {f['path'] for f in manifest['files']}
    all_abs_paths = {str(PROJECT_ROOT / f['path']) for f in manifest['files']}

    # ── Check 1: Dead internal links ──────────────────────────────
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for f in manifest['files']:
        try:
            filepath = PROJECT_ROOT / f['path']
            content = filepath.read_text(errors='ignore')
            for match in link_pattern.finditer(content):
                link_text, link_target = match.groups()
                # Skip external URLs and anchors
                if link_target.startswith(('http', '#', 'mailto')):
                    continue
                # Resolve relative to file's directory
                target_path = (filepath.parent / link_target).resolve()
                if not target_path.exists():
                    issues['error'].append({
                        'type': 'dead_link',
                        'file': f['path'],
                        'detail': f'Link [{link_text}]({link_target}) points to nonexistent file',
                    })
        except Exception:
            pass

    # ── Check 2: Orphaned files (not referenced by anything) ─────
    # Build reference map: which files reference which other files
    referenced_files = set()
    for f in manifest['files']:
        try:
            filepath = PROJECT_ROOT / f['path']
            content = filepath.read_text(errors='ignore')
            for match in link_pattern.finditer(content):
                link_target = match.group(2)
                if not link_target.startswith(('http', '#', 'mailto')):
                    target_path = (filepath.parent / link_target).resolve()
                    rel_path = str(target_path.relative_to(PROJECT_ROOT))
                    referenced_files.add(rel_path)
        except Exception:
            pass

    # Also check references from skills, directives, and CLAUDE.md
    for ref_dir in [PROJECT_ROOT / 'skills', PROJECT_ROOT / 'directives',
                    PROJECT_ROOT / '.agent']:
        if ref_dir.exists():
            for md_file in ref_dir.rglob('*.md'):
                try:
                    content = md_file.read_text(errors='ignore')
                    for match in link_pattern.finditer(content):
                        link_target = match.group(2)
                        if not link_target.startswith(('http', '#', 'mailto')):
                            target_path = (md_file.parent / link_target).resolve()
                            try:
                                rel_path = str(target_path.relative_to(PROJECT_ROOT))
                                referenced_files.add(rel_path)
                            except ValueError:
                                pass
                except Exception:
                    pass

    # Check CLAUDE.md references
    claude_md = PROJECT_ROOT / 'CLAUDE.md'
    if claude_md.exists():
        try:
            content = claude_md.read_text(errors='ignore')
            # Match backtick-quoted paths too
            path_pattern = re.compile(r'`([a-zA-Z_./\-]+\.(?:md|py|json))`')
            for match in path_pattern.finditer(content):
                referenced_files.add(match.group(1))
        except Exception:
            pass

    for f in manifest['files']:
        # Skip compiled outputs, index, and log from orphan check
        if any(skip in f['path'] for skip in ['compiled/', 'index.md', 'log.md', 'synthesis/']):
            continue
        if f['path'] not in referenced_files and f['age_days'] > 30:
            issues['warning'].append({
                'type': 'orphan',
                'file': f['path'],
                'detail': f"Not referenced by any other file ({f['age_days']} days old, {f['word_count']:,} words)",
            })

    # ── Check 3: Domain contradictions (same domain, conflicting names) ──
    # Group by domain, look for files that might contain conflicting advice
    by_domain = defaultdict(list)
    for f in manifest['files']:
        by_domain[f['domain']].append(f)

    contradiction_keywords = {
        'never', 'always', 'don\'t', 'must', 'avoid', 'instead',
        'wrong', 'mistake', 'better', 'worse', 'best', 'worst',
    }
    for domain, files in by_domain.items():
        if len(files) < 2:
            continue
        # Sample strong-opinion sentences from each file
        opinions = {}
        for f in files[:30]:  # Cap per domain to avoid perf issues
            try:
                content = (PROJECT_ROOT / f['path']).read_text(errors='ignore')
                sentences = [s.strip() for s in content.split('.') if
                             any(kw in s.lower() for kw in contradiction_keywords)
                             and 20 < len(s) < 200]
                if sentences:
                    opinions[f['path']] = sentences[:5]
            except Exception:
                pass

        # Flag domains with many strong opinions as potential contradiction zones
        if len(opinions) >= 3:
            issues['info'].append({
                'type': 'contradiction_zone',
                'file': f'domain:{domain}',
                'detail': f'{len(opinions)} files contain strong assertions — review for consistency',
            })

    # ── Check 4: Stale content (> 90 days, different from 30-day stale report) ──
    very_stale = [f for f in manifest['files'] if f['age_days'] > 90]
    if very_stale:
        issues['info'].append({
            'type': 'very_stale',
            'file': 'multiple',
            'detail': f'{len(very_stale)} files are >90 days old — candidates for archive',
        })

    # ── Check 5: Empty/near-empty files ──────────────────────────
    for f in manifest['files']:
        if f['word_count'] < 50:
            issues['warning'].append({
                'type': 'stub',
                'file': f['path'],
                'detail': f'Only {f["word_count"]} words — stub or incomplete',
            })

    # ── Check 6: Missing frontmatter ─────────────────────────────
    no_frontmatter = [f for f in manifest['files'] if not f.get('has_frontmatter')]
    if len(no_frontmatter) > len(manifest['files']) * 0.5:
        issues['info'].append({
            'type': 'missing_frontmatter',
            'file': 'multiple',
            'detail': f'{len(no_frontmatter)}/{len(manifest["files"])} files lack YAML frontmatter — limits metadata queries',
        })

    # ── Generate report ──────────────────────────────────────────
    total_issues = sum(len(v) for v in issues.values())
    lines = [
        "# Wiki Lint Report",
        f"*Generated: {date.today().isoformat()} | {total_issues} issues found*",
        "",
        f"**Errors**: {len(issues['error'])} | **Warnings**: {len(issues['warning'])} | **Info**: {len(issues['info'])}",
        "",
        "---",
        "",
    ]

    for severity in ['error', 'warning', 'info']:
        if issues[severity]:
            lines.append(f"## {severity.upper()} ({len(issues[severity])})")
            lines.append("")
            for issue in issues[severity][:50]:  # Cap at 50 per severity
                lines.append(f"- **[{issue['type']}]** `{issue['file']}` — {issue['detail']}")
            if len(issues[severity]) > 50:
                lines.append(f"- *... and {len(issues[severity]) - 50} more*")
            lines.append("")

    if total_issues == 0:
        lines.append("**Wiki is clean.** No issues detected.")

    lines.extend([
        "---",
        "",
        "## Recommended Actions",
        "",
        "- **Errors**: Fix immediately — broken links degrade navigation",
        "- **Warnings**: Review in next maintenance cycle — orphans and stubs accumulate silently",
        "- **Info**: Address opportunistically — improves wiki health over time",
        "",
        f"*Run `python3 execution/knowledge_compiler.py lint` to regenerate. Schedule: monthly via `/maintenance`.*",
    ])

    report_content = "\n".join(lines)
    report_path = COMPILED_DIR / 'lint-report.md'
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content)

    # Log the lint run
    log_activity('lint', f"Lint scan — {total_issues} issues ({len(issues['error'])} errors, {len(issues['warning'])} warnings)",
                 notes=f"Files scanned: {len(manifest['files'])}")

    print(f"\n  {'='*60}")
    print(f"  WIKI LINT REPORT")
    print(f"  {'='*60}")
    print(f"  Errors:   {len(issues['error'])}")
    print(f"  Warnings: {len(issues['warning'])}")
    print(f"  Info:     {len(issues['info'])}")
    print(f"  Report:   {report_path}")
    print(f"  {'='*60}\n")

    return issues


def auto_archive_stale(manifest: Dict[str, Any] = None,
                       threshold_days: int = 90,
                       dry_run: bool = True) -> List[Dict]:
    """
    Auto-archive files older than threshold_days with zero references.

    Safety: default is dry_run=True (report only). Pass --execute to actually move files.
    Archives to knowledge/archive/, preserving directory structure.
    Git history preserves everything — this is reorganization, not deletion.
    """
    import shutil

    if manifest is None:
        manifest_path = COMPILED_DIR / 'manifest.json'
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        else:
            manifest = generate_inventory()

    archive_dir = PROJECT_ROOT / 'knowledge' / 'archive'

    # Find very stale files
    stale_candidates = [f for f in manifest['files'] if f['age_days'] > threshold_days]

    # Filter to only those in knowledge/ or extractions/ (don't archive research_outputs)
    archivable = [f for f in stale_candidates
                  if f['path'].startswith(('knowledge/', 'extractions/'))
                  and 'compiled' not in f['path']
                  and 'index.md' not in f['path']
                  and 'log.md' not in f['path']
                  and 'archive/' not in f['path']
                  and 'expert-benchmarks/' not in f['path']]

    if not archivable:
        print(f"\n  No files older than {threshold_days} days to archive.")
        return []

    if dry_run:
        print(f"\n  {'='*60}")
        print(f"  AUTO-ARCHIVE DRY RUN (pass --execute to apply)")
        print(f"  {'='*60}")
        print(f"  Threshold: {threshold_days} days")
        print(f"  Candidates: {len(archivable)} files")
        print()
        for f in archivable[:20]:
            print(f"    [{f['age_days']}d] {f['path']} ({f['word_count']:,} words)")
        if len(archivable) > 20:
            print(f"    ... and {len(archivable) - 20} more")
        print(f"\n  Run with --execute to move these to knowledge/archive/")
        print(f"  {'='*60}\n")
        return archivable

    # Execute archival
    archived = []
    archive_dir.mkdir(parents=True, exist_ok=True)

    for f in archivable:
        src = PROJECT_ROOT / f['path']
        # Preserve directory structure under archive/
        rel_from_root = Path(f['path'])
        dest = archive_dir / rel_from_root
        dest.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.move(str(src), str(dest))
            archived.append(f)
            log_activity('archive', f['name'], domain=f['domain'],
                         expert=f.get('expert', ''),
                         notes=f"Moved to archive/ ({f['age_days']} days old)")
        except Exception as e:
            print(f"  Failed to archive {f['path']}: {e}")

    print(f"\n  {'='*60}")
    print(f"  AUTO-ARCHIVE COMPLETE")
    print(f"  {'='*60}")
    print(f"  Archived: {len(archived)} files")
    print(f"  Location: knowledge/archive/")
    print(f"  {'='*60}\n")

    # Regenerate index after archival
    if archived:
        new_manifest = generate_inventory()
        update_index(new_manifest)

    return archived


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


def solution_inventory() -> List[Dict[str, Any]]:
    """Inventory reusable solution docs under docs/solutions/."""
    if not SOLUTIONS_DIR.exists():
        return []

    solutions: list[dict[str, Any]] = []
    for md_file in sorted(SOLUTIONS_DIR.rglob('*.md')):
        if md_file.name.startswith('.') or md_file.name.lower() == 'readme.md':
            continue
        try:
            content = md_file.read_text(errors='ignore')
        except Exception:
            continue

        word_count = len(content.split())
        if word_count < 10:
            continue

        stat = md_file.stat()
        modified = datetime.fromtimestamp(stat.st_mtime)
        rel_path = str(md_file.relative_to(PROJECT_ROOT))
        title = _first_heading(content, md_file.stem)
        searchable = f"{title} {rel_path} {content}"

        solutions.append({
            'path': rel_path,
            'title': title,
            'name': md_file.stem,
            'domain': _classify_domain(md_file, content),
            'word_count': word_count,
            'modified': modified.isoformat(),
            'age_days': (datetime.now() - modified).days,
            'summary': _first_body_snippet(content),
            'tokens': sorted(_tokens(searchable)),
        })

    return solutions


def search_solutions(query: str = "", top: int = 8, write_index: bool = True) -> List[Dict[str, Any]]:
    """
    Surface reusable solution docs for a mission or librarian focus.

    These are intentionally separate from the large knowledge manifest: they
    represent solved-problem guidance that should be consulted before planning.
    """
    solutions = solution_inventory()
    query_tokens = _tokens(query)

    scored: list[dict[str, Any]] = []
    for item in solutions:
        token_set = set(item.get('tokens', []))
        overlap = token_set & query_tokens
        title_tokens = _tokens(item['title'])
        path_tokens = _tokens(item['path'])
        score = len(overlap)
        score += 2 * len(title_tokens & query_tokens)
        score += len(path_tokens & query_tokens)
        if not query_tokens:
            score = 1

        if score > 0:
            match = dict(item)
            match['score'] = score
            match['matched_terms'] = sorted(overlap)
            match.pop('tokens', None)
            scored.append(match)

    scored.sort(key=lambda x: (-x['score'], -x['word_count'], x['path']))
    results = scored[:top]

    lines = [
        "# Reusable Solution Matches",
        f"*Generated: {date.today().isoformat()} | Query: {query or 'all reusable solutions'}*",
        "",
    ]

    if results:
        lines.extend([
            "| Score | Solution | Domain | Why it may matter |",
            "|---:|---|---|---|",
        ])
        for item in results:
            summary = item['summary'] or "Reusable solved-problem guidance."
            terms = f" Matched: {', '.join(item['matched_terms'])}." if item['matched_terms'] else ""
            lines.append(
                f"| {item['score']} | [`{item['title']}`]({item['path']}) | {item['domain']} | {summary}{terms} |"
            )
    else:
        lines.append("*No reusable solution docs matched this focus.*")

    lines.extend([
        "",
        "## Mission Use",
        "",
        "- Review matched solution docs before drafting the mission charter.",
        "- If a solution applies, cite it in the mission's Library Decision.",
        "- If a new reusable lesson appears, capture it in `solution-capture.md` and promote it to `docs/solutions/` only when generalizable.",
    ])

    output = "\n".join(lines)
    if write_index:
        COMPILED_DIR.mkdir(parents=True, exist_ok=True)
        (COMPILED_DIR / 'solution-matches.md').write_text(output)

    print(output)
    return results


def update_index(manifest: Dict[str, Any] = None) -> str:
    """
    Generate a living index.md — domain-organized catalog with one-line summaries.

    This is the Karpathy wiki pattern's primary navigation file:
    the LLM reads index.md first to locate relevant pages,
    replacing traditional RAG infrastructure at moderate scale.

    Updated on every ingest, compilation, or knowledge change.
    """
    if manifest is None:
        manifest_path = COMPILED_DIR / 'manifest.json'
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
        else:
            manifest = generate_inventory()

    # Group files by domain
    by_domain = defaultdict(list)
    for f in manifest['files']:
        by_domain[f['domain']].append(f)

    # Sort domains by file count (largest first), files by word count within domain
    sorted_domains = sorted(by_domain.items(), key=lambda x: -len(x[1]))

    lines = [
        "# Knowledge Index",
        f"*{manifest['total_files']} sources | {manifest['total_words']:,} words | Updated: {date.today().isoformat()}*",
        "",
        "---",
        "",
    ]

    for domain, files in sorted_domains:
        files_sorted = sorted(files, key=lambda x: -x['word_count'])
        lines.append(f"## {domain.title()} ({len(files)} files)")
        lines.append("")
        for f in files_sorted:
            expert_tag = f" [{f['expert']}]" if f['expert'] else ""
            age_tag = " (stale)" if f['age_days'] > 90 else ""
            # Make path relative to knowledge/ (where index.md lives)
            rel_path = os.path.relpath(PROJECT_ROOT / f['path'], PROJECT_ROOT / 'knowledge')
            lines.append(f"- [{f['name']}]({rel_path}){expert_tag} — {f['word_count']:,} words{age_tag}")
        lines.append("")

    # Synthesis section (if exists)
    synthesis_dir = PROJECT_ROOT / 'knowledge' / 'synthesis'
    if synthesis_dir.exists():
        synthesis_files = sorted(synthesis_dir.glob('*.md'))
        if synthesis_files:
            lines.append("## Synthesis (Cross-Domain)")
            lines.append("")
            for sf in synthesis_files:
                lines.append(f"- [{sf.stem}](knowledge/synthesis/{sf.name})")
            lines.append("")

    # Patterns section (if exists)
    patterns_dir = PROJECT_ROOT / 'knowledge' / 'patterns'
    if patterns_dir.exists():
        pattern_files = sorted(patterns_dir.glob('*.md'))
        if pattern_files:
            lines.append("## Evolved Patterns")
            lines.append("")
            for pf in pattern_files:
                lines.append(f"- [{pf.stem}](knowledge/patterns/{pf.name})")
            lines.append("")

    lines.extend([
        "---",
        f"*Auto-maintained by `execution/knowledge_compiler.py`. "
        f"Updated on every ingest, extraction, and compilation.*",
    ])

    index_content = "\n".join(lines)
    index_path = PROJECT_ROOT / 'knowledge' / 'index.md'
    index_path.write_text(index_content)

    print(f"  Index written to: {index_path}")
    print(f"  Domains: {len(sorted_domains)} | Files: {manifest['total_files']}")
    return index_content


def log_activity(action: str, title: str, domain: str = '', expert: str = '', notes: str = ''):
    """
    Append an entry to the knowledge log — chronological record of all wiki activity.

    Karpathy pattern: log.md is append-only with consistent prefixes
    enabling grep-based parsing (e.g., `grep 'ingest' knowledge/log.md`).

    Actions: ingest, query, archive, lint, reflect, evolve, merge, stale
    """
    log_path = PROJECT_ROOT / 'knowledge' / 'log.md'

    # Create log file with header if it doesn't exist
    if not log_path.exists():
        log_path.write_text(
            "# Knowledge Log\n"
            "*Append-only chronological record of all wiki activity.*\n\n"
            "---\n\n"
        )

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    domain_tag = f" | {domain}" if domain else ""
    expert_tag = f" | {expert}" if expert else ""
    notes_tag = f" — {notes}" if notes else ""

    entry = f"- `[{timestamp}]` **{action}** | {title}{domain_tag}{expert_tag}{notes_tag}\n"

    # Append to log
    with open(log_path, 'a') as f:
        f.write(entry)

    print(f"  Logged: {action} | {title}")


def archive_search_result(query: str, result_text: str, domain: str,
                          source: str = '', expert: str = ''):
    """
    Archive a high-value search result into the wiki.

    Karpathy query-writes-back pattern: exploration becomes persistent knowledge.
    Queries enrich the knowledge base instead of disappearing after the session.
    """
    # Create domain directory if needed
    domain_dir = PROJECT_ROOT / 'knowledge' / domain
    domain_dir.mkdir(parents=True, exist_ok=True)

    # Generate slug from query
    slug = query.lower()[:60].replace(' ', '-').replace('/', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    filepath = domain_dir / f"search-{slug}.md"

    # Don't overwrite existing — append a counter
    counter = 1
    while filepath.exists():
        filepath = domain_dir / f"search-{slug}-{counter}.md"
        counter += 1

    content_lines = [
        "---",
        f"source: search-archive",
        f"query: \"{query}\"",
        f"domain: {domain}",
    ]
    if expert:
        content_lines.append(f"expert: {expert}")
    if source:
        content_lines.append(f"source_url: {source}")
    content_lines.extend([
        f"archived: {datetime.now().isoformat()[:10]}",
        "---",
        "",
        f"# {query}",
        "",
        result_text,
        "",
        "---",
        f"*Archived from search on {date.today().isoformat()}. "
        f"Source: {source or 'knowledge-search'}*",
    ])

    filepath.write_text("\n".join(content_lines))

    # Log the archival
    log_activity('query-archive', query, domain=domain, expert=expert,
                 notes=f"saved to {filepath.relative_to(PROJECT_ROOT)}")

    print(f"  Archived search result: {filepath}")
    return str(filepath)


def full_compilation():
    """Run all compilation stages."""
    print("\n  Stage 1: Inventory...")
    manifest = generate_inventory()

    print("\n  Stage 2: Briefing...")
    generate_briefing(manifest)

    print("\n  Stage 3: Living index...")
    update_index(manifest)

    print("\n  Stage 4: Stale content detection...")
    stale = find_stale_content(manifest)

    print("\n  Stage 5: Overlap detection...")
    overlaps = find_overlaps(manifest)

    print("\n  Stage 6: Wiki lint...")
    issues = full_lint(manifest)

    # Log the compilation
    total_issues = sum(len(v) for v in issues.values())
    log_activity('compile', f"Full compilation — {manifest['total_files']} files, {manifest['total_words']:,} words, {total_issues} lint issues")

    print(f"\n{'='*60}")
    print(f"  FULL COMPILATION COMPLETE")
    print(f"{'='*60}")
    print(f"  Manifest: knowledge/compiled/manifest.json")
    print(f"  Briefing: knowledge/compiled/briefing.md")
    print(f"  Index:    knowledge/index.md")
    print(f"  Stale:    knowledge/compiled/stale-report.md")
    print(f"  Overlap:  knowledge/compiled/overlap-report.md")
    print(f"  Lint:     knowledge/compiled/lint-report.md")
    print(f"  Log:      knowledge/log.md")
    print(f"{'='*60}\n")


# ── CLI ─────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Knowledge Compiler — Self-healing knowledge base")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("inventory", help="Generate full knowledge inventory")
    sub.add_parser("briefing", help="Generate session-start briefing")
    sub.add_parser("index", help="Generate/update living index (knowledge/index.md)")

    stale_cmd = sub.add_parser("stale", help="Find stale content")
    stale_cmd.add_argument("--days", type=int, default=30, help="Staleness threshold (default: 30)")

    sub.add_parser("overlap", help="Find overlapping content")
    sub.add_parser("lint", help="Full wiki health check (contradictions, orphans, dead links)")

    archive_stale_cmd = sub.add_parser("auto-archive", help="Auto-archive stale content")
    archive_stale_cmd.add_argument("--days", type=int, default=90, help="Staleness threshold (default: 90)")
    archive_stale_cmd.add_argument("--execute", action="store_true", help="Actually move files (default: dry run)")

    sub.add_parser("full", help="Run all compilation stages")
    sub.add_parser("stats", help="Quick stats overview")

    solutions_cmd = sub.add_parser("solutions", help="Surface reusable docs/solutions entries for a focus")
    solutions_cmd.add_argument("query", nargs="*", help="Mission focus or search query")
    solutions_cmd.add_argument("--top", type=int, default=8, help="Number of solution docs to show")
    solutions_cmd.add_argument("--stdout", action="store_true", help="Print matches without writing knowledge/compiled/solution-matches.md")

    log_cmd = sub.add_parser("log", help="Log an activity to knowledge/log.md")
    log_cmd.add_argument("action", help="Action type (ingest, query, archive, lint, reflect, evolve)")
    log_cmd.add_argument("title", help="Description of the activity")
    log_cmd.add_argument("--domain", default="", help="Knowledge domain")
    log_cmd.add_argument("--expert", default="", help="Expert name")
    log_cmd.add_argument("--notes", default="", help="Additional notes")

    archive_cmd = sub.add_parser("archive", help="Archive a search result to the wiki")
    archive_cmd.add_argument("query", help="The search query")
    archive_cmd.add_argument("result_file", help="Path to file containing the result text")
    archive_cmd.add_argument("--domain", required=True, help="Knowledge domain")
    archive_cmd.add_argument("--source", default="", help="Source URL or reference")
    archive_cmd.add_argument("--expert", default="", help="Expert name")

    args = parser.parse_args()

    if args.command == "inventory":
        generate_inventory()
    elif args.command == "briefing":
        generate_briefing()
    elif args.command == "index":
        update_index()
    elif args.command == "stale":
        find_stale_content(threshold_days=args.days)
    elif args.command == "overlap":
        find_overlaps()
    elif args.command == "lint":
        full_lint()
    elif args.command == "auto-archive":
        auto_archive_stale(threshold_days=args.days, dry_run=not args.execute)
    elif args.command == "full":
        full_compilation()
    elif args.command == "stats":
        quick_stats()
    elif args.command == "solutions":
        search_solutions(" ".join(args.query), top=args.top, write_index=not args.stdout)
    elif args.command == "log":
        log_activity(args.action, args.title, domain=args.domain,
                     expert=args.expert, notes=args.notes)
    elif args.command == "archive":
        result_text = Path(args.result_file).read_text()
        archive_search_result(args.query, result_text, domain=args.domain,
                              source=args.source, expert=args.expert)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
