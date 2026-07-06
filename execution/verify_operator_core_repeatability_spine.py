#!/usr/bin/env python3
"""Verify Repeatability-spine Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "repeatability-spine.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-repeatability-spine" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_REPEATABILITY = Path.home() / ".codex" / "skills" / "repeatability-spine" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-repeatability-spine" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Repeatability-spine behavior",
        "preserves the good example before repair",
        "Every run needs grounded evidence, one primary failure class, Preservation Lock, repair route, validation, regression guard, and replay prompt",
        "Inaccessible conversations are pending evidence, not invented findings",
        "Routing failures require a verifier query or routing feedback log before being called repaired",
        "Mutation-capable repair routes (`/self-evolve`, `/skill-anneal`, `/skill-evolution`) require a Goal Packet before edits",
        "Global `~/.codex` behavior changes require workspace proof and explicit approval",
        "Route broad broken-harness triage to `/autopilot` or `/system-audit`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/repeatability-spine.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "preserve the good example",
        "grounded evidence",
        "primary failure class",
        "Preservation Lock",
        "repair route",
        "validation",
        "regression guard",
        "replay prompt",
        "pending evidence",
        "verifier query or routing feedback log",
        "Goal Packet",
        "workspace proof and explicit approval",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Repeatability-spine Regression Repair",
        "/Users/farricecain/Google Antigravity/.agent/workflows/repeatability-spine.md",
        "thin compatibility wrappers",
        "preserve the good example",
        "grounded evidence",
        "primary failure class",
        "Preservation Lock",
        "repair route",
        "validation",
        "regression guard",
        "replay prompt",
        "pending evidence",
        "verifier query or routing feedback log",
        "Goal Packet",
        "workspace proof and explicit approval",
        "Codex subagents require explicit authorization",
    ],
    GLOBAL_REPEATABILITY: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/repeatability-spine.md",
        "thin compatibility wrapper",
        "preserve the good example",
        "grounded evidence",
        "primary failure class",
        "Preservation Lock",
        "repair route",
        "validation",
        "regression guard",
        "replay prompt",
        "pending evidence",
        "verifier query or routing feedback log",
        "Goal Packet",
        "workspace proof and explicit approval",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/repeatability-spine/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/repeatability-spine.md",
        "thin compatibility wrapper",
        "preserve the good example",
        "grounded evidence",
        "primary failure class",
        "Preservation Lock",
        "repair route",
        "validation",
        "regression guard",
        "replay prompt",
        "pending evidence",
        "verifier query or routing feedback log",
        "Goal Packet",
        "workspace proof and explicit approval",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "revise without a Preservation Lock",
    "invent findings by default",
    "global behavior changes by default",
    "mutate by default",
)

ROUTING_CASES = (
    ("source-command-repeatability-spine preserve what worked in this failed revision", "repeatability-spine", "repeatability"),
    ("the revision got worse and lost the good part", "repeatability-spine", "repeatability"),
    ("wrong route picked the wrong workflow and I need a regression guard", "repeatability-spine", "repeatability"),
    ("audit repeatability-spine operator core drift", "system-audit", "system-failure"),
    ("repeatability-spine is broken and inventing findings", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Repeatability-spine text in {path}: {snippet}")
        results.append(f"repeatability-spine contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_repeatability_spine.py", "--check"])
    return ["repeatability-spine sync helper passes"]


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
    print("REPEATABILITY-SPINE OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
