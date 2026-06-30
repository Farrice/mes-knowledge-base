#!/usr/bin/env python3
"""Verify the existing session-state freshness loop without touching real state."""

from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import checkpoint_manager  # noqa: E402


def parse_last_updated(text: str) -> datetime:
    for line in text.splitlines():
        if line.startswith("> Last updated: "):
            raw = line.split(": ", 1)[1].strip()
            return datetime.strptime(raw, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    raise AssertionError("session-state anchor missing Last updated line")


def main() -> int:
    original_cwd = Path.cwd()
    try:
        with tempfile.TemporaryDirectory(prefix="session-state-freshness-") as tmp:
            os.chdir(tmp)
            state_path = Path(
                checkpoint_manager.save_session_state(
                    active_task="Verify session-state freshness loop",
                    key_findings=["Freshness verifier writes a current temp anchor"],
                    current_phase="verification",
                    next_steps=["Keep chain_runner finalize as the existing freshness path"],
                )
            )
            if state_path != Path(".agent/session-state.md"):
                raise AssertionError(f"unexpected session-state path: {state_path}")
            if not state_path.exists():
                raise AssertionError("session-state freshness verifier did not write a state file")

            text = state_path.read_text(encoding="utf-8")
            required = (
                "# Session State Anchor",
                "## Active Task",
                "Verify session-state freshness loop",
                "## Key Findings (Compressed)",
                "## Next Steps",
            )
            missing = [snippet for snippet in required if snippet not in text]
            if missing:
                raise AssertionError("session-state anchor missing text: " + ", ".join(missing))

            age_seconds = (datetime.now(timezone.utc) - parse_last_updated(text)).total_seconds()
            if age_seconds < 0 or age_seconds > 60:
                raise AssertionError(f"session-state timestamp was not fresh: {age_seconds:.1f}s old")
    finally:
        os.chdir(original_cwd)

    chain_runner = (ROOT / "execution" / "chain_runner.py").read_text(encoding="utf-8", errors="ignore")
    for snippet in ("save_session_state(", 'result["session_state_written"] = True'):
        if snippet not in chain_runner:
            raise AssertionError(f"chain_runner finalize no longer records session state: {snippet}")

    print("SESSION STATE FRESHNESS LOOP VERIFICATION PASS")
    print("- temp session-state anchor was written")
    print("- Last updated timestamp is fresh")
    print("- chain_runner finalize still records session_state_written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
