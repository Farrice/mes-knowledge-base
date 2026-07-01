#!/usr/bin/env python3
"""claude_export_state.py — shared checkpoint for the claude.ai export import pipeline.

One JSON file (`_active/claude-export/state.json`) tracks every stage's progress at
conversation granularity so the whole import is resumable across sessions: kill any
stage, re-run it, and it continues from the last-marked key.

Every stage script (parser / triage / ingest) imports this module and follows the
contract:  before doing work on a key call `is_done(state, stage, key)`; after success
call `mark(state, stage, key, ...)` then `save_state(state)`.

Writes are atomic (write to `.tmp` sibling, then `os.replace`) — a reader never sees a
half-written checkpoint even if the process dies mid-write.

This module has NO network and NO LLM. It is imported, not run directly (though
`python3 execution/claude_export_state.py` prints a status summary for convenience).
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

ROOT = Path(__file__).resolve().parents[1]

# ── Path layout (all git-ignored; code + docs are the only tracked artifacts) ──
# Small derived JSON (state, index, triage, menu) — kept for Farrice's use, git-ignored.
EXPORT_DIR = ROOT / "_active" / "claude-export"
STATE_PATH = EXPORT_DIR / "state.json"
INDEX_PATH = EXPORT_DIR / "index.json"
TRIAGE_DIR = EXPORT_DIR / "triage"
REPORTS_DIR = EXPORT_DIR / "reports"

# Raw private transcripts + bulky redacted markdown live under the .tmp tree
# (already git-ignored via `.tmp/`), never committed.
RAW_DIR = ROOT / ".tmp" / "claude-export" / "raw"
NORMALIZED_DIR = ROOT / ".tmp" / "claude-export" / "normalized"
CONV_MD_DIR = NORMALIZED_DIR / "conversations"
PROJ_MD_DIR = NORMALIZED_DIR / "projects"
MEM_MD_DIR = NORMALIZED_DIR / "memories"

# The stages the pipeline advances a conversation through, in order.
STAGES = ("parsed", "triaged", "ingested", "embedded", "extracted")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _skeleton() -> Dict[str, Any]:
    """A fresh state document."""
    return {
        "version": 1,
        "started_at": _now(),
        "updated_at": _now(),
        "download": {"manifest_path": None, "batches": []},
        "stages": {s: {} for s in STAGES},
        "counts": {},
        "notes": [],
    }


def load_state() -> Dict[str, Any]:
    """Return the state dict, or a fresh skeleton if none exists.

    Tolerates a corrupt/empty file by falling back to a skeleton (the stages are
    idempotent, so a lost checkpoint costs re-work, never wrong results)."""
    if not STATE_PATH.exists():
        return _skeleton()
    try:
        data = json.loads(STATE_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return _skeleton()
    # Forward-compat: ensure every known stage bucket exists.
    data.setdefault("stages", {})
    for s in STAGES:
        data["stages"].setdefault(s, {})
    data.setdefault("download", {"manifest_path": None, "batches": []})
    data.setdefault("counts", {})
    data.setdefault("notes", [])
    return data


def save_state(state: Dict[str, Any]) -> None:
    """Atomically persist the state dict."""
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = _now()
    tmp = STATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2))
    os.replace(tmp, STATE_PATH)  # atomic on POSIX


def mark(state: Dict[str, Any], stage: str, key: str, value: Optional[Dict[str, Any]] = None) -> None:
    """Record that `key` completed `stage`. `value` merges extra fields into the record."""
    if stage not in state["stages"]:
        state["stages"][stage] = {}
    rec: Dict[str, Any] = {"done_at": _now()}
    if value:
        rec.update(value)
    state["stages"][stage][key] = rec


def is_done(state: Dict[str, Any], stage: str, key: str) -> bool:
    """Idempotency gate: has `key` already completed `stage`?"""
    return key in state.get("stages", {}).get(stage, {})


def stage_counts(state: Dict[str, Any]) -> Dict[str, int]:
    """{stage: number of completed keys} for status/stats views."""
    return {s: len(state.get("stages", {}).get(s, {})) for s in STAGES}


def record_download(state: Dict[str, Any], name: str, sha256: str, nbytes: int,
                    url_fingerprint: str = "") -> None:
    """Register a downloaded raw batch and flag its single-use URL as consumed.

    Guards the single-use constraint: a batch with `single_use_consumed=True` must
    never be re-fetched — the pipeline works from the on-disk raw file thereafter."""
    batches = state["download"].setdefault("batches", [])
    for b in batches:
        if b.get("name") == name:  # update in place
            b.update({"sha256": sha256, "bytes": nbytes,
                      "url_fingerprint": url_fingerprint or b.get("url_fingerprint", ""),
                      "downloaded_at": _now(), "single_use_consumed": True})
            return
    batches.append({
        "name": name, "sha256": sha256, "bytes": nbytes,
        "url_fingerprint": url_fingerprint, "downloaded_at": _now(),
        "single_use_consumed": True,
    })


def main() -> int:
    state = load_state()
    counts = stage_counts(state)
    print("─── CLAUDE EXPORT · PIPELINE STATE ───")
    print(f"  state file: {STATE_PATH}")
    print(f"  started:    {state.get('started_at', '?')}")
    print(f"  updated:    {state.get('updated_at', '?')}")
    print(f"  corpus:     {state.get('counts', {})}")
    print("  stage progress:")
    for s in STAGES:
        print(f"    {s:<10} {counts.get(s, 0)}")
    batches = state.get("download", {}).get("batches", [])
    print(f"  downloaded batches: {len(batches)}")
    for b in batches:
        flag = "consumed" if b.get("single_use_consumed") else "pending"
        print(f"    - {b.get('name')} · {b.get('bytes', 0)} bytes · {flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
