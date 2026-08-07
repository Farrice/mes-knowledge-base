#!/usr/bin/env python3
"""Verify Source-to-skill-system Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "source-to-skill-system.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-source-to-skill-system" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SOURCE_TO_SKILL = Path.home() / ".codex" / "skills" / "source-to-skill-system" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-source-to-skill-system" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Source-to-skill-system behavior",
        "turns source material into connected skill systems, not isolated mega-skills",
        "Evidence and existing-route fit come before building",
        "Every build needs the Skill System Contract fields before implementation",
        "Agentic engineering changes require the Agentic Engineering Packet",
        "Self-improvement, maintenance, cleanup, or evolution changes require a Goal Packet",
        "Prefer companion OS layers over duplicate expert skills",
        "Do not create hot skills, global mirrors, external writes, new dependencies, or broad workflow mutations without explicit approval and validation",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/source-to-skill-system.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "connected skill systems",
        "not isolated mega-skills",
        "evidence and existing-route fit",
        "Skill System Contract",
        "Agentic Engineering Packet",
        "Goal Packet",
        "companion OS layers",
        "no hot skill promotion",
        "global mirror",
        "external write",
        "new dependency",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Source-to-skill-system Builder",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/source-to-skill-system.md",
        "thin compatibility wrappers",
        "connected skill systems",
        "not isolated mega-skills",
        "evidence and existing-route fit",
        "Skill System Contract",
        "Agentic Engineering Packet",
        "Goal Packet",
        "companion OS layers",
        "global mirrors",
        "external writes",
        "new dependencies",
        "Codex subagents require explicit authorization",
    ],
    GLOBAL_SOURCE_TO_SKILL: [
        "Project Source Of Truth",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/source-to-skill-system.md",
        "thin compatibility wrapper",
        "connected skill systems",
        "not isolated mega-skills",
        "evidence and existing-route fit",
        "Skill System Contract",
        "Agentic Engineering Packet",
        "Goal Packet",
        "companion OS layers",
        "no hot skill promotion",
        "global mirror",
        "external write",
        "new dependency",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/source-to-skill-system/SKILL.md",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/source-to-skill-system.md",
        "thin compatibility wrapper",
        "connected skill systems",
        "not isolated mega-skills",
        "evidence and existing-route fit",
        "Skill System Contract",
        "Agentic Engineering Packet",
        "Goal Packet",
        "companion OS layers",
        "no hot skill promotion",
        "global mirror",
        "external write",
        "new dependency",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "giant all-purpose skill by default",
    "isolated mega-skill by default",
    "skip source grounding",
    "create hot skills by default",
    "global mirror by default",
    "external write by default",
    "new dependency by default",
    "broad workflow mutation by default",
)

ROUTING_CASES = (
    ("source-command-source-to-skill-system turn this source into a skill system", "source-to-skill-system", "skill-system"),
    ("turn this video into a connected codex skill system", "source-to-skill-system", "skill-system"),
    ("build a companion OS layer from this transcript", "source-to-skill-system", "skill-system"),
    ("audit source-to-skill-system operator core drift", "system-audit", "system-failure"),
    ("source-to-skill-system is broken and creates bloat", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Source-to-skill-system text in {path}: {snippet}")
        results.append(f"source-to-skill-system contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_source_to_skill_system.py", "--check"])
    return ["source-to-skill-system sync helper passes"]


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
    run([sys.executable, "execution/verify_skill_system_contract.py"])
    results.append("skill-system contract verifier passes")
    print("SOURCE-TO-SKILL-SYSTEM OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
