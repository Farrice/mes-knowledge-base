#!/usr/bin/env python3
"""Verify Codex-wide steering closeout defaults and Antigravity routing."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"


GLOBAL_SNIPPETS = [
    "Post-Output Steering Closeout",
    "Every final answer gets an Operator Lesson unless the user explicitly asks for only the direct answer.",
    # Anchor on the stable sentence stem — the global file extends it with
    # "under the Insightful Momentum standard" (behavior unchanged).
    "Close with steering by default: 3 Next Prompts using Use Now, Harden, and Expand",
    "## 3 Next Prompts",
    "Prompt",
    "Expected output",
    "Tiny answers get a micro lesson.",
    "Next-time prompt",
    "Subagent worth it?",
    "Reuse hook",
    "If the user explicitly asks for no next steps or only the direct answer, obey that.",
    "If the user says \"go with your verdict,\" continue the recommended path if clear.",
]


LOCAL_SNIPPETS = {
    # GEMINI.md is compiled (platform_compiler.py) and carries the always-on
    # steering contract; the "go with your verdict" fast-approval phrase is
    # pinned on its owners (global AGENTS.md + steering-compass.md) below.
    "GEMINI.md": [
        "ALWAYS-ON OPERATOR LESSON",
        "Operator Lesson: Next time, ask for [X] if you want [Y].",
        "3 Next Prompts",
    ],
    ".agent/workflows/extraction-governor-agent.md": [
        "Run the closeout steering compass",
        "## 3 Next Prompts",
    ],
    ".agent/workflows/steering-compass.md": [
        "post-output next steps",
        "go with your verdict",
        "always-on Operator Lesson",
        "3 Next Prompts",
    ],
}


SEARCH_QUERIES = [
    "go with your verdict",
    "what should I do next",
    "use your recommendation",
    "post output steering compass next steps recommendations",
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
        if stripped.startswith("1. `/") or stripped.startswith("/steering-compass"):
            return stripped
    return ""


def first_workflow_line(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            return stripped
    return ""


def verify_global_file() -> list[str]:
    if not GLOBAL_AGENTS.exists():
        raise AssertionError(f"Missing global instruction file: {GLOBAL_AGENTS}")

    text = GLOBAL_AGENTS.read_text(encoding="utf-8", errors="ignore")
    for snippet in GLOBAL_SNIPPETS:
        if snippet not in text:
            raise AssertionError(f"Missing global snippet: {snippet}")
    return [f"global AGENTS.md contains steering closeout rule: {GLOBAL_AGENTS}"]


def verify_local_files() -> list[str]:
    results = []
    for relative, snippets in LOCAL_SNIPPETS.items():
        path = ROOT / relative
        if not path.exists():
            raise AssertionError(f"Missing local file: {relative}")
        text = path.read_text(encoding="utf-8", errors="ignore")
        for snippet in snippets:
            if snippet not in text:
                raise AssertionError(f"Missing local snippet in {relative}: {snippet}")
        results.append(f"local steering rule present: {relative}")
    return results


def verify_routes() -> list[str]:
    results = []
    for query in SEARCH_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if "`/steering-compass`" not in first_menu:
            raise AssertionError(f"command_menu did not rank steering first for {query!r}\n{menu}")

        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if not first_router.startswith("/steering-compass"):
            raise AssertionError(f"workflow_router did not rank steering first for {query!r}\n{router}")

        results.append(f"natural phrase routes to steering: {query}")
    return results


def main() -> int:
    checks = []
    checks.extend(verify_global_file())
    checks.extend(verify_local_files())
    checks.extend(verify_routes())
    run([sys.executable, "execution/verify_steering_compass.py"])
    checks.append("workspace steering verifier still passes")

    print("GLOBAL STEERING CLOSEOUT VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
