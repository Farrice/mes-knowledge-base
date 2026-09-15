#!/usr/bin/env python3
"""Additive global Codex installation; no provider calls or blanket hook trust.

Backs up both receiving files and uses expected hashes. Rollback refuses to
clobber later edits. Native hooks/list supplies trust hashes after installation.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import tempfile
import time

BEGIN = '<!-- BEGIN:working-context-reconciliation -->'
END = '<!-- END:working-context-reconciliation -->'
EVENTS = ('SessionStart', 'UserPromptSubmit', 'PreToolUse', 'PostToolUse', 'PreCompact', 'PostCompact', 'Stop')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def desired(home, root):
    home, root = Path(home), Path(root).resolve()
    runtime = root / 'execution/working_context.py'
    contract = root / 'directives/working-context-reconciliation.md'
    if not runtime.is_file() or not contract.is_file():
        raise ValueError('Canonical runtime and contract must exist before installation.')
    hp, ap = home / 'hooks.json', home / 'AGENTS.md'
    hooks = json.loads(hp.read_text()) if hp.exists() else {}
    instructions = ap.read_text() if ap.exists() else ''
    for event in EVENTS:
        entries = hooks.setdefault('hooks', {}).setdefault(event, [])
        # Remove only our own handlers; preserve unrelated handlers in mixed groups.
        preserved = []
        for entry in entries:
            rest = [h for h in entry.get('hooks', []) if not ('working_context.py' in h.get('command', '') and 'hook --harness codex' in h.get('command', ''))]
            if rest or not entry.get('hooks'):
                preserved.append({**entry, 'hooks': rest})
        command = 'python3 ' + shlex.quote(str(runtime)) + ' hook --harness codex --event ' + event
        preserved.append({'matcher': '*', 'hooks': [{'type': 'command', 'command': command, 'timeout': 10}]})
        hooks['hooks'][event] = preserved
    block = f'''{BEGIN}
## Every-turn working context

At every turn, integrate feedback into the whole accumulated intent before
proceeding. Preserve accepted parts and scope; retire rejected direction from
active inputs; maintain one coherent current view. Use the current session
model, without extra user commands, forms, or agents. Safe reads remain allowed.
Read `{contract}` when initializing or reconciling the session. Follow the
native hook's session identity and pending-turn receipt; commit through
`{runtime}`. After writes, verify freshness. Restore this state on resume and
compaction. A hook receipt proves coverage, not semantic understanding. A missed
receipt gets one bounded Stop recovery; never loop or report false success.
This extends existing filing, CANON and handoff owners; it grants no new external
permissions and does not make local feedback a global preference.
{END}'''
    if BEGIN in instructions:
        if instructions.count(BEGIN) != 1 or instructions.count(END) != 1:
            raise ValueError('Ambiguous existing installation markers.')
        before, tail = instructions.split(BEGIN)
        _, after = tail.split(END)
        instructions = before + block + after
    else:
        instructions = block + '\n\n' + instructions
    return {hp: (json.dumps(hooks, indent=2) + '\n').encode(), ap: instructions.encode()}


def atomic(path, data):
    if path.is_symlink():
        raise ValueError('Refusing symlink receiver: ' + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as f:
        f.write(data); f.flush(); os.fsync(f.fileno()); temp = Path(f.name)
    temp.chmod(mode)
    temp.replace(path)


def install(home, root, apply=False):
    files = desired(home, root)
    before = {p: p.read_bytes() if p.exists() else None for p in files}
    changes = {p: data for p, data in files.items() if before[p] != data}
    receipt = {'root': str(Path(root).resolve()), 'applied': False, 'files': [], 'native_trust': 'VERIFY_WITH_HOOKS_LIST'}
    if not changes:
        return {**receipt, 'status': 'ALREADY_CURRENT'}
    backup = Path(home) / 'working-context/backups' / time.strftime('%Y%m%d-%H%M%S')
    if apply:
        backup.mkdir(parents=True, exist_ok=False, mode=0o700)
    for p, data in changes.items():
        record = {'path': str(p), 'before': digest(before[p]) if before[p] is not None else None, 'after': digest(data)}
        if apply and before[p] is not None:
            saved = backup / p.name
            atomic(saved, before[p]); record['backup'] = str(saved)
        receipt['files'].append(record)
    # All backups exist before any receiving file changes.
    for p, data in changes.items():
        if apply:
            if (p.read_bytes() if p.exists() else None) != before[p]:
                raise ValueError('Receiver changed during installation: ' + str(p))
            atomic(p, data)
    receipt.update(applied=apply, status='INSTALLED' if apply else 'DRY_RUN')
    if apply:
        receipt['receipt'] = str(backup / 'receipt.json')
        atomic(backup / 'receipt.json', json.dumps(receipt, indent=2).encode())
    return receipt


def rollback(receipt_path):
    receipt = json.loads(Path(receipt_path).read_text())
    for item in receipt['files']:
        p = Path(item['path'])
        if not p.is_file() or digest(p.read_bytes()) != item['after']:
            raise ValueError('Later edits present; refusing blanket rollback: ' + str(p))
        if item.get('backup') and digest(Path(item['backup']).read_bytes()) != item['before']:
            raise ValueError('Backup hash mismatch.')
    for item in receipt['files']:
        p = Path(item['path'])
        if item.get('backup'):
            atomic(p, Path(item['backup']).read_bytes())
        else:
            p.unlink()
    return {'status': 'ROLLED_BACK', 'receipt': receipt_path}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--home', type=Path, default=Path.home() / '.codex')
    p.add_argument('--root', type=Path, default=Path('/Users/farricecain/Google Antigravity'))
    p.add_argument('--apply', action='store_true')
    p.add_argument('--rollback')
    args = p.parse_args()
    result = rollback(args.rollback) if args.rollback else install(args.home, args.root, args.apply)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
