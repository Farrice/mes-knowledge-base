#!/usr/bin/env python3
"""Verify always-on global and workspace steering closeout persistence."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GLOBAL_AGENTS = Path("/Users/farricecain/.codex/AGENTS.md")
LOCAL_AGENTS = ROOT / "AGENTS.md"
GLOBAL_END_SESSION = Path("/Users/farricecain/.codex/skills/end-session/SKILL.md")


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def require(label: str, text: str, needles: list[str]) -> None:
    lowered = text.lower()
    normalized = " ".join(lowered.split())
    missing = [
        needle
        for needle in needles
        if needle.lower() not in lowered and " ".join(needle.lower().split()) not in normalized
    ]
    if missing:
        fail(f"{label} missing: {', '.join(missing)}")


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def check_global_agents() -> None:
    """Verify that fresh tasks receive the visible closeout contract."""
    text = read(GLOBAL_AGENTS)
    require(
        "global AGENTS",
        text,
        [
            "Three Contextual Next Prompts",
            "After a meaningful response with a real next decision",
            "exactly three",
            "ranked, session-specific",
            "Recommended task title",
            "Expected outcome",
            "Quality bar",
            "materially different",
            "If the best next action is safe, local, and already authorized, execute it",
            "Compact Operator Lesson",
            "Operator move:",
            "Global Execution Bias Contract",
            "Patch + Verify",
            "system-audit",
        ],
    )


def check_local_agents() -> None:
    """Verify the newer Google-local no-padding steering constitution.

    Global persistence and local visible-shipping policy intentionally differ:
    the workspace skips steering on diagnostic, conversational, corrective, and
    mechanical turns while retaining rich closeouts for substantial shipments.
    """
    text = read(LOCAL_AGENTS)
    require(
        "workspace AGENTS",
        text,
        [
            "Per-Exchange Steering",
            "When an exchange SHIPS something",
            "Skip on answers, diagnostics, corrections",
            "Deep closeouts",
            "Insightful Momentum intelligence",
            "visible recommended task title",
            "expected artifact/decision/proof event",
            "inspectable quality bar",
            "contextual_next_prompts.py",
            "A skipped block is fine; a padded block is a failure",
        ],
    )


def check_end_session_bridge() -> None:
    text = read(GLOBAL_END_SESSION)
    require(
        "global end-session wrapper",
        text,
        [
            "Insightful Momentum/frontier standard",
            "legacy thin prompt shell",
            "contextual_next_prompts.py",
            "Output/Capability Move",
            "Operator Insight",
            "Hidden Gap/Opportunity",
            "Capability Revealed",
            "Recommended task title",
            "Expected outcome",
            "Quality bar",
        ],
    )


def check_renderer_visible_fields() -> None:
    proc = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--objective",
            "make this a persistent global per-exchange behavior not a command-only workflow and verify the visible answer surface",
        ]
    )
    if proc.returncode != 0:
        fail(f"contextual_next_prompts failed: {proc.stderr.strip()}")
    require(
        "renderer output",
        proc.stdout,
        [
            "## 3 Next Prompts",
            "Recommended task title",
            "Suggested follow-ups",
            "Output/Capability Move",
            "Operator Insight",
            "Hidden Gap/Opportunity",
            "Capability Revealed",
            "Expected outcome",
            "Quality bar",
            "Skip if",
            "Suggested skills/workflows",
            "normal-answer smoke test",
            "global and workspace instruction surfaces",
            "visible-answer proof",
        ],
    )


def main() -> int:
    checks = [
        check_global_agents,
        check_local_agents,
        check_end_session_bridge,
        check_renderer_visible_fields,
    ]
    failures: list[str] = []
    for check in checks:
        try:
            check()
        except Exception as exc:  # noqa: BLE001 - verifier reports all failures.
            failures.append(f"{check.__name__}: {exc}")
    if failures:
        print("GLOBAL STEERING PERSISTENCE VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("GLOBAL STEERING PERSISTENCE VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
