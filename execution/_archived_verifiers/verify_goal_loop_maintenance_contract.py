#!/usr/bin/env python3
"""Verify the goal-loop maintenance contract and workflow adoption."""

from __future__ import annotations

import sys
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "goal-loop-maintenance-contract.md"
SOURCE_PACKAGE = ROOT / "extractions" / "video-context" / "5xrjO38WUYY"
WORKFLOWS = [
    ROOT / ".agent" / "workflows" / "self-evolve.md",
    ROOT / ".agent" / "workflows" / "skill-anneal.md",
    ROOT / ".agent" / "workflows" / "skill-evolution.md",
    ROOT / ".agent" / "workflows" / "repeatability-spine.md",
    ROOT / ".agent" / "workflows" / "autopilot.md",
    ROOT / ".agent" / "workflows" / "source-to-skill-system.md",
]

REQUIRED_FIELDS = [
    "target",
    "scope",
    "per_item_criteria",
    "permitted_side_effect",
    "proof_artifact",
    "measurable_stop",
    "turn_cap",
    "evaluator",
    "wake_up_check",
    "human_checkpoint",
    "rollback_or_archive_rule",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def validate_packet(packet: dict[str, object]) -> list[str]:
    failures: list[str] = []
    for field in REQUIRED_FIELDS:
        value = packet.get(field)
        if value is None or str(value).strip() == "":
            failures.append(f"missing goal packet field: {field}")
    return failures


def sample_packet() -> dict[str, str]:
    return {
        "target": ".agent/workflows/self-evolve.md",
        "scope": "self-evolution workflow only",
        "per_item_criteria": "every mutation-capable step has proof and stop checks",
        "permitted_side_effect": "workflow edit and verifier report",
        "proof_artifact": "execution/verify_goal_loop_maintenance_contract.py output",
        "measurable_stop": "verifier exits 0 and workflow mentions Goal Packet",
        "turn_cap": "15",
        "evaluator": "required-field verifier plus workflow term checks",
        "wake_up_check": "python3 execution/verify_goal_loop_maintenance_contract.py",
        "human_checkpoint": "approval before broad mutation or global changes",
        "rollback_or_archive_rule": "revert workflow edit or leave queue-only report",
    }


def main() -> int:
    failures: list[str] = []

    if not PRIMITIVE.exists():
        failures.append(f"missing primitive: {PRIMITIVE.relative_to(ROOT)}")
    else:
        primitive = read(PRIMITIVE)
        primitive_lower = primitive.lower()
        for field in REQUIRED_FIELDS:
            if f"`{field}`" not in primitive:
                failures.append(f"primitive missing field: {field}")
        for term in [
            "Evolution Council Preflight",
            "proof artifact",
            "measurable stop",
            "turn cap",
            "wake-up check",
            "Queue-first",
        ]:
            if term.lower() not in primitive_lower:
                failures.append(f"primitive missing term: {term}")

    incomplete = sample_packet()
    incomplete.pop("turn_cap")
    if not validate_packet(sample_packet()):
        pass
    else:
        failures.append("complete sample packet did not validate")
    if not any("turn_cap" in failure for failure in validate_packet(incomplete)):
        failures.append("incomplete sample packet did not fail on turn_cap")

    for workflow in WORKFLOWS:
        if not workflow.exists():
            failures.append(f"missing workflow: {workflow.relative_to(ROOT)}")
            continue
        content = read(workflow)
        if "goal-loop-maintenance-contract.md" not in content:
            failures.append(f"{workflow.relative_to(ROOT)} does not reference goal-loop contract")
        if "Goal Packet" not in content and "goal packet" not in content:
            failures.append(f"{workflow.relative_to(ROOT)} does not mention Goal Packet")

    source_files = [
        SOURCE_PACKAGE / "metadata.json",
        SOURCE_PACKAGE / "source-package.md",
        SOURCE_PACKAGE / "raw-prompt-inventory.md",
        SOURCE_PACKAGE / "uncertainty-report.md",
        SOURCE_PACKAGE / "transcript.txt",
        SOURCE_PACKAGE / "video-context-ledger.md",
    ]
    for path in source_files:
        if not path.exists():
            failures.append(f"source evidence missing: {path.relative_to(ROOT)}")

    metadata_path = SOURCE_PACKAGE / "metadata.json"
    if metadata_path.exists():
        try:
            metadata = json.loads(read(metadata_path))
        except json.JSONDecodeError as exc:
            failures.append(f"metadata.json invalid JSON: {exc}")
            metadata = {}
        package = metadata.get("source_package", {}) if isinstance(metadata, dict) else {}
        if metadata.get("id") != "5xrjO38WUYY":
            failures.append("metadata.json has wrong YouTube id")
        if package.get("evidence_counts", {}).get("observed_spoken", 0) < 100:
            failures.append("source package has too little spoken evidence")
        local_kinds = {item.get("kind") for item in package.get("local_sources", []) if isinstance(item, dict)}
        if {"pdf", "zip"} - local_kinds:
            failures.append("source package does not record both PDF and ZIP local sources")

    prompt_inventory = SOURCE_PACKAGE / "raw-prompt-inventory.md"
    if prompt_inventory.exists():
        inventory = read(prompt_inventory)
        for prompt_name in [
            "01_clean_audit.txt",
            "02_sharpen_skill.txt",
            "03_revive_backlog.txt",
            "04_forge_skills.txt",
            "05_maintain_heartbeat.txt",
        ]:
            if prompt_name not in inventory:
                failures.append(f"prompt inventory missing: {prompt_name}")

    if failures:
        print("GOAL LOOP MAINTENANCE CONTRACT VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("GOAL LOOP MAINTENANCE CONTRACT VERIFICATION PASS")
    print(f"- ok: {PRIMITIVE.relative_to(ROOT)}")
    print("- ok: complete packet passes and incomplete packet fails")
    print(f"- ok: {len(WORKFLOWS)} workflows reference the contract")
    print(f"- ok: {SOURCE_PACKAGE.relative_to(ROOT)} source evidence package")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
