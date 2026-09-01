#!/usr/bin/env python3
"""Verify the bounded, recipient-native Signal Fidelity contract."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "semantic_libraries/antigravity/primitives/signal-fidelity-minimal-contract.md"
SKILL_SYSTEM = ROOT / "semantic_libraries/antigravity/primitives/skill-system-contract.md"
AGENTIC = ROOT / "semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md"
FIXTURE = ROOT / "execution/fixtures/signal-fidelity-minimal/recipient-modes.json"

AI_FIELDS = {"Goal", "Must survive", "Constraints", "Proof state", "Owner", "Stop when"}
STRATEGY_FIELDS = {"Decision", "Must not lose", "Proof boundary"}


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def validate_recipient_modes(fixture: dict) -> list[str]:
    failures: list[str] = []
    cases = {case["recipient"]: case for case in fixture.get("cases", [])}
    require(set(cases) == {"public_reader", "human_collaborator", "ai_agent", "strategy_owner"},
            "fixture must contain exactly four recipient modes", failures)

    for recipient in ("public_reader", "human_collaborator"):
        case = cases.get(recipient, {})
        require(case.get("mode") == "native_only", f"{recipient} must remain native-only", failures)
        require(case.get("signal_fidelity_visible") is False,
                f"{recipient} must not see Signal Fidelity", failures)
        require(case.get("native") == case.get("presented"),
                f"{recipient} output must remain unchanged", failures)

    ai_case = cases.get("ai_agent", {})
    require(ai_case.get("mode") == "explicit_execution_capsule",
            "AI agent must receive the explicit execution capsule", failures)
    require(set(ai_case.get("fields", {})) == AI_FIELDS,
            "AI capsule must use exactly the six bounded fields", failures)

    strategy_case = cases.get("strategy_owner", {})
    require(strategy_case.get("mode") == "optional_decision_spine",
            "strategy mode must remain optional", failures)
    require(set(strategy_case.get("fields", {})) == STRATEGY_FIELDS,
            "strategy spine must use exactly three fields", failures)
    return failures


def sabotage_controls(fixture: dict) -> list[str]:
    failures: list[str] = []
    cases = {case["recipient"]: case for case in fixture["cases"]}

    visible_human = deepcopy(fixture)
    human = next(case for case in visible_human["cases"] if case["recipient"] == "human_collaborator")
    human["presented"] += " Signal Fidelity receipt: complete."
    require(bool(validate_recipient_modes(visible_human)),
            "negative control failed: visible human receipt was accepted", failures)

    incomplete_ai = deepcopy(fixture)
    ai = next(case for case in incomplete_ai["cases"] if case["recipient"] == "ai_agent")
    ai["fields"].pop("Constraints")
    require(bool(validate_recipient_modes(incomplete_ai)),
            "negative control failed: incomplete AI capsule was accepted", failures)

    expanded_strategy = deepcopy(fixture)
    strategy = next(case for case in expanded_strategy["cases"] if case["recipient"] == "strategy_owner")
    strategy["fields"]["Why this route"] = "Extra framework surface"
    require(bool(validate_recipient_modes(expanded_strategy)),
            "negative control failed: expanded strategy receipt was accepted", failures)

    require(len(cases) == 4, "negative controls require all four cases", failures)
    return failures


def main() -> int:
    failures: list[str] = []

    for path in (CONTRACT, SKILL_SYSTEM, AGENTIC, FIXTURE):
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}", failures)
    if failures:
        return finish(failures)

    contract = CONTRACT.read_text(encoding="utf-8")
    skill_system = SKILL_SYSTEM.read_text(encoding="utf-8")
    agentic = AGENTIC.read_text(encoding="utf-8")
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    for marker in (
        "silent loss detector",
        "If the native owner already carries the meaning",
        "This is the only routine visible Signal Fidelity surface",
        "Give the collaborator the natural handoff",
        "Give the reader the native content unchanged",
        "No material loss means no Signal Fidelity output",
        "broad prototype on `codex/signal-fidelity-shadow` is parked",
    ):
        require(marker in contract, f"contract missing boundary: {marker}", failures)

    pointer = "signal-fidelity-minimal-contract.md"
    require(pointer in skill_system, "Skill System owner pointer missing", failures)
    require(pointer in agentic, "Agentic Engineering owner pointer missing", failures)

    failures.extend(validate_recipient_modes(fixture))
    failures.extend(sabotage_controls(fixture))

    activation_surfaces = [
        ROOT / ".agent/workflows",
        ROOT / "skills",
        ROOT / ".codex",
        ROOT / "execution/hooks",
    ]
    for surface in activation_surfaces:
        if not surface.exists():
            continue
        for path in surface.rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            require(pointer not in text,
                    f"forbidden activation pointer: {path.relative_to(ROOT)}", failures)

    for registry in ("SLASH_COMMANDS.md", "DOMAIN_REGISTRY.md", "PRODUCTION_CORE.md"):
        path = ROOT / registry
        if path.exists():
            require(pointer not in path.read_text(encoding="utf-8"),
                    f"forbidden registry pointer: {registry}", failures)

    return finish(failures)


def finish(failures: list[str]) -> int:
    if failures:
        print("Signal Fidelity minimal: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Signal Fidelity minimal: PASS")
    print("- public reader: native content unchanged")
    print("- human collaborator: natural handoff only")
    print("- AI agent: six-field execution capsule")
    print("- strategy owner: optional three-line decision spine")
    print("- activation surfaces: none")
    print("- negative controls: visible human receipt, incomplete AI capsule, and expanded strategy receipt rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
