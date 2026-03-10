#!/usr/bin/env python3
"""
Intelligence Gap Detector — Strategic gap analysis for Antigravity.

Autoresearch analog: The agent forming hypotheses about what to try next
based on results.tsv history. Analyzes performance data + gap logs to
identify systematic gaps in knowledge coverage.

What it detects:
- Domains with consistently low quality scores
- Task types that have no matching skill
- Skills that are never used (dead weight)
- High-traffic skills that plateau (need evolution)
- Pattern families with thin coverage
- Expertise gap log patterns (recurring gaps)

Usage:
    from execution.gap_analysis import run_gap_analysis, get_coverage_map

CLI usage:
    python execution/gap_analysis.py analyze              # Full gap analysis
    python execution/gap_analysis.py coverage              # Coverage map
    python execution/gap_analysis.py dead-skills            # Unused skills
    python execution/gap_analysis.py recommendations        # Prioritized next steps
"""

import os
import re
import json
import argparse
from datetime import date, datetime
from typing import Optional
from pathlib import Path
from collections import Counter, defaultdict
from dotenv import load_dotenv

# Load .env
for env_path in [
    Path(__file__).parent.parent / 'jarvis-bot' / '.env',
    Path(__file__).parent.parent / '.env',
]:
    if env_path.exists():
        load_dotenv(env_path)

from notion_api import NotionAPI

PERFORMANCE_DB_ID = os.getenv(
    'NOTION_DB_PERFORMANCE',
    '31f49875a89781dbb599dee5e7961b5c'
)

SKILLS_DIR = Path(__file__).parent.parent / 'skills'
AGENTS_DIR = Path(__file__).parent.parent / 'agents'
GAP_LOG = Path(__file__).parent.parent / '.agent' / 'gap-log.md'
DOMAIN_REGISTRY = Path(__file__).parent.parent / 'DOMAIN_REGISTRY.md'


def get_all_performance_data(limit: int = 100) -> list:
    """Pull all performance data from Notion."""
    api = NotionAPI()
    result = api.query_database(
        PERFORMANCE_DB_ID,
        sorts=[{'property': 'Date', 'direction': 'descending'}],
        page_size=limit,
    )

    entries = []
    for page in result.get('results', []):
        props = page.get('properties', {})
        entry = {}

        for prop_name, prop_data in props.items():
            ptype = prop_data.get('type')
            if ptype == 'title' and prop_data.get('title'):
                entry['Output'] = prop_data['title'][0].get('plain_text', '')
            elif ptype == 'number':
                entry[prop_name] = prop_data.get('number')
            elif ptype == 'select' and prop_data.get('select'):
                entry[prop_name] = prop_data['select'].get('name', '')
            elif ptype == 'rich_text' and prop_data.get('rich_text'):
                entry[prop_name] = prop_data['rich_text'][0].get('plain_text', '')
            elif ptype == 'date' and prop_data.get('date'):
                entry[prop_name] = prop_data['date'].get('start', '')

        entries.append(entry)

    return entries


def get_all_skills() -> list:
    """Get all skill directories."""
    skills = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / 'SKILL.md'
        genius_md = skill_dir / 'genius.md'
        workflows_dir = skill_dir / 'workflows'

        workflow_count = 0
        if workflows_dir.exists():
            workflow_count = len(list(workflows_dir.glob('*.md')))

        skills.append({
            'name': skill_dir.name,
            'has_skill_md': skill_md.exists(),
            'has_genius': genius_md.exists(),
            'workflow_count': workflow_count,
        })

    return skills


def parse_gap_log() -> list:
    """Parse the gap log for recurring patterns."""
    if not GAP_LOG.exists():
        return []

    content = GAP_LOG.read_text()
    entries = []

    # Parse ## [Date] — [Domain] headers
    blocks = re.split(r'## ', content)
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        header_match = re.match(r'(\d{4}-\d{2}-\d{2})\s*[—–-]\s*(.+)', block.split('\n')[0])
        if not header_match:
            continue

        entry = {
            'date': header_match.group(1),
            'domain': header_match.group(2).strip(),
            'severity': '',
            'mode': '',
            'resolution': '',
            'skill_created': '',
        }

        for line in block.split('\n'):
            line = line.strip()
            if line.startswith('**Severity**:'):
                entry['severity'] = line.split(':', 1)[1].strip()
            elif line.startswith('**Mode**:'):
                entry['mode'] = line.split(':', 1)[1].strip()
            elif line.startswith('**Resolution**:'):
                entry['resolution'] = line.split(':', 1)[1].strip()
            elif line.startswith('**Skill Created**:'):
                entry['skill_created'] = line.split(':', 1)[1].strip()

        entries.append(entry)

    return entries


def analyze_skill_usage(perf_data: list) -> dict:
    """Analyze which skills are used and how they perform."""
    skill_stats = defaultdict(lambda: {
        'count': 0,
        'scores': [],
        'task_types': Counter(),
        'statuses': Counter(),
    })

    for entry in perf_data:
        skill = entry.get('Skill', '')
        if not skill:
            continue

        stats = skill_stats[skill]
        stats['count'] += 1

        score = entry.get('Quality Score')
        if score is not None:
            stats['scores'].append(score)

        task_type = entry.get('Task Type', '')
        if task_type:
            stats['task_types'][task_type] += 1

        status = entry.get('Status', '')
        if status:
            stats['statuses'][status] += 1

    return dict(skill_stats)


def analyze_task_type_coverage(perf_data: list) -> dict:
    """Analyze task type coverage and quality."""
    type_stats = defaultdict(lambda: {
        'count': 0,
        'skills_used': set(),
        'scores': [],
    })

    for entry in perf_data:
        task_type = entry.get('Task Type', '')
        if not task_type:
            continue

        stats = type_stats[task_type]
        stats['count'] += 1

        skill = entry.get('Skill', '')
        if skill:
            stats['skills_used'].add(skill)

        score = entry.get('Quality Score')
        if score is not None:
            stats['scores'].append(score)

    # Convert sets to lists for JSON serialization
    result = {}
    for task_type, stats in type_stats.items():
        result[task_type] = {
            'count': stats['count'],
            'skills_used': sorted(stats['skills_used']),
            'avg_quality': round(sum(stats['scores']) / len(stats['scores']), 1) if stats['scores'] else 0,
        }

    return result


def find_dead_skills(perf_data: list, all_skills: list) -> list:
    """Find skills that exist but have never been used."""
    used_skills = set()
    for entry in perf_data:
        skill = entry.get('Skill', '')
        if skill:
            used_skills.add(skill)

    dead = []
    for skill in all_skills:
        if skill['name'] not in used_skills:
            dead.append(skill)

    return dead


def find_recurring_gaps(gap_log: list) -> list:
    """Find domains that appear 3+ times in the gap log."""
    domain_counts = Counter(e['domain'] for e in gap_log)
    recurring = []
    for domain, count in domain_counts.most_common():
        if count >= 3:
            recurring.append({
                'domain': domain,
                'occurrences': count,
                'severities': [e['severity'] for e in gap_log if e['domain'] == domain],
                'resolved': any(e['skill_created'] for e in gap_log if e['domain'] == domain),
            })
    return recurring


def run_gap_analysis() -> dict:
    """
    Run a comprehensive gap analysis.

    Returns:
    {
        'summary': dict,
        'low_performing_skills': list,
        'dead_skills': list,
        'weak_task_types': list,
        'recurring_gaps': list,
        'recommendations': list,
    }
    """
    perf_data = get_all_performance_data()
    all_skills = get_all_skills()
    gap_log = parse_gap_log()

    skill_usage = analyze_skill_usage(perf_data)
    task_coverage = analyze_task_type_coverage(perf_data)
    dead_skills = find_dead_skills(perf_data, all_skills)
    recurring_gaps = find_recurring_gaps(gap_log)

    # Low performing skills (avg < 6 with 3+ entries)
    low_performers = []
    for skill, stats in skill_usage.items():
        if len(stats['scores']) >= 3:
            avg = sum(stats['scores']) / len(stats['scores'])
            if avg < 6:
                low_performers.append({
                    'skill': skill,
                    'avg_quality': round(avg, 1),
                    'entries': stats['count'],
                    'discard_rate': round(stats['statuses'].get('Discard', 0) / stats['count'], 2) if stats['count'] else 0,
                })

    # Weak task types (avg < 6)
    weak_types = []
    for task_type, stats in task_coverage.items():
        if stats['avg_quality'] < 6 and stats['count'] >= 2:
            weak_types.append({
                'task_type': task_type,
                'avg_quality': stats['avg_quality'],
                'entries': stats['count'],
                'skills_used': stats['skills_used'],
            })

    # Generate recommendations
    recommendations = _generate_gap_recommendations(
        perf_data, low_performers, dead_skills, weak_types, recurring_gaps
    )

    return {
        'summary': {
            'total_performance_entries': len(perf_data),
            'total_skills': len(all_skills),
            'used_skills': len(skill_usage),
            'dead_skills': len(dead_skills),
            'gap_log_entries': len(gap_log),
            'analysis_date': date.today().isoformat(),
        },
        'low_performing_skills': low_performers,
        'dead_skills_count': len(dead_skills),
        'dead_skills_sample': [s['name'] for s in dead_skills[:20]],
        'weak_task_types': weak_types,
        'recurring_gaps': recurring_gaps,
        'task_type_coverage': task_coverage,
        'recommendations': recommendations,
    }


def _generate_gap_recommendations(perf_data, low_performers, dead_skills, weak_types, recurring_gaps) -> list:
    """Generate prioritized gap-closing recommendations."""
    recs = []

    # Priority 1: Recurring gaps (proven demand, no supply)
    for gap in recurring_gaps:
        if not gap['resolved']:
            recs.append({
                'priority': 'HIGH',
                'type': 'RECURRING_GAP',
                'action': f'Extract a skill for "{gap["domain"]}" — appeared {gap["occurrences"]} times in gap log without resolution.',
                'domain': gap['domain'],
            })

    # Priority 2: Low performing skills (quality below threshold)
    for skill in low_performers:
        recs.append({
            'priority': 'HIGH',
            'type': 'LOW_PERFORMER',
            'action': f'Evolve skill "{skill["skill"]}" — averaging {skill["avg_quality"]}/10 across {skill["entries"]} outputs.',
            'skill': skill['skill'],
        })

    # Priority 3: Weak task types
    for tt in weak_types:
        recs.append({
            'priority': 'MEDIUM',
            'type': 'WEAK_TASK_TYPE',
            'action': f'Improve "{tt["task_type"]}" coverage — averaging {tt["avg_quality"]}/10. Skills used: {", ".join(tt["skills_used"][:3])}.',
            'task_type': tt['task_type'],
        })

    # Priority 4: No data yet
    if not perf_data:
        recs.append({
            'priority': 'HIGH',
            'type': 'NO_DATA',
            'action': 'Start using skills and logging outputs. The gap detector needs performance data to work (20+ entries recommended).',
        })
    elif len(perf_data) < 20:
        recs.append({
            'priority': 'MEDIUM',
            'type': 'LOW_DATA',
            'action': f'Continue logging outputs ({len(perf_data)}/20 minimum). Gap detection improves with more data.',
        })

    # Priority 5: Dead skills (cleanup opportunity)
    if len(dead_skills) > 20:
        recs.append({
            'priority': 'LOW',
            'type': 'DEAD_SKILLS',
            'action': f'{len(dead_skills)} skills have never been used. Consider auditing for relevance or archiving unused skills.',
        })

    if not recs:
        recs.append({
            'priority': 'INFO',
            'type': 'HEALTHY',
            'action': 'No critical gaps detected. Continue monitoring and evolving skills.',
        })

    return recs


def generate_gap_report() -> str:
    """Generate a markdown gap analysis report."""
    analysis = run_gap_analysis()
    summary = analysis['summary']

    lines = [
        "# Intelligence Gap Report",
        f"*Generated: {summary['analysis_date']}*",
        "",
        "## System Health",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Performance entries | {summary['total_performance_entries']} |",
        f"| Total skills | {summary['total_skills']} |",
        f"| Active skills (ever used) | {summary['used_skills']} |",
        f"| Unused skills | {summary['dead_skills']} |",
        f"| Gap log entries | {summary['gap_log_entries']} |",
        "",
    ]

    # Recommendations
    lines.extend([
        "## Prioritized Recommendations",
        "",
    ])

    for i, rec in enumerate(analysis['recommendations'], 1):
        emoji = {'HIGH': '!!!', 'MEDIUM': '!!', 'LOW': '!', 'INFO': ''}[rec['priority']]
        lines.append(f"{i}. **[{rec['priority']}]** {rec['action']}")

    lines.append("")

    # Low performers
    if analysis['low_performing_skills']:
        lines.extend([
            "## Low Performing Skills",
            "",
            "| Skill | Avg Quality | Entries | Discard Rate |",
            "|-------|------------|---------|-------------|",
        ])
        for skill in analysis['low_performing_skills']:
            lines.append(f"| {skill['skill']} | {skill['avg_quality']}/10 | {skill['entries']} | {skill['discard_rate']:.0%} |")
        lines.append("")

    # Weak task types
    if analysis['weak_task_types']:
        lines.extend([
            "## Weak Task Types",
            "",
            "| Task Type | Avg Quality | Entries | Skills Used |",
            "|-----------|------------|---------|-------------|",
        ])
        for tt in analysis['weak_task_types']:
            skills = ', '.join(tt['skills_used'][:3])
            lines.append(f"| {tt['task_type']} | {tt['avg_quality']}/10 | {tt['entries']} | {skills} |")
        lines.append("")

    # Recurring gaps
    if analysis['recurring_gaps']:
        lines.extend([
            "## Recurring Knowledge Gaps",
            "",
            "| Domain | Occurrences | Resolved? |",
            "|--------|------------|-----------|",
        ])
        for gap in analysis['recurring_gaps']:
            resolved = 'Yes' if gap['resolved'] else 'No'
            lines.append(f"| {gap['domain']} | {gap['occurrences']} | {resolved} |")
        lines.append("")

    # Task type coverage
    if analysis['task_type_coverage']:
        lines.extend([
            "## Task Type Coverage",
            "",
            "| Task Type | Entries | Avg Quality | Skills Used |",
            "|-----------|---------|------------|-------------|",
        ])
        for tt, stats in sorted(analysis['task_type_coverage'].items(), key=lambda x: x[1]['count'], reverse=True):
            skills = ', '.join(stats['skills_used'][:3])
            lines.append(f"| {tt} | {stats['count']} | {stats['avg_quality']}/10 | {skills} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Gap Analysis CLI')
    sub = parser.add_subparsers(dest='command')

    # analyze
    sub.add_parser('analyze', help='Full gap analysis')

    # coverage
    sub.add_parser('coverage', help='Coverage map')

    # dead-skills
    sub.add_parser('dead-skills', help='List unused skills')

    # recommendations
    sub.add_parser('recommendations', help='Prioritized recommendations')

    args = parser.parse_args()

    if args.command == 'analyze':
        print(generate_gap_report())

    elif args.command == 'coverage':
        perf_data = get_all_performance_data()
        coverage = analyze_task_type_coverage(perf_data)
        if not coverage:
            print("  No performance data yet. Use skills and log outputs to build coverage data.")
        else:
            print("  Task Type Coverage:")
            for tt, stats in sorted(coverage.items(), key=lambda x: x[1]['count'], reverse=True):
                print(f"    {tt}: {stats['count']} entries, avg {stats['avg_quality']}/10, skills: {', '.join(stats['skills_used'][:3])}")

    elif args.command == 'dead-skills':
        perf_data = get_all_performance_data()
        all_skills = get_all_skills()
        dead = find_dead_skills(perf_data, all_skills)
        print(f"  {len(dead)} unused skills (out of {len(all_skills)} total):")
        for skill in dead[:30]:
            wf = f"{skill['workflow_count']} workflows" if skill['workflow_count'] else "no workflows"
            genius = "+ genius" if skill['has_genius'] else "no genius"
            print(f"    {skill['name']} ({wf}, {genius})")
        if len(dead) > 30:
            print(f"    ... and {len(dead) - 30} more")

    elif args.command == 'recommendations':
        analysis = run_gap_analysis()
        if not analysis['recommendations']:
            print("  No recommendations — system is healthy.")
        else:
            print("  Prioritized Recommendations:")
            for i, rec in enumerate(analysis['recommendations'], 1):
                print(f"    {i}. [{rec['priority']}] {rec['action']}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
