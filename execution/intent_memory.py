#!/usr/bin/env python3
"""Workspace-local intent memory for Codex Antigravity.

This script keeps the current working intent in `.agent/intent-memory/current.json`
and mirrors the relevant fields into the shared cohesion state.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import system_cohesion_state


SCHEMA_VERSION = "intent-memory/v1"


def workspace_root() -> Path:
    override = os.environ.get("ANTIGRAVITY_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


ROOT = workspace_root()
AGENT_DIR = ROOT / ".agent"
INTENT_DIR = AGENT_DIR / "intent-memory"
CURRENT_PATH = INTENT_DIR / "current.json"

REQUIRED_TOP_LEVEL_KEYS = (
    "schema_version",
    "updated_at",
    "active_intent",
    "route",
    "mission",
    "next_move",
    "history",
)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def clean_list(values: list[str] | None) -> list[str]:
    return system_cohesion_state.clean_list(values)


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def default_record() -> dict[str, Any]:
    timestamp = now()
    return {
        "schema_version": SCHEMA_VERSION,
        "updated_at": timestamp,
        "active_intent": {
            "goal": "",
            "deliverable": "",
            "audience": "",
            "success_criteria": [],
            "constraints": [],
            "clarity_score": None,
            "confidence": "",
            "ambiguity_map": "",
            "source": "",
            "captured_at": timestamp,
        },
        "route": {
            "mode": "",
            "chosen_route": "",
            "support_gates": [],
            "expert_stack": [],
            "skipped_routes": [],
        },
        "mission": {
            "slug": "",
            "state_path": "",
            "status": "",
        },
        "next_move": {
            "action": "",
            "owner": "",
            "verification": [],
        },
        "history": [],
    }


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def merge_defaults(raw: dict[str, Any]) -> dict[str, Any]:
    record = default_record()
    for key, value in raw.items():
        if isinstance(value, dict) and isinstance(record.get(key), dict):
            record[key].update(value)
        else:
            record[key] = value
    record["schema_version"] = SCHEMA_VERSION
    record["active_intent"]["success_criteria"] = clean_list(
        record["active_intent"].get("success_criteria", [])
    )
    record["active_intent"]["constraints"] = clean_list(
        record["active_intent"].get("constraints", [])
    )
    for key in ("support_gates", "expert_stack", "skipped_routes"):
        record["route"][key] = clean_list(record["route"].get(key, []))
    record["next_move"]["verification"] = clean_list(record["next_move"].get("verification", []))
    if not isinstance(record.get("history"), list):
        record["history"] = []
    return record


def load_record() -> dict[str, Any]:
    if not CURRENT_PATH.exists():
        raise SystemExit(f"Missing intent memory: {CURRENT_PATH.relative_to(ROOT)}")
    return merge_defaults(read_json(CURRENT_PATH))


def history_entry(record: dict[str, Any]) -> dict[str, Any]:
    intent = record.get("active_intent", {})
    route = record.get("route", {})
    next_move = record.get("next_move", {})
    return {
        "updated_at": record.get("updated_at", ""),
        "goal": intent.get("goal", ""),
        "chosen_route": route.get("chosen_route", ""),
        "next_move": next_move.get("action", ""),
    }


def write_record(record: dict[str, Any]) -> dict[str, Any]:
    record = merge_defaults(record)
    record["updated_at"] = now()
    atomic_write_json(CURRENT_PATH, record)
    system_cohesion_state.apply_intent_record(record)
    return record


def apply_args(record: dict[str, Any], args: argparse.Namespace, capture: bool = False) -> dict[str, Any]:
    timestamp = now()
    intent = record["active_intent"]
    if capture:
        intent["captured_at"] = timestamp

    updates = {
        "goal": args.goal,
        "deliverable": args.deliverable,
        "audience": args.audience,
        "clarity_score": args.clarity_score,
        "confidence": args.confidence,
        "ambiguity_map": args.ambiguity_map,
        "source": args.source,
    }
    for key, value in updates.items():
        if value is not None:
            intent[key] = value
    if args.success is not None:
        intent["success_criteria"] = clean_list(args.success)
    if args.constraint is not None:
        intent["constraints"] = clean_list(args.constraint)

    route_updates = {
        "mode": args.mode,
        "chosen_route": args.chosen_route,
    }
    for key, value in route_updates.items():
        if value is not None:
            record["route"][key] = value.lstrip("/") if key == "chosen_route" else value
    if args.support_gate is not None:
        record["route"]["support_gates"] = clean_list(args.support_gate)
    if args.expert is not None:
        record["route"]["expert_stack"] = clean_list(args.expert)
    if args.skipped_route is not None:
        record["route"]["skipped_routes"] = clean_list(
            [item.lstrip("/") for item in args.skipped_route]
        )

    mission_updates = {
        "slug": args.mission_slug,
        "state_path": args.mission_state_path,
        "status": args.mission_status,
    }
    for key, value in mission_updates.items():
        if value is not None:
            record["mission"][key] = value

    if args.next_move is not None:
        record["next_move"]["action"] = args.next_move
    if args.next_owner is not None:
        record["next_move"]["owner"] = args.next_owner
    if args.next_verification is not None:
        record["next_move"]["verification"] = clean_list(args.next_verification)
    return record


def capture(args: argparse.Namespace) -> None:
    existing = merge_defaults(read_json(CURRENT_PATH))
    record = default_record()
    prior_history = existing.get("history", [])
    if existing.get("active_intent", {}).get("goal"):
        prior_history = prior_history + [history_entry(existing)]
    record["history"] = prior_history[-10:]
    record = apply_args(record, args, capture=True)
    record = write_record(record)
    if args.json:
        print(json.dumps(record, indent=2, sort_keys=True))
    else:
        print(f"Captured intent memory: {CURRENT_PATH.relative_to(ROOT)}")
        print(f"Synced cohesion state: {system_cohesion_state.STATE_PATH.relative_to(ROOT)}")


def show(args: argparse.Namespace) -> None:
    record = load_record()
    if args.json:
        print(json.dumps(record, indent=2, sort_keys=True))
        return
    intent = record["active_intent"]
    route = record["route"]
    mission = record["mission"]
    next_move = record["next_move"]
    print(f"Intent memory: {CURRENT_PATH.relative_to(ROOT)}")
    print(f"Updated: {record['updated_at']}")
    print(f"Goal: {intent.get('goal') or '[empty]'}")
    print(f"Deliverable: {intent.get('deliverable') or '[empty]'}")
    print(f"Clarity score: {intent.get('clarity_score')}")
    print(f"Chosen route: /{route.get('chosen_route')}" if route.get("chosen_route") else "Chosen route: [none]")
    print(f"Support gates: {', '.join(route.get('support_gates', [])) or '[none]'}")
    print(f"Expert stack: {', '.join(route.get('expert_stack', [])) or '[none]'}")
    print(f"Mission: {mission.get('slug') or '[none]'}")
    print(f"Next move: {next_move.get('action') or '[none]'}")


def update(args: argparse.Namespace) -> None:
    record = load_record()
    record = apply_args(record, args)
    record = write_record(record)
    if args.json:
        print(json.dumps(record, indent=2, sort_keys=True))
    else:
        print(f"Updated intent memory: {CURRENT_PATH.relative_to(ROOT)}")
        print(f"Synced cohesion state: {system_cohesion_state.STATE_PATH.relative_to(ROOT)}")


def validate_record(record: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in record:
            failures.append(f"missing top-level key: {key}")
    if record.get("schema_version") != SCHEMA_VERSION:
        failures.append(f"schema_version must be {SCHEMA_VERSION}")
    for key in ("active_intent", "route", "mission", "next_move"):
        if not isinstance(record.get(key), dict):
            failures.append(f"{key} must be an object")
    if not isinstance(record.get("history"), list):
        failures.append("history must be a list")
    intent = record.get("active_intent", {})
    if not str(intent.get("goal", "")).strip():
        failures.append("active_intent.goal is required")
    score = intent.get("clarity_score")
    if score is not None and (not isinstance(score, int) or score < 0 or score > 100):
        failures.append("active_intent.clarity_score must be an integer from 0 to 100")
    route = record.get("route", {})
    for key in ("support_gates", "expert_stack", "skipped_routes"):
        if not isinstance(route.get(key, []), list):
            failures.append(f"route.{key} must be a list")
    if not isinstance(record.get("next_move", {}).get("verification", []), list):
        failures.append("next_move.verification must be a list")
    return failures


def verify(args: argparse.Namespace) -> None:
    record = load_record()
    failures = validate_record(record)
    cohesion = system_cohesion_state.load_state()
    failures.extend(system_cohesion_state.validate_state(cohesion))
    if cohesion.get("active_intent", {}).get("goal") != record.get("active_intent", {}).get("goal"):
        failures.append("cohesion active_intent.goal does not match intent memory")
    if cohesion.get("chosen_route", {}).get("route") != record.get("route", {}).get("chosen_route"):
        failures.append("cohesion chosen_route.route does not match intent memory")
    if failures:
        print("Intent memory verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print("Intent memory verification: PASS")


def add_record_arguments(parser: argparse.ArgumentParser, require_goal: bool = False) -> None:
    parser.add_argument("--goal", required=require_goal)
    parser.add_argument("--deliverable")
    parser.add_argument("--audience")
    parser.add_argument("--success", action="append")
    parser.add_argument("--constraint", action="append")
    parser.add_argument("--clarity-score", type=int)
    parser.add_argument("--confidence")
    parser.add_argument("--ambiguity-map")
    parser.add_argument("--source")
    parser.add_argument("--mode")
    parser.add_argument("--chosen-route")
    parser.add_argument("--support-gate", action="append")
    parser.add_argument("--expert", action="append")
    parser.add_argument("--skipped-route", action="append")
    parser.add_argument("--mission-slug")
    parser.add_argument("--mission-state-path")
    parser.add_argument("--mission-status")
    parser.add_argument("--next-move")
    parser.add_argument("--next-owner")
    parser.add_argument("--next-verification", action="append")
    parser.add_argument("--json", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture and maintain workspace-local intent memory")
    sub = parser.add_subparsers(dest="command", required=True)

    capture_cmd = sub.add_parser("capture", help="Capture a fresh current intent")
    add_record_arguments(capture_cmd, require_goal=True)
    capture_cmd.set_defaults(func=capture)

    show_cmd = sub.add_parser("show", help="Show the current intent memory")
    show_cmd.add_argument("--json", action="store_true")
    show_cmd.set_defaults(func=show)

    update_cmd = sub.add_parser("update", help="Update the current intent memory")
    add_record_arguments(update_cmd)
    update_cmd.set_defaults(func=update)

    verify_cmd = sub.add_parser("verify", help="Validate intent memory and cohesion sync")
    verify_cmd.set_defaults(func=verify)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
