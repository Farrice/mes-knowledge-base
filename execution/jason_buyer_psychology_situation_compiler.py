#!/usr/bin/env python3
"""Cold, structured selector for the buyer-psychology mechanism registry.

This compiler deliberately does not infer psychology from free text. It accepts
an explicit Buyer Reality Ledger, applies truth/safety precedence, selects the
earliest observed material friction, and returns a bounded change brief to the
native function owner. Candidate cards are selectable only in development mode.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = (
    ROOT
    / "extractions/jason-fladlien/buyer-psychology-intelligence-layer"
    / "mechanism-registry.json"
)
CANONICAL_REGISTRY_SHA256 = "e055c2e6663f656bde6b6c2d449a623042dd792c7f0430db2d32cb11fe2fd4b7"

ABSTAIN_CLASSES = {
    "neutral-summary",
    "technical-specification",
    "code",
    "evidence-ledger",
    "mechanical-edit",
    "high-stakes-evidence",
}

HIGH_STAKES_ARTIFACT_TOKENS = {
    "medical",
    "health",
    "healthcare",
    "clinical",
    "pharma",
    "supplement",
    "legal",
    "financial",
    "finance",
    "employment",
    "housing",
    "insurance",
    "credit",
    "mortgage",
    "fintech",
    "banking",
    "investment",
    "tax",
}

TRUTH_GAP_ROUTES = (
    ({"unsupported-claim", "missing-proof", "claim-safety"}, "GET_PROOF"),
    ({"broken-offer", "poor-fit", "undefined-capacity"}, "FIX_OFFER"),
    ({"unclear-terms", "hidden-terms", "missing-disclosure"}, "CLARIFY_TERMS"),
    ({"delivery-failure", "performance-gap", "blocked-remedy"}, "IMPROVE_DELIVERY"),
)
ALLOWED_TRUTH_GAPS = frozenset().union(*(codes for codes, _ in TRUTH_GAP_ROUTES))

ALLOWED_BUYER_EVIDENCE = {"OBSERVED", "SUPPORTED", "UNKNOWN"}
ALLOWED_RISK_DOMAINS = {"STANDARD", "HIGH_STAKES"}
ALLOWED_CARD_STATUSES = {"SHADOW", "CANDIDATE"}
REQUIRED_CARD_STRING_FIELDS = {
    "card_id",
    "decision",
    "journey_stage",
    "status",
    "native_owner",
    "decision_job",
    "practitioner_source",
    "smallest_intervention",
    "risk_veto",
}

# The compiler diagnoses and hands off; it never becomes the craft owner.  The
# map is deliberately decision-specific so an arbitrary expert name cannot be
# injected into an otherwise valid intervention receipt.
ALLOWED_NATIVE_OWNERS: dict[str, frozenset[str]] = {
    "Belief": frozenset({"/copy-engine", "/farrice-content-os", "Selected Writing Owner"}),
    "Focus": frozenset({"Selected Writing Owner", "/farrice-content-os", "/copy-engine"}),
    "Recognition": frozenset({"/farrice-content-os", "Selected Writing Owner", "/copy-engine"}),
    "Priority": frozenset({"/farrice-content-os", "Selected Writing Owner", "Selected Client Delivery Owner"}),
    "Fit": frozenset({"/revenue-offer-agent", "/campaign-architect", "Selected Campaign Owner"}),
    "Choice": frozenset({"/revenue-offer-agent", "/campaign-architect", "Selected Campaign Owner"}),
    "Congruence": frozenset({"/campaign-architect", "Selected Campaign Owner", "/copy-engine", "/revenue-offer-agent", "Selected Writing Owner"}),
    "Affect": frozenset({"/copy-engine", "/farrice-content-os"}),
    "Evidence": frozenset({"/research-intelligence-agent", "Selected Proof Owner", "/copy-engine", "Selected Campaign Owner"}),
    "Agency": frozenset({"Qualified Sales Conversation Owner", "/copy-engine", "/revenue-offer-agent"}),
    "Value": frozenset({"/revenue-offer-agent"}),
    "Action": frozenset({"Selected Native Function Owner", "Selected Client Delivery Owner", "Selected Campaign Owner", "/copy-engine", "Qualified Sales Conversation Owner"}),
    "Experience": frozenset({"Selected Client Delivery Owner", "/revenue-offer-agent"}),
}


class CompilerInputError(ValueError):
    """Raised when the structured ledger is malformed."""


def load_registry(path: Path = DEFAULT_REGISTRY) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cards = data.get("cards")
    if not isinstance(cards, list) or not cards:
        raise CompilerInputError("registry must contain a non-empty cards list")
    seen_card_ids: set[str] = set()
    seen_decisions: set[str] = set()
    for index, card in enumerate(cards):
        if not isinstance(card, dict):
            raise CompilerInputError(f"registry card {index} must be an object")
        missing = sorted(REQUIRED_CARD_STRING_FIELDS - set(card))
        if missing:
            raise CompilerInputError(
                f"registry card {index} missing required fields: {', '.join(missing)}"
            )
        for field in REQUIRED_CARD_STRING_FIELDS:
            if not isinstance(card[field], str) or not card[field].strip():
                raise CompilerInputError(
                    f"registry card {index} field {field} must be a nonblank string"
                )
        if card["status"] not in ALLOWED_CARD_STATUSES:
            raise CompilerInputError(
                f"registry card {index} status must be SHADOW or CANDIDATE"
            )
        if card["decision"] not in ALLOWED_NATIVE_OWNERS:
            raise CompilerInputError(
                f"registry card {index} has an unknown decision: {card['decision']}"
            )
        if card["native_owner"] not in ALLOWED_NATIVE_OWNERS[card["decision"]]:
            raise CompilerInputError(
                f"registry card {index} has a disallowed default owner"
            )
        if not isinstance(card.get("journey_order"), int):
            raise CompilerInputError(
                f"registry card {index} journey_order must be an integer"
            )
        activation_codes = card.get("activation_codes")
        if (
            not isinstance(activation_codes, list)
            or not activation_codes
            or any(not isinstance(code, str) or not code.strip() for code in activation_codes)
        ):
            raise CompilerInputError(
                f"registry card {index} activation_codes must be nonblank strings"
            )
        if card["card_id"] in seen_card_ids or card["decision"] in seen_decisions:
            raise CompilerInputError("registry card ids and decisions must be unique")
        seen_card_ids.add(card["card_id"])
        seen_decisions.add(card["decision"])
    return data


def _base_receipt(case: dict[str, Any], development: bool) -> dict[str, Any]:
    return {
        "caseId": case.get("case_id", "UNSPECIFIED"),
        "mode": "DEVELOPMENT_ONLY" if development else "COLD_SHADOW",
        "promotionEligible": False,
        "runtimeMode": "COLD_SHADOW",
        "marketEvent": "NO EVENT",
        "decision": None,
        "primary": None,
        "support": [],
        "route": "",
        "nativeOwner": None,
        "compilerAuthoredFinal": False,
        "loadedCards": [],
        "loadedSourceSlices": [],
        "preservationPass": True,
        "evidenceClass": "STRUCTURALLY_VALIDATED",
        "outcomeClass": "CRAFT_PREFERENCE_ONLY",
        "counterconditionChecked": False,
        "smallestIntervention": None,
        "riskVeto": None,
        "remainingProofGap": "No human preference, buyer behavior, sale, collection, retention, conversion, or causal event.",
        "reason": "",
        "warnings": [],
        "questionsAdded": 0,
        "changesProposed": 0,
        "blocksAdded": 0,
    }


def _finish(receipt: dict[str, Any], route: str, reason: str) -> dict[str, Any]:
    receipt["route"] = route
    receipt["decision"] = route
    receipt["reason"] = reason
    return receipt


def _validate_case(case: dict[str, Any]) -> None:
    if not isinstance(case, dict):
        raise CompilerInputError("input must be a JSON object")
    for key in (
        "case_id",
        "artifact_class",
        "receiver_outcome",
        "material_decision",
        "persuasion_permitted",
        "risk_domain",
        "buyer_evidence",
        "requires_buyer_interpretation",
        "truth_gaps",
        "unsafe_requests",
        "observed_friction_codes",
    ):
        if key not in case:
            raise CompilerInputError(f"missing required field: {key}")
    if not isinstance(case["material_decision"], bool):
        raise CompilerInputError("material_decision must be boolean")
    for key in ("persuasion_permitted", "requires_buyer_interpretation", "handoff_required"):
        if key in case and not isinstance(case[key], bool):
            raise CompilerInputError(f"{key} must be boolean")
    for key in ("case_id", "artifact_class", "receiver_outcome"):
        if not isinstance(case[key], str) or not case[key].strip():
            raise CompilerInputError(f"{key} must be a nonblank string")
    for key in ("truth_gaps", "unsafe_requests", "observed_friction_codes"):
        if not isinstance(case[key], list):
            raise CompilerInputError(f"{key} must be a list")
        if any(not isinstance(item, str) or not item.strip() for item in case[key]):
            raise CompilerInputError(f"{key} entries must be nonblank strings")
    normalized_truth_gaps = {
        item.strip().casefold() for item in case["truth_gaps"]
    }
    unknown_truth_gaps = sorted(normalized_truth_gaps - ALLOWED_TRUTH_GAPS)
    if unknown_truth_gaps:
        raise CompilerInputError(
            f"unknown truth_gaps fail closed: {', '.join(unknown_truth_gaps)}"
        )
    if "support_friction_code" in case and (
        not isinstance(case["support_friction_code"], str)
        or not case["support_friction_code"].strip()
    ):
        raise CompilerInputError("support_friction_code must be a nonblank string")
    if not isinstance(case["buyer_evidence"], str):
        raise CompilerInputError("buyer_evidence must be a string enum")
    buyer_evidence = case["buyer_evidence"].strip().upper()
    if buyer_evidence not in ALLOWED_BUYER_EVIDENCE:
        allowed = ", ".join(sorted(ALLOWED_BUYER_EVIDENCE))
        raise CompilerInputError(f"buyer_evidence must be one of: {allowed}")
    if not isinstance(case["risk_domain"], str):
        raise CompilerInputError("risk_domain must be a string enum")
    risk_domain = case["risk_domain"].strip().upper().replace("-", "_")
    if risk_domain not in ALLOWED_RISK_DOMAINS:
        allowed = ", ".join(sorted(ALLOWED_RISK_DOMAINS))
        raise CompilerInputError(f"risk_domain must be one of: {allowed}")


def compile_case(
    case: dict[str, Any],
    *,
    development: bool = False,
    registry_path: Path = DEFAULT_REGISTRY,
) -> dict[str, Any]:
    """Compile one structured Buyer Reality Ledger into a bounded decision receipt."""

    _validate_case(case)
    try:
        canonical_registry = Path(registry_path).resolve() == DEFAULT_REGISTRY.resolve()
    except TypeError:
        canonical_registry = False
    if not canonical_registry and not development:
        raise CompilerInputError(
            "custom registries are allowed only in explicit development mode"
        )
    if canonical_registry:
        registry_sha256 = hashlib.sha256(DEFAULT_REGISTRY.read_bytes()).hexdigest()
        if registry_sha256 != CANONICAL_REGISTRY_SHA256:
            raise CompilerInputError(
                "canonical registry hash drifted; verify and deliberately update the trust anchor"
            )
    registry = load_registry(registry_path)
    cards = registry["cards"]
    receipt = _base_receipt(case, development)
    if not canonical_registry:
        receipt["evidenceClass"] = "DEVELOPMENT_UNTRUSTED_REGISTRY"
        receipt["warnings"].append(
            "custom registry is development-only and carries no canonical runtime authority"
        )

    unsafe_requests = [str(item) for item in case.get("unsafe_requests", []) if str(item)]
    if unsafe_requests:
        receipt["preservationPass"] = False
        receipt["riskVeto"] = "; ".join(unsafe_requests)
        return _finish(
            receipt,
            "REJECT_UNSAFE",
            "The requested move would weaken truth, evidence, informed choice, safety, or delivery integrity.",
        )

    if case.get("do_not_advance_reason"):
        receipt["riskVeto"] = str(case["do_not_advance_reason"])
        return _finish(receipt, "DO_NOT_ADVANCE", str(case["do_not_advance_reason"]))

    if case.get("handoff_required"):
        owner = str(case.get("handoff_owner") or "qualified native owner")
        receipt["nativeOwner"] = owner
        return _finish(receipt, "HAND_OFF", f"This decision belongs to {owner} before persuasion or craft.")

    artifact_class = case["artifact_class"].strip().casefold()
    persuasion_permitted = case["persuasion_permitted"]
    risk_domain = case["risk_domain"].strip().upper().replace("-", "_")
    # Treat punctuation and whitespace as equivalent boundaries.  The compact
    # fallback catches routine type drift such as ``medicalcopy`` without
    # granting intervention merely because a delimiter disappeared.
    artifact_tokens = set(re.findall(r"[a-z0-9]+", artifact_class))
    artifact_compact = re.sub(r"[^a-z0-9]", "", artifact_class)
    compact_high_stakes = any(
        artifact_compact.startswith(token)
        for token in HIGH_STAKES_ARTIFACT_TOKENS
    )
    if (
        artifact_class in ABSTAIN_CLASSES
        or risk_domain == "HIGH_STAKES"
        or bool(artifact_tokens & HIGH_STAKES_ARTIFACT_TOKENS)
        or compact_high_stakes
        or not persuasion_permitted
    ):
        return _finish(
            receipt,
            "ABSTAIN",
            "This artifact is neutral, mechanical, evidence-led, high-stakes, or outside the permission boundary.",
        )

    receiver_outcome = case["receiver_outcome"].strip().casefold()
    if not case["material_decision"] or receiver_outcome in {"none", "record", "mechanical"}:
        return _finish(receipt, "ABSTAIN", "No material human decision can change.")

    truth_gaps = {str(item).strip().casefold() for item in case.get("truth_gaps", []) if str(item).strip()}
    for gap_set, route in TRUTH_GAP_ROUTES:
        matched = sorted(truth_gaps & gap_set)
        if matched:
            return _finish(
                receipt,
                route,
                f"Truth or delivery repair precedes psychology: {', '.join(matched)}.",
            )

    buyer_evidence = case["buyer_evidence"].strip().upper()
    if case.get("requires_buyer_interpretation", False) and buyer_evidence == "UNKNOWN":
        return _finish(
            receipt,
            "GET_BUYER_EVIDENCE",
            "The proposed interpretation requires buyer evidence that is not present.",
        )

    by_code: dict[str, dict[str, Any]] = {}
    for card in cards:
        for code in card["activation_codes"]:
            if code in by_code:
                raise CompilerInputError(f"duplicate activation code in registry: {code}")
            by_code[code] = card

    observed_codes = [
        str(item).strip().casefold()
        for item in case.get("observed_friction_codes", [])
        if str(item).strip()
    ]
    matched_cards = {by_code[code]["card_id"]: by_code[code] for code in observed_codes if code in by_code}
    unknown_codes = sorted(set(observed_codes) - set(by_code))
    if unknown_codes:
        receipt["warnings"].append(f"unknown friction codes ignored: {', '.join(unknown_codes)}")
    if not matched_cards:
        return _finish(receipt, "ABSTAIN", "No registered observable friction is present.")

    primary = min(matched_cards.values(), key=lambda item: (item["journey_order"], item["decision"]))
    receipt["riskVeto"] = primary["risk_veto"]

    if primary["status"] == "CANDIDATE" and not development:
        receipt["primary"] = primary["decision"]
        receipt["loadedCards"] = [primary["card_id"]]
        return _finish(
            receipt,
            "HAND_OFF",
            f"{primary['decision']} is a cold candidate and is not admitted to runtime selection.",
        )

    countercondition = case.get("countercondition_check")
    countercondition_evidence = (
        countercondition.get("evidence") if isinstance(countercondition, dict) else None
    )
    if (
        not isinstance(countercondition, dict)
        or countercondition.get("passed") is not True
        or not isinstance(countercondition_evidence, str)
        or not countercondition_evidence.strip()
    ):
        return _finish(
            receipt,
            "ABSTAIN",
            "The selected card's countercondition was not explicitly cleared with evidence.",
        )
    preservation_locks = case.get("preservation_locks")
    if not isinstance(preservation_locks, list) or not preservation_locks:
        return _finish(receipt, "ABSTAIN", "No explicit preservation lock was supplied.")
    if not all(isinstance(item, str) for item in preservation_locks):
        return _finish(receipt, "ABSTAIN", "Every preservation lock must be a nonblank string.")
    normalized_locks = [item.strip() for item in preservation_locks]
    if any(not item for item in normalized_locks):
        return _finish(receipt, "ABSTAIN", "Blank preservation locks do not authorize an intervention.")
    if len({item.casefold() for item in normalized_locks}) != len(normalized_locks):
        return _finish(receipt, "ABSTAIN", "Preservation locks must be unique.")

    receipt["counterconditionChecked"] = True

    requested_owner = str(case.get("native_owner") or primary["native_owner"]).strip()
    allowed_owners = ALLOWED_NATIVE_OWNERS.get(primary["decision"], frozenset())
    if requested_owner not in allowed_owners:
        receipt["primary"] = primary["decision"]
        receipt["loadedCards"] = [primary["card_id"]]
        return _finish(
            receipt,
            "HAND_OFF",
            f"{primary['decision']} requires an allowed native function owner before intervention.",
        )

    receipt["primary"] = primary["decision"]
    receipt["route"] = "INTERVENE"
    receipt["decision"] = "INTERVENE"
    receipt["nativeOwner"] = requested_owner
    receipt["loadedCards"] = [primary["card_id"]]
    receipt["loadedSourceSlices"] = [primary["practitioner_source"]]
    receipt["smallestIntervention"] = primary["smallest_intervention"]
    receipt["reason"] = primary["decision_job"]
    receipt["changesProposed"] = 1

    support_code = case.get("support_friction_code")
    if support_code:
        normalized_support_code = str(support_code).strip().casefold()
        support = by_code.get(normalized_support_code)
        if support is None:
            receipt["warnings"].append(f"unknown support code rejected: {normalized_support_code}")
        elif support["decision"] == primary["decision"] or support["journey_stage"] == primary["journey_stage"]:
            receipt["warnings"].append("support rejected because it does not own a distinct decision stage")
        elif support["status"] == "CANDIDATE" and not development:
            receipt["warnings"].append("cold candidate support rejected outside development mode")
        elif requested_owner not in ALLOWED_NATIVE_OWNERS.get(support["decision"], frozenset()):
            receipt["warnings"].append(
                "support rejected because the primary native owner is not allowed for that decision"
            )
        else:
            support_check = case.get("support_countercondition_check")
            support_evidence = (
                support_check.get("evidence") if isinstance(support_check, dict) else None
            )
            if (
                not isinstance(support_check, dict)
                or support_check.get("passed") is not True
                or not isinstance(support_evidence, str)
                or not support_evidence.strip()
            ):
                receipt["warnings"].append("support rejected because its countercondition was not cleared")
            else:
                receipt["support"] = [support["decision"]]
                receipt["loadedCards"].append(support["card_id"])
                receipt["loadedSourceSlices"].append(support["practitioner_source"])

    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile a structured buyer-reality ledger into a cold psychology decision receipt."
    )
    parser.add_argument("--input", required=True, type=Path, help="JSON input file")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--development", action="store_true", help="Permit cold CANDIDATE cards for development fixtures")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    case = json.loads(args.input.read_text(encoding="utf-8"))
    receipt = compile_case(case, development=args.development, registry_path=args.registry)
    print(json.dumps(receipt, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
