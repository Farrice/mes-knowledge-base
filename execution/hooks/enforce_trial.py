#!/usr/bin/env python3
"""enforce_trial.py — shared reader for Wave-2 graduated-enforcement trial files.

One gate = one JSON file under .agent/enforce-trials/<gate>.json:
    {"gate": "...", "active": bool, "starts": "YYYY-MM-DD", "ends": "YYYY-MM-DD",
     "override": "<documented escape hatch>", "revert": "set active:false"}

Semantics (identical to the live routing trial, .agent/routing-enforce-trial.json,
which predates this helper and keeps its own path — do not migrate a live gate):
  - active:false  → gate stays observe/warn-only (DORMANT — the shipped default)
  - active:true   → enforce, but only between starts and ends inclusive
  - past ends     → auto-expired, observe-only again (weekly review decides permanence)

Activation on the due date is ONE FIELD (active:false → true) — deliberately
executable by any conductor tier, no Fable/Opus judgment required.
"""
import json
from datetime import date
from pathlib import Path

TRIALS_DIR = Path(__file__).resolve().parents[2] / ".agent" / "enforce-trials"


def active_trial(gate: str) -> dict | None:
    """Return the trial dict if <gate> is actively enforcing today, else None."""
    try:
        t = json.loads((TRIALS_DIR / f"{gate}.json").read_text())
    except (OSError, ValueError):
        return None
    if not t.get("active"):
        return None
    today = date.today().isoformat()
    if today < str(t.get("starts", "0000-01-01")) or today > str(t.get("ends", "9999-12-31")):
        return None
    return t
