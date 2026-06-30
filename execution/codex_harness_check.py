#!/usr/bin/env python3
"""Codex migration health check for the Antigravity harness."""

from __future__ import annotations

import importlib
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCAL_PACKAGES = ROOT / ".tmp" / "python-packages"
if LOCAL_PACKAGES.exists():
    sys.path.insert(0, str(LOCAL_PACKAGES))

try:
    from codex_live_surface_audit import HOT_COMMANDS as HOT_COMMAND_SKILLS
    from codex_live_surface_audit import DUAL_MODE_COMMANDS
except ModuleNotFoundError:  # pragma: no cover - direct script fallback
    from execution.codex_live_surface_audit import HOT_COMMANDS as HOT_COMMAND_SKILLS
    from execution.codex_live_surface_audit import DUAL_MODE_COMMANDS


def count(pattern: str) -> int:
    return sum(1 for _ in ROOT.glob(pattern))


def command_names() -> set[str]:
    return {p.stem for p in (ROOT / ".claude" / "commands").glob("*.md")}


def skill_command_names() -> set[str]:
    skills = ROOT / ".agents" / "skills"
    prefix = "source-command-"
    return {
        p.name.removeprefix(prefix)
        for p in skills.glob(f"{prefix}*")
        if p.is_dir() and (p / "SKILL.md").exists()
    }


def cold_skill_command_names() -> set[str]:
    skills = ROOT / ".agents" / "cold-skills" / "source-command-wrappers"
    prefix = "source-command-"
    return {
        p.name.removeprefix(prefix)
        for p in skills.glob(f"{prefix}*")
        if p.is_dir() and (p / "SKILL.md").exists()
    }


def workflow_names() -> set[str]:
    workflows = ROOT / ".agent" / "workflows"
    return {p.stem for p in workflows.glob("*.md")}


def run_smoke(label: str, args: list[str]) -> bool:
    env = os.environ.copy()
    if LOCAL_PACKAGES.exists():
        existing = env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = str(LOCAL_PACKAGES) if not existing else f"{LOCAL_PACKAGES}{os.pathsep}{existing}"
    proc = subprocess.run(
        args,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=20,
    )
    ok = proc.returncode == 0
    print(f"{label}: {'ok' if ok else 'FAIL'}")
    if not ok:
        detail = (proc.stderr or proc.stdout).strip().splitlines()
        if detail:
            print(f"  {detail[0][:160]}")
    return ok


def main() -> int:
    checks: list[bool] = []

    print(f"root: {ROOT}")
    for path in ["CODEX.md", "GEMINI.md", "CLAUDE.md", "AGENTS.md", ".env", ".codex/config.toml"]:
        exists = (ROOT / path).exists()
        checks.append(exists)
        print(f"{path}: {'ok' if exists else 'MISSING'}")

    for module in ["dotenv", "requests"]:
        try:
            importlib.import_module(module)
            print(f"python module {module}: ok")
            checks.append(True)
        except Exception as exc:  # pragma: no cover - diagnostic script
            print(f"python module {module}: FAIL ({exc})")
            checks.append(False)

    commands = command_names()
    skill_commands = skill_command_names()
    cold_skill_commands = cold_skill_command_names()
    workflows = workflow_names()
    missing_hot_skills = sorted(HOT_COMMAND_SKILLS - skill_commands)
    non_hot_live_skills = sorted(skill_commands - HOT_COMMAND_SKILLS)
    hot_in_cold = sorted((HOT_COMMAND_SKILLS & cold_skill_commands) - DUAL_MODE_COMMANDS)
    missing_hot_workflows = sorted(HOT_COMMAND_SKILLS - workflows)

    print(f"claude commands: {len(commands)}")
    print(f"codex live command skills: {len(skill_commands)}")
    print(f"codex cold command skills: {len(cold_skill_commands)}")
    print(f"root skills: {count('skills/*/SKILL.md')}")
    print(f"expert agents: {count('agents/*/AGENT.md')}")
    print(f"workflows: {count('.agent/workflows/*.md')}")
    print(f"execution scripts: {count('execution/*.py')}")
    print(f"claude subagents: {count('.claude/agents/*.md')}")

    if missing_hot_skills:
        print("missing hot command skills:")
        for name in missing_hot_skills:
            print(f"  {name}")
        checks.append(False)
    else:
        print("hot command skill coverage: ok")
        checks.append(True)

    # Single-tree topology (canonical, 2026-06-30): every source-command
    # wrapper lives in .agents/skills. "Non-hot wrappers live" is the expected
    # state, not a failure — so this is reported descriptively, never gated.
    print(f"non-hot command skills live (single-tree, informational): {len(non_hot_live_skills)}")

    if hot_in_cold:
        print("hot command skills accidentally cold:")
        for name in hot_in_cold:
            print(f"  {name}")
        checks.append(False)
    else:
        print("hot command skills absent from cold quarantine: ok")
        checks.append(True)

    # Hot command-skill coverage is the gated invariant (asserted above): every
    # hot control-plane command must be present as a live source-command skill.
    # A matching .agent/workflows/*.md file is NOT required — several hot
    # command-skills (e.g. ai-employee-os, video-source-extract, virtuoso)
    # delegate their behavior elsewhere and have no standalone workflow file.
    # So workflow coverage is reported descriptively, never gated.
    if missing_hot_workflows:
        print(f"hot commands without a standalone workflow file (informational): {len(missing_hot_workflows)}")
        for name in missing_hot_workflows:
            print(f"  {name}")
    else:
        print("hot workflow coverage: ok")

    checks.append(run_smoke("codex live surface", [sys.executable, "execution/codex_live_surface_audit.py", "--strict"]))
    checks.append(run_smoke("expert router", [sys.executable, "execution/expert_router.py", "route", "positioning linkedin post"]))
    checks.append(run_smoke("tool router", [sys.executable, "execution/tool_router.py", "route", "positioning linkedin post"]))
    checks.append(run_smoke("context retriever", [sys.executable, "execution/context_retriever.py", "search", "positioning linkedin post"]))
    checks.append(run_smoke("workflow router", [sys.executable, "execution/workflow_router.py", "search", "positioning linkedin post"]))
    checks.append(run_smoke("command menu", [sys.executable, "execution/command_menu.py", "search", "positioning linkedin post"]))
    checks.append(run_smoke("memory store", [sys.executable, "execution/memory_store.py", "stats"]))
    checks.append(run_smoke("knowledge compiler", [sys.executable, "execution/knowledge_compiler.py", "stats"]))

    ok = all(checks)
    print(f"overall: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
