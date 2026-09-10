#!/usr/bin/env python3
"""Verify the recorded human blind reveal and precommitted verdict application."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "extractions/video-context/1KOdiGgMtpY/validation/real-work-pilot-v1"


def main() -> int:
    failures: list[str] = []
    local = json.loads((PILOT / "local-results.json").read_text(encoding="utf-8"))
    human = json.loads((PILOT / "human-blind-result.json").read_text(encoding="utf-8"))
    application = (PILOT / "decision-card-application.md").read_text(encoding="utf-8")
    verdict = (PILOT / "final-provisional-verdict.md").read_text(encoding="utf-8")

    labels = {
        case["case"]: case["label_reveal"]
        for case in local["cases"]
    }
    if any(mapping != {"treatment": "A", "baseline": "B"} for mapping in labels.values()):
        failures.append("recorded A/B reveal does not match the sealed local results")

    submitted = human.get("submitted_verdict", {})
    expected = {
        "strategy": "A",
        "content": "B",
        "handoff_human": "B",
        "handoff_ai_agent": "A",
        "burden": "B",
    }
    if submitted != expected:
        failures.append("human blind response does not match the submitted verdict")

    interpreted = human.get("interpreted_results", {})
    if interpreted.get("strategy") != "treatment_win":
        failures.append("strategy arm was not revealed as treatment")
    if interpreted.get("content") != "baseline_win":
        failures.append("content arm was not revealed as baseline")
    if interpreted.get("handoff") != "recipient_split":
        failures.append("handoff recipient split was not preserved")
    if interpreted.get("burden") != "baseline_win":
        failures.append("burden preference was not preserved")

    for marker in (
        "## KEEP COLD SHADOW\n\nVerdict: `FAIL`.",
        "## REMOVE\n\nVerdict: `FAIL`.",
        "## CHANGE SHADOW\n\nVerdict: `PASS`.",
        "## Required Bounded Repair",
        "## Replay Contract",
    ):
        if marker not in application:
            failures.append(f"decision-card application missing marker: {marker}")

    if "`CHANGE SHADOW`" not in verdict:
        failures.append("final provisional verdict is not CHANGE SHADOW")
    if "General `BLIND_PREFERRED`: not earned" not in verdict:
        failures.append("general blind preference boundary is missing")
    if "Promotion or enforcement: not authorized" not in verdict:
        failures.append("promotion boundary is missing")

    if failures:
        print("Signal Fidelity human verdict: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Signal Fidelity human verdict: PASS")
    print("- reveal: A=treatment, B=baseline")
    print("- independent result: strategy treatment; content baseline; handoff recipient split; burden baseline")
    print("- precommitted application: KEEP fail, REMOVE fail, CHANGE SHADOW pass")
    print("- promotion and enforcement: not authorized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
