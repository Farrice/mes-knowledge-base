#!/usr/bin/env python3
"""Render contextual next prompts for Antigravity closeouts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def existing(paths: list[str]) -> list[str]:
    return [path for path in paths if (ROOT / path).exists()]


def compact(value: Any, fallback: str = "") -> str:
    if value is None:
        return fallback
    if isinstance(value, str):
        return value.strip() or fallback
    return str(value).strip() or fallback


def state_context(objective: str) -> dict[str, Any]:
    intent = read_json(ROOT / ".agent" / "intent-memory" / "current.json")
    cohesion = read_json(ROOT / ".agent" / "system-cohesion-state.json")
    receipt = read_json(ROOT / ".agent" / "run-receipts" / "latest.json")

    inferred_objective = (
        objective
        or compact(intent.get("goal"))
        or compact(receipt.get("query"))
        or "continue the current Codex Antigravity work"
    )
    route = compact(intent.get("chosen_route") or cohesion.get("route") or receipt.get("route"), "autopilot")
    lowered_objective = inferred_objective.lower()
    if any(term in lowered_objective for term in ("steering", "next prompt", "next prompts", "operator lesson")):
        route = "steering-compass"
    elif "handoff" in lowered_objective and any(
        term in lowered_objective for term in ("agent", "session", "conversation", "branch", "transfer")
    ):
        route = "handoff"
    next_action = compact(intent.get("next_move") or cohesion.get("next_move") or receipt.get("next_action"))
    context_paths = existing(
        [
            ".agent/intent-memory/current.json",
            ".agent/system-cohesion-state.json",
            ".agent/run-receipts/latest.md",
            ".agent/session-state.md",
            "CODEX.md",
        ]
    )
    return {
        "objective": inferred_objective,
        "route": route.lstrip("/"),
        "next_action": next_action,
        "context_paths": context_paths,
    }


def prompt_text(route: str, objective: str, instruction: str, context_paths: list[str]) -> str:
    context_clause = ""
    if context_paths:
        context_clause = " Load these context anchors first: " + ", ".join(context_paths[:4]) + "."
    return f"/{route} {instruction} Objective: {objective}.{context_clause}"


def unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        clean = value.strip().lstrip("/")
        if not clean or clean in seen:
            continue
        seen.add(clean)
        result.append(clean)
    return result


def build_prompts(objective: str = "", stage: str = "closeout") -> dict[str, Any]:
    state = state_context(objective)
    obj = state["objective"]
    route = state["route"]
    context_paths = state["context_paths"]

    prompts = [
        {
            "name": "Use Now",
            "route": route if route not in {"", "unknown"} else "autopilot",
            "suggested_skills": unique([route if route else "autopilot", "steering-compass"]),
            "when_to_use": "Use when the next move is execution and the current direction is already good enough.",
            "why": "This converts session momentum into the next concrete artifact instead of another meta-discussion.",
            "prompt": prompt_text(
                route if route not in {"", "unknown"} else "autopilot",
                obj,
                "continue the strongest next step from the current work; keep scope tight, verify the result, and end with 3 Next Prompts.",
                context_paths,
            ),
            "expected_output": "One concrete next artifact or patch plus verification.",
            "quality_bar": "A future session can see what changed, what passed, and what to do next without reconstructing context.",
            "skip_if": "Skip if the direction still needs a taste, risk, or scope decision.",
        },
        {
            "name": "Harden",
            "route": "system-audit",
            "suggested_skills": ["system-audit", "health-check", "routing-intelligence"],
            "when_to_use": "Use when the output is promising but trust, routing, or repeatability still feels fragile.",
            "why": "This turns doubt into proof: route checks, stale-state checks, regression cases, and a clear repair target.",
            "prompt": prompt_text(
                "system-audit",
                obj,
                "audit the current result for routing drift, missing proof, stale state, and repeatability risk; patch only the highest-leverage local issue and verify it.",
                context_paths,
            ),
            "expected_output": "A narrow audit verdict, patched gap if safe, verifier output, and a run receipt.",
            "quality_bar": "The audit names working/stale/broken surfaces and leaves no vague 'probably works' claims.",
            "skip_if": "Skip if this was a tiny answer or no durable behavior changed.",
        },
        {
            "name": "Expand",
            "route": "source-to-skill-system",
            "suggested_skills": ["source-to-skill-system", "extraction-governor-agent", "knowledge-librarian"],
            "when_to_use": "Use when the session revealed a reusable method, source, workflow, or command pattern.",
            "why": "This captures the hidden mechanic so the harness improves instead of the insight dying in one conversation.",
            "prompt": prompt_text(
                "source-to-skill-system",
                obj,
                "extract the reusable mechanic from this session, decide whether it should become a primitive, workflow, skill, reference, or cold route, then build the smallest durable surface with validation.",
                context_paths,
            ),
            "expected_output": "A source-grounded capability contract, smallest durable implementation, and cold-start proof.",
            "quality_bar": "The new surface extends existing routes, avoids duplicate mega-systems, and has a verifier.",
            "skip_if": "Skip if the value is one-off execution rather than a repeatable operating pattern.",
        },
    ]
    return {
        "stage": stage,
        "objective": obj,
        "context_paths": context_paths,
        "prompts": prompts,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = ["## 3 Next Prompts", ""]
    for idx, item in enumerate(payload["prompts"], 1):
        lines.extend(
            [
                f"{idx}. **{item['name']}**",
                f"   - **When to use:** {item['when_to_use']}",
                f"   - **Why this is recommended:** {item['why']}",
                f"   - **Prompt:** `{item['prompt']}`",
                f"   - **Expected output:** {item['expected_output']}",
                f"   - **Quality bar:** {item['quality_bar']}",
                f"   - **Skip if:** {item['skip_if']}",
                f"   - **Suggested skills/workflows:** {', '.join('/' + skill.lstrip('/') for skill in item['suggested_skills'])}",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render contextual next prompts.")
    parser.add_argument("--objective", default="", help="Override the inferred session objective.")
    parser.add_argument("--stage", default="closeout", help="Session stage label.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    args = parser.parse_args()

    payload = build_prompts(objective=args.objective, stage=args.stage)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(render_markdown(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
