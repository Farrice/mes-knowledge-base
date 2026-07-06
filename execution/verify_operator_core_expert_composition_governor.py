#!/usr/bin/env python3
"""Verify Expert-composition-governor Operator Core source truth and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "expert-composition-governor.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-expert-composition-governor" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_EXPERT_COMPOSITION = Path.home() / ".codex" / "skills" / "expert-composition-governor" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-expert-composition-governor" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Google Antigravity/.agent/workflows/expert-composition-governor.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Expert-composition-governor behavior",
        "prevents expert soup and full-arsenal sprawl",
        "more than three experts/routes are plausible",
        "One function owner must integrate the final result",
        "Specialists must occupy bounded slots",
        "The Composition Ledger must show accepted, skipped, or rejected contributions with evidence of change",
        "Expert names are not proof; integration evidence is proof",
        "Do not spawn real Codex subagents unless explicitly authorized",
        "Route broad broken-harness triage to `/autopilot` or `/system-audit`",
        "route reusable source-to-system builds to `/source-to-skill-system`",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/expert-composition-governor.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "prevent expert soup",
        "full-arsenal sprawl",
        "more than three experts/routes",
        "one function owner integrates the final result",
        "bounded slots",
        "Composition Ledger",
        "evidence of change",
        "expert names are not proof",
        "no real Codex subagents unless explicitly authorized",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Expert-composition Governor",
        CANONICAL_PATH,
        "thin compatibility wrappers",
        "prevent expert soup",
        "full-arsenal sprawl",
        "more than three experts/routes",
        "one function owner",
        "bounded slots",
        "Composition Ledger",
        "evidence of change",
        "expert names are not proof",
        "real Codex subagents unless explicitly authorized",
        "/source-to-skill-system",
    ],
    GLOBAL_EXPERT_COMPOSITION: [
        "Project Source Of Truth",
        CANONICAL_PATH,
        "thin compatibility wrapper",
        "prevent expert soup",
        "full-arsenal sprawl",
        "more than three experts/routes",
        "one function owner",
        "bounded slots",
        "Composition Ledger",
        "evidence of change",
        "expert names are not proof",
        "no real Codex subagents unless explicitly authorized",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/expert-composition-governor/SKILL.md",
        CANONICAL_PATH,
        "thin compatibility wrapper",
        "prevent expert soup",
        "full-arsenal sprawl",
        "more than three experts/routes",
        "one function owner",
        "bounded slots",
        "Composition Ledger",
        "evidence of change",
        "expert names are not proof",
        "no real Codex subagents unless explicitly authorized",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "spawn subagents by default",
    "full arsenal by default",
    "experts are proof",
)

ROUTING_CASES = (
    ("expert soup too many agents full arsenal", "expert-composition-governor", "expert-composition"),
    ("source-command-expert-composition-governor full arsenal", "expert-composition-governor", "expert-composition"),
    ("too many experts not interwoven hammer instead of scalpel", "expert-composition-governor", "expert-composition"),
    ("audit expert-composition-governor operator core drift", "system-audit", "system-failure"),
    ("expert-composition-governor is broken and creates expert soup", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Expert-composition-governor text in {path}: {snippet}")
        results.append(f"expert-composition contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_expert_composition_governor.py", "--check"])
    return ["expert-composition sync helper passes"]


def verify_legacy_standard() -> list[str]:
    run([sys.executable, "execution/verify_expert_composition_standard.py"])
    return ["expert-composition legacy standard passes"]


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
    results.extend(verify_legacy_standard())
    results.extend(verify_routes())
    print("EXPERT-COMPOSITION-GOVERNOR OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
