#!/usr/bin/env python3
"""
COS Reminders — dated tickler for promises with a real calendar date.

Why this exists (Farrice, 2026-07-27): he promised JJ a spin top at the
next dentist visit (2026-08-31) and said, in his own words, "You might
forget." A note in life-context.md that says "be mindful on 08-31" is
AI-memory-dependent observability — the exact pattern his own standing
rule bans. This module is the deterministic backstop: a dated entry on
disk that surfaces itself in the morning brief when its window opens,
whether or not any model remembers.

Storage: .agent/cos/reminders.jsonl (one JSON object per line)
    {"id": str, "date": "YYYY-MM-DD", "lead_days": int, "text": str,
     "source": str, "done": bool}

Surfacing window: date - lead_days  ..  date + GRACE_DAYS
(the grace tail means a reminder you blew past still nags instead of
vanishing silently the morning after.)

Stdlib only — cos_prep.py imports render_reminders() and must stay
dependency-free.

CLI:
    python3 execution/cos_reminders.py add --date 2026-08-31 --text "..." \
        [--lead-days 3] [--source "cos 2026-07-27"]
    python3 execution/cos_reminders.py list [--all]
    python3 execution/cos_reminders.py due
    python3 execution/cos_reminders.py done <id>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORE = ROOT / ".agent" / "cos" / "reminders.jsonl"

DEFAULT_LEAD_DAYS = 3
GRACE_DAYS = 7          # keep nagging this long after the date passes


def _today() -> date:
    return datetime.now().date()


def _load() -> list[dict]:
    if not STORE.exists():
        return []
    out = []
    for line in STORE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue        # a corrupt line must never break the morning brief
    return out


def _save(items: list[dict]) -> None:
    STORE.parent.mkdir(parents=True, exist_ok=True)
    STORE.write_text(
        "".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items),
        encoding="utf-8")


def _mint_id(date_str: str, text: str) -> str:
    return hashlib.sha1(f"{date_str}|{text}".encode()).hexdigest()[:12]


def due_reminders(on: date | None = None) -> list[dict]:
    """Reminders whose surfacing window is open on `on` (default today)."""
    on = on or _today()
    live = []
    for r in _load():
        if r.get("done"):
            continue
        try:
            target = datetime.strptime(r["date"], "%Y-%m-%d").date()
        except (KeyError, ValueError):
            continue
        opens = target - timedelta(days=int(r.get("lead_days", DEFAULT_LEAD_DAYS)))
        closes = target + timedelta(days=GRACE_DAYS)
        if opens <= on <= closes:
            r = dict(r)
            r["_days_out"] = (target - on).days
            live.append(r)
    return sorted(live, key=lambda r: r["date"])


def render_reminders(on: date | None = None) -> list[str]:
    """Brief section. Silent no-op when nothing's in window — the brief
    never pads with an empty header."""
    live = due_reminders(on)
    if not live:
        return []
    lines = ["", "## \U0001f5d3️ Coming up"]
    for r in live:
        d = r["_days_out"]
        when = ("TODAY" if d == 0
                else f"in {d}d" if d > 0
                else f"{-d}d ago, still open")
        lines.append(f"- [{r['date']}] ({when}) {r['text']}")
        lines.append(f"  ↳ done: `python3 execution/cos_reminders.py done {r['id']}`"
                     + (f" · from: {r['source']}" if r.get("source") else ""))
    return lines


def cmd_add(args) -> int:
    datetime.strptime(args.date, "%Y-%m-%d")      # validate or raise
    items = _load()
    rid = _mint_id(args.date, args.text)
    if any(i.get("id") == rid for i in items):
        print(f"already exists: {rid}")
        return 0
    items.append({"id": rid, "date": args.date, "lead_days": args.lead_days,
                  "text": args.text, "source": args.source or "", "done": False})
    _save(items)
    print(f"added {rid} — surfaces {args.lead_days}d before {args.date}")
    return 0


def cmd_list(args) -> int:
    items = _load()
    if not args.all:
        items = [i for i in items if not i.get("done")]
    if not items:
        print("no reminders")
        return 0
    for i in items:
        flag = "✓" if i.get("done") else " "
        print(f"[{flag}] {i['id']}  {i['date']}  {i['text']}")
    return 0


def cmd_due(args) -> int:
    live = due_reminders()
    if not live:
        print("nothing in window")
        return 0
    for line in render_reminders():
        print(line)
    return 0


def cmd_done(args) -> int:
    items = _load()
    hit = False
    for i in items:
        if i.get("id") == args.id:
            i["done"] = True
            i["closed_at"] = _today().isoformat()
            hit = True
    if not hit:
        print(f"no reminder with id {args.id}", file=sys.stderr)
        return 1
    _save(items)
    print(f"closed {args.id}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("--date", required=True, help="YYYY-MM-DD")
    a.add_argument("--text", required=True)
    a.add_argument("--lead-days", type=int, default=DEFAULT_LEAD_DAYS)
    a.add_argument("--source", default="")
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list")
    l.add_argument("--all", action="store_true")
    l.set_defaults(func=cmd_list)

    sub.add_parser("due").set_defaults(func=cmd_due)

    d = sub.add_parser("done")
    d.add_argument("id")
    d.set_defaults(func=cmd_done)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
