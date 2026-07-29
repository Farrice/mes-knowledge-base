#!/usr/bin/env python3
"""SessionStart beacon: surface the active campaign so no session starts cold.

Compass, never cage — prints a short deterministic pointer (campaign, next open
mission, standard) and exits 0 no matter what. If there is no active campaign,
it says nothing at all. Farrice's worst-day floor: the next session always
knows where the beat is, even if nobody remembers to ask.

Pointer file: .agent/active-campaign.json
  {"campaign": "<name>", "file": "<repo-relative CAMPAIGN.md path>"}
Deactivate by deleting the pointer file or setting {"active": false}.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POINTER = ROOT / ".agent" / "active-campaign.json"


def main() -> int:
    if not POINTER.exists():
        return 0
    try:
        ptr = json.loads(POINTER.read_text())
    except (json.JSONDecodeError, OSError):
        return 0
    if ptr.get("active") is False:
        return 0
    camp_file = ROOT / ptr.get("file", "")
    if not camp_file.exists():
        print(f"CAMPAIGN BEACON: pointer names {ptr.get('file')} but the file is missing — fix or delete .agent/active-campaign.json")
        return 0

    text = camp_file.read_text()
    open_missions = re.findall(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(?:🔴|⚪)\s*(OPEN[^|]*)\|", text, re.M)
    goal_m = re.search(r"^\*\*Goal:\*\*\s*(.+)$", text, re.M)

    lines = [f"ACTIVE CAMPAIGN (deterministic, from campaign_beacon.py): {ptr.get('campaign', camp_file.parent.name)}"]
    if goal_m:
        lines.append(f"  Goal: {goal_m.group(1).strip()}")
    if open_missions:
        top = open_missions[0]
        lines.append(f"  NEXT OPEN MISSION → #{top[0]}: {top[1].strip()}")
        if len(open_missions) > 1:
            rest = ", ".join(f"#{m[0]}" for m in open_missions[1:4])
            lines.append(f"  Also open: {rest}")
    lines.append(f"  Read {ptr.get('file')} before starting campaign work; update its queue at close. Standard: the five-move recipe (knowledge/lessons/2026-07-28-replication-lesson.md).")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
