#!/usr/bin/env python3
"""Codex-safe wrapper for Antigravity hook scripts.

The shared hook scripts were written for Claude Code and expect
CLAUDE_PROJECT_DIR. Codex may not provide that environment variable, so this
wrapper resolves the active Google Antigravity root, sets the variable, and
forwards stdin/stdout/stderr unchanged.

The runner intentionally supports two launch shapes:

- a hook command stored in the canonical workspace
- a hook command inherited by a Codex worktree

In both cases, hook work must land in the active root, not accidentally in the
canonical checkout because an absolute hook command pointed there.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


CANONICAL_ROOT = Path("/Users/farricecain/Google Antigravity")


def _looks_like_antigravity_root(path: Path) -> bool:
    return (
        path.name == "Google Antigravity"
        and (path / ".agent" / "workflows").exists()
        and (path / "execution").exists()
    )


def _walk_to_root(path: Path) -> Path | None:
    path = path.resolve()
    candidates = [path] if path.is_dir() else [path.parent]
    candidates.extend(candidates[0].parents)
    for candidate in candidates:
        if _looks_like_antigravity_root(candidate):
            return candidate
    return None


def _active_repo_root() -> Path:
    for key in ("CODEX_PROJECT_DIR", "CLAUDE_PROJECT_DIR", "PWD"):
        value = os.environ.get(key)
        if value:
            found = _walk_to_root(Path(value))
            if found:
                return found

    found = _walk_to_root(Path.cwd())
    if found:
        return found

    own_root = Path(__file__).resolve().parents[2]
    if _looks_like_antigravity_root(own_root):
        return own_root

    return CANONICAL_ROOT


REPO_ROOT = _active_repo_root()

TARGETS = {
    "cost-gate": ("execution/hooks/cost_gate_hook.py", []),
    "dangerous-git": (".codex/tools/codex_dangerous_git_guard.py", []),
    "session-ledger": ("execution/hooks/session_ledger_hook.py", None),
    "skill-router": ("execution/skill_router_hook.py", []),
    "active-tool-lock": ("execution/hooks/active_tool_lock.py", ["codex"]),
    "guard-stranded": ("execution/hooks/guard_stranded_deliverables.py", ["check"]),
}


def _python() -> str:
    venv_python = REPO_ROOT / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in TARGETS:
        names = ", ".join(sorted(TARGETS))
        print(f"Usage: codex_hook_runner.py <{names}> [hook args...]", file=sys.stderr)
        return 2

    target_name = sys.argv[1]
    script_rel, fixed_args = TARGETS[target_name]
    script_path = REPO_ROOT / script_rel
    if not script_path.exists():
        print(f"Missing hook target: {script_path}", file=sys.stderr)
        return 0

    args = fixed_args if fixed_args is not None else sys.argv[2:]
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(REPO_ROOT)
    env["CODEX_PROJECT_DIR"] = str(REPO_ROOT)

    proc = subprocess.run(
        [_python(), str(script_path), *args],
        input=sys.stdin.read(),
        text=True,
        capture_output=True,
        cwd=str(REPO_ROOT),
        env=env,
    )
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
