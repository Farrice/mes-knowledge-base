#!/usr/bin/env python3
"""Deterministic, synthetic Lead-to-Proposal Proof Sprint demonstration."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any


REQUIRED = ("lead_id", "company", "contact", "email", "service", "budget", "timeline")
SENSITIVE_KEYS = {"ssn", "medical_record", "diagnosis", "credit_card", "bank_account"}
UNSUPPORTED_PATTERNS = ("guaranteed", "100%", "double revenue", "no risk", "best in the world")


@dataclass
class RunResult:
    lead_id: str
    status: str
    qualification: dict[str, Any]
    missing: list[str]
    flags: list[str]
    proposal_draft: str | None
    follow_up_task: dict[str, Any] | None
    crm_record: dict[str, Any]
    approval_status: str
    external_send_permitted: bool
    receipt_hash: str


class LeadToProposalWorkflow:
    """A safe reference workflow; live integrations remain out of scope."""

    def __init__(self, known_ids: set[str] | None = None) -> None:
        self.known_ids = set(known_ids or set())

    @staticmethod
    def _receipt(payload: dict[str, Any]) -> str:
        raw = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()[:16]

    def run(self, lead: dict[str, Any], integration_ok: bool = True) -> RunResult:
        lead_id = str(lead.get("lead_id", "MISSING"))
        missing = [field for field in REQUIRED if not lead.get(field)]
        flags: list[str] = []

        if lead_id in self.known_ids:
            flags.append("DUPLICATE_INQUIRY")
        if missing:
            flags.append("MISSING_REQUIRED_INFORMATION")
        if lead.get("requirements_conflict"):
            flags.append("CONFLICTING_REQUIREMENTS")
        if SENSITIVE_KEYS.intersection(lead):
            flags.append("SENSITIVE_OR_REGULATED_INFORMATION")
        if not integration_ok:
            flags.append("INTEGRATION_FAILURE")

        claims = " ".join(str(x) for x in lead.get("requested_claims", []))
        if any(pattern.lower() in claims.lower() for pattern in UNSUPPORTED_PATTERNS):
            flags.append("UNSUPPORTED_FACTUAL_CLAIM")

        confidence = 1.0 - (0.13 * len(missing)) - (0.18 * bool(lead.get("requirements_conflict")))
        confidence = round(max(0.0, min(1.0, confidence)), 2)
        if confidence < 0.65:
            flags.append("LOW_CONFIDENCE_QUALIFICATION")

        blocking = bool(flags)
        qualification = {
            "company": lead.get("company"),
            "contact": lead.get("contact"),
            "service_requested": lead.get("service"),
            "budget": lead.get("budget"),
            "timeline": lead.get("timeline"),
            "confidence": confidence,
            "decision": "HUMAN_REVIEW" if blocking else "READY_FOR_PROPOSAL_REVIEW",
        }

        proposal = None
        follow_up = None
        if not blocking:
            proposal = (
                f"DRAFT — HUMAN APPROVAL REQUIRED\n\n"
                f"For {lead['company']}: {lead['service']}\n"
                f"Client-stated budget: {lead['budget']}\n"
                f"Client-stated timeline: {lead['timeline']}\n\n"
                "Scope and claims must be checked against the approved template before sending."
            )
            follow_up = {
                "owner": lead.get("owner", "WORKFLOW_OWNER_PLACEHOLDER"),
                "due": str(date.today() + timedelta(days=1)),
                "action": "Review qualification and proposal draft; approve, edit, or reject.",
            }

        crm_record = {
            "lead_id": lead_id,
            "company": lead.get("company"),
            "contact": lead.get("contact"),
            "email": lead.get("email"),
            "stage": "EXCEPTION_REVIEW" if blocking else "PROPOSAL_DRAFTED",
            "flags": flags,
            "source": lead.get("source", "synthetic_demo"),
        }
        status = "HELD" if blocking else "DRAFT_READY"
        receipt_payload = {"lead_id": lead_id, "status": status, "flags": flags, "crm": crm_record}
        result = RunResult(
            lead_id=lead_id,
            status=status,
            qualification=qualification,
            missing=missing,
            flags=flags,
            proposal_draft=proposal,
            follow_up_task=follow_up,
            crm_record=crm_record,
            approval_status="HOLD_FOR_HUMAN",
            external_send_permitted=False,
            receipt_hash=self._receipt(receipt_payload),
        )
        if lead_id != "MISSING":
            self.known_ids.add(lead_id)
        return result


def run_fixture(fixture_path: Path, output_path: Path) -> dict[str, Any]:
    fixture = json.loads(fixture_path.read_text())
    workflow = LeadToProposalWorkflow()
    results = []
    for case in fixture["cases"]:
        result = workflow.run(case["lead"], integration_ok=case.get("integration_ok", True))
        results.append({"case": case["name"], "expected": case["expected"], "result": asdict(result)})

    passed = 0
    failures = []
    for row in results:
        actual = row["result"]
        expected = row["expected"]
        checks = {
            "status": actual["status"] == expected["status"],
            "required_flags": set(expected.get("flags", [])).issubset(actual["flags"]),
            "human_hold": actual["approval_status"] == "HOLD_FOR_HUMAN",
            "send_blocked": actual["external_send_permitted"] is False,
        }
        if all(checks.values()):
            passed += 1
        else:
            failures.append({"case": row["case"], "checks": checks, "actual": actual})

    receipt = {
        "proof_state": "LOCAL_DEMONSTRATION_ONLY",
        "fixture": str(fixture_path),
        "cases": len(results),
        "passed": passed,
        "failed": len(failures),
        "all_human_holds_worked": all(not r["result"]["external_send_permitted"] for r in results),
        "failures": failures,
        "results": results,
    }
    output_path.write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    receipt = run_fixture(root / "fixtures" / "cases.json", root / "demo-test-receipt.json")
    print(json.dumps({k: receipt[k] for k in ("proof_state", "cases", "passed", "failed", "all_human_holds_worked")}, indent=2))
