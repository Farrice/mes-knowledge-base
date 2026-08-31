#!/usr/bin/env python3
"""Verify the workspace-only Burnout-Safe Output SHADOW pilot."""

from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "execution" / "fixtures" / "burnout_safe_output"
CONTRACT_PATH = FIXTURE_DIR / "contract-v0.1.md"
CASES_PATH = FIXTURE_DIR / "cases.json"
SABOTAGE_PATH = FIXTURE_DIR / "sabotage.json"
HUMAN_GATE_PATH = FIXTURE_DIR / "human-behavior-gate.json"
CODEX_PATH = ROOT / "CODEX.md"

PROOF_STATES = {
    "VERIFIED",
    "LIKELY",
    "UNCONFIRMED",
    "UNTESTED",
    "NO EVENT",
    "CONFLICT",
}
CONTEXT_LEVELS = {"GREEN", "AMBER", "RED"}
PRIORITIES = {
    "Protect outcome",
    "Close consequential gap",
    "Compound without derailing",
}
RECOMMENDATION_FIELDS = (
    "title",
    "priority",
    "why_now",
    "operator_insight",
    "hidden_gap",
    "capability",
    "prompt",
    "expected_output",
    "quality_bar",
    "skip_if",
)
RATING_FIELDS = (
    "understood_and_actionable",
    "no_decode_burden",
    "top_rank_correct",
    "equal_recommendation_depth",
    "depth_preserved",
    "preferred_variant",
    "notes",
)
EXPECTED_CATEGORIES = {
    "tiny-answer",
    "correction",
    "mechanical-confirmation",
    "major-decision",
    "artifact-delivery",
    "system-audit",
    "proof-unconfirmed",
    "no-event",
    "authority-conflict",
    "routine-refinement",
    "strategic-candidate",
    "superseded-artifact",
    "context-green",
    "context-amber",
    "context-red",
    "existing-task-first",
    "rank-close-gap-first",
    "rank-compound-first",
}
CARD_ORDER = (
    "VERDICT",
    "STATE",
    "WHY IT MATTERS",
    "PROOF",
    "WHAT CHANGED",
    "USE THIS",
    "CONTEXT HEALTH",
    "NEXT ACTION",
    "NEED FROM YOU",
)
FORBIDDEN_CHANGED_PATHS = (
    "AGENTS.md",
    "CLAUDE.md",
    ".codex/hooks.json",
    "directives/constitution/shared-blocks.md",
    "execution/contextual_next_prompts.py",
)
FORBIDDEN_CHANGED_PREFIXES = (
    "execution/hooks/",
    ".agent/workflows/",
    "skills/",
)


class CheckFailure(AssertionError):
    """A deterministic pilot check failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def load_json(path: Path) -> dict[str, Any]:
    require(path.exists(), f"missing file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise CheckFailure(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def words(value: Any) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", str(value)))


def nonempty(value: Any, label: str) -> str:
    text = str(value or "").strip()
    require(bool(text), f"{label} is empty; empty rows must be omitted")
    return text


def card_rows(card: dict[str, Any]) -> list[tuple[str, str]]:
    state = card.get("state") or {}
    proof = card.get("proof") or {}
    health = card.get("context_health") or {}
    action = card.get("next_action") or {}
    rows: list[tuple[str, str]] = [
        ("VERDICT", nonempty(card.get("verdict"), "VERDICT")),
        (
            f"STATE — {nonempty(state.get('tag'), 'STATE tag')}",
            nonempty(state.get("text"), "STATE text"),
        ),
        ("WHY IT MATTERS", nonempty(card.get("why_it_matters"), "WHY IT MATTERS")),
        (
            f"PROOF — {nonempty(proof.get('state'), 'PROOF state')}",
            nonempty(proof.get("text"), "PROOF text"),
        ),
    ]
    optional = (
        ("WHAT CHANGED", "what_changed"),
        ("USE THIS", "use_this"),
    )
    for label, key in optional:
        if key in card:
            rows.append((label, nonempty(card.get(key), label)))
    rows.extend(
        [
            (
                f"CONTEXT HEALTH — {nonempty(health.get('level'), 'CONTEXT HEALTH level')}",
                nonempty(health.get("text"), "CONTEXT HEALTH text"),
            ),
            (
                f"NEXT ACTION — {nonempty(action.get('owner'), 'NEXT ACTION owner')}",
                nonempty(action.get("text"), "NEXT ACTION text"),
            ),
        ]
    )
    if "need_from_you" in card:
        rows.append(("NEED FROM YOU", nonempty(card.get("need_from_you"), "NEED FROM YOU")))
    return rows


def render_case(case: dict[str, Any]) -> str:
    parts = [nonempty(case.get("body"), f"{case.get('id')} body")]
    card = case.get("card")
    if isinstance(card, dict):
        parts.append("\n".join(f"**{label}:** {value}" for label, value in card_rows(card)))
    recommendations = case.get("recommendations") or []
    if recommendations:
        lines = ["## 3 Next Prompts"]
        for index, item in enumerate(recommendations, 1):
            lines.extend(
                [
                    f"{index}. **{item['title']}** — {item['why_now']}",
                    f"   **Prompt:** \"{item['prompt']}\"",
                    f"   **Expected output:** {item['expected_output']}",
                    f"   **Quality bar:** {item['quality_bar']}",
                    f"   **Skip if:** {item['skip_if']}",
                ]
            )
        parts.append("\n".join(lines))
    return "\n\n".join(parts)


def card_label_key(label: str) -> str:
    for prefix in ("STATE", "PROOF", "CONTEXT HEALTH", "NEXT ACTION"):
        if label.startswith(prefix + " —"):
            return prefix
    return label


def validate_rendered_card(case: dict[str, Any], rendered: str) -> None:
    card_surface = rendered.split("## 3 Next Prompts", 1)[0]
    card_lines = [
        match.groups()
        for line in card_surface.splitlines()
        if (match := re.match(r"^\*\*(.+?):\*\*\s*(.*)$", line.strip()))
    ]
    if case.get("card") is None:
        require(not card_lines, f"{case['id']} overfires a Command Card on a tiny turn")
        return
    require(card_lines, f"{case['id']} material event is missing a Command Card")
    keys = [card_label_key(label) for label, _ in card_lines]
    require(len(keys) == len(set(keys)), f"{case['id']} repeats a Command Card row")
    expected = [key for key in CARD_ORDER if key in keys]
    require(keys == expected, f"{case['id']} Command Card labels are out of order: {keys}")
    require("PROOF" in keys, f"{case['id']} proof is mandatory")
    for label, value in card_lines:
        require(bool(value.strip()), f"{case['id']} has an empty rendered row: {label}")


def validate_recommendations(case: dict[str, Any]) -> None:
    recommendations = case.get("recommendations") or []
    needs_three = bool(case.get("real_next_decision"))
    require(
        len(recommendations) == (3 if needs_three else 0),
        f"{case['id']} expected {'three' if needs_three else 'no'} recommendations, got {len(recommendations)}",
    )
    if not recommendations:
        require("expected_rank" not in case, f"{case['id']} has a rank without recommendations")
        return

    ranks = [str(item.get("priority") or "") for item in recommendations]
    require(ranks == case.get("expected_rank"), f"{case['id']} ranking does not match live context")
    require(set(ranks).issubset(PRIORITIES), f"{case['id']} has an unknown priority basis")

    depth_counts: list[int] = []
    for index, item in enumerate(recommendations, 1):
        label = f"{case['id']} recommendation {index}"
        for field in RECOMMENDATION_FIELDS:
            nonempty(item.get(field), f"{label} {field}")
        title = str(item["title"]).strip().lower()
        require(title not in {"use now", "harden", "expand"}, f"{label} uses a canned visible title")
        require(words(item["title"]) >= 4, f"{label} title is too generic")
        require(words(item["operator_insight"]) >= 8, f"{label} has shallow Operator Insight")
        require(words(item["hidden_gap"]) >= 7, f"{label} has shallow Hidden Gap")
        require(words(item["capability"]) >= 7, f"{label} has shallow Capability")
        require(words(item["expected_output"]) >= 7, f"{label} has shallow expected output")
        require(words(item["quality_bar"]) >= 7, f"{label} has shallow quality bar")
        require(words(item["skip_if"]) >= 6, f"{label} has shallow skip condition")
        prompt = str(item["prompt"]).strip().lower()
        generic = (
            "continue the strongest next step",
            "do the next step",
            "keep going",
            "continue working",
        )
        require(not any(value in prompt for value in generic), f"{label} has a generic prompt")
        depth_counts.append(sum(words(item[field]) for field in RECOMMENDATION_FIELDS[2:]))

    require(min(depth_counts) >= 65, f"{case['id']} recommendations fall below the intelligence floor")
    require(
        min(depth_counts) / max(depth_counts) >= 0.55,
        f"{case['id']} recommendation depth collapses after rank one: {depth_counts}",
    )


def validate_context_and_authority(case: dict[str, Any], rendered: str) -> None:
    card = case.get("card")
    if not isinstance(card, dict):
        return
    proof = card.get("proof") or {}
    proof_state = str(proof.get("state") or "")
    require(proof_state in PROOF_STATES, f"{case['id']} has invalid proof state: {proof_state}")
    health = card.get("context_health") or {}
    level = str(health.get("level") or "")
    require(level in CONTEXT_LEVELS, f"{case['id']} has invalid context health: {level}")
    lowered = rendered.lower()

    if proof_state == "CONFLICT":
        require("use_this" not in card, f"{case['id']} guesses authority while proof is CONFLICT")
    if case["category"] == "authority-conflict":
        require(proof_state == "CONFLICT", f"{case['id']} hides an authority conflict")
        require(level == "RED", f"{case['id']} authority conflict must be RED")
    if case["category"] == "proof-unconfirmed":
        require(proof_state == "UNCONFIRMED", f"{case['id']} overstates unconfirmed authority")
    if case["category"] == "no-event":
        require(proof_state == "NO EVENT", f"{case['id']} turns missing commercial evidence into activity")
    if case["category"] == "superseded-artifact":
        use_this = str(card.get("use_this") or "").lower()
        require("current" in use_this, f"{case['id']} fails to name the current artifact")
        require("superseded" not in use_this, f"{case['id']} promotes a superseded artifact")
    if case["category"] == "routine-refinement":
        require(proof_state == "VERIFIED", f"{case['id']} auto-promotes without verified continuity")
        require("use_this" in card, f"{case['id']} routine refinement lacks current authority")
    if case["category"] == "strategic-candidate":
        require(
            (card.get("state") or {}).get("tag") == "PENDING APPROVAL",
            f"{case['id']} silently promotes a strategic change",
        )
        require("need_from_you" in card, f"{case['id']} strategic candidate lacks owner approval")

    if level == "AMBER":
        require("checkpoint" in lowered, f"{case['id']} AMBER lacks an in-task checkpoint")
        require("create a new task now" not in lowered, f"{case['id']} AMBER creates a new task")
        require("opened a new task" not in lowered, f"{case['id']} AMBER created a new task")
        require("pause all work" not in lowered, f"{case['id']} AMBER interrupts safe work")
    if level == "RED":
        require("preserve" in lowered, f"{case['id']} RED fails to preserve current state")
        require("pause" in lowered, f"{case['id']} RED fails to pause the conflicting action")
        require(
            "split" in lowered or "separate" in lowered,
            f"{case['id']} RED fails to recommend a split",
        )
        require("created a new task" not in lowered, f"{case['id']} RED auto-created a task")
        require("opened a new task" not in lowered, f"{case['id']} RED auto-created a task")
    if case["category"] == "existing-task-first":
        require("existing task" in lowered, f"{case['id']} loses the existing-task-first rule")
        require("created five checkpoint files" not in lowered, f"{case['id']} creates checkpoint sprawl")
        require("opened a new task" not in lowered, f"{case['id']} creates task sprawl")


def validate_case(case: dict[str, Any], rendered_override: str | None = None) -> str:
    for field in ("id", "category", "prompt", "material_event", "real_next_decision", "body"):
        require(field in case, f"fixture missing {field}")
    require(case["category"] in EXPECTED_CATEGORIES, f"{case['id']} has unknown category")
    require(words(case["body"]) <= 45, f"{case['id']} opening body exceeds the compact topline")
    if case["material_event"]:
        require(isinstance(case.get("card"), dict), f"{case['id']} material event lacks a card")
    else:
        require(case.get("card") is None, f"{case['id']} overfires a card on a tiny turn")
        require(not case.get("recommendations"), f"{case['id']} overfires recommendations on a tiny turn")

    rendered = rendered_override if rendered_override is not None else render_case(case)
    validate_rendered_card(case, rendered)
    validate_context_and_authority(case, rendered)
    validate_recommendations(case)
    if case.get("card"):
        card_text = rendered.split("## 3 Next Prompts", 1)[0]
        require(words(card_text) <= 185, f"{case['id']} Command Card exceeds the 30-second surface")
    return rendered


def validate_contract() -> list[str]:
    require(CONTRACT_PATH.exists(), "pilot contract is missing")
    contract = CONTRACT_PATH.read_text(encoding="utf-8")
    codex = CODEX_PATH.read_text(encoding="utf-8")
    required_contract = (
        "PILOT / SHADOW",
        "fixed; empty rows are omitted",
        "is mandatory whenever the card appears",
        "Protect the outcome",
        "Close the consequential gap",
        "Compound without derailing",
        "Ranking changes priority, not depth",
        "GREEN",
        "AMBER",
        "RED",
        "one living task per coherent outcome",
        "Preservation Lock",
        "go deeper",
        "show proof",
        "technical detail",
        "HUMAN GATE PENDING",
        "No merge, global activation, hook change",
    )
    normalized = re.sub(r"\s+", " ", contract)
    for phrase in required_contract:
        require(phrase.lower() in normalized.lower(), f"contract missing: {phrase}")
    require(codex.count("## Burnout-Safe Output Pilot (SHADOW v0.1)") == 1, "CODEX pilot pointer missing or duplicated")
    require(str(CONTRACT_PATH.relative_to(ROOT)) in codex, "CODEX pilot pointer does not name the contract")
    require("does not replace" in codex, "CODEX pilot pointer does not preserve existing owners")
    return ["pilot contract", "single CODEX pointer", "promotion boundary"]


def validate_changed_surface() -> list[str]:
    proc = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    require(proc.returncode == 0, f"git status failed: {proc.stderr.strip()}")
    changed: list[str] = []
    for line in proc.stdout.splitlines():
        raw = line[3:].strip()
        path = raw.split(" -> ")[-1]
        changed.append(path)
    for path in changed:
        require(path not in FORBIDDEN_CHANGED_PATHS, f"forbidden pilot change: {path}")
        require(
            not any(path.startswith(prefix) for prefix in FORBIDDEN_CHANGED_PREFIXES),
            f"forbidden pilot change: {path}",
        )
    return changed


def validate_corpus(corpus: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    expected_count = int(corpus.get("required_fixture_count") or 0)
    cases = corpus.get("cases") or []
    require(expected_count == 18, "fixture contract must require 18 cases")
    require(len(cases) == expected_count, f"expected 18 fixtures, found {len(cases)}")
    ids = [case.get("id") for case in cases]
    require(len(ids) == len(set(ids)), "fixture IDs are duplicated")
    categories = {str(case.get("category") or "") for case in cases}
    require(categories == EXPECTED_CATEGORIES, f"fixture category coverage drift: {sorted(categories)}")
    for case in cases:
        validate_case(case)
    return cases, [f"{len(cases)}/{expected_count} fixtures", f"{len(categories)} categories"]


def validate_human_gate_schema(human: dict[str, Any], cases_by_id: dict[str, dict[str, Any]]) -> str:
    require("status" not in human, "human behavior status must be computed, not stored")
    examples = human.get("examples") or []
    required_count = int(human.get("required_example_count") or 0)
    require(required_count == 5, "human gate must require five examples")
    require(len(examples) == required_count, f"human gate expected five examples, found {len(examples)}")
    require(len({item.get("task_type") for item in examples}) >= 3, "human gate needs at least three task types")
    require(len({item.get("id") for item in examples}) == len(examples), "human example IDs are duplicated")

    pending = False
    failed = False
    pilot_preferences = 0
    for item in examples:
        case_id = str(item.get("pilot_case_id") or "")
        require(case_id in cases_by_id, f"human example references unknown fixture: {case_id}")
        require(item.get("pilot_position") in {"X", "Y"}, f"{item.get('id')} has invalid pilot position")
        nonempty(item.get("control_response"), f"{item.get('id')} control response")
        ratings = item.get("ratings") or {}
        require(tuple(ratings.keys()) == RATING_FIELDS, f"{item.get('id')} rating fields drifted")
        for field in RATING_FIELDS[:5]:
            value = ratings.get(field)
            require(value in {True, False, None}, f"{item.get('id')} {field} must be true, false, or null")
            pending = pending or value is None
            failed = failed or value is False
        preference = ratings.get("preferred_variant")
        require(preference in {"X", "Y", "TIE", None}, f"{item.get('id')} has invalid preference")
        pending = pending or preference is None
        if preference is not None:
            control_position = "Y" if item["pilot_position"] == "X" else "X"
            failed = failed or preference == control_position
            pilot_preferences += int(preference == item["pilot_position"])
    if pending:
        return "HUMAN GATE PENDING"
    if failed or pilot_preferences < 1:
        return "BEHAVIOR REFINEMENT REQUIRED"
    return "BEHAVIOR PASS"


def mutate_case(case: dict[str, Any], mutation: str, source: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], str | None]:
    rendered_override: str | None = None
    card = case.get("card")
    if mutation == "remove_proof":
        assert isinstance(card, dict)
        card.pop("proof", None)
    elif mutation == "invalid_proof_state":
        assert isinstance(card, dict)
        card["proof"]["state"] = "PROBABLY"
    elif mutation == "empty_verdict":
        assert isinstance(card, dict)
        card["verdict"] = ""
    elif mutation == "reorder_card_labels":
        rendered = render_case(case)
        lines = rendered.splitlines()
        verdict_index = next(index for index, line in enumerate(lines) if line.startswith("**VERDICT:"))
        state_index = next(index for index, line in enumerate(lines) if line.startswith("**STATE —"))
        lines[verdict_index], lines[state_index] = lines[state_index], lines[verdict_index]
        rendered_override = "\n".join(lines)
    elif mutation == "add_empty_need":
        assert isinstance(card, dict)
        card["need_from_you"] = ""
    elif mutation == "card_on_tiny_turn":
        case["card"] = copy.deepcopy(source["BSO-004"]["card"])
    elif mutation == "remove_material_card":
        case["card"] = None
    elif mutation == "conflict_with_use_this":
        assert isinstance(card, dict)
        card["use_this"] = "The newest-looking file."
    elif mutation == "select_superseded_authority":
        assert isinstance(card, dict)
        card["use_this"] = "The superseded AI-boom offer."
    elif mutation == "amber_creates_task":
        assert isinstance(card, dict)
        card["next_action"]["text"] = "Create a new task now for the tangent."
    elif mutation == "amber_pauses_work":
        assert isinstance(card, dict)
        card["next_action"]["text"] = "Pause all work until the tangent is resolved."
    elif mutation == "red_continues_work":
        case["body"] = "The objective changed, but continue overwriting the current files."
        assert isinstance(card, dict)
        card["verdict"] = "Continue the replacement."
        card["why_it_matters"] = "Moving faster matters more than preserving the old objective."
        card["proof"]["text"] = "The objectives differ."
        card["what_changed"] = "The new product replaces the old objective."
        card["context_health"]["text"] = "Continue despite the conflict."
        card["next_action"]["text"] = "Overwrite the current files."
        card["need_from_you"] = "Confirm after the overwrite."
    elif mutation == "red_auto_creates_task":
        assert isinstance(card, dict)
        card["next_action"]["text"] = "Opened a new task and moved the product work there."
    elif mutation == "fixed_visible_title":
        case["recommendations"][0]["title"] = "Use Now"
    elif mutation == "generic_prompt":
        case["recommendations"][0]["prompt"] = "Continue the strongest next step."
    elif mutation == "remove_operator_insight":
        case["recommendations"][0]["operator_insight"] = ""
    elif mutation == "remove_hidden_gap":
        case["recommendations"][0]["hidden_gap"] = ""
    elif mutation == "remove_capability":
        case["recommendations"][0]["capability"] = ""
    elif mutation == "remove_quality_bar":
        case["recommendations"][0]["quality_bar"] = ""
    elif mutation == "remove_skip_condition":
        case["recommendations"][0]["skip_if"] = ""
    elif mutation == "wrong_rank_order":
        case["recommendations"][0], case["recommendations"][1] = (
            case["recommendations"][1],
            case["recommendations"][0],
        )
    elif mutation == "collapse_third_recommendation":
        for field in RECOMMENDATION_FIELDS[2:]:
            case["recommendations"][2][field] = "Too shallow."
    elif mutation == "existing_task_sprawl":
        assert isinstance(card, dict)
        card["what_changed"] = "Opened a new task and created five checkpoint files."
    else:
        raise CheckFailure(f"unknown sabotage mutation: {mutation}")
    return case, rendered_override


def run_sabotage(
    sabotage: dict[str, Any],
    cases_by_id: dict[str, dict[str, Any]],
    human: dict[str, Any],
) -> list[str]:
    items = sabotage.get("cases") or []
    required_count = int(sabotage.get("required_sabotage_count") or 0)
    require(required_count == 24, "sabotage contract must require 24 cases")
    require(len(items) == required_count, f"expected 24 sabotage cases, found {len(items)}")
    require(len({item.get("id") for item in items}) == len(items), "sabotage IDs are duplicated")
    caught: list[str] = []
    for item in items:
        mutation = str(item.get("mutation") or "")
        try:
            if item.get("target") == "HUMAN_GATE":
                mutated_human = copy.deepcopy(human)
                if mutation == "stored_behavior_pass":
                    mutated_human["status"] = "BEHAVIOR PASS"
                validate_human_gate_schema(mutated_human, cases_by_id)
            else:
                target = str(item.get("target") or "")
                require(target in cases_by_id, f"sabotage target missing: {target}")
                mutated, rendered_override = mutate_case(
                    copy.deepcopy(cases_by_id[target]), mutation, cases_by_id
                )
                validate_case(mutated, rendered_override=rendered_override)
        except (CheckFailure, AssertionError, KeyError, TypeError, ValueError):
            caught.append(str(item["id"]))
        else:
            raise CheckFailure(f"sabotage escaped: {item['id']} {mutation}")
    return caught


def print_human_review(human: dict[str, Any], cases_by_id: dict[str, dict[str, Any]]) -> None:
    print(human_review_markdown(human, cases_by_id))


def human_review_markdown(human: dict[str, Any], cases_by_id: dict[str, dict[str, Any]]) -> str:
    lines = [
        "# Burnout-Safe Output v0.1 — Human Behavior Gate",
        "",
        "Status: **HUMAN GATE PENDING**",
        "",
        "Review the variants without inspecting the implementation files first. For each example, choose `X`, `Y`, or `TIE`, then answer the five yes/no questions in the rating sheet.",
        "",
        "The pilot passes only when every required judgment is yes, no control variant is preferred, and at least one comparison prefers the pilot. Missing ratings never become an inferred pass.",
        "",
    ]
    for item in human["examples"]:
        pilot = render_case(cases_by_id[item["pilot_case_id"]])
        control = item["control_response"]
        variants = {item["pilot_position"]: pilot}
        variants["Y" if item["pilot_position"] == "X" else "X"] = control
        lines.extend(
            [
                f"## {item['id']} — {item['task_type']}",
                "",
                f"**Prompt:** {item['prompt']}",
                "",
                "### Variant X",
                "",
                variants["X"],
                "",
                "### Variant Y",
                "",
                variants["Y"],
                "",
            ]
        )
    lines.extend(
        [
            "## Rating Sheet",
            "",
            "For each row, record `Preferred = X/Y/TIE` and `Yes/No` for the five judgments.",
            "",
            "| Example | Preferred | Actionable in 30 seconds? | No decoding burden? | Top rank correct? | Recommendations equally intelligent? | Depth preserved? | Notes |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for item in human["examples"]:
        lines.append(f"| {item['id']} |  |  |  |  |  |  |  |")
    lines.extend(
        [
            "",
            "Reply with the five completed rows. Codex will record the ratings, recompute the gate, and repair only the lowest failing criterion if needed.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-behavior", action="store_true", help="Fail until the human gate passes.")
    parser.add_argument("--human-review", action="store_true", help="Print the five blind review examples.")
    parser.add_argument(
        "--human-review-output",
        help="Write the five blind review examples to a workspace-local Markdown artifact.",
    )
    parser.add_argument("--json", action="store_true", help="Print the computed status as JSON.")
    args = parser.parse_args()

    try:
        contract_checks = validate_contract()
        changed = validate_changed_surface()
        corpus = load_json(CASES_PATH)
        cases, corpus_checks = validate_corpus(corpus)
        cases_by_id = {case["id"]: case for case in cases}
        human = load_json(HUMAN_GATE_PATH)
        behavior_status = validate_human_gate_schema(human, cases_by_id)
        sabotage = load_json(SABOTAGE_PATH)
        caught = run_sabotage(sabotage, cases_by_id, human)
    except Exception as exc:  # noqa: BLE001 - one concise verifier surface.
        print("BURNOUT-SAFE OUTPUT SHADOW PILOT")
        print("STRUCTURAL FAIL")
        print(f"- {exc}")
        return 1

    result = {
        "pilot": "Burnout-Safe Output v0.1",
        "scope": "workspace branch only",
        "structural_status": "PASS",
        "behavior_status": behavior_status,
        "fixtures": len(cases),
        "sabotage_caught": len(caught),
        "changed_paths": changed,
        "promotion_status": "BLOCKED pending explicit approval",
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("BURNOUT-SAFE OUTPUT SHADOW PILOT")
        print("STRUCTURAL PASS")
        print(behavior_status)
        print(f"- checks: {', '.join(contract_checks + corpus_checks)}")
        print(f"- sabotage: {len(caught)}/24 caught")
        print(f"- changed paths: {len(changed)}; forbidden surfaces: 0")
        print("- MERGE / GLOBAL / HOOK PROMOTION BLOCKED pending separate approval")
    if args.human_review:
        print()
        print_human_review(human, cases_by_id)
    if args.human_review_output:
        output_path = (ROOT / args.human_review_output).resolve()
        require(ROOT.resolve() in output_path.parents, "human review output must stay inside the workspace")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(human_review_markdown(human, cases_by_id), encoding="utf-8")
        print(f"- human review artifact: {output_path.relative_to(ROOT)}")
    if args.require_behavior and behavior_status != "BEHAVIOR PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
