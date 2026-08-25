#!/usr/bin/env python3
"""Deterministic cold-start checks for the Oren funnel-flywheel extension."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SKILL = ROOT / "skills" / "oren-one-person-ai-marketer"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def text(path: Path) -> str:
    require(path.is_file(), f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    fixture = json.loads(text(HERE / "validation-fixtures.json"))
    skill_text = text(SKILL / "SKILL.md")
    prompt_corpus = ""

    for index, command in enumerate(fixture["required_commands"], start=13):
        workflow = text(SKILL / "workflows" / f"{index:02d}-{command.removeprefix('oren-')}.md")
        wrapper = text(ROOT / ".agent" / "workflows" / f"{command}.md")
        require(f"/{command}" in skill_text, f"command absent from skill menu: /{command}")
        require(f"workflows/{index:02d}-{command.removeprefix('oren-')}.md" in wrapper, f"wrapper not wired: /{command}")
        require("Quality Gate" in workflow, f"quality gate missing: /{command}")

    for prompt in fixture["required_prompts"]:
        prompt_text = text(SKILL / "references" / "prompts-v2" / prompt)
        prompt_corpus += "\n" + prompt_text
        for marker in ("source_prompt: born-v2", "Role & Activation", "Execution Protocol", "Output Contract", "Quality Gate"):
            require(marker in prompt_text, f"{marker} missing in prompt: {prompt}")

    paid = text(HERE / fixture["commercial_case"])
    neutral = text(HERE / fixture["neutral_case"])
    both = paid + "\n" + neutral
    for section in fixture["standard_outputs"]:
        require(section in both, f"standard output not represented: {section}")

    require("sent 0 / held 0 / sold 0 / collected $0" in paid, "commercial zero state drifted")
    require("50% deposit" in paid, "deposit gate missing")
    require("bookings separately from held calls and deposits" in paid, "booking/revenue separation missing")
    require("five business days" in paid.lower(), "delivery boundary missing")
    require("strategy and scripts only" in paid.lower(), "scope boundary missing")
    require("monthly offer remains locked" in paid.lower(), "monthly evidence gate missing")
    require("ECONOMICS: UNPROVEN" in paid, "paid case invents or omits economics state")

    neutral_lower = neutral.lower()
    for forbidden in ("sports nutrition", "paid social", "framer", "farrice"):
        require(forbidden not in neutral_lower, f"neutral portability leak: {forbidden}")
    require("ECONOMICS: UNPROVEN" in neutral, "neutral case invents or omits economics state")
    require("no message is sent and no record is created" in neutral_lower, "neutral permission veto missing")

    workflow_corpus = "\n".join(
        text(SKILL / "workflows" / f"{number:02d}-{slug}.md")
        for number, slug in (
            (13, "funnel-flywheel"),
            (14, "funnel-route"),
            (15, "capture-to-call"),
            (16, "offer-ladder"),
            (17, "funnel-test-loop"),
        )
    )
    for owner in ("Stockton", "Benoit", "copy owner", "/oren-referral-engine", "/funnel-hack", "/oren-content-flywheel"):
        require(owner in workflow_corpus, f"bounded owner handoff missing: {owner}")
    require("ECONOMICS: UNPROVEN" in workflow_corpus, "economics veto missing from workflows")
    require("full vsl" in workflow_corpus.lower(), "full-VSL handoff boundary missing")
    require("ROAS" in workflow_corpus and "Benoit" in workflow_corpus, "paid-media diagnosis handoff missing")
    require("Framer" not in prompt_corpus, "sponsored tool became a prompt dependency")
    require("Framer" not in workflow_corpus or "optional implementation example" in workflow_corpus, "sponsored tool became a workflow dependency")

    print("PASS: 5 commands, 6 prompts, 2 cold-start proofs, economics/permission/owner boundaries")


if __name__ == "__main__":
    main()
