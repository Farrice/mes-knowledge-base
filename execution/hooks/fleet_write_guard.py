#!/usr/bin/env python3
"""Fleet write guard (PreToolUse: Edit|Write) — merge-discipline Law 1 as a mechanism.

While a repair/build fleet is active (fresh `.agent/fleet-active.json` sentinel),
direct Edit/Write to protected canonical paths is BLOCKED for every session and
subagent on this tree — workers write to their quarantine dir; the conductor merges
serially via shell copy (unaffected by this hook, which only sees Edit/Write).

Wave 3 evidence (2026-07-17): four fleet workers "briefly" edited live skills/
before self-reverting, and one foreign worker contaminated skills/ outright —
prose envelopes don't prevent the first slip. See docs/solutions/
2026-07-17-repair-fleet-poc-three-failure-shapes.md.

Sentinel format (conductor-managed):
  {"mission": "...", "claimed": <epoch>, "protected": ["skills/"], "ttl_min": 90}
Conductor lifecycle: write sentinel at fleet dispatch, delete at fleet close.
Stale sentinels (older than ttl_min) never block — a crashed fleet can't brick edits.
Exit 2 = block (stderr shown to the model); exit 0 = allow.
"""
import json
import os
import sys
import time


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    cwd = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    sentinel_path = os.path.join(cwd, ".agent", "fleet-active.json")
    try:
        s = json.load(open(sentinel_path))
    except (OSError, ValueError):
        return 0

    ttl = float(s.get("ttl_min") or 90) * 60
    if time.time() - float(s.get("claimed") or 0) > ttl:
        return 0  # stale fleet sentinel never blocks

    file_path = (payload.get("tool_input") or {}).get("file_path", "")
    if not file_path:
        return 0
    rel = os.path.relpath(os.path.abspath(file_path), os.path.abspath(cwd))

    for root in s.get("protected", ["skills/"]):
        root = root.rstrip("/") + "/"
        if rel.startswith(root):
            print(
                f"FLEET WRITE GUARD — BLOCKED (deterministic, fleet_write_guard.py): "
                f"fleet '{s.get('mission', '?')}' is active on this tree and '{rel}' is a "
                f"protected canonical path. Workers write ONLY to their quarantine dir "
                f"(.tmp/<batch>/<skill>/); the conductor merges serially through the "
                f"deterministic gate (directives/merge-discipline.md Law 1). If you are "
                f"the conductor needing a direct edit, close the fleet or merge via cp.",
                file=sys.stderr,
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
