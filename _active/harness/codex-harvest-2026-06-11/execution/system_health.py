#!/usr/bin/env python3
"""
System Health Check — Antigravity Activation Monitor

Checks which Antigravity systems are actively firing vs dormant.
Unlike system_audit.py (which checks structural integrity), this checks
whether the feedback loop is actually producing data.

Usage:
    python execution/system_health.py           # Full health report
    python execution/system_health.py --quick   # Summary only

Reports on:
- Performance Log entries (Phase 1: Feedback Ratchet)
- Skill Evolution readiness (Phase 2: needs 20+ entries)
- Cross-Pollination readiness (Phase 3: needs evolution data)
- Gap Detection readiness (Phase 4: needs pattern data)
- Hookify guard status
- Session state freshness
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, date, timedelta

# Load .env
import bootstrap
from dotenv import load_dotenv
for env_path in [
    Path(__file__).parent.parent / '.env',
]:
    if env_path.exists():
        load_dotenv(env_path)

# Import the shared Notion API wrapper
sys.path.insert(0, str(Path(__file__).parent))
from notion_api import NotionAPI, NotionAPIError, status_payload
from log_performance import LOCAL_PERFORMANCE_LOG, get_local_performance_entries, get_sync_summary

ROOT = Path(__file__).parent.parent
CLAUDE_DIR = ROOT / ".claude"
AGENT_DIR = ROOT / ".agent"
DIRECTIVES_DIR = ROOT / "directives"
OUTPUT_DIR = ROOT / ".tmp"

PERFORMANCE_DB_ID = os.getenv(
    'NOTION_DB_PERFORMANCE',
    '31f49875a89781dbb599dee5e7961b5c'
)


def check_performance_log():
    """Query Performance Log DB, falling back to local-first evidence."""
    local_entries = get_local_performance_entries()
    sync = get_sync_summary()

    def summarize_entries(entries, source):
        if not entries:
            return {
                'status': 'DORMANT',
                'health': 'Critical',
                'count': 0,
                'last_date': 'Never',
                'message': 'Zero entries. The feedback loop has never fired.',
                'source': source,
                'sync': sync,
            }

        last_date_raw = entries[0].get('Date', '') or entries[0].get('Timestamp', '')[:10]
        try:
            last_dt = datetime.strptime(last_date_raw[:10], '%Y-%m-%d').date()
            days_ago = (date.today() - last_dt).days
            recency = f'{days_ago} days ago' if days_ago > 0 else 'Today'
        except (ValueError, TypeError):
            recency = last_date_raw or 'Unknown'
            days_ago = 999

        count = len(entries)
        if count >= 20 and days_ago <= 7:
            health = 'Healthy'
            status = 'ACTIVE'
        elif count >= 5:
            health = 'Growing'
            status = 'ACTIVE'
        elif count > 0:
            health = 'Starting'
            status = 'ACTIVE'
        else:
            health = 'Critical'
            status = 'DORMANT'

        return {
            'status': status,
            'health': health,
            'count': count,
            'last_date': recency,
            'message': (
                f'{count} entries from {source}. Last: {recency}. '
                f'Sync: {sync["remote_synced"]} remote, '
                f'{sync["pending"] + sync["local_first"]} pending/local-first, '
                f'{sync["sync_failed"]} failed.'
            ),
            'source': source,
            'sync': sync,
        }

    try:
        api = NotionAPI()
        sorts = [{'property': 'Date', 'direction': 'descending'}]
        result = api.query_database(PERFORMANCE_DB_ID, sorts=sorts, page_size=100)
        pages = result.get('results', [])

        if not pages:
            return summarize_entries(local_entries, 'local')

        entries = []
        for page in pages:
            props = page.get('properties', {})
            date_prop = props.get('Date', {})
            entry_date = ''
            if date_prop.get('type') == 'date' and date_prop.get('date'):
                entry_date = date_prop['date'].get('start', '')
            entries.append({'Date': entry_date})

        return summarize_entries(entries, 'notion')
    except Exception as e:
        if local_entries:
            result = summarize_entries(local_entries, 'local')
            result['message'] += f' Notion unavailable: {e}'
            return result
        result = summarize_entries([], 'local')
        result['message'] += f' Notion unavailable and no local log at {LOCAL_PERFORMANCE_LOG}.'
        return result


def check_hookify_hooks():
    """List all hookify hooks and their status."""
    hooks = []
    if not CLAUDE_DIR.exists():
        return hooks

    for f in sorted(CLAUDE_DIR.iterdir()):
        if f.name.startswith('hookify.') and f.name.endswith('.md'):
            content = f.read_text(encoding='utf-8')
            # Parse frontmatter
            enabled = True
            event = 'unknown'
            action = 'unknown'
            name = f.stem.replace('hookify.', '').replace('.local', '')

            fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                fm = fm_match.group(1)
                for line in fm.split('\n'):
                    if line.strip().startswith('enabled:'):
                        enabled = 'true' in line.lower()
                    elif line.strip().startswith('event:'):
                        event = line.split(':', 1)[1].strip()
                    elif line.strip().startswith('action:'):
                        action = line.split(':', 1)[1].strip()
                    elif line.strip().startswith('name:'):
                        name = line.split(':', 1)[1].strip()

            hooks.append({
                'name': name,
                'enabled': enabled,
                'event': event,
                'action': action,
                'file': f.name,
            })

    return hooks


def check_session_state():
    """Check if session state file exists and is recent."""
    state_file = AGENT_DIR / 'session-state.md'
    if not state_file.exists():
        return {
            'status': 'DORMANT',
            'health': 'Warning',
            'message': 'No session-state.md found.',
        }

    mtime = datetime.fromtimestamp(state_file.stat().st_mtime)
    days_ago = (datetime.now() - mtime).days
    recency = f'{days_ago} days ago' if days_ago > 0 else 'Today'

    return {
        'status': 'ACTIVE' if days_ago <= 7 else 'STALE',
        'health': 'Healthy' if days_ago <= 1 else ('Warning' if days_ago <= 7 else 'Stale'),
        'message': f'Last updated: {recency} ({mtime.strftime("%Y-%m-%d %H:%M")})',
    }


def check_gap_log():
    """Check if gap log has entries."""
    gap_file = AGENT_DIR / 'gap-log.md'
    if not gap_file.exists():
        return {
            'status': 'DORMANT',
            'health': 'OK',
            'count': 0,
            'message': 'No gap-log.md found. Normal until gap detection runs.',
        }

    content = gap_file.read_text(encoding='utf-8')
    # Count entries (lines starting with ## or ### that look like gap entries)
    entries = len(re.findall(r'^##\s+', content, re.MULTILINE))
    if entries == 0:
        # Try counting list items
        entries = len(re.findall(r'^- \*\*', content, re.MULTILINE))

    return {
        'status': 'ACTIVE' if entries > 0 else 'DORMANT',
        'health': 'Healthy' if entries > 0 else 'OK',
        'count': entries,
        'message': f'{entries} gap entries logged.',
    }


def check_routing_intelligence():
    """Check routing intelligence log."""
    ri_file = AGENT_DIR / 'routing-intelligence.json'
    if not ri_file.exists():
        return {
            'status': 'DORMANT',
            'health': 'Warning',
            'count': 0,
            'message': 'No routing-intelligence.json found.',
        }

    try:
        data = json.loads(ri_file.read_text(encoding='utf-8'))
        entries = len(data) if isinstance(data, list) else len(data.get('routing_decisions', []))
        return {
            'status': 'ACTIVE' if entries > 0 else 'DORMANT',
            'health': 'Healthy' if entries > 0 else 'Warning',
            'count': entries,
            'message': f'{entries} routing decisions logged.',
        }
    except (json.JSONDecodeError, Exception) as e:
        return {
            'status': 'ERROR',
            'health': 'Error',
            'count': 0,
            'message': f'Could not read routing log: {e}',
        }


def check_skill_evolution_candidates():
    """Read or build the local-first Skill Evolution candidate snapshot."""
    try:
        from skill_evolution_candidates import build_snapshot, compact_status, load_snapshot

        snapshot = load_snapshot() or build_snapshot()
        summary = snapshot.get('summary', {})
        return {
            'status': 'ok',
            'summary': summary,
            'compact': compact_status(snapshot),
            'top': snapshot.get('top_recommendation') or {},
        }
    except Exception as e:
        return {
            'status': 'error',
            'summary': {'ready': 0, 'watchlist': 0, 'blocked': 0},
            'compact': f'candidate scan unavailable: {e}',
            'top': {},
        }


def generate_health_report(quick=False):
    """Generate the full health report."""
    print("Running Antigravity System Health Check...\n")

    # Run checks
    perf_log = check_performance_log()
    notion = status_payload(database='performance', limit=1)
    hooks = check_hookify_hooks()
    session = check_session_state()
    gap_log = check_gap_log()
    routing = check_routing_intelligence()
    evolution_candidates = check_skill_evolution_candidates()

    # Derive cascade status
    perf_count = perf_log.get('count', 0)
    phase2_ready = perf_count >= 20
    ready_candidates = int(evolution_candidates.get('summary', {}).get('ready', 0) or 0)
    watchlist_candidates = int(evolution_candidates.get('summary', {}).get('watchlist', 0) or 0)
    phase3_ready = False  # Would need to check evolution log
    phase4_ready = perf_count >= 5  # Can run with minimal data

    report = []
    report.append("# Antigravity System Health Report")
    report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("")

    # Activation Status Table
    report.append("## Activation Status")
    report.append("")
    report.append("| System | Status | Last Active | Entries | Health |")
    report.append("|--------|--------|-------------|---------|--------|")
    report.append(f"| Performance Log (Phase 1) | {perf_log['status']} | {perf_log['last_date']} | {perf_log['count']} | {perf_log['health']} |")

    if not phase2_ready:
        phase2_status = f'BLOCKED ({perf_count}/20 entries)'
        phase2_health = 'Waiting'
        phase2_entries = '—'
    elif ready_candidates:
        phase2_status = f'READY - {ready_candidates} candidates'
        phase2_health = 'Ready'
        phase2_entries = f'{ready_candidates} ready / {watchlist_candidates} watch'
    else:
        phase2_status = 'READY - collecting evidence'
        phase2_health = 'Collecting'
        phase2_entries = f'0 ready / {watchlist_candidates} watch'
    report.append(f"| Skill Evolution (Phase 2) | {phase2_status} | — | {phase2_entries} | {phase2_health} |")

    report.append(f"| Cross-Pollination (Phase 3) | {'READY' if phase3_ready else 'BLOCKED'} | — | — | {'Ready' if phase3_ready else 'Needs Phase 2'} |")

    report.append(f"| Gap Detection (Phase 4) | {'READY' if phase4_ready else 'BLOCKED'} | — | — | {'Ready' if phase4_ready else 'Needs data'} |")

    report.append(f"| Session State | {session['status']} | {session['message'].split(':', 1)[-1].strip() if ':' in session['message'] else '—'} | — | {session['health']} |")

    report.append(f"| Routing Intelligence | {routing['status']} | — | {routing.get('count', 0)} | {routing['health']} |")

    report.append(f"| Gap Log | {gap_log['status']} | — | {gap_log.get('count', 0)} | {gap_log['health']} |")
    report.append("")

    report.append("## Skill Evolution Candidates")
    report.append("")
    report.append(f"- {evolution_candidates.get('compact', 'candidate snapshot unavailable')}")
    top = evolution_candidates.get('top') or {}
    if top:
        report.append(f"- Top recommendation: `{top.get('skill')}` ({top.get('state')}) - {top.get('reason')}")
    else:
        report.append("- Top recommendation: none")
    report.append("")

    # Notion Sync
    sync = perf_log.get('sync', {})
    report.append("## Notion Sync")
    report.append("")
    report.append("| Check | Status | Detail |")
    report.append("|-------|--------|--------|")
    report.append(f"| DNS/API preflight | {notion['api']['status']} | {notion['recommendation']} |")
    report.append(f"| Local performance entries | {sync.get('total', 0)} | Source of truth for self-improvement when Notion is unavailable |")
    report.append(f"| Remote synced | {sync.get('remote_synced', 0)} | Entries with confirmed Notion URL |")
    report.append(f"| Pending/local-first | {sync.get('pending', 0) + sync.get('local_first', 0)} | Run `python3 execution/log_performance.py sync-pending --dry-run` before syncing |")
    report.append(f"| Sync failed | {sync.get('sync_failed', 0)} | Usually sandbox DNS/network unless API error says otherwise |")
    report.append("")

    # Hookify Guards
    report.append("## Hookify Guards")
    report.append("")
    report.append("| Hook | Enabled | Event | Action |")
    report.append("|------|---------|-------|--------|")
    for h in hooks:
        enabled_str = 'Yes' if h['enabled'] else 'No'
        report.append(f"| {h['name']} | {enabled_str} | {h['event']} | {h['action']} |")
    report.append("")

    # Cascade Dependencies
    report.append("## Cascade Dependencies")
    report.append("")
    report.append(f"```")
    report.append(f"Performance Log ({perf_count} entries)")
    report.append(f"  └─> Skill Evolution (needs 20+) {phase2_status if phase2_ready else f'[{perf_count}/20]'}")
    report.append(f"        └─> Cross-Pollination (needs evolution data) {'READY' if phase3_ready else '[waiting]'}")
    report.append(f"              └─> Gap Detection (monthly) {'READY' if phase4_ready else '[waiting]'}")
    report.append(f"```")
    report.append("")

    # Recommended Actions
    report.append("## Recommended Actions")
    report.append("")

    actions = []
    if perf_count == 0:
        actions.append("**CRITICAL**: Start logging performance entries. Run the Quality Gate after your next expert-driven output, then log with `python execution/log_performance.py log \"description\" --skill X --type Y --quality N --status Keep`")
    elif perf_count < 20:
        actions.append(f"**IN PROGRESS**: {perf_count}/20 performance entries logged. Need {20 - perf_count} more to unlock Skill Evolution (Phase 2).")

    if phase2_ready:
        if ready_candidates:
            actions.append(f"**READY**: Review `{ready_candidates}` Skill Evolution candidate(s) with `python3 execution/skill_evolution_candidates.py status`.")
        else:
            actions.append("**READY**: Skill Evolution is unlocked; keep collecting target-specific evidence until a candidate becomes ready.")

    if session['status'] == 'DORMANT':
        actions.append("**WARNING**: No session state file found. Write `.agent/session-state.md` after major decisions.")

    if routing['status'] == 'DORMANT':
        actions.append("**WARNING**: No routing decisions logged. The routing intelligence system needs data to improve over time.")

    if not actions:
        actions.append("All systems operational. Keep logging performance data to maintain the feedback loop.")

    for i, action in enumerate(actions, 1):
        report.append(f"{i}. {action}")

    report.append("")

    # Write report
    report_text = "\n".join(report)

    if quick:
        # Print summary to stdout
        print(report_text)
    else:
        OUTPUT_DIR.mkdir(exist_ok=True)
        output_path = OUTPUT_DIR / "health-report.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_text)
        print(report_text)
        print(f"\nReport saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Antigravity System Health Check')
    parser.add_argument('--quick', action='store_true', help='Summary only (no file save)')
    args = parser.parse_args()
    generate_health_report(quick=args.quick)


if __name__ == '__main__':
    main()
