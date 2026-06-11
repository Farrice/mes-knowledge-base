#!/usr/bin/env python3
"""Regression checks for the Deep Research OS command package."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import command_menu  # type: ignore  # noqa: E402
import routing_governor  # type: ignore  # noqa: E402
import workflow_router  # type: ignore  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: str) -> str:
    full = ROOT / path
    require(full.exists(), f"missing file: {path}")
    return full.read_text(encoding="utf-8", errors="ignore")


def names_from_menu(query: str) -> list[str]:
    return [workflow.name for _, workflow in command_menu.search(command_menu.build_index(), query, 8)]


def names_from_workflow_router(query: str) -> list[str]:
    return [workflow["name"] for _, workflow in workflow_router.search_workflows(query, 8)]


def main() -> int:
    workflow = read(".agent/workflows/deep-research-os.md")
    source_command = read(".claude/commands/deep-research-os.md")
    skill = read(".agents/cold-skills/source-command-wrappers/source-command-deep-research-os/SKILL.md")
    guide = read("_active/deep-research-os/00-start-here/deep-research-os-user-guide.md")
    plugin = read("plugins/antigravity-operator-core/skills/antigravity-operator-core/SKILL.md")

    required_terms = (
        "Deep Research OS Trace",
        "source ledger",
        "Social Listening",
        "Anti-Hallucination Gate",
        "Wide Decomposition",
        "real Codex subagents",
        "python3 execution/research_quality_gate.py",
        "python3 execution/research_router.py --health",
    )
    for term in required_terms:
        require(term in workflow, f"workflow missing required term: {term}")

    require(".agent/workflows/deep-research-os.md" in source_command, "source command does not bridge to workflow")
    require("intentionally cold-quarantined" in skill, "cold wrapper must explain hot-surface boundary")
    require("/virtuoso --mode research" in guide, "guide must teach preferred hot entrypoint")
    require("deep-research-os" in plugin, "operator-core plugin must mention deep-research-os")

    query = "deep research social listening market intelligence anti hallucination"
    menu = names_from_menu(query)
    router = names_from_workflow_router(query)
    require(menu and menu[0] == "deep-research-os", f"command_menu should rank deep-research-os first, got {menu[:5]}")
    require(router and router[0] == "deep-research-os", f"workflow_router should rank deep-research-os first, got {router[:5]}")

    decision = routing_governor.evaluate(query, menu, router)
    require(decision.detected_lane == "deep-research-os", f"governor lane mismatch: {decision.detected_lane}")
    require(decision.chosen_route == "deep-research-os", f"governor route mismatch: {decision.chosen_route}")
    require("deep-research-os" in decision.required_candidates, "governor stack missing deep-research-os")

    hot_skill = ROOT / ".agents" / "skills" / "source-command-deep-research-os" / "SKILL.md"
    cold_skill = ROOT / ".agents" / "cold-skills" / "source-command-wrappers" / "source-command-deep-research-os" / "SKILL.md"
    require(not hot_skill.exists(), "deep-research-os should not be hot in v1")
    require(cold_skill.exists(), "deep-research-os cold wrapper missing")

    print("Deep Research OS verification: PASS")
    print("- workflow, source command, cold wrapper, and user guide exist")
    print("- command_menu and workflow_router rank /deep-research-os first for research OS intent")
    print("- routing governor detects the deep-research-os lane")
    print("- hot surface remains clean; wrapper is cold-quarantined")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
