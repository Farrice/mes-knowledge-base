#!/usr/bin/env python3
"""verify_mission_validator.py — Wave-4 acceptance fixture for mission_validator.py.

Born 2026-07-18 (Wave 4, Frontier Elevation). Builds one deliberately-broken temp
payload per hard-fail rule (schema, hollow delivery, path drift, unverified
VERIFIED, absence-claim rule, protected-tree contradiction) plus one fully-clean
payload, runs `mission_validator.py check` against each via subprocess, and
asserts the validator rejects the 6 broken ones and accepts the clean one.

Fixture files live under `.tmp/mission-validator-fixtures/` (gitignored, never
committed). Prints `N/7 PASS` — all 7 must pass for the validator to be trusted.

Usage:
    python3 execution/verify_mission_validator.py
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "execution" / "mission_validator.py"
FIXTURE_DIR = ROOT / ".tmp" / "mission-validator-fixtures"


def write_file(rel_path: str, content: str = "fixture content\n") -> None:
    full = ROOT / rel_path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content)


def write_empty_file(rel_path: str) -> None:
    full = ROOT / rel_path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.touch()


def write_payload(name: str, payload: dict) -> Path:
    path = FIXTURE_DIR / f"{name}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2))
    return path


def run_validator(payload_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "check", str(payload_path)],
        cwd=ROOT, capture_output=True, text=True,
    )


def pick_dirty_path() -> str:
    """Find a real path with uncommitted changes in this repo (read-only git status)."""
    result = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True)
    for line in result.stdout.splitlines():
        # porcelain format: "XY path" — path starts at column 3.
        candidate = line[3:].strip()
        if candidate and (ROOT / candidate).exists():
            return candidate
    # Fallback: known-dirty tracked file per session state at time of writing.
    return ".agent/sessions/observe-log.jsonl"


def build_fixtures() -> dict:
    fixtures = {}

    # 1. schema violation — missing required field "worker".
    write_file(".tmp/mission-validator-fixtures/schema/q/out.txt", "real deliverable\n")
    fixtures["schema"] = {
        "payload": write_payload("1-schema", {
            "stage": "wave4-fixture",
            # "worker" deliberately omitted
            "quarantine_root": ".tmp/mission-validator-fixtures/schema/q",
            "protected_tree_clean": False,
            "gaps": [],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/schema/q/out.txt", "kind": "file", "summary": "test deliverable"},
            ],
        }),
        "expect_pass": False,
        "expect_rule": "schema",
    }

    # 2. hollow delivery — deliverable file exists but is 0 bytes.
    write_empty_file(".tmp/mission-validator-fixtures/hollow/q/empty.txt")
    fixtures["hollow_delivery"] = {
        "payload": write_payload("2-hollow", {
            "stage": "wave4-fixture",
            "worker": "fixture-worker",
            "quarantine_root": ".tmp/mission-validator-fixtures/hollow/q",
            "protected_tree_clean": False,
            "gaps": [],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/hollow/q/empty.txt", "kind": "file", "summary": "empty on purpose"},
            ],
        }),
        "expect_pass": False,
        "expect_rule": "hollow_delivery",
    }

    # 3. path drift — deliverable resolves outside declared quarantine_root.
    write_file(".tmp/mission-validator-fixtures/drift/q/inside.txt", "inside root\n")
    write_file(".tmp/mission-validator-fixtures/drift/outside.txt", "outside root\n")
    fixtures["path_drift"] = {
        "payload": write_payload("3-drift", {
            "stage": "wave4-fixture",
            "worker": "fixture-worker",
            "quarantine_root": ".tmp/mission-validator-fixtures/drift/q",
            "protected_tree_clean": False,
            "gaps": [],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/drift/outside.txt", "kind": "file", "summary": "escapes quarantine_root"},
            ],
        }),
        "expect_pass": False,
        "expect_rule": "path_drift",
    }

    # 4. unverified VERIFIED — claim labeled VERIFIED, source file does not exist.
    write_file(".tmp/mission-validator-fixtures/provenance/q/out.txt", "real deliverable\n")
    fixtures["unverified_provenance"] = {
        "payload": write_payload("4-provenance", {
            "stage": "wave4-fixture",
            "worker": "fixture-worker",
            "quarantine_root": ".tmp/mission-validator-fixtures/provenance/q",
            "protected_tree_clean": False,
            "gaps": [],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/provenance/q/out.txt", "kind": "file", "summary": "test deliverable"},
            ],
            "claims": [
                {"text": "The repair fleet closed 325 skills.", "label": "VERIFIED",
                 "source": ".tmp/mission-validator-fixtures/provenance/nonexistent-source.md"},
            ],
        }),
        "expect_pass": False,
        "expect_rule": "unverified_provenance",
    }

    # 5. absence-claim rule — absence language, correct label, but <3 searched locations.
    write_file(".tmp/mission-validator-fixtures/absence/q/out.txt", "real deliverable\n")
    fixtures["absence_claim"] = {
        "payload": write_payload("5-absence", {
            "stage": "wave4-fixture",
            "worker": "fixture-worker",
            "quarantine_root": ".tmp/mission-validator-fixtures/absence/q",
            "protected_tree_clean": False,
            "gaps": [],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/absence/q/out.txt", "kind": "file", "summary": "test deliverable"},
            ],
            "claims": [
                {"text": "No source found for the original transcript.", "label": "UNCONFIRMED",
                 "searched": ["extractions/", "claude-export archive tarball"]},
            ],
        }),
        "expect_pass": False,
        "expect_rule": "absence_claim",
    }

    # 6. contradiction — protected_tree_clean: true while the named path is actually dirty.
    dirty_path = pick_dirty_path()
    write_file(".tmp/mission-validator-fixtures/contradiction/q/out.txt", "real deliverable\n")
    fixtures["protected_tree_contradiction"] = {
        "payload": write_payload("6-contradiction", {
            "stage": "wave4-fixture",
            "worker": "fixture-worker",
            "quarantine_root": ".tmp/mission-validator-fixtures/contradiction/q",
            "protected_tree_clean": True,
            "protected": dirty_path,
            "gaps": [],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/contradiction/q/out.txt", "kind": "file", "summary": "test deliverable"},
            ],
        }),
        "expect_pass": False,
        "expect_rule": "protected_tree_contradiction",
    }

    # 7. fully clean payload — must pass every rule.
    write_file(".tmp/mission-validator-fixtures/clean/q/out.txt", "real deliverable\n")
    write_file(".tmp/mission-validator-fixtures/clean/q/source.md", "real source for the verified claim\n")
    fixtures["clean"] = {
        "payload": write_payload("7-clean", {
            "stage": "wave4-fixture",
            "worker": "fixture-worker",
            "quarantine_root": ".tmp/mission-validator-fixtures/clean/q",
            "protected_tree_clean": True,
            "gaps": ["no open gaps for this fixture"],
            "deliverables": [
                {"path": ".tmp/mission-validator-fixtures/clean/q/out.txt", "kind": "file", "summary": "clean fixture deliverable"},
            ],
            "claims": [
                {"text": "The validator enforces six hard-fail rules.", "label": "VERIFIED",
                 "source": ".tmp/mission-validator-fixtures/clean/q/source.md"},
                {"text": "This approach is likely the right shape for future stages.", "label": "LIKELY"},
                {"text": "No source found for a fabricated fourth rule.", "label": "UNCONFIRMED",
                 "searched": ["extractions/", "claude-export archive tarball", "_active/codex-harvest-2026-06-11/extractions/"]},
            ],
        }),
        "expect_pass": True,
        "expect_rule": None,
    }

    return fixtures


def main() -> int:
    fixtures = build_fixtures()
    passed = 0
    total = len(fixtures)

    for name, spec in fixtures.items():
        result = run_validator(spec["payload"])
        ok = True
        detail = ""

        if spec["expect_pass"]:
            if result.returncode != 0:
                ok = False
                detail = f"expected exit 0 (clean), got {result.returncode}: {result.stdout.strip()}"
        else:
            if result.returncode == 0:
                ok = False
                detail = f"expected exit 1 (violation), got 0: {result.stdout.strip()}"
            elif spec["expect_rule"] and f"[{spec['expect_rule']}]" not in result.stdout:
                ok = False
                detail = f"expected rule '[{spec['expect_rule']}]' in output, got: {result.stdout.strip()}"

        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"  [{status}] {name}{'' if ok else ' — ' + detail}")

    print(f"\n{passed}/{total} PASS")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
