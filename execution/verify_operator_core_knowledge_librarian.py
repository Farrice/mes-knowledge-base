#!/usr/bin/env python3
"""Verify Knowledge-librarian Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "knowledge-librarian.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-knowledge-librarian" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_KNOWLEDGE_LIBRARIAN = Path.home() / ".codex" / "skills" / "knowledge-librarian" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-knowledge-librarian" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Knowledge-librarian behavior",
        "compact session-start knowledge pulse by default",
        "python3 execution/knowledge_compiler.py stats",
        'python3 execution/knowledge_compiler.py solutions "[focus]" --top 8 --stdout',
        "Read `knowledge/compiled/briefing.md` if it exists",
        "do not generate or refresh the briefing by default",
        "Do not write `.agent/knowledge-librarian-state.md`, refresh compiled knowledge, create solution docs, mutate Mission, perform cleanup, or mirror global files unless explicitly requested",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/knowledge-librarian.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "compact session-start knowledge pulse",
        "read-only default scans",
        "knowledge_compiler.py stats",
        "knowledge_compiler.py solutions",
        "--stdout",
        "existing compiled briefing",
        "local evidence",
        "no state snapshot",
        "Mission mutation",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Knowledge-librarian Pulse",
        "/Users/farricecain/Google Antigravity/.agent/workflows/knowledge-librarian.md",
        "thin compatibility wrappers",
        "compact session-start knowledge pulse",
        "read-only default scans",
        "knowledge_compiler.py stats",
        "knowledge_compiler.py solutions",
        "--stdout",
        "state snapshot",
        "Mission",
        "Codex subagents without explicit authorization",
    ],
    GLOBAL_KNOWLEDGE_LIBRARIAN: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/knowledge-librarian.md",
        "thin compatibility wrapper",
        "compact session-start knowledge pulse",
        "read-only default scans",
        "knowledge_compiler.py stats",
        "knowledge_compiler.py solutions",
        "--stdout",
        "existing compiled briefing",
        "local evidence",
        "no state snapshot",
        "Mission mutation",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/knowledge-librarian/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/knowledge-librarian.md",
        "thin compatibility wrapper",
        "compact session-start knowledge pulse",
        "read-only default scans",
        "knowledge_compiler.py stats",
        "knowledge_compiler.py solutions",
        "--stdout",
        "existing compiled briefing",
        "local evidence",
        "no state snapshot",
        "Mission mutation",
        "real Codex subagents require explicit",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "python execution/knowledge_compiler.py",
    "After producing the Library Pulse, update `.agent/knowledge-librarian-state.md`",
    "write state by default",
    "refresh compiled knowledge by default",
    "create solution docs by default",
    "mutate Mission by default",
    "repair Mission by default",
)

ROUTING_CASES = (
    ("source-command-knowledge-librarian session start pulse", "knowledge-librarian", "knowledge-librarian-pulse"),
    ("knowledge librarian underused workflows", "knowledge-librarian", "knowledge-librarian-pulse"),
    ("find reusable solution docs for this objective", "knowledge-librarian", "knowledge-librarian-pulse"),
    ("audit knowledge-librarian operator core drift", "system-audit", "system-failure"),
    ("the knowledge library routing is broken", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Knowledge-librarian text in {path}: {snippet}")
        results.append(f"knowledge-librarian contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_knowledge_librarian.py", "--check"])
    return ["knowledge-librarian sync helper passes"]


def verify_stdout_mode() -> list[str]:
    target = ROOT / "knowledge" / "compiled" / "solution-matches.md"
    before = target.read_text(encoding="utf-8", errors="ignore") if target.exists() else None
    run([sys.executable, "execution/knowledge_compiler.py", "solutions", "operator core", "--top", "1", "--stdout"])
    after = target.read_text(encoding="utf-8", errors="ignore") if target.exists() else None
    if before != after:
        raise AssertionError("knowledge_compiler.py solutions --stdout changed solution-matches.md")
    return ["knowledge compiler solutions --stdout creates no files"]


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
    results.extend(verify_stdout_mode())
    results.extend(verify_routes())
    print("KNOWLEDGE-LIBRARIAN OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
