#!/usr/bin/env python3
"""Verify the bounded Marketing Specialist Workbench in both directions."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "extractions" / "video-context" / "SupWhagSCm8"
ROUTE_MAP = (
    ROOT
    / "skills"
    / "oren-one-person-ai-marketer"
    / "references"
    / "marketing-specialist-route-map.json"
)
FIXTURES = PACKAGE / "routing-fixtures.json"
BEHAVIOR_FIXTURES = PACKAGE / "behavior-proof-fixtures.json"
RECEIPTS = PACKAGE / "production-receipts.json"

EXPECTED_MODES = {
    "ads",
    "competitor",
    "calendar",
    "email",
    "seo",
    "voice",
    "diagnostics",
}

REQUIRED_FILES = (
    ".agent/workflows/marketing-specialist.md",
    ".agents/skills/source-command-marketing-specialist/SKILL.md",
    ".claude/commands/marketing-specialist.md",
    "skills/oren-one-person-ai-marketer/workflows/13-marketing-specialist-workbench.md",
    "skills/oren-one-person-ai-marketer/references/prompts-v2/marketing-specialist-workbench.md",
    "skills/oren-one-person-ai-marketer/references/marketing-specialist-route-map.json",
    "extractions/video-context/SupWhagSCm8/analysis.md",
    "extractions/video-context/SupWhagSCm8/deep-extraction.md",
    "extractions/video-context/SupWhagSCm8/source-ledger.md",
    "extractions/video-context/SupWhagSCm8/system-contract.md",
    "extractions/video-context/SupWhagSCm8/behavior-proof.md",
    "extractions/video-context/SupWhagSCm8/routing-fixtures.json",
    "extractions/video-context/SupWhagSCm8/production-receipts.json",
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require_text(path: Path, needles: tuple[str, ...], failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"missing file: {path.relative_to(ROOT)}")
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        failures.append(f"empty file: {path.relative_to(ROOT)}")
        return text
    for needle in needles:
        if needle not in text:
            failures.append(f"{path.relative_to(ROOT)} missing required text: {needle}")
    return text


def owner_paths(mode: dict[str, Any]) -> list[str]:
    owners: list[dict[str, Any]] = []
    if mode.get("primary_owner"):
        owners.append(mode["primary_owner"])
    selector = mode.get("primary_owner_selector") or {}
    owners.extend(
        value
        for key, value in selector.items()
        if key != "selection_rule" and isinstance(value, dict)
    )
    support = mode.get("bounded_support")
    if support:
        owners.append(support)
    return [owner.get("workflow") for owner in owners if owner.get("workflow")]


def validate_route_map(route_map: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    activation = route_map.get("activation") or {}
    policy = route_map.get("policy") or {}
    modes = route_map.get("modes") or []

    mode_ids = {mode.get("id") for mode in modes}
    if mode_ids != EXPECTED_MODES:
        failures.append(f"mode set mismatch: {sorted(mode_ids)}")
    if activation.get("natural_language") != "SHADOW":
        failures.append("natural-language activation must remain SHADOW")
    if activation.get("explicit_command") != "ACTIVE_AFTER_VALIDATION":
        failures.append("explicit command must be ACTIVE_AFTER_VALIDATION")
    gate = activation.get("promotion_gate") or {}
    if gate.get("real_production_receipts_required") != 3:
        failures.append("promotion gate must require three production receipts")
    if not gate.get("explicit_farrice_approval_required"):
        failures.append("promotion gate must require explicit Farrice approval")
    if policy.get("primary_owner_limit_per_run") != 1:
        failures.append("primary owner limit must be one")
    if policy.get("bounded_support_limit_per_run") != 1:
        failures.append("bounded support limit must be one")
    if not policy.get("bulk_load_forbidden"):
        failures.append("bulk loading must be forbidden")
    if policy.get("evidence_states") != [
        "VERIFIED",
        "LIKELY",
        "UNCONFIRMED",
        "UNTESTED",
        "NO EVENT",
    ]:
        failures.append("evidence states drifted")

    for mode in modes:
        mode_id = mode.get("id", "<missing>")
        has_owner = bool(mode.get("primary_owner"))
        has_selector = bool(mode.get("primary_owner_selector"))
        if has_owner == has_selector:
            failures.append(f"{mode_id}: define primary_owner XOR primary_owner_selector")
        if not mode.get("signals"):
            failures.append(f"{mode_id}: missing signals")
        if not mode.get("required_inputs"):
            failures.append(f"{mode_id}: missing required inputs")
        if not mode.get("output_contract"):
            failures.append(f"{mode_id}: missing output contract")
        if not mode.get("claim_boundary"):
            failures.append(f"{mode_id}: missing claim boundary")
        selector = mode.get("primary_owner_selector") or {}
        if selector and not selector.get("selection_rule"):
            failures.append(f"{mode_id}: selector missing one-owner selection rule")
        for relative in owner_paths(mode):
            if not (ROOT / relative).exists():
                failures.append(f"{mode_id}: owner workflow missing: {relative}")

    if len(route_map.get("approval_boundaries") or []) < 6:
        failures.append("approval boundary list is incomplete")
    if len(route_map.get("outside_handoffs") or []) < 2:
        failures.append("outside-owner negative controls are incomplete")
    return failures


def external_handoff(query: str, route_map: dict[str, Any]) -> str | None:
    lowered = query.lower()
    for handoff in route_map.get("outside_handoffs") or []:
        if any(signal in lowered for signal in handoff.get("signals") or []):
            return handoff.get("command")
    return None


def approval_state(query: str) -> str | None:
    lowered = query.lower()
    approval_signals = (
        "publish",
        "send outreach",
        "move $",
        "media spend",
        "launch the campaign",
        "launch the campaigns",
        "update the crm",
        "change the ad account",
    )
    return "APPROVAL_REQUIRED" if any(signal in lowered for signal in approval_signals) else None


def select_mode(query: str, route_map: dict[str, Any]) -> str | None:
    lowered = query.lower()
    scored: list[tuple[int, int, str]] = []
    for index, mode in enumerate(route_map.get("modes") or []):
        score = sum(1 for signal in mode.get("signals") or [] if signal in lowered)
        scored.append((score, -index, mode["id"]))
    best = max(scored, default=(0, 0, ""))
    return best[2] if best[0] else None


def select_branch(mode: str | None, query: str) -> str | None:
    lowered = query.lower()
    if mode == "calendar":
        return "creator" if "creator" in lowered else "brand"
    if mode == "voice":
        return "client" if "client" in lowered else "farrice"
    if mode == "diagnostics":
        if "incrementality" in lowered or "attribution" in lowered:
            return "measurement"
        if "spend map" in lowered or "full-funnel allocation" in lowered:
            return "spend_map"
        return "golden_core"
    return None


def evidence_state(query: str) -> str | None:
    lowered = query.lower()
    signals = ("without campaign data", "without data", "without sources", "invent current", "make up")
    return "PROVISIONAL_EVIDENCE_REQUIRED" if any(signal in lowered for signal in signals) else None


def validate_fixtures(route_map: dict[str, Any], fixtures: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    positives = fixtures.get("positive") or []
    negatives = fixtures.get("negative") or []
    if len(positives) != 7:
        failures.append(f"expected seven positive fixtures, found {len(positives)}")
    if len(negatives) != 6:
        failures.append(f"expected six negative fixtures, found {len(negatives)}")

    for fixture in positives:
        actual_mode = select_mode(fixture["query"], route_map)
        if actual_mode != fixture.get("expected_mode"):
            failures.append(f"{fixture['id']}: expected {fixture.get('expected_mode')}, got {actual_mode}")
        expected_branch = fixture.get("expected_branch")
        if expected_branch and select_branch(actual_mode, fixture["query"]) != expected_branch:
            failures.append(f"{fixture['id']}: branch mismatch")

    for fixture in negatives:
        query = fixture["query"]
        if fixture.get("expected_external_command"):
            actual = external_handoff(query, route_map)
            if actual != fixture["expected_external_command"]:
                failures.append(f"{fixture['id']}: expected handoff {fixture['expected_external_command']}, got {actual}")
            continue
        expected_mode = fixture.get("expected_mode")
        if expected_mode and select_mode(query, route_map) != expected_mode:
            failures.append(f"{fixture['id']}: expected mode {expected_mode}")
        expected_state = fixture.get("expected_state")
        actual_state = approval_state(query) or evidence_state(query)
        if expected_state and actual_state != expected_state:
            failures.append(f"{fixture['id']}: expected state {expected_state}, got {actual_state}")
    return failures


def validate_behavior(fixtures: dict[str, Any], receipts: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    cases = fixtures.get("cases") or []
    if len(cases) != 3:
        failures.append(f"expected three frozen comparison cases, found {len(cases)}")
    wins = 0
    labels_seen: set[tuple[str, str]] = set()
    for case in cases:
        baseline = case.get("baseline") or {}
        integrated = case.get("integrated") or {}
        pair = (baseline.get("blind_label"), integrated.get("blind_label"))
        labels_seen.add(pair)
        if not all(integrated.get(field) for field in ("artifact", "evidence_state", "next_test")):
            failures.append(f"{case.get('id')}: integrated artifact lacks proof fields")
        if case.get("blind_winner") != integrated.get("blind_label"):
            failures.append(f"{case.get('id')}: blind winner is not the integrated artifact")
        if case.get("result") == "INTEGRATED_WIN":
            wins += 1
    if wins < 2:
        failures.append(f"blind comparison lift below threshold: {wins}/3 wins")
    if len(labels_seen) < 2:
        failures.append("A/B label positions were not alternated")

    receipt_rows = receipts.get("receipts") or []
    if receipts.get("current") != len(receipt_rows):
        failures.append("production receipt counter does not match receipt rows")
    if receipts.get("required") != 3:
        failures.append("production promotion must require three receipts")
    if receipts.get("current") != 0 or receipt_rows:
        failures.append("new build must not invent retrospective production receipts")
    if receipts.get("status") != "PENDING_REAL_USE":
        failures.append("production status must remain PENDING_REAL_USE")
    return failures


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            failures.append(f"missing required file: {relative}")

    route_map = load_json(ROUTE_MAP)
    fixtures = load_json(FIXTURES)
    behavior = load_json(BEHAVIOR_FIXTURES)
    receipts = load_json(RECEIPTS)

    failures.extend(validate_route_map(route_map))
    failures.extend(validate_fixtures(route_map, fixtures))
    failures.extend(validate_behavior(behavior, receipts))

    require_text(
        ROOT / ".agent/workflows/marketing-specialist.md",
        ("ACTIVE_AFTER_VALIDATION", "SHADOW", "five-part output spine", "approval boundary"),
        failures,
    )
    require_text(
        ROOT / "skills/oren-one-person-ai-marketer/references/prompts-v2/marketing-specialist-workbench.md",
        ("## Output Contract", "## Output Skeleton", "## Quality Gate", "## Deploy When"),
        failures,
    )
    require_text(
        ROOT / "skills/oren-one-person-ai-marketer/SKILL.md",
        ("workflows: 13", "Marketing Specialist Workbench", "marketing-specialist-workbench.md"),
        failures,
    )
    require_text(
        PACKAGE / "behavior-proof.md",
        ("3 wins, 0 ties, 0 losses", "0/3", "NO EVENT", "UNTESTED"),
        failures,
    )
    require_text(
        PACKAGE / "uncertainty-report.md",
        ("Visual frames and OCR were not collected", "UNTESTED", "NO EVENT"),
        failures,
    )

    # False-green control: a route map missing one approved mode must fail.
    sabotaged = copy.deepcopy(route_map)
    sabotaged["modes"] = [mode for mode in sabotaged["modes"] if mode.get("id") != "ads"]
    if not validate_route_map(sabotaged):
        failures.append("false-green control failed: missing mode was accepted")

    if failures:
        print("Marketing Specialist Workbench: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Marketing Specialist Workbench: PASS "
        "(7 modes; 7 positive fixtures; 6 negative controls; "
        "3 frozen integrated wins; 0/3 real receipts; natural-language SHADOW; false-green caught)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
