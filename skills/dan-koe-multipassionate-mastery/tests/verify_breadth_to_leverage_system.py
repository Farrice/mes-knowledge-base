#!/usr/bin/env python3
"""Deterministic verifier for the Breadth-to-Leverage skill subsystem."""

from __future__ import annotations

import json
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
PRIMARY_SOURCE = REPO_ROOT / "extractions" / "video-context" / "UnXm_R1APxo"
SUPPORT_SOURCE = REPO_ROOT / "extractions" / "video-context" / "YNJ18ggqwqM"


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    required = (
        SKILL_ROOT / "workflows" / "breadth-to-leverage-system.md",
        SKILL_ROOT / "references" / "prompts-v2" / "breadth-to-leverage-decision-brief.md",
        SKILL_ROOT / "references" / "breadth-to-leverage-skill-system-contract.md",
        REPO_ROOT / ".agent" / "workflows" / "breadth-to-leverage.md",
    )
    for path in required:
        require(path.is_file() and path.stat().st_size > 0, f"missing or empty: {path}", failures)

    for package in (PRIMARY_SOURCE, SUPPORT_SOURCE):
        for name in (
            "metadata.json",
            "transcript.vtt",
            "transcript.txt",
            "transcript_segments.json",
            "video-context-ledger.md",
            "video-context-ledger.json",
            "uncertainty-report.md",
            "analysis.md",
        ):
            path = package / name
            require(path.is_file() and path.stat().st_size > 0, f"source package missing: {path}", failures)

    workflow = (SKILL_ROOT / "workflows" / "breadth-to-leverage-system.md").read_text(encoding="utf-8")
    for boundary in (
        "working hypotheses",
        "withhold `Polymath`",
        "Work broadly, execute narrowly",
        "No external action",
        "COMMERCIAL PROOF",
    ):
        require(boundary.lower() in workflow.lower(), f"workflow boundary missing: {boundary}", failures)

    prompt = (SKILL_ROOT / "references" / "prompts-v2" / "breadth-to-leverage-decision-brief.md").read_text(encoding="utf-8")
    for section in (
        "## Role & Activation",
        "## Input Required",
        "## Execution Protocol",
        "## Output Contract",
        "## Output Skeleton",
        "## Quality Gate",
        "## Creative Latitude",
        "## Deploy When",
    ):
        require(section in prompt, f"born-v2 prompt lacks {section}", failures)

    fixture = json.loads((Path(__file__).parent / "fixtures" / "breadth-to-leverage-cold-start.json").read_text(encoding="utf-8"))
    receipt = (Path(__file__).parent / "receipts" / "breadth-to-leverage-cold-start.md").read_text(encoding="utf-8")
    require(fixture["external_action_permission"] == "NO PERMISSION", "negative-control permission changed", failures)
    require(bool(fixture["missing_evidence"]), "negative control no longer has missing evidence", failures)
    require("WORKING HYPOTHESIS" in receipt, "receipt inflated hypothesis into diagnosis", failures)
    require("Polymath is withheld" in receipt, "receipt granted flattering Polymath identity", failures)
    require("NO PERMISSION" in receipt and "No external action was taken" in receipt, "permission boundary failed", failures)
    require("Collected: `NO EVENT`" in receipt, "receipt fabricated commercial proof", failures)
    require("NOT YET ELIGIBLE" in receipt, "interestingness handoff fired before proof artifact", failures)

    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    require("/breadth-to-leverage" in skill_text, "SKILL.md does not expose /breadth-to-leverage", failures)

    sys.path.insert(0, str(REPO_ROOT / "execution"))
    from expert_router import route as route_expert  # noqa: PLC0415
    from workflow_router import search_workflows  # noqa: PLC0415

    query = "I have too many interests and keep building frameworks instead of deploying; help me work broadly but execute narrowly"
    expert_results = route_expert(query, top_n=5)
    require(any(item[1] == "dan-koe" for item in expert_results), "expert routing did not include Dan Koe", failures)
    workflow_results = search_workflows(query, top_n=10)
    require(any(item[1]["name"] == "breadth-to-leverage" for item in workflow_results), "workflow routing did not include /breadth-to-leverage", failures)

    if failures:
        print("Breadth-to-Leverage skill system: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Breadth-to-Leverage skill system: PASS")
    print("- primary and supporting video-context source packages present")
    print("- behavior-hypothesis, focus-lock, permission, and proof boundaries present")
    print("- cold-start negative control withholds Polymath and commercial proof")
    print("- natural-language routing finds Dan Koe and /breadth-to-leverage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
