#!/usr/bin/env python3
"""Concurrent-session alarm (SessionStart hook) — the Golden Rule as a mechanism.

v3 (2026-08-30, integration-only-main repair): every writer gets a lane.
- Sees siblings ACROSS ALL WORKTREES (each tree's path flattens to a different
  ~/.claude/projects/ dir, so the v1 scan was blind to lane siblings).
- In the MAIN tree: emits the AUTO-LANE directive before any write, even for
  the first session. Main is an integration surface, not an authoring tree.
- In a LANE: informational line naming the lane and the auto-merge promise.
- FULL-POWER WATCHDOG: surfaces fresh hook-failure beacons and degraded lanes
  (.agent/hook-failures.log + lanes.json health) so silent harness
  degradation is structurally impossible to miss.

Deterministic backstop, not AI memory (feedback_ai-memory-dependent-observability).
Exit 0 always — this WARNS/DIRECTS, it never blocks (COS = compass, never cage).

Tunables via env: CONCURRENT_ALARM_WINDOW_MIN (default 10).
"""
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    import worktree_lane as wl
except Exception:
    wl = None

WINDOW_MIN = int(os.environ.get("CONCURRENT_ALARM_WINDOW_MIN", "10"))


def _flatten(p) -> str:
    # Claude Code flattens EVERY non-alphanumeric char to '-' (paths with spaces
    # included) — plain '/'-replacement made this alarm silently dead on this project
    # ("Google Antigravity" has a space). Found by the Wave 0 fixture, 2026-07-17.
    return re.sub(r"[^A-Za-z0-9]", "-", str(p))


def _fresh_sessions(tree, own_id, exclude_ids, now):
    """Fresh sibling transcripts for one tree's projects dir."""
    proj_dir = os.path.expanduser(os.path.join("~/.claude/projects", _flatten(tree)))
    out = []
    try:
        for name in os.listdir(proj_dir):
            if not name.endswith(".jsonl"):
                continue
            sid = name[:-6]
            if sid == own_id or sid in exclude_ids:
                continue
            try:
                age_min = (now - os.stat(os.path.join(proj_dir, name)).st_mtime) / 60.0
            except OSError:
                continue
            if age_min <= WINDOW_MIN:
                out.append((sid, age_min))
    except OSError:
        pass
    return out


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    own_id = payload.get("session_id", "")
    source = payload.get("source", "startup")  # startup|resume|clear|compact
    cwd = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    now = time.time()

    in_lane, main_tree, lanes, exclude_ids, registry = False, Path(cwd), {}, set(), {}
    if wl is not None:
        try:
            in_lane = wl.is_lane(Path(cwd))
            main_tree = wl.main_root(Path(cwd))
            lanes = wl.active_lanes(main_tree)
            registry = wl.load_registry(main_tree)
            # sessions registered to lanes are lane writers, not main writers,
            # even though their transcripts stay in main's projects dir
            exclude_ids = {m.get("session_id") for m in registry.values()
                           if m.get("session_id")}
        except Exception:
            pass

    fresh_main = _fresh_sessions(main_tree, own_id, exclude_ids, now)
    fresh_lane_sessions = []
    for branch, path in lanes.items():
        for sid, age in _fresh_sessions(path, own_id, set(), now):
            fresh_lane_sessions.append((branch, sid, age))

    # session_lock status — a fresh foreign lock with NO fresh Claude sibling
    # means a non-Claude driver (Codex, launchd runner) may hold the main tree.
    lock_line = "session_lock: no lock claimed"
    lock_fresh = False
    lock_path = os.path.join(main_tree, ".agent", "session.lock")
    try:
        d = json.load(open(lock_path))
        hb_age = (now - d.get("heartbeat", 0)) / 60.0
        lock_fresh = hb_age < 45
        state = "FRESH" if lock_fresh else "stale"
        lock_line = (f"session_lock: {state} lock held — mission '{d.get('mission', '?')}' "
                     f"(heartbeat {hb_age:.0f}m ago)")
    except (OSError, ValueError):
        pass

    # ── main output ────────────────────────────────────────────────
    if in_lane:
        branch = wl.current_branch(Path(cwd)) if wl else "?"
        print(f"LANE SESSION (deterministic, from concurrent_session_alarm.py): you are in "
              f"worktree lane '{branch}' — single writer by construction, full harness power "
              f"(bootstrap parity ran at SessionStart). Work merges back to main automatically "
              f"at end-session; conflicts park the branch with one line. No lock needed here.")
    else:
        fresh_main.sort(key=lambda t: t[1])
        sibling_note = ""
        if fresh_main:
            listing = ", ".join(
                f"{sid[:8]}… ({age:.0f}m ago)" for sid, age in fresh_main[:4]
            )
            sibling_note = (
                f" {len(fresh_main)} fresh main session(s) also detected: {listing}."
            )
        print(
            f"AUTO-LANE (deterministic, from concurrent_session_alarm.py): main is "
            f"integration-only (source={source}). Read-only inspection may continue here; "
            f"before ANY write, call the EnterWorktree tool now (name: a short mission slug). "
            f"Bootstrap is automatic (hooks provision .env/.venv/MCP/memory and prove FULL "
            f"POWER); clean work auto-merges into main and conflicts park safely.{sibling_note} "
            f"{lock_line}."
        )

    # Lane siblings are informational — they can't collide with this tree.
    if fresh_lane_sessions and not in_lane:
        listing = ", ".join(f"{b} ({sid[:8]}…, {age:.0f}m)" for b, sid, age in fresh_lane_sessions[:4])
        print(f"LANES ACTIVE: {len(fresh_lane_sessions)} session(s) working in lanes — {listing}. "
              f"They merge back automatically; `python3 execution/worktree_lane.py list` for status.")

    # ── FULL-POWER WATCHDOG ────────────────────────────────────────
    beacon = Path(main_tree) / ".agent" / "hook-failures.log"
    try:
        if beacon.exists() and (now - beacon.stat().st_mtime) < 24 * 3600:
            tail = beacon.read_text().splitlines()[-3:]
            print(f"⚠ HOOK DEGRADATION (full-power watchdog): {len(tail)} recent entr(ies) in "
                  f".agent/hook-failures.log — a tree ran with degraded hooks. Latest: "
                  f"{tail[-1][:110]} — fix: python3 execution/worktree_lane.py doctor --fix, "
                  f"then clear the log.")
    except Exception:
        pass
    try:
        degraded = [(b, m.get("health", "")) for b, m in registry.items()
                    if m.get("health") and m["health"] != "full-power"
                    and m.get("status") == "active"]
        if degraded:
            b, h = degraded[0]
            print(f"⚠ LANE DEGRADED (full-power watchdog): {len(degraded)} lane(s) below full "
                  f"power — {b}: {h[:90]} — fix: python3 execution/worktree_lane.py doctor --fix")
    except Exception:
        pass


if __name__ == "__main__":
    main()
    sys.exit(0)
