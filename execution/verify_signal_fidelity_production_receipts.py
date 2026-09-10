#!/usr/bin/env python3
"""Verify three real-artifact Signal Fidelity SHADOW receipts and their limits."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from signal_fidelity_shadow import evaluate


ROOT = Path(__file__).resolve().parents[1]
RECEIPTS = ROOT / "extractions/video-context/1KOdiGgMtpY/validation/production-receipts-v1"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def words(text: str) -> int:
    return len(re.findall(r"\b[\w$'-]+\b", text))


def marker_present(text: str, markers: list[str]) -> bool:
    normalized = " ".join(text.casefold().split())
    return any(" ".join(marker.casefold().split()) in normalized for marker in markers)


def recoverability_scores(rubric: dict) -> dict[str, dict[str, object]]:
    scores: dict[str, dict[str, object]] = {}
    for artifact_id, spec in rubric["artifacts"].items():
        path = ROOT / spec["path"] if spec.get("root_relative") else RECEIPTS / spec["path"]
        text = path.read_text(encoding="utf-8")
        recovered = [
            dimension
            for dimension, markers in spec["markers"].items()
            if marker_present(text, markers)
        ]
        scores[artifact_id] = {
            "recovered": recovered,
            "score": len(recovered),
            "total": len(rubric["dimensions"]),
            "words": words(text),
        }
    return scores


def strategy_contract() -> dict:
    return {
        "recipient": "Farrice deciding whether to run the seven-day revenue sprint",
        "intended_change": "decide whether to prepare three Authority Flywheel demonstrations",
        "source_of_conviction": "free work can act as delivery proof and marketing",
        "promise": "seek one paid pilot and create reusable portfolio proof",
        "limit": "conversion math is an assumption and external action remains approval-gated",
        "proof_state": "NO EVENT",
        "human_owner": "Farrice",
        "source_path": "_active/linkedin/05-lead-gen/demo-proof-strategy.md",
        "must_survive": [
            {"id": "three-targets", "kind": "decision", "markers": ["three Authority Flywheel demonstrations", "three targets"], "required_in": ["artifact"]},
            {"id": "seven-days", "kind": "decision", "markers": ["seven-day"], "required_in": ["artifact"]},
            {"id": "pilot-range", "kind": "decision", "markers": ["$500-$750"], "required_in": ["artifact"]},
            {"id": "portfolio-proof", "kind": "decision", "markers": ["portfolio proof", "portfolio evidence"], "required_in": ["artifact"]},
            {"id": "approval-boundary", "kind": "limit", "markers": ["separate approval", "approval before external action"], "required_in": ["artifact"]}
        ],
    }


def handoff_contract() -> dict:
    return {
        "recipient": "the next offer-packaging collaborator or AI agent",
        "intended_change": "continue the existing Jen-Team Pilot package without rebuilding it",
        "source_of_conviction": "a bounded founding offer needs clear delivery and kill criteria",
        "promise": "a pitchable and repeatable $200 Listing Launch Kit",
        "limit": "do not widen the offer or perform external pitching",
        "proof_state": "UNTESTED",
        "human_owner": "Farrice",
        "source_path": ".agent/handoffs/2026-08-29-offer-packaging.md",
        "must_survive": [
            {"id": "founding-price", "kind": "decision", "markers": ["$200 founding"], "required_in": ["artifact"]},
            {"id": "fallback", "kind": "handoff", "markers": ["fallback offer", "fallback SKU"], "required_in": ["artifact"]},
            {"id": "three-pitches", "kind": "handoff", "markers": ["three pitch drafts"], "required_in": ["artifact"]},
            {"id": "six-steps", "kind": "handoff", "markers": ["six-step", "six delivery steps"], "required_in": ["artifact"]},
            {"id": "trial", "kind": "handoff", "markers": ["30-day trial"], "required_in": ["artifact"]},
            {"id": "kill", "kind": "limit", "markers": ["kill criteria", "kill-criteria"], "required_in": ["artifact"]},
            {"id": "no-rebuild", "kind": "limit", "markers": ["don't rebuild", "don’t rebuild", "Do not rebuild"], "required_in": ["artifact"]}
        ],
    }


def main() -> int:
    failures: list[str] = []
    manifest = load_json(RECEIPTS / "manifest.json")

    for case in manifest["cases"]:
        source = ROOT / case["source_path"]
        if sha256(source) != case["source_sha256"]:
            failures.append(f"{case['id']}: frozen source hash changed")

    rubric = load_json(RECEIPTS / "recoverability-rubric.json")
    scores = recoverability_scores(rubric)
    expected_scores = {
        "strategy_native": 5,
        "strategy_signal": 6,
        "handoff_human": 6,
        "handoff_ai_agent": 6,
        "public_content": 6,
    }
    for artifact_id, expected in expected_scores.items():
        if scores[artifact_id]["score"] != expected:
            failures.append(
                f"{artifact_id}: recoverability {scores[artifact_id]['score']}/6, expected {expected}/6"
            )

    strategy_text = (RECEIPTS / "strategy-signal.md").read_text(encoding="utf-8")
    strategy = evaluate({
        "recipient_mode": "strategy",
        "signal_contract": strategy_contract(),
        "artifact_text": strategy_text,
        "artifact_proof_state": "NO EVENT",
        "playback_text": "",
    })

    human_text = (RECEIPTS / "handoff-human.md").read_text(encoding="utf-8")
    human = evaluate({
        "recipient_mode": "human",
        "signal_contract": handoff_contract(),
        "artifact_text": human_text,
        "artifact_proof_state": "UNTESTED",
        "playback_text": "",
    })

    ai_text = (RECEIPTS / "handoff-ai-agent.md").read_text(encoding="utf-8")
    ai = evaluate({
        "recipient_mode": "ai_agent",
        "signal_contract": handoff_contract(),
        "artifact_text": ai_text,
        "artifact_proof_state": "UNTESTED",
        "playback_text": "",
    })

    public_packet = load_json(RECEIPTS / "public-content-audit.json")
    public_path = ROOT / public_packet["signal_contract"]["source_path"]
    public_packet["artifact_text"] = public_path.read_text(encoding="utf-8")
    public = evaluate(public_packet)

    reports = {
        "strategy": strategy,
        "handoff_human": human,
        "handoff_ai_agent": ai,
        "public_content": public,
    }
    for report_id, report in reports.items():
        if report["enforcement"] or report["can_block"]:
            failures.append(f"{report_id}: acquired enforcement or blocking authority")
        if report["surface_policy"]["composition_authority"] or report["surface_policy"]["can_mutate_artifact"]:
            failures.append(f"{report_id}: acquired composition or mutation authority")
        if any("?" in cue for cue in report["human_review"]):
            failures.append(f"{report_id}: generated a review question")
        if report["distortion_hypotheses"]:
            failures.append(f"{report_id}: reported an unexpected marker distortion")

    if not strategy["signal_capsule"] or not ai["signal_capsule"]:
        failures.append("strategy or AI-agent mode failed to expose its selected capsule")
    if human["signal_capsule"] is not None or public["signal_capsule"] is not None:
        failures.append("human or public-content mode exposed a signal capsule")
    if not human["native_surface_primary"] or not public["native_surface_primary"]:
        failures.append("human or public-content native surface is not primary")
    if public["manual_checks"] == []:
        failures.append("public-content audit lost the owner-only creative meaning cue")

    if failures:
        print("Signal Fidelity production receipts: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    strategy_delta = scores["strategy_signal"]["words"] - scores["strategy_native"]["words"]
    handoff_delta = scores["handoff_ai_agent"]["words"] - scores["handoff_human"]["words"]
    print("Signal Fidelity production receipts: PASS")
    print(f"- strategy recoverability: native 5/6 -> signal 6/6; visible word delta {strategy_delta:+d}")
    print(f"- paired handoff recoverability: human 6/6; AI agent 6/6; AI word delta {handoff_delta:+d}")
    print("- public content recoverability: 6/6; visible artifact unchanged; visible word delta +0")
    print("- generated questions, false blocks, proof upgrades, and mutations: 0")
    print("- independent human comprehension: NO EVENT")
    print("- field effect and trust effect: UNTESTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
