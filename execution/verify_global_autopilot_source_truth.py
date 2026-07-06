#!/usr/bin/env python3
"""Verify global Autopilot delegates to the local intent-to-outcome source."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "autopilot.md"
PROJECT_WORKFLOW_TEXT = str(PROJECT_WORKFLOW)
GLOBAL_AUTOPILOT = Path("/Users/farricecain/.codex/skills/autopilot/SKILL.md")
GLOBAL_WRAPPER = Path("/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md")

REQUIRED_GLOBAL = (
    "Project Source Of Truth",
    PROJECT_WORKFLOW_TEXT,
    "compatibility/front-door wrapper",
    "not a competing behavior contract",
    "intent-to-outcome",
    "Execution Decision",
    "Running now",
    "Needs judgment",
    "Blocked by risk",
    "Plan only",
    "safe local execution",
    "Run Prompt",
    "Run Receipt",
    "Friction Ledger",
    "autopilot_runtime_preflight.py",
    "3 Next Prompts",
    "Operator Lesson",
    "Next-time prompt",
    "Subagent worth it?",
    "Reuse hook",
    "real Codex subagents require explicit authorization",
)

REQUIRED_WRAPPER = (
    "compatibility alias",
    "/Users/farricecain/.codex/skills/autopilot/SKILL.md",
    PROJECT_WORKFLOW_TEXT,
    "source of truth",
    "intent-to-outcome",
    "Execution Decision",
    "Running now",
    "Needs judgment",
    "Blocked by risk",
    "Plan only",
    "safe workspace-local work",
    "Run Prompt",
    "Run Receipt",
    "Friction Ledger",
    "3 Next Prompts",
    "Operator Lesson",
    "Next-time prompt",
    "Subagent worth it?",
    "Reuse hook",
    "real Codex subagents require explicit authorization",
)

FORBIDDEN = (
    "pause every time",
    "Waiting for explicit approval before execution",
    "**Execution not performed**",
    "Approval Checkpoint that always waits",
    "approval-gated planning",
)


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8", errors="ignore")


def require(label: str, text: str, snippets: tuple[str, ...]) -> list[str]:
    normalized = re.sub(r"\s+", " ", text)
    return [
        f"{label} missing: {snippet}"
        for snippet in snippets
        if re.sub(r"\s+", " ", snippet) not in normalized
    ]


def forbid(label: str, text: str) -> list[str]:
    text_lower = text.lower()
    failures = []
    for snippet in FORBIDDEN:
        if snippet.lower() in text_lower:
            failures.append(f"{label} contains stale Autopilot contract: {snippet}")
    return failures


def main() -> int:
    failures: list[str] = []

    project = read(PROJECT_WORKFLOW)
    global_autopilot = read(GLOBAL_AUTOPILOT)
    global_wrapper = read(GLOBAL_WRAPPER)

    failures.extend(require("project workflow", project, ("Intent-To-Outcome", "Execution Decision", "Running now")))
    failures.extend(require("global autopilot", global_autopilot, REQUIRED_GLOBAL))
    failures.extend(require("global source-command wrapper", global_wrapper, REQUIRED_WRAPPER))
    failures.extend(forbid("global autopilot", global_autopilot))
    failures.extend(forbid("global source-command wrapper", global_wrapper))

    if failures:
        print("GLOBAL AUTOPILOT SOURCE TRUTH VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("GLOBAL AUTOPILOT SOURCE TRUTH VERIFICATION PASS")
    print(f"- project source: {PROJECT_WORKFLOW.relative_to(ROOT)}")
    print(f"- global skill: {GLOBAL_AUTOPILOT}")
    print(f"- global wrapper: {GLOBAL_WRAPPER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
