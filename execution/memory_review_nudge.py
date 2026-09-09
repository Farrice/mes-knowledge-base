#!/usr/bin/env python3
"""memory_review_nudge.py — weekly tap on the shoulder for the memory review queue.

Goal + scar (Farrice, 2026-08-21): "I won't remember to do it if I don't do it"
— the review queue sat 26 days with a daily alarm nobody saw because it lived
in a launchd log. The in-session line (memory_pulse.py) helps, but he asked for
a mechanism that PROMPTS him. This is it: once a week (launchd
com.antigravity.memory-review-nudge, Monday 09:00), if and only if proposals
are pending, push a Mac/phone notification via notify.py with the exact
command and the time cost. Zero pending = zero noise. Compass doctrine: a
nudge that reaches him, never a gate that holds anything.

Manual test:  python3 execution/memory_review_nudge.py --force
Uninstall:    launchctl unload ~/Library/LaunchAgents/com.antigravity.memory-review-nudge.plist
"""
from __future__ import annotations

import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / ".memory" / "sovereign.db"
PY = str(ROOT / ".venv" / "bin" / "python3")
if not Path(PY).exists():
    PY = sys.executable


def pending() -> tuple[int, float]:
    """(count, oldest_age_days) of pending flagged_review rows."""
    if not DB.exists():
        return 0, 0.0
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True, timeout=2.0)
    try:
        count, oldest = con.execute(
            "SELECT COUNT(*), MIN(created_at) FROM flagged_review WHERE status = 'pending'"
        ).fetchone()
    finally:
        con.close()
    if not count or not oldest:
        return 0, 0.0
    try:
        dt = datetime.fromisoformat(oldest)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        age = (datetime.now(timezone.utc) - dt).total_seconds() / 86400.0
    except Exception:
        age = 0.0
    return count, age


def main() -> int:
    force = "--force" in sys.argv
    count, age = pending()
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if count == 0 and not force:
        print(f"[{now}] memory-review-nudge: queue empty — silent")
        return 0
    title = "🧠 Memory review — ~5 min"
    if count == 0:
        body = "(test fire) Queue is empty right now."
    elif age > 14:
        body = (f"{count} proposed rule(s) waiting, oldest {age:.0f} days. "
                f"Open a Claude session and say: review the memory queue with me")
    else:
        body = (f"{count} proposed rule(s) from this week's distill. "
                f"Open a Claude session and say: review the memory queue with me")
    rc = subprocess.run(
        [PY, str(ROOT / "execution" / "notify.py"), "send", title, body],
        cwd=ROOT, timeout=30,
    ).returncode
    print(f"[{now}] memory-review-nudge: pending={count} oldest={age:.0f}d notify_rc={rc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
