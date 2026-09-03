#!/usr/bin/env python3
"""Deterministic evidence-bounded diagnostic core for the Instagram Growth OS."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPAIR_ORDER = ["OFFER", "TRUST", "PROFILE", "ATTRACTION"]


def _ratio(numerator: Any, denominator: Any) -> float | None:
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        return None
    if denominator <= 0:
        return None
    return round(numerator / denominator, 4)


def diagnose(record: dict[str, Any]) -> dict[str, Any]:
    """Return one primary break using declared evidence states, never guessed thresholds."""
    missing = [
        field
        for field in ("offer_clarity", "compliance_risk", "profile_state", "trust_state", "monetization_state")
        if field not in record
    ]

    if record.get("compliance_risk") is True:
        primary = "COMPLIANCE"
        fixes = ["Run category-specific compliance review", "Remove or substantiate restricted claims", "Re-audit the funnel after clearance"]
    elif record.get("offer_clarity") in {"vague", "contradicted"}:
        primary = "OFFER"
        fixes = ["Complete Offer Canvas", "Validate one transformation and price architecture", "Rebuild trust assets around the selected offer"]
    elif record.get("trust_state") in {"voiceless", "generic", "proof_light"}:
        primary = "TRUST"
        fixes = ["Add attributable opinion and voice", "Add one bounded proof object", "Reform Trial and feed versions"]
    elif record.get("profile_state") in {"vague", "unbingeable", "high_friction"}:
        primary = "PROFILE"
        fixes = ["Clarify cold-scan promise", "Rebuild pins/highlights as a binge path", "Reduce to one primary link"]
    elif record.get("monetization_state") in {"fragmented", "undercapturing"}:
        primary = "MONETIZATION"
        fixes = ["Select one conversion event", "Align one-link promise and offer ladder", "Instrument sold and collected revenue"]
    elif record.get("attraction_state") == "wrong_audience":
        primary = "ATTRACTION"
        fixes = ["Rebuild ICP topic map", "Test 0.5-second visual clarity", "Measure non-follower audience match"]
    else:
        primary = "UNVERIFIED"
        fixes = ["Supply missing evidence", "Run the inspection sequence", "Name a break only after denominators exist"]

    metrics = record.get("metrics", {}) if isinstance(record.get("metrics"), dict) else {}
    ratios = {
        "profile_visit_rate": _ratio(metrics.get("profile_visits"), metrics.get("reach", metrics.get("views"))),
        "profile_follow_rate": _ratio(metrics.get("follows"), metrics.get("profile_visits")),
        "profile_dm_rate": _ratio(metrics.get("dms"), metrics.get("profile_visits")),
        "call_close_rate": _ratio(metrics.get("sales"), metrics.get("calls")),
    }
    return {
        "case": record.get("case", "unnamed"),
        "breaking_point": primary,
        "confidence": "HIGH" if primary != "UNVERIFIED" and not missing else "LOW",
        "missing_evidence": missing,
        "ratios": ratios,
        "next_fixes": fixes,
        "repair_order": REPAIR_ORDER,
        "revenue_state": "VERIFIED_EVENT" if record.get("payment_receipt") else "NO_EVENT",
    }


def validate_spec(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    skills = payload.get("skills", [])
    required = {"id", "slug", "name", "layer", "input", "process", "output", "success_metric", "automation_advantage", "system_prompt_path", "external_boundary"}
    errors: list[str] = []
    if len(skills) != 10:
        errors.append(f"expected 10 skills, found {len(skills)}")
    for index, skill in enumerate(skills, start=1):
        absent = sorted(required - set(skill))
        if absent:
            errors.append(f"skill {index} missing: {', '.join(absent)}")
    ids = [item.get("id") for item in skills]
    slugs = [item.get("slug") for item in skills]
    if len(ids) != len(set(ids)):
        errors.append("skill ids are not unique")
    if len(slugs) != len(set(slugs)):
        errors.append("skill slugs are not unique")
    return {"status": "PASS" if not errors else "FAIL", "skills": len(skills), "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    diagnose_parser = sub.add_parser("diagnose")
    diagnose_parser.add_argument("input", type=Path)
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("spec", type=Path)
    args = parser.parse_args()

    if args.command == "diagnose":
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        records = payload if isinstance(payload, list) else [payload]
        print(json.dumps([diagnose(record) for record in records], indent=2))
        return 0
    result = validate_spec(args.spec)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
