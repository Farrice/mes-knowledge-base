#!/usr/bin/env python3
"""Verify Extraction-governor-agent Operator Core source truth and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "extraction-governor-agent.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_EXTRACTION = Path.home() / ".codex" / "skills" / "extraction-governor-agent" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/extraction-governor-agent.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Extraction-governor-agent behavior",
        "owns source-to-capability triage and routing, not isolated summarization or collection",
        "Default mode is read-only triage",
        "Preserve source grounding before synthesis",
        "Run existing-route and duplicate-system checks before recommending a new skill, workflow, agent, command bridge, or knowledge artifact",
        "Do not write `.agent/extraction-governor-agent-state.md`, create artifacts, promote hot skills, mirror global files, use paid/quota-heavy tools, fetch external sources, or mutate workflows unless explicitly requested and validated",
        "Hand off connected skill-system or orchestration builds to `/source-to-skill-system`",
        "overlap or prior-decision questions to `/knowledge-librarian`",
        "travel/plugin packaging decisions to `/plugin-readiness-audit`",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/extraction-governor-agent.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "source-to-capability triage",
        "read-only triage",
        "source grounding before synthesis",
        "existing-route and duplicate-system checks",
        "no state writes",
        "hot skill promotion",
        "global mirrors",
        "paid/quota-heavy tools",
        "external source fetches",
        "workflow mutation",
        "/source-to-skill-system",
        "/knowledge-librarian",
        "/plugin-readiness-audit",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Extraction-governor-agent Source Triage",
        CANONICAL_PATH,
        "thin compatibility wrappers",
        "source-to-capability triage",
        "read-only triage",
        "source grounding before synthesis",
        "existing-route and duplicate-system checks",
        "no state writes",
        "hot skill promotion",
        "global mirrors",
        "paid/quota-heavy tools",
        "external source fetches",
        "/source-to-skill-system",
        "/knowledge-librarian",
        "/plugin-readiness-audit",
        "Codex subagents require explicit authorization",
    ],
    GLOBAL_EXTRACTION: [
        "Project Source Of Truth",
        CANONICAL_PATH,
        "thin compatibility wrapper",
        "source-to-capability triage",
        "read-only triage",
        "source grounding before synthesis",
        "existing-route and duplicate-system checks",
        "no state writes",
        "hot skill promotion",
        "global mirrors",
        "paid/quota-heavy tools",
        "external source fetches",
        "workflow mutation",
        "/source-to-skill-system",
        "/knowledge-librarian",
        "/plugin-readiness-audit",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/extraction-governor-agent/SKILL.md",
        CANONICAL_PATH,
        "thin compatibility wrapper",
        "source-to-capability triage",
        "read-only triage",
        "source grounding before synthesis",
        "existing-route and duplicate-system checks",
        "no state writes",
        "hot skill promotion",
        "global mirrors",
        "paid/quota-heavy tools",
        "external source fetches",
        "workflow mutation",
        "/source-to-skill-system",
        "/knowledge-librarian",
        "/plugin-readiness-audit",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "knowledge_compiler.py briefing",
    "automatically update lightweight state",
    "automatically write state",
    "create artifacts by default",
    "promote hot skills by default",
    "global mirror by default",
    "external source fetch by default",
    "paid tool by default",
    "workflow mutation by default",
    "spawn subagents by default",
)

ROUTING_CASES = (
    ("source-command-extraction-governor-agent route this source into reusable capability", "extraction-governor-agent", "extraction-governance"),
    ("extraction governor hidden mechanics duplicate-system avoidance", "extraction-governor-agent", "extraction-governance"),
    ("classify build shape for this source without creating artifacts", "extraction-governor-agent", "extraction-governance"),
    ("turn this video into a connected codex skill system", "source-to-skill-system", "skill-system"),
    ("audit extraction-governor-agent operator core drift", "system-audit", "system-failure"),
    ("extraction-governor-agent is broken and writes state automatically", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Extraction-governor-agent text in {path}: {snippet}")
        results.append(f"extraction-governor-agent contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_extraction_governor_agent.py", "--check"])
    return ["extraction-governor-agent sync helper passes"]


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
    results.extend(verify_routes())
    print("EXTRACTION-GOVERNOR-AGENT OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
