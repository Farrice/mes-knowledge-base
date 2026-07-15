#!/usr/bin/env python3
"""Concurrent-session alarm (SessionStart hook) — the Golden Rule as a mechanism.

Detects OTHER live Claude Code sessions on this same working tree by scanning
sibling session transcripts in ~/.claude/projects/<flattened-cwd>/ for recent
mtimes. A fresh sibling means a second driver may be writing to this tree —
the 2026-07-15 forge race (docs/solutions/2026-07-15-concurrent-session-race-
accept-repair-dedupe.md) and the 2026-06-30 "apply one fix, another breaks"
corruption both start here.

Deterministic backstop, not AI memory (feedback_ai-memory-dependent-observability).
Exit 0 always — this WARNS, it never blocks (COS = compass, never cage).
Also surfaces session_lock.py status so the session knows to claim before builds.

Tunables via env: CONCURRENT_ALARM_WINDOW_MIN (default 10).
"""
import json
import os
import sys
import time

WINDOW_MIN = int(os.environ.get("CONCURRENT_ALARM_WINDOW_MIN", "10"))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    own_id = payload.get("session_id", "")
    cwd = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

    flat = cwd.replace("/", "-")
    proj_dir = os.path.expanduser(os.path.join("~/.claude/projects", flat))
    if not os.path.isdir(proj_dir):
        return

    now = time.time()
    fresh = []
    try:
        for name in os.listdir(proj_dir):
            if not name.endswith(".jsonl"):
                continue
            sid = name[:-6]
            if sid == own_id:
                continue
            path = os.path.join(proj_dir, name)
            try:
                age_min = (now - os.stat(path).st_mtime) / 60.0
            except OSError:
                continue
            if age_min <= WINDOW_MIN:
                fresh.append((sid, age_min))
    except OSError:
        return

    if not fresh:
        return

    fresh.sort(key=lambda t: t[1])
    listing = ", ".join(f"{sid[:8]}… ({age:.0f}m ago)" for sid, age in fresh[:4])

    # session_lock status (informational)
    lock_line = "session_lock: no lock claimed"
    lock_path = os.path.join(cwd, ".agent", "session.lock")
    try:
        d = json.load(open(lock_path))
        hb_age = (now - d.get("heartbeat", 0)) / 60.0
        state = "FRESH" if hb_age < 45 else "stale"
        lock_line = (f"session_lock: {state} lock held — mission '{d.get('mission', '?')}' "
                     f"(heartbeat {hb_age:.0f}m ago)")
    except (OSError, ValueError):
        pass

    print(
        f"⚠ CONCURRENT SESSION ALARM (deterministic, from concurrent_session_alarm.py): "
        f"{len(fresh)} other session(s) on this working tree were active within the last "
        f"{WINDOW_MIN} min — {listing}. GOLDEN RULE: one live writer per tree. Before any "
        f"build/forge/multi-file work: coordinate with Farrice, claim the lock "
        f"(python3 execution/session_lock.py claim \"<mission>\"), or move this session to a "
        f"git worktree. If files change that this session didn't write, apply "
        f"docs/solutions/2026-07-15-concurrent-session-race-accept-repair-dedupe.md "
        f"(accept → repair → dedupe, never revert). {lock_line}. "
        f"NOTE: a sibling may be read-only — this is a warning, never a block."
    )


if __name__ == "__main__":
    main()
    sys.exit(0)
