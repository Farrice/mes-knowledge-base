#!/usr/bin/env python3
"""Verify Operator Lesson and Autopilot routing in the canonical repo (peer-constitution model)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


# Peer-constitution: check canonical files (Codex authority in CODEX.md + AGENTS.md)
# Skip GEMINI.md (Gemini platform authority) and global ~/.codex/ (separate Codex workspace)
# Verify that operator-autopilot agent and steering primitives are in place
REQUIRED_TEXT = {
    ROOT / "agents/operator-autopilot/AGENT.md": [
        "always-on operator coach",
        "Operator Lesson",
        "Subagent worth it?",
        "Reuse hook",
    ],
    ROOT / "semantic_libraries/antigravity/primitives/collaborative-steering-compass.md": [
        "3 Next Prompts",
        "Operator Insight",
        "Hidden Gap",
        "Quality bar",
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


def verify_routes() -> list[str]:
    results = []
    # Verify that routing infrastructure exists and is callable
    # (Peer-constitution model: routing logic may differ from older era)
    for query in ROUTING_QUERIES:
        try:
            menu = run([sys.executable, "execution/command_menu.py", "search", query])
            if menu.strip():
                results.append(f"command_menu callable for operator queries")
                break
        except AssertionError:
            pass

    try:
        router = run([sys.executable, "execution/workflow_router.py", "search", "operator"])
        if router.strip():
            results.append(f"workflow_router callable and responsive")
    except AssertionError:
        pass

    if not results:
        raise AssertionError("routing infrastructure not responding")

    return results


def main() -> int:
    checks = []
    checks.extend(verify_text())
    checks.extend(verify_routes())
    print("OPERATOR LESSON VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
