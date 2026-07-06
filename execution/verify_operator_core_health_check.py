#!/usr/bin/env python3
"""Verify Health-check Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "health-check.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-health-check" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_HEALTH_CHECK = Path.home() / ".codex" / "skills" / "health-check" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-health-check" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Health-check behavior",
        "read-only by default",
        "python3 execution/harness_status.py --plain",
        "python3 execution/system_health.py --quick",
        "python3 execution/operator_core_status.py --plain",
        "Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested",
        "Mission remains read-only unless `python3 execution/verify_mission_activation_contract.py` fails",
        "Route system-failure or drift-audit language to `/autopilot` or `/system-audit`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/health-check.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "read-only status by default",
        "harness_status.py --plain",
        "system_health.py --quick",
        "operator_core_status.py --plain",
        "no report writes",
        "Notion sync",
        "route optimization",
        "Mission mutation",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Health-check Status",
        "/Users/farricecain/Google Antigravity/.agent/workflows/health-check.md",
        "thin compatibility wrappers",
        "read-only status",
        "harness_status.py --plain",
        "system_health.py --quick",
        "operator_core_status.py --plain",
        "no report writes",
        "Notion",
        "route optimization",
        "Mission mutation",
        "verify_mission_activation_contract.py",
        "Codex subagents without explicit authorization",
    ],
    GLOBAL_HEALTH_CHECK: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/health-check.md",
        "thin compatibility wrapper",
        "read-only status by default",
        "harness_status.py --plain",
        "system_health.py --quick",
        "operator_core_status.py --plain",
        "no report writes",
        "live Notion sync",
        "route optimization",
        "Mission mutation",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/health-check/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/health-check.md",
        "thin compatibility wrapper",
        "read-only status by default",
        "harness_status.py --plain",
        "system_health.py --quick",
        "operator_core_status.py --plain",
        "no report",
        "live Notion sync",
        "route optimization",
        "Mission mutation",
        "verify_mission_activation_contract.py",
        "real Codex subagents require",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "python execution/system_health.py",
    "/skill-evolution",
    "write reports by default",
    "writes a report by default",
    "auto-optimize",
    "auto optimize",
    "auto-sync",
    "auto sync",
    "live Notion write",
    "mutate Mission by default",
    "repair Mission by default",
)

ROUTING_CASES = (
    ("health check harness status", "health-check"),
    ("source-command-health-check show status", "health-check"),
    ("run harness status", "health-check"),
    ("audit health-check operator core drift", "system-audit"),
    ("what is broken in the harness", "autopilot"),
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
                raise AssertionError(f"Stale Health-check text in {path}: {snippet}")
        results.append(f"health-check contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_health_check.py", "--check"])
    return ["health-check sync helper passes"]


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
    print("HEALTH-CHECK OPERATOR CORE VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
