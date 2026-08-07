#!/usr/bin/env python3
"""FROZEN V1 EXPERIMENT for the original Reality Before Rhetoric benchmark.

No active workflow may import this helper. It is retained only so the historical
V1 activation and artifact-tier experiment remains inspectable and reproducible.
The active optional-practice contract is documentation-led and claim-local.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


CONTRACT_PATH = (
    "semantic_libraries/antigravity/primitives/"
    "reality-before-rhetoric-contract.md"
)

MECHANICAL_TERMS = (
    "alphabetize",
    "sort these",
    "preserve every word",
    "format this json",
    "format the json",
    "fix the typo",
    "correct the typo",
    "rename the local variable",
    "rename this variable",
    "run the existing unit test",
    "change the filename",
    "convert this date",
)

CONSEQUENTIAL_TERMS = (
    "story",
    "transformation",
    "manifesto",
    "personal",
    "lived",
    "publishing",
    "before and after",
    "before-and-after",
    "offer",
    "copy",
    "buyer",
    "case study",
    "proof",
    "outcome",
    "claim",
    "strategy",
    "launch plan",
    "best launch",
    "tradeoff",
    "trade-off",
    "falsifier",
    "research",
    "study",
    "paper",
    "evidence",
    "definitive conclusion",
    "synthesize",
    "repair",
    "fixed",
    "working",
    "ready everywhere",
    "runtime",
    "behavior",
    "router",
    "routing",
    "hook",
    "launchpad gate",
)

ACTIVATING_ROUTES = {
    "farrice-content-os",
    "high-taste-writing-os",
    "high-taste-os",
    "dhar-transformational-content-factory",
    "dhar-mann",
    "deep-research",
    "system-audit",
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def has_any(value: str, terms: Iterable[str]) -> bool:
    return any(term in value for term in terms)


def infer_domain(query: str, route: str = "") -> str:
    q = normalize(query)
    route = normalize(route).lstrip("/")
    if has_any(q, ("research", "study", "paper", "evidence", "synthesize")) or route == "deep-research":
        return "research"
    if has_any(q, ("repair", "fixed", "working", "runtime", "router", "routing", "hook", "launchpad gate")) or route == "system-audit":
        return "system-repair"
    if has_any(q, ("strategy", "launch plan", "best launch", "tradeoff", "trade-off", "falsifier")):
        return "strategy"
    if has_any(q, ("offer", "buyer", "case study", "sales copy", "offer copy", "outcome")):
        return "offer-copy"
    if has_any(q, ("story", "transformation", "manifesto", "personal", "lived", "publishing")) or route == "farrice-content-os":
        return "personal-content"
    return "general"


def classify_activation(query: str, *, route: str = "", lane: str = "") -> dict[str, Any]:
    """Return the minimum gate decision without pretending source was retrieved."""

    q = normalize(query)
    normalized_route = normalize(route).lstrip("/")
    domain = infer_domain(query, route)

    if has_any(q, MECHANICAL_TERMS):
        return {
            "activation": "bypass",
            "domain": domain,
            "reason": "Mechanical work has a supplied, inspectable correctness condition and does not need source acquisition.",
            "contract": CONTRACT_PATH,
            "required_handoff": None,
        }

    if has_any(q, CONSEQUENTIAL_TERMS) or normalized_route in ACTIVATING_ROUTES:
        return {
            "activation": "activate",
            "domain": domain,
            "reason": "The requested artifact or claim depends on consequential lived, observed, external, buyer, strategic, or runtime evidence.",
            "contract": CONTRACT_PATH,
            "required_handoff": "Source Depth Packet",
            "lane": normalize(lane) or "unspecified",
        }

    return {
        "activation": "bypass",
        "domain": domain,
        "reason": "No consequential source-dependent claim or state change was detected.",
        "contract": CONTRACT_PATH,
        "required_handoff": None,
    }


def evaluate_source_profile(profile: dict[str, Any]) -> dict[str, Any]:
    """Evaluate an explicit evidence profile against the shared decision vocabulary."""

    gap_effect = profile.get("gap_effect", "blocks")
    gap_owner = profile.get("gap_owner", "unknown")
    permission = profile.get("permission", "unknown")
    fallback_supported = bool(profile.get("fallback_supported", False))

    if permission == "blocked":
        source_status = "permission-blocked"
        artifact_tier = "hold"
        may_draft = False
    elif gap_effect == "blocks":
        source_status = "source-missing"
        if gap_owner == "user":
            artifact_tier = "acquire-lived-source"
        elif gap_owner == "external":
            artifact_tier = "acquire-external-evidence"
        else:
            artifact_tier = "diagnostic-only"
        may_draft = False
    elif gap_effect == "narrows":
        source_status = "source-limited"
        artifact_tier = "draft" if fallback_supported else "diagnostic-only"
        may_draft = fallback_supported
    elif gap_effect == "none":
        source_status = "source-ready"
        artifact_tier = "draft"
        may_draft = True
    else:
        raise ValueError(f"unsupported gap_effect: {gap_effect!r}")

    result = {
        "source_status": source_status,
        "artifact_tier": artifact_tier,
        "hinge": profile.get("hinge", "missing"),
        "may_draft": may_draft,
        "gap_owner": gap_owner,
        "fallback_supported": fallback_supported,
    }
    if profile.get("claim_class"):
        result["claim_class"] = profile["claim_class"]
    if profile.get("proof_state"):
        result["proof_state"] = profile["proof_state"]
    return result


def benchmark(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    cases = []
    for fixture in payload.get("fixtures", []):
        expected = fixture["accepted_behavior"]
        activation = classify_activation(fixture["query"], route=fixture["route"])
        source_decision = evaluate_source_profile(fixture["source_profile"])
        fields = [
            "source_status",
            "artifact_tier",
            "hinge",
            "may_draft",
            "claim_class",
            "proof_state",
        ]
        mismatches = {
            field: {"expected": expected.get(field), "actual": source_decision.get(field)}
            for field in fields
            if field in expected and expected.get(field) != source_decision.get(field)
        }
        if activation["activation"] != expected["activation"]:
            mismatches["activation"] = {
                "expected": expected["activation"],
                "actual": activation["activation"],
            }
        if activation["domain"] != fixture["domain"]:
            mismatches["domain"] = {
                "expected": fixture["domain"],
                "actual": activation["domain"],
            }
        cases.append(
            {
                "id": fixture["id"],
                "domain": fixture["domain"],
                "passed": not mismatches,
                "activation": activation,
                "source_decision": source_decision,
                "mismatches": mismatches,
            }
        )

    controls = []
    for control in payload.get("bypass_controls", []):
        actual = classify_activation(control["query"], route=control["route"])
        controls.append(
            {
                "id": control["id"],
                "passed": actual["activation"] == control["expected_activation"],
                "activation": actual,
            }
        )

    return {
        "schema_version": "reality-before-rhetoric-benchmark/v1",
        "cases": cases,
        "bypass_controls": controls,
        "passed": all(case["passed"] for case in cases)
        and all(control["passed"] for control in controls),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Reality Before Rhetoric helper.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    classify_parser = subparsers.add_parser("classify")
    classify_parser.add_argument("query", nargs="+")
    classify_parser.add_argument("--route", default="")
    classify_parser.add_argument("--lane", default="")

    evaluate_parser = subparsers.add_parser("evaluate")
    evaluate_parser.add_argument("profile", help="JSON object containing an evidence profile.")

    benchmark_parser = subparsers.add_parser("benchmark")
    benchmark_parser.add_argument("fixture_path", type=Path)

    args = parser.parse_args()
    if args.command == "classify":
        result = classify_activation(
            " ".join(args.query), route=args.route, lane=args.lane
        )
    elif args.command == "evaluate":
        result = evaluate_source_profile(json.loads(args.profile))
    else:
        result = benchmark(args.fixture_path)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("passed", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
