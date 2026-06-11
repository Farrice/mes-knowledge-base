#!/usr/bin/env python3
"""Verify always-on Operator Lesson defaults and Autopilot routing cues."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_AUTOPILOT = Path.home() / ".codex" / "skills" / "autopilot" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-autopilot" / "SKILL.md"


REQUIRED_TEXT = {
    GLOBAL_AGENTS: [
        "Always-On Operator Lesson",
        "Every final answer gets an Operator Lesson unless the user explicitly asks for only the direct answer.",
        "3 Next Prompts",
        "Operator Lesson: Next time, ask for [X] if you want [Y].",
        "Subagent worth it?",
        "Next-time prompt",
        "Reuse hook",
        "Do not add this after special tool actions that require silence",
        "real Codex subagents require explicit authorization",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/autopilot.md",
        "compatibility/front-door wrapper",
    ],
    GLOBAL_AUTOPILOT: [
        "3 Next Prompts",
        "Operator Lesson",
        "Subagent worth it?",
        "Next-time prompt",
        "Reuse hook",
        "real Codex subagents require explicit authorization",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/autopilot.md",
        "compatibility/front-door wrapper",
        "not a competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "3 Next Prompts",
        "Operator Lesson",
        "Subagent worth it?",
        "Next-time prompt",
        "Reuse hook",
        "real Codex subagents require explicit authorization",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/autopilot.md",
    ],
    ROOT / "GEMINI.md": [
        "ALWAYS-ON OPERATOR LESSON",
        "Operator Lesson: Next time, ask for [X] if you want [Y].",
        "Subagent worth it?",
        "Reuse hook",
    ],
    ROOT / ".agent/workflows/autopilot.md": [
        "3 Next Prompts",
        "Operator Lesson",
        "Subagent worth it?",
        "Next-time prompt",
        "Reuse hook",
        "real Codex subagents require explicit authorization",
    ],
    ROOT / ".agents/skills/source-command-autopilot/SKILL.md": [
        "canonical behavior source",
        "3 Next Prompts",
        "Operator Lesson",
        "Subagent worth it?",
        "Next-time prompt",
        "Reuse hook",
        "real Codex subagents require explicit authorization",
    ],
    ROOT / "agents/operator-autopilot/AGENT.md": [
        "always-on operator coach",
        "Operator Lesson",
        "Subagent worth it?",
        "Reuse hook",
    ],
    ROOT / "semantic_libraries/antigravity/primitives/collaborative-steering-compass.md": [
        "always-on Operator Lesson",
        "Every final answer gives the user something to react to",
        "micro Operator Lesson",
        "Subagent worth it?",
        "Next-time prompt",
    ],
}


ROUTING_QUERIES = [
    "underusing agents forgetting subagents teach me every exchange",
    "autopilot plan mode operator lesson subagent worth it",
]


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


def verify_text() -> list[str]:
    results = []
    for path, snippets in REQUIRED_TEXT.items():
        if not path.exists():
            raise AssertionError(f"Missing file: {path}")
        text = path.read_text(encoding="utf-8", errors="ignore")
        normalized_text = " ".join(text.split())
        for snippet in snippets:
            if " ".join(snippet.split()) not in normalized_text:
                raise AssertionError(f"Missing snippet in {path}: {snippet}")
        results.append(f"operator lesson text present: {path}")
    return results


def verify_global_alignment_helper() -> list[str]:
    run([sys.executable, "execution/sync_global_operator_core.py", "--check"])
    return ["global Operator Core sync helper passes"]


def verify_routes() -> list[str]:
    results = []
    for query in ROUTING_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if "`/autopilot`" not in first_menu:
            raise AssertionError(f"command_menu did not rank autopilot first for {query!r}\n{menu}")

        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if not first_router.startswith("/autopilot"):
            raise AssertionError(f"workflow_router did not rank autopilot first for {query!r}\n{router}")

        results.append(f"autopilot routes first: {query}")
    return results


def main() -> int:
    checks = []
    checks.extend(verify_text())
    checks.extend(verify_global_alignment_helper())
    checks.extend(verify_routes())
    print("OPERATOR LESSON VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
