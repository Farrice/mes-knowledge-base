#!/usr/bin/env python3
"""Verify the explicit-only /embody command surface and ownership boundary."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> str:
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr or completed.stdout)
    return completed.stdout


def first_route(output: str) -> str | None:
    match = re.search(r"(?:^\s*1\.\s+|^\s*)(`?/[^`\s]+`?)", output, re.MULTILINE)
    return match.group(1).strip("`") if match else None


def main() -> int:
    errors: list[str] = []
    paths = {
        "workflow": ROOT / ".agent/workflows/embody.md",
        "operator_owner": ROOT / ".agent/workflows/operator-school.md",
        "codex_bridge": ROOT / ".agents/skills/source-command-embody/SKILL.md",
        "codex_policy": ROOT / ".agents/skills/source-command-embody/agents/openai.yaml",
        "claude_bridge": ROOT / ".claude/commands/embody.md",
    }
    for label, path in paths.items():
        if not path.exists():
            errors.append(f"missing {label}: {path.relative_to(ROOT)}")

    if not errors:
        workflow = paths["workflow"].read_text()
        owner = paths["operator_owner"].read_text()
        bridge = paths["codex_bridge"].read_text()
        policy = paths["codex_policy"].read_text()

        required_workflow_phrases = (
            "Use only when Farrice explicitly invokes `/embody`",
            "Run-Scoped Default",
            "Cold Retrieval",
            "Blind Discrimination",
            "Near And Far Transfer",
            "Recovery Rep",
            "Performance And Teach-Back",
            "Same-session fluency is not called retention",
        )
        for phrase in required_workflow_phrases:
            if phrase not in workflow:
                errors.append(f"workflow missing contract phrase: {phrase}")
        if "## Explicit Embody Mode" not in owner:
            errors.append("operator-school does not own Explicit Embody Mode")
        if "thin command bridge" not in bridge:
            errors.append("Codex bridge does not declare thin ownership")
        if "allow_implicit_invocation: false" not in policy:
            errors.append("Codex skill policy is not explicit-only")

    try:
        command_output = run(
            "execution/command_menu.py", "search", "/embody this extraction"
        )
        if first_route(command_output) != "/embody":
            errors.append("explicit /embody query does not rank /embody first")

        negative_output = run(
            "execution/workflow_router.py",
            "search",
            "convene a deliberate council to debate this strategy",
        )
        if first_route(negative_output) != "/convene":
            errors.append("deliberate-council negative control no longer belongs to /convene")
    except RuntimeError as exc:
        errors.append(f"route probe failed: {exc}")

    if errors:
        print("EMBODY COMMAND VERIFICATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("EMBODY COMMAND VERIFICATION PASS")
    print("- owner: /operator-school")
    print("- invocation: explicit-only /embody")
    print("- persistence: off by default")
    print("- deliberate-council negative control: /convene")
    return 0


if __name__ == "__main__":
    sys.exit(main())
