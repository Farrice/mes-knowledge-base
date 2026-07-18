#!/usr/bin/env python3
"""mission_validator.py — deterministic validator for mission stage payloads.

Born 2026-07-18 (Wave 4, Frontier Elevation) to give JCC / supercomputer / swarm /
fleet batches a single machine-checked contract for the JSON a worker/stage hands
back describing its deliverables. Encodes the carded fleet failure shapes plus the
worker-envelope-standard rules (`directives/worker-envelope-standard.md`) as HARD
FAILS instead of hoping a reviewer catches them by eye.

Each rule below names the failure it prevents:
  1. schema shape        — missing/extra-type fields; a payload that can't even
                            describe itself correctly is not trustworthy.
  2. hollow delivery      — deliverable path missing or a 0-byte file on disk
                            (shape 5: paperwork without payload).
  3. path drift           — deliverable path resolves outside the declared
                            quarantine_root (shape 2: a worker's path claim is a
                            claim like any other, never taken on faith).
  4. unverified VERIFIED  — a claim labeled VERIFIED whose source file does not
                            exist on disk (invented provenance — the one
                            unforgivable failure per worker-envelope-standard).
  5. absence-claim rule   — claim text matching /(no source|not found|absent|
                            unrecoverable|0 bytes|does not exist)/i must be
                            labeled UNCONFIRMED and carry >=3 searched locations
                            (the THREE-LOCATION RULE, worker-envelope-standard #4).
  6. contradiction        — protected_tree_clean: true while `git status
                            --porcelain <protected>` is actually non-empty (a
                            worker or stage lying about not touching the
                            protected tree).

Usage:
    python3 execution/mission_validator.py check <payload.json>
    python3 execution/mission_validator.py schema

Exit: 0 clean · 1 one or more violations found.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ABSENCE_PATTERN = re.compile(
    r"(no source|not found|absent|unrecoverable|0 bytes|does not exist)", re.IGNORECASE
)

VALID_LABELS = {"VERIFIED", "LIKELY", "UNCONFIRMED"}

STAGE_PAYLOAD_SCHEMA = {
    "stage": {"type": str, "required": True},
    "worker": {"type": str, "required": True},
    "quarantine_root": {"type": str, "required": True},
    "protected_tree_clean": {"type": bool, "required": True},
    "gaps": {"type": list, "of": str, "required": True},
    "deliverables": {
        "type": list,
        "required": True,
        "min_len": 1,
        "item_schema": {
            "path": {"type": str, "required": True},
            "kind": {"type": str, "required": True},
            "summary": {"type": str, "required": True, "max_len": 300},
        },
    },
    "claims": {
        "type": list,
        "required": False,
        "item_schema": {
            "text": {"type": str, "required": True},
            "label": {"type": str, "required": True, "one_of": sorted(VALID_LABELS)},
            "source": {"type": str, "required": False},
            "searched": {"type": list, "of": str, "required": False},
        },
    },
    "protected": {"type": str, "required": False},
}


class Violation:
    def __init__(self, rule: str, message: str):
        self.rule = rule
        self.message = message

    def __str__(self):
        return f"[{self.rule}] {self.message}"


def _type_name(t) -> str:
    return {str: "string", bool: "boolean", list: "array", dict: "object", int: "number", float: "number"}.get(t, str(t))


def _check_field_type(value, expected_type, field_label: str, violations: list, rule: str) -> bool:
    """Returns True if the type is correct (safe to keep validating this field)."""
    if expected_type is bool:
        # bool is a subclass of int in Python — guard explicitly both ways.
        if not isinstance(value, bool):
            violations.append(Violation(rule, f"{field_label} must be a boolean, got {_type_name(type(value))}"))
            return False
        return True
    if expected_type is str:
        if not isinstance(value, str):
            violations.append(Violation(rule, f"{field_label} must be a string, got {_type_name(type(value))}"))
            return False
        return True
    if expected_type is list:
        if not isinstance(value, list):
            violations.append(Violation(rule, f"{field_label} must be an array, got {_type_name(type(value))}"))
            return False
        return True
    if expected_type is dict:
        if not isinstance(value, dict):
            violations.append(Violation(rule, f"{field_label} must be an object, got {_type_name(type(value))}"))
            return False
        return True
    return isinstance(value, expected_type)


def check_schema(payload: dict) -> list:
    """Rule 1: schema shape — missing required fields, wrong types, malformed items."""
    violations = []
    if not isinstance(payload, dict):
        return [Violation("schema", f"payload root must be an object, got {_type_name(type(payload))}")]

    for field, spec in STAGE_PAYLOAD_SCHEMA.items():
        present = field in payload
        if spec.get("required") and not present:
            violations.append(Violation("schema", f"missing required field: {field}"))
            continue
        if not present:
            continue
        value = payload[field]

        if not _check_field_type(value, spec["type"], field, violations, "schema"):
            continue

        if spec["type"] is str and "one_of" in spec and value not in spec["one_of"]:
            violations.append(Violation("schema", f"{field} must be one of {spec['one_of']}, got {value!r}"))

        if spec["type"] is list:
            if spec.get("min_len") and len(value) < spec["min_len"]:
                violations.append(Violation("schema", f"{field} must have at least {spec['min_len']} item(s), got {len(value)}"))
            if "of" in spec:
                for i, item in enumerate(value):
                    if not isinstance(item, spec["of"]):
                        violations.append(Violation("schema", f"{field}[{i}] must be a {_type_name(spec['of'])}, got {_type_name(type(item))}"))
            if "item_schema" in spec:
                for i, item in enumerate(value):
                    if not isinstance(item, dict):
                        violations.append(Violation("schema", f"{field}[{i}] must be an object, got {_type_name(type(item))}"))
                        continue
                    for sub_field, sub_spec in spec["item_schema"].items():
                        sub_present = sub_field in item
                        if sub_spec.get("required") and not sub_present:
                            violations.append(Violation("schema", f"{field}[{i}] missing required field: {sub_field}"))
                            continue
                        if not sub_present:
                            continue
                        sub_value = item[sub_field]
                        label = f"{field}[{i}].{sub_field}"
                        if not _check_field_type(sub_value, sub_spec["type"], label, violations, "schema"):
                            continue
                        if sub_spec["type"] is str and sub_spec.get("max_len") and len(sub_value) > sub_spec["max_len"]:
                            violations.append(Violation("schema", f"{label} exceeds max length {sub_spec['max_len']} ({len(sub_value)} chars)"))
                        if sub_spec["type"] is str and "one_of" in sub_spec and sub_value not in sub_spec["one_of"]:
                            violations.append(Violation("schema", f"{label} must be one of {sub_spec['one_of']}, got {sub_value!r}"))
                        if sub_spec["type"] is list and "of" in sub_spec:
                            for j, sub_item in enumerate(sub_value):
                                if not isinstance(sub_item, sub_spec["of"]):
                                    violations.append(Violation("schema", f"{label}[{j}] must be a {_type_name(sub_spec['of'])}, got {_type_name(type(sub_item))}"))

    known_fields = set(STAGE_PAYLOAD_SCHEMA.keys())
    extra = set(payload.keys()) - known_fields
    for field in sorted(extra):
        violations.append(Violation("schema", f"unknown field not in STAGE_PAYLOAD_SCHEMA: {field}"))

    return violations


def _resolve(path_str: str) -> Path:
    p = Path(path_str)
    return p if p.is_absolute() else (ROOT / p)


def check_hollow_delivery(payload: dict) -> list:
    """Rule 2: hollow delivery — missing or empty-file deliverable paths (shape 5)."""
    violations = []
    for i, d in enumerate(payload.get("deliverables", []) or []):
        if not isinstance(d, dict) or "path" not in d or not isinstance(d["path"], str):
            continue  # already flagged by schema check
        full = _resolve(d["path"])
        if not full.exists():
            violations.append(Violation("hollow_delivery", f"deliverables[{i}].path does not exist on disk: {d['path']}"))
            continue
        if full.is_file() and full.stat().st_size == 0:
            violations.append(Violation("hollow_delivery", f"deliverables[{i}].path is an empty file (0 bytes): {d['path']}"))
    return violations


def check_path_drift(payload: dict) -> list:
    """Rule 3: path drift — deliverable path resolves outside quarantine_root (shape 2)."""
    violations = []
    qroot_str = payload.get("quarantine_root")
    if not isinstance(qroot_str, str):
        return violations  # already flagged by schema check
    qroot = _resolve(qroot_str).resolve()
    for i, d in enumerate(payload.get("deliverables", []) or []):
        if not isinstance(d, dict) or "path" not in d or not isinstance(d["path"], str):
            continue
        full = _resolve(d["path"])
        try:
            resolved = full.resolve()
        except (OSError, RuntimeError):
            resolved = full
        try:
            resolved.relative_to(qroot)
        except ValueError:
            violations.append(Violation("path_drift", f"deliverables[{i}].path escapes quarantine_root ({qroot_str}): {d['path']}"))
    return violations


def check_unverified_provenance(payload: dict) -> list:
    """Rule 4: unverified VERIFIED — VERIFIED claim whose source file is missing (invented provenance)."""
    violations = []
    for i, c in enumerate(payload.get("claims", []) or []):
        if not isinstance(c, dict):
            continue
        label = c.get("label")
        if label != "VERIFIED":
            continue
        source = c.get("source")
        if not source or not isinstance(source, str):
            violations.append(Violation("unverified_provenance", f"claims[{i}] is labeled VERIFIED but has no source field"))
            continue
        if not _resolve(source).exists():
            violations.append(Violation("unverified_provenance", f"claims[{i}] is labeled VERIFIED but source does not exist on disk: {source}"))
    return violations


def check_absence_claims(payload: dict) -> list:
    """Rule 5: absence-claim rule — absence language must be UNCONFIRMED + >=3 searched locations."""
    violations = []
    for i, c in enumerate(payload.get("claims", []) or []):
        if not isinstance(c, dict):
            continue
        text = c.get("text")
        if not isinstance(text, str) or not ABSENCE_PATTERN.search(text):
            continue
        label = c.get("label")
        if label != "UNCONFIRMED":
            violations.append(Violation("absence_claim", f"claims[{i}] reads as an absence claim ({text!r}) but is labeled {label!r}, must be UNCONFIRMED"))
        searched = c.get("searched")
        if not isinstance(searched, list) or len(searched) < 3:
            got = len(searched) if isinstance(searched, list) else 0
            violations.append(Violation("absence_claim", f"claims[{i}] is an absence claim and must carry >=3 searched locations (three-location rule), got {got}"))
    return violations


def check_protected_tree_contradiction(payload: dict) -> list:
    """Rule 6: contradiction — protected_tree_clean: true while git status --porcelain is non-empty."""
    violations = []
    if payload.get("protected_tree_clean") is not True:
        return violations
    protected = payload.get("protected")
    if not protected or not isinstance(protected, str):
        return violations  # nothing to check the claim against
    result = subprocess.run(
        ["git", "status", "--porcelain", protected],
        cwd=ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        violations.append(Violation("protected_tree_contradiction", f"git status --porcelain failed for {protected!r}: {result.stderr.strip()}"))
        return violations
    if result.stdout.strip():
        violations.append(Violation(
            "protected_tree_contradiction",
            f"protected_tree_clean: true but `git status --porcelain {protected}` is non-empty:\n{result.stdout.strip()}",
        ))
    return violations


ALL_CHECKS = [
    check_schema,
    check_hollow_delivery,
    check_path_drift,
    check_unverified_provenance,
    check_absence_claims,
    check_protected_tree_contradiction,
]


def validate(payload: dict) -> list:
    violations = []
    for check in ALL_CHECKS:
        violations.extend(check(payload))
    return violations


def cmd_check(args) -> int:
    payload_path = Path(args.payload)
    if not payload_path.is_absolute():
        payload_path = ROOT / payload_path
    if not payload_path.exists():
        print(f"NO PAYLOAD: {payload_path} does not exist")
        return 1
    try:
        payload = json.loads(payload_path.read_text())
    except json.JSONDecodeError as e:
        print(f"INVALID JSON: {payload_path}: {e}")
        return 1

    violations = validate(payload)
    if not violations:
        print(f"CLEAN: {payload_path.relative_to(ROOT) if payload_path.is_relative_to(ROOT) else payload_path} — 0 violations")
        return 0

    print(f"{len(violations)} violation(s) in {payload_path.relative_to(ROOT) if payload_path.is_relative_to(ROOT) else payload_path}:")
    for v in violations:
        print(f"  {v}")
    return 1


def cmd_schema(_args) -> int:
    def _render(spec, indent=0):
        pad = "  " * indent
        for field, s in spec.items():
            type_name = _type_name(s["type"])
            req = "required" if s.get("required") else "optional"
            extras = []
            if "one_of" in s:
                extras.append(f"one_of={s['one_of']}")
            if "of" in s:
                extras.append(f"of={_type_name(s['of'])}")
            if "min_len" in s:
                extras.append(f"min_len={s['min_len']}")
            if "max_len" in s:
                extras.append(f"max_len={s['max_len']}")
            extra_str = f" ({', '.join(extras)})" if extras else ""
            print(f"{pad}{field}: {type_name} [{req}]{extra_str}")
            if "item_schema" in s:
                print(f"{pad}  items:")
                _render(s["item_schema"], indent + 2)

    print("STAGE_PAYLOAD_SCHEMA:")
    _render(STAGE_PAYLOAD_SCHEMA, 1)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)

    check_p = sub.add_parser("check", help="validate a stage payload JSON file")
    check_p.add_argument("payload", help="path to payload.json (repo-relative or absolute)")
    check_p.set_defaults(func=cmd_check)

    schema_p = sub.add_parser("schema", help="print STAGE_PAYLOAD_SCHEMA")
    schema_p.set_defaults(func=cmd_schema)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
