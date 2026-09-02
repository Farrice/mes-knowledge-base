#!/usr/bin/env python3
"""Verify source fidelity, routing surfaces, prompts, applied proof and no-call boundaries."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE = ROOT / "extractions/tom-youngs/sources/2026-08-25-three-sales-assets"
SKILL = ROOT / "skills/john-whiting-propaganda-machine"
APPLIED = ROOT / "deliverables/marketing-engineering/health-performance-control-beater/zero-call-three-asset-system"
sys.path.insert(0, str(ROOT / "execution"))
from prose_classifier import classify_prose  # noqa: E402


def require(path: Path, failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"missing: {path.relative_to(ROOT)}")
        return ""
    if path.is_file() and path.stat().st_size == 0:
        failures.append(f"empty: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8", errors="ignore") if path.is_file() else ""


def contains(text: str, needles: list[str], label: str, failures: list[str]) -> None:
    for needle in needles:
        if needle not in text:
            failures.append(f"{label} missing required marker: {needle}")


def section_between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def main() -> int:
    failures: list[str] = []

    source_files = [
        "metadata.json",
        "source-metadata-raw.json",
        "transcript.vtt",
        "transcript.txt",
        "transcript_segments.json",
        "analysis.md",
        "video-context-ledger.md",
        "frame-notes.md",
        "uncertainty-report.md",
        "skill-system-contract.md",
    ]
    for name in source_files:
        require(SOURCE / name, failures)
    frames = sorted((SOURCE / "frames").glob("cue_*.jpg"))
    if len(frames) != 12:
        failures.append(f"expected 12 reviewed frames, found {len(frames)}")

    try:
        segments = json.loads((SOURCE / "transcript_segments.json").read_text(encoding="utf-8"))
        if not isinstance(segments, list) or len(segments) < 100:
            failures.append("transcript_segments.json must contain at least 100 segments")
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid transcript segments: {exc}")

    ledger = require(SOURCE / "video-context-ledger.md", failures)
    contains(
        ledger,
        ["SOURCE SELF-REPORT - UNVERIFIED", "SOURCE GAP", "Model", "Machine", "Invite", "TY-018"],
        "source ledger",
        failures,
    )

    workflow = require(SKILL / "workflows/jw-three-asset-close.md", failures)
    contains(
        workflow,
        [
            "Offer Truth Packet",
            "DISCOVER_FIRST",
            "HOLD",
            "REJECT",
            "No setter. No closer. No pre-sale call.",
            "Model: sell the shift",
            "Machine: sell the vehicle",
            "Invite: invite the right person",
            "Market state remains `NO EVENT`",
        ],
        "workflow",
        failures,
    )

    prompt_names = [
        "model-belief-shift-video.md",
        "machine-inspection-video.md",
        "invite-decision-document.md",
        "zero-call-close-path.md",
    ]
    required_prompt_sections = [
        "## Role & Activation",
        "## Input Required",
        "## Execution Protocol",
        "## Output Contract",
        "## Output Skeleton",
        "## Quality Gate",
        "## Deploy When",
    ]
    for name in prompt_names:
        text = require(SKILL / "references/prompts-v2" / name, failures)
        contains(text, required_prompt_sections, name, failures)

    bridge_files = [
        ROOT / ".agent/workflows/jw-three-asset-close.md",
        ROOT / ".claude/commands/jw-three-asset-close.md",
        ROOT / ".agents/skills/source-command-jw-three-asset-close/SKILL.md",
    ]
    for path in bridge_files:
        require(path, failures)

    applied_names = [
        "README.md",
        "README.metadata.json",
        "00-offer-truth-packet.md",
        "offer-truth-packet.json",
        "01-model-belief-shift-video.md",
        "02-machine-inspection-video.md",
        "03-invite-decision-document.md",
        "04-zero-call-close-path.md",
        "05-behavior-proof.md",
        "06-expert-business-adapter.md",
    ]
    for name in applied_names:
        require(APPLIED / name, failures)

    model = require(APPLIED / "01-model-belief-shift-video.md", failures)
    if "$500" in model or "five static" in model.lower():
        failures.append("Model leaks offer price or deliverable count")
    contains(model, ["problem-aware", "solution-aware", "Decision before design", "Machine handoff"], "Model", failures)
    model_spoken = section_between(model, "## Record-ready script", "## Proof ledger")
    if classify_prose(model_spoken).get("verdict") != "CLEAN":
        failures.append("Model record-ready script must pass the anti-slop classifier as CLEAN")

    machine = require(APPLIED / "02-machine-inspection-video.md", failures)
    contains(machine, ["Re-anchored belief", "qualified reviewer", "cannot promise performance", "Invite handoff"], "Machine", failures)
    machine_spoken = section_between(machine, "## Record-ready script", "## Inputs and owners")
    if classify_prose(machine_spoken).get("verdict") != "CLEAN":
        failures.append("Machine record-ready script must pass the anti-slop classifier as CLEAN")

    invite = require(APPLIED / "03-invite-decision-document.md", failures)
    contains(invite, ["$500 prepaid", "72 hours", "This is not for you if", "No pitch call"], "Invite", failures)
    for forbidden in ("book a call", "calendar link", "schedule a call"):
        if forbidden in invite.lower():
            failures.append(f"Invite contains forbidden pre-sale CTA: {forbidden}")

    close_path = require(APPLIED / "04-zero-call-close-path.md", failures)
    contains(close_path, ["NO EVENT", "SOLD`, not `COLLECTED", "payment route", "No pitch call"], "Close Path", failures)

    try:
        packet = json.loads((APPLIED / "offer-truth-packet.json").read_text(encoding="utf-8"))
        if packet.get("payment", {}).get("route_state") != "PENDING":
            failures.append("Control-Beater payment route must remain PENDING")
        if packet.get("requires_pre_sale_call") is not False:
            failures.append("Control-Beater packet must prohibit pre-sale calls")
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid applied Offer Truth Packet JSON: {exc}")

    readiness = subprocess.run(
        [sys.executable, str(ROOT / "execution/jw_three_asset_readiness.py"), "--self-test"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if readiness.returncode != 0:
        failures.append("readiness self-test failed: " + (readiness.stdout + readiness.stderr).strip())

    routing = subprocess.run(
        [
            sys.executable,
            str(ROOT / "execution/routing_governor.py"),
            "evaluate",
            "Build the Model, Machine, and Invite with no pre-sale calls",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    try:
        routing_result = json.loads(routing.stdout)
    except json.JSONDecodeError:
        routing_result = {}
    if routing.returncode != 0 or routing_result.get("chosen_route") != "jw-three-asset-close":
        failures.append("natural-language no-call routing did not select jw-three-asset-close")

    productized_control = subprocess.run(
        [
            sys.executable,
            str(ROOT / "execution/routing_governor.py"),
            "evaluate",
            "Build a productized AI service OS with no-call intake",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    try:
        productized_result = json.loads(productized_control.stdout)
    except json.JSONDecodeError:
        productized_result = {}
    if productized_result.get("chosen_route") == "jw-three-asset-close":
        failures.append("generic no-call productized-service intent falsely selected jw-three-asset-close")

    if failures:
        print("FAIL: jw-three-asset-close system")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: source package, 12 frames, workflow, 4 prompts, 3 bridges, applied pack, stage integrity, no-call boundary, routing, and negative controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
