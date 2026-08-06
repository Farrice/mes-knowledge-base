#!/usr/bin/env python3
"""
event_listener.py — External events → mission-queue cards (deterministic, no LLM).

Born 2026-08-06 from the God Agent delta memo, adoptable move #1
(`_active/mastery-forge/01-research/god-agent-delta.md`): the harness was
clock-driven only — nothing outside the machine could wake it. This listener
closes that gap by POLLING event sources and minting T1 Mission Cards into
`.agent/mission-queue/pending/`, which execution/mission_runner.py already
consumes unattended (T1-only, refusal net for publish/send/spend).

The listener itself is intelligence-free and outward-action-free: read-only
polls + local file writes. All judgment happens downstream in the mission
runner under its existing gates. Per feedback_ai-memory-dependent-observability
this is a deterministic backstop, never an AI-remembering-to-check pattern.

Sources (v1):
  inbox     — watch folder `.agent/inbox/`: any file dropped becomes a card
              (zero auth; live immediately). Processed files move to
              `.agent/inbox/processed/`.
  gmail     — unread human mail in the last 24h via `gws` (needs gmail scope;
              degrades to SKIPPED note on auth failure, never crashes).
  calendar  — events in the next 48h via `gws` (same graceful degradation).

Usage:
    python3 execution/event_listener.py poll            # all sources
    python3 execution/event_listener.py poll --source inbox
    python3 execution/event_listener.py status          # state + last results

Dedup state: `.agent/event-listener-state.json` (seen ids, per-day card marks).
Volume guard: max ONE digest card per source per day; each inbox file gets its
own card (bounded by what Farrice drops).
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
PENDING = os.path.join(ROOT, '.agent', 'mission-queue', 'pending')
INBOX = os.path.join(ROOT, '.agent', 'inbox')
PROCESSED = os.path.join(INBOX, 'processed')
STATE_FILE = os.path.join(ROOT, '.agent', 'event-listener-state.json')

NOREPLY_RE = re.compile(r'no-?reply|notifications?@|newsletter|marketing@|mailer-daemon|updates@', re.I)


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {'seen_gmail_ids': [], 'seen_event_ids': [], 'daily_cards': {}, 'runs': []}


def save_state(state):
    state['seen_gmail_ids'] = state['seen_gmail_ids'][-500:]
    state['seen_event_ids'] = state['seen_event_ids'][-200:]
    state['runs'] = state['runs'][-30:]
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def today():
    return datetime.now().strftime('%Y-%m-%d')


def daily_card_done(state, source):
    return state['daily_cards'].get(source) == today()


def mark_daily_card(state, source):
    state['daily_cards'][source] = today()


def write_card(filename, title, objective_lines, context_lines=None):
    """Mint a T1 mission card in the exact format mission_runner.py parses."""
    os.makedirs(PENDING, exist_ok=True)
    path = os.path.join(PENDING, filename)
    if os.path.exists(path):
        return None
    lines = [
        f"# Mission Card — {title}",
        "Tier: T1",
        f"Produced: {today()} (queued by execution/event_listener.py)",
        "",
        "## Objective",
        *objective_lines,
        "",
    ]
    if context_lines:
        lines += ["## Context to load first", *context_lines, ""]
    lines += [
        "## Constraints",
        "- DRAFTS AND FILES ONLY. Nothing is transmitted, sent, posted, or purchased.",
        "- Density over completeness; one labeled block per item.",
        "- If an item needs Farrice's judgment, write the question + your recommendation and stop there.",
    ]
    with open(path, 'w') as f:
        f.write("\n".join(lines) + "\n")
    return path


def gws(args_list, timeout=30):
    """Run a gws command; return (ok, parsed_json_or_error_string)."""
    try:
        r = subprocess.run(['gws'] + args_list, capture_output=True, text=True, timeout=timeout)
        out = r.stdout.strip()
        start = out.find('{')
        if start == -1:
            return False, (r.stderr.strip() or out or 'empty response')[:200]
        data = json.loads(out[start:])
        if isinstance(data, dict) and 'error' in data:
            return False, data['error'].get('message', 'api error')[:200]
        return True, data
    except FileNotFoundError:
        return False, 'gws CLI not installed'
    except Exception as e:
        return False, f'{type(e).__name__}: {str(e)[:150]}'


def poll_inbox(state):
    """Watch folder: every dropped file becomes its own mission card."""
    os.makedirs(INBOX, exist_ok=True)
    os.makedirs(PROCESSED, exist_ok=True)
    minted = []
    for name in sorted(os.listdir(INBOX)):
        src = os.path.join(INBOX, name)
        if name.startswith('.') or name == 'processed' or not os.path.isfile(src):
            continue
        dest = os.path.join(PROCESSED, f"{today()}-{name}")
        shutil.move(src, dest)
        slug = re.sub(r'[^a-z0-9]+', '-', os.path.splitext(name)[0].lower())[:40].strip('-')
        card = write_card(
            f"card-event-inbox-{today()}-{slug}.md",
            f"Dropped item: {name}",
            [
                f"Farrice dropped `{dest}` into the event inbox.",
                "Read it, work out what it is (idea, task, screenshot, source material, half-thought),",
                "and take it to its natural next artifact: park a thought-bank entry, draft the asset,",
                "brief the extraction, or write a 3-line triage note — whichever the content calls for.",
                f"Land the result next to the source as `{dest}.result.md` and reference any assets created.",
            ],
        )
        if card:
            minted.append(card)
    return minted, 'OK'


def poll_gmail(state):
    """Unread human mail (24h) → one digest card per day."""
    if daily_card_done(state, 'gmail'):
        return [], 'daily card already minted'
    ok, data = gws(['gmail', 'users', 'messages', 'list', '--params',
                    json.dumps({'userId': 'me', 'q': 'is:unread newer_than:1d -category:promotions -category:social', 'maxResults': 15})])
    if not ok:
        return [], f'SKIPPED ({data})'
    msgs = data.get('messages') or []
    fresh = [m for m in msgs if m['id'] not in state['seen_gmail_ids']]
    items = []
    for m in fresh[:10]:
        ok2, full = gws(['gmail', 'users', 'messages', 'get', '--params',
                         json.dumps({'userId': 'me', 'id': m['id'], 'format': 'metadata', 'metadataHeaders': ['From', 'Subject', 'Date']})])
        if not ok2:
            continue
        headers = {h['name']: h['value'] for h in full.get('payload', {}).get('headers', [])}
        sender = headers.get('From', '?')
        if NOREPLY_RE.search(sender):
            state['seen_gmail_ids'].append(m['id'])
            continue
        items.append(f"- from: {sender} | subject: {headers.get('Subject', '(none)')} | {headers.get('Date', '')} | snippet: {full.get('snippet', '')[:140]}")
        state['seen_gmail_ids'].append(m['id'])
    if not items:
        return [], 'no human mail'
    card = write_card(
        f"card-event-gmail-{today()}.md",
        f"Inbound email triage ({len(items)} human messages)",
        [
            "New unread email from real humans landed in the last 24h:",
            *items,
            "",
            "For each: classify (client / lead / personal / admin), and where a reply is",
            "warranted DRAFT it in Farrice's voice (load `_active/farrice-brand/voice/VOICE-CARD.md`,",
            "dial BLEND). Write everything to `.agent/cos/email-triage-" + today() + ".md`.",
        ],
    )
    if card:
        mark_daily_card(state, 'gmail')
        return [card], 'OK'
    return [], 'card existed'


def poll_calendar(state):
    """Events in the next 48h → one prep card per day."""
    if daily_card_done(state, 'calendar'):
        return [], 'daily card already minted'
    from datetime import timedelta, timezone
    now = datetime.now(timezone.utc)
    ok, data = gws(['calendar', 'events', 'list', '--params',
                    json.dumps({'calendarId': 'primary', 'timeMin': now.isoformat(),
                                'timeMax': (now + timedelta(hours=48)).isoformat(),
                                'singleEvents': True, 'orderBy': 'startTime', 'maxResults': 10})])
    if not ok:
        return [], f'SKIPPED ({data})'
    fresh = [e for e in data.get('items', []) if e.get('id') not in state['seen_event_ids'] and e.get('status') != 'cancelled']
    if not fresh:
        return [], 'no new events'
    items = []
    for e in fresh:
        start = e.get('start', {}).get('dateTime', e.get('start', {}).get('date', '?'))
        items.append(f"- {start} | {e.get('summary', '(untitled)')} | attendees: {len(e.get('attendees', []))}")
        state['seen_event_ids'].append(e.get('id'))
    card = write_card(
        f"card-event-calendar-{today()}.md",
        f"Upcoming events prep ({len(items)} in next 48h)",
        [
            "New calendar events in the next 48 hours:",
            *items,
            "",
            "For any event that benefits from prep (client call, meeting with a named person),",
            "write a half-page prep note: who, context from memory/repo, what Farrice likely",
            "wants out of it, 3 talking points. Land in `.agent/cos/event-prep-" + today() + ".md`.",
            "Skip personal/routine events with a one-line reason.",
        ],
    )
    if card:
        mark_daily_card(state, 'calendar')
        return [card], 'OK'
    return [], 'card existed'


SOURCES = {'inbox': poll_inbox, 'gmail': poll_gmail, 'calendar': poll_calendar}


def cmd_poll(args):
    state = load_state()
    results = {}
    minted_total = []
    for name, fn in SOURCES.items():
        if args.source and name != args.source:
            continue
        try:
            minted, note = fn(state)
        except Exception as e:
            minted, note = [], f'ERROR {type(e).__name__}: {str(e)[:120]}'
        results[name] = {'minted': [os.path.basename(p) for p in minted], 'note': note}
        minted_total += minted
    state['runs'].append({'ts': datetime.now().isoformat(timespec='seconds'), 'results': results})
    save_state(state)
    if minted_total:
        try:
            from execution.notify import send as notify_send
            names = ', '.join(os.path.basename(p) for p in minted_total)
            notify_send('Antigravity: new mission cards', f'{len(minted_total)} card(s) queued: {names}')
        except Exception:
            pass
    print(json.dumps({'minted': len(minted_total), 'results': results}, indent=2))


def cmd_status(args):
    state = load_state()
    print(json.dumps({
        'last_runs': state['runs'][-3:],
        'daily_cards': state['daily_cards'],
        'seen_gmail': len(state['seen_gmail_ids']),
        'seen_events': len(state['seen_event_ids']),
        'inbox_drop_zone': INBOX,
    }, indent=2))


def main():
    p = argparse.ArgumentParser(description='External events → mission-queue cards')
    sub = p.add_subparsers(dest='command')
    pp = sub.add_parser('poll', help='Poll sources and mint mission cards')
    pp.add_argument('--source', choices=list(SOURCES), default=None)
    sub.add_parser('status', help='Show listener state')
    args = p.parse_args()
    if args.command == 'poll':
        cmd_poll(args)
    elif args.command == 'status':
        cmd_status(args)
    else:
        p.print_help()


if __name__ == '__main__':
    main()
