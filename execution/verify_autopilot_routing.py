#!/usr/bin/env python3
"""Regression checks for Autopilot routing and intent-to-outcome behavior."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

SYSTEM_QUERY = "autopilot notion routing orchestration skill selection triage menu self improving monitoring"
MISSION_QUERY = "mission mode long running multi milestone client system build handoffs validation contract"
REVENUE_QUERY = "make income with our system side project cash first revenue client acquisition 48 hour"
SKILL_SYSTEM_QUERY = "make skills make sense 10x better turn this video into a reusable skill system improve Codex orchestration"
REPEATABILITY_QUERY = "the revision got worse and lost the good part"
FRONT_DOOR_CHOICE_QUERIES = [
    "I have too many tools and don't know what to use",
    "what should I use next?",
    "co creative launching pad intent alignment apex before build raw intent",
]
LAUNCHPAD_SOURCE_SYSTEM_QUERY = "turn this video source into a co-creative launchpad OS for the harness"
MENU_BACKEND_QUERY = "show me the menu of options"
RESEARCH_STACK_QUERY = "Research the current market for AI lead generation tools with live sources"

CRITICAL_ROUTES = ["autopilot", "source-to-skill-system", "orchestrate", "routing-intelligence", "self-evolve", "skill-anneal"]
REPEATABILITY_ROUTES = ["repeatability-spine", "autopilot", "system-audit", "publishable-copy-gate", "self-evolve", "skill-anneal"]
MISSION_ROUTES = ["mission", "autopilot", "orchestrate"]
REVENUE_ROUTES = ["first-10k", "revenue-offer-agent", "client-acquire", "zero-to-client-sprint", "service-first-productization"]
SKILL_SYSTEM_ROUTES = ["source-to-skill-system", "extraction-governor-agent", "mission", "autopilot", "self-evolve", "skill-anneal"]
FRONT_DOOR_CHOICE_ROUTES = ["autopilot", "orchestrate", "routing-intelligence", "knowledge-librarian", "mission"]
MENU_BACKEND_ROUTES = ["orchestrate", "autopilot"]
RESEARCH_STACK_ROUTES = [
    "deep-research-os",
    "research-intelligence-agent",
    "deep-research",
    "ground-truth",
    "adversarial-review",
]
RETIRED_RESEARCH_ROUTES = {"research-swarm", "parallel-research", "deep-research-gemini"}


def run(args: list[str], env: dict[str, str] | None = None) -> str:
    run_env = os.environ.copy()
    if env:
        run_env.update(env)
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=run_env,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def parse_command_menu(output: str) -> list[str]:
    routes = []
    for line in output.splitlines():
        line = line.strip()
        if not line or not line[0].isdigit() or "`/" not in line:
            continue
        routes.append(line.split("`/", 1)[1].split("`", 1)[0])
    return routes


def parse_workflow_router(output: str) -> list[str]:
    routes = []
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            routes.append(stripped[1:].split(None, 1)[0])
    return routes


def assert_first(routes: list[str], expected: set[str], label: str) -> None:
    if not routes:
        raise AssertionError(f"{label} returned no routes")
    if routes[0] not in expected:
        raise AssertionError(f"{label} expected first route in {sorted(expected)}, got /{routes[0]}")


def assert_contains(routes: list[str], expected: list[str], label: str) -> None:
    missing = [route for route in expected if route not in routes]
    if missing:
        raise AssertionError(f"{label} missing routes: {', '.join(missing)}")


def check_route_pair(query: str, expected_first: set[str], expected_routes: list[str], label: str) -> None:
    menu = parse_command_menu(run([sys.executable, "execution/command_menu.py", "search", query]))
    router = parse_workflow_router(run([sys.executable, "execution/workflow_router.py", "search", query]))
    assert_first(menu, expected_first, f"command_menu {label}")
    assert_first(router, expected_first, f"workflow_router {label}")
    assert_contains(menu, expected_routes, f"command_menu {label}")
    assert_contains(router, expected_routes, f"workflow_router {label}")


def check_routing() -> None:
    check_route_pair(SYSTEM_QUERY, {"autopilot"}, CRITICAL_ROUTES, "system")
    check_route_pair(MISSION_QUERY, {"mission"}, MISSION_ROUTES, "mission")
    check_route_pair(REVENUE_QUERY, {"first-10k", "revenue-offer-agent"}, REVENUE_ROUTES, "revenue")
    check_route_pair(SKILL_SYSTEM_QUERY, {"source-to-skill-system"}, SKILL_SYSTEM_ROUTES, "skill-system")
    check_route_pair(LAUNCHPAD_SOURCE_SYSTEM_QUERY, {"source-to-skill-system"}, SKILL_SYSTEM_ROUTES, "launchpad-source-system")
    check_route_pair(REPEATABILITY_QUERY, {"repeatability-spine"}, REPEATABILITY_ROUTES, "repeatability")
    for query in FRONT_DOOR_CHOICE_QUERIES:
        check_route_pair(query, {"autopilot"}, FRONT_DOOR_CHOICE_ROUTES, f"front-door-choice: {query}")
    check_route_pair(MENU_BACKEND_QUERY, {"orchestrate"}, MENU_BACKEND_ROUTES, "menu-backend")


def check_research_stack_routing() -> None:
    menu = parse_command_menu(run([sys.executable, "execution/command_menu.py", "search", RESEARCH_STACK_QUERY]))
    router = parse_workflow_router(run([sys.executable, "execution/workflow_router.py", "search", RESEARCH_STACK_QUERY]))
    assert_contains(menu, RESEARCH_STACK_ROUTES, "command_menu research stack")
    assert_contains(router, RESEARCH_STACK_ROUTES, "workflow_router research stack")
    leaked = RETIRED_RESEARCH_ROUTES & (set(menu) | set(router))
    if leaked:
        raise AssertionError(f"retired paid/delegated research routes leaked into Free-First stack: {sorted(leaked)}")


def check_routing_governor() -> None:
    cases = [
        (REVENUE_QUERY, ["**Detected lane**: revenue", "**Chosen route**: /first-10k"]),
        (SKILL_SYSTEM_QUERY, ["**Detected lane**: skill-system", "**Chosen route**: /source-to-skill-system"]),
        (LAUNCHPAD_SOURCE_SYSTEM_QUERY, ["**Detected lane**: skill-system", "**Chosen route**: /source-to-skill-system"]),
        (REPEATABILITY_QUERY, ["**Detected lane**: repeatability", "**Chosen route**: /repeatability-spine"]),
        (MENU_BACKEND_QUERY, ["**Detected lane**: menu-backend", "**Chosen route**: /orchestrate"]),
    ]
    for query, required in cases:
        output = run([sys.executable, "execution/routing_governor.py", "evaluate", query])
        missing = [item for item in required if item not in output]
        if missing:
            raise AssertionError(f"Routing governor missing {missing} for {query}:\n{output}")


def check_misroute_feedback() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        data_file = str(Path(tmpdir) / "routing-intelligence.json")
        env = {"ANTIGRAVITY_ROUTING_DATA_FILE": data_file}
        run([
            sys.executable,
            "execution/routing_intelligence.py",
            "misroute",
            "--request",
            REVENUE_QUERY,
            "--wrong",
            "fourth-wall-client-experience",
            "--correct",
            "first-10k",
            "--notes",
            "revenue routing regression test",
        ], env=env)
        scoreboard = run([sys.executable, "execution/routing_intelligence.py", "scoreboard"], env=env)
    required = ["| Total Feedback | 1 |", "| Negative | 1 |", "fourth-wall-client-experience", "first-10k", "Routing fix queued"]
    missing = [item for item in required if item not in scoreboard]
    if missing:
        raise AssertionError(f"Misroute feedback scoreboard missing: {', '.join(missing)}\n{scoreboard}")


def check_autopilot_contract() -> None:
    workflow = (ROOT / ".agent" / "workflows" / "autopilot.md").read_text(encoding="utf-8")
    required = [
        "Intent-To-Outcome",
        "Co-Creative Launchpad",
        "Execution Decision",
        "Running now",
        "Needs judgment",
        "Blocked by risk",
        "Blocked by configuration",
        "Plan only",
        "Run Prompt",
        "Run Receipt",
        "Friction Ledger",
        "Capability Graph",
        "Outcome Recipes",
        "Plugin Packaging Ladder",
        "safe workspace-local execution",
    ]
    missing = [item for item in required if item not in workflow]
    if missing:
        raise AssertionError("Autopilot intent-to-outcome contract missing: " + ", ".join(missing))
    forbidden = ["Autopilot pauses every time", "**Execution not performed**", "Waiting for explicit approval before execution."]
    hits = [item for item in forbidden if item in workflow]
    if hits:
        raise AssertionError("Autopilot still contains old always-pause terms: " + ", ".join(hits))


def check_runtime_preflight() -> None:
    output = run([sys.executable, "execution/verify_autopilot_runtime_preflight.py"])
    required = [
        "Autopilot intent-to-outcome runtime verification: PASS",
        "safe-local-run: route=/autopilot, lane=general, status=Running now",
        "plan-mode-pauses: route=/autopilot, lane=general, status=Plan only",
        "publish-risk-blocks: route=/autopilot, lane=general, status=Blocked by risk",
        "plugin-packaging: route=/plugin-readiness-audit, lane=plugin-packaging, status=Running now",
        "current-market-research-free-first: route=/deep-research-os, lane=deep-research-os, status=Running now",
        "negative-control: nonexistent route and verifier cannot inherit Running now",
    ]
    missing = [item for item in required if item not in output]
    if missing:
        raise AssertionError("Runtime preflight verifier missing proof: " + ", ".join(missing) + "\n" + output)


def check_helpers() -> None:
    run([sys.executable, "execution/capability_graph.py", "--json"])
    run([sys.executable, "execution/outcome_recipes.py", "autopilot package this as plugin", "--json"])
    run([sys.executable, "execution/friction_ledger.py", "verify"])
    run([sys.executable, "execution/run_receipt.py", "--verify"])


def check_bridge_policy() -> None:
    workflows = {path.stem for path in (ROOT / ".agent" / "workflows").glob("*.md")}
    codex_skills = {
        path.parent.name.removeprefix("source-command-")
        for path in (ROOT / ".agents" / "skills").glob("source-command-*/SKILL.md")
    }
    for command in ("autopilot", "orchestrate", "mission", "repeatability-spine"):
        if command not in workflows or command not in codex_skills:
            raise AssertionError(f"/{command} must exist as workflow and Codex source-command skill")


def main() -> int:
    checks = [
        ("routing order", check_routing),
        ("research stack routing", check_research_stack_routing),
        ("routing governor evaluation", check_routing_governor),
        ("misroute feedback capture", check_misroute_feedback),
        ("Autopilot intent-to-outcome contract", check_autopilot_contract),
        ("Autopilot runtime preflight", check_runtime_preflight),
        ("intent-to-outcome helpers", check_helpers),
        ("Claude/Codex bridge policy", check_bridge_policy),
    ]
    for label, check in checks:
        check()
        print(f"ok: {label}")
    print("Autopilot routing regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
