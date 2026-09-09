#!/usr/bin/env python3
"""
COS Board Cast — deterministic Step-1 caster for the Standing Board daily sitting.

Reads the morning brief (data appendix), the seat charter in .agent/cos/board.md
(the BEGIN:seat-table block is marked for this script), and .agent/cos/board-ledger.md,
then scores each staffed seat's Mandate Keywords against the brief and returns the
casting JSON the /cos daily workflow (skills/chief-of-staff-os/workflows/cos-daily.md
Step 1) documents:

    {advisors: [{seat, name, genius_path, mandate, ledger_lines}], situation, mode}

Daily mode = 2 most-relevant staffed seats + 1 rotating specialist (cast via
council_cast.py strike-mode relevance: top card not duplicating a staffed expert;
rotation comes from the situation changing daily). Weekly = all 5 staffed seats.

Charter rules honored (board.md Rotation Rules):
- Chairman wins a daily slot only when life signals dominate — implemented as:
  Chairman is eligible for the top-2 only when it strictly outranks every other
  staffed seat.
- genius_path is the expert's skill DIRECTORY (Step 2 loads files from it).

Privacy boundary (board.md, BINDING): keyword scoring runs over the full brief
locally, but the emitted `situation` string — which enters sub-agent prompts —
carries only allowlisted sections (streak, goal pulse, on deck, outer-loop
numbers, world pulse) plus a neutral life-staleness digest (section name + days,
nothing else). Question bodies and life specifics never enter it.

Stdlib-only, zero model calls. Exit 0 = casting JSON on stdout; exit 2 = error
JSON on stdout (loud failure, never a silent fallback).

CLI:
    python3 execution/cos_board_cast.py --brief .agent/cos/briefs/YYYY-MM-DD.md
        [--mode daily|weekly] [--ledger-lines 3]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / ".agent" / "cos" / "board.md"
LEDGER = ROOT / ".agent" / "cos" / "board-ledger.md"

DAILY_STAFFED = 2          # staffed seats in a daily sitting (charter: lean)
KEYWORD_CAP = 5            # per-keyword occurrence cap so one repeated token can't dominate


class CastError(Exception):
    pass


# ── board.md seat table ──────────────────────────────────────────────

def parse_seats(board_path: Path) -> List[Dict]:
    if not board_path.exists():
        raise CastError(f"board charter missing: {board_path}")
    text = board_path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"<!--\s*BEGIN:seat-table.*?-->(.*?)<!--\s*END:seat-table\s*-->",
                  text, re.DOTALL)
    if not m:
        raise CastError(f"seat-table markers not found in {board_path} "
                        "(BEGIN:seat-table / END:seat-table)")
    seats: List[Dict] = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("Seat", "") or set(cells[0]) <= {"-", " "}:
            continue
        seat, expert, skill_dir, mandate, slot, kw = cells[:6]
        keywords = [k for k in kw.split() if k]
        if not keywords:
            raise CastError(f"seat {seat} has no Mandate Keywords in the charter table")
        seats.append({
            "seat": seat, "name": expert, "skill_dir": skill_dir,
            "mandate": mandate, "slot": slot, "keywords": keywords,
        })
    if not seats:
        raise CastError(f"seat-table in {board_path} parsed to zero seats")
    for s in seats:
        if not (ROOT / s["skill_dir"]).is_dir():
            raise CastError(f"seat {s['seat']} ({s['name']}): skill dir not found: "
                            f"{s['skill_dir']} — fix the charter table")
    return seats


# ── keyword scoring ──────────────────────────────────────────────────

def _clean_for_scoring(text: str) -> str:
    """Strip inline code and markdown link targets so file paths and close
    commands (e.g. `.agent/health/...`, `revenue_tracker.py ...`) don't create
    phantom mandate relevance."""
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"\]\([^)\n]*\)", "] ", text)
    # filenames in link text (life-context.md, revenue-outcomes.json) are paths,
    # not situation signal — they'd hand seats phantom keyword hits
    text = re.sub(r"\S+\.(?:md|py|json|log|txt|ya?ml)\b", " ", text)
    return text.lower()


def score_seat(keywords: List[str], cleaned_brief: str) -> Tuple[int, Dict[str, int]]:
    total, hits = 0, {}
    for kw in keywords:
        n = len(re.findall(r"\b" + re.escape(kw.lower()) + r"\b", cleaned_brief))
        n = min(n, KEYWORD_CAP)
        if n:
            hits[kw] = n
            total += n
    return total, hits


# ── ledger lines (own seat only) ─────────────────────────────────────

_LEDGER_LINE = re.compile(
    r"^\s*(?:-\s*)?\*{0,2}\[(?P<seat>[^:\]]+):\s*(?P<name>[^\]]+)\]\*{0,2}:?\s*(?P<body>.+)$")
_DATE_HEAD = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})")


def ledger_lines_for(name: str, ledger_path: Path, limit: int) -> List[str]:
    if not ledger_path.exists():
        return []
    out: List[str] = []
    current_date = ""
    target = name.casefold().strip()
    for line in ledger_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        dm = _DATE_HEAD.match(line)
        if dm:
            current_date = dm.group(1)
            continue
        lm = _LEDGER_LINE.match(line)
        if lm and lm.group("name").casefold().strip() == target:
            prefix = f"{current_date}: " if current_date else ""
            out.append(prefix + lm.group("body").strip())
    return out[-limit:]


# ── situation string (privacy-allowlisted) ───────────────────────────

def _section(text: str, header_pattern: str) -> List[str]:
    """Top-level bullets of the first section whose ## header matches the pattern."""
    lines = text.splitlines()
    out, inside = [], False
    for ln in lines:
        if ln.startswith("## "):
            inside = bool(re.search(header_pattern, ln, re.IGNORECASE))
            continue
        if inside and re.match(r"^- \S", ln):
            out.append(re.sub(r"\]\([^)\n]*\)", "]", ln[2:]).strip())
    return out


def build_situation(brief_text: str) -> str:
    parts: List[str] = []
    for ln in brief_text.splitlines():
        if ln.startswith("# "):
            parts.append(ln[2:].strip())
            break
    m = re.search(r"^\*\*Streak:.*$", brief_text, re.MULTILINE)
    if m:
        parts.append(re.sub(r"\*", "", m.group(0)).strip())
    goals = _section(brief_text, r"Goal pulse")
    if goals:
        parts.append("Goals: " + "; ".join(goals))
    deck = _section(brief_text, r"On deck")
    if deck:
        parts.append("On deck: " + "; ".join(deck))
    outer = _section(brief_text, r"Outer Loop")
    keep = [b for b in outer if re.search(r"check-ins|revenue", b, re.IGNORECASE)]
    if keep:
        parts.append("Outer loop: " + "; ".join(keep))
    pulse = _section(brief_text, r"World pulse")
    if pulse:
        parts.append("World pulse: " + "; ".join(pulse))
    stale = re.findall(r"life-context\.md\s*§\s*([\w &]+)\].*?(\d+)d since update",
                       brief_text)
    if stale:
        parts.append("Life-context staleness: "
                     + "; ".join(f"{sec.strip()} {d}d" for sec, d in stale))
    return " | ".join(parts)[:1500]


# ── rotating specialist ──────────────────────────────────────────────

def _name_tokens(name: str) -> set:
    base = re.split(r"[—(—]", name)[0]
    return {t for t in re.findall(r"[a-z]+", base.casefold()) if len(t) > 2}


def cast_specialist(situation: str, staffed: List[Dict],
                    ledger_path: Path, ledger_n: int) -> Optional[Dict]:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import council_cast  # deterministic, no network

    plan = council_cast.build_council_plan(situation, mode="strike")
    staffed_tokens = set()
    for s in staffed:
        staffed_tokens |= _name_tokens(s["name"])
    eligible = []
    for card in plan["roster"]:
        if card.get("is_user") or not card.get("genius_path"):
            continue
        if _name_tokens(card["name"]) & staffed_tokens:
            continue  # never duplicate a staffed expert
        eligible.append(card)
    if not eligible:
        return None
    # charter: "top invocation-card not duplicating a staffed expert" — rotation
    # comes from the situation changing daily, not from an artificial cycle
    card = eligible[0]
    name = re.split(r"\s+—\s+", card["name"])[0].strip()
    skill_dir = str(Path(card["genius_path"]).parent)
    return {
        "seat": "Specialist",
        "name": name,
        "genius_path": skill_dir,
        "mandate": f"Rotating specialist — {card.get('lens') or card.get('core_method', '')}".strip(" —"),
        "ledger_lines": ledger_lines_for(name, ledger_path, ledger_n),
    }


# ── casting ──────────────────────────────────────────────────────────

def cast(brief_path: Path, mode: str = "daily", ledger_n: int = 3,
         board_path: Path = BOARD, ledger_path: Path = LEDGER) -> Dict:
    if not brief_path.exists():
        raise CastError(f"brief not found: {brief_path} — run "
                        "`python3 execution/cos_prep.py prep` first")
    brief_text = brief_path.read_text(encoding="utf-8", errors="ignore")
    if not brief_text.strip():
        raise CastError(f"brief is empty: {brief_path}")
    seats = parse_seats(board_path)
    cleaned = _clean_for_scoring(brief_text)
    for i, s in enumerate(seats):
        s["charter_order"] = i
        s["score"], s["keyword_hits"] = score_seat(s["keywords"], cleaned)

    situation = build_situation(brief_text)
    notes: List[str] = []

    def advisor(s: Dict) -> Dict:
        return {
            "seat": s["seat"],
            "name": s["name"],
            "genius_path": s["skill_dir"],
            "mandate": s["mandate"],
            "ledger_lines": ledger_lines_for(s["name"], ledger_path, ledger_n),
            "score": s["score"],
        }

    if mode == "weekly":
        return {"advisors": [advisor(s) for s in seats],
                "situation": situation, "mode": "weekly",
                "casting_notes": notes}

    ranked = sorted(seats, key=lambda s: (-s["score"], s["charter_order"]))
    chairman = next((s for s in seats if s["seat"].casefold() == "chairman"), None)
    if chairman is not None:
        top_other = max(s["score"] for s in seats if s is not chairman)
        if chairman["score"] <= top_other:
            ranked = [s for s in ranked if s is not chairman]
            notes.append("Chairman skipped: life signals do not dominate "
                         f"(score {chairman['score']} vs top {top_other})")
        else:
            notes.append(f"Chairman seated: life signals dominate (score {chairman['score']})")

    if all(s["score"] == 0 for s in seats):
        ranked = [s for s in seats if s["seat"] in ("CEO", "CFO")]
        notes.append("zero-signal brief: fell back to CEO + CFO (Spine + Risk Gate)")

    picked = ranked[:DAILY_STAFFED]
    advisors = [advisor(s) for s in picked]

    specialist = cast_specialist(situation, seats, ledger_path, ledger_n)
    if specialist is not None:
        advisors.append(specialist)
    else:
        bench = [s for s in ranked if s not in picked]
        if bench:
            advisors.append(advisor(bench[0]))
            notes.append(f"no eligible specialist card — seated next staffed seat "
                         f"({bench[0]['seat']}) instead")
        else:
            notes.append("no eligible specialist card and no bench seat — sitting with 2")

    skipped = [s["seat"] for s in seats
               if s["seat"] not in {a["seat"] for a in advisors}]
    if skipped:
        notes.append("skipped seats: " + ", ".join(skipped))

    return {"advisors": advisors, "situation": situation, "mode": "daily",
            "casting_notes": notes}


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(prog="cos_board_cast.py",
                                description="Cast the Standing Board for a sitting (deterministic, $0).")
    p.add_argument("--brief", required=True, help="path to the morning brief data appendix")
    p.add_argument("--mode", default="daily", choices=["daily", "weekly"])
    p.add_argument("--ledger-lines", type=int, default=3,
                   help="prior ledger lines per advisor (own seat only)")
    a = p.parse_args(argv)
    try:
        result = cast(Path(a.brief), mode=a.mode, ledger_n=a.ledger_lines)
    except CastError as e:
        print(json.dumps({"error": str(e)}, indent=2))
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
