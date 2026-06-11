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
from datetime import date, datetime
from typing import Optional
from pathlib import Path
try:
    import bootstrap
except ModuleNotFoundError:
    from execution import bootstrap
from dotenv import load_dotenv

# Load .env
for env_path in [
    Path(__file__).parent.parent / 'jarvis-bot' / '.env',
    Path(__file__).parent.parent / '.env',
]:
    if env_path.exists():
        load_dotenv(env_path)

# Import the shared Notion API wrapper
try:
    from notion_api import NotionAPI, NotionAPIError
except ModuleNotFoundError:
    from execution.notion_api import NotionAPI, NotionAPIError

PERFORMANCE_DB_ID = os.getenv(
    'NOTION_DB_PERFORMANCE',
    '31f49875a89781dbb599dee5e7961b5c'
)

ROOT = Path(__file__).parent.parent
LOCAL_PERFORMANCE_LOG = ROOT / '.agent' / 'performance-log.jsonl'


def _local_entry(
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
    lane: str = 'Unknown',
    source_artifact: str = '',
    registration_source: str = 'manual',
    auto_confidence: Optional[float] = None,
    review_state: str = 'committed',
) -> dict:
    """Build the local source-of-truth performance entry."""
    timestamp = datetime.now().isoformat(timespec='seconds')
    return {
        'Local ID': f'pl_{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}',
        'Output': output,
        'Date': date.today().isoformat(),
        'Timestamp': timestamp,
        'Agent': agent,
        'Skill': skill,
        'Workflow': workflow,
        'Task Type': task_type,
        'Quality Score': quality_score,
        'User Rating': user_rating,
        'Intent Alignment': intent_alignment,
        'Expert Standard': expert_standard,
        'Adversarial Resilience': adversarial_resilience,
        'Status': status,
        'Notes': notes,
        'Experiment Tag': experiment_tag,
        'Lane': lane,
        'Source Artifact': source_artifact,
        'Registration Source': registration_source,
        'Auto Confidence': auto_confidence,
        'Review State': review_state,
        'Notion URL': '',
        'Sync Status': 'local-first',
        'Sync Error': '',
    }


def _append_local_entry(entry: dict) -> str:
    """Append a performance entry locally so feedback survives network failures."""
    LOCAL_PERFORMANCE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOCAL_PERFORMANCE_LOG.open('a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    return entry['Local ID']


def _write_local_performance_entries(entries: list[dict]) -> None:
    """Rewrite the local JSONL log after updating sync metadata."""
    LOCAL_PERFORMANCE_LOG.parent.mkdir(parents=True, exist_ok=True)
    text = ''.join(json.dumps(entry, ensure_ascii=False) + '\n' for entry in entries)
    LOCAL_PERFORMANCE_LOG.write_text(text, encoding='utf-8')


def _update_local_entry(local_id: str, updates: dict) -> bool:
    """Patch one local entry by Local ID. Returns True when an entry was updated."""
    if not LOCAL_PERFORMANCE_LOG.exists():
        return False

    changed = False
    entries: list[dict] = []
    for line in LOCAL_PERFORMANCE_LOG.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            entries.append({'Raw Corrupt Line': line})
            continue
        if entry.get('Local ID') == local_id:
            entry.update(updates)
            changed = True
        entries.append(entry)

    if changed:
        _write_local_performance_entries(entries)
    return changed


def get_local_performance_entries(
    skill: Optional[str] = None,
    agent: Optional[str] = None,
    window: Optional[int] = None,
) -> list[dict]:
    """Read local performance entries, newest first."""
    if not LOCAL_PERFORMANCE_LOG.exists():
        return []

    entries: list[dict] = []
    for line in LOCAL_PERFORMANCE_LOG.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if skill and skill not in str(entry.get('Skill', '')):
            continue
        if agent and agent not in str(entry.get('Agent', '')):
            continue
        entries.append(entry)

    entries.sort(key=lambda e: (e.get('Date', ''), e.get('Timestamp', '')), reverse=True)
    if window is not None:
        return entries[:window]
    return entries


def _props_from_entry(api: NotionAPI, entry: dict) -> dict:
    """Build Notion Performance Log properties from a local entry."""
    props = {
        'Output': api.title(str(entry.get('Output', 'Untitled'))),
        'Date': api.date(str(entry.get('Date') or date.today().isoformat())),
        'Status': api.select(str(entry.get('Status') or 'Keep')),
    }

    text_fields = {
        'Agent': entry.get('Agent'),
        'Skill': entry.get('Skill'),
        'Workflow': entry.get('Workflow'),
        'Notes': entry.get('Notes'),
        'Experiment Tag': entry.get('Experiment Tag'),
    }
    for name, value in text_fields.items():
        if value:
            props[name] = api.rich_text(str(value))

    if entry.get('Task Type'):
        props['Task Type'] = api.select(str(entry.get('Task Type')))

    number_fields = [
        'Quality Score',
        'User Rating',
        'Intent Alignment',
        'Expert Standard',
        'Adversarial Resilience',
    ]
    for name in number_fields:
        value = entry.get(name)
        if isinstance(value, (int, float)):
            props[name] = api.number(float(value))

    return props


def _notion_title_filter(output: str, entry_date: str) -> dict:
    return {
        'and': [
            {'property': 'Output', 'title': {'equals': output}},
            {'property': 'Date', 'date': {'equals': entry_date}},
        ]
    }


def _find_existing_remote_entry(api: NotionAPI, entry: dict) -> Optional[str]:
    """Return an existing Notion URL for the same Output + Date, if present."""
    output = str(entry.get('Output') or '')
    entry_date = str(entry.get('Date') or '')
    if not output or not entry_date:
        return None

    result = api.query_database(
        PERFORMANCE_DB_ID,
        filter=_notion_title_filter(output, entry_date),
        page_size=1,
    )
    pages = result.get('results', [])
    if not pages:
        return None
    return pages[0].get('url')


def _needs_remote_sync(entry: dict) -> bool:
    status = str(entry.get('Sync Status') or '').lower()
    notion_url = str(entry.get('Notion URL') or '')
    if notion_url.startswith('https://'):
        return False
    return status in {'', 'local-first', 'pending', 'sync-failed'}


def get_sync_summary() -> dict:
    """Summarize local Performance Log remote sync state."""
    entries = get_local_performance_entries()
    summary = {
        'total': len(entries),
        'remote_synced': 0,
        'pending': 0,
        'sync_failed': 0,
        'local_first': 0,
    }
    for entry in entries:
        status = str(entry.get('Sync Status') or 'local-first').lower()
        if status == 'remote-synced' or str(entry.get('Notion URL') or '').startswith('https://'):
            summary['remote_synced'] += 1
        elif status == 'sync-failed':
            summary['sync_failed'] += 1
        elif status == 'pending':
            summary['pending'] += 1
        else:
            summary['local_first'] += 1
    return summary


def sync_pending_entries(limit: int = 10, dry_run: bool = True) -> dict:
    """Sync local-first Performance Log entries to Notion with duplicate protection."""
    entries = get_local_performance_entries()
    pending = [entry for entry in reversed(entries) if _needs_remote_sync(entry)]
    if limit:
        pending = pending[:limit]

    summary = {
        'dry_run': dry_run,
        'checked': len(pending),
        'would_sync': 0,
        'synced': 0,
        'deduped': 0,
        'failed': 0,
        'entries': [],
    }

    if dry_run:
        for entry in pending:
            summary['would_sync'] += 1
            summary['entries'].append({
                'local_id': entry.get('Local ID'),
                'output': entry.get('Output'),
                'date': entry.get('Date'),
                'sync_status': entry.get('Sync Status', 'local-first'),
            })
        return summary

    api = NotionAPI()
    for entry in pending:
        local_id = entry.get('Local ID')
        item = {
            'local_id': local_id,
            'output': entry.get('Output'),
            'date': entry.get('Date'),
            'action': '',
            'url': '',
            'error': '',
        }
        try:
            existing_url = _find_existing_remote_entry(api, entry)
            if existing_url:
                _update_local_entry(str(local_id), {
                    'Notion URL': existing_url,
                    'Sync Status': 'remote-synced',
                    'Sync Error': '',
                })
                summary['deduped'] += 1
                item['action'] = 'matched-existing'
                item['url'] = existing_url
            else:
                result = api.create_page(PERFORMANCE_DB_ID, _props_from_entry(api, entry))
                notion_url = result.get('url', '')
                _update_local_entry(str(local_id), {
                    'Notion URL': notion_url,
                    'Sync Status': 'remote-synced',
                    'Sync Error': '',
                })
                summary['synced'] += 1
                item['action'] = 'created'
                item['url'] = notion_url
        except Exception as e:
            _update_local_entry(str(local_id), {
                'Sync Status': 'sync-failed',
                'Sync Error': str(e),
            })
            summary['failed'] += 1
            item['action'] = 'failed'
            item['error'] = str(e)
        summary['entries'].append(item)

    return summary


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
    lane: str = 'Unknown',
    source_artifact: str = '',
    registration_source: str = 'manual',
    auto_confidence: Optional[float] = None,
    review_state: str = 'committed',
    sync_remote: bool = True,
) -> dict:
    """Log a performance entry locally first, then sync to Notion if available."""
    entry = _local_entry(
        output=output,
        agent=agent,
        skill=skill,
        workflow=workflow,
        task_type=task_type,
        quality_score=quality_score,
        user_rating=user_rating,
        intent_alignment=intent_alignment,
        expert_standard=expert_standard,
        adversarial_resilience=adversarial_resilience,
        status=status,
        notes=notes,
        experiment_tag=experiment_tag,
        lane=lane,
        source_artifact=source_artifact,
        registration_source=registration_source,
        auto_confidence=auto_confidence,
        review_state=review_state,
    )
    local_id = _append_local_entry(entry)

    if not sync_remote:
        return {
            'url': f'local://{local_id}',
            'local_id': local_id,
            'local_path': str(LOCAL_PERFORMANCE_LOG),
            'sync_status': 'local-first',
            'notion_url': '',
        }

    try:
        api = NotionAPI()
        result = api.create_page(PERFORMANCE_DB_ID, _props_from_entry(api, entry))
        notion_url = result.get('url', '')
        _update_local_entry(local_id, {
            'Notion URL': notion_url,
            'Sync Status': 'remote-synced',
            'Sync Error': '',
        })
        result['local_id'] = local_id
        result['local_path'] = str(LOCAL_PERFORMANCE_LOG)
        result['sync_status'] = 'remote-synced'
        result['notion_url'] = notion_url
        return result
    except Exception as e:
        _update_local_entry(local_id, {
            'Sync Status': 'sync-failed',
            'Sync Error': str(e),
        })
        return {
            'url': f'local://{local_id}',
            'local_id': local_id,
            'local_path': str(LOCAL_PERFORMANCE_LOG),
            'sync_status': 'sync-failed',
            'notion_error': str(e),
        }


def _baseline_from_entries(entries: list[dict]) -> dict:
    if not entries:
        return {'count': 0, 'avg_quality': 0, 'avg_intent': 0, 'avg_expert': 0, 'avg_adversarial': 0, 'keep_rate': 0, 'source': 'local'}

    def number(entry, prop_name):
        value = entry.get(prop_name)
        return value if isinstance(value, (int, float)) else None

    quality_scores = [s for s in (number(e, 'Quality Score') for e in entries) if s is not None]
    intent_scores = [s for s in (number(e, 'Intent Alignment') for e in entries) if s is not None]
    expert_scores = [s for s in (number(e, 'Expert Standard') for e in entries) if s is not None]
    adversarial_scores = [s for s in (number(e, 'Adversarial Resilience') for e in entries) if s is not None]
    keep_count = sum(1 for e in entries if e.get('Status') == 'Keep')

    return {
        'count': len(entries),
        'avg_quality': sum(quality_scores) / len(quality_scores) if quality_scores else 0,
        'avg_intent': sum(intent_scores) / len(intent_scores) if intent_scores else 0,
        'avg_expert': sum(expert_scores) / len(expert_scores) if expert_scores else 0,
        'avg_adversarial': sum(adversarial_scores) / len(adversarial_scores) if adversarial_scores else 0,
        'keep_rate': keep_count / len(entries) if entries else 0,
        'source': 'local',
    }


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
    local_entries = get_local_performance_entries(skill=skill, agent=agent, window=window)

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

    try:
        api = NotionAPI()
        sorts = [{'property': 'Date', 'direction': 'descending'}]
        result = api.query_database(PERFORMANCE_DB_ID, filter=query_filter, sorts=sorts, page_size=window)
        pages = result.get('results', [])
    except Exception:
        return _baseline_from_entries(local_entries)

    if not pages:
        return _baseline_from_entries(local_entries)

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
        'source': 'notion',
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
    log.add_argument('--lane', default='Unknown', help='Client/Personal/System/Creative/Research/Unknown')
    log.add_argument('--source-artifact', default='', help='Path or report that produced the entry')
    log.add_argument('--registration-source', default='manual', help='manual/end-session/daily-backfill/system-governor')
    log.add_argument('--auto-confidence', type=float, help='Auto-registration confidence 0-1')
    log.add_argument('--review-state', default='committed', help='committed/inbox/promoted/skipped')
    log.add_argument('--local-only', action='store_true', help='Append locally without attempting Notion sync')

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

    # sync-pending
    sp = sub.add_parser('sync-pending', help='Sync local-first entries to Notion with duplicate protection')
    sp.add_argument('--limit', type=int, default=10, help='Max entries to inspect/sync')
    sp.add_argument('--dry-run', action='store_true', help='List pending entries without writing to Notion')
    sp.add_argument('--json', action='store_true', help='Print machine-readable JSON')

    # sync-status
    sub.add_parser('sync-status', help='Summarize local Performance Log sync state')

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
            lane=args.lane,
            source_artifact=args.source_artifact,
            registration_source=args.registration_source,
            auto_confidence=args.auto_confidence,
            review_state=args.review_state,
            sync_remote=not args.local_only,
        )
        print(f'  Logged: {result["url"]}')

    elif args.command == 'baseline':
        result = get_baseline(skill=args.skill or None, agent=args.agent or None, window=args.window)
        print(f'  Baseline ({result["count"]} entries):')
        print(f'    Source:           {result.get("source", "notion")}')
        print(f'    Avg Quality:      {result["avg_quality"]:.1f}')
        print(f'    Avg Intent:       {result["avg_intent"]:.1f}')
        print(f'    Avg Expert:       {result["avg_expert"]:.1f}')
        print(f'    Avg Adversarial:  {result["avg_adversarial"]:.1f}')
        print(f'    Keep Rate:        {result["keep_rate"]:.0%}')

    elif args.command == 'check':
        result = check_regression(skill=args.skill or None, agent=args.agent or None, latest_score=args.score)
        print(f'  {result["message"]}')

    elif args.command == 'sync-pending':
        result = sync_pending_entries(limit=args.limit, dry_run=args.dry_run)
        if args.json:
            print(json.dumps(result, indent=2))
        elif args.dry_run:
            print(f'  Pending local entries: {result["would_sync"]}')
            for item in result['entries']:
                print(f'    {item["local_id"]}: {item["output"]} ({item["sync_status"]})')
        else:
            print('  Sync pending complete:')
            print(f'    Created:          {result["synced"]}')
            print(f'    Matched existing: {result["deduped"]}')
            print(f'    Failed:           {result["failed"]}')
            for item in result['entries']:
                target = item.get('url') or item.get('error', '')
                print(f'    {item["action"]}: {item["local_id"]} {target}')

    elif args.command == 'sync-status':
        result = get_sync_summary()
        print('  Performance Log Sync:')
        print(f'    Total local:     {result["total"]}')
        print(f'    Remote synced:   {result["remote_synced"]}')
        print(f'    Pending:         {result["pending"]}')
        print(f'    Sync failed:     {result["sync_failed"]}')
        print(f'    Local-first:     {result["local_first"]}')

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
