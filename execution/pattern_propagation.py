#!/usr/bin/env python3
"""
Pattern Propagation — Cross-pollination engine for Antigravity skills.

Autoresearch analog: Karpathy's SETI@home vision — multiple agents sharing
discoveries. When one skill discovers an effective pattern improvement,
surface it to related skills that share the same pattern family.

This script:
1. Scans Evolution Logs across all genius.md files
2. Identifies KEPT improvements
3. Maps pattern families across skills
4. Generates transfer candidates for related skills

Usage:
    from execution.pattern_propagation import (
        scan_evolution_logs,
        find_related_skills,
        generate_propagation_report,
    )

CLI usage:
    python execution/pattern_propagation.py scan              # Scan all evolution logs
    python execution/pattern_propagation.py related <skill>   # Find related skills
    python execution/pattern_propagation.py report            # Full propagation report
"""

import os
import re
import json
import argparse
from datetime import date
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

# Load .env
for env_path in [
    Path(__file__).parent.parent / 'jarvis-bot' / '.env',
    Path(__file__).parent.parent / '.env',
]:
    if env_path.exists():
        load_dotenv(env_path)

SKILLS_DIR = Path(__file__).parent.parent / 'skills'
DOMAIN_REGISTRY = Path(__file__).parent.parent / 'DOMAIN_REGISTRY.md'

# ─── Pattern Families ────────────────────────────────────────────
# Skills are grouped by the types of patterns they use.
# A skill can belong to multiple families.
# When one skill in a family improves a pattern, all related skills
# in that family are candidates for receiving the improvement.

PATTERN_FAMILIES = {
    'persuasion': {
        'description': 'Techniques for changing minds, building belief, overcoming objections',
        'keywords': ['proof', 'persuasion', 'objection', 'belief', 'trust', 'credibility', 'sales', 'closing', 'nepq', 'identity'],
    },
    'hooks': {
        'description': 'Attention capture — first lines, thumbnails, scroll-stoppers',
        'keywords': ['hook', 'attention', 'scroll', 'viral', 'dopamine', 'curiosity', 'open-loop'],
    },
    'structure': {
        'description': 'Content architecture — frameworks, templates, flow patterns',
        'keywords': ['structure', 'framework', 'template', 'architecture', 'outline', 'format', 'flow'],
    },
    'voice': {
        'description': 'Tone, rhythm, sentence craft, stylistic patterns',
        'keywords': ['voice', 'tone', 'rhythm', 'sentence', 'style', 'prose', 'rhetoric', 'literary'],
    },
    'research': {
        'description': 'Analysis, data gathering, market intelligence, consumer insight',
        'keywords': ['research', 'analysis', 'intelligence', 'consumer', 'market', 'persona', 'validation'],
    },
    'conversion': {
        'description': 'Turning attention into action — CTAs, funnels, landing pages',
        'keywords': ['conversion', 'cta', 'funnel', 'landing', 'opt-in', 'email', 'sequence', 'sales-page'],
    },
    'storytelling': {
        'description': 'Narrative techniques — story arcs, emotional architecture, character',
        'keywords': ['story', 'narrative', 'emotion', 'character', 'arc', 'frame', 'anecdote'],
    },
    'positioning': {
        'description': 'Market positioning, differentiation, category design, brand',
        'keywords': ['positioning', 'differentiation', 'brand', 'category', 'premium', 'authority', 'niche'],
    },
    'systems': {
        'description': 'AI systems, automation, agent architecture, workflows',
        'keywords': ['system', 'automation', 'agent', 'workflow', 'pipeline', 'orchestration', 'ai'],
    },
}


def classify_skill_families(skill_name: str, genius_content: str = '') -> list:
    """
    Classify a skill into pattern families based on its name and genius.md content.
    Returns a list of family names.
    """
    families = []
    searchable = (skill_name + ' ' + genius_content).lower()

    for family, config in PATTERN_FAMILIES.items():
        matches = sum(1 for kw in config['keywords'] if kw in searchable)
        # Need at least 2 keyword matches to classify
        if matches >= 2:
            families.append(family)

    # If no families matched, use the skill name heuristics
    if not families:
        # Fallback: match on single strong keyword in skill name
        name_lower = skill_name.lower()
        for family, config in PATTERN_FAMILIES.items():
            if any(kw in name_lower for kw in config['keywords']):
                families.append(family)

    return families if families else ['uncategorized']


def scan_evolution_logs() -> list:
    """
    Scan all genius.md files for Evolution Log entries.

    Returns list of:
    {
        'skill': str,
        'date': str,
        'description': str,
        'result': str,  # 'KEPT' or 'DISCARDED'
        'hypothesis': str,
        'change': str,
        'lesson': str,
        'families': list,
    }
    """
    entries = []

    for genius_path in sorted(SKILLS_DIR.glob('*/genius.md')):
        skill_name = genius_path.parent.name
        content = genius_path.read_text()

        # Check if there's an Evolution Log section
        if '## Evolution Log' not in content:
            continue

        # Extract the Evolution Log section
        log_section = content.split('## Evolution Log')[1]
        # Stop at the next ## section if there is one
        next_section = re.search(r'\n## [^E]', log_section)
        if next_section:
            log_section = log_section[:next_section.start()]

        # Parse individual entries (### headers)
        entry_blocks = re.split(r'### ', log_section)
        for block in entry_blocks:
            block = block.strip()
            if not block:
                continue

            # Parse the header line: "[Date] — [Description]"
            header_match = re.match(r'(\d{4}-\d{2}-\d{2})\s*[—–-]\s*(.+)', block.split('\n')[0])
            if not header_match:
                continue

            entry = {
                'skill': skill_name,
                'date': header_match.group(1),
                'description': header_match.group(2).strip(),
                'result': 'KEPT' if 'KEPT' in block.upper() or 'kept' in block.lower() else 'DISCARDED',
                'hypothesis': '',
                'change': '',
                'lesson': '',
            }

            # Extract fields
            for line in block.split('\n'):
                line = line.strip()
                if line.startswith('- **Hypothesis**:'):
                    entry['hypothesis'] = line.split(':', 1)[1].strip()
                elif line.startswith('- **Change**:'):
                    entry['change'] = line.split(':', 1)[1].strip()
                elif line.startswith('- **Lesson**:'):
                    entry['lesson'] = line.split(':', 1)[1].strip()

            # Classify into pattern families
            genius_content = content[:2000]  # First 2000 chars for classification
            entry['families'] = classify_skill_families(skill_name, genius_content)

            entries.append(entry)

    return entries


def find_related_skills(skill_name: str, pattern_type: str = '') -> list:
    """
    Find skills related to the given skill via pattern family overlap.

    Returns list of:
    {
        'skill': str,
        'shared_families': list,
        'overlap_score': int,
    }
    """
    # Get the source skill's families
    source_genius = SKILLS_DIR / skill_name / 'genius.md'
    source_content = source_genius.read_text() if source_genius.exists() else ''
    source_families = classify_skill_families(skill_name, source_content[:2000])

    if pattern_type:
        # If a specific pattern type is given, prioritize skills in that family
        source_families = [pattern_type] + [f for f in source_families if f != pattern_type]

    related = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == skill_name:
            continue

        genius_path = skill_dir / 'genius.md'
        if not genius_path.exists():
            continue

        target_content = genius_path.read_text()[:2000]
        target_families = classify_skill_families(skill_dir.name, target_content)

        shared = set(source_families) & set(target_families)
        if shared:
            related.append({
                'skill': skill_dir.name,
                'shared_families': sorted(shared),
                'overlap_score': len(shared),
            })

    # Sort by overlap score (most related first)
    related.sort(key=lambda x: x['overlap_score'], reverse=True)
    return related


def generate_propagation_report() -> str:
    """
    Generate a full cross-pollination report.

    Scans all evolution logs, identifies KEPT improvements,
    and maps them to related skills that could benefit.
    """
    entries = scan_evolution_logs()
    kept_entries = [e for e in entries if e['result'] == 'KEPT']

    if not entries:
        return (
            "# Cross-Pollination Report\n\n"
            f"*Generated: {date.today().isoformat()}*\n\n"
            "**No evolution logs found.** Skills need to go through the evolution cycle "
            "(Phase 2) before cross-pollination can identify transferable improvements.\n\n"
            "Run `/skill-evolution <skill-name>` to start improving skills."
        )

    lines = [
        "# Cross-Pollination Report",
        f"*Generated: {date.today().isoformat()}*",
        "",
        f"## Summary",
        f"- **Total evolution entries**: {len(entries)}",
        f"- **Kept improvements**: {len(kept_entries)}",
        f"- **Discarded attempts**: {len(entries) - len(kept_entries)}",
        "",
    ]

    if not kept_entries:
        lines.append("**No kept improvements to propagate yet.** Continue evolution cycles to generate transferable patterns.")
        return "\n".join(lines)

    lines.extend([
        "## Transferable Improvements",
        "",
    ])

    for entry in kept_entries:
        related = find_related_skills(entry['skill'])
        if not related:
            continue

        lines.extend([
            f"### {entry['description']}",
            f"- **Source skill**: {entry['skill']}",
            f"- **Date**: {entry['date']}",
            f"- **Change**: {entry['change'] or entry['hypothesis']}",
            f"- **Pattern families**: {', '.join(entry['families'])}",
            "",
            "**Candidate skills for transfer:**",
            "",
            "| Skill | Shared Families | Overlap |",
            "|-------|----------------|---------|",
        ])

        for rel in related[:10]:  # Top 10 related
            lines.append(f"| {rel['skill']} | {', '.join(rel['shared_families'])} | {rel['overlap_score']} |")

        lines.append("")

    # Pattern family summary
    lines.extend([
        "## Pattern Family Map",
        "",
        "| Family | Description | Skill Count |",
        "|--------|-------------|-------------|",
    ])

    family_counts = {}
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        genius_path = skill_dir / 'genius.md'
        content = genius_path.read_text()[:2000] if genius_path.exists() else ''
        families = classify_skill_families(skill_dir.name, content)
        for fam in families:
            family_counts[fam] = family_counts.get(fam, 0) + 1

    for fam, count in sorted(family_counts.items(), key=lambda x: x[1], reverse=True):
        desc = PATTERN_FAMILIES.get(fam, {}).get('description', 'Uncategorized')
        lines.append(f"| {fam} | {desc} | {count} |")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Pattern Propagation CLI')
    sub = parser.add_subparsers(dest='command')

    # scan
    sub.add_parser('scan', help='Scan all evolution logs')

    # related
    rel = sub.add_parser('related', help='Find related skills')
    rel.add_argument('skill', help='Source skill name')
    rel.add_argument('--pattern', default='', help='Specific pattern type to prioritize')

    # report
    sub.add_parser('report', help='Generate full propagation report')

    args = parser.parse_args()

    if args.command == 'scan':
        entries = scan_evolution_logs()
        if not entries:
            print("  No evolution log entries found across any skills.")
        else:
            print(f"  Found {len(entries)} evolution entries:")
            for e in entries:
                status = 'KEPT' if e['result'] == 'KEPT' else 'DISC'
                print(f"    [{status}] {e['skill']}: {e['description']} ({e['date']})")

    elif args.command == 'related':
        related = find_related_skills(args.skill, args.pattern)
        if not related:
            print(f"  No related skills found for '{args.skill}'.")
        else:
            print(f"  Related skills for '{args.skill}':")
            for r in related[:15]:
                print(f"    {r['skill']} — families: {', '.join(r['shared_families'])} (overlap: {r['overlap_score']})")

    elif args.command == 'report':
        print(generate_propagation_report())

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
