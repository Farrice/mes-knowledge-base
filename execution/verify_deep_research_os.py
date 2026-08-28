#!/usr/bin/env python3
"""Regression checks for the Deep Research OS command package."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import command_menu  # type: ignore  # noqa: E402
import routing_enforcer  # type: ignore  # noqa: E402
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
    skill = read(".agents/skills/source-command-deep-research-os/SKILL.md")
    free_first_contract = read(
        "semantic_libraries/antigravity/primitives/free-first-research-mission-contract.md"
    )
    free_first_runtime = read("execution/free_first_research.py")
    acquisition_bakeoff = read("execution/deep_research_acquisition_bakeoff.py")
    acquisition_fixture = read(
        "execution/fixtures/research-acquisition-bakeoff/health-performance-30.json"
    )
    read("execution/verify_free_first_research_mission.py")
    legacy_command = read(".claude/commands/deep-research.md")
    legacy_skill = read(".agents/skills/source-command-deep-research/SKILL.md")
    legacy_workflow = read(".agent/workflows/deep-research.md")
    routing_doc = read("directives/routing-bindings.md")

    required_terms = (
        "Deep Research OS Trace",
        "source ledger",
        "Social Listening",
        "Anti-Hallucination Gate",
        "Wide Decomposition",
        "real Codex subagents",
        "python3 execution/research_quality_gate.py",
        "Codex Free-First Default",
        "python3 execution/free_first_research.py plan",
        "live external evidence retrieved in this run",
        "Tavily **Search and Extract**",
        "cost_usd: 0.0",
        "public no-key Jina Reader endpoint",
        "not a new scraper, command, scheduler",
    )
    for term in required_terms:
        require(term in workflow, f"workflow missing required term: {term}")

    require(".agent/workflows/deep-research-os.md" in source_command, "source command does not bridge to workflow")
    require(".agent/workflows/deep-research-os.md" in skill, "skill wrapper does not bridge to workflow")
    require(
        "free-first-research-mission-contract.md" in skill,
        "skill wrapper does not load the free-first companion contract",
    )
    require("Authority Order" in free_first_contract, "free-first authority order missing")
    require("Value Receipt" in free_first_contract, "free-first value receipt missing")
    require("def cmd_tavily" in free_first_runtime, "free-first Tavily Search/Extract leg missing")
    require("def cmd_rss" in free_first_runtime, "free-first RSS leg missing")
    require(
        "Target URL returned error" in acquisition_bakeoff,
        "acquisition bakeoff lacks the Jina wrapper false-green regression",
    )
    require(
        '"name": "health-performance-real-corpus-30"' in acquisition_fixture,
        "30-URL acquisition fixture identity missing",
    )
    require(
        acquisition_fixture.count('"id":') == 30,
        "acquisition fixture must contain exactly 30 URL ids",
    )
    require(
        "execution/research_router.py" not in workflow,
        "workflow still points to nonexistent research_router.py",
    )
    require(
        workflow.index("Codex Free-First Default") < workflow.index("Provider-backed entrypoint"),
        "provider-backed path appears before Codex free-first default",
    )
    require(
        "deep-research-os.md" in legacy_command and "--free-first" in legacy_command,
        "/deep-research command does not alias the free-first owner",
    )
    require(
        "deep-research-os.md" in legacy_skill and "--free-first" in legacy_skill,
        "migrated /deep-research skill does not alias the free-first owner",
    )
    require(
        "Legacy provider-backed escalation only" in legacy_workflow,
        "legacy paid/swarm workflow lacks an explicit escalation boundary",
    )
    require(
        "social_listening_free_first" in routing_doc,
        "routing appendix is missing the free-first social-listening owner",
    )

    query = "current decision grade deep research in Codex with native web Tavily RSS and no paid tools"
    menu = names_from_menu(query)
    router = names_from_workflow_router(query)
    require(menu and menu[0] == "deep-research-os", f"command_menu should rank deep-research-os first, got {menu[:5]}")
    require(router and router[0] == "deep-research-os", f"workflow_router should rank deep-research-os first, got {router[:5]}")

    decision = routing_governor.evaluate(query, menu, router)
    require(decision.detected_lane == "deep-research-os", f"governor lane mismatch: {decision.detected_lane}")
    require(decision.chosen_route == "deep-research-os", f"governor route mismatch: {decision.chosen_route}")
    require("deep-research-os" in decision.required_candidates, "governor stack missing deep-research-os")

    bound = routing_enforcer.check_routing(query, "deep-research-os")
    require(bound["valid"], f"free-first owner failed unified research binding: {bound}")
    legacy = routing_enforcer.check_routing(query, "deep-research")
    require(not legacy["valid"], "generic current research still accepts the legacy paid/swarm route")
    social = routing_enforcer.check_routing(
        "research what is happening in this niche using current social listening",
        "deep-research-os",
    )
    require(social["valid"], f"free-first owner failed social-listening binding: {social}")

    print("Deep Research OS verification: PASS")
    print("- workflow, source command, and skill wrapper exist and bridge correctly")
    print("- Codex current research defaults to the free-first companion contract")
    print("- native web, direct HTTP, no-key Jina, Tavily Search/Extract, RSS, stale-context, and value-receipt boundaries are present")
    print("- 30-URL bakeoff remains an evaluation asset, not a new command or scraper surface")
    print("- command_menu, workflow_router, and mandatory bindings rank /deep-research-os first for ordinary current research")
    print("- /deep-research aliases free-first; its paid/swarm workflow is explicit escalation only")
    print("- routing governor detects the deep-research-os lane")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
