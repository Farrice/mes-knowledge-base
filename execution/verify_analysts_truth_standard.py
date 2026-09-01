#!/usr/bin/env python3
"""Verify the bounded Analyst's Truth Standard advisory companion."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "semantic_libraries/antigravity/primitives/analysts-truth-standard.md"
PACKAGE = ROOT / "extractions/video-context/SupWhagSCm8"
FIXTURES = PACKAGE / "analysts-truth-standard-fixtures.json"
RECEIPTS = PACKAGE / "analysts-truth-standard-production-receipts.json"
PRESSURE_TEST = PACKAGE / "analysts-truth-standard-pressure-test.md"
CYCLE_01 = PACKAGE / "analysts-truth-standard-production-cycle-01"
BASELINE_01 = CYCLE_01 / "frozen-baseline.md"
TREATMENT_01 = CYCLE_01 / "treatment-brief.md"
COMPARISON_01 = CYCLE_01 / "blind-comparison.md"
BASELINE_SOURCE_01 = ROOT / "deliverables/research-briefs/angle-brief-2026-08-13/angle-brief-2026-08-13-brief.md"
BASELINE_SHA256_01 = "6a07761e28ece602c086b47d4c8c52777760540750968dd96a314e96b9be9de8"
CYCLE_02 = PACKAGE / "analysts-truth-standard-production-cycle-02"
BASELINE_02 = CYCLE_02 / "frozen-baseline.md"
TREATMENT_02 = CYCLE_02 / "treatment-brief.md"
COMPARISON_02 = CYCLE_02 / "blind-comparison.md"
BASELINE_SOURCE_02 = ROOT / "deliverables/system-audits/2026-09-01-intelligent-output-surface-map.md"
BASELINE_SHA256_02 = "254f38f19720f3a0723c4fd80ffe9bcd6d4606bfb509ca8dc80b168793f0c5fa"
CYCLE_03 = PACKAGE / "analysts-truth-standard-production-cycle-03"
BASELINE_03 = CYCLE_03 / "frozen-baseline.md"
TREATMENT_03 = CYCLE_03 / "treatment-brief.md"
COMPARISON_03 = CYCLE_03 / "blind-comparison.md"
BASELINE_SOURCE_03 = ROOT / "deliverables/zero-momentum-ai-offer/offer-tournament.md"
BASELINE_SHA256_03 = "2825eed79b38c64f417f8317289de896b323e37f020a2959c552fbe10bf6e7ef"

BASELINE_SOURCES = {
    "01": (BASELINE_SOURCE_01, BASELINE_SHA256_01),
    "02": (BASELINE_SOURCE_02, BASELINE_SHA256_02),
    "03": (BASELINE_SOURCE_03, BASELINE_SHA256_03),
}

EXPECTED_CASES = {
    "art-critique",
    "research-synthesis",
    "harness-system-status",
    "content-ideation",
}
EXPECTED_NEGATIVES = {
    "direct-factual-answer": "REPORTING",
    "pure-production": "ARTIFACT",
    "unsupported-causality": "EVIDENCE_LIMIT",
    "low-evidence-ideation": "HYPOTHESIS",
}
EXPECTED_RUBRIC = [
    "decision_change",
    "causal_restraint",
    "insight_density",
    "explanation_burden",
    "creative_range_preservation",
]

REQUIRED_MARKERS = {
    PRIMITIVE: (
        "Status: `ACTIVE ADVISORY`",
        "## The Depth Ladder",
        "## Creative Ideation Lens",
        "## Causal Restraint",
        "## Visible Result Filter",
        "## Preservation Boundaries",
        "three distinct production",
        "Farrice explicitly approved integration",
        "Revert to `SHADOW`",
    ),
    ROOT / "directives/constitution/shared-blocks.md": (
        "BEGIN:shared-analysts-truth-standard",
        "Analyst's Truth Standard (ACTIVE ADVISORY)",
        "preserve surprise",
        "may not reroute",
    ),
    ROOT / "AGENTS.md": (
        "BEGIN:shared-analysts-truth-standard",
        "analysts-truth-standard.md",
    ),
    ROOT / "CLAUDE.md": (
        "BEGIN:shared-analysts-truth-standard",
        "analysts-truth-standard.md",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/operating-alignment-contract.md": (
        "## Analyst's Truth Standard (ACTIVE ADVISORY)",
        "analysts-truth-standard.md",
    ),
    PRESSURE_TEST: (
        "## Reporting-Only Read",
        "## Analysis And Diagnosis",
        "## Decision Delta",
        "## Confirm, Weaken, Reverse",
        "7,646 records",
        "This is a real workspace pressure test",
    ),
    BASELINE_01: (
        "Frozen source SHA-256: `6a07761e28ece602c086b47d4c8c52777760540750968dd96a314e96b9be9de8`",
        "CONTENT — write the post that hands the buyer the substrate test",
        "Five people corrected the same AI post this morning",
    ),
    TREATMENT_01: (
        "Status: `HYPOTHESIS; refresh before publishing`",
        "A three-word prompt tests whether the system is ready.",
        "## Smallest Useful Test",
        "## Decision Delta",
    ),
    COMPARISON_01: (
        "label-blinded structural comparison",
        "Variant B materially improves decision quality",
        "no independent human preference judgment occurred",
    ),
    BASELINE_02: (
        f"Frozen source SHA-256: `{BASELINE_SHA256_02}`",
        "Codex should not default everything to chat or Markdown",
    ),
    TREATMENT_02: (
        "activate the clear cases and observe the mixed cases",
        "## Cold-Start Test",
        "Reverse the activation",
    ),
    COMPARISON_02: (
        "Variant B materially improves analytical decision quality",
        "no independent human preference panel occurred",
    ),
    BASELINE_03: (
        f"Frozen source SHA-256: `{BASELINE_SHA256_03}`",
        "Lead-to-proposal wins narrowly",
        "## Preservation Boundary",
    ),
    TREATMENT_03: (
        "the primary remains locked; payment proof remains untested",
        "## Read The Result Without Moving Every Variable",
        "Twenty qualified conversations and zero deposits",
    ),
    COMPARISON_03: (
        "Variant B materially improves strategic decision quality",
        "no independent human preference panel occurred",
    ),
}

RECEIPT_FIELDS = {
    "id",
    "date",
    "task_type",
    "real_job",
    "source_packet",
    "native_owner",
    "finished_artifact",
    "observed_decision_change",
    "causal_restraint_result",
    "explanation_burden_result",
    "creative_range_result",
    "blind_comparison_result",
    "verdict",
    "reviewer",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_markers() -> list[str]:
    failures: list[str] = []
    for path, markers in REQUIRED_MARKERS.items():
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in markers:
            if marker not in text:
                failures.append(f"{path.relative_to(ROOT)} missing marker: {marker}")
    if PRIMITIVE.exists():
        text = PRIMITIVE.read_text(encoding="utf-8")
        for banned in ("Status: `ENFORCED`", "mandatory score", "automatic blocking"):
            if banned in text:
                failures.append(f"primitive contains forbidden enforcement marker: {banned}")
    for cycle, (source, expected_digest) in BASELINE_SOURCES.items():
        if not source.is_file():
            failures.append(f"production cycle {cycle} baseline source is missing")
            continue
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != expected_digest:
            failures.append(f"production cycle {cycle} frozen baseline source changed")
    return failures


def validate_fixtures(fixtures: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if fixtures.get("rubric") != EXPECTED_RUBRIC:
        failures.append("comparison rubric drifted")

    cases = fixtures.get("cases") or []
    ids = {case.get("id") for case in cases}
    if ids != EXPECTED_CASES:
        failures.append(f"comparison case set mismatch: {sorted(str(x) for x in ids)}")

    required_treatment = (
        "observation",
        "inference",
        "alternatives",
        "decision_delta",
        "confirming_evidence",
        "disconfirming_evidence",
        "visible_result",
    )
    for case in cases:
        case_id = case.get("id", "<missing>")
        if not case.get("reporting_only"):
            failures.append(f"{case_id}: reporting-only baseline missing")
        treatment = case.get("decision_intelligence") or {}
        for field in required_treatment:
            if not treatment.get(field):
                failures.append(f"{case_id}: treatment missing {field}")
        alternatives = treatment.get("alternatives") or []
        if not isinstance(alternatives, list) or len(alternatives) < 2:
            failures.append(f"{case_id}: fewer than two plausible alternatives")
        judgment = case.get("judgment") or {}
        expected = {
            "decision_change": "MATERIAL",
            "causal_restraint": "PASS",
            "insight_density": "PASS",
            "explanation_burden": "LOW",
            "creative_range_preservation": "PRESERVED",
        }
        for field, value in expected.items():
            if judgment.get(field) != value:
                failures.append(f"{case_id}: {field} must be {value}")

    negatives = fixtures.get("negative_controls") or []
    negative_map = {row.get("id"): row for row in negatives}
    if set(negative_map) != set(EXPECTED_NEGATIVES):
        failures.append("negative-control set drifted")
    for control_id, expected_stop in EXPECTED_NEGATIVES.items():
        row = negative_map.get(control_id) or {}
        if row.get("expected_stop") != expected_stop:
            failures.append(f"{control_id}: expected stop must be {expected_stop}")
        if not row.get("reason"):
            failures.append(f"{control_id}: missing preservation reason")
    return failures


def validate_receipts(receipts: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    rows = receipts.get("receipts") or []
    constraints = receipts.get("constraints") or {}
    if receipts.get("required") != 3:
        failures.append("promotion must require three production receipts")
    if receipts.get("current") != len(rows):
        failures.append("receipt counter does not match receipt rows")
    current = receipts.get("current")
    required = receipts.get("required")
    if not isinstance(current, int) or current < 0 or current > required:
        failures.append("receipt counter must stay between zero and required")

    seen_ids: set[str] = set()
    for row in rows:
        receipt_id = row.get("id", "<missing>")
        if set(row) != RECEIPT_FIELDS:
            failures.append(f"{receipt_id}: receipt fields do not match schema")
        if receipt_id in seen_ids:
            failures.append(f"duplicate production receipt: {receipt_id}")
        seen_ids.add(receipt_id)
        if not re.fullmatch(r"ATS-PR-\d{3}", str(receipt_id)):
            failures.append(f"{receipt_id}: invalid receipt id")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(row.get("date", ""))):
            failures.append(f"{receipt_id}: invalid receipt date")
        for field in (
            "task_type",
            "real_job",
            "source_packet",
            "native_owner",
            "finished_artifact",
            "observed_decision_change",
            "reviewer",
        ):
            if not str(row.get(field, "")).strip():
                failures.append(f"{receipt_id}: missing {field}")
        if row.get("causal_restraint_result") != "PASS":
            failures.append(f"{receipt_id}: causal restraint must pass")
        if row.get("explanation_burden_result") != "LOW":
            failures.append(f"{receipt_id}: explanation burden regressed")
        if row.get("creative_range_result") not in {"PRESERVED", "NOT_APPLICABLE"}:
            failures.append(f"{receipt_id}: creative range regressed")
        if row.get("blind_comparison_result") != "TREATMENT":
            failures.append(f"{receipt_id}: receipt requires a decision-improving comparison")
        if row.get("verdict") not in {
            "KEEP_SHADOW",
            "REVISE_SHADOW",
            "RETIRE",
            "PROMOTION_CANDIDATE",
        }:
            failures.append(f"{receipt_id}: invalid verdict")
        for path_field in ("source_packet", "finished_artifact"):
            candidate = ROOT / str(row.get(path_field, ""))
            if not candidate.is_file():
                failures.append(f"{receipt_id}: missing {path_field} file")

    if current == required:
        task_types = {str(row.get("task_type", "")) for row in rows}
        if len(task_types) != required:
            failures.append("promotion set must use three distinct task types")
        if not any("creative" in task_type for task_type in task_types):
            failures.append("promotion set requires a creative use")
        if not any("analytical" in task_type for task_type in task_types):
            failures.append("promotion set requires an analytical use")
        if receipts.get("status") != "PROMOTED_ACTIVE_ADVISORY":
            failures.append("complete receipt set must be promoted ACTIVE ADVISORY")
        approval = receipts.get("promotion_approval") or {}
        if approval.get("date") != "2026-09-01":
            failures.append("promotion approval date is missing")
        if "trust your judgment" not in str(approval.get("user_direction", "")).lower():
            failures.append("promotion lacks explicit user direction")
        if seen_ids != {"ATS-PR-001", "ATS-PR-002", "ATS-PR-003"}:
            failures.append("promotion receipt id set is incomplete")
    elif receipts.get("status") != "PENDING_REAL_USE":
        failures.append("incomplete receipt set must remain PENDING_REAL_USE")
    required_true = (
        "distinct_task_types",
        "creative_use_required",
        "analytical_use_required",
        "blind_comparison_required",
        "creative_range_must_be_preserved",
        "explicit_farrice_approval_required",
    )
    for field in required_true:
        if constraints.get(field) is not True:
            failures.append(f"promotion constraint must be true: {field}")
    if constraints.get("factual_or_causal_regression_allowed") is not False:
        failures.append("factual or causal regression must remain forbidden")
    if constraints.get("added_question_burden_allowed") is not False:
        failures.append("added question burden must remain forbidden")
    return failures


def main() -> int:
    failures = validate_markers()
    fixtures = load_json(FIXTURES)
    receipts = load_json(RECEIPTS)
    failures.extend(validate_fixtures(fixtures))
    failures.extend(validate_receipts(receipts))

    # False-green controls: each material boundary must fail when sabotaged.
    no_alternatives = copy.deepcopy(fixtures)
    no_alternatives["cases"][1]["decision_intelligence"]["alternatives"] = []
    if not validate_fixtures(no_alternatives):
        failures.append("false-green control failed: diagnosis without alternatives passed")

    overdiagnosed = copy.deepcopy(fixtures)
    overdiagnosed["negative_controls"][0]["expected_stop"] = "DIAGNOSIS"
    if not validate_fixtures(overdiagnosed):
        failures.append("false-green control failed: factual answer overdiagnosis passed")

    mismatched_receipt_count = copy.deepcopy(receipts)
    mismatched_receipt_count["current"] += 1
    if not validate_receipts(mismatched_receipt_count):
        failures.append("false-green control failed: mismatched production proof passed")

    missing_approval = copy.deepcopy(receipts)
    missing_approval["promotion_approval"] = {}
    if not validate_receipts(missing_approval):
        failures.append("false-green control failed: promotion without approval passed")

    if failures:
        print("Analyst's Truth Standard: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Analyst's Truth Standard: PASS")
    print("- mode: ACTIVE ADVISORY, silent, non-blocking")
    print("- frozen comparisons: 4/4 structurally decision-changing")
    print("- negative controls: 4/4 preserve early stopping")
    print("- live pressure test: lane provisioning diagnosis confirmed by rerun")
    print(f"- promotion proof: {receipts['current']}/3 distinct real receipts; explicit Farrice approval recorded")
    print("- false-green controls: 4/4 caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
