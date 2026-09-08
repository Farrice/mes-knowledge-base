#!/usr/bin/env python3
"""Validate weekly eval receipts; never execute models, tools, or notifications.

A valid receipt is not an independent judgment of writing quality. This check
rejects missing/instruction-only evidence and measures E5's observable form.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

EVAL_KINDS = {f'E{i}': 'tool-run' if i in (3, 4) else 'model-run' for i in range(1, 7)}
STATUSES = {'PASS', 'FAIL', 'NOT_RUN', 'BLOCKED'}


def evidence_text(row: dict, base: Path, prefix: str = 'evidence') -> str:
    raw = row.get(f'{prefix}_file')
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(f'missing {prefix}_file')
    path = (base / raw).resolve()
    if path.name in {'AGENTS.md', 'CLAUDE.md', 'CODEX.md', 'SKILL.md', 'eval_set_v1.md'}:
        raise ValueError('an instruction file is not execution evidence')
    data = path.read_bytes()
    if not data.strip():
        raise ValueError('execution evidence is empty')
    if hashlib.sha256(data).hexdigest() != row.get(f'{prefix}_sha256'):
        raise ValueError(f'{prefix} hash missing or does not match current file')
    return data.decode('utf-8')


def e5_form_errors(response: str) -> list[str]:
    errors = []
    words = len(response.split())
    if words == 0 or words > 120:
        errors.append(f'E5 response has {words} words; expected 1–120')
    if len(re.split(r'\n\s*\n', response.strip())) != 1:
        errors.append('E5 response is not one paragraph')
    if re.search(r'(?m)^\s*(?:#{1,6}\s|[-*+]\s|\d+[.)]\s|```)', response):
        errors.append('E5 response contains a heading, list or code fence')
    return errors


def validate(payload: dict, base: Path) -> list[str]:
    errors = []
    rows = payload.get('results', [])
    if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
        return ['results must be a list of eval receipts']
    ids = [r.get('id') for r in rows]
    if any(not isinstance(key, str) for key in ids):
        return ['each eval id must be a string']
    if len(ids) != 6 or set(ids) != set(EVAL_KINDS):
        errors.append('include E1–E6 exactly once, including unrun or blocked cases')
    for row in rows:
        key, status = row.get('id'), row.get('status')
        if key not in EVAL_KINDS or not isinstance(status, str) or status not in STATUSES:
            errors.append(f'{key}: unknown eval or status')
            continue
        if not isinstance(row.get('observation'), str) or not row['observation'].strip():
            errors.append(f'{key}: missing observed result or reason not run')
        if status in {'NOT_RUN', 'BLOCKED'}:
            continue
        if row.get('kind') != EVAL_KINDS[key]:
            errors.append(f'{key}: expected {EVAL_KINDS[key]}, not instruction presence')
        if not isinstance(row.get('execution_ref'), str) or not row['execution_ref'].strip():
            errors.append(f'{key}: missing actual task/turn or command-run reference')
        if not isinstance(row.get('input'), str) or not row['input'].strip():
            errors.append(f'{key}: missing exact prompt or probe command')
        try:
            observed = evidence_text(row, base)
            if key == 'E1':
                evidence_text(row, base, 'trace')
            if key == 'E5' and status == 'PASS':
                errors.extend(e5_form_errors(observed))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f'{key}: {exc}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('receipt', type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.receipt.read_text())
        if not isinstance(payload, dict):
            raise ValueError('receipt must be an object')
        errors = validate(payload, args.receipt.resolve().parent)
    except (OSError, ValueError) as exc:
        errors, payload = [str(exc)], {}
    counts = {s: sum(r.get('status') == s for r in payload.get('results', []) if isinstance(r, dict))
              for s in sorted(STATUSES)} if isinstance(payload.get('results', []), list) else {}
    print(json.dumps({'evidence_valid': not errors, 'behavioral_results': counts,
                      'errors': errors,
                      'limit': 'Receipt validation; semantic verdicts still require inspection of the actual run.'}, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
