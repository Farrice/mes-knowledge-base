#!/usr/bin/env python3
"""Derive and verify a RelayNote behavior verdict from raw, hash-bound run evidence."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "skills/kyle-milligan-copy-chief/tests/fixtures/relaynote"
SPEAKER_LEDGER = ROOT / "extractions/kyle-milligan-copywriting/speaker-ledger.jsonl"
SPEAKER_MANIFEST = ROOT / "extractions/kyle-milligan-copywriting/speaker-ledger.manifest.json"
EXPECTED_RQ_WEIGHTS = {
    "RQ-01": 20,
    "RQ-02": 15,
    "RQ-03": 15,
    "RQ-04": 15,
    "RQ-05": 15,
    "RQ-06": 10,
    "RQ-07": 5,
    "RQ-08": 5,
}
EXPECTED_KF_IDS = {f"KF-{index:02d}" for index in range(1, 13)}
EXPECTED_AC_IDS = {f"AC-{index:02d}" for index in range(1, 19)}
PROOF_BOUNDARY = "Synthetic detached fixture behavior only; not market evidence or A-tier embodiment proof."
ACCEPTANCE_HEADINGS = [
    "# Acceptance Result",
    "## Case",
    "## Decision",
    "## Evidence",
    "## Required Action",
    "## Prohibited Action",
    "## Proof Boundary",
]
MECHANIC_CONTRACT = {
    "KM-531": {"name": "5-3-1 primary-swipe discipline", "rows": {"SL-023"}},
    "KM-PROMISE": {"name": "evidence-derived singular promise", "rows": {"SL-009", "SL-011"}},
    "KM-FOUR-BEAT": {"name": "claim-to-demonstration four-beat progression", "rows": {"SL-038"}},
    "KM-FIRST-FOUR": {"name": "first-four continuation repair", "rows": {"SL-006", "SL-045"}},
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_digest(path: Path, errors: list[str], label: str | None = None) -> str:
    try:
        return digest(path)
    except OSError as exc:
        errors.append(f"{label or path}: cannot hash file: {exc}")
        return ""


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid or missing JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: top-level value must be an object")
        return {}
    return value


def expected_run_paths() -> set[str]:
    paths = {
        "proof-receipt.json",
        "method-deltas.json",
        "provenance/run-plan.json",
        "provenance/run-events.jsonl",
        "provenance/attempt-ledger.json",
        "provenance/runtime-parity.json",
        "provenance/fairness-repair.json",
        "blind/label-map.commitment.json",
        "blind/label-map.revealed.json",
        "blind/packet-manifest.json",
        "blind/evaluator-receipt.json",
        "blind/scores.json",
        "blind/scores.seal.json",
        "fidelity/evaluator-receipt.json",
    }
    for replicate in range(1, 4):
        paths.update(
            {
                f"blind/pair-{replicate}-X.md",
                f"blind/pair-{replicate}-Y.md",
                f"arms/arm-b/replicate-{replicate}-initial.md",
                f"arms/arm-b/replicate-{replicate}-audit.md",
                f"arms/arm-b/replicate-{replicate}-final.md",
                f"arms/arm-c/replicate-{replicate}-swipe-packet.md",
                f"arms/arm-c/replicate-{replicate}-promise-card.md",
                f"arms/arm-c/replicate-{replicate}-initial.md",
                f"arms/arm-c/replicate-{replicate}-audit.md",
                f"arms/arm-c/replicate-{replicate}-final.md",
                f"route-receipts/arm-b-{replicate}.json",
                f"route-receipts/arm-c-{replicate}.json",
            }
        )
    for index in range(1, 19):
        paths.add(f"acceptance/AC-{index:02d}.md")
        paths.add(f"acceptance/AC-{index:02d}.route.json")
    return paths


def verify_manifest(run_dir: Path, fixture_hash: str, errors: list[str]) -> dict:
    manifest_path = run_dir / "run-manifest.json"
    manifest = load_json(manifest_path, errors)
    actual = sorted(
        path for path in run_dir.rglob("*")
        if path.is_file() and path != manifest_path
    )
    actual_paths = [str(path.relative_to(run_dir)) for path in actual]
    if set(actual_paths) != expected_run_paths():
        missing = sorted(expected_run_paths() - set(actual_paths))
        extra = sorted(set(actual_paths) - expected_run_paths())
        errors.append(f"run inventory drifted; missing={missing}, extra={extra}")
    if any(path.is_symlink() for path in run_dir.rglob("*")):
        errors.append("run bundle may not contain symlinks")
    listed = manifest.get("files", [])
    if not isinstance(listed, list) or any(not isinstance(entry, dict) for entry in listed):
        errors.append("run manifest files must be an array of objects")
        return manifest
    if [entry.get("path") for entry in listed] != actual_paths:
        errors.append("run manifest does not exactly list sorted run evidence")
    for entry in listed:
        relative = entry.get("path", "")
        if not isinstance(relative, str):
            errors.append("run manifest path entries must be strings")
            continue
        path = run_dir / relative
        try:
            path.resolve().relative_to(run_dir.resolve())
        except ValueError:
            errors.append(f"run manifest path escapes run root: {relative}")
            continue
        if not path.is_file():
            errors.append(f"run manifest lists missing file: {entry.get('path')}")
            continue
        if entry.get("sha256") != safe_digest(path, errors) or entry.get("bytes") != path.stat().st_size:
            errors.append(f"run evidence hash/size mismatch: {entry.get('path')}")
    if manifest.get("fixture_manifest_sha256") != fixture_hash:
        errors.append("run manifest is not bound to the current frozen fixture")
    if manifest.get("proof_boundary") != PROOF_BOUNDARY:
        errors.append("run manifest proof boundary drifted")
    return manifest


def verify_output(path: Path, product: dict, veto: dict, errors: list[str]) -> None:
    try:
        text = path.read_text()
    except OSError as exc:
        errors.append(f"{path}: cannot read output: {exc}")
        return
    expected_headings = [
        "## Opening 1",
        "### Opening 1 Evidence Map",
        "## Opening 2",
        "### Opening 2 Evidence Map",
        "## Opening 3",
        "### Opening 3 Evidence Map",
        "## Recommendation",
        "### Recommendation Evidence Map",
    ]
    actual_headings = [line.strip() for line in text.splitlines() if line.startswith("#")]
    if actual_headings != expected_headings:
        errors.append(f"{path}: exact output headings/order violated: {actual_headings}")
        return

    allowed_truth_ids = {item["id"] for item in product.get("truths", [])}
    hypotheses: list[str] = []
    production_copy: list[str] = []
    next_heading = {1: "## Opening 2", 2: "## Opening 3", 3: "## Recommendation"}
    for index in range(1, 4):
        opening_marker = f"## Opening {index}"
        evidence_marker = f"### Opening {index} Evidence Map"
        opening_start = text.index(opening_marker) + len(opening_marker)
        opening_end = text.index(evidence_marker)
        evidence_start = opening_end + len(evidence_marker)
        evidence_end = text.index(next_heading[index])
        opening = text[opening_start:opening_end].strip()
        evidence = text[evidence_start:evidence_end].strip()
        lines = [line.strip() for line in opening.splitlines() if line.strip()]
        evidence_lines = [line.strip() for line in evidence.splitlines() if line.strip()]
        production_copy.extend(lines)
        words = re.findall(r"\b[\w’'-]+\b", opening)
        if not (4 <= len(lines) <= 8):
            errors.append(f"{path}: Opening {index} has {len(lines)} lines; required 4–8")
        if not (55 <= len(words) <= 115):
            errors.append(f"{path}: Opening {index} has {len(words)} words; required 55–115")
        if opening.lower().count("book a demo") != 1:
            errors.append(f"{path}: Opening {index} must contain Book a demo exactly once")
        if lines and not any("book a demo" in line.lower() for line in lines[2:]):
            errors.append(f"{path}: Opening {index} places the action before the promise/proof spine")
        if not evidence_lines or not evidence_lines[0].startswith("- Hypothesis: "):
            errors.append(f"{path}: Opening {index} lacks the machine-readable hypothesis row")
            hypothesis = ""
        else:
            hypothesis = evidence_lines[0].split(":", 1)[1].strip().lower()
            if not hypothesis:
                errors.append(f"{path}: Opening {index} hypothesis is empty")
        hypotheses.append(hypothesis)

        mappings: dict[int, tuple[str, set[str]]] = {}
        mapping_pattern = re.compile(r"^- Line ([1-9][0-9]*): (.+) \| Evidence: (PT-[A-Z]+-[0-9]{3}(?:,PT-[A-Z]+-[0-9]{3})*)$")
        for row in evidence_lines[1:]:
            match = mapping_pattern.fullmatch(row)
            if not match:
                errors.append(f"{path}: Opening {index} malformed evidence row: {row}")
                continue
            line_number = int(match.group(1))
            ids = set(match.group(3).split(","))
            if line_number in mappings:
                errors.append(f"{path}: Opening {index} duplicates evidence for line {line_number}")
            if not ids.issubset(allowed_truth_ids):
                errors.append(f"{path}: Opening {index} line {line_number} uses unknown Product Truth IDs")
            mappings[line_number] = (match.group(2), ids)
        if set(mappings) != set(range(1, len(lines) + 1)):
            errors.append(f"{path}: Opening {index} does not map every line exactly once")
        for line_number, line in enumerate(lines, 1):
            mapped_text, ids = mappings.get(line_number, ("", set()))
            if mapped_text != line:
                errors.append(f"{path}: Opening {index} line {line_number} evidence text is not verbatim")
            lower_line = line.lower()
            lower_opening = opening.lower()
            if "book a demo" in lower_line and "PT-ACT-001" not in ids:
                errors.append(f"{path}: Opening {index} CTA is not mapped to PT-ACT-001")
            if ("transcript" in lower_line or "draft follow-up" in lower_line) and "PT-CAP-001" not in ids:
                errors.append(f"{path}: Opening {index} transcript-to-draft claim lacks PT-CAP-001")
            if ("owner and date" in lower_line or "owner/date" in lower_line) and (
                "PT-CAP-002" not in ids or "when" not in lower_line
            ):
                errors.append(f"{path}: Opening {index} owner/date claim loses its PT-CAP-002 when-present boundary")
            if "23%" in lower_line and not {"PT-MET-001", "PT-TEST-001", "PT-TEST-003"}.issubset(ids):
                errors.append(f"{path}: Opening {index} 23% line lacks metric, synthetic-test, or denominator IDs")
            if "23%" in lower_opening and not ("1,248" in lower_opening and "synthetic" in lower_opening and "manual" in lower_opening):
                errors.append(f"{path}: Opening {index} 23% claim lacks its full synthetic/manual denominator context")
            if "18 minutes" in lower_line and "PT-MET-002" not in ids:
                errors.append(f"{path}: Opening {index} 18-minute claim lacks PT-MET-002")
            if "4 minutes" in lower_line and "PT-MET-003" not in ids:
                errors.append(f"{path}: Opening {index} 4-minute claim lacks PT-MET-003")
            if "91%" in lower_line and "PT-MET-004" not in ids:
                errors.append(f"{path}: Opening {index} 91% claim lacks PT-MET-004")
            if "91%" in lower_opening and not ("held-out" in lower_opening and "200-call" in lower_opening and ("synthetic" in lower_opening or "fixture" in lower_opening)):
                errors.append(f"{path}: Opening {index} 91% claim lacks held-out 200-call fixture context")
        for token in ("23%", "18 minutes", "4 minutes", "91%", "30-day", "1,248", "200-call"):
            if token in opening.lower() and not any(label in opening.lower() for label in ("synthetic", "fixture")):
                errors.append(f"{path}: Opening {index} uses {token} without synthetic/fixture qualification")

    if len(set(hypotheses)) != 3 or "" in hypotheses:
        errors.append(f"{path}: the three opening hypotheses are not distinct and non-empty")

    recommendation_start = text.index("## Recommendation") + len("## Recommendation")
    recommendation_end = text.index("### Recommendation Evidence Map")
    recommendation = text[recommendation_start:recommendation_end].strip()
    recommendation_map = text[recommendation_end + len("### Recommendation Evidence Map"):].strip()
    recommendation_rows = [line.strip() for line in recommendation_map.splitlines() if line.strip()]
    if len(re.findall(r"\b[\w’'-]+\b", recommendation)) > 90:
        errors.append(f"{path}: recommendation exceeds 90 words")
    if not recommendation_rows or not re.fullmatch(r"- Selected: Opening [1-3]", recommendation_rows[0]):
        errors.append(f"{path}: recommendation does not select exactly one opening")
    else:
        selected = recommendation_rows[0].removeprefix("- Selected: ")
        if selected.lower() not in recommendation.lower():
            errors.append(f"{path}: recommendation prose does not name the selected opening")
        other_openings = {f"opening {index}" for index in range(1, 4)} - {selected.lower()}
        if any(other in recommendation.lower() for other in other_openings) or "blend" in recommendation.lower():
            errors.append(f"{path}: recommendation blends or compares multiple options")
    rationale_labels = ["Audience fit", "Singular promise", "Proof fit", "Continuation strength"]
    if len(recommendation_rows) != 5:
        errors.append(f"{path}: Recommendation Evidence Map must contain exactly five rows")
    for offset, label in enumerate(rationale_labels, 1):
        if offset >= len(recommendation_rows):
            continue
        row = recommendation_rows[offset]
        match = re.fullmatch(rf"- {re.escape(label)}: .+ \| Evidence: (PT-[A-Z]+-[0-9]{{3}}(?:,PT-[A-Z]+-[0-9]{{3}})*)", row)
        if not match or not set(match.group(1).split(",")).issubset(allowed_truth_ids):
            errors.append(f"{path}: malformed or unknown-ID recommendation row for {label}")

    copy_text = "\n".join(production_copy).lower()
    for token in veto.get("hard_failure_tokens_in_output", []) + veto.get("hard_failure_metric_tokens_in_output", []):
        if token.lower() in copy_text:
            errors.append(f"{path}: copied control token detected: {token}")
    forbidden_phrases = (
        "revenue lift",
        "conversion lift",
        "pipeline efficiency",
        "pipeline growth",
        "closed-won",
        "78% faster",
        "14 minutes saved",
        "guarantee",
        "customer evidence",
        "market evidence",
    )
    for phrase in forbidden_phrases:
        if phrase in copy_text:
            errors.append(f"{path}: unsupported outcome/derived claim detected: {phrase}")
    for identity in ("kyle", "luke", "matthew", "workflow", "5-3-1", "four-beat", "nesb"):
        if identity in copy_text:
            errors.append(f"{path}: route or method identity leaked into production copy: {identity}")


def verify_route_receipts(
    run_dir: Path,
    receipt: dict,
    arms: dict,
    fixture_hash: str,
    errors: list[str],
) -> None:
    shared = set(arms.get("shared_inputs", []))
    b_allowed = shared | set(arms.get("arm_b", {}).get("route_specific_inputs", [])) | set(
        arms.get("arm_b", {}).get("allowed_method_reads", [])
    )
    c_allowed = shared | set(arms.get("arm_c", {}).get("route_specific_inputs", [])) | set(
        arms.get("arm_c", {}).get("allowed_method_reads", [])
    )
    run_config = json.loads((FIXTURE / "run-config.json").read_text())
    expected_settings_sha = hashlib.sha256(canonical(run_config.get("settings", {})).encode()).hexdigest()
    runtime_identities: set[tuple[str, str, str, str]] = set()
    worker_ids: set[str] = set()

    def resolve_read(relative: str) -> Path:
        if relative.startswith("skills/") or relative.startswith("extractions/"):
            return ROOT / relative
        if relative.startswith("arms/"):
            return run_dir / relative
        return FIXTURE / relative

    for arm in ("b", "c"):
        receipt_items = receipt.get(f"arm_{arm}_route_receipts", [])
        if {item.get("replicate_id") for item in receipt_items} != {1, 2, 3}:
            errors.append(f"Arm {arm.upper()} route receipt replicate IDs must be exactly 1,2,3")
        for replicate in range(1, 4):
            path = run_dir / f"route-receipts/arm-{arm}-{replicate}.json"
            item = load_json(path, errors)
            embedded = next((entry for entry in receipt_items if entry.get("replicate_id") == replicate), None)
            if embedded != item:
                errors.append(f"Arm {arm.upper()} replicate {replicate} embedded route receipt differs from file")
            if item.get("fixture_manifest_sha256") != fixture_hash or item.get("cold_start") is not True:
                errors.append(f"Arm {arm.upper()} replicate {replicate} lacks cold fixture binding")
            read_paths = set(item.get("read_paths", []))
            allowed = b_allowed if arm == "b" else c_allowed
            dynamic_allowed = {
                f"arms/arm-{arm}/replicate-{replicate}-initial.md",
                f"arms/arm-{arm}/replicate-{replicate}-audit.md",
            }
            if arm == "c":
                dynamic_allowed.update(
                    {
                        f"arms/arm-c/replicate-{replicate}-swipe-packet.md",
                        f"arms/arm-c/replicate-{replicate}-promise-card.md",
                    }
                )
            required_reads = allowed | dynamic_allowed
            if read_paths != required_reads:
                errors.append(
                    f"Arm {arm.upper()} replicate {replicate} read set differs from the frozen required set; "
                    f"missing={sorted(required_reads - read_paths)}, extra={sorted(read_paths - required_reads)}"
                )
            read_hashes = item.get("read_hashes", {})
            if set(read_hashes) != required_reads:
                errors.append(f"Arm {arm.upper()} replicate {replicate} read-hash keys differ from required reads")
            for relative in sorted(required_reads):
                local = resolve_read(relative)
                if not local.is_file() or read_hashes.get(relative) != safe_digest(local, errors, relative):
                    errors.append(f"Arm {arm.upper()} replicate {replicate} read hash mismatch: {relative}")
            expected_task = f"relaynote-arm-{arm}-replicate-{replicate}"
            if item.get("worker_task") != expected_task or item.get("attempt_ordinal") != 1:
                errors.append(f"Arm {arm.upper()} replicate {replicate} worker task/attempt is not frozen")
            worker_id = item.get("worker_id", "")
            if not worker_id or worker_id in worker_ids:
                errors.append(f"Arm {arm.upper()} replicate {replicate} worker ID is missing or reused")
            worker_ids.add(worker_id)
            if item.get("settings_sha256") != expected_settings_sha:
                errors.append(f"Arm {arm.upper()} replicate {replicate} runtime settings hash mismatch")
            runtime_identities.add(
                (
                    item.get("parent_snapshot", ""),
                    item.get("model_family", ""),
                    item.get("model_version", ""),
                    item.get("settings_sha256", ""),
                )
            )
            if arm == "b":
                if item.get("kyle_excluded") is not True:
                    errors.append(f"Arm B replicate {replicate} did not attest Kyle exclusion")
                for field in ("owner_path", "support_path", "adapter_path"):
                    local = ROOT / item.get(field, "")
                    hash_field = field.replace("path", "sha256")
                    if not local.is_file() or item.get(hash_field) != safe_digest(local, errors):
                        errors.append(f"Arm B replicate {replicate} {field} hash mismatch")
                for stage in ("initial", "audit", "final"):
                    output = run_dir / f"arms/arm-b/replicate-{replicate}-{stage}.md"
                    if item.get(f"{stage}_sha256") != safe_digest(output, errors):
                        errors.append(f"Arm B replicate {replicate} {stage} output hash mismatch")
            else:
                if item.get("baseline_methods_excluded") is not True:
                    errors.append(f"Arm C replicate {replicate} did not attest baseline exclusion")
                skill_path = ROOT / item.get("skill_path", "")
                if not skill_path.is_file() or item.get("skill_sha256") != safe_digest(skill_path, errors):
                    errors.append(f"Arm C replicate {replicate} skill hash mismatch")
                workflow_paths = item.get("workflow_paths", [])
                if workflow_paths != [
                    "skills/kyle-milligan-copy-chief/workflows/01-531-swipe-discipline.md",
                    "skills/kyle-milligan-copy-chief/workflows/02-unique-promise-spine.md",
                    "skills/kyle-milligan-copy-chief/workflows/03-four-beat-opening-builder.md",
                    "skills/kyle-milligan-copy-chief/workflows/04-first-four-lines-audit.md",
                ]:
                    errors.append(f"Arm C replicate {replicate} workflow scope must remain 01–04")
                for workflow in workflow_paths:
                    if item.get("workflow_sha256", {}).get(workflow) != safe_digest(ROOT / workflow, errors):
                        errors.append(f"Arm C replicate {replicate} workflow hash mismatch: {workflow}")
                if item.get("speaker_ledger_manifest_sha256") != safe_digest(SPEAKER_MANIFEST, errors):
                    errors.append(f"Arm C replicate {replicate} speaker-ledger manifest hash mismatch")
                for stage in ("swipe-packet", "promise-card", "initial", "audit", "final"):
                    output = run_dir / f"arms/arm-c/replicate-{replicate}-{stage}.md"
                    if item.get(f"{stage.replace('-', '_')}_sha256") != safe_digest(output, errors):
                        errors.append(f"Arm C replicate {replicate} {stage} output hash mismatch")
    if len(runtime_identities) != 1:
        errors.append(f"Arm B/C runtime parity failed: observed {len(runtime_identities)} distinct identities")


def verify_provenance(run_dir: Path, receipt: dict, fixture_hash: str, errors: list[str]) -> None:
    plan = load_json(run_dir / "provenance/run-plan.json", errors)
    attempts = load_json(run_dir / "provenance/attempt-ledger.json", errors)
    parity = load_json(run_dir / "provenance/runtime-parity.json", errors)
    fairness = load_json(run_dir / "provenance/fairness-repair.json", errors)
    run_config = json.loads((FIXTURE / "run-config.json").read_text())
    expected_settings_sha = hashlib.sha256(canonical(run_config.get("settings", {})).encode()).hexdigest()
    current_grade = run_config.get("provenance_policy", {}).get("current_available_grade")
    declared_grade = receipt.get("provenance_grade")
    if declared_grade != current_grade:
        errors.append(
            f"provenance grade {declared_grade!r} exceeds or differs from the frozen current runtime grade {current_grade!r}"
        )
    if receipt.get("registration_eligible") is not (declared_grade == "RUNTIME_OBSERVED"):
        errors.append("registration eligibility is not derived from provenance grade")
    if not receipt.get("provenance_limitations"):
        errors.append("proof receipt must state non-empty provenance limitations")
    if plan.get("schema_version") != "relaynote-run-plan/v1":
        errors.append("run plan schema version is missing or wrong")
    if plan.get("run_id") != receipt.get("run_id") or plan.get("fixture_manifest_sha256") != fixture_hash:
        errors.append("run plan is not bound to the proof receipt and frozen fixture")
    if plan.get("provenance_grade") != declared_grade or plan.get("settings_sha256") != expected_settings_sha:
        errors.append("run plan provenance/settings differ from the frozen contract")
    if plan.get("created_before_generation") is not True:
        errors.append("run plan lacks the pre-generation orchestration attestation")
    expected_tasks = {
        f"relaynote-arm-{arm}-replicate-{replicate}"
        for arm in ("b", "c")
        for replicate in range(1, 4)
    }
    planned_workers = plan.get("workers", [])
    if {item.get("worker_task") for item in planned_workers} != expected_tasks or len(planned_workers) != 6:
        errors.append("run plan must freeze exactly six arm/replicate worker tasks")
    for item in planned_workers:
        if item.get("attempt_ordinal") != 1 or item.get("fork_turns") != "none" or item.get("model_override") is not None:
            errors.append(f"run plan worker is not a one-attempt inherited-model cold start: {item.get('worker_task')}")

    attempt_rows = attempts.get("attempts", [])
    if {item.get("worker_task") for item in attempt_rows} != expected_tasks or len(attempt_rows) != 6:
        errors.append("attempt ledger must contain exactly one row for each of the six planned workers")
    worker_ids: set[str] = set()
    for item in attempt_rows:
        if item.get("attempt_ordinal") != 1 or item.get("status") != "COMPLETED":
            errors.append(f"attempt ledger contains a non-first or incomplete attempt: {item.get('worker_task')}")
        worker_id = item.get("worker_id", "")
        if not worker_id or worker_id in worker_ids:
            errors.append("attempt ledger worker IDs must be non-empty and unique")
        worker_ids.add(worker_id)
    receipt_workers = {
        item.get("worker_id")
        for key in ("arm_b_route_receipts", "arm_c_route_receipts")
        for item in receipt.get(key, [])
    }
    if worker_ids != receipt_workers:
        errors.append("attempt-ledger worker IDs differ from route receipts")

    parity_fields = parity.get("identity", {})
    route_rows = receipt.get("arm_b_route_receipts", []) + receipt.get("arm_c_route_receipts", [])
    for field in ("parent_snapshot", "model_family", "model_version", "settings_sha256"):
        values = {item.get(field) for item in route_rows}
        if len(values) != 1 or parity_fields.get(field) != next(iter(values), None):
            errors.append(f"runtime parity file does not derive the single {field} value")
    if parity.get("all_six_equal") is not True or parity.get("provenance_grade") != declared_grade:
        errors.append("runtime parity verdict/grade is inconsistent")
    if fairness.get("status") != "NONE" or fairness.get("repair_attempts") != 0:
        errors.append("this v1 run bundle does not permit hidden, partial, or post-score fairness reruns")

    try:
        events = [json.loads(line) for line in (run_dir / "provenance/run-events.jsonl").read_text().splitlines() if line]
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid provenance event log: {exc}")
        events = []
    event_ids = [item.get("event_id") for item in events]
    if len(events) < 12 or len(event_ids) != len(set(event_ids)) or any(not isinstance(event_id, int) for event_id in event_ids):
        errors.append("provenance event log must contain unique integer start/complete events")
    if event_ids != sorted(event_ids):
        errors.append("provenance event IDs are not monotonically ordered")
    for task in expected_tasks:
        kinds = [item.get("kind") for item in events if item.get("worker_task") == task]
        if kinds != ["START", "COMPLETE"]:
            errors.append(f"provenance event log lacks exactly one ordered START/COMPLETE pair for {task}")


def verify_intermediates(run_dir: Path, product: dict, veto: dict, errors: list[str]) -> None:
    def headings(path: Path) -> list[str]:
        try:
            return [line.strip() for line in path.read_text().splitlines() if line.startswith("#")]
        except OSError as exc:
            errors.append(f"{path}: cannot read intermediate: {exc}")
            return []

    def verify_revision(initial_path: Path, audit_path: Path, final_path: Path, forbidden: tuple[str, ...]) -> None:
        try:
            initial = initial_path.read_text()
            audit = audit_path.read_text()
            final = final_path.read_text()
        except OSError as exc:
            errors.append(f"revision chain cannot be read: {exc}")
            return
        if initial.strip() == final.strip():
            errors.append(f"{final_path}: revision is identical to its initial draft")
        ratio = difflib.SequenceMatcher(None, initial, final).ratio()
        if ratio > 0.995:
            errors.append(f"{final_path}: revision is only a trivial/near-identical change")
        audit_lower = audit.lower()
        for token in forbidden:
            if token in audit_lower:
                errors.append(f"{audit_path}: excluded method identity leaked into audit: {token}")
        replacements = re.findall(r"^- Replace: (.+)\n- With: (.+)$", audit, flags=re.MULTILINE)
        if not replacements:
            errors.append(f"{audit_path}: no machine-checkable Replace/With revision directive")
        for before, after in replacements:
            if len(before) < 20 or len(after) < 20:
                errors.append(f"{audit_path}: revision directive is too small to prove a substantive edit")
            if before not in initial or before in final:
                errors.append(f"{audit_path}: Replace text is not removed from the matching initial draft")
            if after not in final or after in initial:
                errors.append(f"{audit_path}: With text is not newly present in the matching final draft")

    for replicate in range(1, 4):
        b_initial = run_dir / f"arms/arm-b/replicate-{replicate}-initial.md"
        b_audit = run_dir / f"arms/arm-b/replicate-{replicate}-audit.md"
        b_final = run_dir / f"arms/arm-b/replicate-{replicate}-final.md"
        verify_output(b_initial, product, veto, errors)
        expected_b_audit_headings = [
            "# Matthew Audit",
            "## Hook",
            "## Flow",
            "## Close",
            "## Voice",
            "## Required Revision",
            "## Proof Boundary",
        ]
        if headings(b_audit) != expected_b_audit_headings:
            errors.append(f"{b_audit}: exact bounded Hook/Flow/Close/Voice audit headings violated")
        verify_revision(b_initial, b_audit, b_final, ("kyle", "5-3-1", "four-beat", "thumbtack", "mumbo jumbo"))

        swipe = run_dir / f"arms/arm-c/replicate-{replicate}-swipe-packet.md"
        promise = run_dir / f"arms/arm-c/replicate-{replicate}-promise-card.md"
        c_initial = run_dir / f"arms/arm-c/replicate-{replicate}-initial.md"
        c_audit = run_dir / f"arms/arm-c/replicate-{replicate}-audit.md"
        c_final = run_dir / f"arms/arm-c/replicate-{replicate}-final.md"
        expected_swipe_headings = [
            "# Swipe Packet",
            "## Assignment Lock",
            "## Five-Source Relevance Map",
            "## Three Breakdowns",
            "## Primary Swipe",
            "## Borrowing Boundary",
            "## Handoff",
        ]
        if headings(swipe) != expected_swipe_headings:
            errors.append(f"{swipe}: exact Swipe Packet headings violated")
        try:
            swipe_text = swipe.read_text()
        except OSError:
            swipe_text = ""
        for marker in ("S1", "S2", "S3", "S4", "S5"):
            if marker not in swipe_text:
                errors.append(f"{swipe}: missing frozen five-read marker {marker}")
        for line in (
            "Breakdown set: S2,S1,S3",
            "Primary: S2",
            "Transfer boundary: CONTROL_FACTS_AND_WORDING_FORBIDDEN",
        ):
            if line not in swipe_text.splitlines():
                errors.append(f"{swipe}: missing frozen intermediate marker: {line}")

        expected_promise_headings = [
            "# Promise Card",
            "## Classification",
            "## Evidence Graph",
            "## Candidate Promises",
            "## Locked Promise",
            "## Rejected Alternatives",
            "## NESB Evidence Check",
            "## Handoff",
        ]
        if headings(promise) != expected_promise_headings:
            errors.append(f"{promise}: exact Promise Card headings violated")
        try:
            promise_text = promise.read_text()
        except OSError:
            promise_text = ""
        for line in ("Mode: OPPORTUNITY_LED", "Mechanism status: NOT_VERIFIED_NON_APPLICABLE", "Primary swipe: S2"):
            if line not in promise_text.splitlines():
                errors.append(f"{promise}: missing frozen promise marker: {line}")
        if promise_text.count("Locked promise: ") != 1 or not re.search(r"PT-[A-Z]+-[0-9]{3}", promise_text):
            errors.append(f"{promise}: must contain exactly one PT-grounded locked promise")

        verify_output(c_initial, product, veto, errors)
        expected_c_audit_headings = [
            "# First-Four-Lines Verdict",
            "## Context Lock",
            "## Line Job Map",
            "## Verdict",
            "## Required Revision",
            "## Handoff",
            "## Proof Boundary",
        ]
        if headings(c_audit) != expected_c_audit_headings:
            errors.append(f"{c_audit}: exact bounded first-four audit headings violated")
        verify_revision(c_initial, c_audit, c_final, ("luke", "matthew", "hook/flow/close/voice"))


def verify_blind_evaluation(
    run_dir: Path,
    receipt: dict,
    errors: list[str],
) -> tuple[list[dict], float, float, float, int, list[str]]:
    commitment_path = run_dir / "blind/label-map.commitment.json"
    reveal_path = run_dir / "blind/label-map.revealed.json"
    scores_path = run_dir / "blind/scores.json"
    seal_path = run_dir / "blind/scores.seal.json"
    packet_path = run_dir / "blind/packet-manifest.json"
    evaluator_path = run_dir / "blind/evaluator-receipt.json"
    commitment = load_json(commitment_path, errors)
    reveal = load_json(reveal_path, errors)
    scores = load_json(scores_path, errors)
    score_seal = load_json(seal_path, errors)
    packet = load_json(packet_path, errors)
    evaluator = load_json(evaluator_path, errors)
    protocol = json.loads((FIXTURE / "evaluation-protocol.json").read_text())
    expected_packet_paths = {
        (f"blind/{name}" if name.startswith("pair-") or name == "label-map.commitment.json" else f"fixture/{name}")
        for name in protocol.get("blind_packet", {}).get("allowed_files", [])
    }
    packet_entries = packet.get("files", [])
    if {entry.get("path") for entry in packet_entries} != expected_packet_paths or len(packet_entries) != len(expected_packet_paths):
        errors.append("blind packet manifest does not contain the exact frozen evaluator allowlist")
    for entry in packet_entries:
        relative = entry.get("path", "")
        local = (FIXTURE / relative.removeprefix("fixture/")) if relative.startswith("fixture/") else (run_dir / relative)
        if not local.is_file() or entry.get("sha256") != safe_digest(local, errors):
            errors.append(f"blind packet hash mismatch: {relative}")
    if packet.get("run_id") != receipt.get("run_id") or packet.get("fixture_manifest_sha256") != receipt.get("fixture_manifest_sha256"):
        errors.append("blind packet is not bound to the run and fixture")
    expected_evaluator_reads = sorted(expected_packet_paths | {"blind/packet-manifest.json"})
    if evaluator.get("worker_task") != f"relaynote-blind-evaluator-{safe_digest(commitment_path, errors)[:12]}":
        errors.append("blind evaluator task is not bound to the pre-score commitment")
    if evaluator.get("fresh_context") is not True or evaluator.get("fork_turns") != "none":
        errors.append("blind evaluator was not declared as a fresh no-history worker")
    if evaluator.get("read_paths") != expected_evaluator_reads:
        errors.append("blind evaluator read set differs from its exact packet allowlist")
    if evaluator.get("packet_manifest_sha256") != safe_digest(packet_path, errors):
        errors.append("blind evaluator receipt is not bound to the packet manifest")
    if evaluator.get("scores_sha256") != safe_digest(scores_path, errors):
        errors.append("blind evaluator receipt is not bound to the raw score file")
    if evaluator.get("provenance_grade") != receipt.get("provenance_grade"):
        errors.append("blind evaluator provenance grade differs from the run")
    mapping = reveal.get("mapping", {})
    salt = reveal.get("salt", "")
    if not re.fullmatch(r"[a-f0-9]{64}", salt):
        errors.append("label-map salt must encode at least 256 bits as 64 lowercase hex characters")
    calculated_commitment = hashlib.sha256((canonical(mapping) + salt).encode()).hexdigest()
    if commitment.get("algorithm") != "sha256" or commitment.get("commitment") != calculated_commitment:
        errors.append("label-map commitment does not match revealed mapping and salt")
    if "mapping" in commitment or "salt" in commitment:
        errors.append("pre-score label commitment leaked mapping or salt")
    if commitment.get("created_before_scores") is not True or reveal.get("revealed_after_score_seal") is not True:
        errors.append("label commitment/reveal order attestations are invalid")
    if score_seal.get("scores_sha256") != safe_digest(scores_path, errors) or score_seal.get("sealed_before_label_reveal") is not True:
        errors.append("blind scores were not hash-sealed before label reveal")
    seal_bindings = {
        "run_id": receipt.get("run_id"),
        "fixture_manifest_sha256": receipt.get("fixture_manifest_sha256"),
        "packet_manifest_sha256": safe_digest(packet_path, errors),
        "label_commitment_sha256": safe_digest(commitment_path, errors),
        "scores_sha256": safe_digest(scores_path, errors),
        "evaluator_receipt_sha256": safe_digest(evaluator_path, errors),
    }
    for field, expected in seal_bindings.items():
        if score_seal.get(field) != expected:
            errors.append(f"blind score seal binding mismatch: {field}")
    if reveal.get("score_seal_sha256") != safe_digest(seal_path, errors):
        errors.append("label reveal is not bound to the score seal")
    if receipt.get("label_map_sha256") != safe_digest(reveal_path, errors):
        errors.append("proof receipt label-map hash mismatch")
    expected_mapping_keys = {"1", "2", "3"}
    if set(mapping) != expected_mapping_keys:
        errors.append("revealed label map must contain replicates 1,2,3")
    for replicate, pair in mapping.items():
        if set(pair) != {"X", "Y"} or set(pair.values()) != {"B", "C"}:
            errors.append(f"replicate {replicate} label map is not a B/C permutation")

    evaluations = scores.get("evaluations", [])
    if {item.get("replicate_id") for item in evaluations} != {1, 2, 3} or len(evaluations) != 3:
        errors.append("blind scores must contain exactly replicates 1,2,3")
    derived: list[dict] = []
    global_hard_failures: list[str] = []
    b_values: list[float] = []
    c_values: list[float] = []
    preferences_for_c = 0
    for replicate in range(1, 4):
        pair_map = mapping.get(str(replicate), {})
        evaluation = next((item for item in evaluations if item.get("replicate_id") == replicate), {})
        label_results: dict[str, dict] = {}
        for label in ("X", "Y"):
            result = evaluation.get(label, {})
            criteria = result.get("criteria", {})
            if set(criteria) != set(EXPECTED_RQ_WEIGHTS):
                errors.append(f"replicate {replicate} label {label} criterion IDs drifted")
            for criterion, maximum in EXPECTED_RQ_WEIGHTS.items():
                score = criteria.get(criterion, -1)
                if not isinstance(score, (int, float)) or not 0 <= score <= maximum:
                    errors.append(f"replicate {replicate} label {label} {criterion} score out of range")
            total = sum(criteria.get(key, 0) for key in EXPECTED_RQ_WEIGHTS)
            if result.get("total") != total:
                errors.append(f"replicate {replicate} label {label} total is not derived from criteria")
            citations = result.get("citations", {})
            if set(citations) != set(EXPECTED_RQ_WEIGHTS):
                errors.append(f"replicate {replicate} label {label} lacks criterion-by-criterion line citations")
            blind_path = run_dir / f"blind/pair-{replicate}-{label}.md"
            try:
                blind_lines = blind_path.read_text().splitlines()
            except OSError:
                blind_lines = []
            for criterion in EXPECTED_RQ_WEIGHTS:
                rows = citations.get(criterion, [])
                if not rows:
                    errors.append(f"replicate {replicate} label {label} {criterion} has no evidence citation")
                for citation in rows:
                    start = citation.get("line_start", 0)
                    end = citation.get("line_end", 0)
                    if not isinstance(start, int) or not isinstance(end, int) or not (1 <= start <= end <= len(blind_lines)):
                        errors.append(f"replicate {replicate} label {label} {criterion} citation range is invalid")
                        continue
                    excerpt = "\n".join(blind_lines[start - 1:end])
                    excerpt_sha = hashlib.sha256(excerpt.encode()).hexdigest()
                    if citation.get("excerpt_sha256") != excerpt_sha:
                        errors.append(f"replicate {replicate} label {label} {criterion} citation hash mismatch")
            failures = result.get("hard_failures", [])
            label_results[pair_map.get(label, label)] = {"score": total, "hard_failures": failures}
            global_hard_failures.extend(f"R{replicate}-{pair_map.get(label, label)}: {failure}" for failure in failures)
            arm_path = run_dir / f"arms/arm-{pair_map.get(label, '').lower()}/replicate-{replicate}-final.md"
            if not arm_path.is_file() or safe_digest(blind_path, errors) != safe_digest(arm_path, errors):
                errors.append(f"replicate {replicate} label {label} does not hash-match revealed arm output")
        b_result = label_results.get("B", {"score": 0, "hard_failures": ["missing"]})
        c_result = label_results.get("C", {"score": 0, "hard_failures": ["missing"]})
        b_values.append(b_result["score"])
        c_values.append(c_result["score"])
        preferred_label = evaluation.get("preference")
        if preferred_label not in {"X", "Y"} or not evaluation.get("rationale"):
            errors.append(f"replicate {replicate} blind preference/rationale missing")
        preference = pair_map.get(preferred_label)
        if preference == "C":
            preferences_for_c += 1
        derived.append(
            {
                "replicate_id": replicate,
                "arm_b_score": b_result["score"],
                "arm_c_score": c_result["score"],
                "arm_b_hard_failures": b_result["hard_failures"],
                "arm_c_hard_failures": c_result["hard_failures"],
                "blind_preference": preference,
            }
        )
    b_median = statistics.median(b_values)
    c_median = statistics.median(c_values)
    return derived, b_median, c_median, c_median - b_median, preferences_for_c, sorted(set(global_hard_failures))


def verify_acceptance(run_dir: Path, receipt: dict, errors: list[str]) -> tuple[bool, list[str]]:
    frozen_cases: dict[str, dict] = {}
    for line in (FIXTURE / "acceptance-cases.jsonl").read_text().splitlines():
        case = json.loads(line)
        frozen_cases[case["case_id"]] = case
    contracts = json.loads((FIXTURE / "acceptance-contracts.json").read_text())
    contract_cases = contracts.get("cases", {})
    if set(contract_cases) != EXPECTED_AC_IDS or contracts.get("common_output_headings_exact") != ACCEPTANCE_HEADINGS:
        errors.append("frozen acceptance contracts do not contain the exact 18-case heading-bound set")
    receipts = receipt.get("acceptance_receipts", [])
    if {item.get("case_id") for item in receipts} != EXPECTED_AC_IDS or len(receipts) != 18:
        errors.append("acceptance receipts must contain unique AC-01 through AC-18")
    failures: list[str] = []
    all_pass = True
    worker_ids: set[str] = set()
    base_reads = {
        "skills/kyle-milligan-copy-chief/SKILL.md",
        "skills/kyle-milligan-copy-chief/genius.md",
        "skills/kyle-milligan-copy-chief/references/source-ledger.md",
        "skills/kyle-milligan-copy-chief/references/mechanics-ledger.md",
    }
    for item in receipts:
        case_id = item.get("case_id", "")
        frozen = frozen_cases.get(case_id, {})
        contract = contract_cases.get(case_id, {})
        output = run_dir / f"acceptance/{case_id}.md"
        route_path = run_dir / f"acceptance/{case_id}.route.json"
        route = load_json(route_path, errors)
        expected_route_keys = {
            "schema_version", "case_id", "case_contract_sha256", "case_input_sha256",
            "selected_route", "selected_route_sha256", "loaded_routes", "read_paths", "read_hashes",
            "output_sha256", "worker_task", "worker_id", "attempt_ordinal", "fresh_context",
            "fork_turns", "provenance_grade",
        }
        if set(route) != expected_route_keys or route.get("schema_version") != "relaynote-acceptance-route/v1" or route.get("case_id") != case_id:
            errors.append(f"{case_id}: route receipt schema/field set drifted")
        output_hash = safe_digest(output, errors)
        route_hash = safe_digest(route_path, errors)
        contract_hash = hashlib.sha256(canonical(contract).encode()).hexdigest()
        input_hash = hashlib.sha256(canonical(frozen).encode()).hexdigest()
        if item.get("output_sha256") != output_hash or route.get("output_sha256") != output_hash:
            errors.append(f"{case_id}: acceptance output hash mismatch")
        if item.get("route_receipt_sha256") != route_hash:
            errors.append(f"{case_id}: proof receipt is not bound to its route receipt")
        if item.get("case_sha256") != contract_hash or route.get("case_contract_sha256") != contract_hash:
            errors.append(f"{case_id}: acceptance contract hash mismatch")
        if route.get("case_input_sha256") != input_hash:
            errors.append(f"{case_id}: acceptance pressure/input hash mismatch")
        if item.get("expected") != frozen.get("expected"):
            errors.append(f"{case_id}: expected behavior differs from frozen case")
        try:
            output_text = output.read_text()
        except OSError as exc:
            errors.append(f"{case_id}: cannot read acceptance output: {exc}")
            output_text = ""
        actual_headings = [line.strip() for line in output_text.splitlines() if line.startswith("#")]
        if actual_headings != ACCEPTANCE_HEADINGS:
            errors.append(f"{case_id}: exact acceptance output headings/order violated")
        normalized_lines = {line.strip() for line in output_text.splitlines() if line.strip()}
        required_lines = set(contracts.get("common_required_lines", [])) | set(contract.get("required_lines", []))
        missing_lines = sorted(required_lines - normalized_lines)
        if missing_lines:
            errors.append(f"{case_id}: missing frozen behavior markers: {missing_lines}")
        forbidden: list[str] = []
        lower_lines = {line.lower() for line in normalized_lines}
        for marker in contract.get("forbidden_lines", []):
            if ":" in marker or "=" in marker:
                present = marker.lower() in lower_lines
            else:
                present = re.search(rf"\b{re.escape(marker.lower())}\b", output_text.lower()) is not None
            if present:
                forbidden.append(marker)
        if forbidden:
            errors.append(f"{case_id}: forbidden behavior markers present: {forbidden}")
        decision_rows = [line for line in normalized_lines if line.startswith("Decision: ")]
        derived_decision = decision_rows[0].removeprefix("Decision: ") if len(decision_rows) == 1 else "INVALID_DECISION"
        selected = contract.get("selected_route", "")
        loaded_routes = route.get("loaded_routes", [])
        read_paths = set(route.get("read_paths", []))
        prompt_stem = re.sub(r"^[0-9]+-", "", Path(selected).stem)
        required_reads = set(base_reads)
        if selected != "skills/kyle-milligan-copy-chief/SKILL.md":
            required_reads.add(selected)
            required_reads.add(f"skills/kyle-milligan-copy-chief/references/prompts-v2/{prompt_stem}.md")
        other_workflows = {
            path for path in read_paths
            if path.startswith("skills/kyle-milligan-copy-chief/workflows/") and path != selected
        }
        if loaded_routes != [selected] or other_workflows or read_paths != required_reads:
            errors.append(f"{case_id}: selected route/read set violates one-route isolation")
        for relative in sorted(read_paths):
            local = ROOT / relative
            if not local.is_file() or route.get("read_hashes", {}).get(relative) != safe_digest(local, errors):
                errors.append(f"{case_id}: route receipt read hash mismatch: {relative}")
        if set(route.get("read_hashes", {})) != read_paths:
            errors.append(f"{case_id}: route receipt read-hash keys differ from declared reads")
        if route.get("selected_route") != selected or route.get("selected_route_sha256") != safe_digest(ROOT / selected, errors):
            errors.append(f"{case_id}: frozen selected-route binding mismatch")
        if route.get("worker_task") != f"relaynote-acceptance-{case_id.lower()}" or route.get("attempt_ordinal") != 1:
            errors.append(f"{case_id}: acceptance worker task/attempt is not frozen")
        worker_id = route.get("worker_id", "")
        if not worker_id or worker_id in worker_ids:
            errors.append(f"{case_id}: acceptance worker ID is missing or reused")
        worker_ids.add(worker_id)
        if route.get("fresh_context") is not True or route.get("fork_turns") != "none":
            errors.append(f"{case_id}: acceptance worker was not a fresh isolated run")
        if route.get("provenance_grade") != receipt.get("provenance_grade"):
            errors.append(f"{case_id}: acceptance provenance grade differs from the run")

        derived_failures: list[str] = []
        if missing_lines:
            derived_failures.append("missing required behavior markers")
        if forbidden:
            derived_failures.append("forbidden behavior markers present")
        if derived_decision != frozen.get("expected"):
            derived_failures.append("derived decision differs from frozen expected behavior")
        derived_pass = not derived_failures and actual_headings == ACCEPTANCE_HEADINGS and loaded_routes == [selected] and not other_workflows
        if item.get("selected_route") != selected or item.get("loaded_routes") != loaded_routes or set(item.get("read_paths", [])) != read_paths:
            errors.append(f"{case_id}: embedded acceptance receipt differs from route evidence")
        if item.get("derived_decision") != derived_decision:
            errors.append(f"{case_id}: receipt decision is not parsed from the output")
        if item.get("hard_failures") != derived_failures or item.get("pass") is not derived_pass:
            errors.append(f"{case_id}: pass/failure fields are not verifier-derived")
        if not derived_pass:
            all_pass = False
        failures.extend(f"{case_id}: {failure}" for failure in derived_failures)
    return all_pass, sorted(set(failures))


def verify_fidelity(
    run_dir: Path,
    receipt: dict,
    acceptance_pass: bool,
    errors: list[str],
) -> tuple[bool, list[str]]:
    rubric = json.loads((FIXTURE / "kyle-fidelity-rubric.json").read_text())
    policy = rubric["evidence_policy"]
    fidelity = receipt.get("kyle_fidelity", {})
    criteria = fidelity.get("criteria", [])
    ids = [item.get("id") for item in criteria]
    if set(ids) != EXPECTED_KF_IDS or len(ids) != 12:
        errors.append("fidelity receipt must contain unique KF-01 through KF-12")
    scores = [item.get("score", -1) for item in criteria]
    for item in criteria:
        criterion_id = item.get("id")
        sources = set(item.get("evidence_sources", []))
        if criterion_id in policy.get("main_arm_required_ids", []) and not any(
            re.fullmatch(r"ARM-C-[1-3]", source) for source in sources
        ):
            errors.append(f"{criterion_id}: main Arm C evidence is required")
        required_cases = set(policy.get("acceptance_case_evidence", {}).get(criterion_id, []))
        if required_cases and not required_cases.issubset(sources):
            errors.append(f"{criterion_id}: missing required acceptance evidence {sorted(required_cases - sources)}")
        if not item.get("evidence"):
            errors.append(f"{criterion_id}: evidence explanation is empty")
        for citation in item.get("evidence_citations", []):
            relative = citation.get("path", "")
            target = run_dir / relative
            try:
                target.resolve().relative_to(run_dir.resolve())
            except ValueError:
                errors.append(f"{criterion_id}: evidence citation escapes run root")
                continue
            if not target.is_file():
                errors.append(f"{criterion_id}: evidence citation target is missing: {relative}")
                continue
            lines = target.read_text().splitlines()
            start = citation.get("line_start", 0)
            end = citation.get("line_end", 0)
            if not isinstance(start, int) or not isinstance(end, int) or not (1 <= start <= end <= len(lines)):
                errors.append(f"{criterion_id}: evidence citation range is invalid: {relative}")
                continue
            excerpt = "\n".join(lines[start - 1:end])
            if citation.get("excerpt_sha256") != hashlib.sha256(excerpt.encode()).hexdigest():
                errors.append(f"{criterion_id}: evidence citation hash mismatch: {relative}")
            source_matches = False
            for source in sources:
                if re.fullmatch(r"ARM-C-[1-3]", source):
                    source_matches |= relative.startswith(f"arms/arm-c/replicate-{source[-1]}-")
                elif re.fullmatch(r"AC-[0-9]{2}", source):
                    source_matches |= relative == f"acceptance/{source}.md"
            if not source_matches:
                errors.append(f"{criterion_id}: citation path is not authorized by its evidence sources: {relative}")
    minimum = min(scores) if scores else -1
    truth_item = next((item for item in criteria if item.get("id") == "KF-12"), {})
    derived_pass = minimum >= 7 and truth_item.get("score") == 10 and acceptance_pass
    if fidelity.get("minimum_score") != minimum or fidelity.get("truth_score") != truth_item.get("score"):
        errors.append("fidelity summary scores are not derived from criterion rows")
    if fidelity.get("pass") is not derived_pass:
        errors.append("fidelity pass flag is not derived from scores and acceptance evidence")

    fidelity_evaluator_path = run_dir / "fidelity/evaluator-receipt.json"
    fidelity_evaluator = load_json(fidelity_evaluator_path, errors)
    expected_fidelity_reads = {
        "fixture/kyle-fidelity-rubric.json",
        "fixture/acceptance-contracts.json",
        "extractions/kyle-milligan-copywriting/speaker-ledger.jsonl",
    }
    for replicate in range(1, 4):
        for stage in ("swipe-packet", "promise-card", "initial", "audit", "final"):
            expected_fidelity_reads.add(f"arms/arm-c/replicate-{replicate}-{stage}.md")
    expected_fidelity_reads.update(f"acceptance/AC-{index:02d}.md" for index in range(1, 19))
    expected_fidelity_keys = {
        "schema_version", "worker_task", "worker_id", "fresh_context", "fork_turns",
        "read_paths", "read_hashes", "fidelity_payload_sha256", "provenance_grade",
    }
    if set(fidelity_evaluator) != expected_fidelity_keys or fidelity_evaluator.get("schema_version") != "relaynote-fidelity-evaluator/v1":
        errors.append("fidelity evaluator receipt schema/field set drifted")
    if fidelity_evaluator.get("worker_task") != "relaynote-fidelity-evaluator" or fidelity_evaluator.get("fresh_context") is not True or fidelity_evaluator.get("fork_turns") != "none":
        errors.append("fidelity evaluator was not a fresh, frozen worker task")
    if set(fidelity_evaluator.get("read_paths", [])) != expected_fidelity_reads:
        errors.append("fidelity evaluator read set differs from its exact allowlist")
    if not fidelity_evaluator.get("worker_id"):
        errors.append("fidelity evaluator worker ID is missing")
    read_hashes = fidelity_evaluator.get("read_hashes", {})
    if set(read_hashes) != expected_fidelity_reads:
        errors.append("fidelity evaluator read-hash keys differ from its allowlist")
    for relative in sorted(expected_fidelity_reads):
        if relative.startswith("fixture/"):
            local = FIXTURE / relative.removeprefix("fixture/")
        elif relative.startswith("extractions/"):
            local = ROOT / relative
        else:
            local = run_dir / relative
        if not local.is_file() or read_hashes.get(relative) != safe_digest(local, errors):
            errors.append(f"fidelity evaluator read hash mismatch: {relative}")
    payload_sha = hashlib.sha256(canonical(fidelity).encode()).hexdigest()
    if fidelity_evaluator.get("fidelity_payload_sha256") != payload_sha:
        errors.append("fidelity evaluator receipt is not bound to the scored payload")
    if fidelity_evaluator.get("provenance_grade") != receipt.get("provenance_grade"):
        errors.append("fidelity evaluator provenance grade differs from the run")

    deltas_doc = load_json(run_dir / "method-deltas.json", errors)
    deltas = deltas_doc.get("deltas", [])
    visible = receipt.get("visible_kyle_mechanics", [])
    speaker_rows = {json.loads(line)["row_id"]: json.loads(line) for line in SPEAKER_LEDGER.read_text().splitlines()}
    if deltas_doc.get("schema_version") != "relaynote-method-deltas/v2" or set(deltas_doc) != {"notice", "schema_version", "deltas"}:
        errors.append("method-deltas document schema/field set drifted")
    if len({item.get("mechanic_id") for item in deltas}) != len(deltas):
        errors.append("method-delta mechanic IDs must be unique")
    if {item.get("mechanic_id") for item in visible} != {item.get("mechanic_id") for item in deltas} or len(visible) != len(deltas):
        errors.append("visible-mechanics receipt must exactly mirror the method-delta set")
    delta_replicates: set[int] = set()
    for delta in deltas:
        expected_delta_keys = {
            "mechanic_id", "name", "replicate_id", "before_path", "after_path", "audit_path",
            "before_line_start", "before_line_end", "after_line_start", "after_line_end",
            "before_excerpt", "after_excerpt", "before_excerpt_sha256", "after_excerpt_sha256",
            "audit_directive", "source_rows", "delta_sha256", "output_delta",
        }
        if set(delta) != expected_delta_keys:
            errors.append(f"method delta field set drifted: {delta.get('mechanic_id')}")
        mechanic_id = delta.get("mechanic_id", "")
        contract = MECHANIC_CONTRACT.get(mechanic_id)
        replicate = delta.get("replicate_id")
        if not contract or delta.get("name") != (contract or {}).get("name") or replicate not in (1, 2, 3):
            errors.append(f"method delta has an unfrozen mechanic/name/replicate: {mechanic_id}")
            continue
        delta_replicates.add(replicate)
        expected_before = f"arms/arm-c/replicate-{replicate}-initial.md"
        expected_after = f"arms/arm-c/replicate-{replicate}-final.md"
        expected_audit = f"arms/arm-c/replicate-{replicate}-audit.md"
        if delta.get("before_path") != expected_before or delta.get("after_path") != expected_after or delta.get("audit_path") != expected_audit:
            errors.append(f"method delta {mechanic_id} is not same-replicate Arm C initial-to-final evidence")
            continue
        before_path = run_dir / expected_before
        after_path = run_dir / expected_after
        audit_path = run_dir / expected_audit
        if not before_path.is_file() or not after_path.is_file() or not audit_path.is_file():
            errors.append(f"method delta {mechanic_id} references missing output")
            continue
        before_excerpt = delta.get("before_excerpt", "")
        after_excerpt = delta.get("after_excerpt", "")
        before_lines = before_path.read_text().splitlines()
        after_lines = after_path.read_text().splitlines()
        before_start, before_end = delta.get("before_line_start", 0), delta.get("before_line_end", 0)
        after_start, after_end = delta.get("after_line_start", 0), delta.get("after_line_end", 0)
        if not all(isinstance(value, int) for value in (before_start, before_end, after_start, after_end)) or not (
            1 <= before_start <= before_end <= len(before_lines) and 1 <= after_start <= after_end <= len(after_lines)
        ):
            errors.append(f"method delta {mechanic_id} has invalid line spans")
            continue
        derived_before = "\n".join(before_lines[before_start - 1:before_end])
        derived_after = "\n".join(after_lines[after_start - 1:after_end])
        if before_excerpt != derived_before or after_excerpt != derived_after:
            errors.append(f"method delta {mechanic_id} excerpts are not derived from declared spans")
        if delta.get("before_excerpt_sha256") != hashlib.sha256(before_excerpt.encode()).hexdigest() or delta.get("after_excerpt_sha256") != hashlib.sha256(after_excerpt.encode()).hexdigest():
            errors.append(f"method delta {mechanic_id} excerpt hashes mismatch")
        normalized_before = re.sub(r"[^a-z0-9]+", "", before_excerpt.lower())
        normalized_after = re.sub(r"[^a-z0-9]+", "", after_excerpt.lower())
        if len(normalized_before) < 20 or len(normalized_after) < 20 or normalized_before == normalized_after:
            errors.append(f"method delta {mechanic_id} is trivial, empty, or punctuation-only")
        if before_excerpt in after_path.read_text() or after_excerpt in before_path.read_text():
            errors.append(f"method delta {mechanic_id} does not show a removed-before/new-after change")
        directive = f"- Replace: {before_excerpt}\n- With: {after_excerpt}"
        if delta.get("audit_directive") != directive or directive not in audit_path.read_text():
            errors.append(f"method delta {mechanic_id} is not bound to the matching audit directive")
        source_rows = set(delta.get("source_rows", []))
        if not source_rows or not source_rows.issubset(contract["rows"]):
            errors.append(f"method delta {mechanic_id} uses source rows outside its frozen allowlist")
        for row_id in source_rows:
            row = speaker_rows.get(row_id, {})
            if row.get("speaker_class") != "KYLE" or row.get("truth_class") != "OBSERVED" or row.get("claim_kind") != "METHOD":
                errors.append(f"method delta {mechanic_id} source row is not eligible Kyle-observed method evidence: {row_id}")
        delta_material = {
            "mechanic_id": mechanic_id,
            "replicate_id": replicate,
            "before_path": expected_before,
            "after_path": expected_after,
            "before_excerpt": before_excerpt,
            "after_excerpt": after_excerpt,
            "source_rows": sorted(source_rows),
        }
        derived_delta_sha = hashlib.sha256(canonical(delta_material).encode()).hexdigest()
        if delta.get("delta_sha256") != derived_delta_sha:
            errors.append(f"method delta {mechanic_id} binding hash mismatch")
        expected_output_delta = f"R{replicate} {mechanic_id}: initial lines {before_start}-{before_end} -> final lines {after_start}-{after_end}"
        if delta.get("output_delta") != expected_output_delta:
            errors.append(f"method delta {mechanic_id} output_delta is not verifier-derived")
        matching = next((item for item in visible if item.get("mechanic_id") == mechanic_id), None)
        expected_visible = {
            "mechanic_id": mechanic_id,
            "name": contract["name"],
            "replicate_id": replicate,
            "source_rows": sorted(source_rows),
            "delta_sha256": derived_delta_sha,
            "output_delta": expected_output_delta,
        }
        if matching != expected_visible:
            errors.append(f"method delta {mechanic_id} differs from the proof receipt")
    if len(deltas) < 3 or len(visible) < 3 or len(delta_replicates) < 2:
        derived_pass = False
    return derived_pass, []


def verify_schema(receipt: dict, errors: list[str]) -> None:
    schema = json.loads((FIXTURE / "post-run-receipt.schema.json").read_text())
    try:
        import jsonschema  # type: ignore

        jsonschema.Draft202012Validator.check_schema(schema)
        validation_errors = sorted(
            jsonschema.Draft202012Validator(schema).iter_errors(receipt),
            key=lambda item: list(item.path),
        )
        for item in validation_errors:
            path = ".".join(str(part) for part in item.path) or "<root>"
            errors.append(f"receipt schema violation at {path}: {item.message}")
    except ImportError:
        errors.append("jsonschema is required for behavior-proof verification; refusing fail-open fallback")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    errors: list[str] = []
    try:
        run_dir.relative_to((ROOT / "extractions/kyle-milligan-copywriting/behavior-proof/relaynote").resolve())
    except ValueError:
        errors.append("run directory must be inside the approved RelayNote behavior-proof root")
    if not run_dir.is_dir():
        errors.append(f"run directory does not exist: {run_dir}")
        return report(errors)

    fixture_hash = safe_digest(FIXTURE / "manifest.json", errors)
    manifest = verify_manifest(run_dir, fixture_hash, errors)
    missing_evidence = sorted(path for path in expected_run_paths() if not (run_dir / path).is_file())
    if missing_evidence:
        errors.append(f"required run evidence is missing: {missing_evidence}")
    if errors:
        return report(errors)
    receipt = load_json(run_dir / "proof-receipt.json", errors)
    verify_schema(receipt, errors)
    if errors:
        return report(errors)
    if receipt.get("run_id") != manifest.get("run_id"):
        errors.append("run ID differs between manifest and proof receipt")
    if receipt.get("fixture_manifest_sha256") != fixture_hash:
        errors.append("proof receipt is not bound to current frozen fixture")
    if receipt.get("proof_boundary") != PROOF_BOUNDARY:
        errors.append("proof receipt proof boundary drifted")

    product = json.loads((FIXTURE / "product-truth.json").read_text())
    veto = json.loads((FIXTURE / "transfer-veto.json").read_text())
    arms = json.loads((FIXTURE / "arm-contracts.json").read_text())
    verify_provenance(run_dir, receipt, fixture_hash, errors)
    verify_intermediates(run_dir, product, veto, errors)
    for arm in ("b", "c"):
        for replicate in range(1, 4):
            verify_output(run_dir / f"arms/arm-{arm}/replicate-{replicate}-final.md", product, veto, errors)
    verify_route_receipts(run_dir, receipt, arms, fixture_hash, errors)
    derived_scores, b_median, c_median, delta, preferences, score_failures = verify_blind_evaluation(
        run_dir, receipt, errors
    )
    if receipt.get("replicate_scores") != derived_scores:
        errors.append("receipt replicate scores/preferences differ from blinded raw scores")
    if receipt.get("arm_b_median") != b_median or receipt.get("arm_c_median") != c_median:
        errors.append("receipt medians are not recomputed from three replicates")
    if receipt.get("c_minus_b") != delta or receipt.get("blind_preferences_for_c") != preferences:
        errors.append("receipt delta or blind-preference count is not derived")

    acceptance_pass, acceptance_failures = verify_acceptance(run_dir, receipt, errors)
    fidelity_pass, fidelity_failures = verify_fidelity(run_dir, receipt, acceptance_pass, errors)
    all_failures = sorted(set(score_failures + acceptance_failures + fidelity_failures))
    if receipt.get("hard_failures") != all_failures:
        errors.append("global hard-failure list is not the union of raw evidence failures")

    pass_conditions = (
        b_median >= 65
        and c_median >= 80
        and delta >= 15
        and preferences >= 2
        and not all_failures
        and acceptance_pass
        and fidelity_pass
        and len(receipt.get("visible_kyle_mechanics", [])) >= 3
    )
    if pass_conditions:
        derived_verdict = (
            "PASS_INCREMENTAL_BEHAVIOR"
            if receipt.get("provenance_grade") == "RUNTIME_OBSERVED"
            else "PASS_DIAGNOSTIC_BEHAVIOR"
        )
    else:
        derived_verdict = "FAIL_NO_REGISTRATION"
    if receipt.get("verdict") != derived_verdict:
        errors.append(f"declared verdict {receipt.get('verdict')} != derived verdict {derived_verdict}")

    return report(
        errors,
        verdict=derived_verdict,
        b_median=b_median,
        c_median=c_median,
        delta=delta,
        preferences=preferences,
    )


def report(
    errors: list[str],
    verdict: str = "UNVERIFIED",
    b_median: float = 0,
    c_median: float = 0,
    delta: float = 0,
    preferences: int = 0,
) -> int:
    if errors:
        print("RELAYNOTE BEHAVIOR RUN: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("RELAYNOTE BEHAVIOR RUN: PASS")
    print(f"- derived verdict: {verdict}")
    print(f"- Arm B median: {b_median}")
    print(f"- Arm C median: {c_median}")
    print(f"- C minus B: {delta}")
    print(f"- blind preferences for C: {preferences}/3")
    print("- acceptance cases: 18/18 hash-bound and isolated")
    if verdict == "PASS_DIAGNOSTIC_BEHAVIOR":
        print("- registration: BLOCKED; runtime provenance is attested, not runtime-observed")
    print("- proof boundary: synthetic task-local behavior only; no market or A-tier embodiment claim")
    return 0


if __name__ == "__main__":
    sys.exit(main())
