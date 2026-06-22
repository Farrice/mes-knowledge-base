#!/usr/bin/env python3
"""Codex bootstrap and parity check for Google Antigravity roots."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOT = Path("/Users/farricecain/Google Antigravity")
GLOBAL_CONFIG = Path.home() / ".codex" / "config.toml"
HOOKS_PATH = REPO_ROOT / ".codex" / "hooks.json"
CANONICAL_HOOKS_PATH = CANONICAL_ROOT / ".codex" / "hooks.json"


REQUIRED_VERIFIERS = [
    "execution/verify_codex_context_load_manifest.py",
    "execution/verify_system_control_plane.py",
    "execution/verify_autopilot_runtime_preflight.py",
    "execution/verify_autopilot_routing.py",
    "execution/verify_codex_authority.py",
    "execution/codex_live_surface_audit.py",
    "execution/codex_harness_check.py",
]


def _role() -> str:
    root = REPO_ROOT.resolve()
    if root == CANONICAL_ROOT:
        return "canonical"
    if ".codex/worktrees" in str(root) and root.name == "Google Antigravity":
        return "worktree"
    return "other"


def _python() -> Path:
    venv = REPO_ROOT / ".venv" / "bin" / "python"
    if venv.exists():
        return venv
    return Path(sys.executable)


def _run(args: list[str], timeout: int = 20) -> dict[str, Any]:
    try:
        proc = subprocess.run(args, cwd=REPO_ROOT, text=True, capture_output=True, timeout=timeout)
        return {"ok": proc.returncode == 0, "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}
    except Exception as exc:
        return {"ok": False, "stdout": "", "stderr": str(exc)}


def _config_text() -> str:
    if not GLOBAL_CONFIG.exists():
        return ""
    return GLOBAL_CONFIG.read_text(errors="ignore")


def _hook_state_count(config: str, hooks_path: Path) -> int:
    count = 0
    current = False
    needle = str(hooks_path)
    for line in config.splitlines():
        if line.startswith("[hooks.state.") and needle in line:
            current = True
        elif current and line.strip().startswith("enabled"):
            if "true" in line.lower():
                count += 1
            current = False
    return count


def _hooks_commands() -> list[str]:
    if not HOOKS_PATH.exists():
        return []
    try:
        data = json.loads(HOOKS_PATH.read_text())
    except json.JSONDecodeError:
        return []
    commands: list[str] = []
    for groups in data.get("hooks", {}).values():
        for group in groups:
            for hook in group.get("hooks", []):
                command = hook.get("command")
                if command:
                    commands.append(str(command))
    return commands


def _import_check() -> dict[str, bool]:
    code = "import yaml, dotenv, requests; print('ok')"
    result = _run([str(_python()), "-c", code])
    google = _run([str(_python()), "-c", "import google.genai; print('ok')"])
    return {
        "yaml_dotenv_requests": result["ok"],
        "google_genai": google["ok"],
    }


def main() -> int:
    config = _config_text()
    imports = _import_check()
    commands = _hooks_commands()
    role = _role()

    checks = [
        ("root_is_google_antigravity", REPO_ROOT.name == "Google Antigravity"),
        ("hooks_json_exists", HOOKS_PATH.exists()),
        ("canonical_hooks_json_exists", CANONICAL_HOOKS_PATH.exists()),
        ("active_root_trusted", f'[projects."{REPO_ROOT}"]' in config),
        ("canonical_root_trusted", f'[projects."{CANONICAL_ROOT}"]' in config),
        ("active_hook_states_enabled", _hook_state_count(config, HOOKS_PATH) > 0),
        ("canonical_hook_states_enabled", _hook_state_count(config, CANONICAL_HOOKS_PATH) > 0),
        ("python_runtime_exists", _python().exists()),
        ("python_core_deps", imports["yaml_dotenv_requests"]),
        ("preflight_exists", (REPO_ROOT / ".codex" / "tools" / "codex_orchestration_preflight.py").exists()),
        ("hook_runner_exists", (REPO_ROOT / ".codex" / "tools" / "codex_hook_runner.py").exists()),
        ("hook_runner_active_root_aware", "CODEX_PROJECT_DIR" in (REPO_ROOT / ".codex" / "tools" / "codex_hook_runner.py").read_text(errors="ignore")),
    ]

    for verifier in REQUIRED_VERIFIERS:
        checks.append((f"verifier:{verifier}", (REPO_ROOT / verifier).exists()))

    hard_failures = [name for name, ok in checks if not ok and name not in {"active_hook_states_enabled"}]
    warnings = []
    if role == "worktree" and not any(str(REPO_ROOT) in command for command in commands):
        warnings.append("worktree hooks do not use worktree-absolute commands; active-root-aware runner is required")
    if role == "worktree" and _hook_state_count(config, HOOKS_PATH) == 0:
        warnings.append("no direct hook trust state for this worktree; canonical trust plus active-root runner is the fallback")
    if not imports["google_genai"]:
        warnings.append("google.genai unavailable; memory may degrade to fallback search")

    print("# Codex Worktree Parity Check")
    print(f"root: {REPO_ROOT}")
    print(f"role: {role}")
    print(f"python: {_python()}")
    print()
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    for warning in warnings:
        print(f"WARN {warning}")

    if hard_failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
