#!/usr/bin/env python3
"""Verify the cold Sales and Buyer Psychology Mastery development layer."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from build_jason_canonical_admission_map import build as build_admission_map
from jason_buyer_psychology_runtime_surface import (
    COLD_RUNTIME_MARKERS,
    active_runtime_paths,
    overlay_pointer_paths,
    promotion_violations,
    runtime_payloads,
    runtime_policy_attestation,
    runtime_surface_digest,
)


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer"
REGISTRY = BASE / "mechanism-registry.json"
ADMISSION = BASE / "canonical-admission-map.json"
FIXTURES = BASE / "development-fixtures.json"
MAPPING = BASE / "development-expected-mapping.json"
BLIND_PACKETS = BASE / "development-blind-packets.json"
BLIND_MAPPING = BASE / "development-blind-mapping.json"
EVALUATOR_RECEIPTS = BASE / "development-evaluator-receipts.json"
RUN_RECEIPT = BASE / "canonical-verification-receipt.json"
BENCHMARK_SUMMARY = BASE / "development-benchmark.md"
COMPILER = ROOT / "execution/jason_buyer_psychology_situation_compiler.py"
OVERLAY = ROOT / "semantic_libraries/antigravity/primitives/buyer-psychology-decision-intelligence-overlay.md"
JASON_SKILL = ROOT / "skills/jason-fladlien-marketing/SKILL.md"
WORKFLOW_ROOT = ROOT / "skills/jason-fladlien-marketing/workflows"
PROMPT_ROOT = ROOT / "skills/jason-fladlien-marketing/references/prompts"
PROMPT_V2_ROOT = ROOT / "skills/jason-fladlien-marketing/references/prompts-v2"
LEGACY_PROMPT_ROOT = ROOT / "skills/jason-fladlien-marketing/references/_legacy-prompts"

METADATA_RELATIVE_PATHS = (
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/amplification-report.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/architecture.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/behavior-proof.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/canonical-admission-map.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/canonical-deployment-receipt.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/development-behavior-proof.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/development-benchmark.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/implementation-receipt.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/legacy-admission-map.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/mastery-benchmark-protocol.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/mastery-expansion-receipt.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/mechanism-card-template.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/mechanism-registry.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/sales-psychology-mastery-blueprint.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/situation-compiler-contract.md.metadata.json",
    "extractions/jason-fladlien/buyer-psychology-intelligence-layer/source-corpus-index.md.metadata.json",
)

ALLOWED_OVERLAY_POINTERS = {
    ".agent/workflows/campaign-architect.md",
    ".agent/workflows/copy-engine.md",
    ".agent/workflows/farrice-content-os.md",
    ".agent/workflows/high-taste-writing-os.md",
    ".agent/workflows/revenue-offer-agent.md",
    "skills/jason-fladlien-marketing/SKILL.md",
}
EXPECTED_PROOF_GAP = "No human preference, buyer behavior, sale, collection, retention, conversion, or causal event."
EXPECTED_NO_EVENT_ASSERTIONS = {
    "humanPreferenceObserved": False,
    "productionReceiptObserved": False,
    "buyerBehaviorObserved": False,
    "saleObserved": False,
    "collectionObserved": False,
    "conversionClaimAuthorized": False,
    "hotPromotionAuthorized": False,
}
ALLOWED_METADATA_MODES = {
    "SHADOW",
    "DEVELOPMENT_ONLY",
    "COLD_DEVELOPMENT",
    "COLD_CANDIDATE",
    "COLD_DEFENSIVE",
    "COLD_REFERENCE",
}

SHADOW_DECISIONS = {"Belief", "Focus", "Recognition", "Priority", "Fit", "Choice", "Congruence", "Affect"}
CANDIDATE_DECISIONS = {"Evidence", "Agency", "Value", "Action", "Experience"}
ALLOWED_ADMISSION = {"ADMIT", "DEFENSIVE-LITERACY-ONLY", "EXCLUDE-FROM-MASTER"}
REQUIRED_CARD_FIELDS = {
    "card_id", "decision", "journey_stage", "journey_order", "status", "native_owner",
    "optional_specialist", "decision_job", "activation_codes", "observable_activation_signals",
    "buyer_evidence_required", "forbidden_inferences", "earlier_weak_link", "practitioner_source",
    "source_observed_move", "independent_calibration", "evidence_status", "causal_limit",
    "smallest_intervention", "countercondition", "risk_veto", "abstention_or_handoff",
    "preservation_lock", "forbidden_uses", "receipt_outcome_class", "review_or_quarantine_trigger",
}

# The verifier holds one non-self-referential trust anchor. The receipt in turn
# binds the exact source packages, human-facing layer documents, structured
# fixtures, canonical owner seams, skill pointer, compiler, and admission map.
# It is a local Git-backed receipt, not an external signature or market proof.
FROZEN_RECEIPT_SHA256 = "fa2059253807d77c51d37c43f839ab0624afd5583ca2ab30b8cbadf6a265190f"

SOURCE_IDS = (
    "jbPNjNtQqk0",
    "8U0BDpRnPFU",
    "nGZbkwKboVU",
    "ooGeFK70d5U",
    "H_TvNSNbRiU",
    "B90eANIJ2XI",
)

TRUST_STATIC_RELATIVE_PATHS = (
    ".agent/workflows/campaign-architect.md",
    ".agent/workflows/copy-engine.md",
    ".agent/workflows/farrice-content-os.md",
    ".agent/workflows/high-taste-writing-os.md",
    ".agent/workflows/revenue-offer-agent.md",
    "execution/build_jason_canonical_admission_map.py",
    "execution/context_retriever.py",
    "execution/finalize_sales_psychology_canonical_receipt.py",
    "execution/jason_buyer_psychology_runtime_surface.py",
    "execution/jason_buyer_psychology_situation_compiler.py",
    "execution/verify_jason_buyer_psychology_overlay.py",
    "semantic_libraries/antigravity/primitives/buyer-psychology-decision-intelligence-overlay.md",
    "skills/jason-fladlien-marketing/SKILL.md",
    "skills/jason-fladlien-marketing/references/buyer-psychology-decision-layer.md",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm_hash(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _canonical_context_chunks(chunks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Remove volatile IDs and produce a deterministic Jason chunk subset."""
    fields = ("source", "expert", "skill", "file_type", "section", "content", "word_count")
    canonical = [
        {field: chunk.get(field) for field in fields}
        for chunk in chunks
    ]
    canonical.sort(
        key=lambda chunk: (
            str(chunk.get("source")),
            str(chunk.get("section")),
            str(chunk.get("content")),
        )
    )
    return canonical


def _context_subset_hash(chunks: list[dict[str, Any]]) -> str:
    payload = json.dumps(chunks, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def jason_context_index_attestation() -> dict[str, Any]:
    """Bind cached Jason chunks to a fresh deterministic chunking of live files."""
    index = load_json(ROOT / "execution/skill_chunks.json")
    current = _canonical_context_chunks([
        chunk
        for chunk in index.get("chunks", [])
        if chunk.get("skill") == "jason-fladlien-marketing"
        or str(chunk.get("source", "")).startswith("skills/jason-fladlien-marketing/")
    ])

    retriever_path = ROOT / "execution/context_retriever.py"
    spec = importlib.util.spec_from_file_location("jason_context_retriever_attestation", retriever_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("context retriever could not be loaded for attestation")
    retriever = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(retriever)
    skill_dir = ROOT / "skills/jason-fladlien-marketing"
    expected_chunks: list[dict[str, Any]] = []
    for filename in retriever.retrieval_file_names(skill_dir):
        path = skill_dir / filename
        if path.is_file():
            expected_chunks.extend(retriever.chunk_skill_file(path))
    expected = _canonical_context_chunks(expected_chunks)

    return {
        "chunkCount": len(current),
        "subsetSha256": _context_subset_hash(current),
        "expectedChunkCount": len(expected),
        "expectedSubsetSha256": _context_subset_hash(expected),
        "matchesLiveSkill": current == expected,
    }


def active_routing_paths() -> list[Path]:
    return active_runtime_paths(ROOT)


def active_routing_digest(injected_surface: tuple[str, str] | None = None) -> tuple[str, list[tuple[str, str]]]:
    digest, _ = runtime_surface_digest(ROOT, injected_surface)
    payloads = [
        (relative, data.decode("utf-8", errors="replace"))
        for relative, data in runtime_payloads(ROOT, injected_surface)
    ]
    return digest, payloads


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_compiler():
    spec = importlib.util.spec_from_file_location("jason_psychology_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition: bool, code: str, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(f"{code}: {message}")


def trust_paths() -> list[Path]:
    paths = {ROOT / relative for relative in TRUST_STATIC_RELATIVE_PATHS}
    paths.update(path for path in BASE.iterdir() if path.is_file() and path != RUN_RECEIPT)
    for source_id in SOURCE_IDS:
        package = ROOT / "extractions/video-context" / source_id
        paths.update(path for path in package.rglob("*") if path.is_file())
    return sorted(paths, key=lambda path: str(path.relative_to(ROOT)))


def validate_frozen_files(failures: list[str]) -> None:
    require(bool(FROZEN_RECEIPT_SHA256), "receipt-trust-anchor", "frozen receipt hash is unset", failures)
    require(RUN_RECEIPT.is_file(), "receipt-missing", str(RUN_RECEIPT.relative_to(ROOT)), failures)
    if not RUN_RECEIPT.is_file():
        return
    require(sha256(RUN_RECEIPT) == FROZEN_RECEIPT_SHA256, "receipt-trust-anchor", "canonical receipt bytes changed", failures)
    receipt = load_json(RUN_RECEIPT)
    manifest = receipt.get("manifest_sha256", {})
    expected = {str(path.relative_to(ROOT)) for path in trust_paths()}
    require(set(manifest) == expected, "receipt-manifest-set", f"missing={sorted(expected-set(manifest))} extra={sorted(set(manifest)-expected)}", failures)
    for relative, expected_hash in manifest.items():
        path = ROOT / relative
        require(path.is_file(), "frozen-file-missing", relative, failures)
        if path.is_file():
            require(sha256(path) == expected_hash, "frozen-file-hash", relative, failures)


def metadata_payload_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if payload.get("userFacingSurface") != "rendered-conversation-document":
        errors.append("metadata-user-surface")
    if payload.get("sourceRole") != "persistence-copy":
        errors.append("metadata-source-role")
    if payload.get("externalExportRequested") is not False:
        errors.append("metadata-external-export")
    if payload.get("deploymentMode") not in ALLOWED_METADATA_MODES:
        errors.append("metadata-deployment-mode")
    if payload.get("promotionEligible") is not False:
        errors.append("metadata-promotion")
    if payload.get("marketEvent") != "NO EVENT":
        errors.append("metadata-market-event")
    if payload.get("runtimeAuthorityChanged") is not False:
        errors.append("metadata-runtime-authority")
    return errors


def validate_metadata_sidecars(failures: list[str]) -> None:
    actual = {str(path.relative_to(ROOT)) for path in BASE.glob("*.metadata.json")}
    expected = set(METADATA_RELATIVE_PATHS)
    require(actual == expected, "metadata-inventory", f"missing={sorted(expected-actual)} extra={sorted(actual-expected)}", failures)
    receipt_manifest = set(load_json(RUN_RECEIPT).get("manifest_sha256", {})) if RUN_RECEIPT.is_file() else set()
    require(expected <= receipt_manifest, "metadata-frozen-set", "one or more metadata sidecars are not hash anchored", failures)
    for relative in METADATA_RELATIVE_PATHS:
        path = ROOT / relative
        require(path.is_file(), "metadata-missing", relative, failures)
        if path.is_file():
            errors = metadata_payload_errors(load_json(path))
            require(not errors, "metadata-boundary", f"{relative}: {errors}", failures)


def validate_registry(registry: dict[str, Any], failures: list[str]) -> None:
    cards = registry.get("cards", [])
    require(registry.get("deployment_mode") == "COLD_DEVELOPMENT", "registry-mode", "must remain cold", failures)
    require(registry.get("runtime_authority_changed") is False, "registry-authority", "runtime authority changed", failures)
    require(len(cards) == 13, "registry-count", f"expected 13 cards, got {len(cards)}", failures)

    decisions = [card.get("decision") for card in cards]
    card_ids = [card.get("card_id") for card in cards]
    require(len(set(decisions)) == len(decisions), "registry-decision-unique", "duplicate decision", failures)
    require(len(set(card_ids)) == len(card_ids), "registry-card-id-unique", "duplicate card id", failures)
    require(set(decisions) == SHADOW_DECISIONS | CANDIDATE_DECISIONS, "registry-decision-set", str(decisions), failures)

    status_by_decision = {card.get("decision"): card.get("status") for card in cards}
    require(all(status_by_decision.get(item) == "SHADOW" for item in SHADOW_DECISIONS), "registry-shadow-status", str(status_by_decision), failures)
    require(all(status_by_decision.get(item) == "CANDIDATE" for item in CANDIDATE_DECISIONS), "registry-candidate-status", str(status_by_decision), failures)
    require(Counter(card.get("status") for card in cards) == Counter({"SHADOW": 8, "CANDIDATE": 5}), "registry-status-count", str(status_by_decision), failures)

    activation_codes: list[str] = []
    for card in cards:
        missing = REQUIRED_CARD_FIELDS - set(card)
        require(not missing, "registry-card-fields", f"{card.get('decision')}: {sorted(missing)}", failures)
        require(isinstance(card.get("activation_codes"), list) and len(card["activation_codes"]) == 1, "registry-activation-code", str(card.get("decision")), failures)
        activation_codes.extend(card.get("activation_codes", []))
        for field in ("decision_job", "buyer_evidence_required", "causal_limit", "smallest_intervention", "countercondition", "risk_veto"):
            require(bool(str(card.get(field, "")).strip()), "registry-card-content", f"{card.get('decision')}:{field}", failures)
        require(bool(card.get("preservation_lock")), "registry-preservation", str(card.get("decision")), failures)
        require(bool(card.get("forbidden_uses")), "registry-forbidden-use", str(card.get("decision")), failures)
        require("SOURCE-OBSERVED" not in card.get("evidence_status", []) or bool(card.get("practitioner_source")), "registry-source-anchor", str(card.get("decision")), failures)

    require(len(activation_codes) == len(set(activation_codes)), "registry-code-unique", "activation collision", failures)
    priority = next(card for card in cards if card["decision"] == "Priority")
    congruence = next(card for card in cards if card["decision"] == "Congruence")
    require("PRIMARY-CORROBORATED" not in priority["evidence_status"], "priority-overclaim", "Priority is SO+OS only", failures)
    require("PRIMARY-CORROBORATED" not in congruence["evidence_status"], "congruence-overclaim", "Congruence is SO+OS only", failures)


def validate_admission(admission: dict[str, Any], failures: list[str]) -> None:
    entries = admission.get("entries", [])
    actual_workflows = {str(path.relative_to(ROOT)) for path in WORKFLOW_ROOT.glob("*.md")}
    actual_prompts = {str(path.relative_to(ROOT)) for path in PROMPT_ROOT.glob("*.md")}
    actual_prompts_v2 = {str(path.relative_to(ROOT)) for path in PROMPT_V2_ROOT.glob("*.md")}
    actual = actual_workflows | actual_prompts | actual_prompts_v2
    mapped = {entry.get("path") for entry in entries}

    require(len(actual_workflows) == 38, "admission-workflow-count", str(len(actual_workflows)), failures)
    require(len(actual_prompts) == 26, "admission-prompt-count", str(len(actual_prompts)), failures)
    require(len(actual_prompts_v2) == 33, "admission-prompt-v2-count", str(len(actual_prompts_v2)), failures)
    require(len(entries) == 97, "admission-entry-count", str(len(entries)), failures)
    require(mapped == actual, "admission-exact-inventory", f"missing={sorted(actual-mapped)} extra={sorted(mapped-actual)}", failures)
    require(all(entry.get("status") in ALLOWED_ADMISSION for entry in entries), "admission-status", "invalid admission status", failures)
    require(Counter(entry.get("status") for entry in entries) == Counter({"ADMIT": 28, "DEFENSIVE-LITERACY-ONLY": 39, "EXCLUDE-FROM-MASTER": 30}), "admission-status-count", str(Counter(entry.get("status") for entry in entries)), failures)
    require(all(str(entry.get("safe_kernel", "")).strip() and str(entry.get("risk_anchor", "")).strip() for entry in entries), "admission-reason", "every entry needs kernel and anchor", failures)
    require(all(entry.get("review_state") == "CANONICAL-ADJUDICATED" for entry in entries), "admission-review-state", "every entry must be canonically adjudicated", failures)
    require(admission == build_admission_map(), "admission-builder-drift", "manifest differs from current canonical hashes or policy", failures)

    identical = 0
    for prompt in sorted(PROMPT_ROOT.glob("*.md")):
        counterpart = LEGACY_PROMPT_ROOT / prompt.name
        require(counterpart.is_file(), "legacy-counterpart", prompt.name, failures)
        if counterpart.is_file() and prompt.read_bytes() == counterpart.read_bytes():
            identical += 1
    require(identical == 26, "legacy-byte-duplicates", str(identical), failures)
    require(admission.get("summary", {}).get("legacy_duplicate_evidence_weight") == 0, "legacy-corroboration", "duplicates must add zero evidence", failures)


def validate_registry_default_owners(
    registry: dict[str, Any],
    compiler: Any,
    failures: list[str],
) -> None:
    for card in registry.get("cards", []):
        decision = card.get("decision")
        owner = card.get("native_owner")
        allowed = compiler.ALLOWED_NATIVE_OWNERS.get(decision, frozenset())
        require(
            owner in allowed,
            "registry-default-owner",
            f"{decision}: {owner!r} not in {sorted(allowed)}",
            failures,
        )


def validate_output(case: dict[str, Any], expected: dict[str, Any], output: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("route", "primary", "support", "nativeOwner"):
        if output.get(key) != expected.get(key):
            errors.append(f"mapping-{key}")
    if output.get("decision") != output.get("route"):
        errors.append("decision-route-mismatch")
    if output.get("caseId") != case.get("case_id"):
        errors.append("case-id-exact")
    if output.get("mode") != "DEVELOPMENT_ONLY":
        errors.append("mode-exact")
    if output.get("promotionEligible") is not False:
        errors.append("promotion-eligible")
    if output.get("runtimeMode") != "COLD_SHADOW":
        errors.append("runtime-mode")
    if output.get("marketEvent") != "NO EVENT":
        errors.append("market-event")
    if output.get("compilerAuthoredFinal") is not False:
        errors.append("compiler-authored-final")
    if output.get("evidenceClass") != "STRUCTURALLY_VALIDATED":
        errors.append("evidence-inflation")
    if output.get("outcomeClass") != "CRAFT_PREFERENCE_ONLY":
        errors.append("outcome-inflation")
    if output.get("remainingProofGap") != EXPECTED_PROOF_GAP:
        errors.append("remaining-proof-gap-exact")
    if output.get("questionsAdded") != 0:
        errors.append("question-burden")
    if output.get("blocksAdded") != 0:
        errors.append("block-burden")
    if output.get("warnings") != []:
        errors.append("warnings-exact")
    support = output.get("support", [])
    if not isinstance(support, list) or len(support) > 1:
        errors.append("support-cardinality")
    loaded = output.get("loadedCards", [])
    slices = output.get("loadedSourceSlices", [])
    if len(loaded) > 2 or len(slices) != len(loaded):
        errors.append("cold-load-boundary")
    if output.get("route") == "INTERVENE":
        primary_decision = output.get("primary")
        if not primary_decision:
            errors.append("missing-primary")
            primary_card = None
        else:
            cards = {
                card.get("decision"): card
                for card in load_json(REGISTRY).get("cards", [])
            }
            primary_card = cards.get(primary_decision)
            if primary_card is None:
                errors.append("unknown-primary-card")
        if output.get("counterconditionChecked") is not True:
            errors.append("countercondition")
        if output.get("changesProposed") != 1:
            errors.append("change-brief-count")
        if not case.get("preservation_locks"):
            errors.append("preservation-lock")
        if output.get("preservationPass") is not True:
            errors.append("preservation-pass")
        if primary_card is not None:
            cards_by_decision = {
                card.get("decision"): card
                for card in load_json(REGISTRY).get("cards", [])
            }
            support_cards = [
                cards_by_decision.get(decision)
                for decision in output.get("support", [])
            ]
            if any(card is None for card in support_cards):
                errors.append("unknown-support-card")
                support_cards = []
            expected_cards = [primary_card["card_id"]] + [card["card_id"] for card in support_cards]
            expected_slices = [primary_card["practitioner_source"]] + [
                card["practitioner_source"] for card in support_cards
            ]
            if output.get("loadedCards") != expected_cards:
                errors.append("loaded-cards-exact")
            if output.get("loadedSourceSlices") != expected_slices:
                errors.append("loaded-source-slices-exact")
            if output.get("smallestIntervention") != primary_card["smallest_intervention"]:
                errors.append("smallest-intervention-exact")
            if output.get("riskVeto") != primary_card["risk_veto"]:
                errors.append("risk-veto-exact")
            if output.get("reason") != primary_card["decision_job"]:
                errors.append("decision-job-exact")
    else:
        if output.get("changesProposed") != 0:
            errors.append("non-intervention-change")
        if output.get("loadedCards") or output.get("loadedSourceSlices"):
            errors.append("non-intervention-cold-load")
        if output.get("smallestIntervention") is not None:
            errors.append("non-intervention-smallest-change")
        if output.get("counterconditionChecked") is not False:
            errors.append("non-intervention-countercondition")
        expected_preservation = output.get("route") != "REJECT_UNSAFE"
        if output.get("preservationPass") is not expected_preservation:
            errors.append("non-intervention-preservation")
        route = output.get("route")
        expected_reason: str | None = None
        expected_risk: str | None = None
        if route == "REJECT_UNSAFE":
            expected_reason = "The requested move would weaken truth, evidence, informed choice, safety, or delivery integrity."
            expected_risk = "; ".join(case.get("unsafe_requests", []))
        elif route == "DO_NOT_ADVANCE":
            expected_reason = str(case.get("do_not_advance_reason"))
            expected_risk = expected_reason
        elif route == "HAND_OFF":
            owner = str(case.get("handoff_owner") or "qualified native owner")
            expected_reason = f"This decision belongs to {owner} before persuasion or craft."
        elif route == "GET_BUYER_EVIDENCE":
            expected_reason = "The proposed interpretation requires buyer evidence that is not present."
        elif route in {"GET_PROOF", "FIX_OFFER", "CLARIFY_TERMS", "IMPROVE_DELIVERY"}:
            normalized_gaps = sorted(str(item).strip().casefold() for item in case.get("truth_gaps", []))
            expected_reason = f"Truth or delivery repair precedes psychology: {', '.join(normalized_gaps)}."
        elif route == "ABSTAIN":
            expected_reason = (
                "No registered observable friction is present."
                if not case.get("observed_friction_codes")
                and case.get("material_decision")
                and case.get("persuasion_permitted")
                else "This artifact is neutral, mechanical, evidence-led, high-stakes, or outside the permission boundary."
            )
        if output.get("reason") != expected_reason:
            errors.append("non-intervention-reason-exact")
        if output.get("riskVeto") != expected_risk:
            errors.append("non-intervention-risk-veto-exact")
    if not str(output.get("reason", "")).strip():
        errors.append("reason-required")
    if case["case_id"].startswith("A"):
        if output.get("primary") is not None or output.get("support") != []:
            errors.append("abstention-card")
        if any(output.get(field) != 0 for field in ("questionsAdded", "changesProposed", "blocksAdded")):
            errors.append("abstention-burden")
    return errors


def validate_cases(registry: dict[str, Any], fixtures: dict[str, Any], mapping: dict[str, Any], compiler: Any, failures: list[str]) -> dict[str, dict[str, Any]]:
    cases = fixtures.get("cases", [])
    expected = mapping.get("expected", {})
    ids = [case.get("case_id") for case in cases]
    require(fixtures.get("mode") == "DEVELOPMENT_ONLY", "fixture-mode", "must be development only", failures)
    require(fixtures.get("promotionEligible") is False, "fixture-promotion", "must not be promotion eligible", failures)
    require(fixtures.get("marketEvent") == "NO EVENT", "fixture-market-event", "market event must remain NO EVENT", failures)
    require(len(cases) == 33, "fixture-count", str(len(cases)), failures)
    require(Counter(str(item)[0] for item in ids) == Counter({"P": 13, "A": 7, "R": 7, "X": 6}), "fixture-lanes", str(Counter(str(item)[0] for item in ids)), failures)
    require(len(ids) == len(set(ids)), "fixture-id-unique", "duplicate ids", failures)
    require(set(ids) == set(expected), "fixture-mapping-set", "mapping and fixture IDs differ", failures)
    normalized = [norm_hash(case.get("frozen_fixture", "")) for case in cases]
    require(len(normalized) == len(set(normalized)), "fixture-content-unique", "duplicate normalized fixture", failures)

    outputs: dict[str, dict[str, Any]] = {}
    for case in cases:
        case_id = case["case_id"]
        output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
        outputs[case_id] = output
        errors = validate_output(case, expected[case_id], output)
        require(not errors, "fixture-output", f"{case_id}: {errors}", failures)

    positive_decisions = [outputs[f"P{index:02d}"]["primary"] for index in range(1, 14)]
    require(set(positive_decisions) == SHADOW_DECISIONS | CANDIDATE_DECISIONS, "positive-card-coverage", str(positive_decisions), failures)
    require(len(positive_decisions) == len(set(positive_decisions)), "positive-card-once", str(positive_decisions), failures)
    require(outputs["P06"]["support"] == ["Fit"], "support-p06", str(outputs["P06"]), failures)
    require(sum(bool(outputs[f"P{index:02d}"]["support"]) for index in range(1, 14)) == 1, "support-only-once", "only P06 may use support", failures)

    # Candidate signals remain non-admitted outside explicit development mode.
    for case_id in ("P09", "P10", "P11", "P12", "P13"):
        case = next(case for case in cases if case["case_id"] == case_id)
        cold_output = compiler.compile_case(case, development=False, registry_path=REGISTRY)
        card = next(item for item in registry["cards"] if item["decision"] == outputs[case_id]["primary"])
        require(cold_output.get("route") == "HAND_OFF", "candidate-cold-gate", f"{case_id}: {cold_output.get('route')}", failures)
        require(
            cold_output.get("decision") == "HAND_OFF"
            and cold_output.get("primary") == card["decision"]
            and cold_output.get("loadedCards") == [card["card_id"]]
            and cold_output.get("loadedSourceSlices") == []
            and cold_output.get("nativeOwner") is None
            and cold_output.get("changesProposed") == 0
            and cold_output.get("preservationPass") is True,
            "candidate-cold-receipt",
            f"{case_id}: {cold_output}",
            failures,
        )

    return outputs


def validate_blind_packets(failures: list[str]) -> None:
    packets = load_json(BLIND_PACKETS)
    mapping = load_json(BLIND_MAPPING)
    cases = packets.get("cases", [])
    positions = mapping.get("treatment_positions", {})
    ids = [case.get("case_id") for case in cases]
    require(ids == ["D1", "D2", "D3", "D4", "D5", "D6"], "blind-case-set", str(ids), failures)
    require(set(ids) == set(positions), "blind-mapping-set", "packet and map differ", failures)
    require(Counter(positions.values()) == Counter({"A": 3, "B": 3}), "blind-position-balance", str(positions), failures)
    require(mapping.get("promotionEligible") is False, "blind-promotion", "model round cannot promote", failures)
    for case in cases:
        require(bool(case.get("source_facts")) and bool(case.get("preservation_locks")), "blind-locks", str(case.get("case_id")), failures)
        require(bool(case.get("version_a")) and bool(case.get("version_b")), "blind-versions", str(case.get("case_id")), failures)


def validate_receipts(failures: list[str]) -> None:
    receipts = load_json(EVALUATOR_RECEIPTS)
    blind_mapping = load_json(BLIND_MAPPING)["treatment_positions"]
    valid = receipts.get("valid", [])
    excluded = receipts.get("excludedDevelopmentEvaluations", [])
    require(receipts.get("mode") == "DEVELOPMENT_ONLY", "evaluator-mode", "not development only", failures)
    require(receipts.get("promotionEligible") is False, "evaluator-promotion", "model receipts cannot promote", failures)
    require(receipts.get("marketEvent") == "NO EVENT", "evaluator-market-event", "market event inflated", failures)
    require(receipts.get("runUuidAvailable") is False, "evaluator-uuid-truth", "runtime did not expose evaluator UUIDs", failures)
    require(len(valid) == 6, "evaluator-valid-count", str(len(valid)), failures)
    require({item.get("caseId") for item in valid} == set(blind_mapping), "evaluator-case-set", str(valid), failures)
    for item in valid:
        case_id = item["caseId"]
        require(item.get("treatmentPosition") == blind_mapping[case_id], "evaluator-position", case_id, failures)
        require(item.get("winner") == item.get("treatmentPosition"), "evaluator-winner", case_id, failures)
        require(item.get("result") == "TREATMENT_WIN", "evaluator-result", case_id, failures)
        require(item.get("preservation") == "PASS", "evaluator-preservation", case_id, failures)
        require(item.get("manipulation") == "PASS", "evaluator-manipulation", case_id, failures)
        require(bool(str(item.get("taskPath", "")).strip()), "evaluator-task-path", case_id, failures)
    require(len(excluded) == 2, "evaluator-excluded-count", str(len(excluded)), failures)
    require(any(item.get("result") == "TREATMENT_LOSS" for item in excluded), "evaluator-loss-preserved", "initial loss missing", failures)
    require(any(item.get("result") == "TREATMENT_WIN_EXCLUDED" for item in excluded), "evaluator-incomplete-preserved", "incomplete packet receipt missing", failures)
    claim_ceiling = str(receipts.get("claimCeiling", "")).lower()
    require("no human" in claim_ceiling and "no" in claim_ceiling and "conversion" in claim_ceiling, "evaluator-claim-ceiling", claim_ceiling, failures)

    run = load_json(RUN_RECEIPT)
    require(bool(re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", str(run.get("run_uuid", "")))), "run-uuid", str(run.get("run_uuid")), failures)
    require(run.get("mode") == "CANONICAL_SHADOW", "run-mode", str(run.get("mode")), failures)
    require(run.get("promotionEligible") is False and run.get("runtimeAuthorityChanged") is False, "run-authority", "promotion or authority inflated", failures)
    require(run.get("marketEvent") == "NO EVENT", "run-market-event", str(run.get("marketEvent")), failures)
    expected_counts = {
        "sourcePackages": 6,
        "shadowDecisions": 8,
        "candidateDecisions": 5,
        "developmentFixtures": 33,
        "mutationRejections": 78,
        "ownerSeams": 5,
        "jasonWorkflows": 38,
        "jasonPromptsV2": 33,
        "jasonCompatibilityPrompts": 26,
        "admissionSurfaces": 97,
    }
    require(run.get("counts") == expected_counts, "run-counts", str(run.get("counts", {})), failures)
    require(set(run.get("allowedOverlayPointers", [])) == ALLOWED_OVERLAY_POINTERS, "run-pointer-set", str(run.get("allowedOverlayPointers")), failures)
    expected_runtime = runtime_policy_attestation(ROOT)
    actual_runtime = run.get("activeRuntimeSurface", {})
    require(
        actual_runtime.get("scannedFileCount") == expected_runtime.get("scannedFileCount"),
        "run-runtime-file-count",
        str(actual_runtime.get("scannedFileCount")),
        failures,
    )
    for field in ("fullSurfaceSha256", "policyAggregateSha256", "overlayPointers", "pointerParagraphSha256", "coldMarkerViolations", "promotionViolations"):
        require(
            actual_runtime.get(field) == expected_runtime.get(field),
            "run-runtime-surface",
            f"{field}: {actual_runtime.get(field)}",
            failures,
        )
    expected_context_index = jason_context_index_attestation()
    require(
        expected_context_index.get("matchesLiveSkill") is True,
        "live-jason-context-index",
        str(expected_context_index),
        failures,
    )
    require(
        run.get("jasonContextIndex") == expected_context_index,
        "run-jason-context-index",
        str(run.get("jasonContextIndex")),
        failures,
    )
    manifest = run.get("manifest_sha256", {})
    expected_manifest = {str(path.relative_to(ROOT)) for path in trust_paths()}
    require(set(manifest) == expected_manifest, "run-manifest-set", "manifest file set differs", failures)
    for relative, expected_hash in manifest.items():
        path = ROOT / relative
        require(path.is_file() and sha256(path) == expected_hash, "run-manifest-hash", relative, failures)
    assertions = run.get("assertions", {})
    require(assertions == EXPECTED_NO_EVENT_ASSERTIONS, "run-assertions", str(assertions), failures)
    require(run.get("verdict") == "CANONICAL SHADOW COMPILER VALIDATED / HUMAN, PRODUCTION, AND MARKET EFFECT UNTESTED", "run-verdict", str(run.get("verdict")), failures)

    summary_errors = validate_summary_text(BENCHMARK_SUMMARY.read_text(encoding="utf-8"))
    require(not summary_errors, "benchmark-summary", str(summary_errors), failures)


def validate_runtime_boundary(
    failures: list[str],
    injected_surface: tuple[str, str] | None = None,
) -> None:
    payloads = [
        (relative, data.decode("utf-8", errors="replace"))
        for relative, data in runtime_payloads(ROOT, injected_surface)
    ]
    violations = [
        f"{relative}:{marker}"
        for relative, text in payloads
        for marker in COLD_RUNTIME_MARKERS
        if marker in text.lower()
    ]
    require(not violations, "runtime-pointer", f"cold compiler markers on active surfaces: {violations[:5]}", failures)
    overlay_pointers = overlay_pointer_paths(ROOT, injected_surface)
    require(
        overlay_pointers == ALLOWED_OVERLAY_POINTERS,
        "overlay-pointer-surface",
        f"expected={sorted(ALLOWED_OVERLAY_POINTERS)} actual={sorted(overlay_pointers)}",
        failures,
    )
    require(
        not promotion_violations(ROOT, injected_surface),
        "overlay-promotion-surface",
        f"forbidden promotion prose: {promotion_violations(ROOT, injected_surface)[:5]}",
        failures,
    )
    require("Status: SHADOW" in OVERLAY.read_text(encoding="utf-8"), "overlay-mode", "existing overlay is not SHADOW", failures)
    require(len(list(WORKFLOW_ROOT.glob("*.md"))) == 38, "jason-workflow-count", "canonical Jason workflow count changed", failures)
    require(len(list(PROMPT_V2_ROOT.glob("*.md"))) == 33, "jason-prompt-v2-count", "canonical Jason prompts-v2 count changed", failures)
    require(not (ROOT / ".agent/workflows/sales-psychology-situation-compiler.md").exists(), "new-workflow", "new compiler workflow exists", failures)
    require(not (ROOT / ".agents/skills/sales-psychology-situation-compiler/SKILL.md").exists(), "new-skill", "new compiler skill exists", failures)


def validate_summary_text(text: str) -> list[str]:
    errors: list[str] = []
    lowered = text.lower()
    forbidden = [
        "proves conversion", "proved conversion", "market proof", "caused sales", "drove revenue",
        "buyers paid because", "promotion achieved", "human-preferred"  # no human event in this round
    ]
    if any(phrase in lowered for phrase in forbidden):
        errors.append("summary-evidence-inflation")
    outcome_inflation = re.compile(
        r"\b(?:validated|demonstrates?|proved|improved|increased|caused|drove|boosted|generated|produced|delivered|lifted|raised|grew)\b"
        r"[^.!?\n]{0,80}\b(?:sales?|purchases?|conversion|revenue|lift|impact)\b"
        r"|\b(?:sales?|purchases?|conversion|revenue|lift|impact)\b"
        r"[^.!?\n]{0,80}\b(?:validated|demonstrates?|proved|improved|increased|caused|drove|boosted|generated|produced|delivered|lifted|raised|grew)\b",
        re.IGNORECASE,
    )
    if outcome_inflation.search(text):
        errors.append("summary-outcome-inflation")
    observed_event = re.compile(
        r"\b(?:human(?:s|\s+judges?)?|reviewers?|buyers?|customers?|prospects?)\s+"
        r"(?:(?:have|had|strongly|clearly|overwhelmingly|all|mostly)\s+){0,3}"
        r"(?:preferred|chose|selected|purchased|bought|paid|converted|booked|clicked|responded|replied|accepted)\b"
        r"|\b(?:treatment|overlay|layer|version)\s+(?:was|is|were|has\s+been)\s+"
        r"(?:strongly\s+)?preferred\s+by\s+(?:human(?:s|\s+judges?)?|reviewers?|buyers?|customers?|prospects?)\b",
        re.IGNORECASE,
    )
    if observed_event.search(text):
        errors.append("summary-observed-event-inflation")
    for required in ("development_only", "no event", "production and market effect untested"):
        if required not in lowered:
            errors.append(f"summary-missing-{required.replace(' ', '-')}")
    return errors


def mutation_suite(
    registry: dict[str, Any],
    fixtures: dict[str, Any],
    mapping: dict[str, Any],
    outputs: dict[str, dict[str, Any]],
    compiler: Any,
) -> list[str]:
    by_id = {case["case_id"]: case for case in fixtures["cases"]}
    expected = mapping["expected"]
    results: list[str] = []

    def rejected(mutation_id: str, errors: list[str]) -> None:
        if errors:
            results.append(mutation_id)

    output = copy.deepcopy(outputs["P06"]); output["support"] = ["Fit", "Value"]
    rejected("M01", validate_output(by_id["P06"], expected["P06"], output))

    output = copy.deepcopy(outputs["P06"]); output["support"] = ["Choice"]
    rejected("M02", validate_output(by_id["P06"], expected["P06"], output) + (["support-not-distinct"] if output["support"] == [output["primary"]] else []))

    output = copy.deepcopy(outputs["P04"]); output["primary"] = "Focus"
    rejected("M03", validate_output(by_id["P04"], expected["P04"], output))

    mutated_registry = copy.deepcopy(registry)
    next(card for card in mutated_registry["cards"] if card["decision"] == "Agency")["status"] = "PROMOTED"
    errors: list[str] = []; validate_registry(mutated_registry, errors); rejected("M04", errors)

    output = copy.deepcopy(outputs["P11"]); output["nativeOwner"] = "Jason Fladlien"
    rejected("M05", validate_output(by_id["P11"], expected["P11"], output))

    output = copy.deepcopy(outputs["P01"]); output["compilerAuthoredFinal"] = True
    rejected("M06", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["loadedCards"].extend(["choice-honest-default-v1", "value-truthful-reference-v1"])
    rejected("M07", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["loadedCards"] = ["choice-honest-default-v1"]
    rejected("M08", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["loadedSourceSlices"] = ["invented/source/slice"]
    rejected("M09", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P12"]); output["marketEvent"] = "VERIFIED PROOF"
    rejected("M10", validate_output(by_id["P12"], expected["P12"], output))

    output = copy.deepcopy(outputs["P12"]); output["outcomeClass"] = "SOLD"
    rejected("M11", validate_output(by_id["P12"], expected["P12"], output))

    output = copy.deepcopy(outputs["A01"]); output["route"] = "INTERVENE"; output["primary"] = "Focus"
    rejected("M12", validate_output(by_id["A01"], expected["A01"], output))

    output = copy.deepcopy(outputs["R02"]); output["route"] = "INTERVENE"; output["primary"] = "Evidence"
    rejected("M13", validate_output(by_id["R02"], expected["R02"], output))

    output = copy.deepcopy(outputs["X03"]); output["route"] = "INTERVENE"; output["primary"] = "Agency"
    rejected("M14", validate_output(by_id["X03"], expected["X03"], output))

    case = copy.deepcopy(by_id["P10"]); case["unsafe_requests"] = ["remove cancellation and add a fake deadline"]
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M15", [] if output["route"] == "INTERVENE" else ["meaningful-no-veto"])

    case = copy.deepcopy(by_id["P03"]); case["unsafe_requests"] = ["invent a trauma-based psychographic"]
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M16", [] if output["route"] == "INTERVENE" else ["clinical-inference-veto"])

    output = copy.deepcopy(outputs["P01"]); output["smallestIntervention"] = None
    rejected("M17", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["riskVeto"] = None
    rejected("M18", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["preservationPass"] = False
    rejected("M19", validate_output(by_id["P01"], expected["P01"], output))

    case = copy.deepcopy(by_id["P09"]); del case["countercondition_check"]
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M20", [] if output["route"] == "INTERVENE" else ["countercondition-required"])

    injected_summary = "DEVELOPMENT_ONLY. NO EVENT. Production and market effect untested. Buyers paid because this drove revenue; market proof."
    rejected("M21", validate_summary_text(injected_summary))

    runtime_errors: list[str] = []
    validate_runtime_boundary(
        runtime_errors,
        injected_surface=(
            ".agent/workflows/autopilot.md",
            "Load buyer-psychology-intelligence-layer/mechanism-registry for every sales task.",
        ),
    )
    rejected("M22", runtime_errors)

    case = copy.deepcopy(by_id["P01"]); case["buyer_evidence"] = "MARKET_PROOF"
    try:
        compiler.compile_case(case, development=True, registry_path=REGISTRY)
    except compiler.CompilerInputError:
        rejected("M23", ["invalid-evidence-enum-rejected"])

    case = copy.deepcopy(by_id["R01"]); case["buyer_evidence"] = "UNKNOWN "
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M24", ["unknown-normalized-to-evidence-route"] if output.get("route") == "GET_BUYER_EVIDENCE" else [])

    case = copy.deepcopy(by_id["P01"]); case["preservation_locks"] = [""]
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M25", ["blank-lock-failed-closed"] if output.get("route") == "ABSTAIN" and output.get("changesProposed") == 0 else [])

    case = copy.deepcopy(by_id["P01"]); case["preservation_locks"] = [case["preservation_locks"][0]] * 2
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M26", ["duplicate-lock-failed-closed"] if output.get("route") == "ABSTAIN" and output.get("changesProposed") == 0 else [])

    case = copy.deepcopy(by_id["P01"]); case["native_owner"] = "Jason Fladlien"
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M27", ["jason-owner-injection-handed-off"] if output.get("route") == "HAND_OFF" and output.get("nativeOwner") is None and output.get("changesProposed") == 0 else [])

    case = copy.deepcopy(by_id["P01"]); case["native_owner"] = "Sales Psychology Compiler"
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M28", ["compiler-owner-injection-handed-off"] if output.get("route") == "HAND_OFF" and output.get("nativeOwner") is None and output.get("changesProposed") == 0 else [])

    metadata = load_json(ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer/development-benchmark.md.metadata.json")
    altered = copy.deepcopy(metadata); altered["promotionEligible"] = True
    rejected("M29", metadata_payload_errors(altered))
    altered = copy.deepcopy(metadata); altered["marketEvent"] = "MARKET_PROOF"
    rejected("M30", metadata_payload_errors(altered))
    altered = copy.deepcopy(metadata); altered["runtimeAuthorityChanged"] = True
    rejected("M31", metadata_payload_errors(altered))

    case = copy.deepcopy(by_id["P01"]); case["artifact_class"] = " Code "
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M32", ["abstention-class-normalized"] if output.get("route") == "ABSTAIN" else [])

    case = copy.deepcopy(by_id["P01"]); case["persuasion_permitted"] = "false"
    try:
        compiler.compile_case(case, development=True, registry_path=REGISTRY)
    except compiler.CompilerInputError:
        rejected("M33", ["permission-type-rejected"])

    case = copy.deepcopy(by_id["P12"]); case.pop("native_owner", None)
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected(
        "M34",
        ["action-default-owner-consistent"]
        if output.get("route") == "INTERVENE"
        and output.get("nativeOwner") == "Selected Native Function Owner"
        else [],
    )

    case = copy.deepcopy(by_id["R02"]); case["truth_gaps"] = [" Missing-Proof "]
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M35", ["truth-gap-normalized"] if output.get("route") == "GET_PROOF" else [])

    case = copy.deepcopy(by_id["P01"]); case["observed_friction_codes"] = [" HEAD-ON-BELIEF-DEFENSE "]
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected("M36", ["friction-code-normalized"] if output.get("route") == "INTERVENE" else [])

    command_runtime_errors: list[str] = []
    validate_runtime_boundary(
        command_runtime_errors,
        injected_surface=(
            ".claude/commands/autopilot.md",
            "Load the Buyer Psychology Decision Intelligence Overlay for every task.",
        ),
    )
    rejected("M37", command_runtime_errors)

    title_runtime_errors: list[str] = []
    validate_runtime_boundary(
        title_runtime_errors,
        injected_surface=(
            ".agent/workflows/autopilot.md",
            "Always activate Buyer Psychology Decision Intelligence Overlay.",
        ),
    )
    rejected("M38", title_runtime_errors)

    output = copy.deepcopy(outputs["P01"]); output["decision"] = "BELIEF_SELECTED"
    rejected("M39", validate_output(by_id["P01"], expected["P01"], output))

    for mutation_id, missing_field in (
        ("M40", "requires_buyer_interpretation"),
        ("M41", "truth_gaps"),
        ("M42", "unsafe_requests"),
        ("M43", "observed_friction_codes"),
    ):
        case = copy.deepcopy(by_id["P01"])
        case.pop(missing_field)
        try:
            compiler.compile_case(case, development=True, registry_path=REGISTRY)
        except compiler.CompilerInputError:
            rejected(mutation_id, [f"missing-{missing_field}-rejected"])

    case = copy.deepcopy(by_id["P01"])
    case["support_friction_code"] = "choice-overload"
    case["support_countercondition_check"] = {
        "passed": True,
        "evidence": "Choice support supplied solely to test cross-owner rejection.",
    }
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected(
        "M44",
        ["support-owner-boundary-held"]
        if output.get("route") == "INTERVENE"
        and output.get("support") == []
        and any("native owner" in warning for warning in output.get("warnings", []))
        else [],
    )

    mutated_registry = copy.deepcopy(registry)
    next(
        card for card in mutated_registry["cards"] if card["decision"] == "Belief"
    )["native_owner"] = "Jason Fladlien"
    owner_errors: list[str] = []
    validate_registry_default_owners(mutated_registry, compiler, owner_errors)
    rejected("M45", owner_errors)

    case = copy.deepcopy(by_id["P01"]); case["truth_gaps"] = ["unknown-claim-gap"]
    try:
        compiler.compile_case(case, development=True, registry_path=REGISTRY)
    except compiler.CompilerInputError:
        rejected("M46", ["unknown-truth-gap-rejected"])

    case = copy.deepcopy(by_id["P01"]); case.pop("persuasion_permitted")
    try:
        compiler.compile_case(case, development=True, registry_path=REGISTRY)
    except compiler.CompilerInputError:
        rejected("M47", ["missing-permission-rejected"])

    case = copy.deepcopy(by_id["P01"]); case["artifact_class"] = "medical-copy"
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected(
        "M48",
        ["high-stakes-class-abstained"]
        if output.get("route") == "ABSTAIN"
        and output.get("changesProposed") == 0
        else [],
    )

    case = copy.deepcopy(by_id["P01"]); case.pop("risk_domain")
    try:
        compiler.compile_case(case, development=True, registry_path=REGISTRY)
    except compiler.CompilerInputError:
        rejected("M49", ["missing-risk-domain-rejected"])

    case = copy.deepcopy(by_id["P01"]); case["risk_domain"] = "HIGH_STAKES"; case["artifact_class"] = "healthcare-copy"
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected(
        "M50",
        ["declared-high-stakes-abstained"]
        if output.get("route") == "ABSTAIN"
        and output.get("changesProposed") == 0
        else [],
    )

    case = copy.deepcopy(by_id["P01"]); case["risk_domain"] = "UNDECLARED"
    try:
        compiler.compile_case(case, development=True, registry_path=REGISTRY)
    except compiler.CompilerInputError:
        rejected("M51", ["unknown-risk-domain-rejected"])

    for mutation_id, artifact_class in (
        ("M52", "medical copy"),
        ("M53", "legal/financial copy"),
        ("M54", "supplement.sales-page"),
        ("M55", "medicalcopy"),
    ):
        case = copy.deepcopy(by_id["P01"]); case["artifact_class"] = artifact_class
        output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
        rejected(
            mutation_id,
            ["high-stakes-boundary-abstained"]
            if output.get("route") == "ABSTAIN"
            and output.get("changesProposed") == 0
            else [],
        )

    promotion_runtime_errors: list[str] = []
    validate_runtime_boundary(
        promotion_runtime_errors,
        injected_surface=(
            ".agent/workflows/copy-engine.md",
            "Always activate Buyer Psychology Decision Intelligence Overlay for every copy task; this is mandatory.",
        ),
    )
    rejected("M56", promotion_runtime_errors)

    mutated_registry = copy.deepcopy(registry)
    next(card for card in mutated_registry["cards"] if card["decision"] == "Belief")["status"] = "EXCLUDED"

    class RegistryPayload:
        def read_text(self, encoding: str = "utf-8") -> str:
            return json.dumps(mutated_registry)

    try:
        compiler.load_registry(RegistryPayload())
    except compiler.CompilerInputError:
        rejected("M57", ["unknown-registry-status-rejected"])

    case = copy.deepcopy(by_id["P01"]); case["countercondition_check"]["evidence"] = {}
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected(
        "M58",
        ["non-string-primary-evidence-rejected"]
        if output.get("route") == "ABSTAIN" and output.get("changesProposed") == 0
        else [],
    )

    case = copy.deepcopy(by_id["P06"]); case["support_countercondition_check"]["evidence"] = {}
    output = compiler.compile_case(case, development=True, registry_path=REGISTRY)
    rejected(
        "M59",
        ["non-string-support-evidence-rejected"]
        if output.get("route") == "INTERVENE"
        and output.get("support") == []
        and any("countercondition" in warning for warning in output.get("warnings", []))
        else [],
    )

    high_stakes_compounds = (
        "pharmaceutical-copy",
        "medicalnewsletter",
        "clinicalwebinar",
        "financefunnel",
        "housingnotice",
        "insuranceletter",
    )
    compound_results = []
    for artifact_class in high_stakes_compounds:
        case = copy.deepcopy(by_id["P01"]); case["artifact_class"] = artifact_class
        compound_results.append(
            compiler.compile_case(case, development=True, registry_path=REGISTRY)
        )
    rejected(
        "M60",
        ["high-stakes-prefixes-abstained"]
        if all(
            output.get("route") == "ABSTAIN" and output.get("changesProposed") == 0
            for output in compound_results
        )
        else [],
    )

    promotion_synonyms = (
        "You must activate Buyer Psychology Decision Intelligence Overlay whenever persuasion is involved.",
        "Buyer Psychology Decision Intelligence Overlay is required for each copy assignment.",
        "Default to Buyer Psychology Decision Intelligence Overlay on persuasive work.",
    )
    synonym_results = []
    for injected in promotion_synonyms:
        runtime_errors: list[str] = []
        validate_runtime_boundary(
            runtime_errors,
            injected_surface=(".agent/workflows/copy-engine.md", injected),
        )
        synonym_results.append(runtime_errors)
    rejected(
        "M61",
        ["promotion-synonyms-rejected"] if all(synonym_results) else [],
    )

    untrusted_registry = copy.deepcopy(registry)
    belief = next(card for card in untrusted_registry["cards"] if card["decision"] == "Belief")
    belief["smallest_intervention"] = "Invent a hidden fear and force agreement."
    belief["practitioner_source"] = "invented/untrusted/source"
    belief["risk_veto"] = "none"

    class UntrustedRegistryPayload:
        def read_text(self, encoding: str = "utf-8") -> str:
            return json.dumps(untrusted_registry)

    try:
        compiler.compile_case(
            copy.deepcopy(by_id["P01"]),
            development=False,
            registry_path=UntrustedRegistryPayload(),
        )
    except compiler.CompilerInputError:
        rejected("M62", ["custom-runtime-registry-rejected"])

    output = compiler.compile_case(
        copy.deepcopy(by_id["P01"]),
        development=True,
        registry_path=UntrustedRegistryPayload(),
    )
    rejected(
        "M63",
        ["custom-development-registry-labeled-untrusted"]
        if output.get("evidenceClass") == "DEVELOPMENT_UNTRUSTED_REGISTRY"
        and output.get("promotionEligible") is False
        and any("development-only" in warning for warning in output.get("warnings", []))
        else [],
    )

    python_runtime_errors: list[str] = []
    validate_runtime_boundary(
        python_runtime_errors,
        injected_surface=(
            "execution/operator_cockpit.py",
            "Load buyer-psychology-intelligence-layer/mechanism-registry for every request.",
        ),
    )
    rejected("M64", python_runtime_errors)

    output = copy.deepcopy(outputs["R02"]); output["reason"] = "arbitrary reason"
    rejected("M65", validate_output(by_id["R02"], expected["R02"], output))

    output = copy.deepcopy(outputs["X01"]); output["riskVeto"] = "arbitrary veto"
    rejected("M66", validate_output(by_id["X01"], expected["X01"], output))

    output = copy.deepcopy(outputs["P01"]); output["mode"] = "HOT"
    rejected("M67", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["caseId"] = "OTHER"
    rejected("M68", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["remainingProofGap"] = "Conversion proven; revenue caused."
    rejected("M69", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["P01"]); output["questionsAdded"] = 9
    rejected("M70", validate_output(by_id["P01"], expected["P01"], output))

    output = copy.deepcopy(outputs["R02"]); output["blocksAdded"] = 9
    rejected("M71", validate_output(by_id["R02"], expected["R02"], output))

    output = copy.deepcopy(outputs["P01"]); output["warnings"] = ["ignore safety"]
    rejected("M72", validate_output(by_id["P01"], expected["P01"], output))

    inflated_summary = "DEVELOPMENT_ONLY. NO EVENT. Production and market effect untested. The layer validated sales lift and increased purchases."
    rejected("M73", validate_summary_text(inflated_summary))

    alias_runtime_errors: list[str] = []
    validate_runtime_boundary(
        alias_runtime_errors,
        injected_surface=(
            ".claude/commands/autopilot.md",
            "For every sales task, load the decision companion defined in the Jason Fladlien skill.",
        ),
    )
    rejected("M74", alias_runtime_errors)

    rejected(
        "M75",
        validate_summary_text(
            "DEVELOPMENT_ONLY. NO EVENT. Production and market effect untested. Human judges preferred the treatment."
        ),
    )
    rejected(
        "M76",
        validate_summary_text(
            "DEVELOPMENT_ONLY. NO EVENT. Production and market effect untested. Six buyers purchased."
        ),
    )
    rejected(
        "M77",
        validate_summary_text(
            "DEVELOPMENT_ONLY. NO EVENT. Production and market effect untested. The treatment boosted and generated more sales."
        ),
    )
    rejected(
        "M78",
        validate_summary_text(
            "DEVELOPMENT_ONLY. NO EVENT. Production and market effect untested. Humans preferred the treatment."
        ),
    )

    return results


def main() -> int:
    failures: list[str] = []
    for path in (REGISTRY, ADMISSION, FIXTURES, MAPPING, BLIND_PACKETS, BLIND_MAPPING, EVALUATOR_RECEIPTS, RUN_RECEIPT, BENCHMARK_SUMMARY, COMPILER, OVERLAY, JASON_SKILL):
        require(path.is_file(), "required-file", str(path.relative_to(ROOT)), failures)
    if failures:
        print("FAIL")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    registry = load_json(REGISTRY)
    admission = load_json(ADMISSION)
    fixtures = load_json(FIXTURES)
    mapping = load_json(MAPPING)
    compiler = load_compiler()

    validate_frozen_files(failures)
    validate_metadata_sidecars(failures)
    validate_registry(registry, failures)
    validate_registry_default_owners(registry, compiler, failures)
    validate_admission(admission, failures)
    outputs = validate_cases(registry, fixtures, mapping, compiler, failures)
    validate_blind_packets(failures)
    validate_receipts(failures)
    validate_runtime_boundary(failures)

    mutations = mutation_suite(registry, fixtures, mapping, outputs, compiler)
    require(mutations == [f"M{index:02d}" for index in range(1, 79)], "mutation-suite", f"rejected={mutations}", failures)

    if failures:
        print("FAIL — Sales Psychology Mastery Layer")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    print("PASS — Sales Psychology Mastery Layer")
    print("registry=13 (SHADOW=8, CANDIDATE=5)")
    print("canonical-admission=97 (ADMIT=28, DEFENSIVE=39, EXCLUDE=30); byte-identical legacy prompts=26, evidence weight=0")
    print("development=33/33 (positives=13, abstentions=7, repairs=7, rejects=6)")
    print("mutations=78/78 rejected")
    print("active-overlay-pointers=6 exact surfaces (Jason skill + 5 canonical owner seams)")
    print("imported-blind-model-declarations=6/6 treatment preferences; excluded iterations=2; original evaluator outputs not independently reverified; human comparisons=0")
    print("mode=CANONICAL_SHADOW; candidate runtime authority unchanged; market event=NO EVENT")
    print("verdict=CANONICAL SHADOW COMPILER VALIDATED / HUMAN, PRODUCTION, AND MARKET EFFECT UNTESTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
