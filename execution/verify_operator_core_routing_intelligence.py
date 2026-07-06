#!/usr/bin/env python3
"""Verify Routing-intelligence Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "routing-intelligence.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-routing-intelligence" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_ROUTING_INTELLIGENCE = Path.home() / ".codex" / "skills" / "routing-intelligence" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-routing-intelligence" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Routing-intelligence behavior",
        "read-only analytics by default",
        "python3 execution/routing_intelligence.py scoreboard",
        "python3 execution/routing_intelligence.py utilization",
        "python3 execution/routing_intelligence.py unused",
        "python3 execution/routing_intelligence.py domain-dist",
        "python3 execution/routing_intelligence.py top-combos",
        "python3 execution/routing_intelligence.py underperforming",
        "python3 execution/routing_intelligence.py misroute",
        "Only write routing feedback through `misroute` when the user explicitly reports a wrong route",
        "Do not auto-optimize routes, mutate workflows, sync Notion, mutate Mission, perform cleanup, or mirror global files",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/routing-intelligence.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "read-only routing analytics by default",
        "routing_intelligence.py scoreboard",
        "misroute",
        "explicitly reports a wrong route",
        "no auto-optimization",
        "Mission mutation",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Routing-intelligence Analytics",
        "/Users/farricecain/Google Antigravity/.agent/workflows/routing-intelligence.md",
        "thin compatibility wrappers",
        "read-only analytics dashboard",
        "routing_intelligence.py scoreboard",
        "misroute",
        "explicitly reports a wrong route",
        "Mission mutation",
        "Codex subagents without explicit authorization",
    ],
    GLOBAL_ROUTING_INTELLIGENCE: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/routing-intelligence.md",
        "thin compatibility wrapper",
        "read-only routing analytics by default",
        "routing_intelligence.py scoreboard",
        "misroute",
        "explicitly reports a wrong route",
        "no auto-optimization",
        "Mission mutation",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/routing-intelligence/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/routing-intelligence.md",
        "thin compatibility wrapper",
        "read-only routing analytics by default",
        "routing_intelligence.py scoreboard",
        "misroute",
        "explicitly reports a wrong route",
        "no auto-optimization",
        "Mission mutation",
        "real Codex subagents require explicit",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "python execution/routing_intelligence.py",
    "auto-optimize routes by default",
    "auto optimize routes by default",
    "mutate workflows by default",
    "sync Notion by default",
    "mutate Mission by default",
    "repair Mission by default",
    "write route feedback by default",
)

ROUTING_CASES = (
    ("routing intelligence dashboard", "routing-intelligence", "routing-intelligence-analytics"),
    ("source-command-routing-intelligence scoreboard", "routing-intelligence", "routing-intelligence-analytics"),
    ("show routing scoreboard", "routing-intelligence", "routing-intelligence-analytics"),
    ("audit routing-intelligence operator core drift", "system-audit", "system-failure"),
    ("the router is broken and routing intelligence is wrong", "autopilot", "system-failure"),
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


def detected_lane(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("- **Detected lane**:"):
            return stripped.split(":", 1)[-1].strip()
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
                raise AssertionError(f"Stale Routing-intelligence text in {path}: {snippet}")
        results.append(f"routing-intelligence contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_routing_intelligence.py", "--check"])
    return ["routing-intelligence sync helper passes"]


def verify_routes() -> list[str]:
    results = []
    for query, expected, expected_lane in ROUTING_CASES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if f"`/{expected}`" not in first_menu:
            raise AssertionError(f"command_menu expected /{expected} first for {query!r}; got {first_menu}")

        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if f"/{expected}" not in first_router:
            raise AssertionError(f"workflow_router expected /{expected} first for {query!r}; got {first_router}")

        governor = run([sys.executable, "execution/routing_governor.py", "evaluate", query])
        chosen = chosen_route(governor)
        lane = detected_lane(governor)
        if chosen != expected:
            raise AssertionError(f"routing_governor expected /{expected} for {query!r}; got /{chosen}")
        if lane != expected_lane:
            raise AssertionError(f"routing_governor expected lane {expected_lane} for {query!r}; got {lane}")
        results.append(f"routing guard: {query!r} -> /{expected} ({lane})")
    return results


def main() -> int:
    results = []
    results.extend(verify_text())
    results.extend(verify_sync_helper())
    results.extend(verify_routes())
    print("ROUTING-INTELLIGENCE OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
