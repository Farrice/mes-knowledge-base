#!/usr/bin/env python3
"""Verify an Expert Practice OS route artifact from packet, route, and contract.

This verifier never trusts a declared PASS, proof stage, payment count, runtime
provenance, or registration flag. It derives a diagnostic verdict from the
artifacts and emits hashes so a later detached runtime receipt can bind to the
exact input and output.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any


PRACTICE_TYPES = {
    "AI_CONSULTING",
    "LIFE_COACHING_OR_LIFE_DESIGN",
    "SOLOPRENEURSHIP",
}
STAGES = {
    "STAGE_0_PAID_PROOF",
    "STAGE_1_REPEATABLE_PRACTICE",
    "STAGE_2_PRODUCTIZED_PRACTICE",
    "STAGE_3_SCALED_COMPANY",
}
PROVENANCE = {
    "RUNTIME_OBSERVED",
    "ORCHESTRATOR_ATTESTED",
    "OPERATOR_ATTESTED",
}
TERMINALS = {
    "ADVANCE_TO_REPEATABILITY",
    "REVISE_POP",
    "STOP_OR_HOLD",
}


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def get_path(value: Any, dotted: str) -> Any:
    current = value
    for part in dotted.split("."):
        if isinstance(current, list):
            try:
                current = current[int(part)]
            except (ValueError, IndexError, TypeError):
                return None
        elif isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def add_error(errors: list[str], code: str) -> None:
    if code not in errors:
        errors.append(code)


def text_blob(value: Any) -> str:
    return json.dumps(value, sort_keys=True).lower()


def is_generic(text: Any, phrases: set[str]) -> bool:
    if not isinstance(text, str):
        return True
    normalized = re.sub(r"[^a-z0-9 ]+", " ", text.lower()).strip()
    return normalized in phrases or len(normalized.split()) < 6


def dated_events(packet: dict[str, Any], key: str) -> list[dict[str, Any]]:
    events = get_path(packet, f"actuals.{key}")
    return events if isinstance(events, list) else []


def validate_packet(packet: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    qualification_paths = [
        "practitioner.identity",
        "practitioner.credentials",
        "practitioner.scope.allowed",
        "practitioner.scope.excluded",
    ]
    if any(get_path(packet, path) in (None, "", []) for path in qualification_paths):
        add_error(errors, "E_INPUT_QUALIFICATION_MISSING")

    required_paths = [
        "practitioner.public_role",
        "practitioner.experience",
        "practitioner.repeated_results",
        "practitioner.evidence_provenance",
        "protocol.name",
        "protocol.steps",
        "protocol.dependencies",
        "protocol.evidence",
        "protocol.claims.allowed",
        "protocol.claims.restricted",
        "protocol.claims.unsupported",
        "buyer.observable_problem",
        "buyer.present_state",
        "buyer.outcome_limits",
        "buyer.alternatives",
        "buyer.failed_attempts",
        "buyer.investment_conditions",
        "buyer.disqualifiers",
        "offer.name",
        "offer.scope",
        "offer.format",
        "offer.price_status",
        "offer.terms_status",
        "proof.source",
        "proof.practitioner",
        "proof.demand",
        "proof.delivery",
        "proof.outcome",
        "proof.repeatability",
        "proof.permissions.measurement",
        "proof.permissions.quotation",
        "proof.permissions.anonymization",
        "proof.permissions.reuse",
        "stage.proof_stage",
        "stage.requested_next_stage",
        "capacity.available_hours_per_week",
        "capacity.working_weeks",
        "capacity.delivery_hours_per_unit",
        "capacity.support_hours_per_unit",
        "capacity.concurrency",
        "capacity.sales_call_limit",
        "capacity.life_constraints",
        "capacity.margin_floor",
        "acquisition.primary_path",
        "acquisition.secondary_paths",
        "actuals.sent",
        "actuals.held",
        "actuals.sold",
        "actuals.collected",
        "actuals.delivered_units",
        "economics.requested_model",
        "authorization.requested_result",
        "authorization.authorized_local_outputs",
        "authorization.forbidden_external_actions",
        "authorization.provenance",
    ]
    if any(get_path(packet, path) is None for path in required_paths):
        add_error(errors, "E_INPUT_REQUIRED_FIELD_MISSING")

    claims = get_path(packet, "protocol.claims.allowed") or []
    claim_text = text_blob(claims)
    credential_text = text_blob(get_path(packet, "practitioner.credentials") or [])
    if re.search(r"\b(treat|diagnose|cure)\b.*\b(depression|anxiety|trauma|disorder)\b", claim_text):
        clinical_credential = re.search(
            r"\blicensed\b.{0,40}\b(clinical|therapist|psychologist|physician|counselor)\b"
            r"|\b(clinical psychologist|clinical social worker|licensed therapist|licensed counselor|physician)\b",
            credential_text,
        )
        if not clinical_credential:
            add_error(errors, "E_SCOPE_HIGH_STAKES_UNCLEARED")

    if is_generic(
        get_path(packet, "buyer.specific_buyer"),
        {"people who want a better life", "everyone", "anyone", "people", "business owners"},
    ):
        add_error(errors, "E_ROUTE_BUYER_GENERIC")

    if is_generic(
        get_path(packet, "buyer.desired_state"),
        {"become your best self", "be successful", "improve your life", "grow your business"},
    ):
        add_error(errors, "E_ROUTE_OUTCOME_NONOBSERVABLE")

    desired = str(get_path(packet, "buyer.desired_state") or "").lower()
    protocol_name = str(get_path(packet, "protocol.name") or "").lower()
    if re.search(r"six[- ]figure|revenue|business in 90 days", desired) and "life" in protocol_name:
        add_error(errors, "E_ROUTE_PROTOCOL_PROMISE_MISMATCH")

    paid_gate = get_path(packet, "offer.paid_event_gate")
    price = get_path(packet, "offer.price")
    if paid_gate in (None, "", "UNKNOWN") or price in (None, "", "$0", 0):
        add_error(errors, "E_OFFER_PAID_UNIT_UNDEFINED")

    sold = dated_events(packet, "sold")
    collected = dated_events(packet, "collected")
    if any(event.get("kind") != "sale" for event in sold):
        add_error(errors, "E_PROOF_INTERVIEW_AS_SALE")
    if any(not isinstance(event.get("amount"), (int, float)) or event.get("amount", 0) <= 0 for event in collected):
        add_error(errors, "E_PROOF_FREE_AS_PAID")

    today = dt.date.today()
    for key in ("sent", "held", "sold", "collected", "delivered_units"):
        for event in dated_events(packet, key):
            try:
                if dt.date.fromisoformat(str(event.get("date"))) > today:
                    add_error(errors, "E_PROOF_FUTURE_EVENT_INFLATION")
            except ValueError:
                add_error(errors, "E_PROOF_EVENT_DATE_INVALID")

    for outcome in get_path(packet, "proof.outcome") or []:
        if str(outcome.get("evidence_class", "")).upper() == "SOURCE_REPORTED" or outcome.get("source_video_id"):
            add_error(errors, "E_PROOF_SOURCE_AS_CLIENT_OUTCOME")

    if re.search(r"\bguarantee(?:d)?\b|six[- ]figure.*(?:90 days|guarantee)", claim_text):
        add_error(errors, "E_CLAIM_UNSUPPORTED_GUARANTEE")

    secondary = get_path(packet, "acquisition.secondary_paths") or []
    if any(not isinstance(item, dict) or item.get("status") == "ACTIVE" for item in secondary):
        add_error(errors, "E_ROUTE_MULTIPLE_ACQUISITION_PATHS")

    stage = get_path(packet, "stage.proof_stage")
    delivered = dated_events(packet, "delivered_units")
    if stage not in STAGES:
        add_error(errors, "E_STAGE_ENUM_INVALID")
    elif stage != "STAGE_0_PAID_PROOF" and len(delivered) < 3:
        add_error(errors, "E_STAGE_PROOF_INFLATION")

    provenance = get_path(packet, "authorization.provenance")
    if provenance not in PROVENANCE:
        add_error(errors, "E_PROVENANCE_INVALID")

    if len(collected) > len(sold) or len(sold) > len(dated_events(packet, "held")):
        add_error(errors, "E_PROOF_COUNTER_SEQUENCE_INVALID")

    return errors


def valid_runtime_receipt(
    runtime_receipt: dict[str, Any] | None,
    packet_hash: str,
    actual_hash: str,
) -> bool:
    if not runtime_receipt:
        return False
    return all(
        [
            runtime_receipt.get("provenance") == "RUNTIME_OBSERVED",
            runtime_receipt.get("detached") is True,
            runtime_receipt.get("input_sha256") == packet_hash,
            runtime_receipt.get("actual_sha256") == actual_hash,
        ]
    )


def verify(
    packet: dict[str, Any],
    actual: dict[str, Any],
    acceptance: dict[str, Any],
    runtime_receipt: dict[str, Any] | None = None,
) -> dict[str, Any]:
    errors = validate_packet(packet)
    packet_hash = sha256(packet)
    actual_hash = sha256(actual)
    acceptance_hash = sha256(acceptance)

    lane_owner = actual.get("selected_lane_owner")
    if not isinstance(lane_owner, str):
        add_error(errors, "E_ROUTE_MULTIPLE_LANE_OWNERS")
    elif lane_owner != acceptance.get("expected_lane_owner"):
        add_error(errors, "E_ROUTE_LANE_PAYLOAD_LEAK")

    expected_fields = {
        "practice_type": "expected_practice_type",
        "proof_stage": "expected_proof_stage",
        "next_stage": "expected_next_stage",
        "active_public_offer": "expected_public_offer",
        "terminal_decision": "expected_terminal_decision",
        "terminal_reason_code": "expected_terminal_reason_code",
        "economics_status": "expected_economics_status",
    }
    for actual_key, expected_key in expected_fields.items():
        if actual.get(actual_key) != acceptance.get(expected_key):
            add_error(errors, "E_ROUTE_FIELD_MISMATCH")

    if actual.get("practice_type") not in PRACTICE_TYPES:
        add_error(errors, "E_ROUTE_PRACTICE_ENUM_INVALID")
    if actual.get("proof_stage") not in STAGES or actual.get("next_stage") not in STAGES:
        add_error(errors, "E_STAGE_ENUM_INVALID")
    if actual.get("terminal_decision") not in TERMINALS:
        add_error(errors, "E_TERMINAL_ENUM_INVALID")

    if actual.get("function_owners") != acceptance.get("expected_function_owners"):
        add_error(errors, "E_ROUTE_FUNCTION_OWNER_MISMATCH")
    if set(actual.get("selected_workflow_paths", [])) != set(acceptance.get("expected_workflow_paths", [])):
        add_error(errors, "E_ROUTE_WORKFLOW_MISMATCH")

    loaded = actual.get("loaded_context_paths", [])
    if set(loaded) != set(acceptance.get("expected_loaded_context_paths", [])):
        add_error(errors, "E_CONTEXT_EXPERT_SOUP")

    forbidden_owners = set(acceptance.get("forbidden_owner_paths", []))
    if (isinstance(lane_owner, str) and lane_owner in forbidden_owners) or forbidden_owners.intersection(loaded):
        add_error(errors, "E_ROUTE_LANE_PAYLOAD_LEAK")

    components = {str(item).lower() for item in actual.get("delivery_components", [])}
    forbidden_components = {str(item).lower() for item in acceptance.get("forbidden_delivery_components", [])}
    if components.intersection(forbidden_components):
        add_error(errors, "E_DELIVERY_FORCED_COMMUNITY")

    if actual.get("proof_reuse_requested") is True and get_path(packet, "proof.permissions.reuse") == "NO_PERMISSION":
        add_error(errors, "E_PROOF_PERMISSION_VIOLATION")

    if actual.get("economics_status") != "LOCKED_PRE_RUNTIME" or actual.get("economics_model") is not None:
        add_error(errors, "E_ECON_PREMATURE_OUTPUT")

    if actual.get("external_actions_taken"):
        add_error(errors, "E_ACTION_UNAUTHORIZED_EXTERNAL")

    route_provenance = actual.get("provenance")
    runtime_ok = valid_runtime_receipt(runtime_receipt, packet_hash, actual_hash)
    if route_provenance not in PROVENANCE:
        add_error(errors, "E_PROVENANCE_INVALID")
    elif route_provenance == "RUNTIME_OBSERVED" and not runtime_ok:
        add_error(errors, "E_PROVENANCE_SELF_DECLARED_RUNTIME")

    declared_registration = actual.get("registration_eligible") is True
    human_registration_approval = bool(runtime_receipt and runtime_receipt.get("human_registration_approval") is True)
    if declared_registration and not (runtime_ok and human_registration_approval):
        add_error(errors, "E_REGISTRATION_PREMATURE")

    expected_counts = {
        "sent": len(dated_events(packet, "sent")),
        "held": len(dated_events(packet, "held")),
        "sold": len(dated_events(packet, "sold")),
        "collected": len(dated_events(packet, "collected")),
        "delivered_units": len(dated_events(packet, "delivered_units")),
    }
    if actual.get("truth_counters") != expected_counts:
        add_error(errors, "E_PROOF_COUNTER_MISMATCH")

    registration_eligible = bool(not errors and runtime_ok and human_registration_approval)
    economics_eligible = bool(
        registration_eligible
        and runtime_receipt
        and runtime_receipt.get("economics_build_approval") is True
        and actual.get("proof_stage") != "STAGE_0_PAID_PROOF"
    )

    return {
        "verifier": "expert-practice-os/verify_behavior_run.py",
        "verifier_status": "PASS" if not errors else "FAIL",
        "fixture_id": packet.get("fixture_id"),
        "input_sha256": packet_hash,
        "actual_sha256": actual_hash,
        "acceptance_sha256": acceptance_hash,
        "provenance_observed": route_provenance,
        "runtime_receipt_valid": runtime_ok,
        "registration_eligible": registration_eligible,
        "economics_eligible": economics_eligible,
        "terminal_decision_observed": actual.get("terminal_decision"),
        "terminal_reason_observed": actual.get("terminal_reason_code"),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify an Expert Practice OS behavior artifact.")
    parser.add_argument("--packet", required=True)
    parser.add_argument("--actual", required=True)
    parser.add_argument("--acceptance", required=True)
    parser.add_argument("--runtime-receipt")
    args = parser.parse_args()

    receipt = verify(
        load_json(args.packet),
        load_json(args.actual),
        load_json(args.acceptance),
        load_json(args.runtime_receipt) if args.runtime_receipt else None,
    )
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["verifier_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
