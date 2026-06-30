#!/usr/bin/env python3
"""Shared cohesion-state helper for Codex Antigravity.

The cohesion state is the compact handoff spine between Autopilot, Mission OS,
verifiers, and future weekly platter work. It intentionally stores only the
current operating picture, not a heavy session transcript.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "system-cohesion-state/v1"


def workspace_root() -> Path:
    override = os.environ.get("ANTIGRAVITY_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


ROOT = workspace_root()
AGENT_DIR = ROOT / ".agent"
STATE_PATH = AGENT_DIR / "system-cohesion-state.json"

REQUIRED_TOP_LEVEL_KEYS = (
    "schema_version",
    "updated_at",
    "active_intent",
    "mission",
    "chosen_route",
    "support_gates",
    "expert_stack",
    "activation_queue",
    "verifier_status",
    "weekly_platter",
    "next_move",
)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def clean_list(values: list[str] | None) -> list[str]:
    if not values:
        return []
    seen: set[str] = set()
    cleaned: list[str] = []
    for value in values:
        item = str(value).strip()
        if item and item not in seen:
            cleaned.append(item)
            seen.add(item)
    return cleaned


def default_state() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "updated_at": now(),
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
        },
        "mission": {
            "slug": "",
            "state_path": "",
            "status": "",
        },
        "chosen_route": {
            "route": "",
            "mode": "",
            "reason": "",
        },
        "support_gates": [],
        "expert_stack": [],
        "activation_queue": [],
        "verifier_status": {
            "py_compile": "not_run",
            "intent_memory_contract": "not_run",
            "system_cohesion_spine": "not_run",
            "last_checked_at": "",
        },
        "weekly_platter": {
            "status": "not_started",
            "path": "",
            "last_generated_at": "",
            "next_due": "",
        },
        "next_move": {
            "action": "",
            "owner": "",
            "verification": [],
        },
    }


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def merge_defaults(raw: dict[str, Any]) -> dict[str, Any]:
    state = default_state()
    for key, value in raw.items():
        if isinstance(value, dict) and isinstance(state.get(key), dict):
            state[key].update(value)
        else:
            state[key] = value
    state["schema_version"] = SCHEMA_VERSION
    for key in ("support_gates", "expert_stack", "activation_queue"):
        state[key] = clean_list(state.get(key, []))
    state["active_intent"]["success_criteria"] = clean_list(
        state["active_intent"].get("success_criteria", [])
    )
    state["active_intent"]["constraints"] = clean_list(
        state["active_intent"].get("constraints", [])
    )
    state["next_move"]["verification"] = clean_list(
        state["next_move"].get("verification", [])
    )
    return state


def load_state(create: bool = False) -> dict[str, Any]:
    if not STATE_PATH.exists():
        if create:
            return default_state()
        raise SystemExit(f"Missing cohesion state: {STATE_PATH.relative_to(ROOT)}")
    return merge_defaults(read_json(STATE_PATH))


def write_state(state: dict[str, Any]) -> None:
    state = merge_defaults(state)
    state["updated_at"] = now()
    atomic_write_json(STATE_PATH, state)


def apply_intent_record(record: dict[str, Any]) -> dict[str, Any]:
    state = merge_defaults(read_json(STATE_PATH))
    intent = record.get("active_intent", {})
    route = record.get("route", {})
    mission = record.get("mission", {})
    next_move = record.get("next_move", {})

    state["active_intent"].update(
        {
            "goal": intent.get("goal", state["active_intent"].get("goal", "")),
            "deliverable": intent.get(
                "deliverable", state["active_intent"].get("deliverable", "")
            ),
            "audience": intent.get("audience", state["active_intent"].get("audience", "")),
            "success_criteria": clean_list(
                intent.get("success_criteria", state["active_intent"].get("success_criteria", []))
            ),
            "constraints": clean_list(
                intent.get("constraints", state["active_intent"].get("constraints", []))
            ),
            "clarity_score": intent.get(
                "clarity_score", state["active_intent"].get("clarity_score")
            ),
            "confidence": intent.get(
                "confidence", state["active_intent"].get("confidence", "")
            ),
            "ambiguity_map": intent.get(
                "ambiguity_map", state["active_intent"].get("ambiguity_map", "")
            ),
            "source": intent.get("source", state["active_intent"].get("source", "")),
        }
    )
    state["mission"].update(
        {
            "slug": mission.get("slug", state["mission"].get("slug", "")),
            "state_path": mission.get("state_path", state["mission"].get("state_path", "")),
            "status": mission.get("status", state["mission"].get("status", "")),
        }
    )
    state["chosen_route"].update(
        {
            "route": route.get("chosen_route", state["chosen_route"].get("route", "")),
            "mode": route.get("mode", state["chosen_route"].get("mode", "")),
        }
    )
    if route.get("support_gates") is not None:
        state["support_gates"] = clean_list(route.get("support_gates", []))
    if route.get("expert_stack") is not None:
        state["expert_stack"] = clean_list(route.get("expert_stack", []))
    state["next_move"].update(
        {
            "action": next_move.get("action", state["next_move"].get("action", "")),
            "owner": next_move.get("owner", state["next_move"].get("owner", "")),
            "verification": clean_list(
                next_move.get("verification", state["next_move"].get("verification", []))
            ),
        }
    )
    write_state(state)
    return state


def parse_verifier(values: list[str] | None) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for value in values or []:
        if "=" not in value:
            raise SystemExit(f"Verifier must use name=status format: {value}")
        name, status = value.split("=", 1)
        name = name.strip()
        status = status.strip()
        if not name or not status:
            raise SystemExit(f"Verifier must use name=status format: {value}")
        parsed[name] = status
    return parsed


def update_from_args(args: argparse.Namespace) -> dict[str, Any]:
    state = load_state(create=True)
    intent_updates = {
        "goal": args.intent_goal,
        "deliverable": args.intent_deliverable,
        "audience": args.intent_audience,
        "clarity_score": args.clarity_score,
        "confidence": args.confidence,
        "ambiguity_map": args.ambiguity_map,
        "source": args.source,
    }
    for key, value in intent_updates.items():
        if value is not None:
            state["active_intent"][key] = value
    if args.success is not None:
        state["active_intent"]["success_criteria"] = clean_list(args.success)
    if args.constraint is not None:
        state["active_intent"]["constraints"] = clean_list(args.constraint)

    mission_updates = {
        "slug": args.mission_slug,
        "state_path": args.mission_state_path,
        "status": args.mission_status,
    }
    for key, value in mission_updates.items():
        if value is not None:
            state["mission"][key] = value

    route_updates = {
        "route": args.route,
        "mode": args.mode,
        "reason": args.route_reason,
    }
    for key, value in route_updates.items():
        if value is not None:
            state["chosen_route"][key] = value

    if args.support_gate is not None:
        state["support_gates"] = clean_list(args.support_gate)
    if args.expert is not None:
        state["expert_stack"] = clean_list(args.expert)
    if args.activation is not None:
        state["activation_queue"] = clean_list(args.activation)

    verifier_updates = parse_verifier(args.verifier)
    if verifier_updates:
        state["verifier_status"].update(verifier_updates)
        state["verifier_status"]["last_checked_at"] = now()

    weekly_updates = {
        "status": args.weekly_platter_status,
        "path": args.weekly_platter_path,
        "last_generated_at": args.weekly_platter_last_generated_at,
        "next_due": args.weekly_platter_next_due,
    }
    for key, value in weekly_updates.items():
        if value is not None:
            state["weekly_platter"][key] = value

    if args.next_move is not None:
        state["next_move"]["action"] = args.next_move
    if args.next_owner is not None:
        state["next_move"]["owner"] = args.next_owner
    if args.next_verification is not None:
        state["next_move"]["verification"] = clean_list(args.next_verification)

    write_state(state)
    return load_state()


def validate_state(state: dict[str, Any], require_active: bool = True) -> list[str]:
    failures: list[str] = []
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in state:
            failures.append(f"missing top-level key: {key}")
    if state.get("schema_version") != SCHEMA_VERSION:
        failures.append(f"schema_version must be {SCHEMA_VERSION}")
    for key in ("active_intent", "mission", "chosen_route", "verifier_status", "weekly_platter", "next_move"):
        if not isinstance(state.get(key), dict):
            failures.append(f"{key} must be an object")
    for key in ("support_gates", "expert_stack", "activation_queue"):
        if not isinstance(state.get(key), list):
            failures.append(f"{key} must be a list")
    intent = state.get("active_intent", {})
    if require_active and not str(intent.get("goal", "")).strip():
        failures.append("active_intent.goal is required")
    score = intent.get("clarity_score")
    if score is not None and (not isinstance(score, int) or score < 0 or score > 100):
        failures.append("active_intent.clarity_score must be an integer from 0 to 100")
    if not isinstance(state.get("next_move", {}).get("verification", []), list):
        failures.append("next_move.verification must be a list")
    return failures


def render_summary(state: dict[str, Any]) -> str:
    intent = state["active_intent"]
    route = state["chosen_route"]
    mission = state["mission"]
    next_move = state["next_move"]
    return "\n".join(
        [
            f"State: {STATE_PATH.relative_to(ROOT)}",
            f"Updated: {state['updated_at']}",
            f"Active intent: {intent.get('goal') or '[empty]'}",
            f"Mission: {mission.get('slug') or '[none]'} ({mission.get('status') or 'not_recorded'})",
            f"Chosen route: /{route.get('route')}" if route.get("route") else "Chosen route: [none]",
            f"Support gates: {', '.join(state['support_gates']) or '[none]'}",
            f"Expert stack: {', '.join(state['expert_stack']) or '[none]'}",
            f"Activation queue: {', '.join(state['activation_queue']) or '[none]'}",
            f"Verifier status: {json.dumps(state['verifier_status'], sort_keys=True)}",
            f"Weekly platter: {state['weekly_platter'].get('status') or '[none]'}",
            f"Next move: {next_move.get('action') or '[none]'}",
        ]
    )


def show(args: argparse.Namespace) -> None:
    state = load_state()
    if args.json:
        print(json.dumps(state, indent=2, sort_keys=True))
    else:
        print(render_summary(state))


def update(args: argparse.Namespace) -> None:
    state = update_from_args(args)
    if args.json:
        print(json.dumps(state, indent=2, sort_keys=True))
    else:
        print(f"Updated cohesion state: {STATE_PATH.relative_to(ROOT)}")


def verify(args: argparse.Namespace) -> None:
    state = load_state()
    failures = validate_state(state, require_active=not args.allow_empty)
    if failures:
        print("System cohesion state verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print("System cohesion state verification: PASS")


def add_update_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--intent-goal")
    parser.add_argument("--intent-deliverable")
    parser.add_argument("--intent-audience")
    parser.add_argument("--success", action="append")
    parser.add_argument("--constraint", action="append")
    parser.add_argument("--clarity-score", type=int)
    parser.add_argument("--confidence")
    parser.add_argument("--ambiguity-map")
    parser.add_argument("--source")
    parser.add_argument("--mission-slug")
    parser.add_argument("--mission-state-path")
    parser.add_argument("--mission-status")
    parser.add_argument("--route")
    parser.add_argument("--mode")
    parser.add_argument("--route-reason")
    parser.add_argument("--support-gate", action="append")
    parser.add_argument("--expert", action="append")
    parser.add_argument("--activation", action="append")
    parser.add_argument("--verifier", action="append", help="Use name=status. Can be repeated.")
    parser.add_argument("--weekly-platter-status")
    parser.add_argument("--weekly-platter-path")
    parser.add_argument("--weekly-platter-last-generated-at")
    parser.add_argument("--weekly-platter-next-due")
    parser.add_argument("--next-move")
    parser.add_argument("--next-owner")
    parser.add_argument("--next-verification", action="append")
    parser.add_argument("--json", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read and update the shared system cohesion state")
    sub = parser.add_subparsers(dest="command", required=True)

    show_cmd = sub.add_parser("show", help="Show the current cohesion state")
    show_cmd.add_argument("--json", action="store_true")
    show_cmd.set_defaults(func=show)

    update_cmd = sub.add_parser("update", help="Update fields in the cohesion state")
    add_update_arguments(update_cmd)
    update_cmd.set_defaults(func=update)

    verify_cmd = sub.add_parser("verify", help="Validate the cohesion-state contract")
    verify_cmd.add_argument("--allow-empty", action="store_true")
    verify_cmd.set_defaults(func=verify)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
