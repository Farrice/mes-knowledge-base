#!/usr/bin/env python3
"""Verify that the steering compass is wired as a closeout default."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


REQUIRED_FILES = [
    Path("GEMINI.md"),
    Path(".agent/workflows/steering-compass.md"),
    Path(".claude/commands/steering-compass.md"),
    Path(".agents/cold-skills/source-command-wrappers/source-command-steering-compass/SKILL.md"),
    Path(".agent/workflows/extraction-governor-agent.md"),
    Path("skills/semantic-document-library-os/workflows/steering-compass.md"),
    Path("semantic_libraries/antigravity/primitives/collaborative-steering-compass.md"),
    Path("semantic_libraries/antigravity/primitives/high-floor-operator-os.md"),
]


REQUIRED_TEXT = {
    "GEMINI.md": [
        "ALWAYS-ON OPERATOR LESSON",
        "go with your verdict",
        "Operator Lesson: Next time, ask for [X] if you want [Y].",
    ],
    ".agent/workflows/extraction-governor-agent.md": [
        "Run the closeout steering compass",
        "## 3 Next Prompts",
        "**Use Now**",
        "**Harden**",
        "**Expand**",
        "**Prompt:**",
    ],
    ".agent/workflows/steering-compass.md": [
        "post-output next steps",
        "go with your verdict",
        "always-on Operator Lesson",
        "completed work into momentum",
        "3 Next Prompts",
        "copy-paste prompt",
    ],
    ".claude/commands/steering-compass.md": [
        "post-output next steps",
        "go with your verdict",
        "always-on Operator Lesson",
    ],
    ".agents/cold-skills/source-command-wrappers/source-command-steering-compass/SKILL.md": [
        "post-output next steps",
        "go with your verdict",
        "always-on Operator Lesson",
    ],
    "skills/semantic-document-library-os/workflows/steering-compass.md": [
        "Fast approval phrase",
        "execute the recommended path directly",
        "## 3 Next Prompts",
        "**Prompt:**",
    ],
    "semantic_libraries/antigravity/primitives/collaborative-steering-compass.md": [
        "go with your verdict",
        "Every final answer gives the user something to react to",
        "Operator Lesson",
        "Execute the prior recommended path if clear",
        "3 Next Prompts",
        "copy-paste continuation prompts",
    ],
    "semantic_libraries/antigravity/primitives/high-floor-operator-os.md": [
        "Final answer lacks a learning cue",
        "Operator Lesson",
        "Execute the prior recommended path if clear",
    ],
}


SEARCH_QUERIES = [
    "post output steering compass next steps recommendations",
    "what should I do next after extraction output",
    "three next prompts after final answer",
    "turn this output into contextual next prompts",
    "go with your verdict you just gave me",
    "use your verdict and do the next step",
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
        if stripped.startswith("1. `/") or stripped.startswith("/steering-compass") or stripped.startswith("/"):
            return stripped
    return ""


def first_workflow_line(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            return stripped
    return ""


def verify_files() -> list[str]:
    results = []
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.exists():
            raise AssertionError(f"Missing required file: {relative}")
        results.append(f"file exists: {relative}")

    for relative, snippets in REQUIRED_TEXT.items():
        text = (ROOT / relative).read_text(encoding="utf-8", errors="ignore")
        for snippet in snippets:
            if snippet not in text:
                raise AssertionError(f"Missing snippet in {relative}: {snippet}")
        results.append(f"content check: {relative}")
    return results


def verify_bridge() -> list[str]:
    output = run([sys.executable, "execution/command_menu.py", "show", "steering-compass"])
    required = [
        "Workflow: `.agent/workflows/steering-compass.md`",
        "Source command: `.claude/commands/steering-compass.md`",
        "Cold Codex wrapper: `.agents/cold-skills/source-command-wrappers/source-command-steering-compass/SKILL.md`",
    ]
    for snippet in required:
        if snippet not in output:
            raise AssertionError(f"Bridge show missing: {snippet}\n{output}")
    return ["bridge show: steering-compass"]


def verify_search() -> list[str]:
    results = []
    for query in SEARCH_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if "`/steering-compass`" not in first_menu:
            raise AssertionError(f"command_menu did not rank steering-compass first for {query!r}\n{menu}")

        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if not first_router.startswith("/steering-compass"):
            raise AssertionError(f"workflow_router did not rank steering-compass first for {query!r}\n{router}")

        results.append(f"search ranks steering first: {query}")
    return results


def main() -> int:
    checks = []
    checks.extend(verify_files())
    checks.extend(verify_bridge())
    checks.extend(verify_search())

    print("STEERING COMPASS VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
