#!/usr/bin/env python3
"""Sabotage checks for unattended lane reconciliation safety."""
from __future__ import annotations

import tempfile
import time
from pathlib import Path
from unittest.mock import patch

import lane_reconciler as lr
import worktree_lane as wtl


def lane(branch: str = "codex/test") -> list[dict]:
    return [{"branch": branch, "path": "/tmp/test-lane"}]


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS: {message}")


def main() -> int:
    now = time.time()
    fresh = now - 5 * 60
    quiet = now - 2 * 60 * 60
    stale = now - 30 * 60 * 60

    common = [patch.object(lr, "lanes", return_value=lane()),
              patch.object(lr, "load_registry", return_value={})]

    with common[0], common[1], \
         patch.object(lr, "commits_ahead", return_value=1), \
         patch.object(lr, "worktree_state", return_value=(0, "", 0)), \
         patch.object(lr, "lane_activity_epoch", return_value=fresh):
        result = lr.reconcile(dry_run=True)
        check(result["results"][0]["action"] == "skipped-fresh",
              "fresh clean lane is not merged mid-session")

    with patch.object(lr, "lanes", return_value=lane()), \
         patch.object(lr, "load_registry", return_value={}), \
         patch.object(lr, "commits_ahead", return_value=1), \
         patch.object(lr, "worktree_state", return_value=(0, "", 0)), \
         patch.object(lr, "lane_activity_epoch", return_value=quiet), \
         patch.object(lr, "merge_probe", return_value=([], "")):
        result = lr.reconcile(dry_run=True)
        check(result["results"][0]["action"] == "would-merge",
              "quiet clean lane becomes locally mergeable")

    with patch.object(lr, "lanes", return_value=lane()), \
         patch.object(lr, "load_registry", return_value={}), \
         patch.object(lr, "commits_ahead", return_value=0), \
         patch.object(lr, "worktree_state", return_value=(3, "", stale)), \
         patch.object(lr, "lane_activity_epoch", return_value=stale):
        result = lr.reconcile(dry_run=True)
        check(result["results"][0]["action"] == "parked-stale-dirty",
              "stale dirty lane is preserved and surfaced, never guessed")

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        (root / "new-deliverable.md").write_text("work in progress\n")
        with patch.object(lr, "git", return_value=(0, "?? new-deliverable.md")):
            count, error, _ = lr.worktree_state(str(root))
        check(count == 1 and not error, "untracked authored file counts as dirty work")

    calls: list[tuple[str, ...]] = []
    def fake_lane_tool(*args: str) -> tuple[int, str]:
        calls.append(args)
        return 0, "LANE MERGED: codex/test -> main"

    with tempfile.TemporaryDirectory() as temp, \
         patch.object(lr, "RECEIPT", Path(temp) / "receipt.json"), \
         patch.object(lr, "lanes", return_value=lane()), \
         patch.object(lr, "load_registry", return_value={}), \
         patch.object(lr, "commits_ahead", return_value=1), \
         patch.object(lr, "worktree_state", return_value=(0, "", 0)), \
         patch.object(lr, "lane_activity_epoch", return_value=quiet), \
         patch.object(lr, "merge_probe", return_value=([], "")), \
         patch.object(lr, "run_lane_tool", side_effect=fake_lane_tool):
        result = lr.reconcile()
        check(result["results"][0]["action"] == "merged",
              "quiet conflict-free lane delegates to audited merge")
        check("--no-push" in calls[0], "unattended reconciliation never pushes remote state")

    with patch.object(lr, "lanes", return_value=lane()), \
         patch.object(lr, "load_registry", return_value={}), \
         patch.object(lr, "commits_ahead", return_value=1), \
         patch.object(lr, "worktree_state", return_value=(0, "cannot read worktree status", 0)), \
         patch.object(lr, "lane_activity_epoch", return_value=quiet):
        result = lr.reconcile(dry_run=True)
        check(result["results"][0]["action"] == "parked-status-error",
              "status failure fails closed instead of masquerading as clean")

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        (root / ".agent").mkdir()
        check(wtl.fresh_main_writer(root) is None,
              "read-only main sessions do not block integration without write evidence")
        (root / ".agent" / "session.lock").write_text(
            '{"heartbeat": %s, "token": "foreign", "mission": "active edit"}' % time.time()
        )
        writer = wtl.fresh_main_writer(root, own_lock_token="ours")
        check(writer is not None and "session lock" in writer,
              "fresh foreign main write-lock still blocks integration")

    print("PASS: lane reconciler safety suite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
