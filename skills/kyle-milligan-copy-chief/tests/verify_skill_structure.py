#!/usr/bin/env python3
"""Verify the approved cold Kyle skill surface without registering it."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills/kyle-milligan-copy-chief"
EXPECTED_WORKFLOWS = [
    "01-531-swipe-discipline.md",
    "02-unique-promise-spine.md",
    "03-four-beat-opening-builder.md",
    "04-first-four-lines-audit.md",
    "05-thumbtack-continuity-audit.md",
    "06-proof-texture-dimensionalizer.md",
    "07-mumbo-jumbo-pruner.md",
    "08-negative-space-copy-chief.md",
]
EXPECTED_PROMPTS = [
    "531-swipe-discipline.md",
    "unique-promise-spine.md",
    "four-beat-opening-builder.md",
    "first-four-lines-audit.md",
    "thumbtack-continuity-audit.md",
    "proof-texture-dimensionalizer.md",
    "mumbo-jumbo-pruner.md",
    "negative-space-copy-chief.md",
]
EXPECTED_REFERENCES = {
    "PROVENANCE-2026-08-02.md",
    "source-ledger.md",
    "mechanics-ledger.md",
    "skill-system-contract.md",
    "composition-ledger.md",
    "compatibility-map.md",
}
PROMPT_MAP = {
    workflow: prompt
    for workflow, prompt in zip(EXPECTED_WORKFLOWS, EXPECTED_PROMPTS)
}


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    try:
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError:
        return {}


def main() -> int:
    errors: list[str] = []
    workflow_paths = sorted((SKILL / "workflows").glob("*.md"))
    prompt_paths = sorted((SKILL / "references/prompts-v2").glob("*.md"))
    if sorted(path.name for path in workflow_paths) != sorted(EXPECTED_WORKFLOWS):
        errors.append("workflow inventory must be the exact approved eight")
    if sorted(path.name for path in prompt_paths) != sorted(EXPECTED_PROMPTS):
        errors.append("born-v2 prompt inventory must be the exact approved eight")
    if (SKILL / "AGENT.md").exists() or (SKILL / "agents").exists():
        errors.append("persona/agent manifest is forbidden by the approved architecture")

    skill_text = (SKILL / "SKILL.md").read_text()
    skill_fm = frontmatter(skill_text)
    if skill_fm.get("name") != "kyle-milligan-copy-chief":
        errors.append("SKILL name drifted")
    if skill_fm.get("routing") != "long-tail" or skill_fm.get("status") != "cold-pre-verification":
        errors.append("skill must remain cold and long-tail")
    if skill_fm.get("workflows") != 8:
        errors.append("SKILL frontmatter must declare eight workflows")
    for required in ("## Domain", "## When to Use", "## When NOT to Use", "One Failure, One Owner"):
        if required not in skill_text:
            errors.append(f"SKILL router is missing {required}")
    if "Never run all eight automatically" not in skill_text:
        errors.append("SKILL router lacks the no-all-eight invariant")
    if "A-tier is impossible" not in skill_text:
        errors.append("SKILL router lacks the A-tier proof boundary")
    if "/four-punches" in skill_text:
        errors.append("SKILL router must not expose a /four-punches command")

    ledger_rows = {
        json.loads(line)["row_id"]: json.loads(line)
        for line in (ROOT / "extractions/kyle-milligan-copywriting/speaker-ledger.jsonl").read_text().splitlines()
    }
    required_sections = (
        "## Input Required",
        "## Hard Stop / Refusal",
        "## Procedure",
        "## Output Contract",
        "## Quality Gate",
        "## Handoff",
        "## Execution Prompt",
    )
    for path in workflow_paths:
        text = path.read_text()
        fm = frontmatter(text)
        for section in required_sections:
            if section not in text:
                errors.append(f"{path.name}: missing {section}")
        expected_prompt = PROMPT_MAP[path.name]
        if fm.get("prompt") != f"references/prompts-v2/{expected_prompt}":
            errors.append(f"{path.name}: frontmatter prompt pointer drifted")
        if f"../references/prompts-v2/{expected_prompt}" not in text:
            errors.append(f"{path.name}: body prompt pointer drifted")
        exemption = str(fm.get("menu_exempt", ""))
        if path.name.startswith(("05-", "07-")):
            if "permanently internal" not in exemption:
                errors.append(f"{path.name}: permanent internal exemption missing")
        elif "pending detached behavior proof" not in exemption:
            errors.append(f"{path.name}: pending-proof exemption missing")
        source_rows = [item.strip() for item in str(fm.get("source_rows", "")).split(",") if item.strip()]
        if not source_rows:
            errors.append(f"{path.name}: source_rows missing")
        for row_id in source_rows:
            row = ledger_rows.get(row_id)
            if not row:
                errors.append(f"{path.name}: unknown source row {row_id}")
            elif row.get("truth_class") != "OBSERVED":
                errors.append(f"{path.name}: non-observed row {row_id} cannot ground procedure")

    for path in prompt_paths:
        text = path.read_text()
        fm = frontmatter(text)
        if fm.get("source_prompt") != "born-v2" or fm.get("standard") != "structure-pure-v2" or fm.get("forged") != "born-v2":
            errors.append(f"{path.name}: born-v2 frontmatter drifted")
        for section in (
            "## Role & Activation",
            "## Input Required",
            "## Execution Protocol",
            "## Output Contract",
            "## Output Skeleton",
            "## Quality Gate",
            "## Creative Latitude",
            "## Deploy When",
        ):
            if section not in text:
                errors.append(f"{path.name}: missing {section}")

    reference_names = {path.name for path in (SKILL / "references").iterdir() if path.is_file()}
    if reference_names != EXPECTED_REFERENCES:
        errors.append(f"reference inventory drifted: {sorted(reference_names ^ EXPECTED_REFERENCES)}")

    genius = (SKILL / "genius.md").read_text()
    pattern_numbers = set(int(value) for value in re.findall(r"^### ([0-9]+)\. ", genius, re.M))
    hidden_section = genius.split("## 11 Hidden-Knowledge Items", 1)[1].split("## Source-Derived Anti-Patterns", 1)[0]
    hidden_numbers = set(int(value) for value in re.findall(r"^### ([0-9]+)\. ", hidden_section, re.M))
    if pattern_numbers < set(range(1, 19)):
        errors.append("genius.md must contain numbered patterns 1–18")
    if hidden_numbers != set(range(1, 12)):
        errors.append("genius.md must contain exactly eleven numbered hidden-knowledge items")
    if genius.count("Source: `SL-") < 11 or genius.count("\n> “") < 3:
        errors.append("genius.md source anti-patterns or verbatim calibration fragments are incomplete")
    if "## Anti-Exemplar" not in genius or genius.count("### 1.") < 2:
        errors.append("genius.md exemplar/anti-exemplar surface is incomplete")

    for verifier in (
        "verify_source_ledger.py",
        "verify_relaynote_fixture.py",
        "verify_skill_structure.py",
        "verify_behavior_run.py",
    ):
        if not (SKILL / "tests" / verifier).is_file():
            errors.append(f"skill-local verifier missing: {verifier}")

    public_surfaces = [
        *(ROOT / ".agent/workflows").glob("kyle-*.md"),
        *(ROOT / ".claude/commands").glob("kyle-*.md"),
    ]
    if public_surfaces:
        errors.append(f"pre-proof public Kyle routes exist: {[str(path.relative_to(ROOT)) for path in public_surfaces]}")

    if errors:
        print("KYLE SKILL STRUCTURE: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("KYLE SKILL STRUCTURE: PASS")
    print("- router: cold, long-tail, one-failure/one-owner")
    print("- implementation: 8 workflows + 8 same-deliverable born-v2 prompts")
    print("- menu policy: 6 pending proof + 2 permanently internal")
    print("- source grounding: all procedure anchors resolve to OBSERVED atomic rows")
    print("- public routes: 0 before behavior proof")
    print("- tier boundary: B at most; A requires two real Kyle pieces + Farrice blind verdict")
    return 0


if __name__ == "__main__":
    sys.exit(main())
