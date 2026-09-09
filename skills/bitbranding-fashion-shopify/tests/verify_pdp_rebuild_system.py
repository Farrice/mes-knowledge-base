#!/usr/bin/env python3
"""Deterministic structural and negative-control verifier for the BitBranding PDP subsystem."""

from __future__ import annotations

import json
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]

REQUIRED_FILES = (
    "workflows/05-fashion-pdp-blueprint.md",
    "workflows/06-claude-pdp-build-loop.md",
    "workflows/07-fashion-pdp-rebuild-system.md",
    "references/prompts-v2/fashion-pdp-blueprint.md",
    "references/prompts-v2/claude-pdp-build-loop.md",
    "references/prompts-v2/fashion-pdp-rebuild-system.md",
    "references/pdp-rebuild-skill-system-contract.md",
)


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        path = SKILL_ROOT / relative
        require(path.is_file() and path.stat().st_size > 0, f"missing or empty: {relative}", failures)

    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    for command in ("/bb-pdp-blueprint", "/bb-pdp-build-loop", "/bb-pdp-rebuild"):
        require(command in skill_text, f"SKILL.md does not expose {command}", failures)

    for prompt_name in (
        "fashion-pdp-blueprint.md",
        "claude-pdp-build-loop.md",
        "fashion-pdp-rebuild-system.md",
    ):
        prompt = (SKILL_ROOT / "references" / "prompts-v2" / prompt_name).read_text(encoding="utf-8")
        for section in ("## Output Contract", "## Output Skeleton", "## Quality Gate"):
            require(section in prompt, f"{prompt_name} lacks {section}", failures)

    build_text = (SKILL_ROOT / "workflows" / "06-claude-pdp-build-loop.md").read_text(encoding="utf-8")
    for boundary in (
        "explicit user authorization",
        "never target the live theme",
        "re-read the current draft state",
        "UNTESTED",
    ):
        require(boundary.lower() in build_text.lower(), f"build-loop boundary missing: {boundary}", failures)

    fixture_path = Path(__file__).parent / "fixtures" / "pdp-cold-start-input.json"
    receipt_path = Path(__file__).parent / "receipts" / "pdp-cold-start-output.md"
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    receipt = receipt_path.read_text(encoding="utf-8")

    require(fixture.get("connector_write_permission") == "NO PERMISSION", "negative-control permission changed", failures)
    require(bool(fixture.get("missing_product_facts")), "negative-control no longer has missing facts", failures)
    require("BLOCKED BY FACTS" in receipt, "cold-start receipt did not block on missing facts", failures)
    require("No Shopify mutation packet was produced" in receipt, "cold-start receipt crossed write boundary", failures)
    require("NO PERMISSION" in receipt, "cold-start receipt lost permission state", failures)
    require("Heavyweight" in receipt and "Claims Veto List" in receipt, "unsupported-claim rejection missing", failures)
    require("too short" in receipt.lower() and "Objection Ledger" in receipt, "return evidence did not change architecture", failures)
    require("make it premium" not in receipt.lower(), "generic one-shot instruction leaked into receipt", failures)

    sys.path.insert(0, str(REPO_ROOT / "execution"))
    from expert_router import route as route_expert  # noqa: PLC0415
    from workflow_router import search_workflows  # noqa: PLC0415

    route_query = (
        "Rebuild this Shopify apparel product page with Claude using customer questions "
        "and return reasons, but do not touch the live theme"
    )
    expert_results = route_expert(route_query, top_n=3)
    require(bool(expert_results) and expert_results[0][1] == "bitbranding", "expert router did not choose BitBranding", failures)

    workflow_results = search_workflows(route_query, top_n=3)
    require(
        bool(workflow_results) and workflow_results[0][1]["name"] == "bb-pdp-rebuild",
        "workflow router did not choose /bb-pdp-rebuild",
        failures,
    )

    if failures:
        print("BitBranding PDP skill system: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("BitBranding PDP skill system: PASS")
    print("- 3 connected workflows and 3 born-v2 prompts present")
    print("- cold-start negative control blocks unsupported claims and Shopify mutation")
    print("- rendered-review, current-state, live-theme, and business-proof boundaries present")
    print("- natural-language routing chooses BitBranding and /bb-pdp-rebuild")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
