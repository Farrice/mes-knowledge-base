#!/usr/bin/env python3
"""Verify Orchestrate Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "orchestrate.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-orchestrate" / "SKILL.md"
GLOBAL_ORCHESTRATE = Path.home() / ".codex" / "skills" / "orchestrate" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-orchestrate" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Orchestrate behavior",
        "menu-only backend",
        "must not execute",
        "mutate files",
        "choose on Farrice's behalf",
        "safe-run execution after trace",
        "Real Codex subagents require explicit authorization",
        "Do not run the recommended first prompt or command",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/orchestrate.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "menu-only backend",
        "execution intent routes through `/autopilot`",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_ORCHESTRATE: [
        "/Users/farricecain/Google Antigravity/.agent/workflows/orchestrate.md",
        "thin compatibility wrapper",
        "menu-only backend",
        "must not execute",
        "execution intent routes through `/autopilot`",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/orchestrate/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/orchestrate.md",
        "menu-only backend",
        "must not execute",
        "execution intent routes through `/autopilot`",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "plan-first approval checkpoint",
    "Plan First Always",
    "approval checkpoint for meaningful work",
    "plan-first checkpoint",
)

ROUTING_CASES = (
    ("orchestrate execution menu ranked options", "orchestrate"),
    ("source-command-orchestrate show me ranked options", "orchestrate"),
    ("show me the menu of options", "orchestrate"),
    ("what should I use next", "autopilot"),
    ("autopilot is useless orchestration is useless they execute without menu", "autopilot"),
)


def run(args: list[str]) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(args)}\n{completed.stdout}")
    return completed.stdout


def first_command_line(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("1. `/") or stripped.startswith("/"):
            return stripped
    return ""


def first_workflow_line(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            return stripped
    return ""


def chosen_route(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("- **Chosen route**: /"):
            return stripped.rsplit("/", 1)[-1]
    return ""


def verify_text() -> list[str]:
    results = []
    for path, snippets in REQUIRED_TEXT.items():
        if not path.exists():
            raise AssertionError(f"Missing file: {path}")
        text = path.read_text(encoding="utf-8", errors="ignore")
        normalized = " ".join(text.split())
        for snippet in snippets:
            if " ".join(snippet.split()) not in normalized:
                raise AssertionError(f"Missing snippet in {path}: {snippet}")
        for snippet in FORBIDDEN:
            if snippet.lower() in text.lower():
                raise AssertionError(f"Stale Orchestrate text in {path}: {snippet}")
        results.append(f"orchestrate contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_orchestrate.py", "--check"])
    return ["orchestrate sync helper passes"]


def verify_routes() -> list[str]:
    results = []
    for query, expected in ROUTING_CASES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if f"`/{expected}`" not in first_menu:
            raise AssertionError(f"command_menu did not rank /{expected} first for {query!r}\n{menu}")

        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if not first_router.startswith(f"/{expected}"):
            raise AssertionError(f"workflow_router did not rank /{expected} first for {query!r}\n{router}")

        governor = run([sys.executable, "execution/routing_governor.py", "evaluate", query])
        if chosen_route(governor) != expected:
            raise AssertionError(f"routing_governor did not choose /{expected} for {query!r}\n{governor}")

        results.append(f"route ok: {query} -> /{expected}")
    return results


def main() -> int:
    checks = []
    checks.extend(verify_text())
    checks.extend(verify_sync_helper())
    checks.extend(verify_routes())
    print("ORCHESTRATE OPERATOR CORE VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
