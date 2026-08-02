#!/usr/bin/env python3
"""Verify End-session Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "end-session.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-end-session" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_END_SESSION = Path.home() / ".codex" / "skills" / "end-session" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-end-session" / "SKILL.md"

CODEX_NATIVE_TEXT = [
    "handoff_store.py verify",
    "codex_end_session.py run --manifest",
    "[Domain]: [Specific Object] - [Outcome]",
    "archive only",
    "dedicated `codex/*` worktree",
    "Never auto-commit, auto-merge, or auto-push `main`",
]

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for End-session behavior",
        "whole-session closeout",
        "not `/handoff`",
        "not `/steering-compass`",
        "3 Next Prompts",
        "Operator Lesson",
        "Next-time prompt",
        "Subagent worth it?",
        "Reuse hook",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        *CODEX_NATIVE_TEXT,
        "Optional cleanup must be reviewed",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/end-session.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "whole-session closeout",
        "closeout intelligence capture",
        "3 Next Prompts",
        "Operator Lesson",
        "Next-time prompt",
        "Subagent worth it?",
        "Reuse hook",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        *CODEX_NATIVE_TEXT,
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global End-Session Closeout",
        "/Users/farricecain/Google Antigravity/.agent/workflows/end-session.md",
        "thin compatibility wrappers",
        "whole-session closeout",
        "retrieval handoff",
        "closeout intelligence capture",
        "3 Next Prompts",
        "Operator Lesson",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        *CODEX_NATIVE_TEXT,
        "Real Codex subagents require explicit authorization",
    ],
    GLOBAL_END_SESSION: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/end-session.md",
        "thin compatibility wrapper",
        "whole-session closeout",
        "retrieval handoff",
        "closeout intelligence capture",
        "3 Next Prompts",
        "Operator Lesson",
        "Next-time prompt",
        "Subagent worth it?",
        "Reuse hook",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        *CODEX_NATIVE_TEXT,
        "Insightful Momentum/frontier standard",
        "legacy thin prompt shell",
        "contextual_next_prompts.py",
        "Output/Capability Move",
        "Operator Insight",
        "Hidden Gap/Opportunity",
        "Capability Revealed",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/end-session/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/end-session.md",
        "thin compatibility wrapper",
        "whole-session closeout",
        "retrieval handoff",
        "closeout intelligence capture",
        "3 Next Prompts",
        "Operator Lesson",
        "Next-time prompt",
        "Subagent worth it?",
        "Reuse hook",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        *CODEX_NATIVE_TEXT,
        "real Codex subagents require explicit",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "conversation_index.py update <current-conversation-id>",
    "manual closeout only",
    "skip closeout intelligence",
    "generic handoff only",
    "spawn real Codex subagents by default",
    "push without confirmation",
    "plan-first approval checkpoint",
)

ROUTING_CASES = (
    ("end session handoff closeout intelligence", "end-session"),
    ("wrap this session", "end-session"),
    ("source-command-end-session closeout", "end-session"),
    ("session closeout intelligence", "end-session"),
    ("prepare a handoff document for a fresh agent to continue this in another conversation", "handoff"),
    ("three next prompts after final answer", "steering-compass"),
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
                raise AssertionError(f"Stale End-session text in {path}: {snippet}")
        results.append(f"end-session contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_end_session.py", "--check"])
    return ["end-session sync helper passes"]


def verify_routes() -> list[str]:
    results = []
    for query, expected in ROUTING_CASES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if f"`/{expected}`" not in first_menu:
            raise AssertionError(f"command_menu did not rank /{expected} first for {query!r}\n{menu}")

        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if not first_router.startswith(f"/{expected}"):
            raise AssertionError(f"workflow_router did not rank /{expected} first for {query!r}\n{router}")

        governor = run([sys.executable, "execution/routing_governor.py", "evaluate", query])
        if chosen_route(governor) != expected:
            raise AssertionError(f"routing_governor did not choose /{expected} for {query!r}\n{governor}")

        results.append(f"route ok: {query} -> /{expected}")
    return results


def main() -> int:
    checks = []
    checks.extend(verify_text())
    checks.extend(verify_sync_helper())
    checks.extend(verify_routes())
    print("END-SESSION OPERATOR CORE VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
