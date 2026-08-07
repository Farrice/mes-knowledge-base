#!/usr/bin/env python3
"""Verify the immutable RelayNote fixture before any behavior generation."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "skills/kyle-milligan-copy-chief/tests/fixtures/relaynote"
NOTICE = "Fixture data. Not market evidence."
EXPECTED_TRUTH_IDS = {
    "PT-AUD-001",
    "PT-CAP-001",
    "PT-CAP-002",
    "PT-TEST-001",
    "PT-TEST-002",
    "PT-TEST-003",
    "PT-MET-001",
    "PT-MET-002",
    "PT-MET-003",
    "PT-MET-004",
    "PT-ACT-001",
}
EXPECTED_TRUTH_VALUES = {
    "PT-AUD-001": "agencies with 5–20 people",
    "PT-CAP-001": "turns a call transcript into a draft follow-up email",
    "PT-CAP-002": "extracts an assigned next-step owner and date when those details appear in the transcript",
    "PT-TEST-001": "30-day synthetic test",
    "PT-TEST-002": "12 fictional agencies",
    "PT-TEST-003": "1,248 synthetic call records",
    "PT-MET-001": "23% of assigned next steps were absent from the first manually drafted follow-up",
    "PT-MET-002": "18 minutes median manual drafting time",
    "PT-MET-003": "4 minutes median RelayNote drafting time",
    "PT-MET-004": "91% owner-and-date extraction accuracy",
    "PT-ACT-001": "Book a demo",
}
EXPECTED_FIXTURE_PATHS = {
    "README.md",
    "acceptance-contracts.json",
    "acceptance-cases.jsonl",
    "arm-b-adapter.md",
    "arm-contracts.json",
    "audience-brief.json",
    "blind-quality-rubric.json",
    "breakdown-lock.json",
    "context-packet.md",
    "evaluation-protocol.json",
    "kyle-fidelity-rubric.json",
    "output-contract.json",
    "post-run-receipt.schema.json",
    "product-truth.json",
    "provenance-contract.json",
    "run-config.json",
    "swipes/S1.md",
    "swipes/S2.md",
    "swipes/S3.md",
    "swipes/S4.md",
    "swipes/S5.md",
    "swipes/index.json",
    "transfer-veto.json",
    "weak-draft.md",
}
EXPECTED_CONTROL_METRIC_TOKENS = {
    "21-day", "87%", "16 minutes", "19%", "5 minutes", "160 synthetic matters",
    "89%", "417 abandoned carts", "31%", "40 synthetic teams", "93%", "11 hours",
}
EXPECTED_ACCEPTANCE_RESULTS = {
    "missing-context": "STOP_FOR_CONTEXT",
    "insufficient-swipes": "STOP_FOR_FIVE",
    "irrelevant-famous-swipes": "KEEP_S2_PRIMARY",
    "invented-mechanism": "BLOCK_PROMISE",
    "four-punches-distinction": "FAIL_SOURCE_FIDELITY",
    "nesb-stuffing": "REPLACE_WITH_EVIDENCE",
    "unsupported-growth": "HARD_FAIL_REMOVE_OUTCOME",
    "multiple-undefined-mechanisms": "ONE_SUPPORTED_CONCEPT",
    "naked-authority": "PROOF_GAP",
    "hook-barrage": "CONSOLIDATE_PROMISE",
    "missing-results": "DIAGNOSE_ABSENT_DEMONSTRATION",
    "claim-demo-mismatch": "REJECT_OR_RELOCATE_PROOF",
    "matthew-attribution": "FAIL_ATTRIBUTION",
    "shaming-feedback": "FAIL_TONE",
    "all-eight-veto": "SELECT_ONE_ROUTE",
    "regulated-claim-veto": "DOMAIN_GATE",
    "self-reported-credential": "REMOVE_SELF_REPORTED_PROOF",
    "one-pass-hot-promotion": "KEEP_COLD",
}
EXPECTED_ACCEPTANCE_NAMES = {
    "missing-context",
    "insufficient-swipes",
    "irrelevant-famous-swipes",
    "invented-mechanism",
    "four-punches-distinction",
    "nesb-stuffing",
    "unsupported-growth",
    "multiple-undefined-mechanisms",
    "naked-authority",
    "hook-barrage",
    "missing-results",
    "claim-demo-mismatch",
    "matthew-attribution",
    "shaming-feedback",
    "all-eight-veto",
    "regulated-claim-veto",
    "self-reported-credential",
    "one-pass-hot-promotion",
}
EXPECTED_WEAK_DRAFT = (
    "Revenue teams are under pressure to move faster. RelayNote uses AI-powered "
    "conversation intelligence and workflow automation to help agencies optimize "
    "follow-up and improve pipeline efficiency. Our platform turns calls into "
    "action items and emails. Book a demo today."
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(relative: str, errors: list[str]) -> dict:
    path = FIXTURE / relative
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{relative}: invalid or missing JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{relative}: top level must be an object")
        return {}
    return value


def main() -> int:
    errors: list[str] = []
    manifest = load_json("manifest.json", errors)
    if errors:
        return report(errors)

    actual_files = sorted(
        path for path in FIXTURE.rglob("*")
        if path.is_file() and path != FIXTURE / "manifest.json"
    )
    listed = manifest.get("files", [])
    listed_paths = [entry.get("path") for entry in listed]
    actual_paths = [str(path.relative_to(FIXTURE)) for path in actual_files]
    if set(actual_paths) != EXPECTED_FIXTURE_PATHS:
        missing = sorted(EXPECTED_FIXTURE_PATHS - set(actual_paths))
        extra = sorted(set(actual_paths) - EXPECTED_FIXTURE_PATHS)
        errors.append(f"fixture allowlist drifted; missing={missing}, extra={extra}")
    for path in FIXTURE.rglob("*"):
        if path.is_symlink():
            errors.append(f"fixture symlink is forbidden: {path.relative_to(FIXTURE)}")
        try:
            path.resolve().relative_to(FIXTURE.resolve())
        except ValueError:
            errors.append(f"fixture path escapes root: {path}")
    if manifest.get("status") != "FROZEN_BEFORE_GENERATION":
        errors.append("manifest status must be FROZEN_BEFORE_GENERATION")
    if manifest.get("file_count_excluding_manifest") != len(actual_files):
        errors.append("manifest file count does not match fixture inventory")
    if listed_paths != actual_paths:
        errors.append("manifest paths do not exactly match the sorted fixture inventory")
    for entry in listed:
        relative = entry.get("path", "")
        path = FIXTURE / relative
        if not path.is_file():
            errors.append(f"manifest lists missing file: {relative}")
            continue
        if entry.get("sha256") != digest(path):
            errors.append(f"frozen byte hash mismatch: {relative}")
        if entry.get("bytes") != path.stat().st_size:
            errors.append(f"frozen byte count mismatch: {relative}")

    for path in [FIXTURE / "manifest.json", *actual_files]:
        try:
            content = path.read_text()
        except UnicodeDecodeError:
            errors.append(f"fixture contains a non-text file: {path.relative_to(FIXTURE)}")
            continue
        if NOTICE not in content:
            errors.append(f"fixture notice missing: {path.relative_to(FIXTURE)}")

    product = load_json("product-truth.json", errors)
    truths = product.get("truths", [])
    truths_by_id = {item.get("id"): item for item in truths}
    if set(truths_by_id) != EXPECTED_TRUTH_IDS or len(truths) != len(EXPECTED_TRUTH_IDS):
        errors.append("Product Truth IDs must be the exact frozen eleven-ID set")
    for truth_id, expected_value in EXPECTED_TRUTH_VALUES.items():
        if truths_by_id.get(truth_id, {}).get("value") != expected_value:
            errors.append(f"{truth_id}: frozen value drifted")
    if truths_by_id.get("PT-CAP-002", {}).get("copy_permission") != (
        "Must always retain the when-present qualifier. PT-MET-004 does not remove or weaken it."
    ):
        errors.append("PT-CAP-002 must always retain its when-present qualifier")
    if truths_by_id.get("PT-MET-001", {}).get("denominator") != (
        "all assigned next steps recorded across 1,248 synthetic call records"
    ):
        errors.append("PT-MET-001 denominator must remain the assigned-next-step set")
    mechanism = product.get("mechanism_status", {})
    if mechanism.get("status") != "NOT_VERIFIED_NON_APPLICABLE" or "forbidden" not in mechanism.get("rule", ""):
        errors.append("fixture must forbid mechanism-led claims")
    opportunity = product.get("opportunity_graph", {})
    expected_graph_ids = {
        "catalyst": {"PT-CAP-001", "PT-CAP-002"},
        "recurring_pattern": {"PT-TEST-001", "PT-TEST-002", "PT-TEST-003", "PT-MET-001", "PT-MET-002"},
        "bounded_path": {"PT-CAP-001", "PT-CAP-002"},
        "supported_fixture_result": {"PT-MET-003", "PT-MET-004"},
    }
    for node, truth_ids in expected_graph_ids.items():
        if set(opportunity.get(node, {}).get("truth_ids", [])) != truth_ids:
            errors.append(f"opportunity graph node {node} drifted")
    unproven = " ".join(product.get("explicitly_unproven", [])).lower()
    for required in ("revenue", "conversion", "pipeline", "closed-won", "market", "78% faster", "14 minutes saved"):
        if required not in unproven:
            errors.append(f"explicitly_unproven is missing {required!r}")

    weak_text = (FIXTURE / "weak-draft.md").read_text()
    if weak_text.count(EXPECTED_WEAK_DRAFT) != 1:
        errors.append("weak-draft.md must contain the exact control draft once")
    audience = load_json("audience-brief.json", errors)
    if audience.get("placement") != "Problem-aware B2B demo-page opening with unknown prior trust.":
        errors.append("shared placement is missing or drifted")
    if audience.get("voice_evidence") != "UNAVAILABLE" or "Do not imitate" not in audience.get("voice_rule", ""):
        errors.append("shared voice limitation is missing or drifted")
    context_text = (FIXTURE / "context-packet.md").read_text()
    for required_context in (
        "NOT_VERIFIED_NON_APPLICABLE",
        "problem-aware B2B demo-page opening with unknown prior trust",
        "Frozen Opportunity Graph",
        "Voice evidence: unavailable",
    ):
        if required_context not in context_text:
            errors.append(f"shared context is missing {required_context!r}")

    swipe_index = load_json("swipes/index.json", errors)
    swipes = swipe_index.get("swipes", [])
    swipe_ids = [item.get("id") for item in swipes]
    if swipe_ids != ["S1", "S2", "S3", "S4", "S5"]:
        errors.append("swipe index must contain exactly ordered S1–S5")
    brands: list[str] = []
    scores: dict[str, int] = {}
    for swipe in swipes:
        swipe_id = swipe.get("id", "")
        relative = swipe.get("path", "")
        path = FIXTURE / relative
        brand = swipe.get("fictional_brand", "")
        brands.append(brand)
        scores[swipe_id] = swipe.get("synthetic_control_score")
        if not path.is_file():
            errors.append(f"{swipe_id}: full-text swipe file missing")
            continue
        text = path.read_text()
        if brand not in text or len(re.findall(r"\b[\w’'-]+\b", text)) < 90:
            errors.append(f"{swipe_id}: swipe is not a full synthetic control text")
        if f"`{scores[swipe_id]}/100`" not in text:
            errors.append(f"{swipe_id}: synthetic label differs between index and full text")

    breakdown = load_json("breakdown-lock.json", errors)
    if breakdown.get("five_read_set") != ["S1", "S2", "S3", "S4", "S5"]:
        errors.append("5-3-1 five-read set drifted")
    if breakdown.get("three_breakdown_set") != ["S2", "S1", "S3"]:
        errors.append("5-3-1 breakdown set must remain S2, S1, S3")
    if breakdown.get("primary_swipe_id") != "S2" or breakdown.get("locked") is not True:
        errors.append("S2 must remain the locked primary swipe")
    if scores and scores.get("S2") == max(scores.values()):
        errors.append("fixture no longer tests relevance over highest synthetic status")
    s2 = next((item for item in swipes if item.get("id") == "S2"), {})
    if not all(s2.get(field) in {"exact", "closest"} for field in ("audience_match", "problem_match", "mechanism_match")):
        errors.append("S2 must remain the closest audience/problem/mechanism control")

    veto = load_json("transfer-veto.json", errors)
    if not set(brands).issubset(set(veto.get("hard_failure_tokens_in_output", []))):
        errors.append("transfer veto must include every fictional control brand")
    if set(veto.get("hard_failure_metric_tokens_in_output", [])) != EXPECTED_CONTROL_METRIC_TOKENS:
        errors.append("transfer veto must enumerate every synthetic control metric token")
    veto_text = " ".join(veto.get("vetoed_from_transfer", [])).lower()
    for required in ("metrics", "source-video", "kyle", "matthew", "mechanism", "authority"):
        if required not in veto_text:
            errors.append(f"transfer veto is missing {required!r}")

    output = load_json("output-contract.json", errors)
    rules = output.get("opening_rules", {})
    if rules.get("count") != 3 or not rules.get("distinct_hypotheses_required"):
        errors.append("output contract must require exactly three distinct opening hypotheses")
    if rules.get("required_action") != "Book a demo":
        errors.append("output contract action drifted")
    if "PT-*" not in rules.get("factual_annotation_format", ""):
        errors.append("output contract must require PT-* evidence maps")
    if rules.get("word_count_each") != {"minimum": 55, "maximum": 115}:
        errors.append("opening word bounds must remain 55–115")
    if rules.get("line_count_each") != {"minimum": 4, "maximum": 8}:
        errors.append("opening line bounds must remain 4–8")
    if output.get("sections_in_order") != [
        "Opening 1", "Opening 1 Evidence Map", "Opening 2", "Opening 2 Evidence Map",
        "Opening 3", "Opening 3 Evidence Map", "Recommendation", "Recommendation Evidence Map",
    ]:
        errors.append("output section order drifted")
    if len(output.get("shared_constraints", [])) != 7:
        errors.append("output shared-constraint set is incomplete")
    if not output.get("recommendation_rules", {}).get("must_not_blend_options"):
        errors.append("recommendation must preserve one option rather than blend")

    arms = load_json("arm-contracts.json", errors)
    for relative in arms.get("shared_inputs", []):
        if not (FIXTURE / relative).is_file():
            errors.append(f"arm parity input missing: {relative}")
    arm_b = arms.get("arm_b", {})
    arm_c = arms.get("arm_c", {})
    for owner_key in ("required_owner", "required_support"):
        owner_path = arm_b.get(owner_key, "")
        if not (ROOT / owner_path).is_file():
            errors.append(f"Arm B required local comparator missing: {owner_path}")
    if arm_b.get("output_contract") != arm_c.get("output_contract") or arm_b.get("output_contract") != "output-contract.json":
        errors.append("Arms B and C must share the exact output contract")
    if not any("kyle-milligan-copy-chief" in item for item in arm_b.get("excluded", [])):
        errors.append("Arm B must explicitly exclude the Kyle system")
    for relative in arm_b.get("allowed_method_reads", []):
        if not (ROOT / relative).is_file():
            errors.append(f"Arm B allowed method read is missing: {relative}")
    if "breakdown-lock.json" not in arm_b.get("excluded", []):
        errors.append("Arm B must not receive the Kyle 5-3-1 breakdown lock")
    if arm_b.get("route_specific_inputs") != ["arm-b-adapter.md"]:
        errors.append("Arm B must use the frozen fixture-local comparator adapter")
    if not (FIXTURE / "arm-b-adapter.md").is_file():
        errors.append("Arm B comparator adapter is missing")
    if arm_b.get("revision_rounds_per_replicate") != 1 or len(arm_b.get("execution_protocol", [])) != 4:
        errors.append("Arm B must freeze Luke draft → Matthew audit → one Luke revision → format check")
    route_inputs = arm_c.get("route_specific_inputs", [])
    if route_inputs != [
        "breakdown-lock.json",
        "skills/kyle-milligan-copy-chief/references/mechanics-ledger.md",
    ]:
        errors.append("Arm C route-specific input lock drifted")
    if not (FIXTURE / "breakdown-lock.json").is_file() or not (
        ROOT / "skills/kyle-milligan-copy-chief/references/mechanics-ledger.md"
    ).is_file():
        errors.append("Arm C route-specific method input is missing")
    if not {"skills/luke-iha-vsl-leads", "skills/matthew-volkwyn-copywriting"}.issubset(
        set(arm_c.get("excluded", []))
    ):
        errors.append("Arm C must exclude both baseline method trees")
    for relative in arm_c.get("allowed_method_reads", []):
        if not (ROOT / relative).is_file():
            errors.append(f"Arm C allowed method read is missing: {relative}")
    kyle_root = ROOT / "skills/kyle-milligan-copy-chief"
    if len(list((kyle_root / "workflows").glob("*.md"))) != 8:
        errors.append("Arm C owner must contain exactly eight workflow files")
    if len(list((kyle_root / "references/prompts-v2").glob("*.md"))) != 8:
        errors.append("Arm C owner must contain exactly eight born-v2 prompts")
    if not (kyle_root / "SKILL.md").is_file() or not (kyle_root / "genius.md").is_file():
        errors.append("Arm C owner router or genius layer is missing")

    run = load_json("run-config.json", errors)
    settings = run.get("settings", {})
    comparison = run.get("comparison", {})
    if settings.get("replicates_per_generated_arm") != 3:
        errors.append("Arms B and C require three cold replicates")
    if settings.get("network") != "disabled" or settings.get("external_cache") != "disabled":
        errors.append("behavior runs must disable network and external cache")
    if settings.get("hidden_chat_context") != "forbidden" or settings.get("prior_arm_output_access") != "forbidden":
        errors.append("cold-start isolation settings drifted")
    if settings.get("creative_passes_per_replicate") != 2:
        errors.append("each arm must use two creative passes per replicate")
    if settings.get("method_specific_audit_passes_per_replicate") != 1:
        errors.append("each arm must use one method-specific audit pass per replicate")
    if settings.get("deterministic_format_checks_per_replicate") != 1:
        errors.append("each arm must use one non-creative format/truth check per replicate")
    if comparison.get("aggregate") != "median route-neutral score across three replicates":
        errors.append("comparison must use three-replicate medians")
    if comparison.get("arm_c_minimum_median") != 80 or comparison.get("arm_c_minus_arm_b_minimum") != 15:
        errors.append("incremental behavior thresholds drifted")
    if comparison.get("blind_pairwise_preferences_required") != 2 or comparison.get("blind_pairwise_trials") != 3:
        errors.append("blind pairwise threshold must remain 2 of 3")
    model = run.get("model", {})
    if not model.get("family") or not model.get("version") or "same inherited" not in model.get("parity_requirement", ""):
        errors.append("model family/version/parity lock is incomplete")

    neutral = load_json("blind-quality-rubric.json", errors)
    criteria = neutral.get("criteria", [])
    if neutral.get("score_total") != 100 or sum(item.get("weight", 0) for item in criteria) != 100:
        errors.append("route-neutral rubric weights must total 100")
    expected_weights = [20, 15, 15, 15, 15, 10, 5, 5]
    if [item.get("weight") for item in criteria] != expected_weights:
        errors.append("route-neutral rubric criterion weights drifted")
    if len(neutral.get("hard_failures", [])) < 8:
        errors.append("route-neutral rubric hard-failure surface is incomplete")

    fidelity = load_json("kyle-fidelity-rubric.json", errors)
    fidelity_criteria = fidelity.get("criteria", [])
    if len(fidelity_criteria) != 12 or fidelity.get("minimum_each") != 7:
        errors.append("Kyle fidelity rubric must contain twelve criteria with a 7 floor")
    truth_criterion = next((item for item in fidelity_criteria if item.get("id") == "KF-12"), {})
    if truth_criterion.get("required_score") != 10 or fidelity.get("visible_mechanics_required") != 3:
        errors.append("Kyle fidelity requires truth=10 and at least three visible mechanics")
    evidence_policy = fidelity.get("evidence_policy", {})
    if evidence_policy.get("main_arm_workflows") != [
        "01-531-swipe-discipline",
        "02-unique-promise-spine",
        "03-four-beat-opening-builder",
        "04-first-four-lines-audit",
    ]:
        errors.append("fidelity main-arm workflow scope must remain 01–04 only")
    acceptance_evidence = evidence_policy.get("acceptance_case_evidence", {})
    for fidelity_id in ("KF-07", "KF-08", "KF-09", "KF-10", "KF-11", "KF-12"):
        if not acceptance_evidence.get(fidelity_id):
            errors.append(f"fidelity criterion {fidelity_id} lacks isolated acceptance evidence")
    if "N/A cannot pass" not in evidence_policy.get("n_a_policy", ""):
        errors.append("fidelity evidence cannot award unexercised N/A criteria")
    if "never be concatenated" not in evidence_policy.get("no_all_eight_rule", ""):
        errors.append("fidelity acceptance evidence must preserve the no-all-eight rule")

    evaluation = load_json("evaluation-protocol.json", errors)
    label_generation = evaluation.get("label_generation", {})
    if label_generation.get("labels") != ["X", "Y"] or "fresh" not in label_generation.get("method", ""):
        errors.append("evaluation labels must be freshly randomized per pair")
    if "secret salt" not in label_generation.get("method", "") or "After evaluator scores" not in label_generation.get("seal", ""):
        errors.append("label map must use a pre-score salted commitment and post-score reveal")
    blind_packet = evaluation.get("blind_packet", {})
    if len(blind_packet.get("allowed_files", [])) != 12:
        errors.append("blind evaluator allowlist must contain the six pairs, five neutral inputs, and commitment")
    if "no inherited task turns" not in blind_packet.get("evaluator_context", ""):
        errors.append("blind evaluator must start without inherited task context")

    acceptance_path = FIXTURE / "acceptance-cases.jsonl"
    acceptance: list[dict] = []
    for line_number, line in enumerate(acceptance_path.read_text().splitlines(), start=1):
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"acceptance case line {line_number} is invalid JSON: {exc}")
            continue
        if case.get("notice") != NOTICE:
            errors.append(f"acceptance case line {line_number} lacks the exact notice")
        acceptance.append(case)
    if len(acceptance) != 18:
        errors.append("acceptance inventory must contain exactly 18 cases")
    if {case.get("name") for case in acceptance} != EXPECTED_ACCEPTANCE_NAMES:
        errors.append("acceptance case names drifted")
    for case in acceptance:
        if case.get("expected") != EXPECTED_ACCEPTANCE_RESULTS.get(case.get("name")):
            errors.append(f"{case.get('case_id')}: frozen expected behavior drifted")
        if len(case.get("required_behavior", "")) < 20:
            errors.append(f"{case.get('case_id')}: required behavior is underspecified")
    if [case.get("case_id") for case in acceptance] != [f"AC-{index:02d}" for index in range(1, 19)]:
        errors.append("acceptance case IDs must remain ordered AC-01 through AC-18")

    acceptance_contract = load_json("acceptance-contracts.json", errors)
    contract_cases = acceptance_contract.get("cases", {})
    if set(contract_cases) != {f"AC-{index:02d}" for index in range(1, 19)}:
        errors.append("acceptance contract must contain exact AC-01 through AC-18 keys")
    if acceptance_contract.get("common_output_headings_exact") != [
        "# Acceptance Result", "## Case", "## Decision", "## Evidence",
        "## Required Action", "## Prohibited Action", "## Proof Boundary",
    ]:
        errors.append("acceptance output heading contract drifted")
    for case_id, contract in contract_cases.items():
        if not (ROOT / contract.get("selected_route", "")).is_file():
            errors.append(f"{case_id}: frozen selected route is missing")
        expected = next((case.get("expected") for case in acceptance if case.get("case_id") == case_id), "")
        if f"Decision: {expected}" not in contract.get("required_lines", []):
            errors.append(f"{case_id}: acceptance contract does not bind the frozen expected decision")
        if not contract.get("forbidden_lines"):
            errors.append(f"{case_id}: acceptance contract lacks forbidden behavior markers")

    provenance = load_json("provenance-contract.json", errors)
    grades = provenance.get("grades", {})
    if grades.get("RUNTIME_OBSERVED", {}).get("registration_eligible") is not True:
        errors.append("runtime-observed provenance must be the only registration-eligible grade")
    for grade in ("ORCHESTRATOR_ATTESTED", "OPERATOR_ATTESTED"):
        if grades.get(grade, {}).get("registration_eligible") is not False:
            errors.append(f"{grade} must remain registration-ineligible")
    if "actual reads" not in " ".join(provenance.get("not_provable_from_final_bundle_alone", [])):
        errors.append("provenance contract must disclose the actual-read evidence limit")

    receipt_schema = load_json("post-run-receipt.schema.json", errors)
    verdict = receipt_schema.get("properties", {}).get("verdict", {}).get("enum", [])
    if set(verdict) != {"PASS_INCREMENTAL_BEHAVIOR", "PASS_DIAGNOSTIC_BEHAVIOR", "FAIL_NO_REGISTRATION"}:
        errors.append("post-run receipt schema lacks pass/fail registration verdicts")
    if "fixture_manifest_sha256" not in receipt_schema.get("required", []):
        errors.append("post-run receipt must bind to the frozen fixture manifest")
    if "acceptance_receipts" not in receipt_schema.get("required", []):
        errors.append("post-run receipt must include isolated acceptance receipts")
    receipt_properties = receipt_schema.get("properties", {})
    if receipt_properties.get("visible_kyle_mechanics", {}).get("items", {}).get("required") != [
        "mechanic_id", "name", "replicate_id", "source_rows", "delta_sha256", "output_delta"
    ]:
        errors.append("post-run mechanics must carry frozen identity, replicate, source rows, hash, and output delta")
    for required in ("provenance_grade", "registration_eligible", "provenance_limitations"):
        if required not in receipt_schema.get("required", []):
            errors.append(f"post-run receipt must include {required}")
    pass_then = receipt_schema.get("allOf", [{}])[0].get("then", {}).get("properties", {})
    if pass_then.get("arm_b_median", {}).get("minimum") != 65:
        errors.append("receipt PASS condition must enforce Arm B fairness floor")
    if pass_then.get("arm_c_median", {}).get("minimum") != 80 or pass_then.get("c_minus_b", {}).get("minimum") != 15:
        errors.append("receipt PASS condition must enforce C median and incremental delta")
    if pass_then.get("hard_failures", {}).get("maxItems") != 0 or pass_then.get("visible_kyle_mechanics", {}).get("minItems") != 3:
        errors.append("receipt PASS condition must reject hard failures and require three visible mechanics")
    if pass_then.get("acceptance_receipts", {}).get("items", {}).get("properties", {}).get("pass", {}).get("const") is not True:
        errors.append("receipt PASS condition must require every acceptance case to pass")

    return report(errors, manifest_sha256=digest(FIXTURE / "manifest.json"), file_count=len(actual_files))


def report(errors: list[str], manifest_sha256: str = "", file_count: int = 0) -> int:
    if errors:
        print("RELAYNOTE FIXTURE: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("RELAYNOTE FIXTURE: PASS")
    print(f"- immutable files: {file_count + 1} including manifest")
    print(f"- manifest sha256: {manifest_sha256}")
    print("- Product Truth IDs: 11")
    print("- synthetic full-text controls: 5; locked breakdown: S2/S1/S3; primary: S2")
    print("- generated arms: 3 cold replicates each for B/C; median comparison; 2/3 blind preference")
    print("- proof boundary: frozen inputs only; no behavior, embodiment, or market claim yet")
    return 0


if __name__ == "__main__":
    sys.exit(main())
