#!/usr/bin/env python3
"""Sabotage fixtures for integration-only main write ownership."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GUARD = ROOT / "execution" / "hooks" / "main_write_guard.py"
CODEX_BRIDGE = ROOT / ".codex" / "tools" / "codex_dangerous_git_guard.py"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS: {message}")


def run(payload: dict, cwd: Path, script: Path = GUARD) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script)], cwd=cwd, text=True,
        input=json.dumps(payload), capture_output=True,
    )


def git(cwd: Path, *args: str) -> None:
    proc = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)
    if proc.returncode != 0:
        raise AssertionError(proc.stderr)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="main-write-guard-") as temp:
        main_root = Path(temp) / "repo"
        lane_root = Path(temp) / "lane"
        main_root.mkdir()
        git(main_root, "init", "-q")
        git(main_root, "config", "user.email", "guard@example.test")
        git(main_root, "config", "user.name", "Guard Test")
        (main_root / ".gitignore").write_text(".runtime/\n")
        (main_root / "tracked.md").write_text("baseline\n")
        git(main_root, "add", ".gitignore", "tracked.md")
        git(main_root, "commit", "-qm", "baseline")

        edit = {"tool_name": "Edit", "cwd": str(main_root),
                "tool_input": {"file_path": str(main_root / "tracked.md")}}
        check(run(edit, main_root).returncode == 2,
              "native edit on main is blocked")
        check(run(edit, main_root, CODEX_BRIDGE).returncode == 2,
              "trusted Codex guard bridge enforces native main-write ownership")

        ignored = {"tool_name": "Write", "cwd": str(main_root),
                   "tool_input": {"file_path": str(main_root / ".runtime" / "state.json")}}
        check(run(ignored, main_root).returncode == 0,
              "ignored runtime state on main remains writable")

        safe = {"tool_name": "Bash", "cwd": str(main_root),
                "tool_input": {"command": "git status --short"}}
        check(run(safe, main_root).returncode == 0,
              "read-only Git inspection on main is allowed")

        commit = {"tool_name": "Bash", "cwd": str(main_root),
                  "tool_input": {"command": "git add tracked.md && git commit -m test"}}
        check(run(commit, main_root).returncode == 2,
              "direct Git authoring on main is blocked")

        closeout = {"tool_name": "Bash", "cwd": str(main_root),
                    "tool_input": {"command": "python3 execution/end_session_closeout.py run"}}
        check(run(closeout, main_root).returncode == 2,
              "known tracked-tree closeout writer on main is blocked")

        integrator = {"tool_name": "Bash", "cwd": str(main_root),
                      "tool_input": {"command": "python3 execution/worktree_lane.py merge --lane codex/test"}}
        check(run(integrator, main_root).returncode == 0,
              "audited lane integrator on main is allowed")

        git(main_root, "worktree", "add", "-q", "-b", "codex/test-lane", str(lane_root))
        lane_edit = {"tool_name": "Edit", "cwd": str(lane_root),
                     "tool_input": {"file_path": str(lane_root / "tracked.md")}}
        check(run(lane_edit, lane_root).returncode == 0,
              "ordinary authoring inside a worktree lane is allowed")

    print("PASS: main write guard safety suite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
