#!/usr/bin/env python3
"""Verify Signal Fidelity SHADOW behavior, restraint, and owner wiring."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from signal_fidelity_shadow import evaluate


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "semantic_libraries/antigravity/primitives/signal-fidelity-shadow-contract.md"
SOURCE = ROOT / "extractions/video-context/1KOdiGgMtpY"
FIXTURES = ROOT / "execution/fixtures/signal-fidelity-shadow"

OWNER_MARKERS = {
    ROOT / "semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md": (
        "## Signal Fidelity Capture (SHADOW)",
        "signal-fidelity-shadow-contract.md",
        "optional",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/skill-system-contract.md": (
        "## Signal Fidelity Handoff (SHADOW)",
        "signal-fidelity-shadow-contract.md",
        "optional",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md": (
        "## Recipient Playback (SHADOW)",
        "signal-fidelity-shadow-contract.md",
        "optional",
    ),
}

REQUIRED_SOURCE_FILES = (
    "metadata.json",
    "transcript.vtt",
    "transcript.txt",
    "transcript_segments.json",
    "video-context-ledger.md",
    "video-context-ledger.json",
    "uncertainty-report.md",
    "analysis.md",
    "signal-fidelity-build-contract.md",
    "behavior-proof.md",
)

FORBIDDEN_SURFACES = (
    ROOT / ".agent/workflows/signal-fidelity.md",
    ROOT / ".agent/workflows/signal-fidelity-shadow.md",
    ROOT / ".agents/skills/source-command-signal-fidelity",
    ROOT / "skills/signal-fidelity",
    ROOT / "agents/signal-fidelity",
)


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def codes(report: dict) -> set[str]:
    return {item["code"] for item in report["distortion_hypotheses"]}


def classes(report: dict) -> set[str]:
    return {item["class"] for item in report["distortion_hypotheses"]}


def main() -> int:
    failures: list[str] = []

    if not PRIMITIVE.exists():
        failures.append("missing Signal Fidelity primitive")
    else:
        text = PRIMITIVE.read_text(encoding="utf-8")
        for marker in (
            "Status: `SHADOW`",
            "## Three Distortion Checks",
            "## Recipient Playback",
            "## Deliberate Evolution",
            "## SHADOW Rules",
            "Production behavior, recipient comprehension improvement, workflow burden, and trust effect: `UNTESTED`",
        ):
            if marker not in text:
                failures.append(f"primitive missing marker: {marker}")
        for banned in ("Status: `ENFORCED`", "mandatory score", "HARD BLOCK"):
            if banned in text:
                failures.append(f"primitive contains enforcement marker: {banned}")

    for path, markers in OWNER_MARKERS.items():
        if not path.exists():
            failures.append(f"missing owner file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"owner wiring missing in {path.relative_to(ROOT)}: {marker}")

    for filename in REQUIRED_SOURCE_FILES:
        path = SOURCE / filename
        if not path.exists() or path.stat().st_size == 0:
            failures.append(f"missing or empty source artifact: {path.relative_to(ROOT)}")

    for path in FORBIDDEN_SURFACES:
        if path.exists():
            failures.append(f"forbidden hot or competing surface exists: {path.relative_to(ROOT)}")

    hooks = ROOT / ".codex/hooks.json"
    if hooks.exists() and "signal_fidelity" in hooks.read_text(encoding="utf-8"):
        failures.append("Signal Fidelity was wired into Codex hooks")
    slash_commands = ROOT / "SLASH_COMMANDS.md"
    if slash_commands.exists() and "/signal-fidelity" in slash_commands.read_text(encoding="utf-8"):
        failures.append("Signal Fidelity was promoted into slash commands")

    preserved = evaluate(load_fixture("preserved.json"))
    if preserved["decision"] != "CLEAR" or preserved["distortion_hypotheses"]:
        failures.append("preserved fixture did not return CLEAR")

    source = evaluate(load_fixture("source-distortion.json"))
    if "source_distortion" not in classes(source) or "signal_field_missing" not in codes(source):
        failures.append("source-distortion fixture did not detect missing source signal")

    handoff = evaluate(load_fixture("handoff-distortion.json"))
    if "handoff_distortion" not in classes(handoff) or "playback_gap" not in classes(handoff):
        failures.append("handoff-distortion fixture did not detect artifact and playback loss")

    machine = evaluate(load_fixture("machine-distortion.json"))
    required_machine_codes = {
        "limit_missing_from_artifact",
        "proof_state_changed",
        "recipient_did_not_recover_marker",
    }
    if not required_machine_codes.issubset(codes(machine)):
        failures.append("machine-distortion fixture missed limit, proof, or playback loss")

    adaptation = evaluate(load_fixture("intentional-adaptation.json"))
    if adaptation["decision"] != "REVIEW":
        failures.append("intentional adaptation should remain REVIEW, not CLEAR or blocked")
    if any(item["field"] == "consultant-frame" for item in adaptation["distortion_hypotheses"]):
        failures.append("owner-approved adaptation was incorrectly called distortion")
    if not any(item["field"] == "consultant-frame" for item in adaptation["approved_changes"]):
        failures.append("owner-approved adaptation was not preserved in the report")

    for report_name, report in (
        ("preserved", preserved),
        ("source", source),
        ("handoff", handoff),
        ("machine", machine),
        ("adaptation", adaptation),
    ):
        if report.get("enforcement") is not False or report.get("can_block") is not False:
            failures.append(f"{report_name} report claims enforcement or blocking authority")

    for fixture in FIXTURES.glob("*.json"):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "execution/signal_fidelity_shadow.py"), str(fixture), "--format", "json"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if completed.returncode != 0:
            failures.append(f"valid review fixture blocked execution: {fixture.name} exit={completed.returncode}")

    if failures:
        print("Signal Fidelity SHADOW: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Signal Fidelity SHADOW: PASS")
    print("- source package: present and bounded")
    print("- owner integrations: 3 optional pointer-level references")
    print("- positive control: preserved signal returns CLEAR")
    print("- negative controls: source, handoff, machine, proof-state, and playback gaps detected")
    print("- restraint control: owner-approved adaptation remains REVIEW and is not called distortion")
    print("- enforcement: none; valid packets exit 0")
    print("- hot surfaces: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
