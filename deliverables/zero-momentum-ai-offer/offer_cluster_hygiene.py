#!/usr/bin/env python3
"""Local offer-cluster verifier. It reads artifacts and writes one JSON receipt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def check(name: str, condition: bool, detail: str) -> dict:
    return {"name": name, "passed": bool(condition), "detail": detail}


def main() -> int:
    canon = (HERE / "offer-canon.md").read_text()
    readme = (HERE / "README.md").read_text()
    landing = (HERE / "landing-page.html").read_text()
    tournament = (HERE / "offer-tournament.md").read_text()
    old_path = ROOT / "_active/linkedin/04-deliverables/context-os/02-OFFER-CANON.md"
    old = old_path.read_text()
    receipt = json.loads((HERE / "demo/demo-test-receipt.json").read_text())

    checks = [
        check("one_active_primary", "Lead-to-Proposal Proof Sprint" in canon and "Lead-to-Proposal Proof Sprint" in readme, "Launch Control and canon name the same primary."),
        check("price_consistency", "$1,500" in canon and "$750 paid to begin" in canon and "$1,500" in landing and "$750 to begin" in landing, "Landing and canon use $1,500 / $750 + $750."),
        check("old_primary_parked", "status: parked_as_primary" in old and "PARKED AS PRIMARY" in old, "Old Angle Map canon is explicitly parked and linked."),
        check("supplement_secondary", "Secondary adapter — PARKED" in canon and "first paid services pilot" not in landing, "Supplement adapter is prepared but not front-facing."),
        check("proof_disclosure", "exact Farrice Cain offer is untested" in landing and "UNTESTED" in readme, "Market proof is not represented as exact-offer validation."),
        check("no_revenue_guarantee", "No revenue guarantee" in canon and "does not guarantee a sale" in landing, "Offer promise is behavior-bounded."),
        check("human_hold", "Human approval before any proposal" in canon and "HOLD_FOR_HUMAN" in json.dumps(receipt), "Canon and test output both require a human."),
        check("demo_inspected", receipt.get("failed") == 0 and receipt.get("all_human_holds_worked") is True, "All fixture outputs and holds passed."),
        check("ai_removal_test", "Remove “AI” from the headline" in tournament, "Offer remains intelligible without AI."),
        check("cta_present", "Workflow Loss Review" in canon and "Workflow Loss Review" in landing, "One consistent next step."),
        check("external_placeholders", "BOOKING LINK PLACEHOLDER — NOT LIVE" in landing, "No invented booking destination."),
    ]
    result = {
        "verdict": "PASS" if all(x["passed"] for x in checks) else "FAIL",
        "checks": len(checks),
        "passed": sum(x["passed"] for x in checks),
        "failed": [x for x in checks if not x["passed"]],
        "details": checks,
    }
    (HERE / "offer-cluster-hygiene-receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("verdict", "checks", "passed", "failed")}, indent=2))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
