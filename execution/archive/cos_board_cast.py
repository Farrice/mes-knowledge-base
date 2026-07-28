#!/usr/bin/env python3
"""
COS Board Cast — seating adapter for the Standing Board (COS v3, 2026-07-14).

Reads the seat charter from .agent/cos/board.md and today's data appendix
(the cos_prep.py brief), then picks who sits today:

  daily : the 2 staffed seats most relevant to the live situation
          + 1 rotating specialist cast via council_cast.py (strike mode).
          Chairman only wins a daily slot when its life-signal relevance
          DOMINATES (>= every other seat's score) — the board polices
          revenue/shipping by default, life when life is loud.
  weekly: all 5 staffed seats + tight-mode wildcards.

Pure planning logic, stdlib-only, $0, deterministic (date-seeded tie-breaks).
Consumed by skills/chief-of-staff-os/workflows/cos-daily.md / cos-weekly.md.

CLI:
    python3 execution/cos_board_cast.py --brief .agent/cos/briefs/YYYY-MM-DD.md
    python3 execution/cos_board_cast.py --brief <path> --weekly
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / ".agent" / "cos" / "board.md"
LEDGER = ROOT / ".agent" / "cos" / "board-ledger.md"

sys.path.insert(0, str(ROOT / "execution"))
from council_cast import build_council_plan, _keywords  # noqa: E402

DAILY_STAFFED_SEATS = 2
DAILY_TOTAL_CAP = 3  # hard token cap: never more than 3 advisor sub-agents


def parse_seat_table(text: str | None = None) -> list[dict]:
    """Parse the BEGIN:seat-table block in board.md into seat dicts."""
    text = text if text is not None else BOARD.read_text(encoding="utf-8")
    m = re.search(r"<!-- BEGIN:seat-table.*?-->\n(.*?)<!-- END:seat-table -->",
                  text, re.DOTALL)
    if not m:
        return []
    seats = []
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("Seat", "---") or cells[0].startswith("-"):
            continue
        seats.append({
            "seat": cells[0],
            "name": cells[1],
            "skill_dir": cells[2],
            "mandate": cells[3],
            "slot": cells[4],
            "mandate_keywords": cells[5],
            "genius_path": f"{cells[2]}/genius.md",
        })
    return seats


def build_situation(brief_path: Path) -> str:
    """Distill the data appendix into a situation string for relevance scoring.
    Keeps headline content, drops command lines / provenance / markup noise."""
    try:
        text = brief_path.read_text(encoding="utf-8")
    except Exception:
        return ""
    keep: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("<!--", "↳", "#", "**Streak")):
            continue
        if "`python3" in s or s.startswith("- Data:") or s.startswith("- Full pulse:"):
            continue
        keep.append(s.lstrip("-*0123456789. ").strip())
    return " ".join(keep)[:4000]


def ledger_lines(name: str, limit: int = 5) -> list[str]:
    """The advisor's own most recent ledger lines (accountability callbacks)."""
    try:
        lines = [l for l in LEDGER.read_text(encoding="utf-8").splitlines()
                 if f": {name}]" in l or f"[{name}" in l or f" {name}]" in l]
        return lines[-limit:]
    except Exception:
        return []


def _score(seat: dict, situation_kws: set) -> int:
    seat_kws = _keywords(seat["mandate_keywords"] + " " + seat["mandate"])
    return len(seat_kws & situation_kws)


def _stable_tiebreak(date_str: str, seat: str) -> int:
    return int(hashlib.md5(f"{date_str}|{seat}".encode()).hexdigest(), 16) % 1000


def cast(brief_path: Path, weekly: bool = False, date_str: str = "") -> dict:
    date_str = date_str or datetime.now().date().isoformat()
    seats = parse_seat_table()
    if not seats:
        return {"error": "no seat table found in .agent/cos/board.md"}
    situation = build_situation(brief_path)
    situation_kws = _keywords(situation)

    if weekly:
        chosen = list(seats)
        plan = build_council_plan(situation or "weekly board session", mode="tight")
        staffed_names = {s["name"].lower() for s in seats}
        wildcards = [
            {"seat": "Wildcard", "name": r["name"], "skill_dir": "",
             "mandate": r["core_method"], "slot": "Wildcard",
             "genius_path": r.get("genius_path")}
            for r in plan["roster"]
            if r.get("wildcard") and r["name"].lower() not in staffed_names
        ]
        advisors = chosen + wildcards
        mode = "weekly"
    else:
        scored = sorted(
            seats,
            key=lambda s: (_score(s, situation_kws),
                           _stable_tiebreak(date_str, s["seat"])),
            reverse=True,
        )
        # Chairman dominance rule: only sits daily when its life-signal score
        # >= every other seat's score (life is loud today).
        chairman = next((s for s in scored if s["seat"] == "Chairman"), None)
        others = [s for s in scored if s["seat"] != "Chairman"]
        if chairman and _score(chairman, situation_kws) >= max(
                (_score(s, situation_kws) for s in others), default=0):
            chosen = [chairman] + others[:DAILY_STAFFED_SEATS - 1]
        else:
            chosen = others[:DAILY_STAFFED_SEATS]

        # Rotating specialist via strike-mode relevance cast, dedup vs staffed.
        staffed_names = {s["name"].lower() for s in seats}
        specialist = None
        plan = build_council_plan(situation or "operator daily briefing",
                                  mode="strike")
        for r in plan["roster"]:
            if r.get("is_user") or not r.get("genius_path"):
                continue
            if r["name"].lower() in staffed_names:
                continue
            specialist = {"seat": "Specialist", "name": r["name"],
                          "skill_dir": str(Path(r["genius_path"]).parent),
                          "mandate": r["core_method"], "slot": "Specialist",
                          "genius_path": r["genius_path"]}
            break
        advisors = chosen + ([specialist] if specialist else [])
        advisors = advisors[:DAILY_TOTAL_CAP]
        mode = "daily"

    for a in advisors:
        a["ledger_lines"] = ledger_lines(a["name"])
        a["score"] = _score(a, situation_kws) if a.get("mandate_keywords") else None
    return {
        "date": date_str,
        "mode": mode,
        "advisor_count": len(advisors),
        "situation": situation[:600],
        "advisors": advisors,
    }


def main() -> int:
    p = argparse.ArgumentParser(prog="cos_board_cast.py")
    p.add_argument("--brief", required=True, help="path to today's data appendix")
    p.add_argument("--weekly", action="store_true")
    p.add_argument("--date", default="", help="override date for deterministic tests")
    a = p.parse_args()
    print(json.dumps(cast(Path(a.brief), weekly=a.weekly, date_str=a.date),
                     indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
