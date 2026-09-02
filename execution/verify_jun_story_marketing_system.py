#!/usr/bin/env python3
"""Deterministic coverage and negative controls for the full Jun story-marketing system."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from workflow_router import search_workflows


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "extractions/jun-yuh-story-marketing-system/fixtures/system-cases.json"

REQUIRED_FILES = [
    "extractions/jun-yuh-story-marketing-system/skill-system-contract.md",
    "extractions/jun-yuh-story-marketing-system/source-coverage-audit.md",
    "extractions/jun-yuh-story-marketing-system/behavior-proof.md",
    "extractions/jun-yuh-story-marketing-system/USER-GUIDE.md",
    "extractions/jun-yuh-story-marketing-system/fixtures/system-cases.json",
    "skills/jun-yuh-creator-vision/workflows/expertise-to-story-content.md",
    "skills/jun-yuh-creator-vision/workflows/story-mission-campaign.md",
    "skills/jun-yuh-creator-vision/workflows/story-led-conversion-asset.md",
    "skills/jun-yuh-creator-vision/workflows/story-selling-masterclass.md",
    "skills/jun-yuh-creator-vision/workflows/story-bank-flywheel.md",
    "skills/jun-yuh-creator-vision/workflows/story-performance-learning-loop.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/expertise-to-story-content.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-mission-campaign.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-led-conversion-asset.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-selling-masterclass.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-bank-flywheel.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-performance-learning-loop.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/content-marketing-playbook.md",
    ".agent/workflows/junyuh-marketing.md",
    ".claude/commands/junyuh-marketing.md",
    ".agents/skills/source-command-junyuh-marketing/SKILL.md",
]

DIRECT_WORK = {"incident", "status", "procedure", "specification", "calculation"}


def expertise_state(case: dict[str, object]) -> str:
    if str(case.get("work_type", "")).lower() in DIRECT_WORK:
        return "NO_STORY"
    if bool(case.get("claims_customer_result")) and case.get("proof_ceiling") != "MARKET":
        return "CLAIM_BOUNDARY"
    if int(case.get("steps", 0)) < 2 or int(case.get("decision_rules", 0)) < 1:
        return "NEEDS_SOURCE"
    if not str(case.get("output", "")).strip():
        return "NEEDS_SOURCE"
    return "EXPERTISE_STORY_READY"


def performance_state(case: dict[str, object]) -> str:
    if not bool(case.get("deployed")):
        return "NO_EVENT"
    if float(case.get("collected", 0)) > 0:
        return "COLLECTED"
    if int(case.get("payments", 0)) > 0:
        return "SALE"
    if int(case.get("qualified_replies", 0)) > 0 or int(case.get("calls", 0)) > 0:
        return "INTENT_SIGNAL"
    if int(case.get("views", 0)) > 0:
        return "ATTENTION_SIGNAL"
    return "NO_EVENT"


def roi_eligible(case: dict[str, object]) -> bool:
    return (
        float(case.get("collected", 0)) > 0
        and float(case.get("cost", 0)) > 0
        and bool(case.get("attribution"))
    )


def require_tokens(path: str, tokens: tuple[str, ...], failures: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            failures.append(f"{path}: missing token {token!r}")


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    if failures:
        print("JUN STORY MARKETING SYSTEM VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    payload = json.loads(FIXTURES.read_text(encoding="utf-8"))

    expertise_results: dict[str, str] = {}
    for case in payload["expertise_cases"]:
        actual = expertise_state(case)
        expertise_results[str(case["id"])] = actual
        if actual != case["expected"]:
            failures.append(f"{case['id']}: expected {case['expected']}, got {actual}")

    performance_results: dict[str, str] = {}
    for case in payload["performance_cases"]:
        actual = performance_state(case)
        performance_results[str(case["id"])] = actual
        if actual != case["expected"]:
            failures.append(f"{case['id']}: expected {case['expected']}, got {actual}")
        if roi_eligible(case) != bool(case["roi_eligible"]):
            failures.append(f"{case['id']}: ROI eligibility mismatch")

    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/content-marketing-playbook.md",
        (
            "Problem → Pursuit → Payoff",
            "ATTRACT",
            "NURTURE",
            "POSITION",
            "CONVERT",
            "NEEDS SOURCE",
            "NO OFFER",
            "MARKET PROOF: NO EVENT",
            "ROI",
            "story-bank-flywheel.md",
        ),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/expertise-to-story-content.md",
        ("SERVICE", "PHYSICAL PRODUCT", "COACHING", "FOUNDER", "EDUCATION", "METHOD_CANDIDATE"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/story-led-conversion-asset.md",
        ("IDENTIFICATION", "TRUST", "BELIEF", "NEXT ACTION", "SYSTEM SYNTHESIS", "NO CTA"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/story-selling-masterclass.md",
        ("useful win", "implementation vehicle", "guarantees", "scarcity", "one presentation/copy owner"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/story-performance-learning-loop.md",
        ("ATTENTION SIGNAL", "RECOGNITION SIGNAL", "INTENT SIGNAL", "COLLECTED", "attributable revenue and cost"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/SKILL.md",
        ("workflows: 24", "Expertise-to-Story Content Engine", "Story Performance and ROI Learning Loop"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/references/source-ledger.md",
        ("Promise as a fourth Jun P", "REJECTED ATTRIBUTION", "Story content produces ROI", "UNTESTED"),
        failures,
    )
    require_tokens(
        "extractions/jun-yuh-story-marketing-system/source-coverage-audit.md",
        (
            "Bounded Tacit-Pattern and Decision-Sequence Audit",
            "Material mining precedes formatting",
            "identification, trust, and belief before attaching the CTA",
            "Rejected Inferences",
        ),
        failures,
    )
    require_tokens(
        "extractions/jun-yuh-story-marketing-system/behavior-proof.md",
        (
            "Cold Unlike-Business Test",
            "_active/clients/_shared/realtor-editorial-system/GIGI-KICKOFF.md",
            "NEEDS SOURCE",
            "fair-housing",
        ),
        failures,
    )

    expected_tacit_controls = {
        "material_before_format": "SOURCE-SUPPORTED",
        "pursuit_before_payoff_compression": "SOURCE-SUPPORTED",
        "identification_trust_belief_before_cta": "SOURCE-SUPPORTED",
        "mission_before_asset": "SOURCE-SUPPORTED",
        "promise_as_fourth_jun_p": "REJECTED ATTRIBUTION",
        "story_causes_roi": "UNTESTED",
    }
    if payload.get("tacit_sequence_controls") != expected_tacit_controls:
        failures.append("tacit sequence controls do not match the locked evidence boundary")

    routing_queries = (
        "turn my expertise into a complete story-led content marketing campaign",
        "use Jun Yuh problem pursuit payoff for attract nurture position and convert content",
        "build a story marketing system from my expertise that can lead into an offer and measure buyer response",
    )
    routing_results: dict[str, str] = {}
    for query in routing_queries:
        matches = search_workflows(query, top_n=5)
        names = [match[1]["name"] for match in matches]
        routing_results[query] = names[0] if names else "NONE"
        if "junyuh-marketing" not in names[:3]:
            failures.append(f"routing miss for {query!r}: top three were {names[:3]}")

    if failures:
        print("JUN STORY MARKETING SYSTEM VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("JUN STORY MARKETING SYSTEM VERIFY: PASS")
    print(f"- required files: {len(REQUIRED_FILES)}/{len(REQUIRED_FILES)}")
    print(f"- expertise controls: {expertise_results}")
    print(f"- performance controls: {performance_results}")
    print("- ROI controls: views/replies are not ROI; collected revenue still needs cost and attribution")
    print(f"- routing controls: {routing_results}")
    print("- preservation: focused Jun Story Engine remains a separate verified front door")
    return 0


if __name__ == "__main__":
    sys.exit(main())
