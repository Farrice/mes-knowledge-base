#!/usr/bin/env python3
"""
Skill Benchmark — Fixed-budget evaluation harness for skill workflows.

Autoresearch analog: Every experiment (workflow variant) gets evaluated
against the same benchmark tasks with the same scoring rubric. This is
the "prepare.py" for skill evolution — the immutable evaluation surface.

Usage:
    from execution.skill_benchmark import benchmark_skill, compare_variants

    # Benchmark a skill's current workflows
    results = benchmark_skill("luke-iha-proof-mechanisms")

    # Compare a variant workflow against current
    comparison = compare_variants(
        skill="luke-iha-proof-mechanisms",
        workflow="01-proof-fortified-ad-pipeline",
        variant_path="skills/luke-iha-proof-mechanisms/workflows/01-proof-fortified-ad-pipeline.variant.md",
    )

CLI usage:
    python execution/skill_benchmark.py benchmark <skill-name>
    python execution/skill_benchmark.py compare <skill> <workflow> <variant-path>
    python execution/skill_benchmark.py report <skill-name>
"""

import os
import json
import argparse
from datetime import date, datetime
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

from notion_api import NotionAPI

PERFORMANCE_DB_ID = os.getenv(
    'NOTION_DB_PERFORMANCE',
    '31f49875a89781dbb599dee5e7961b5c'
)

SKILLS_DIR = Path(__file__).parent.parent / 'skills'
AGENTS_DIR = Path(__file__).parent.parent / 'agents'


# ─── Standard Benchmark Tasks ────────────────────────────────────
# Each domain has 3 standard test prompts. When benchmarking a skill,
# we match the skill's domain to the right test set.

BENCHMARK_TASKS = {
    'copywriting': [
        'Write a cold email for a B2B SaaS product that reduces churn by 40%.',
        'Create 3 headline variations for a landing page selling an AI writing tool to content agencies.',
        'Rewrite this weak copy into something compelling: "Our product is good and helps businesses grow."',
    ],
    'content': [
        'Create a TikTok script hook + first 15 seconds for a personal finance channel targeting 25-35 year olds.',
        'Write a LinkedIn post announcing a new AI tool launch — needs to drive comments, not just likes.',
        'Outline a YouTube video on "Why most people fail at freelancing" using storytelling structure.',
    ],
    'strategy': [
        'Position a new AI writing assistant in a market dominated by Jasper and Copy.ai.',
        'Design a go-to-market strategy for a $97/month community for first-time founders.',
        'Create a competitive analysis framework for entering the AI video generation space.',
    ],
    'sales': [
        'Handle this objection: "I need to think about it" — the prospect is a small business owner considering a $5K consulting package.',
        'Write a 3-email nurture sequence for leads who downloaded a free AI automation guide.',
        'Create a VSL outline for a $2,000 course on building an AI agency.',
    ],
    'research': [
        'Analyze the competitive landscape for AI-powered SEO tools in 2026.',
        'Create a consumer persona for someone buying their first online course on personal branding.',
        'Identify 3 underserved niches in the AI services market with unit economics.',
    ],
    'brand': [
        'Develop a positioning statement for a personal brand that teaches AI to non-technical founders.',
        'Create a brand voice guide for a premium newsletter about wealth building.',
        'Design a content pillar strategy for a creator who covers AI, productivity, and business.',
    ],
    'default': [
        'Create a professional deliverable in your domain of expertise for a small business owner.',
        'Analyze a common problem in your domain and provide an actionable framework.',
        'Write educational content explaining a complex concept in your field to a beginner audience.',
    ],
}

# Domain mapping — maps skill name keywords to benchmark domains
DOMAIN_KEYWORDS = {
    'copywriting': ['copy', 'copywriting', 'sales-page', 'email', 'vsl', 'direct-response', 'proof', 'rhetoric'],
    'content': ['content', 'viral', 'tiktok', 'youtube', 'social', 'hook', 'shareworthy'],
    'strategy': ['strategy', 'positioning', 'consulting', 'intelligence', 'market', 'business'],
    'sales': ['sales', 'persuasion', 'objection', 'closing', 'outreach', 'lead-gen'],
    'research': ['research', 'consumer', 'validation', 'behavioral', 'persona'],
    'brand': ['brand', 'personal-brand', 'linkedin', 'authority', 'differentiation'],
}


def detect_domain(skill_name: str) -> str:
    """Detect benchmark domain from skill name."""
    name_lower = skill_name.lower()
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in name_lower for kw in keywords):
            return domain
    return 'default'


def get_skill_info(skill_name: str) -> dict:
    """Read a skill's SKILL.md and enumerate its workflows."""
    skill_dir = SKILLS_DIR / skill_name
    if not skill_dir.exists():
        raise FileNotFoundError(f"Skill not found: {skill_dir}")

    info = {
        'name': skill_name,
        'path': str(skill_dir),
        'workflows': [],
        'has_genius': False,
        'domain': detect_domain(skill_name),
    }

    # Check for genius.md
    genius_path = skill_dir / 'genius.md'
    info['has_genius'] = genius_path.exists()

    # Enumerate workflows
    workflow_dir = skill_dir / 'workflows'
    if workflow_dir.exists():
        for wf in sorted(workflow_dir.glob('*.md')):
            if not wf.name.endswith('.variant.md'):
                info['workflows'].append({
                    'name': wf.stem,
                    'path': str(wf),
                    'filename': wf.name,
                })

    return info


def get_performance_history(skill_name: str, limit: int = 20) -> list:
    """Pull performance history for a skill from Notion."""
    api = NotionAPI()
    result = api.query_database(
        PERFORMANCE_DB_ID,
        filter={'property': 'Skill', 'rich_text': {'contains': skill_name}},
        sorts=[{'property': 'Date', 'direction': 'descending'}],
        page_size=limit,
    )

    entries = []
    for page in result.get('results', []):
        props = page.get('properties', {})
        entry = {
            'id': page['id'],
            'url': page.get('url', ''),
        }

        # Extract properties
        for prop_name, prop_data in props.items():
            ptype = prop_data.get('type')
            if ptype == 'title' and prop_data.get('title'):
                entry['output'] = prop_data['title'][0].get('plain_text', '')
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


def benchmark_skill(skill_name: str) -> dict:
    """
    Run a full benchmark assessment of a skill.

    Returns:
    {
        'skill': str,
        'domain': str,
        'workflow_count': int,
        'performance': {
            'entries': int,
            'avg_quality': float,
            'avg_intent': float,
            'avg_expert': float,
            'avg_adversarial': float,
            'trend': str,  # 'improving', 'stable', 'declining'
        },
        'weakest_workflow': str or None,
        'weakest_dimension': str or None,
        'benchmark_tasks': list,
        'recommendations': list,
    }
    """
    info = get_skill_info(skill_name)
    history = get_performance_history(skill_name)

    report = {
        'skill': skill_name,
        'domain': info['domain'],
        'workflow_count': len(info['workflows']),
        'has_genius': info['has_genius'],
        'workflows': [w['name'] for w in info['workflows']],
        'performance': _analyze_performance(history),
        'weakest_workflow': None,
        'weakest_dimension': None,
        'benchmark_tasks': BENCHMARK_TASKS.get(info['domain'], BENCHMARK_TASKS['default']),
        'recommendations': [],
    }

    # Identify weakest workflow (if we have per-workflow data)
    workflow_scores = {}
    for entry in history:
        wf = entry.get('Workflow', '')
        score = entry.get('Quality Score')
        if wf and score is not None:
            workflow_scores.setdefault(wf, []).append(score)

    if workflow_scores:
        weakest_wf = min(workflow_scores, key=lambda k: sum(workflow_scores[k]) / len(workflow_scores[k]))
        weakest_avg = sum(workflow_scores[weakest_wf]) / len(workflow_scores[weakest_wf])
        report['weakest_workflow'] = weakest_wf
        report['weakest_workflow_avg'] = round(weakest_avg, 1)

    # Identify weakest dimension
    perf = report['performance']
    dimensions = {
        'Intent Alignment': perf.get('avg_intent', 0),
        'Expert Standard': perf.get('avg_expert', 0),
        'Adversarial Resilience': perf.get('avg_adversarial', 0),
    }
    nonzero = {k: v for k, v in dimensions.items() if v > 0}
    if nonzero:
        report['weakest_dimension'] = min(nonzero, key=nonzero.get)

    # Generate recommendations
    report['recommendations'] = _generate_recommendations(report)

    return report


def _analyze_performance(history: list) -> dict:
    """Analyze performance trends from history entries."""
    if not history:
        return {
            'entries': 0,
            'avg_quality': 0,
            'avg_intent': 0,
            'avg_expert': 0,
            'avg_adversarial': 0,
            'trend': 'no_data',
        }

    quality = [e.get('Quality Score') for e in history if e.get('Quality Score') is not None]
    intent = [e.get('Intent Alignment') for e in history if e.get('Intent Alignment') is not None]
    expert = [e.get('Expert Standard') for e in history if e.get('Expert Standard') is not None]
    adversarial = [e.get('Adversarial Resilience') for e in history if e.get('Adversarial Resilience') is not None]

    # Trend detection: compare first half vs second half of quality scores
    trend = 'no_data'
    if len(quality) >= 4:
        mid = len(quality) // 2
        # History is sorted newest-first, so recent = quality[:mid], older = quality[mid:]
        recent_avg = sum(quality[:mid]) / mid
        older_avg = sum(quality[mid:]) / (len(quality) - mid)
        delta = recent_avg - older_avg
        if delta > 0.5:
            trend = 'improving'
        elif delta < -0.5:
            trend = 'declining'
        else:
            trend = 'stable'
    elif quality:
        trend = 'insufficient_data'

    return {
        'entries': len(history),
        'avg_quality': round(sum(quality) / len(quality), 1) if quality else 0,
        'avg_intent': round(sum(intent) / len(intent), 1) if intent else 0,
        'avg_expert': round(sum(expert) / len(expert), 1) if expert else 0,
        'avg_adversarial': round(sum(adversarial) / len(adversarial), 1) if adversarial else 0,
        'trend': trend,
    }


def _generate_recommendations(report: dict) -> list:
    """Generate actionable evolution recommendations."""
    recs = []
    perf = report['performance']

    if perf['entries'] == 0:
        recs.append('NO_DATA: Use this skill to establish a performance baseline (need 3+ entries).')
        return recs

    if perf['entries'] < 3:
        recs.append(f'LOW_DATA: Only {perf["entries"]} entries. Need 3+ for meaningful analysis.')

    if perf['trend'] == 'declining':
        recs.append('REGRESSION: Quality trend is declining. Review recent changes to genius.md and workflows.')

    if report['weakest_dimension']:
        dim = report['weakest_dimension']
        score = perf.get(f'avg_{dim.lower().replace(" ", "_")}', 0)
        if score < 6:
            recs.append(f'WEAK_DIMENSION: {dim} averaging {score}/10. Focus evolution efforts here.')

    if report['weakest_workflow']:
        recs.append(f'WEAK_WORKFLOW: "{report["weakest_workflow"]}" averaging {report.get("weakest_workflow_avg", "?")}/10. Candidate for variant testing.')

    if not report['has_genius']:
        recs.append('MISSING_GENIUS: No genius.md found. Skill may lack deep context for quality outputs.')

    if perf['avg_quality'] >= 8:
        recs.append('HIGH_PERFORMER: Averaging 8+. Consider cross-pollinating patterns to related skills.')

    if not recs:
        recs.append('STABLE: Skill performing within normal range. Continue monitoring.')

    return recs


def compare_variants(skill_name: str, workflow: str, variant_path: str) -> dict:
    """
    Compare a variant workflow file against the current version.

    Returns a comparison report with structural analysis.
    This does NOT auto-run the variant — it analyzes the diff for
    a human or agent to review before committing.
    """
    info = get_skill_info(skill_name)
    current_wf = None
    for wf in info['workflows']:
        if wf['name'] == workflow or wf['filename'] == workflow:
            current_wf = wf
            break

    if not current_wf:
        raise FileNotFoundError(f"Workflow '{workflow}' not found in skill '{skill_name}'")

    variant = Path(variant_path)
    if not variant.exists():
        raise FileNotFoundError(f"Variant not found: {variant_path}")

    current_content = Path(current_wf['path']).read_text()
    variant_content = variant.read_text()

    return {
        'skill': skill_name,
        'workflow': workflow,
        'current_path': current_wf['path'],
        'variant_path': str(variant),
        'current_lines': len(current_content.splitlines()),
        'variant_lines': len(variant_content.splitlines()),
        'size_delta': len(variant_content) - len(current_content),
        'status': 'ready_for_review',
        'instructions': (
            'To test this variant:\n'
            '1. Run the variant against benchmark tasks\n'
            '2. Score outputs using quality gate (directives/quality_gate.md)\n'
            '3. Compare scores against current workflow baseline\n'
            '4. If variant wins → replace current + log to Evolution Log\n'
            '5. If variant loses → discard + log the attempt'
        ),
    }


def generate_evolution_report(skill_name: str) -> str:
    """Generate a markdown evolution report for a skill."""
    report = benchmark_skill(skill_name)
    perf = report['performance']

    lines = [
        f"# Evolution Report: {skill_name}",
        f"*Generated: {date.today().isoformat()}*",
        "",
        "## Performance Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Entries | {perf['entries']} |",
        f"| Avg Quality | {perf['avg_quality']}/10 |",
        f"| Avg Intent Alignment | {perf['avg_intent']}/10 |",
        f"| Avg Expert Standard | {perf['avg_expert']}/10 |",
        f"| Avg Adversarial Resilience | {perf['avg_adversarial']}/10 |",
        f"| Trend | {perf['trend']} |",
        "",
        "## Workflows",
        "",
    ]

    for wf in report['workflows']:
        lines.append(f"- {wf}")
    lines.append("")

    if report['weakest_workflow']:
        lines.append(f"**Weakest Workflow**: {report['weakest_workflow']} (avg {report.get('weakest_workflow_avg', '?')}/10)")
        lines.append("")

    if report['weakest_dimension']:
        lines.append(f"**Weakest Dimension**: {report['weakest_dimension']}")
        lines.append("")

    lines.append("## Benchmark Tasks")
    lines.append("")
    for i, task in enumerate(report['benchmark_tasks'], 1):
        lines.append(f"{i}. {task}")
    lines.append("")

    lines.append("## Recommendations")
    lines.append("")
    for rec in report['recommendations']:
        lines.append(f"- {rec}")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Skill Benchmark CLI')
    sub = parser.add_subparsers(dest='command')

    # benchmark
    bm = sub.add_parser('benchmark', help='Benchmark a skill')
    bm.add_argument('skill', help='Skill directory name')

    # compare
    cmp = sub.add_parser('compare', help='Compare workflow variant')
    cmp.add_argument('skill', help='Skill directory name')
    cmp.add_argument('workflow', help='Workflow name')
    cmp.add_argument('variant', help='Path to variant workflow file')

    # report
    rpt = sub.add_parser('report', help='Generate evolution report')
    rpt.add_argument('skill', help='Skill directory name')

    args = parser.parse_args()

    if args.command == 'benchmark':
        result = benchmark_skill(args.skill)
        print(json.dumps(result, indent=2))

    elif args.command == 'compare':
        result = compare_variants(args.skill, args.workflow, args.variant)
        print(json.dumps(result, indent=2))

    elif args.command == 'report':
        print(generate_evolution_report(args.skill))

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
