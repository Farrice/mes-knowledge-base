#!/usr/bin/env python3
"""Verify the six-domain storytelling corpus and its no-scope-expansion seals."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[3]
EXPECTED_CASES = {
    "FND-01": ("founder", "FULL STORY"),
    "SAL-01": ("sales", "STORY FRAGMENT"),
    "HLT-01": ("health", "STORY FRAGMENT"),
    "TEC-01": ("technical", "NO STORY"),
    "EDU-01": ("educational", "STORY FRAGMENT"),
    "OPS-01": ("operational", "NO STORY"),
}
DECISIONS = ["FULL STORY", "STORY FRAGMENT", "NO STORY"]
BODY_RANGES = {
    "FND-01": (650, 900),
    "SAL-01": (650, 900),
    "HLT-01": (450, 650),
    "TEC-01": (350, 500),
    "EDU-01": (700, 900),
    "OPS-01": (450, 650),
}
REQUIRED_REGRESSIONS = {
    "SAL-01-owner-output-contract-scope.md",
    "SAL-01-unsupported-icp-tell-mechanism.md",
    "HLT-01-owner-output-contract-scope.md",
    "HLT-01-invented-narrator-attitude.md",
    "SAL-01-copy-rewrite-misclassified-full-story.md",
    "CORPUS-01-reference-body-length-miscalculated.md",
    "SAL-REF-01-prose-surface.md",
    "CORPUS-02-capability-handoff-missing.md",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reference_body_words(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    try:
        body = text.split("## Reference Asset", 1)[1].split("## Reference Receipt", 1)[0]
    except IndexError:
        return -1
    return len(body.split())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--final",
        action="store_true",
        help="also require replay, evaluation, regression, and final-report artifacts",
    )
    args = parser.parse_args()
    failures: list[str] = []

    manifest_path = ROOT / "corpus-manifest.json"
    try:
        manifest = load_json(manifest_path)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load corpus manifest: {exc}")
        return 1

    scope = manifest.get("routerScope", {})
    if scope.get("decisions") != DECISIONS:
        failures.append("router decisions differ from the locked three-decision set")
    if scope.get("newRoutesAllowed") is not False:
        failures.append("newRoutesAllowed must remain false")
    if scope.get("newExpertsAllowed") is not False:
        failures.append("newExpertsAllowed must remain false")
    if scope.get("maxBodyOwners") != 1:
        failures.append("maxBodyOwners must remain 1")

    cases = manifest.get("cases", [])
    by_id = {case.get("id"): case for case in cases}
    if len(cases) != 6 or set(by_id) != set(EXPECTED_CASES):
        failures.append("manifest must contain exactly the six locked case IDs")

    reference_paths: set[str] = set()
    for case_id, (domain, expected_decision) in EXPECTED_CASES.items():
        case = by_id.get(case_id)
        if not case:
            continue
        if case.get("domain") != domain:
            failures.append(f"{case_id}: expected domain {domain}")
        if case.get("expectedDecision") != expected_decision:
            failures.append(f"{case_id}: expected decision {expected_decision}")
        for field in ("brief", "reference", "currentReference"):
            relative = case.get(field)
            if not isinstance(relative, str) or not (ROOT / relative).is_file():
                failures.append(f"{case_id}: missing {field}")
        if isinstance(case.get("reference"), str):
            reference_paths.add(case["reference"])

    current_reference_paths = {
        case.get("currentReference") for case in cases if isinstance(case.get("currentReference"), str)
    }

    seal_path = ROOT / manifest.get("referenceSeal", "reference-seal.json")
    try:
        seal = load_json(seal_path)
        sealed_refs = seal.get("references", {})
        if set(sealed_refs) != reference_paths:
            failures.append("reference seal does not cover exactly the manifest references")
        for relative, expected_hash in sealed_refs.items():
            path = ROOT / relative
            if not path.is_file() or digest(path) != expected_hash:
                failures.append(f"reference seal mismatch: {relative}")
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"cannot verify reference seal: {exc}")

    current_seal_path = ROOT / manifest.get("currentReferenceSeal", "current-reference-seal.json")
    try:
        current_seal = load_json(current_seal_path)
        current_refs = current_seal.get("references", {})
        if set(current_refs) != current_reference_paths:
            failures.append("current reference seal does not cover exactly the v2 references")
        for relative, expected_hash in current_refs.items():
            path = ROOT / relative
            if not path.is_file() or digest(path) != expected_hash:
                failures.append(f"current reference seal mismatch: {relative}")
        for case_id, (low, high) in BODY_RANGES.items():
            case = by_id.get(case_id, {})
            relative = case.get("currentReference")
            if not isinstance(relative, str):
                continue
            count = reference_body_words(ROOT / relative)
            if count < low or count > high:
                failures.append(f"{case_id}: current reference body has {count} words; expected {low}-{high}")
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"cannot verify current reference seal: {exc}")

    router_seal_path = ROOT / manifest.get("routerScopeSeal", "router-scope-seal.json")
    try:
        router_seal = load_json(router_seal_path)
        if router_seal.get("decisions") != DECISIONS:
            failures.append("router scope seal decisions changed")
        if router_seal.get("maxBodyOwners") != 1:
            failures.append("router scope seal body-owner limit changed")
        for relative, expected_hash in router_seal.get("files", {}).items():
            path = REPO_ROOT / relative
            if not path.is_file() or digest(path) != expected_hash:
                failures.append(f"router scope changed: {relative}")
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"cannot verify router scope seal: {exc}")

    if args.final:
        for required in ("blind-pass-report.md", "USER-GUIDE.md", "AFTER-ACTION-REVIEW.md"):
            if not (ROOT / required).is_file():
                failures.append(f"missing {required}")
        regression_dir = ROOT / "regressions"
        present_regressions = {
            path.name for path in regression_dir.glob("*.md") if path.name != "README.md"
        }
        missing_regressions = REQUIRED_REGRESSIONS - present_regressions
        if missing_regressions:
            failures.append(
                "missing required regression fixtures: " + ", ".join(sorted(missing_regressions))
            )
        for case_id in EXPECTED_CASES:
            replay = ROOT / "replays" / f"{case_id}-pass-1.md"
            evaluation_path = ROOT / "evaluations" / f"{case_id}.json"
            if not replay.is_file():
                failures.append(f"{case_id}: missing first blind replay")
                continue
            try:
                evaluation = load_json(evaluation_path)
            except (OSError, json.JSONDecodeError) as exc:
                failures.append(f"{case_id}: invalid evaluation: {exc}")
                continue
            if evaluation.get("caseId") != case_id:
                failures.append(f"{case_id}: evaluation identity mismatch")
            initial = evaluation.get("initialVerdict")
            final = evaluation.get("finalVerdict")
            if initial not in {"PASS", "REPAIR", "INVALID"}:
                failures.append(f"{case_id}: invalid initial verdict")
            if final not in {"PASS", "PENDING"}:
                failures.append(f"{case_id}: invalid final verdict")
            observed = evaluation.get("failures", [])
            if initial in {"REPAIR", "INVALID"} and not observed:
                failures.append(f"{case_id}: failed replay has no recorded failure")
            for item in observed:
                relative = item.get("regressionFixture") if isinstance(item, dict) else None
                if not isinstance(relative, str) or not (ROOT / relative).is_file():
                    failures.append(f"{case_id}: failure lacks a regression fixture")
            repair_replay = evaluation.get("repairReplay")
            if isinstance(repair_replay, str) and not (ROOT / repair_replay).is_file():
                failures.append(f"{case_id}: named repair replay is missing")
            if initial == "REPAIR" and final == "PASS":
                if not isinstance(repair_replay, str) or not (ROOT / repair_replay).is_file():
                    failures.append(f"{case_id}: repaired PASS lacks a bounded repair replay")

    if failures:
        print("FAIL")
        for item in failures:
            print(f"- {item}")
        return 1

    mode = "final" if args.final else "structural"
    print(f"PASS: six-domain corpus ({mode}); reference and router-scope seals intact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
