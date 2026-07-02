#!/usr/bin/env python3
"""Verify the Raw Intent Virtuoso Bridge packet compiler."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import raw_intent_run_packet  # type: ignore  # noqa: E402


PREFIXES = ("/raw-intent-bridge", "raw-intent-bridge:", "source-command-raw-intent-bridge:")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_prefix_stripped(packet: dict, label: str) -> None:
    for field in ("raw_intent", "first_safe_action", "operator_run_prompt"):
        value = str(packet[field]).lower()
        for prefix in PREFIXES:
            require(prefix.lower() not in value, f"{label} leaked {prefix} into {field}: {packet[field]}")


def assert_packet_shape(packet: dict) -> None:
    required = {
        "raw_intent",
        "predicted_need",
        "center",
        "success_standard",
        "constraints",
        "missing_inputs",
        "questions_that_change_execution",
        "chosen_route",
        "support_gates",
        "composition_slots",
        "context_plan",
        "execution_decision",
        "first_safe_action",
        "verification_plan",
        "operator_run_prompt",
        "plugin_packaging_verdict",
    }
    missing = sorted(required - set(packet))
    require(not missing, f"packet missing fields: {missing}")
    require(len(packet["composition_slots"]) == 5, "packet must include five composition slots")
    require(packet["plugin_packaging_verdict"]["status"] == "deferred", "plugin packaging must be deferred in v1")
    require(
        "global ~/.codex writes during normal packet runs" in packet["context_plan"]["skip"],
        "normal packet runs must skip global writes",
    )
    require("python3 execution/verify_raw_intent_global_skill.py" in packet["verification_plan"], "global skill verifier missing")
    require("python3 execution/verify_raw_intent_bridge_command.py" in packet["verification_plan"], "command verifier missing")
    require("python3 execution/verify_raw_intent_run_packet.py" in packet["verification_plan"], "self verifier missing")


def main() -> int:
    revenue = raw_intent_run_packet.build_packet(
        "I have messy notes and need to make money with an offer but I do not know how to ask Codex",
        mode="revenue",
    )
    assert_packet_shape(revenue)
    require(revenue["chosen_route"] in {"first-10k", "revenue-offer-agent", "client-acquire"}, "revenue fixture did not choose a revenue route")
    require(
        {"revenue-offer-agent", "client-acquire"} & set(revenue["support_gates"]),
        "revenue fixture missing revenue support gates",
    )

    creative = raw_intent_run_packet.build_packet(
        "I have a rough campaign idea and need world-class creative content but I do not know how to ask Codex",
        mode="creative",
    )
    assert_packet_shape(creative)
    require(
        {"high-taste-writing-os", "publishable-copy-gate", "excellence-gate"} & set(creative["support_gates"]),
        "creative fixture missing creative quality gates",
    )
    require(creative["chosen_route"] not in {"orlean-research-to-story", "orlean-yarn-engine"}, "creative fixture captured unrelated literary route")

    system = raw_intent_run_packet.build_packet(
        "Build a raw intent bridge and run packet companion layer so I do not need to know how to ask Codex",
        mode="system",
    )
    assert_packet_shape(system)
    require(system["chosen_route"] == "source-to-skill-system", "system fixture should choose /source-to-skill-system")
    require({"autopilot", "virtuoso"} <= set(system["support_gates"]), "system fixture missing Autopilot/Virtuoso support")

    regression = raw_intent_run_packet.build_packet(
        "Be my world-class prompt engineer and virtuoso for entrepreneurial tasks because I do not know how to ask Codex",
        mode="auto",
    )
    assert_packet_shape(regression)
    require(
        regression["chosen_route"] in {"autopilot", "source-to-skill-system"},
        f"regression fixture misrouted to /{regression['chosen_route']}",
    )
    require(regression["chosen_route"] not in {"albom-theme-first-engine", "connelly-brand-momentum"}, "prompt wording captured unrelated creative-writing route")

    prefix_fixtures = {
        "slash": (
            "/raw-intent-bridge I have a messy business idea and need the right execution path",
            {"autopilot", "first-10k", "revenue-offer-agent", "client-acquire"},
        ),
        "colon": (
            "raw-intent-bridge: I have a rough offer idea but do not know how to ask Codex",
            {"first-10k", "revenue-offer-agent", "client-acquire"},
        ),
        "source-command": (
            "source-command-raw-intent-bridge: audit this raw task and give me the first safe action",
            {"system-audit", "autopilot", "source-to-skill-system"},
        ),
    }
    for label, (intent, allowed_routes) in prefix_fixtures.items():
        packet = raw_intent_run_packet.build_packet(intent, mode="auto")
        assert_packet_shape(packet)
        assert_prefix_stripped(packet, label)
        require(packet["chosen_route"] in allowed_routes, f"{label} fixture chose unexpected route: {packet['chosen_route']}")
        require(packet["first_safe_action"].startswith("/"), f"{label} first safe action is not executable: {packet['first_safe_action']}")

    cli = subprocess.run(
        [
            sys.executable,
            "execution/raw_intent_run_packet.py",
            "raw intent bridge for Codex run packets",
            "--mode",
            "system",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(cli.returncode == 0, f"CLI failed: {cli.stderr}")
    parsed = json.loads(cli.stdout)
    assert_packet_shape(parsed)
    require(parsed["chosen_route"] == "source-to-skill-system", "CLI system mode did not choose source-to-skill-system")
    assert_prefix_stripped(parsed, "json CLI")

    plain = subprocess.run(
        [
            sys.executable,
            "execution/raw_intent_run_packet.py",
            "messy context and I do not know how to ask Codex",
            "--plain",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(plain.returncode == 0, f"plain CLI failed: {plain.stderr}")
    require("## Raw Intent Run Packet" in plain.stdout, "plain renderer missing packet header")

    print("Raw Intent Virtuoso Bridge verification: PASS")
    print("- revenue fixture routes toward revenue/offer work")
    print("- creative fixture exposes quality gates")
    print("- system fixture routes to /source-to-skill-system with Autopilot/Virtuoso support")
    print("- prompt-engineer/virtuoso wording does not misroute into unrelated creative-writing routes")
    print("- slash, colon, and source-command prefix forms strip before route/action generation")
    print("- JSON and plain CLIs render valid packets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
