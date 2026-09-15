#!/usr/bin/env python3
"""Every-turn working context. Local, transactional, no model calls or cleanup sweeps.

The session model interprets feedback; this runtime owns receipt coverage,
intent/preservation checks, immutable revisions and current-view generation.
Document-history remains the owner of physical document retirement.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import tempfile
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / 'directives/working-context-reconciliation.md'
MARKER = '<!-- managed-by: working_context.py -->'
HISTORY = {'rejected', 'superseded', 'parked', 'archived'}
ROLES = HISTORY | {'candidate', 'reference', 'approved'}


class Conflict(ValueError):
    pass


def sha(value):
    if not isinstance(value, bytes):
        value = json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(value).hexdigest()


def store_path():
    return Path(os.environ.get('WORKING_CONTEXT_STORE', str(Path.home() / '.codex/working-context/state.sqlite3')))


def key(harness, session):
    if harness not in {'codex', 'claude'} or not re.fullmatch(r'[A-Za-z0-9_-]{6,160}', session or '') or session == 'unknown':
        raise Conflict('Missing or invalid native session identity; no guessed task binding.')
    return harness + ':' + session


@contextmanager
def database(path=None):
    path = Path(path or store_path())
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise Conflict('Runtime database must not be a symlink.')
    db = sqlite3.connect(path, timeout=5, isolation_level=None)
    os.chmod(path, 0o600)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('PRAGMA synchronous=FULL')
    db.executescript('''
      CREATE TABLE IF NOT EXISTS sessions (
        id TEXT PRIMARY KEY, workspace TEXT NOT NULL, revision INTEGER NOT NULL DEFAULT 0,
        snapshot TEXT, write_root TEXT, updated REAL NOT NULL);
      CREATE TABLE IF NOT EXISTS turns (
        session TEXT NOT NULL, seq INTEGER NOT NULL, event_id TEXT NOT NULL,
        text TEXT NOT NULL, source TEXT NOT NULL, resolved INTEGER NOT NULL DEFAULT 0,
        effect TEXT, PRIMARY KEY(session,seq), UNIQUE(session,event_id));
      CREATE TABLE IF NOT EXISTS history (
        session TEXT NOT NULL, revision INTEGER NOT NULL, snapshot TEXT NOT NULL,
        PRIMARY KEY(session,revision));
      CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY, session TEXT NOT NULL, event TEXT NOT NULL,
        data TEXT NOT NULL, created REAL NOT NULL);
    ''')
    try:
        db.execute('BEGIN IMMEDIATE')
        yield db
        db.execute('COMMIT')
    except BaseException:
        if db.in_transaction:
            db.execute('ROLLBACK')
        raise
    finally:
        db.close()


def log(db, sid, event, data):
    db.execute('INSERT INTO events(session,event,data,created) VALUES(?,?,?,?)',
               (sid, event, json.dumps(data, ensure_ascii=False), time.time()))


def load(db, sid):
    row = db.execute('SELECT * FROM sessions WHERE id=?', (sid,)).fetchone()
    if row is None:
        raise Conflict('No captured turn for this session. Wait for its native prompt event or explicitly import it.')
    out = dict(row)
    out['snapshot'] = json.loads(out['snapshot']) if out['snapshot'] else None
    out['pending'] = [dict(t) for t in db.execute('SELECT seq,text,source FROM turns WHERE session=? AND resolved=0 ORDER BY seq', (sid,))]
    return out


def observe(sid, workspace, text, event_id=None, source='native:UserPromptSubmit', path=None):
    if not isinstance(text, str) or not text.strip():
        raise Conflict('Prompt event did not contain user text; coverage is unknown.')
    # Never silently truncate the decision evidence.
    if len(text.encode()) > 2_000_000:
        raise Conflict('Prompt exceeds capture limit; preserve its transcript and reconcile explicitly.')
    with database(path) as db:
        db.execute('INSERT OR IGNORE INTO sessions(id,workspace,updated) VALUES(?,?,?)',
                   (sid, str(Path(workspace).resolve()), time.time()))
        event_id = event_id or str(uuid.uuid4())
        old = db.execute('SELECT * FROM turns WHERE session=? AND event_id=?', (sid, event_id)).fetchone()
        if old:
            if old['text'] != text:
                raise Conflict('Native turn identity was reused with different text.')
            return load(db, sid)
        seq = db.execute('SELECT COALESCE(MAX(seq),0)+1 FROM turns WHERE session=?', (sid,)).fetchone()[0]
        db.execute('INSERT INTO turns(session,seq,event_id,text,source) VALUES(?,?,?,?,?)', (sid, seq, event_id, text, source))
        db.execute('UPDATE sessions SET revision=revision+1,updated=? WHERE id=?', (time.time(), sid))
        log(db, sid, 'prompt-captured', {'seq': seq, 'event_id': event_id, 'sha256': sha(text)})
        return load(db, sid)


def citation(db, sid, value, pending=None):
    if not isinstance(value, dict) or not isinstance(value.get('turn'), int):
        raise Conflict('Decision needs a captured turn number and exact quote.')
    row = db.execute('SELECT text FROM turns WHERE session=? AND seq=?', (sid, value['turn'])).fetchone()
    quote = value.get('quote')
    if not row or not isinstance(quote, str) or not quote.strip() or quote not in row['text']:
        raise Conflict('Decision quote does not match its captured user turn.')
    if pending is not None and value['turn'] not in pending:
        raise Conflict('This change requires new feedback, not reused old permission.')


def validate_snapshot(db, sid, old, snapshot, pending, overrides):
    if not isinstance(snapshot, dict):
        raise Conflict('Snapshot must be an object.')
    if not all(isinstance(snapshot.get(k), str) and snapshot[k].strip() for k in ('intent', 'working_brief')):
        raise Conflict('Preserve the overall intent and one coherent working brief.')
    if len(json.dumps(snapshot).encode()) > 48000:
        raise Conflict('Working state is too large; keep history and rejected bodies in the journal.')
    if old and old['intent'] != snapshot['intent']:
        citation(db, sid, overrides.get('intent'), pending)
        if overrides['intent'].get('kind') != 'objective-change':
            raise Conflict('A refinement must not silently replace the overall objective.')
    for field in ('preserved', 'artifacts'):
        if not isinstance(snapshot.get(field, []), list):
            raise Conflict(field + ' must be a list.')
        if any(not isinstance(i, dict) for i in snapshot.get(field, [])):
            raise Conflict(field + ' entries must be objects.')
        ids = [i.get('id') for i in snapshot.get(field, [])]
        if any(not i for i in ids) or len(set(ids)) != len(ids):
            raise Conflict('Missing or duplicate identities in ' + field)
    preserved = {i['id']: i for i in snapshot.get('preserved', [])}
    for i in preserved.values():
        if not i.get('text') or i.get('scope') not in {'component', 'artifact', 'task', 'project', 'global'}:
            raise Conflict('Preserved decisions need exact text and explicit scope.')
        citation(db, sid, i.get('evidence'))
        if i['scope'] == 'global' and i.get('explicit_global') is not True:
            raise Conflict('Local feedback cannot become a global preference by inference.')
    for i in (old or {}).get('preserved', []):
        if i != preserved.get(i['id']):
            citation(db, sid, overrides.get(i['id']), pending)
    old_artifacts = {i['id']: i for i in (old or {}).get('artifacts', [])}
    slots = set()
    for i in snapshot.get('artifacts', []):
        if i.get('role') not in ROLES or not i.get('purpose') or not i.get('path'):
            raise Conflict('Artifact needs a path, purpose and explicit lifecycle role.')
        if not Path(i['path']).is_absolute():
            raise Conflict('Artifact references must be absolute and task-specific.')
        citation(db, sid, i.get('evidence'))
        if i['role'] in HISTORY:
            if not i.get('reason'):
                raise Conflict('Retirement needs a reason; original bytes remain preserved.')
        else:
            p = Path(i['path'])
            if not p.is_file():
                raise Conflict('Active source is missing: ' + str(p))
            actual = sha(p.read_bytes())
            if i.get('sha256') and i['sha256'] != actual:
                raise Conflict('Source changed since inspection: ' + str(p))
            i['sha256'] = actual
        if i['role'] in {'candidate', 'approved'}:
            if i['purpose'] in slots:
                raise Conflict('Multiple current artifacts claim the same purpose.')
            slots.add(i['purpose'])
        prev = old_artifacts.get(i['id'])
        if prev and ((prev['role'] in HISTORY and i['role'] not in HISTORY) or
                     (prev['role'] == 'approved' and any(i.get(k) != prev.get(k) for k in ('role','path','sha256')))):
            citation(db, sid, overrides.get(i['id']), pending)
    current_ids = {i['id'] for i in snapshot.get('artifacts', [])}
    if set(old_artifacts) - current_ids:
        raise Conflict('Registered artifacts must be retired explicitly, not silently dropped.')
    action = snapshot.get('next_action')
    if action:
        if not isinstance(action, dict) or not action.get('text'):
            raise Conflict('Next action needs text and explicit artifact targets (or an empty list).')
        targets = action.get('targets')
        if not isinstance(targets, list):
            raise Conflict('Next action targets must be a list.')
        active = {i['id'] for i in snapshot.get('artifacts', []) if i['role'] not in HISTORY}
        if not set(targets).issubset(active):
            raise Conflict('Next action points to rejected, retired or unknown work.')


def check_write_root(root):
    p = Path(root).resolve(strict=True)
    if not p.is_dir():
        raise Conflict('Write root is not a directory.')
    # Never author a current view inside a main/integration checkout.
    for parent in [p, *p.parents]:
        if (parent / '.git').exists():
            if not (parent / '.git').is_file():
                raise Conflict('Bind the owning worktree, not the integration checkout.')
            break
    return str(p)


def commit(sid, request, path=None):
    if not isinstance(request, dict):
        raise Conflict('Commit request must be an object.')
    with database(path) as db:
        state = load(db, sid)
        if request.get('expected_revision') != state['revision']:
            raise Conflict('Stale revision; reread and reconcile intervening feedback before retrying.')
        pending = {t['seq'] for t in state['pending']}
        resolutions = request.get('resolutions', [])
        ids = [r.get('turn') for r in resolutions]
        if len(ids) != len(set(ids)) or set(ids) != pending:
            raise Conflict('Account for every pending turn exactly once, including no-change turns.')
        for resolution in resolutions:
            citation(db, sid, resolution, pending)
            if not resolution.get('effect'):
                raise Conflict('Each turn needs its integrated effect or a no-change reason.')
        snapshot = request.get('snapshot', state['snapshot'])
        if snapshot is None:
            if not request.get('no_change_reason'):
                raise Conflict('Initialize coherent intent, or explicitly acknowledge a conversation-only turn.')
        elif 'snapshot' in request:
            validate_snapshot(db, sid, state['snapshot'], snapshot, pending, request.get('overrides', {}))
        elif drift(state):
            raise Conflict('Sources changed; update the snapshot before acknowledging the turn.')
        root = check_write_root(request['write_root']) if request.get('write_root') else state['write_root']
        revision = state['revision'] + 1
        encoded = json.dumps(snapshot, ensure_ascii=False)
        db.execute('UPDATE sessions SET revision=?,snapshot=?,write_root=?,updated=? WHERE id=?',
                   (revision, encoded if snapshot else None, root, time.time(), sid))
        db.execute('INSERT INTO history(session,revision,snapshot) VALUES(?,?,?)', (sid, revision, encoded))
        for r in resolutions:
            db.execute('UPDATE turns SET resolved=1,effect=? WHERE session=? AND seq=?', (r['effect'], sid, r['turn']))
        log(db, sid, 'reconciled', {'revision': revision, 'turns': ids, 'snapshot_sha256': sha(snapshot)})
        result = load(db, sid)
    # Current view is a derivative. A crash here cannot lose the authoritative
    # transaction. read/verify reports a stale view; render repairs it explicitly.
    if root and snapshot:
        render(result, path)
    return result


def drift(state):
    issues = []
    for i in (state['snapshot'] or {}).get('artifacts', []):
        if i['role'] in HISTORY:
            continue
        p = Path(i['path'])
        try:
            if not p.is_file() or sha(p.read_bytes()) != i['sha256']:
                issues.append('SOURCE_CHANGED: ' + str(p))
        except OSError:
            issues.append('SOURCE_UNREADABLE: ' + str(p))
    return issues


def view_path(state):
    if not state.get('write_root'):
        return None
    return Path(state['write_root']) / '.working-context' / (sha(state['id'])[:20] + '.md')


def render_text(state):
    s = state['snapshot']
    lines = ['# Current Working Context', '', MARKER, '', 'Session: ' + state['id'],
             'Revision: ' + str(state['revision']), '', '## Whole intent', '', s['intent'],
             '', '## Integrated working brief', '', s['working_brief'], '', '## Preserve', '']
    lines += [f"- {p['text']} (scope: {p['scope']}; user turn {p['evidence']['turn']})" for p in s.get('preserved', [])]
    lines += ['', '## Active references', '']
    lines += [f"- {i['role'].upper()}: {i['path']} — {i['purpose']}" for i in s.get('artifacts', []) if i['role'] not in HISTORY]
    lines += ['', '## Retired direction — reasons only', '']
    lines += [f"- {i['id']}: {i['reason']}" for i in s.get('artifacts', []) if i['role'] in HISTORY]
    lines += ['', '## Next action', '', (s.get('next_action') or {}).get('text', 'No action selected.'), '',
              'This view is regenerated, never prepended. Read the runtime before reuse; a newer user turn invalidates this snapshot until reconciled.', '']
    return '\n'.join(lines)


def render(state, store=None):
    with database(store) as db:
        state = load(db, state['id'])
        p = view_path(state)
        if not p or not state['snapshot']:
            return None
        parent = p.parent
        if parent.is_symlink() or p.is_symlink():
            raise Conflict('Current-view destination must not be a symlink.')
        parent.mkdir(exist_ok=True)
        previous = p.read_text() if p.exists() else None
        if previous is not None and MARKER not in previous:
            raise Conflict('Refusing to overwrite a human-owned file.')
        text = render_text(state)
        if previous is not None and previous != text:
            log(db, state['id'], 'current-view-preserved', {'path': str(p), 'text': previous})
        with tempfile.NamedTemporaryFile(mode='w', dir=parent, delete=False, prefix='.context-', encoding='utf-8') as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
            temporary = Path(f.name)
        temporary.replace(p)
        return str(p)


def read(sid, path=None):
    with database(path) as db:
        state = load(db, sid)
    state['issues'] = drift(state)
    p = view_path(state)
    if p and state['snapshot'] and (not p.exists() or p.read_text() != render_text(state)):
        state['issues'].append('CURRENT_VIEW_STALE: ' + str(p))
    state['status'] = 'PENDING' if state['pending'] else 'DRIFT' if state['issues'] else 'CURRENT'
    state['current_view'] = str(p) if p else None
    return state


def handoff(sid, path=None):
    state = read(sid, path)
    if state['status'] != 'CURRENT':
        raise Conflict('Reconcile pending feedback or drift before exporting a handoff.')
    s = state['snapshot']
    return {'session': sid, 'revision': state['revision'], 'digest': sha(s),
            'snapshot': {**s, 'artifacts': [i for i in s.get('artifacts', []) if i['role'] not in HISTORY]} if s else None}


def verify_handoff(sid, packet, path=None):
    if packet != handoff(sid, path):
        raise Conflict('Handoff is stale, altered or from another task.')
    return True


def job_context_note():
    """Read-only bridge for existing job consumers; no session guessing or writes."""
    session = os.environ.get('CODEX_THREAD_ID') or os.environ.get('CLAUDE_SESSION_ID')
    harness = 'codex' if os.environ.get('CODEX_THREAD_ID') else 'claude'
    if not session or not store_path().exists():
        return ''
    try:
        sid = key(harness, session)
        state = read(sid)
    except Conflict:
        return ''
    except (OSError, sqlite3.Error) as exc:
        return '\n## Working context unavailable\n\nRecover the source session before using this packet: ' + str(exc) + '\n'
    if state['status'] != 'CURRENT':
        return '\n## Working context requires reconciliation\n\n' + instruction(state) + '\n'
    if not state['snapshot']:
        return ''
    current = handoff(sid)
    return ('\n## Current working context — verify before execution\n\n'
            + f'Source session: {sid}; revision: {current["revision"]}; digest: {current["digest"]}.\n'
            + 'This integrated user direction governs the older card where they conflict. '
            + 'Read and verify this source session with execution/working_context.py before using this packet; '
            + 'pending feedback or changed hashes invalidate it. Recipient writes to its own session, never this source.\n\n'
            + json.dumps(current, ensure_ascii=False, indent=2) + '\n')


def historical_read_note(state, payload):
    tin = payload.get('tool_input') or {}
    if not isinstance(tin, dict):
        return ''
    fp = tin.get('file_path') or tin.get('path')
    command = str(tin.get('command') or tin.get('cmd') or '')
    requested = str((Path(payload.get('cwd') or state['workspace']) / fp).resolve()) if isinstance(fp, str) else ''
    hits = [i for i in (state['snapshot'] or {}).get('artifacts', [])
            if i['role'] in HISTORY and (i['path'] == requested or i['path'] in command)]
    return '\n'.join(f"HISTORICAL INPUT: {i['path']} is {i['role']}. {i['reason']} Use only for explicitly requested history/comparison; it is not current direction." for i in hits)


def instruction(state):
    seqs = [t['seq'] for t in state['pending']]
    cmd = f'python3 "{Path(__file__).resolve()}" read --session "{state["id"].split(":",1)[1]}" --harness {state["id"].split(":",1)[0]}'
    text = ('WORKING CONTEXT — every-turn reconciliation. '
            f'Pending turns: {seqs or "none"}; revision {state["revision"]}. '
            'Interpret new feedback within the whole accumulated intent. Preserve accepted parts; '
            'retire rejected direction; never turn a local correction into a global rule. '
            f'Read state: {cmd}. Contract: {CONTRACT}. '
            'Before dependent production, reconcile all pending turns via commit (or explicit no-change). '
            'Use the current model; no extra agents or user forms. After writes, verify sources and current view.')
    if state['snapshot']:
        intent = state['snapshot']['intent']
        text += '\nWhole intent: ' + (intent if len(intent) <= 1800 else '[read full intent from state; omitted here to avoid truncating it]')
    return text


def hook(payload, harness, event, path=None):
    if not isinstance(payload, dict):
        raise Conflict('Hook payload must be an object.')
    session = payload.get('session_id') or payload.get('thread_id')
    sid = key(harness, session)
    if event == 'UserPromptSubmit':
        state = observe(sid, payload.get('cwd') or os.getcwd(), payload.get('prompt') or payload.get('user_message'),
                        payload.get('turn_id') or payload.get('prompt_id'), path=path)
    else:
        try:
            state = read(sid, path)
        except Conflict:
            return {}
    with database(path) as db:
        log(db, sid, 'hook:' + event, {'pending': [t['seq'] for t in state['pending']],
                                     'revision': state['revision'], 'native_tool': payload.get('tool_name')})
    if event == 'Stop':
        problems = state['pending'] or state.get('issues')
        if problems and not payload.get('stop_hook_active'):
            return {'decision': 'block', 'reason': instruction(state) + '\nOne bounded recovery: reconcile now, then finish. If recovery is impossible, state the exact fault; do not loop or claim healthy coverage.'}
        return {}
    historical = historical_read_note(state, payload) if event in {'PreToolUse', 'PostToolUse'} else ''
    if event in {'PreToolUse', 'PostToolUse'} and not state['pending'] and not state.get('issues') and not historical:
        return {}
    text = instruction(state)
    if state.get('issues'):
        text += '\n' + '\n'.join(state['issues'])
    if historical:
        text += '\n' + historical
    return {'hookSpecificOutput': {'hookEventName': event, 'additionalContext': text}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', help='Explicit isolated store for tests or approved alternate deployment')
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('read', 'commit', 'render', 'handoff', 'verify'):
        p = sub.add_parser(name)
        p.add_argument('--session', default=os.environ.get('CODEX_THREAD_ID') or os.environ.get('CLAUDE_SESSION_ID'))
        p.add_argument('--harness', choices=['codex', 'claude'], default='codex')
        if name == 'commit':
            p.add_argument('--packet', required=True, help='JSON request file or - for stdin')
        if name == 'verify':
            p.add_argument('--handoff')
    p = sub.add_parser('hook')
    p.add_argument('--harness', choices=['codex', 'claude'], required=True)
    p.add_argument('--event', choices=['SessionStart','UserPromptSubmit','PreToolUse','PostToolUse','PreCompact','PostCompact','Stop'], required=True)
    args = parser.parse_args()
    try:
        if args.command == 'hook':
            payload = json.load(sys.stdin)
            out = hook(payload, args.harness, args.event, args.store)
        else:
            sid = key(args.harness, args.session)
            if args.command == 'read':
                out = read(sid, args.store)
            elif args.command == 'commit':
                request = json.load(sys.stdin) if args.packet == '-' else json.loads(Path(args.packet).read_text())
                out = commit(sid, request, args.store)
            elif args.command == 'render':
                out = {'path': render(read(sid, args.store), args.store)}
            elif args.command == 'handoff':
                out = handoff(sid, args.store)
            elif args.handoff:
                out = {'verified': verify_handoff(sid, json.loads(Path(args.handoff).read_text()), args.store)}
            else:
                out = read(sid, args.store)
                if out['status'] != 'CURRENT':
                    print(json.dumps(out, ensure_ascii=False))
                    return 2
        if out:
            print(json.dumps(out, ensure_ascii=False, indent=None if args.command == 'hook' else 2))
        return 0
    except (Conflict, OSError, sqlite3.Error, ValueError, TypeError, KeyError) as exc:
        if args.command == 'hook':
            text = f'WORKING CONTEXT FAULT: {type(exc).__name__}: {exc}. Coverage is degraded; do not claim automatic reconciliation. Preserve current work and report the fault.'
            if args.event == 'Stop':
                print(json.dumps({'decision':'block','reason':text}) if not (payload.get('stop_hook_active') if isinstance(locals().get('payload'), dict) else False) else '{}')
            else:
                print(json.dumps({'hookSpecificOutput': {'hookEventName':args.event, 'additionalContext':text}}))
            return 0
        print(f'WORKING CONTEXT: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
