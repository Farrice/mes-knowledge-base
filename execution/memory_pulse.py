#!/usr/bin/env python3
"""memory_pulse.py — one-line second-brain state for the SessionStart digest.

Goal + scar (2026-08-21 second-brain audit): the memory stack wrote perfectly
and was never read — session_brief.py queried zero memory stores, the semantic
tier stalled 12 days, and the review queue's daily staleness alarm was ignored
26 straight days because it only printed into a launchd log nobody opens.
This script is the receipts-keyed surface: sovereign.db freshness, review-queue
age, and operator-ledger flow, compressed to one line for session_brief.py's
digest (its contract: first meaningful line only, alarms compressed never
swallowed). Nudge only — never blocks, always exits 0.

CLI: python3 execution/memory_pulse.py        # one line (or nothing if all quiet)
     python3 execution/memory_pulse.py --full # per-store breakdown
"""
from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / ".memory" / "sovereign.db"
LEDGER = ROOT / "knowledge" / "lessons" / "LEDGER.jsonl"

SEMANTIC_STALE_DAYS = 7
REVIEW_STALE_DAYS = 14


def _age_days(iso: str) -> float | None:
    try:
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - dt).total_seconds() / 86400.0
    except Exception:
        return None


def gather() -> dict:
    state: dict = {}
    if DB.exists():
        try:
            con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True, timeout=2.0)
            try:
                state["semantic_newest"] = con.execute(
                    "SELECT MAX(created_at) FROM memories WHERE tier = 'semantic'"
                ).fetchone()[0]
                state["semantic_count"] = con.execute(
                    "SELECT COUNT(*) FROM memories WHERE tier IN ('semantic', 'procedural')"
                ).fetchone()[0]
                row = con.execute(
                    "SELECT COUNT(*), MIN(created_at) FROM flagged_review WHERE status = 'pending'"
                ).fetchone()
                state["review_pending"], state["review_oldest"] = row or (0, None)
            finally:
                con.close()
        except Exception:
            pass
    if LEDGER.exists():
        try:
            week = 0
            total = 0
            cutoff = datetime.now(timezone.utc).timestamp() - 7 * 86400
            with open(LEDGER, encoding="utf-8") as fh:
                for ln in fh:
                    try:
                        rec = json.loads(ln)
                    except Exception:
                        continue
                    total += 1
                    age = _age_days(rec.get("ts", ""))
                    if age is not None and age <= 7:
                        week += 1
            state["lessons_total"] = total
            state["lessons_week"] = week
            _ = cutoff
        except Exception:
            pass
    return state


def one_line(state: dict) -> str:
    parts = []
    if "lessons_total" in state:
        parts.append(f"{state.get('lessons_week', 0)} lesson(s) this week ({state['lessons_total']} in ledger)")
    sem_age = _age_days(state.get("semantic_newest") or "")
    if sem_age is not None and sem_age > SEMANTIC_STALE_DAYS:
        parts.append(f"⚠ semantic tier stale {sem_age:.0f}d — distiller may be down")
    pending = state.get("review_pending") or 0
    if pending:
        oldest_age = _age_days(state.get("review_oldest") or "")
        if oldest_age is not None and oldest_age > REVIEW_STALE_DAYS:
            parts.append(
                f"⚠ {pending} memory review(s) pending, oldest {oldest_age:.0f}d — "
                f"python3 execution/memory_review.py list (~5 min)"
            )
        else:
            parts.append(f"{pending} memory review(s) pending")
    if not parts:
        return ""
    return "MEMORY: " + " · ".join(parts)


def main() -> int:
    state = gather()
    if "--full" in sys.argv:
        print(json.dumps(state, indent=2, default=str))
        return 0
    line = one_line(state)
    if line:
        print(line)
        surface = ROOT / "_active" / "farrice-brand" / "intelligence" / "index.html"
        if surface.exists():
            print("Intelligence layer: http://127.0.0.1:8765/intelligence")
    return 0


if __name__ == "__main__":
    sys.exit(main())
