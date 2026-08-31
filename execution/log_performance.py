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

# Local-first mirror (2026-07-15). session_log_registrar and
# activation_governor were written against get_local_performance_entries /
# get_sync_summary, but no local store ever existed — the registrar
# import-crashed on every run and skill-evolution "local history" was
# permanently zero. Every log_output call now lands here FIRST; Notion is the
# sync target, not the source of truth.
LOCAL_LOG_PATH = Path(__file__).parent.parent / '.agent' / 'performance-log.jsonl'


def _append_local(entry: dict) -> None:
    LOCAL_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOCAL_LOG_PATH.open('a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def get_local_performance_entries() -> list:
    """All locally-mirrored performance entries (oldest first)."""
    try:
        return [json.loads(l) for l in LOCAL_LOG_PATH.read_text().splitlines() if l.strip()]
    except FileNotFoundError:
        return []


def get_sync_summary() -> dict:
    """Counts by Notion-sync state for the local mirror."""
    entries = get_local_performance_entries()
    by = lambda s: sum(1 for e in entries if e.get('sync') == s)  # noqa: E731
    return {
        'total': len(entries),
        'remote_synced': by('synced'),
        'pending': by('pending'),
        'sync_failed': by('failed'),
        'local_first': len(entries),
    }


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
    lane: str = '',
    source_artifact: str = '',
    registration_source: str = '',
    auto_confidence: Optional[float] = None,
    review_state: str = '',
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

    local_entry = {
        'date': date.today().isoformat(),
        'output': output, 'agent': agent, 'skill': skill, 'workflow': workflow,
        'task_type': task_type, 'quality_score': quality_score,
        'user_rating': user_rating, 'intent_alignment': intent_alignment,
        'expert_standard': expert_standard,
        'adversarial_resilience': adversarial_resilience,
        'status': status, 'notes': notes, 'experiment_tag': experiment_tag,
        'lane': lane, 'source_artifact': source_artifact,
        'registration_source': registration_source,
        'auto_confidence': auto_confidence, 'review_state': review_state,
    }
    try:
        page = api.create_page(PERFORMANCE_DB_ID, props)
        local_entry['sync'] = 'synced'
        _append_local(local_entry)
        return page
    except Exception:
        # Notion down/misconfigured must never lose the entry — mirror it
        # locally as failed, then surface the original error to the caller.
        local_entry['sync'] = 'failed'
        _append_local(local_entry)
        raise


def get_baseline(
    skill: Optional[str] = None,
    agent: Optional[str] = None,
    window: int = 10,
) -> dict:
    """
    Get the rolling baseline from the local-first performance ledger.

    Notion is the sync target, not the runtime source of truth. Regression
    checks run during every finalize, including sandboxed Codex runs that may
    not have DNS access to api.notion.com. Reading the append-only local ledger
    keeps regression detection available without making Notion a critical-path
    dependency.

    Returns: {
        'count': int,
        'avg_quality': float,
        'avg_intent': float,
        'avg_expert': float,
        'avg_adversarial': float,
        'keep_rate': float,  # % of outputs marked 'Keep'
    }
    """
    entries = get_local_performance_entries()
    if skill:
        entries = [e for e in entries if skill.lower() in str(e.get('skill', '')).lower()]
    if agent:
        entries = [e for e in entries if agent.lower() in str(e.get('agent', '')).lower()]
    entries = entries[-window:]

    if not entries:
        return {
            'count': 0, 'avg_quality': 0, 'avg_intent': 0,
            'avg_expert': 0, 'avg_adversarial': 0, 'keep_rate': 0,
            'source': 'local_performance_ledger',
        }

    quality_scores = [e.get('quality_score') for e in entries if e.get('quality_score') is not None]
    intent_scores = [e.get('intent_alignment') for e in entries if e.get('intent_alignment') is not None]
    expert_scores = [e.get('expert_standard') for e in entries if e.get('expert_standard') is not None]
    adversarial_scores = [e.get('adversarial_resilience') for e in entries if e.get('adversarial_resilience') is not None]
    statuses = [e.get('status') for e in entries]

    keep_count = sum(1 for s in statuses if s == 'Keep')

    return {
        'count': len(entries),
        'avg_quality': sum(quality_scores) / len(quality_scores) if quality_scores else 0,
        'avg_intent': sum(intent_scores) / len(intent_scores) if intent_scores else 0,
        'avg_expert': sum(expert_scores) / len(expert_scores) if expert_scores else 0,
        'avg_adversarial': sum(adversarial_scores) / len(adversarial_scores) if adversarial_scores else 0,
        'keep_rate': keep_count / len(entries) if entries else 0,
        'source': 'local_performance_ledger',
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
