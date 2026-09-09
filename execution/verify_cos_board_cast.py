#!/usr/bin/env python3
"""
Sabotage gate for cos_board_cast.py (pattern: verify_cos_primer_gate.py).

Verification-spine rule: every check proven in BOTH directions before trust —
the caster must select the right seats when the signal is there (detect) AND
fail loudly / fall back honestly when inputs are broken or signal-free (reject).
If a future change lets either direction slip, this exits 1 and says which.

Run: python3 execution/verify_cos_board_cast.py   (exit 0 = all pass)
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cos_board_cast import BOARD, CastError, cast  # noqa: E402

# ── synthetic fixtures ───────────────────────────────────────────────

REVENUE_BRIEF = """# Morning Brief — 2026-01-05 (Monday)
**Streak:** 3

## Goal pulse
- revenue-5k — on track

## 💰 Outer Loop
- 12 outcome check-ins overdue; collected cash stalled, revenue ask unsent
- Close the client offer today: pricing confirmed, sales sprint day 4, cash collected $4,650
"""

SYSTEMS_BRIEF = """# Morning Brief — 2026-01-06 (Tuesday)
**Streak:** 4

## On deck
- Threads drifting: 9 open loops, systems bottleneck in triage, process drift unnamed
- Park or kill the stale threads; the bottleneck is time triage
"""

LIFE_BRIEF = """# Morning Brief — 2026-01-07 (Wednesday)
**Streak:** 5

## On deck
- JJ dental recheck today; Jen carrying the week solo; sleep debt 3 nights
- Health recommit due; father presence goal review; mindset drift under family stress
"""

TIE_BRIEF = """# Morning Brief — 2026-01-08 (Thursday)
**Streak:** 6

## On deck
- One revenue item and one family item, equal weight
"""

# Every mandate-ish token appears ONLY as a filename or inside backticks —
# a correct scorer sees zero signal; a broken one hands out phantom hits.
POLLUTED_BRIEF = """# Morning Brief — 2026-01-09 (Friday)
**Streak:** 7

## On deck
- [life-context.md § Notes](x/life-context.md) needs nothing
- run `python3 execution/revenue_tracker.py due` and check revenue-outcomes.json
- see health-report.md and family-notes.md and focus-today.py
"""

SYNTH_LEDGER = """# Board Ledger

### 2026-01-01
- [CFO: Alex Hormozi]: Send the invoice today | callback: first sitting
- [Chairman: Dr. K]: Ten minutes with JJ, phone away | callback: first sitting

### 2026-01-02
- [CFO: Alex Hormozi]: Log the collected cash | callback: followed
"""

BROKEN_BOARD_NO_MARKERS = """# The Standing Board — Charter
| Seat | Expert | Skill Dir | Mandate | Slot | Mandate Keywords |
|---|---|---|---|---|---|
| CEO | Justin Welsh | skills/justin-welsh-solopreneur | Focus | Spine | focus ship |
"""

BROKEN_BOARD_BAD_DIR = """# Charter
<!-- BEGIN:seat-table -->
| Seat | Expert | Skill Dir | Mandate | Slot | Mandate Keywords |
|---|---|---|---|---|---|
| CEO | Justin Welsh | skills/DOES-NOT-EXIST | Focus | Spine | focus ship |
<!-- END:seat-table -->
"""

STAFFED_NAMES = {"Justin Welsh", "Alex Hormozi", "Dan Martell", "Dr. K", "Robert Greene"}

FAILURES: list = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  {'✓' if ok else '✗'} {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(name)


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="verify_board_cast_"))

    def write(name: str, text: str) -> Path:
        p = tmp / name
        p.write_text(text, encoding="utf-8")
        return p

    ledger = write("ledger.md", SYNTH_LEDGER)

    print("Direction 1 — DETECT (right seats when the signal is there):")

    r = cast(write("rev.md", REVENUE_BRIEF), ledger_path=ledger)
    seats = [a["seat"] for a in r["advisors"]]
    check("revenue-heavy brief seats the CFO", "CFO" in seats, f"got {seats}")
    check("daily sitting is exactly 3 advisors", len(r["advisors"]) == 3, f"got {len(r['advisors'])}")
    for a in r["advisors"]:
        missing = {"seat", "name", "genius_path", "mandate", "ledger_lines"} - set(a)
        check(f"contract keys present ({a['seat']})", not missing, f"missing {missing}")
    check("top-level contract keys", {"advisors", "situation", "mode"} <= set(r),
          f"got {sorted(r)}")
    check("mode is 'daily'", r["mode"] == "daily")
    check("genius paths exist on disk",
          all((BOARD.parents[2] / a["genius_path"]).is_dir() for a in r["advisors"]),
          str([a["genius_path"] for a in r["advisors"]]))
    check("specialist never duplicates a staffed expert",
          all(a["name"] not in STAFFED_NAMES for a in r["advisors"] if a["seat"] == "Specialist"))

    cfo = next(a for a in r["advisors"] if a["seat"] == "CFO")
    check("CFO gets own ledger lines only",
          len(cfo["ledger_lines"]) == 2 and all("JJ" not in ln for ln in cfo["ledger_lines"]),
          str(cfo["ledger_lines"]))

    s = cast(write("sys.md", SYSTEMS_BRIEF), ledger_path=ledger)
    check("systems-heavy brief seats the COO",
          "COO" in [a["seat"] for a in s["advisors"]],
          str([a["seat"] for a in s["advisors"]]))

    life = cast(write("life.md", LIFE_BRIEF), ledger_path=ledger)
    check("life-dominant brief seats the Chairman",
          "Chairman" in [a["seat"] for a in life["advisors"]],
          str([(a["seat"], a.get("score")) for a in life["advisors"]]))

    r2 = cast(write("rev2.md", REVENUE_BRIEF), ledger_path=ledger)
    check("deterministic: same brief → identical cast",
          json.dumps(r, sort_keys=True) == json.dumps(r2, sort_keys=True))

    w = cast(write("rev3.md", REVENUE_BRIEF), mode="weekly", ledger_path=ledger)
    check("weekly mode seats all 5 staffed, no specialist",
          len(w["advisors"]) == 5 and all(a["seat"] != "Specialist" for a in w["advisors"]))

    print("Direction 2 — REJECT (loud failure / honest fallback on bad input):")

    tie = cast(write("tie.md", TIE_BRIEF), ledger_path=ledger)
    check("Chairman tie does NOT win a daily slot (gate holds)",
          "Chairman" not in [a["seat"] for a in tie["advisors"]],
          str([(a["seat"], a.get("score")) for a in tie["advisors"]]))

    pol = cast(write("pol.md", POLLUTED_BRIEF), ledger_path=ledger)
    check("filename/backtick tokens give NO phantom relevance (zero-signal fallback)",
          any("zero-signal" in n for n in pol.get("casting_notes", [])),
          str(pol.get("casting_notes")))

    try:
        cast(tmp / "nope.md", ledger_path=ledger)
        check("missing brief fails loudly", False, "no error raised")
    except CastError:
        check("missing brief fails loudly", True)

    try:
        cast(write("rev4.md", REVENUE_BRIEF), board_path=write("empty.md", ""), ledger_path=ledger)
        check("empty board charter fails loudly", False, "no error raised")
    except CastError:
        check("empty board charter fails loudly", True)

    try:
        cast(write("rev5.md", REVENUE_BRIEF),
             board_path=write("nomark.md", BROKEN_BOARD_NO_MARKERS), ledger_path=ledger)
        check("charter without seat-table markers fails loudly", False, "no error raised")
    except CastError:
        check("charter without seat-table markers fails loudly", True)

    try:
        cast(write("rev6.md", REVENUE_BRIEF),
             board_path=write("baddir.md", BROKEN_BOARD_BAD_DIR), ledger_path=ledger)
        check("charter pointing at a missing skill dir fails loudly", False, "no error raised")
    except CastError as e:
        check("charter pointing at a missing skill dir fails loudly",
              "DOES-NOT-EXIST" in str(e), str(e))

    try:
        cast(write("blank.md", "   \n"), ledger_path=ledger)
        check("empty brief fails loudly", False, "no error raised")
    except CastError:
        check("empty brief fails loudly", True)

    print()
    if FAILURES:
        print(f"FAIL — {len(FAILURES)} check(s): {FAILURES}")
        return 1
    print("PASS — cos_board_cast verified in both directions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
