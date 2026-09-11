#!/usr/bin/env python3
"""Verify and score the frozen Signal Fidelity real-work pilot locally."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from signal_fidelity_shadow import evaluate


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "extractions/video-context/1KOdiGgMtpY/validation/real-work-pilot-v1"
MANIFEST = PILOT / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text))


def blind_labels(seed: str, case_id: str) -> dict[str, str]:
    arms = []
    for arm in ("baseline", "treatment"):
        key = hashlib.sha256(f"{seed}:{case_id}:{arm}".encode()).hexdigest()
        arms.append((key, arm))
    arms.sort()
    return {arms[0][1]: "A", arms[1][1]: "B"}


def score_arm(case: dict, arm: str) -> dict:
    path = PILOT / "candidates" / f"{case['id']}-{arm}.md"
    text = path.read_text(encoding="utf-8")
    packet = {
        "signal_contract": case["signal_contract"],
        "artifact_text": text,
        "playback_text": "",
        "artifact_proof_state": case["proof_state"],
        "owner_approved_changes": [],
    }
    report = evaluate(packet)
    literal_items = {
        item["id"]
        for item in case["signal_contract"]["must_survive"]
        if item.get("match_policy", "literal") == "literal"
    }
    preserved = {
        item["field"]
        for item in report["preserved"]
        if item.get("surface") == "artifact"
    }
    covered = sorted(literal_items & preserved)
    missing = sorted(literal_items - preserved)
    proof_inflation = any(
        item["code"] == "proof_state_changed"
        for item in report["distortion_hypotheses"]
    )
    return {
        "path": str(path.relative_to(ROOT)),
        "words": word_count(text),
        "word_cap": case["word_cap"],
        "within_cap": word_count(text) <= case["word_cap"],
        "literal_total": len(literal_items),
        "literal_covered": len(covered),
        "covered_ids": covered,
        "missing_ids": missing,
        "manual_checks": [item["field"] for item in report["manual_checks"]],
        "proof_inflation": proof_inflation,
        "can_block": report["can_block"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write local-results.json")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures: list[str] = []
    results: list[dict] = []
    wins = {"treatment": 0, "baseline": 0, "tie": 0}
    material_deltas = 0
    proof_inflation = 0
    false_blocks = 0

    for case in manifest["cases"]:
        source = ROOT / case["source_path"]
        if not source.exists() or sha256(source) != case["source_sha256"]:
            failures.append(f"source drift: {case['id']}")
            continue
        labels = blind_labels(manifest["seed"], case["id"])
        arms = {arm: score_arm(case, arm) for arm in ("baseline", "treatment")}
        for arm, score in arms.items():
            score["blind_label"] = labels[arm]
            if not score["within_cap"]:
                failures.append(f"word cap exceeded: {case['id']} {arm}")
            proof_inflation += int(score["proof_inflation"])
            false_blocks += int(score["can_block"])
        baseline_score = arms["baseline"]["literal_covered"]
        treatment_score = arms["treatment"]["literal_covered"]
        if treatment_score > baseline_score:
            verdict = "treatment"
            wins["treatment"] += 1
            material_deltas += treatment_score - baseline_score
        elif baseline_score > treatment_score:
            verdict = "baseline"
            wins["baseline"] += 1
        else:
            verdict = "tie"
            wins["tie"] += 1
        results.append(
            {
                "case": case["id"],
                "blind_verdict": verdict,
                "arms_by_label": {
                    score["blind_label"]: {
                        key: value
                        for key, value in score.items()
                        if key != "blind_label"
                    }
                    for score in arms.values()
                },
                "label_reveal": labels,
            }
        )

    if failures:
        outcome = "INVALID"
    elif (
        wins["treatment"] >= 2
        and wins["baseline"] == 0
        and proof_inflation == 0
        and false_blocks == 0
        and material_deltas >= 2
    ):
        outcome = "ADVANCE_TO_HUMAN_BLIND"
    elif wins["baseline"] >= 2 or wins["treatment"] == 0:
        outcome = "RETIRE"
    else:
        outcome = "REVISE_SHADOW"

    output = {
        "schema_version": "signal-fidelity-local-results/v1",
        "status": "LOCAL_BUILDER_CONTROLLED",
        "outcome": outcome,
        "conclusion_ceiling": manifest["conclusion_ceiling"],
        "wins": wins,
        "material_literal_deltas": material_deltas,
        "proof_inflation_events": proof_inflation,
        "false_blocks": false_blocks,
        "added_user_questions": 0,
        "independent_human_blind": "PENDING",
        "creative_range_judgment": "PENDING_HUMAN",
        "cases": results,
        "failures": failures,
    }
    rendered = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        (PILOT / "local-results.json").write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
