#!/usr/bin/env python3
"""council_pulse.py — the standing-council outcome loop, one line (the Mailroom, 2026-08-27).

Goal + scar (rule contract): councils/buyers/calibration.jsonl predictions sat at
"pending" forever and councils/<name>/decisions.md stayed empty templates for six
months — the system declared it wants a learning loop (councils/README.md trust
calibration) and demonstrably wasn't getting one, because nothing watched for
outcomes. This is the watcher: deterministic (no LLM, no cost), silent when clean,
one line into the SessionStart digest when a loop is open. Grounds in Farrice in
one hop (pulse → digest → him). Consumer: /cos check-in + /weekly-closeout.

CLI:
    python3 execution/council_pulse.py          # one line or silence (digest mode)
    python3 execution/council_pulse.py --full   # per-item detail
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALIBRATION = ROOT / "councils" / "buyers" / "calibration.jsonl"
COUNCILS = ROOT / "councils"
SESSIONS = ROOT / "knowledge" / "council-sessions"

STALE_DAYS = 14
TEMPLATE_MAX_LINES = 10  # a decisions.md at/below this is still the empty template


def pending_calibrations() -> list[dict]:
    rows = []
    if not CALIBRATION.exists():
        return rows
    cutoff = datetime.now() - timedelta(days=STALE_DAYS)
    for line in CALIBRATION.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except Exception:
            continue
        if row.get("real_outcome") != "pending":
            continue
        stamp = row.get("ts") or row.get("date") or row.get("timestamp") or ""
        try:
            when = datetime.fromisoformat(str(stamp)[:19])
        except Exception:
            when = None
        if when is None or when < cutoff:
            rows.append(row)
    return rows


def empty_decision_memories() -> list[str]:
    names = []
    if not COUNCILS.exists():
        return names
    for d in sorted(COUNCILS.iterdir()):
        p = d / "decisions.md"
        if d.is_dir() and p.exists():
            try:
                lines = [ln for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines() if ln.strip()]
            except Exception:
                continue
            if len(lines) <= TEMPLATE_MAX_LINES:
                names.append(d.name)
    return names


def main() -> int:
    full = "--full" in sys.argv
    pending = pending_calibrations()
    empty = empty_decision_memories()

    parts = []
    if pending:
        parts.append(f"{len(pending)} calibration prediction(s) pending >{STALE_DAYS}d — close with real outcomes")
    if empty:
        parts.append(f"{len(empty)} standing council(s) with empty decision memory")
    if not parts:
        if full:
            print("COUNCIL: all outcome loops closed.")
        return 0  # silence in digest mode — nudges get out of the way

    print(f"COUNCIL: {' · '.join(parts)}")
    if full:
        for row in pending:
            print(f"  - pending: {row.get('prediction', row)!s}"[:160])
        for name in empty:
            print(f"  - empty decisions.md: councils/{name}/ (populate at next live session close)")
        print("  Close path: .agent/workflows/roundtable-live.md Step 6 / directives/agent-mailroom.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
