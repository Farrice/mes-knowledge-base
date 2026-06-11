#!/usr/bin/env python3
"""Verify persisted Skill Evolution candidate snapshot freshness.

This verifier is intentionally read-only. It checks the persisted local-first
candidate state and fails closed when the snapshot is stale, missing its
generation timestamp, future-dated, or contains invalid/future evidence dates.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "evolution_store" / "queue" / "skill_evolution_candidates.json"
SAFE_REFRESH_COMMAND = "python3 execution/skill_evolution_candidates.py scan --write"
CANDIDATE_SECTIONS = ("ready_candidates", "watchlist", "blocked")


@dataclass
class CheckResult:
    path: Path
    today: date
    generated_at: str
    checked_candidates: int
    errors: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_dateish(value: Any, label: str, errors: list[str]) -> date | None:
    if value in (None, ""):
        errors.append(f"missing timestamp: {label}")
        return None
    text = str(value).strip()
    try:
        if len(text) == 10:
            return date.fromisoformat(text)
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        errors.append(f"invalid timestamp: {label}={text!r}")
        return None


def load_snapshot(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"snapshot not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"snapshot is not valid JSON: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"snapshot root must be an object: {path}")
    return data


def safe_int(value: Any, label: str, errors: list[str]) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        errors.append(f"invalid count: {label}={value!r}")
        return 0


def iter_candidate_rows(snapshot: dict[str, Any]) -> list[tuple[str, int, dict[str, Any]]]:
    rows: list[tuple[str, int, dict[str, Any]]] = []
    for section in CANDIDATE_SECTIONS:
        value = snapshot.get(section, [])
        if not isinstance(value, list):
            rows.append((section, -1, {"_schema_error": f"{section} must be a list"}))
            continue
        for index, row in enumerate(value):
            if isinstance(row, dict):
                rows.append((section, index, row))
            else:
                rows.append((section, index, {"_schema_error": f"{section}[{index}] must be an object"}))
    return rows


def validate_snapshot(snapshot: dict[str, Any], path: Path, today: date) -> CheckResult:
    errors: list[str] = []
    generated_at = str(snapshot.get("generated_at") or "")
    generated_date = parse_dateish(generated_at, "generated_at", errors)
    if generated_date:
        if generated_date < today:
            errors.append(f"stale snapshot: generated_at date {generated_date.isoformat()} is before today {today.isoformat()}")
        if generated_date > today:
            errors.append(f"future snapshot: generated_at date {generated_date.isoformat()} is after today {today.isoformat()}")

    checked_candidates = 0
    for section, index, row in iter_candidate_rows(snapshot):
        schema_error = row.get("_schema_error")
        if schema_error:
            errors.append(f"schema error: {schema_error}")
            continue
        checked_candidates += 1
        row_label = f"{section}[{index}]"
        metrics = row.get("metrics")
        if isinstance(metrics, dict) and metrics.get("latest_date") not in (None, ""):
            latest_date = parse_dateish(metrics.get("latest_date"), f"{row_label}.metrics.latest_date", errors)
            if latest_date and latest_date > today:
                skill = row.get("skill", "unknown")
                errors.append(
                    f"future candidate evidence: {row_label} skill={skill!r} latest_date {latest_date.isoformat()} is after today {today.isoformat()}"
                )
        elif row.get("state") in {"ready", "watchlist"} and safe_int(row.get("evidence_count"), f"{row_label}.evidence_count", errors) > 0:
            skill = row.get("skill", "unknown")
            errors.append(f"missing timestamp: {row_label} skill={skill!r} has evidence_count but no metrics.latest_date")

    return CheckResult(
        path=path,
        today=today,
        generated_at=generated_at,
        checked_candidates=checked_candidates,
        errors=errors,
    )


def run_check(path: Path, today: date) -> CheckResult:
    snapshot = load_snapshot(path)
    return validate_snapshot(snapshot, path, today)


def print_result(result: CheckResult) -> None:
    status = "PASS" if result.ok else "FAIL"
    print(f"SKILL EVOLUTION CANDIDATE FRESHNESS {status}")
    print(f"- snapshot: {result.path}")
    print(f"- today: {result.today.isoformat()}")
    print(f"- generated_at: {result.generated_at or '(missing)'}")
    print(f"- checked candidates: {result.checked_candidates}")
    if result.errors:
        for error in result.errors:
            print(f"- error: {error}")
        print(f"- safe refresh command: {SAFE_REFRESH_COMMAND}")


def assert_fails(snapshot: dict[str, Any], today: date, expected: str) -> None:
    result = validate_snapshot(snapshot, Path("<fixture>"), today)
    if result.ok:
        raise AssertionError(f"expected fixture to fail with {expected!r}")
    if not any(expected in error for error in result.errors):
        raise AssertionError(f"expected {expected!r}, got {result.errors!r}")


def run_self_test() -> int:
    today = date(2026, 5, 19)
    fresh = {
        "generated_at": today.isoformat() + "T08:00:00",
        "ready_candidates": [
            {
                "candidate_id": "ready-1",
                "state": "ready",
                "skill": "fixture-skill",
                "evidence_count": 1,
                "metrics": {"latest_date": today.isoformat()},
            }
        ],
        "watchlist": [],
        "blocked": [],
    }
    with tempfile.TemporaryDirectory(prefix="skill-evolution-freshness-") as tmp:
        path = Path(tmp) / "skill_evolution_candidates.json"
        path.write_text(json.dumps(fresh), encoding="utf-8")
        result = run_check(path, today)
        if not result.ok:
            raise AssertionError(f"fresh fixture failed: {result.errors!r}")

    stale = dict(fresh, generated_at=(today - timedelta(days=1)).isoformat())
    assert_fails(stale, today, "stale snapshot")

    missing_generated = dict(fresh)
    missing_generated.pop("generated_at", None)
    assert_fails(missing_generated, today, "missing timestamp: generated_at")

    future_generated = dict(fresh, generated_at=(today + timedelta(days=1)).isoformat())
    assert_fails(future_generated, today, "future snapshot")

    future_candidate = json.loads(json.dumps(fresh))
    future_candidate["ready_candidates"][0]["metrics"]["latest_date"] = (today + timedelta(days=1)).isoformat()
    assert_fails(future_candidate, today, "future candidate evidence")

    missing_candidate_date = json.loads(json.dumps(fresh))
    missing_candidate_date["ready_candidates"][0]["metrics"].pop("latest_date")
    assert_fails(missing_candidate_date, today, "has evidence_count but no metrics.latest_date")

    print("SKILL EVOLUTION CANDIDATE FRESHNESS SELF-TEST PASS")
    print("- ok: fresh persisted snapshot passes")
    print("- ok: stale generated_at fails")
    print("- ok: missing generated_at fails")
    print("- ok: future generated_at fails")
    print("- ok: future candidate latest_date fails")
    print("- ok: evidence-backed candidate missing latest_date fails")
    return 0


def parse_today(value: str | None) -> date:
    if not value:
        return date.today()
    return date.fromisoformat(value)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Skill Evolution candidate snapshot freshness")
    parser.add_argument("--path", type=Path, default=SNAPSHOT_PATH, help="Candidate snapshot path to verify")
    parser.add_argument("--today", help="Override today's date as YYYY-MM-DD for deterministic tests")
    parser.add_argument("--self-test", action="store_true", help="Run fixture checks without touching repo state")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()

    try:
        result = run_check(args.path, parse_today(args.today))
    except Exception as exc:
        print("SKILL EVOLUTION CANDIDATE FRESHNESS FAIL")
        print(f"- snapshot: {args.path}")
        print(f"- error: {exc}")
        print(f"- safe refresh command: {SAFE_REFRESH_COMMAND}")
        return 1

    print_result(result)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
