#!/usr/bin/env python3
"""Validate Mastery Transfer Proof Spine manifests without model calls."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PROOF_STATES = (
    "CAPTURED",
    "GROUNDED",
    "RUNNABLE",
    "TRANSFERRED",
    "GENERALIZED",
    "BLIND_PREFERRED",
    "FIELD_VALIDATED",
    "SURPASSING",
)
ALLOWED_STATUSES = {"PASS", "PARTIAL", "UNTESTED", "NO_EVENT", "FAIL", "BLOCKED"}
REPO_ROOT = Path(__file__).resolve().parents[1]


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _evidence_paths(entry: dict[str, Any]) -> list[str]:
    evidence = entry.get("evidence", [])
    return evidence if isinstance(evidence, list) else []


def validate_manifest(
    manifest: dict[str, Any], *, repo_root: Path = REPO_ROOT, check_paths: bool = True
) -> list[str]:
    """Return human-readable validation errors. An empty list means PASS."""
    errors: list[str] = []

    if manifest.get("schema_version") != "mastery-transfer-proof/v1":
        errors.append("schema_version must be mastery-transfer-proof/v1")
    if not _nonempty(manifest.get("capability")):
        errors.append("capability is required")
    if not _nonempty(manifest.get("claim_boundary")):
        errors.append("claim_boundary is required")
    if not _nonempty(manifest.get("next_gate")):
        errors.append("next_gate is required")

    governance = manifest.get("governance", {})
    if not isinstance(governance, dict):
        errors.append("governance must be an object")
        governance = {}
    if governance.get("mode") != "SHADOW":
        errors.append("governance.mode must remain SHADOW")
    if governance.get("promotion_eligible") is not False:
        errors.append("SHADOW manifests must set promotion_eligible to false")
    if governance.get("automatic_enforcement") is not False:
        errors.append("automatic_enforcement must be false")

    states = manifest.get("proof_states", {})
    if not isinstance(states, dict):
        errors.append("proof_states must be an object")
        states = {}

    passed: list[str] = []
    gap_seen = False
    for state in PROOF_STATES:
        entry = states.get(state)
        if not isinstance(entry, dict):
            errors.append(f"proof_states.{state} is required")
            gap_seen = True
            continue
        status = entry.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"proof_states.{state}.status is invalid: {status!r}")
            gap_seen = True
            continue
        if status == "PASS":
            if gap_seen:
                errors.append(f"{state} cannot PASS after an earlier unearned state")
            passed.append(state)
            evidence = _evidence_paths(entry)
            if not evidence:
                errors.append(f"{state} PASS requires at least one evidence path")
            elif check_paths:
                for raw_path in evidence:
                    if not isinstance(raw_path, str) or not raw_path.strip():
                        errors.append(f"{state} contains an invalid evidence path")
                        continue
                    path = Path(raw_path)
                    resolved = path if path.is_absolute() else repo_root / path
                    if not resolved.exists():
                        errors.append(f"{state} evidence does not exist: {raw_path}")
        else:
            gap_seen = True

    expected_current = passed[-1] if passed else None
    if manifest.get("current_state") != expected_current:
        errors.append(
            f"current_state must equal highest contiguous PASS: {expected_current!r}"
        )

    generalized = states.get("GENERALIZED", {})
    if isinstance(generalized, dict) and generalized.get("status") == "PASS":
        tests = generalized.get("tests", {})
        for name in ("near_transfer", "far_transfer", "negative_control"):
            result = tests.get(name, {}) if isinstance(tests, dict) else {}
            if result.get("status") != "PASS" or result.get("held_out") is not True:
                errors.append(
                    f"GENERALIZED PASS requires sealed held-out {name} with status PASS"
                )

    blind = states.get("BLIND_PREFERRED", {})
    if isinstance(blind, dict) and blind.get("status") == "PASS":
        evaluation = blind.get("evaluation", {})
        required = {
            "independent": True,
            "blind": True,
            "precommitted_mapping": True,
            "preservation_pass": True,
        }
        for key, expected in required.items():
            if not isinstance(evaluation, dict) or evaluation.get(key) is not expected:
                errors.append(f"BLIND_PREFERRED PASS requires evaluation.{key}=true")
        if not isinstance(evaluation, dict) or evaluation.get("verdict") not in {
            "TREATMENT_WIN",
            "MATERIAL_TREATMENT_WIN",
        }:
            errors.append("BLIND_PREFERRED PASS requires a treatment-win verdict")
        if isinstance(evaluation, dict) and evaluation.get("builder") == evaluation.get("evaluator"):
            errors.append("builder cannot be the blind evaluator")

    field = states.get("FIELD_VALIDATED", {})
    if isinstance(field, dict) and field.get("status") == "PASS":
        events = manifest.get("field_events", {})
        if not isinstance(events, dict) or int(events.get("real_uses", 0)) < 1:
            errors.append("FIELD_VALIDATED PASS requires at least one real use")
        if not isinstance(events, dict) or int(events.get("observed_outcomes", 0)) < 1:
            errors.append("FIELD_VALIDATED PASS requires at least one observed outcome")
        if isinstance(events, dict) and events.get("state") == "NO_EVENT":
            errors.append("FIELD_VALIDATED cannot PASS with field_events.state=NO_EVENT")

    surpassing = states.get("SURPASSING", {})
    if isinstance(surpassing, dict) and surpassing.get("status") == "PASS":
        comparison = manifest.get("comparison", {})
        for key in ("baseline", "dimension", "threshold", "measured_result"):
            if not isinstance(comparison, dict) or not _nonempty(comparison.get(key)):
                errors.append(f"SURPASSING PASS requires comparison.{key}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot", required=True, help="Path to a proof manifest JSON")
    args = parser.parse_args()

    path = Path(args.pilot)
    if not path.is_absolute():
        path = REPO_ROOT / path
    try:
        manifest = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"MASTERY TRANSFER PROOF FAIL\n- unable to read manifest: {exc}")
        return 1

    errors = validate_manifest(manifest)
    if errors:
        print("MASTERY TRANSFER PROOF FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    summary = {
        "capability": manifest["capability"],
        "mode": manifest["governance"]["mode"],
        "current_state": manifest["current_state"],
        "next_gate": manifest["next_gate"],
        "promotion_eligible": manifest["governance"]["promotion_eligible"],
    }
    print("MASTERY TRANSFER PROOF PASS")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
