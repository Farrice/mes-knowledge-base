#!/usr/bin/env python3
"""
cos_notify.py — the COS morning nudge as a macOS notification (money-lane A3, 2026-07-29).

WHY: the COS brief generates every morning via launchd, but it waited for
Farrice to open a session. His life is naptime-sized windows and a full
calendar — the day's ONE next action should reach him, not wait for him.
Reads the nudge_line cos_prep already computes (no new state); silent when
there's nothing to say. Never blocks anything (compass).

Wired: launchd com.antigravity.cos-notify, mornings after cos-prep.
Manual test: python3 execution/cos_notify.py
"""
import json
import subprocess
import sys
from pathlib import Path

STATE = Path(__file__).resolve().parents[1] / ".agent" / "cos" / "state.json"


def main() -> int:
    try:
        state = json.loads(STATE.read_text())
    except Exception:
        return 0
    nudge = (state.get("nudge_line") or "").strip()
    if not nudge:
        return 0
    extras = []
    if state.get("open_missions"):
        extras.append(f"{state['open_missions']} open mission(s)")
    subtitle = " · ".join(extras)
    # osascript display notification — the least-machinery push channel on macOS.
    script = (
        f'display notification {json.dumps(nudge[:180])} '
        f'with title "Antigravity — today" '
        + (f'subtitle {json.dumps(subtitle)}' if subtitle else "")
    )
    try:
        subprocess.run(["osascript", "-e", script], capture_output=True, timeout=10)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
