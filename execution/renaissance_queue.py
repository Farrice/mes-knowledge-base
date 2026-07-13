#!/usr/bin/env python3
"""renaissance_queue.py — build the next Prompt Renaissance wave input (deterministic, resumable).

Selects canonical prompts that don't yet have a structure-pure v2 (v2-exists check = the
resume mechanism), ranks money-path first, groups by skill (one fleet agent per group, no
shared files), writes `_active/prompt-renaissance/wave-input.json`.

Usage:
    python3 execution/renaissance_queue.py --wave-size 150     # next wave (default)
    python3 execution/renaissance_queue.py --wave-size 200 --include-extractions
    python3 execution/renaissance_queue.py --status            # remaining counts only

Standard + fleet-prompt template: _active/prompt-renaissance/04-deliverables/RUNBOOK.md
Legacy mirrors (skills/*/references/_legacy-prompts/) are duplicates of the canonical
prompts and are NEVER queued.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_active" / "prompt-renaissance"

MONEY = re.compile(r'iha|georgi|fladlien|halbert|sultanic|deutsch|cardinal|cimorelli|wiebe|clemens|'
                   r'brunson|hormozi|priestley|godin|kallaway|acosta|cole|brendan-kane|welsh|lakajev|'
                   r'dan-koe|justin-welsh|perell|mcgarry|monk-ai|copy|offer|content|hook|vsl|email|'
                   r'linkedin|extract|coach|brand|avatar|proof|newsletter|ghostwrit')


def candidates(include_extractions: bool):
    idx = json.loads((ROOT / ".agent" / "prompt-index.json").read_text())
    core = {s["id"] for s in json.loads((ROOT / ".agent" / "production-core.json").read_text())["skills"]}
    out = []
    for e in idx["entries"]:
        if e["kind"] == "skill-prompt":
            v2 = ROOT / Path(e["path"]).parent.parent / "prompts-v2" / Path(e["path"]).name
        elif e["kind"] == "extraction-prompt" and include_extractions:
            v2 = ROOT / Path(e["path"]).parent.parent / "prompts-v2" / Path(e["path"]).name
        else:
            continue  # legacy mirrors + already-v2 entries never queue
        if v2.exists():
            continue
        score = (10 if e["skill"] in core else 0) + (6 if MONEY.search(e["skill"]) else 0) \
              + (2 if MONEY.search(e["title"].lower()) else 0)
        out.append((score, e))
    out.sort(key=lambda x: (-x[0], x[1]["skill"]))
    return out


def main() -> int:
    # One-driver-per-tree guard (orchestration doctrine Law 5)
    import os as _os, subprocess as _sp
    _lock = _sp.run(["python3", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "session_lock.py"),
                     "check", _os.environ.get("SESSION_LOCK_TOKEN", "")], capture_output=True, text=True)
    if _lock.returncode != 0:
        print(_lock.stdout.strip() or "BLOCKED by session lock")
        return 1
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave-size", type=int, default=150)
    ap.add_argument("--include-extractions", action="store_true",
                    help="also queue extractions/*/prompts (the 42 raw-era originals)")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    cands = candidates(args.include_extractions)
    if args.status:
        print(f"remaining un-refactored canonical prompts: {len(cands)}")
        return 0

    wave = [e for _, e in cands[:args.wave_size]]
    groups: dict = {}
    for e in wave:
        groups.setdefault(e["skill"], []).append({"path": e["path"], "title": e["title"]})
    data = {"standard": "structure-pure-v2 (see _active/prompt-renaissance/04-deliverables/RUNBOOK.md)",
            "total": len(wave), "remaining_after_wave": len(cands) - len(wave),
            "groups": [{"skill": s, "prompts": ps}
                       for s, ps in sorted(groups.items(), key=lambda kv: -len(kv[1]))]}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "wave-input.json").write_text(json.dumps(data, indent=1))
    print(f"wave: {len(wave)} prompts · {len(groups)} skill groups · remaining after: {data['remaining_after_wave']}")
    print(f"→ {OUT / 'wave-input.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
