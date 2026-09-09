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

import json
import os
import subprocess
import sys
from pathlib import Path


CANONICAL_ROOT = Path("/Users/farricecain/Google Antigravity")


def _looks_like_antigravity_root(path: Path) -> bool:
    return (
        (path / ".agent" / "workflows").exists()
        and (path / "execution").exists()
        and (path / "CODEX.md").exists()
    )


def _walk_to_root(path: Path) -> Path | None:
    path = path.resolve()
    candidates = [path] if path.is_dir() else [path.parent]
    candidates.extend(candidates[0].parents)
    for candidate in candidates:
        if _looks_like_antigravity_root(candidate):
            return candidate
    return None


def _active_repo_root(payload: dict | None = None) -> Path:
    payload_cwd = str((payload or {}).get("cwd") or "").strip()
    if payload_cwd:
        found = _walk_to_root(Path(payload_cwd))
        if found:
            return found

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


TARGETS = {
    "cost-gate": ("execution/hooks/cost_gate_hook.py", []),
    "dangerous-git": (".codex/tools/codex_dangerous_git_guard.py", []),
    "session-ledger": ("execution/hooks/session_ledger_hook.py", None),
    "skill-router": ("execution/skill_router_hook.py", []),
    "active-tool-lock": ("execution/hooks/active_tool_lock.py", ["codex"]),
    "guard-stranded": ("execution/hooks/guard_stranded_deliverables.py", ["check"]),
    "artifact-placement": ("execution/hooks/artifact_placement_hook.py", []),
    # Alignment parity port (2026-09-09, gpt-6-astra regression): the steering
    # hooks Claude Code already runs, now fired by Codex through this runner.
    "steering-loop": ("execution/hooks/steering_loop_hook.py", None),
    "session-brief": ("execution/hooks/session_brief.py", []),
    "session-alarm": ("execution/hooks/concurrent_session_alarm.py", []),
    "lane-bootstrap": ("execution/worktree_lane.py", ["bootstrap", "--if-needed"]),
    "superseded-read": ("execution/hooks/superseded_read_guard.py", []),
}

# Codex requires hookSpecificOutput.hookEventName on every context-bearing
# reply (stricter than Claude Code, which accepts bare stdout on
# UserPromptSubmit/SessionStart). Targets listed here print plain text; the
# runner wraps it into the envelope for the event named.
PLAIN_STDOUT_EVENT = {
    "steering-loop": "UserPromptSubmit",   # `stop` mode prints nothing
    "session-brief": "SessionStart",
    "session-alarm": "SessionStart",
    "lane-bootstrap": "SessionStart",
    "superseded-read": "PostToolUse",
}


def _wrap_plain_stdout(target_name: str, args: list[str], stdout: str) -> str:
    """Wrap plain-text stdout into Codex's hookSpecificOutput envelope. JSON
    stdout passes through untouched; empty stdout stays empty; the Stop mode
    of the steering loop is observe-only and emits nothing."""
    event = PLAIN_STDOUT_EVENT.get(target_name)
    if not event or not stdout.strip():
        return stdout
    if target_name == "steering-loop" and args and args[0] != "prompt":
        return stdout
    try:
        parsed = json.loads(stdout)
        if isinstance(parsed, dict):
            return stdout
    except (json.JSONDecodeError, ValueError):
        pass
    return json.dumps({"hookSpecificOutput": {
        "hookEventName": event,
        "additionalContext": stdout.rstrip("\n"),
    }})


def _python(repo_root: Path) -> str:
    venv_python = repo_root / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in TARGETS:
        names = ", ".join(sorted(TARGETS))
        print(f"Usage: codex_hook_runner.py <{names}> [hook args...]", file=sys.stderr)
        return 2

    target_name = sys.argv[1]
    hook_input = sys.stdin.read()
    try:
        payload = json.loads(hook_input) if hook_input.strip() else {}
    except json.JSONDecodeError:
        payload = {}
    repo_root = _active_repo_root(payload if isinstance(payload, dict) else {})
    sys.path.insert(0, str(repo_root / "execution"))
    from tool_event import normalize_event
    if isinstance(payload, dict):
        hook_input = json.dumps(normalize_event(payload))
    script_rel, fixed_args = TARGETS[target_name]
    script_path = repo_root / script_rel
    if not script_path.exists():
        print(f"Missing hook target: {script_path}", file=sys.stderr)
        return 0

    args = fixed_args if fixed_args is not None else sys.argv[2:]
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(repo_root)
    env["CODEX_PROJECT_DIR"] = str(repo_root)
    # Tell shared hooks which harness fired them (dialect card resolution
    # reads the Codex config.toml model under Codex, never the Claude seat).
    env["ANTIGRAVITY_HARNESS"] = "codex"

    proc = subprocess.run(
        [_python(repo_root), str(script_path), *args],
        input=hook_input,
        text=True,
        capture_output=True,
        cwd=str(repo_root),
        env=env,
    )
    stdout, stderr = proc.stdout, proc.stderr
    stdout = _wrap_plain_stdout(target_name, list(args), stdout)
    # Reuse trusted prompt/stop registrations. The companion may add context or
    # advisory observations, never replace a target's decision or exit status.
    try:
        from outcome_next_proof import augment
        stdout, stderr = augment(target_name, args, payload, repo_root, stdout, stderr)
    except Exception as exc:
        stderr += f"[outcome-next-proof] UNOBSERVED ({type(exc).__name__}); existing hook preserved.\n"
    if stdout:
        print(stdout, end="")
    if stderr:
        print(stderr, end="", file=sys.stderr)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
