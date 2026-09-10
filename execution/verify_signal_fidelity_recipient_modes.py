#!/usr/bin/env python3
"""Replay the frozen recipient-mode repair without promoting Signal Fidelity."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from signal_fidelity_shadow import evaluate


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "extractions/video-context/1KOdiGgMtpY/validation/real-work-pilot-v1"
FIXTURES = ROOT / "execution/fixtures/signal-fidelity-shadow"

CASES = {
    "strategy": {
        "candidate": "strategy-treatment.md",
        "recipient_mode": "strategy",
        "sha256": "6175b00b95fe5c0a969781def0e24bd25e8195aa1012618e7692ce71ab07d0cb",
        "native_surface": False,
        "capsule": "explicit",
    },
    "content": {
        "candidate": "content-baseline.md",
        "recipient_mode": "public_content",
        "sha256": "05d3e2e6f120c8ecc39251d86b32306f0ae6124fe5d68999f61964e5706aa3b8",
        "native_surface": True,
        "capsule": "audit_only",
    },
    "handoff_human": {
        "manifest_case": "handoff",
        "candidate": "handoff-baseline.md",
        "recipient_mode": "human",
        "sha256": "9b5d222c8fd59743e2f653b4725e9029456c0f94ebc6a35f3ef1280be78844b3",
        "native_surface": True,
        "capsule": "cold",
    },
    "handoff_ai_agent": {
        "manifest_case": "handoff",
        "candidate": "handoff-treatment.md",
        "recipient_mode": "ai_agent",
        "sha256": "fb090d91fd3616a7894e0252c2a2315ef737c50d8b802400a822a70d70da7df3",
        "native_surface": False,
        "capsule": "explicit",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    manifest = load_json(PILOT / "manifest.json")
    contracts = {case["id"]: case["signal_contract"] for case in manifest["cases"]}
    failures: list[str] = []
    replayed: list[str] = []

    for replay_name, case in CASES.items():
        candidate = PILOT / "candidates" / case["candidate"]
        actual_hash = sha256(candidate)
        if actual_hash != case["sha256"]:
            failures.append(f"{replay_name}: frozen visible artifact hash changed")
            continue

        manifest_case = case.get("manifest_case", replay_name)
        packet = {
            "recipient_mode": case["recipient_mode"],
            "signal_contract": contracts[manifest_case],
            "artifact_text": candidate.read_text(encoding="utf-8"),
            "playback_text": "",
            "artifact_proof_state": contracts[manifest_case]["proof_state"],
        }
        report = evaluate(packet)
        policy = report["surface_policy"]
        replayed.append(replay_name)

        if report["enforcement"] or report["can_block"]:
            failures.append(f"{replay_name}: acquired enforcement or blocking authority")
        if policy["composition_authority"] or policy["can_mutate_artifact"]:
            failures.append(f"{replay_name}: acquired composition or mutation authority")
        if report["native_surface_primary"] is not case["native_surface"]:
            failures.append(f"{replay_name}: wrong native-surface policy")
        if policy["signal_capsule"] != case["capsule"]:
            failures.append(f"{replay_name}: wrong capsule delivery policy")
        expected_explicit = case["capsule"] == "explicit"
        if bool(report["signal_capsule"]) is not expected_explicit:
            failures.append(f"{replay_name}: explicit capsule visibility mismatch")
        if any("?" in cue for cue in report["human_review"]):
            failures.append(f"{replay_name}: generated a review question")

    manual_packet = load_json(FIXTURES / "metaphor-manual.json")
    manual_packet["recipient_mode"] = "public_content"
    manual = evaluate(manual_packet)
    if manual["distortion_hypotheses"] or manual["signal_capsule"] is not None:
        failures.append("creative/manual control alleged distortion or exposed a capsule")
    if manual["surface_policy"]["composition_authority"]:
        failures.append("creative/manual control acquired composition authority")

    sparse_packet = load_json(FIXTURES / "sparse-brief-not-selected.json")
    sparse_packet["recipient_mode"] = "public_content"
    sparse = evaluate(sparse_packet)
    if sparse["decision"] != "NOT_RUN" or sparse["human_review"]:
        failures.append("sparse control added review burden")

    if failures:
        print("Signal Fidelity recipient-mode replay: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Signal Fidelity recipient-mode replay: PASS")
    print(f"- frozen visible artifacts: {len(replayed)}/4 unchanged")
    print("- strategy: explicit selected decision receipt")
    print("- AI-agent handoff: explicit execution capsule")
    print("- human handoff: native summary plus cold sidecar")
    print("- public content: native artifact plus owner-only audit")
    print("- creative/manual control: no distortion allegation and no composition authority")
    print("- sparse control: NOT_RUN with no review burden")
    print("- enforcement, blocking, mutation, and generated questions: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
