#!/usr/bin/env python3
"""Verify lifecycle-truthful End-session visible closeout behavior."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".agent" / "workflows" / "end-session.md"
BENCHMARK = (
    ROOT
    / "semantic_libraries"
    / "antigravity"
    / "primitives"
    / "end-session-visible-closeout-benchmark.md"
)

LEGACY_VISIBLE_LABELS = (
    "Output/Capability Move",
    "Operator Insight",
    "Hidden Gap/Opportunity",
    "Capability Revealed",
    "Suggested follow-ups:",
    "**Use Now**",
    "**Harden**",
    "**Expand**",
)


def audit_visible_closeout(text: str, state: str) -> list[str]:
    """Return contract violations for a completed or approval-blocked answer."""
    failures: list[str] = []
    numbered = re.findall(r"(?m)^[1-3]\. \*\*", text)
    prompt_lines = re.findall(r"(?m)^\s+\*\*Prompt:\*\*", text)

    if state == "completed":
        required = (
            "Closeout: COMPLETE",
            "Coordinator receipt: VALID",
            "## 3 Next Prompts",
            "Operator move:",
        )
        for marker in required:
            if marker not in text:
                failures.append(f"completed closeout missing {marker!r}")
        if len(numbered) != 3:
            failures.append(f"completed closeout needs exactly 3 numbered prompts, found {len(numbered)}")
        if len(prompt_lines) != 3:
            failures.append(f"completed closeout needs exactly 3 Prompt lines, found {len(prompt_lines)}")
        if re.search(r"(?im)^\s*\*\*Prompt:\*\*.*?/end-session\b", text):
            failures.append("completed closeout routes a prompt back into /end-session")
        if "Closeout: PENDING APPROVAL" in text:
            failures.append("completed closeout also claims pending approval")
    elif state == "approval-blocked":
        required = (
            "Closeout: PENDING APPROVAL",
            "Coordinator receipt: BLOCKED",
            "Task remains unarchived",
            "Prepared artifacts remain in",
        )
        for marker in required:
            if marker not in text:
                failures.append(f"approval-blocked closeout missing {marker!r}")
        approval_lines = re.findall(r"(?m)^Approval needed: .+", text)
        if len(approval_lines) != 1:
            failures.append(
                f"approval-blocked closeout needs exactly one Approval needed line, found {len(approval_lines)}"
            )
        if "## 3 Next Prompts" in text or numbered or prompt_lines:
            failures.append("approval-blocked closeout contains a completion-shaped prompt menu")
        for claim in ("Saved + pinned", "Archived successfully", "Closeout: COMPLETE"):
            if claim.lower() in text.lower():
                failures.append(f"approval-blocked closeout makes false completion claim {claim!r}")
        if not re.search(r"Prepared artifacts remain in [`']?(?:\.tmp/|\.agent/|/)", text):
            failures.append("approval-blocked closeout has no exact recoverable artifact path")
    else:
        failures.append(f"unknown closeout state: {state}")

    for label in LEGACY_VISIBLE_LABELS:
        if label in text:
            failures.append(f"visible closeout leaks retired label {label!r}")
    return failures


def render_compact_fixture() -> str:
    command = [
        sys.executable,
        "execution/contextual_next_prompts.py",
        "--objective",
        "Parallel Lanes Reliability closeout",
        "--format",
        "compact",
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise AssertionError(f"compact renderer failed: {result.stderr.strip()}")
    return "\n".join(
        [
            "Closeout: COMPLETE",
            "Coordinator receipt: VALID — handoff verified and task action applied.",
            "Handoff: `.agent/handoffs/2026-08-31-parallel-lanes-reliability.md`",
            "",
            result.stdout.strip(),
            "",
            "Operator move: Let the receipt choose the lifecycle state before presentation chooses the format.",
        ]
    )


def verify_static_contract() -> list[str]:
    failures: list[str] = []
    workflow = WORKFLOW.read_text(encoding="utf-8")
    benchmark = BENCHMARK.read_text(encoding="utf-8")
    workflow_markers = (
        "valid: true",
        "dry_run: false",
        "--format compact",
        "Closeout: PENDING APPROVAL",
        "Task remains unarchived",
        "Approval needed:",
        "end-session-visible-closeout-benchmark.md",
        "never route a completed closeout back into `/end-session`",
    )
    for marker in workflow_markers:
        if marker not in workflow:
            failures.append(f"canonical workflow missing {marker!r}")
    benchmark_markers = (
        "## Skill System Contract",
        "## Goal Packet",
        "## Agentic Engineering Packet",
        "## Winning Example: Verified Completed",
        "## Winning Example: Approval-Blocked",
        "## Failure Cases",
        "## Verifier Expectations",
        "## Cold-Start Replay Prompt",
        "## Reuse Hook",
    )
    for marker in benchmark_markers:
        if marker not in benchmark:
            failures.append(f"benchmark missing {marker!r}")
    return failures


def verify_controls() -> list[str]:
    failures: list[str] = []

    completed = render_compact_fixture()
    failures.extend(audit_visible_closeout(completed, "completed"))

    blocked = """Closeout: PENDING APPROVAL
Coordinator receipt: BLOCKED — global pointer write and branch push were not authorized.
Task remains unarchived. Prepared artifacts remain in `.tmp/end-session/parallel-lanes-reliability/`.
Approval needed: "Approve the coordinator to write pointer receipts and push only the named Codex branch."
"""
    failures.extend(audit_visible_closeout(blocked, "approval-blocked"))

    known_bad = {
        "blocked-menu": (
            blocked + "\n## 3 Next Prompts\n1. **Keep going**\n   **Prompt:** \"Continue.\"",
            "approval-blocked",
        ),
        "blocked-false-completion": (
            blocked + "\nSaved + pinned: `.agent/handoffs/example.md`\nArchived successfully.",
            "approval-blocked",
        ),
        "legacy-rich-fields": (
            completed
            + "\n**Use Now**\n**Output/Capability Move:** X\n**Operator Insight:** Y\n"
            + "**Hidden Gap/Opportunity:** Z\n**Capability Revealed:** Q",
            "completed",
        ),
        "self-loop": (
            completed.replace(
                "**Prompt:** \"",
                "**Prompt:** \"/end-session ",
                1,
            ),
            "completed",
        ),
        "vague-blocker": (
            "Closeout: PENDING APPROVAL\nCoordinator receipt: BLOCKED\nI need approval to continue.",
            "approval-blocked",
        ),
    }
    for name, (text, state) in known_bad.items():
        if not audit_visible_closeout(text, state):
            failures.append(f"known-bad control unexpectedly passed: {name}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, help="Audit one visible closeout file.")
    parser.add_argument("--state", choices=("completed", "approval-blocked"))
    args = parser.parse_args()

    if args.file:
        if not args.state:
            parser.error("--state is required with --file")
        failures = audit_visible_closeout(args.file.read_text(encoding="utf-8"), args.state)
    else:
        failures = verify_static_contract() + verify_controls()

    if failures:
        print("END-SESSION VISIBLE CLOSEOUT VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("END-SESSION VISIBLE CLOSEOUT VERIFICATION PASS")
    print("- completed fixture: compact, ranked, receipt-gated")
    print("- approval-blocked fixture: bounded, recoverable, unarchived")
    print("- known-bad controls: rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
