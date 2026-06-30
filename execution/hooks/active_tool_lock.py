#!/usr/bin/env python3
"""Active-tool coordination guard (the GOLDEN RULE backstop).

Two tools — Claude Code and Codex — share ONE working tree at
/Users/farricecain/Google Antigravity with no OS-level lock. Running both at
once corrupts the tree (root-caused 2026-06-30). This PreToolUse hook stamps
`.agent/active-tool.lock` on each write-class action and WARNS (never blocks)
when a *different* tool stamped it within the TTL window.

Design invariants:
- WARN-ONLY. Always exits 0. It must never block a real session.
- FAIL-SAFE. Any error -> exit 0 silently. A guard must never become the bug.
- TTL'd. A crashed/abandoned session's stamp expires (default 10 min) so it
  cannot wedge the other tool forever.

Invocation:
  Claude Code (.claude/settings.json):  active_tool_lock.py claude-code
  Codex (.codex/hooks.json):            active_tool_lock.py codex
Tool name may also come from env ANTIGRAVITY_TOOL; argv wins.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

TTL_SECONDS = 600  # 10 minutes; a stamp older than this is treated as stale


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False
    except Exception:
        return True  # unknown -> assume alive (conservative warning)


def main() -> int:
    try:
        tool = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ANTIGRAVITY_TOOL", "claude-code")).strip() or "claude-code"
        root = Path(__file__).resolve().parents[2]  # execution/hooks/ -> repo root
        lock = root / ".agent" / "active-tool.lock"
        now = time.time()
        mypid = os.getpid()

        prev = None
        if lock.exists():
            try:
                prev = json.loads(lock.read_text())
            except Exception:
                prev = None

        # warn if a DIFFERENT tool stamped within the TTL window.
        # NOTE: the stored pid is the ephemeral hook-subprocess pid (dead by the next
        # call), so it is NOT a reliable liveness signal — the TTL is the real guard.
        if prev and isinstance(prev, dict):
            prev_tool = str(prev.get("tool", ""))
            prev_ts = float(prev.get("ts", 0) or 0)
            prev_pid = int(prev.get("pid", 0) or 0)
            age = now - prev_ts
            if prev_tool and prev_tool != tool and 0 <= age < TTL_SECONDS:
                mins = int(age // 60)
                secs = int(age % 60)
                sys.stderr.write(
                    f"\n⚠️  GOLDEN RULE WARNING: '{prev_tool}' was active in this repo "
                    f"{mins}m{secs:02d}s ago (pid {prev_pid}). You are now '{tool}'.\n"
                    f"   Two tools editing one working tree at once corrupts it. "
                    f"Finish/close the other tool to a clean `git status` before continuing here.\n\n"
                )

        # stamp ours (best-effort; never fail the action on a write error)
        try:
            lock.parent.mkdir(parents=True, exist_ok=True)
            lock.write_text(json.dumps({"tool": tool, "pid": mypid, "ts": now}))
        except Exception:
            pass

    except Exception:
        pass  # fail-safe: a guard must never block real work
    return 0


if __name__ == "__main__":
    sys.exit(main())
