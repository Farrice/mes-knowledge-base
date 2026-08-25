#!/usr/bin/env python3
"""Deterministic cold-start and bridge checks for the universal Oren front door."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
ROUTE_MAP = ROOT / "agents/oren-taste-development/references/universal-route-map.json"
FIXTURES = PACKAGE / "oren-front-door-validation-fixtures.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def route(query: str, route_map: dict) -> str:
    """Return the cold-start route using external-owner vetoes, then signal coverage."""
    normalized = query.casefold()
    external_scores = {
        item["id"]: sum(signal.casefold() in normalized for signal in item["signals"])
        for item in route_map["external_handoffs"]
    }
    external_winner = max(external_scores, key=external_scores.get)
    if external_scores[external_winner] > 0:
        return external_winner

    scores = {
        item["id"]: sum(signal.casefold() in normalized for signal in item["signals"])
        for item in route_map["routes"]
    }
    winner = max(scores, key=scores.get)
    if scores[winner] == 0:
        raise ValueError(f"no route signal for: {query}")
    return winner


def check_static_contract(route_map: dict) -> list[str]:
    failures: list[str] = []
    expected_ids = {
        "taste", "luxury", "repositioning", "operations", "one_person_ai_marketer",
        "identity", "archetype", "content_team", "ad_psychology", "world_building", "slop_era",
    }
    actual_ids = {item["id"] for item in route_map["routes"]}
    if actual_ids != expected_ids:
        failures.append(f"route inventory mismatch: {sorted(actual_ids ^ expected_ids)}")

    policy = route_map["policy"]
    if policy != {
        "primary_skill_limit": 1,
        "support_skill_limit": 1,
        "bulk_load_forbidden": True,
        "route_on_purchased_job": True,
    }:
        failures.append("route policy drifted from one-owner thin-conductor contract")

    for item in route_map["routes"]:
        target = ROOT / item["front_door"]
        if not target.is_file():
            failures.append(f"missing front door for {item['id']}: {item['front_door']}")
        for required in ("skill", "signals", "boundary"):
            if not item.get(required):
                failures.append(f"{item['id']} missing {required}")

    required_files = {
        ".agent/workflows/oren.md": ["Never bulk-load all Oren skills", "exactly **one primary Oren skill**", "Oren Route Card"],
        ".agent/workflows/oren-one.md": ["do not default every request to the weekly OS", "oren-funnel-flywheel.md"],
        ".claude/commands/oren.md": [".agent/workflows/oren.md"],
        ".agents/skills/source-command-oren/SKILL.md": [".agent/workflows/oren.md", "Do not reproduce its route table"],
    }
    for relative, needles in required_files.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing bridge: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{relative} missing contract text: {needle}")
    return failures


def main() -> int:
    route_map = load_json(ROUTE_MAP)
    fixtures = load_json(FIXTURES)
    failures = check_static_contract(route_map)
    checks = 0
    for group in ("positive", "negative"):
        for fixture in fixtures[group]:
            checks += 1
            try:
                actual = route(fixture["query"], route_map)
            except ValueError as exc:
                failures.append(f"{fixture['id']}: {exc}")
                continue
            if actual != fixture["expected"]:
                failures.append(f"{fixture['id']}: expected {fixture['expected']}, got {actual}")

    if failures:
        print(f"FAIL: Oren front door ({len(failures)} failure(s), {checks} fixtures)")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"PASS: Oren front door ({checks} cold-start fixtures; 11 packages; 2 hot bridges)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
