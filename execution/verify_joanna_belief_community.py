#!/usr/bin/env python3
"""Verify the Joanna Wiebe belief-community extension and its negative controls."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from verify_video_context_source_package import verify_package


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "extractions/video-context/Tnv9PuMo84E/source-package.md",
    "extractions/video-context/Tnv9PuMo84E/deep-extraction.md",
    "extractions/video-context/Tnv9PuMo84E/research-claim-audit.md",
    "extractions/video-context/Tnv9PuMo84E/uncertainty-report.md",
    "extractions/video-context/Tnv9PuMo84E/skill-system-contract.md",
    "extractions/video-context/Tnv9PuMo84E/behavior-proof.md",
    "skills/joanna-wiebe-persuasion-mastery/references/belief-community-architecture.md",
    "skills/joanna-wiebe-persuasion-mastery/workflows/belief-community-architecture.md",
    "skills/joanna-wiebe-persuasion-mastery/workflows/worldview-contrast-system.md",
    "skills/joanna-wiebe-persuasion-mastery/workflows/participation-language-system.md",
    "skills/joanna-wiebe-persuasion-mastery/workflows/earned-conviction-deployment.md",
    "skills/joanna-wiebe-persuasion-mastery/references/prompts-v2/belief-community-system.md",
    "skills/joanna-wiebe-persuasion-mastery/references/prompts-v2/worldview-contrast-system.md",
    "skills/joanna-wiebe-persuasion-mastery/references/prompts-v2/participation-language-system.md",
    "skills/joanna-wiebe-persuasion-mastery/references/prompts-v2/earned-conviction-deployment.md",
    ".agent/workflows/belief-community-architecture.md",
    ".agent/workflows/joanna-wiebe.md",
    ".agent/workflows/worldview-contrast-system.md",
    ".agent/workflows/participation-language-system.md",
    ".agent/workflows/earned-conviction-deployment.md",
    ".claude/commands/belief-community-architecture.md",
    ".claude/commands/joanna-wiebe.md",
    ".claude/commands/worldview-contrast-system.md",
    ".claude/commands/participation-language-system.md",
    ".claude/commands/earned-conviction-deployment.md",
    ".agents/skills/source-command-belief-community-architecture/SKILL.md",
    ".agents/skills/source-command-joanna-wiebe/SKILL.md",
    ".agents/skills/source-command-worldview-contrast-system/SKILL.md",
    ".agents/skills/source-command-participation-language-system/SKILL.md",
    ".agents/skills/source-command-earned-conviction-deployment/SKILL.md",
)

PROMPTS = tuple(path for path in REQUIRED_FILES if "/prompts-v2/" in path)
WORKFLOWS = tuple(
    path for path in REQUIRED_FILES if path.startswith("skills/") and "/workflows/" in path
)
PROMPT_SECTIONS = (
    "## Role & Activation",
    "## Input Required",
    "## Execution Protocol",
    "## Output Contract",
    "## Output Skeleton",
    "## Quality Gate",
    "## Creative Latitude",
    "## Deploy When",
)
CHAIN = (
    "lens",
    "devil",
    "symbol",
    "ritual",
    "language",
    "conviction",
)
ALLOWED_ENEMY_KINDS = {"behavior", "belief", "status_quo", "institution"}
FORBIDDEN_RUNTIME_PATHS = (
    "skills/belief-community-architecture",
    "agents/belief-community-architecture",
)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def audit_candidate(candidate: dict[str, object]) -> list[str]:
    failures: list[str] = []
    for layer in CHAIN:
        if not str(candidate.get(layer, "")).strip():
            failures.append(f"missing layer: {layer}")

    enemy_kind = str(candidate.get("enemy_kind", ""))
    if enemy_kind not in ALLOWED_ENEMY_KINDS:
        failures.append(f"unsafe enemy kind: {enemy_kind or 'missing'}")

    if not str(candidate.get("protected_boundary", "")).strip():
        failures.append("missing protected boundary")

    ritual = candidate.get("ritual_safeguards")
    required_safeguards = {"voluntary", "useful", "reversible", "proportionate", "easy_exit"}
    supplied = set(ritual) if isinstance(ritual, list) else set()
    missing = sorted(required_safeguards - supplied)
    if missing:
        failures.append("ritual safeguards missing: " + ", ".join(missing))

    forbidden = {
        "humiliation",
        "pain",
        "collateral",
        "secret initiation",
        "exit penalty",
        "exploitative lock-in",
    }
    text = " ".join(str(value) for value in candidate.values()).lower()
    detected = sorted(term for term in forbidden if term in text)
    if detected:
        failures.append("coercive ritual detected: " + ", ".join(detected))

    evidence_state = str(candidate.get("evidence_state", ""))
    if candidate.get("certainty_claim") is True and evidence_state not in {"VERIFIED", "LIKELY"}:
        failures.append(f"unearned certainty: {evidence_state or 'missing'}")

    if not str(candidate.get("disconfirming_condition", "")).strip():
        failures.append("missing disconfirming condition")
    return failures


def run_controls(failures: list[str], notes: list[str]) -> None:
    positive = {
        "lens": "Safer content makes the evidence state visible.",
        "devil": "Confidence theater.",
        "enemy_kind": "behavior",
        "protected_boundary": "People and groups are not targets.",
        "symbol": "VERIFIED / LIKELY / UNCONFIRMED strip.",
        "ritual": "Proof Pass with a claim ledger.",
        "ritual_safeguards": ["voluntary", "useful", "reversible", "proportionate", "easy_exit"],
        "language": "proof-bounded; confidence theater; no-event",
        "conviction": "The proof and the sentence should agree.",
        "evidence_state": "UNTESTED",
        "certainty_claim": False,
        "disconfirming_condition": "Revise if adoption evidence contradicts the thesis.",
    }
    positive_failures = audit_candidate(positive)
    if positive_failures:
        failures.append("positive control failed: " + "; ".join(positive_failures))
    else:
        notes.append("positive control accepted a complete proof-bounded system")

    negative_controls = {
        "human_enemy": ({**positive, "enemy_kind": "person"}, "unsafe enemy kind"),
        "coercive_ritual": (
            {
                **positive,
                "ritual": "Secret initiation with collateral and an exit penalty.",
                "ritual_safeguards": ["useful"],
            },
            "coercive ritual detected",
        ),
        "unearned_certainty": (
            {**positive, "evidence_state": "UNCONFIRMED", "certainty_claim": True},
            "unearned certainty",
        ),
        "missing_language": ({**positive, "language": ""}, "missing layer: language"),
    }
    for name, (candidate, expected) in negative_controls.items():
        result = audit_candidate(candidate)
        if not any(expected in item for item in result):
            failures.append(f"negative control {name} did not detect {expected!r}: {result}")
        else:
            notes.append(f"negative control rejected {name}")


def verify() -> tuple[bool, list[str], list[str]]:
    failures: list[str] = []
    notes: list[str] = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing file: {relative}")
        elif path.stat().st_size == 0:
            failures.append(f"empty file: {relative}")

    if failures:
        return False, failures, notes

    source_ok, source_failures, source_notes = verify_package(
        ROOT / "extractions/video-context/Tnv9PuMo84E"
    )
    if not source_ok:
        failures.extend(f"source package: {item}" for item in source_failures)
    else:
        notes.append("source package passed transcript and provenance verification")
        notes.extend(f"source package: {item}" for item in source_notes)

    skill = read("skills/joanna-wiebe-persuasion-mastery/SKILL.md")
    for term in (
        "Belief Community Architecture",
        "Worldview Contrast System",
        "Participation and Language System",
        "Earned Conviction Deployment",
    ):
        if term not in skill:
            failures.append(f"skill missing route: {term}")

    for relative in WORKFLOWS:
        content = read(relative)
        for term in ("Input Required", "Output Contract", "Quality Gate"):
            if term not in content:
                failures.append(f"{relative} missing {term}")

    for relative in PROMPTS:
        content = read(relative)
        for term in ("source_prompt: born-v2", "forged: born-v2", *PROMPT_SECTIONS):
            if term not in content:
                failures.append(f"{relative} missing {term}")

    behavior = read("extractions/video-context/Tnv9PuMo84E/behavior-proof.md")
    for term in (
        "Baseline output",
        "Workflow-applied output",
        "Behavior delta",
        "UNTESTED",
        "NO EVENT",
        "confidence theater",
    ):
        if term not in behavior:
            failures.append(f"behavior proof missing term: {term}")

    contract = read("extractions/video-context/Tnv9PuMo84E/skill-system-contract.md")
    for term in (
        "Erica Mallet",
        "/category-building-os",
        "No standalone",
        "Runtime posture",
    ):
        if term not in contract:
            failures.append(f"skill-system contract missing term: {term}")

    front_door = read(".agent/workflows/joanna-wiebe.md")
    for term in (
        "Adaptive Joanna",
        "Full Joanna Deployment",
        "joanna-wiebe-persuasion-mastery",
        "joanna-wiebe-writing-careers",
        "capabilities used",
        "capabilities parked",
    ):
        if term not in front_door:
            failures.append(f"Joanna front door missing term: {term}")

    for relative in FORBIDDEN_RUNTIME_PATHS:
        if (ROOT / relative).exists():
            failures.append(f"forbidden duplicate runtime exists: {relative}")

    run_controls(failures, notes)
    return not failures, failures, notes


def main() -> int:
    ok, failures, notes = verify()
    payload = {"status": "PASS" if ok else "FAIL", "failures": failures, "notes": notes}
    if "--json" in sys.argv:
        print(json.dumps(payload, indent=2))
    else:
        print(f"JOANNA BELIEF COMMUNITY: {payload['status']}")
        for note in notes:
            print(f"  PASS: {note}")
        for failure in failures:
            print(f"  FAIL: {failure}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
