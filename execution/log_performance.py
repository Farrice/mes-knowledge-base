#!/usr/bin/env python3
"""
Performance Log — Autoresearch-inspired feedback ratchet for Antigravity.

Logs quality signals to the Performance Log Notion database after every
significant output. Over time, this creates per-agent/skill/workflow
baselines that enable the skill evolution engine (Phase 2).

Usage:
    from execution.log_performance import log_output, get_baseline, check_regression

    # Log a completed output
    log_output(
        output="Strategy brief for SaaS positioning",
        agent="cardinal-mason",
        skill="cardinal-mason-ai-copywriting",
        workflow="01-client-acquisition",
        task_type="Strategy",
        quality_score=8,
        intent_alignment=9,
        expert_standard=7,
        adversarial_resilience=8,
        status="Keep",
        notes="Strong hook section, weak CTA"
    )

    # Get rolling baseline for a skill
    baseline = get_baseline(skill="cardinal-mason-ai-copywriting")

    # Check for regression
    regression = check_regression(skill="cardinal-mason-ai-copywriting", latest_score=5)

CLI usage:
    python execution/log_performance.py log "Brief title" --agent cardinal-mason --skill cardinal-mason-ai-copywriting --workflow 01-client-acquisition --type Strategy --quality 8 --status Keep
    python execution/log_performance.py baseline --skill cardinal-mason-ai-copywriting
    python execution/log_performance.py check --skill cardinal-mason-ai-copywriting --score 5
"""

import os
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

# Import the shared Notion API wrapper
from notion_api import NotionAPI, NotionAPIError

PERFORMANCE_DB_ID = os.getenv(
    'NOTION_DB_PERFORMANCE',
    '31f49875a89781dbb599dee5e7961b5c'
)


def log_output(
    output: str,
    agent: str = '',
    skill: str = '',
    workflow: str = '',
    task_type: str = 'System',
    quality_score: Optional[float] = None,
    user_rating: Optional[float] = None,
    intent_alignment: Optional[float] = None,
    expert_standard: Optional[float] = None,
    adversarial_resilience: Optional[float] = None,
    status: str = 'Keep',
    notes: str = '',
    experiment_tag: str = '',
) -> dict:
    """Log a performance entry to the Performance Log database."""
    api = NotionAPI()
    props = {
        'Output': api.title(output),
        'Date': api.date(date.today().isoformat()),
        'Status': api.select(status),
    }
    if agent:
        props['Agent'] = api.rich_text(agent)
    if skill:
        props['Skill'] = api.rich_text(skill)
    if workflow:
        props['Workflow'] = api.rich_text(workflow)
    if task_type:
        props['Task Type'] = api.select(task_type)
    if quality_score is not None:
        props['Quality Score'] = api.number(quality_score)
    if user_rating is not None:
        props['User Rating'] = api.number(user_rating)
    if intent_alignment is not None:
        props['Intent Alignment'] = api.number(intent_alignment)
    if expert_standard is not None:
        props['Expert Standard'] = api.number(expert_standard)
    if adversarial_resilience is not None:
        props['Adversarial Resilience'] = api.number(adversarial_resilience)
    if notes:
        props['Notes'] = api.rich_text(notes)
    if experiment_tag:
        props['Experiment Tag'] = api.rich_text(experiment_tag)

    return api.create_page(PERFORMANCE_DB_ID, props)


def get_baseline(
    skill: Optional[str] = None,
    agent: Optional[str] = None,
    window: int = 10,
) -> dict:
    """
    Get rolling baseline (last N outputs) for a skill or agent.

    Returns: {
        'count': int,
        'avg_quality': float,
        'avg_intent': float,
        'avg_expert': float,
        'avg_adversarial': float,
        'keep_rate': float,  # % of outputs marked 'Keep'
    }
    """
    api = NotionAPI()

    # Build filter — Notion 2022-06-28 filter syntax
    filters = []
    if skill:
        filters.append({
            'property': 'Skill',
            'rich_text': {'contains': skill}
        })
    if agent:
        filters.append({
            'property': 'Agent',
            'rich_text': {'contains': agent}
        })

    query_filter = None
    if len(filters) == 1:
        query_filter = filters[0]
    elif len(filters) > 1:
        query_filter = {'and': filters}

    sorts = [{'property': 'Date', 'direction': 'descending'}]
    result = api.query_database(PERFORMANCE_DB_ID, filter=query_filter, sorts=sorts, page_size=window)
    pages = result.get('results', [])

    if not pages:
        return {'count': 0, 'avg_quality': 0, 'avg_intent': 0, 'avg_expert': 0, 'avg_adversarial': 0, 'keep_rate': 0}

    def extract_number(page, prop_name):
        prop = page.get('properties', {}).get(prop_name, {})
        return prop.get('number') if prop.get('type') == 'number' else None

    def extract_select(page, prop_name):
        prop = page.get('properties', {}).get(prop_name, {})
        sel = prop.get('select')
        return sel.get('name') if sel else None

    quality_scores = [s for s in (extract_number(p, 'Quality Score') for p in pages) if s is not None]
    intent_scores = [s for s in (extract_number(p, 'Intent Alignment') for p in pages) if s is not None]
    expert_scores = [s for s in (extract_number(p, 'Expert Standard') for p in pages) if s is not None]
    adversarial_scores = [s for s in (extract_number(p, 'Adversarial Resilience') for p in pages) if s is not None]
    statuses = [extract_select(p, 'Status') for p in pages]

    keep_count = sum(1 for s in statuses if s == 'Keep')

    return {
        'count': len(pages),
        'avg_quality': sum(quality_scores) / len(quality_scores) if quality_scores else 0,
        'avg_intent': sum(intent_scores) / len(intent_scores) if intent_scores else 0,
        'avg_expert': sum(expert_scores) / len(expert_scores) if expert_scores else 0,
        'avg_adversarial': sum(adversarial_scores) / len(adversarial_scores) if adversarial_scores else 0,
        'keep_rate': keep_count / len(pages) if pages else 0,
    }


def check_regression(
    skill: Optional[str] = None,
    agent: Optional[str] = None,
    latest_score: float = 0,
    threshold: float = 1.0,
) -> dict:
    """
    Check if a latest score represents a regression from the rolling baseline.

    Returns: {
        'is_regression': bool,
        'baseline_avg': float,
        'delta': float,
        'message': str,
    }
    """
    baseline = get_baseline(skill=skill, agent=agent)
    avg = baseline['avg_quality']

    if baseline['count'] < 3:
        return {
            'is_regression': False,
            'baseline_avg': avg,
            'delta': 0,
            'message': f'Insufficient data ({baseline["count"]} entries). Need 3+ for regression detection.',
        }

    delta = latest_score - avg
    is_regression = delta < -threshold

    if is_regression:
        msg = f'REGRESSION: Score {latest_score} is {abs(delta):.1f} below baseline {avg:.1f}. Review skill for degradation.'
    elif delta > threshold:
        msg = f'IMPROVEMENT: Score {latest_score} is {delta:.1f} above baseline {avg:.1f}. Consider propagating improvement.'
    else:
        msg = f'STABLE: Score {latest_score} is within {threshold} of baseline {avg:.1f}.'

    return {
        'is_regression': is_regression,
        'baseline_avg': avg,
        'delta': delta,
        'message': msg,
    }


def main():
    parser = argparse.ArgumentParser(description='Performance Log CLI')
    sub = parser.add_subparsers(dest='command')

    # log
    log = sub.add_parser('log', help='Log a performance entry')
    log.add_argument('output', help='Output title/description')
    log.add_argument('--agent', default='', help='Agent name')
    log.add_argument('--skill', default='', help='Skill name')
    log.add_argument('--workflow', default='', help='Workflow name')
    log.add_argument('--type', default='System', help='Task type')
    log.add_argument('--quality', type=float, help='Quality score (1-10)')
    log.add_argument('--rating', type=float, help='User rating (1-10)')
    log.add_argument('--intent', type=float, help='Intent alignment (1-10)')
    log.add_argument('--expert', type=float, help='Expert standard (1-10)')
    log.add_argument('--adversarial', type=float, help='Adversarial resilience (1-10)')
    log.add_argument('--status', default='Keep', help='Keep/Discard/Needs Improvement/Baseline')
    log.add_argument('--notes', default='', help='Freeform notes')
    log.add_argument('--tag', default='', help='Experiment tag')

    # baseline
    bl = sub.add_parser('baseline', help='Get rolling baseline')
    bl.add_argument('--skill', default='', help='Filter by skill')
    bl.add_argument('--agent', default='', help='Filter by agent')
    bl.add_argument('--window', type=int, default=10, help='Rolling window size')

    # check
    ch = sub.add_parser('check', help='Check for regression')
    ch.add_argument('--skill', default='', help='Filter by skill')
    ch.add_argument('--agent', default='', help='Filter by agent')
    ch.add_argument('--score', type=float, required=True, help='Latest quality score')

    args = parser.parse_args()

    if args.command == 'log':
        result = log_output(
            output=args.output,
            agent=args.agent,
            skill=args.skill,
            workflow=args.workflow,
            task_type=args.type,
            quality_score=args.quality,
            user_rating=args.rating,
            intent_alignment=args.intent,
            expert_standard=args.expert,
            adversarial_resilience=args.adversarial,
            status=args.status,
            notes=args.notes,
            experiment_tag=args.tag,
        )
        print(f'  Logged: {result["url"]}')

    elif args.command == 'baseline':
        result = get_baseline(skill=args.skill or None, agent=args.agent or None, window=args.window)
        print(f'  Baseline ({result["count"]} entries):')
        print(f'    Avg Quality:      {result["avg_quality"]:.1f}')
        print(f'    Avg Intent:       {result["avg_intent"]:.1f}')
        print(f'    Avg Expert:       {result["avg_expert"]:.1f}')
        print(f'    Avg Adversarial:  {result["avg_adversarial"]:.1f}')
        print(f'    Keep Rate:        {result["keep_rate"]:.0%}')

    elif args.command == 'check':
        result = check_regression(skill=args.skill or None, agent=args.agent or None, latest_score=args.score)
        print(f'  {result["message"]}')

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
