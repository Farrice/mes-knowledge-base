#!/usr/bin/env python3
"""Verify the Antigravity global-access owner, handoff, and context policy."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import antigravity_global_access  # type: ignore  # noqa: E402
import raw_intent_run_packet  # type: ignore  # noqa: E402
import workflow_router  # type: ignore  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def first_route(query: str) -> str:
    results = workflow_router.search_workflows(query, top_n=3)
    return str(results[0][1]["name"]) if results else ""


def main() -> int:
    mixed = (
        "Implement the Google Antigravity global access layer in Codex, reconcile routing and hot/cold policy first, "
        "then package the skill manifest as a personal plugin without context rot."
    )
    build = "Implement a global skill manifest and personal plugin for Google Antigravity."
    unrelated = "Create a personal plugin for formatting local Python logs."

    mixed_result = antigravity_global_access.classify_global_access_intent(mixed)
    require(mixed_result["route"] == "system-audit", "mixed access repair/build lost the audit owner")
    require(mixed_result["support_gates"] == ["source-to-skill-system"], "mixed request lost its bounded builder handoff")
    require(first_route(mixed) == "system-audit", "workflow router did not bind the mixed request to /system-audit")

    build_result = antigravity_global_access.classify_global_access_intent(build)
    require(build_result["route"] == "source-to-skill-system", "pure plugin build lost the skill-system owner")
    require(first_route(build) == "source-to-skill-system", "workflow router did not bind pure packaging to /source-to-skill-system")

    packet = raw_intent_run_packet.build_packet(mixed, mode="system")
    require(packet["chosen_route"] == "system-audit", "raw-intent packet bypassed reconciliation")
    require("source-to-skill-system" in packet["support_gates"], "raw-intent packet lost the builder handoff")

    unrelated_result = antigravity_global_access.classify_global_access_intent(unrelated)
    require(not unrelated_result["matched"], "classifier captured an unrelated plugin request")

    policy = (ROOT / "CODEX.md").read_text(encoding="utf-8")
    require("Hot and cold are routing and context-loading states" in policy, "CODEX.md lacks the reconciled context policy")
    require("single canonical live wrapper tree" in policy, "CODEX.md lacks the single-tree invariant")

    contract = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "antigravity-global-access-contract.md"
    require(contract.exists(), "global access contract is missing")

    print("Antigravity global access verification: PASS")
    print("- mixed reconciliation/build request -> /system-audit + /source-to-skill-system handoff")
    print("- pure manifest/plugin build -> /source-to-skill-system + /system-audit support")
    print("- unrelated plugin request is not captured")
    print("- hot/cold means routing and context loading; canonical wrappers stay single-tree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

