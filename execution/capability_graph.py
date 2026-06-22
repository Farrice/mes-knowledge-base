#!/usr/bin/env python3
"""Live capability graph for the Antigravity harness."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"
sys.path.insert(0, str(EXECUTION))

import command_menu  # type: ignore  # noqa: E402
import plugin_readiness_audit  # type: ignore  # noqa: E402
from outcome_recipes import RECIPES, OutcomeRecipe, as_jsonable  # noqa: E402


def _exists(path: Path) -> bool:
    return path.exists()


def route_status(route: str) -> dict[str, Any]:
    workflow = ROOT / ".agent" / "workflows" / f"{route}.md"
    skill = ROOT / ".agents" / "skills" / f"source-command-{route}" / "SKILL.md"
    cold_skill = ROOT / ".agents" / "cold-skills" / "source-command-wrappers" / f"source-command-{route}" / "SKILL.md"
    command = ROOT / ".claude" / "commands" / f"{route}.md"
    route_counts = plugin_readiness_audit.routing_counts()
    score = plugin_readiness_audit.score_candidate(route, route_counts)

    if _exists(skill):
        classification = "Use Now"
    elif score.total >= 80:
        classification = "Package Later"
    elif _exists(workflow):
        classification = "Harden"
    elif _exists(cold_skill) or _exists(command):
        classification = "Cold Reference"
    else:
        classification = "Archive Candidate"

    return {
        "route": route,
        "workflow": _exists(workflow),
        "hot_skill": _exists(skill),
        "cold_skill": _exists(cold_skill),
        "legacy_command": _exists(command),
        "plugin_score": score.total,
        "plugin_decision": score.decision,
        "classification": classification,
    }


def recipe_entry(recipe: OutcomeRecipe) -> dict[str, Any]:
    entry = as_jsonable(recipe)
    routes = [recipe.primary_route, *recipe.support_gates]
    seen: set[str] = set()
    entry["routes"] = []
    for route in routes:
        if route in seen:
            continue
        seen.add(route)
        entry["routes"].append(route_status(route))
    return entry


def build_graph() -> dict[str, Any]:
    workflows = command_menu.build_index()
    return {
        "summary": {
            "workflow_count": len(workflows),
            "recipe_count": len(RECIPES),
            "policy": "Use routes through outcome recipes first; package only after readiness proof.",
        },
        "recipes": {name: recipe_entry(recipe) for name, recipe in RECIPES.items()},
    }


def render_markdown(graph: dict[str, Any]) -> str:
    lines = [
        "# Antigravity Capability Graph",
        "",
        f"Workflows indexed: {graph['summary']['workflow_count']}",
        f"Outcome recipes: {graph['summary']['recipe_count']}",
        "",
        "| Outcome | Primary Route | Gates | Artifact | Packaging |",
        "|---|---|---|---|---|",
    ]
    for name, recipe in graph["recipes"].items():
        gates = ", ".join(f"/{route['route']}" for route in recipe["routes"][1:])
        lines.append(
            f"| {name} | /{recipe['primary_route']} | {gates or 'none'} | "
            f"{recipe['artifact']} | {recipe['plugin_ladder']} |"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the live Antigravity capability graph.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    graph = build_graph()
    if args.json:
        print(json.dumps(graph, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(graph))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
