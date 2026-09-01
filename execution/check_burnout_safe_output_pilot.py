#!/usr/bin/env python3
"""Verify the workspace-only Artifact Comprehension SHADOW pilot."""

from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "execution" / "fixtures" / "burnout_safe_output"
V01_CONTRACT = FIXTURE_DIR / "contract-v0.1.md"
V01_HUMAN = FIXTURE_DIR / "human-behavior-gate.json"
V02_CONTRACT = FIXTURE_DIR / "artifact-comprehension-contract-v0.2.md"
V02_CASES = FIXTURE_DIR / "artifact-cases-v0.2.json"
V02_SABOTAGE = FIXTURE_DIR / "artifact-sabotage-v0.2.json"
SURFACE_CASES = FIXTURE_DIR / "surface-selection-cases-v0.2.json"
SURFACE_SABOTAGE = FIXTURE_DIR / "surface-selection-sabotage-v0.2.json"
V02_HUMAN_HISTORY = FIXTURE_DIR / "artifact-human-gate-v0.2.json"
V021_HUMAN_HISTORY = FIXTURE_DIR / "artifact-human-gate-v0.2.1.json"
V02_HUMAN = FIXTURE_DIR / "artifact-human-gate-v0.2.2.json"
CODEX_PATH = ROOT / "CODEX.md"

ALLOWED_SURFACES = {"native_artifact", "markdown", "visual_brief"}
ALLOWED_REPRESENTATIONS = {
    "summary", "prose", "evidence", "decision", "playbook", "timeline",
    "flow", "stats", "bars", "matrix", "caveats",
}
EXPECTED_SHAPES = {
    "decision", "comparison", "chronology", "evidence", "metrics",
    "implementation", "nuance", "tiny",
}
HUMAN_RATING_FIELDS = ("preferred_variant", "notes")
EXPECTED_SURFACES = {
    "immediate_answer": "conversation",
    "finished_reusable_prose": "writing_block",
    "durable_knowledge": "native_artifact",
    "dependent_execution": "native_artifact",
    "quantitative_data": "spreadsheet",
    "presentation_story": "slides",
    "live_interactive_state": "briefing_room",
    "visual_concept": "generated_visual",
}
FORBIDDEN_CHANGED_PATHS = {
    "AGENTS.md", "CLAUDE.md", ".codex/hooks.json",
    "directives/constitution/shared-blocks.md",
    "execution/contextual_next_prompts.py", "execution/render_brief.py",
}
FORBIDDEN_CHANGED_PREFIXES = ("execution/hooks/", ".agent/workflows/", "skills/")


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
    require(bool(text), f"{label} is empty")
    return text


def validate_contracts() -> list[str]:
    v01 = V01_CONTRACT.read_text(encoding="utf-8")
    v02 = V02_CONTRACT.read_text(encoding="utf-8")
    codex = CODEX_PATH.read_text(encoding="utf-8")
    v01_normalized = re.sub(r"\s+", " ", v01)
    v02_normalized = re.sub(r"\s+", " ", v02)
    for phrase in (
        "BEHAVIOR REFINEMENT REQUIRED", "SUPERSEDED FOR ACTIVE TESTING",
        "historical regression evidence only", str(V02_CONTRACT.relative_to(ROOT)),
    ):
        require(phrase.lower() in v01_normalized.lower(), f"v0.1 history label missing: {phrase}")
    for phrase in (
        "PILOT / SHADOW / BEHAVIOR PASS",
        "does not govern ordinary conversation or closeouts",
        "smallest sufficient representation wins", "Plain prose is not a failure",
        "Intelligent Surface Selection", "A writing block is not a decorative box",
        "Surface selection remains SHADOW",
        "Three Contextual Next Prompts", "No merge, global activation, hook change",
    ):
        require(phrase.lower() in v02_normalized.lower(), f"v0.2 contract missing: {phrase}")
    require(
        codex.count("## Artifact Comprehension Pilot (SHADOW v0.2)") == 1,
        "CODEX v0.2 pointer missing or duplicated",
    )
    require(str(V02_CONTRACT.relative_to(ROOT)) in codex, "CODEX does not name v0.2 contract")
    require("defer entirely" in codex, "CODEX does not defer to successful global behavior")
    require("Do not create a new renderer" in codex, "CODEX does not freeze new system creation")
    require("## Burnout-Safe Output Pilot (SHADOW v0.1)" not in codex, "v0.1 remains active in CODEX")
    return ["v0.1 superseded", "v0.2 artifact-only", "global behavior frozen"]


def changed_paths() -> list[str]:
    base = subprocess.run(
        ["git", "merge-base", "HEAD", "main"], cwd=ROOT, text=True,
        capture_output=True, check=False,
    )
    require(base.returncode == 0, f"git merge-base failed: {base.stderr.strip()}")
    diff = subprocess.run(
        ["git", "diff", "--name-only", base.stdout.strip()], cwd=ROOT,
        text=True, capture_output=True, check=False,
    )
    require(diff.returncode == 0, f"git diff failed: {diff.stderr.strip()}")
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=ROOT, text=True,
        capture_output=True, check=False,
    )
    require(status.returncode == 0, f"git status failed: {status.stderr.strip()}")
    paths = {line.strip() for line in diff.stdout.splitlines() if line.strip()}
    for line in status.stdout.splitlines():
        raw = line[3:].strip().split(" -> ")[-1]
        if raw:
            paths.add(raw)
    for path in paths:
        require(path not in FORBIDDEN_CHANGED_PATHS, f"forbidden pilot change: {path}")
        require(
            not any(path.startswith(prefix) for prefix in FORBIDDEN_CHANGED_PREFIXES),
            f"forbidden pilot change: {path}",
        )
    return sorted(paths)


def validate_v01_human_verdict(human: dict[str, Any]) -> str:
    require(human.get("revision_required") is True, "v0.1 qualitative veto is not recorded")
    nonempty(human.get("revision_reason"), "v0.1 revision reason")
    require(len(human.get("examples") or []) == 5, "v0.1 must retain five reviewed examples")
    pilot_preferences = ties = control_preferences = 0
    for item in human["examples"]:
        preference = (item.get("ratings") or {}).get("preferred_variant")
        require(preference in {"X", "Y", "TIE"}, f"{item.get('id')} preference is missing")
        if preference == "TIE":
            ties += 1
        elif preference == item.get("pilot_position"):
            pilot_preferences += 1
        else:
            control_preferences += 1
    require(
        (pilot_preferences, ties, control_preferences) == (3, 2, 0),
        "v0.1 receipt must remain 3 pilot / 2 tie / 0 control",
    )
    return "BEHAVIOR REFINEMENT REQUIRED"


def validate_v02_round1(human: dict[str, Any]) -> str:
    require(human.get("revision_required") is True, "v0.2 round-one refinement is not recorded")
    nonempty(human.get("revision_reason"), "v0.2 round-one revision reason")
    lock = human.get("preservation_lock") or {}
    require(
        set(lock) == {"keep", "change", "do_not_disturb", "risk", "gate"},
        "v0.2 round one lacks a complete Preservation Lock",
    )
    for key, value in lock.items():
        nonempty(value, f"v0.2 Preservation Lock {key}")
    expected = {"AHG-001": "Y", "AHG-002": "X", "AHG-003": "Y"}
    examples = human.get("examples") or []
    require(len(examples) == 3, "v0.2 round one must retain three examples")
    for item in examples:
        require(
            (item.get("ratings") or {}).get("preferred_variant") == expected.get(item.get("id")),
            f"{item.get('id')} round-one preference drifted",
        )
        nonempty((item.get("ratings") or {}).get("notes"), f"{item.get('id')} round-one note")
    return "BEHAVIOR REFINEMENT REQUIRED"


def validate_v021_round2(human: dict[str, Any]) -> str:
    require(human.get("revision_required") is True, "v0.2.1 refinement is not recorded")
    nonempty(human.get("revision_reason"), "v0.2.1 revision reason")
    lock = human.get("preservation_lock") or {}
    require(
        set(lock) == {"keep", "change", "do_not_disturb", "risk", "gate"},
        "v0.2.1 lacks a complete Preservation Lock",
    )
    for key, value in lock.items():
        nonempty(value, f"v0.2.1 Preservation Lock {key}")
    expected = {"AHG-002R": "Y", "AHG-003R": "X"}
    examples = human.get("examples") or []
    require(len(examples) == 2, "v0.2.1 must retain two examples")
    for item in examples:
        require(
            (item.get("ratings") or {}).get("preferred_variant") == expected.get(item.get("id")),
            f"{item.get('id')} v0.2.1 preference drifted",
        )
        nonempty((item.get("ratings") or {}).get("notes"), f"{item.get('id')} v0.2.1 note")
    return "BEHAVIOR REFINEMENT REQUIRED"


def validate_boundary(boundary: dict[str, Any]) -> None:
    for key in (
        "alters_global_clear_depth", "alters_global_closeout",
        "alters_ordinary_replies", "creates_new_task",
    ):
        require(boundary.get(key) is False, f"frozen boundary violated: {key}")
    require(boundary.get("new_system_components") == [], "pilot invents a new system component")


def validate_case(case: dict[str, Any]) -> None:
    case_id = nonempty(case.get("id"), "fixture id")
    for field in (
        "artifact_type", "information_shape", "decision_job", "surface",
        "why_selection", "detail_preservation", "example",
    ):
        nonempty(case.get(field), f"{case_id} {field}")
    shape = str(case["information_shape"])
    require(shape in EXPECTED_SHAPES, f"{case_id} has unknown information shape: {shape}")
    require(case.get("surface") in ALLOWED_SURFACES, f"{case_id} has an unknown surface")
    require(isinstance(case.get("activate"), bool), f"{case_id} activation must be boolean")
    require(words(case["why_selection"]) >= 12, f"{case_id} does not explain why the representation earns its place")
    require(words(case["detail_preservation"]) >= 10, f"{case_id} does not preserve depth explicitly")
    require(words(case["example"]) >= 8, f"{case_id} example is too thin")

    selected = case.get("selected_representations") or []
    jobs = case.get("representation_jobs") or {}
    require(1 <= len(selected) <= 3, f"{case_id} must use one to three representations")
    require(len(selected) == len(set(selected)), f"{case_id} duplicates a representation")
    require(set(selected).issubset(ALLOWED_REPRESENTATIONS), f"{case_id} invents a representation")
    require(set(jobs) == set(selected), f"{case_id} representation jobs do not match selections")
    normalized_jobs = [nonempty(jobs[item], f"{case_id} {item} job").lower() for item in selected]
    require(len(normalized_jobs) == len(set(normalized_jobs)), f"{case_id} repeats the same information job")

    support = case.get("evidence_support")
    require(support in {"verified", "mixed", "none"}, f"{case_id} has invalid evidence support")
    require(isinstance(case.get("certainty_claim"), bool), f"{case_id} certainty flag must be boolean")
    if case["certainty_claim"]:
        require(support == "verified", f"{case_id} implies certainty beyond its evidence")
    if "bars" in selected:
        require(case.get("has_comparable_metrics") is True, f"{case_id} uses a chart without comparable metrics")

    if shape == "decision":
        require({"summary", "decision"}.issubset(selected), f"{case_id} loses the decision surface")
    elif shape == "comparison":
        require("matrix" in selected, f"{case_id} hides repeated comparison fields in prose")
    elif shape == "chronology":
        require("timeline" in selected, f"{case_id} loses sequence")
    elif shape == "evidence":
        require({"evidence", "caveats"}.issubset(selected), f"{case_id} separates evidence from its caveat")
    elif shape == "metrics":
        require(case.get("has_comparable_metrics") is True, f"{case_id} metrics are not comparable")
        require(bool({"stats", "bars"}.intersection(selected)), f"{case_id} metrics lack a numeric representation")
    elif shape == "implementation":
        require(
            bool({"playbook", "flow"}.intersection(selected)),
            f"{case_id} implementation lacks an executable sequence or decision flow",
        )
    elif shape == "nuance":
        require("prose" in selected, f"{case_id} nuance loses prose")
        require(
            not {"matrix", "timeline", "flow", "stats", "bars"}.intersection(selected),
            f"{case_id} forces a visual onto nuanced prose",
        )
    elif shape == "tiny":
        require(case.get("activate") is False, f"{case_id} overfires on a tiny artifact")
        require(case.get("surface") == "markdown", f"{case_id} gives a tiny artifact a heavy surface")
        require(selected == ["prose"], f"{case_id} gives a tiny artifact unnecessary structure")
    if case.get("surface") == "visual_brief":
        require(case.get("activate") is True, f"{case_id} forces a visual brief without activation")
        require(len(selected) >= 2, f"{case_id} visual brief has no material visual job")
    if case_id == "AC-004":
        example = case["example"].lower()
        require(words(case["example"]) <= 75, "AC-004 loses value-per-word density")
        for phrase in ("no proof", "what it does not prove", "run one paid test", "interest earns another test"):
            require(phrase in example, f"AC-004 loses restored insight: {phrase}")
        for phrase in ("category interest", "payment event"):
            require(phrase not in example, f"AC-004 restores avoidable jargon: {phrase}")
    if case_id == "AC-006":
        example = case["example"].lower()
        require(words(case["example"]) <= 55, "AC-006 loses value-per-word density")
        for phrase in (
            "without touching", "flowchart", "try to break", "human review",
            "needs work", "ask before promotion", "no merge",
        ):
            require(phrase in example, f"AC-006 loses restored insight: {phrase}")
        for phrase in ("negative controls", "artifact-only fixtures", "human artifact ratings", "promotion decision"):
            require(phrase not in example, f"AC-006 restores system jargon: {phrase}")


def validate_corpus(corpus: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    require(corpus.get("schema_version") == "artifact-comprehension/v0.2", "v0.2 corpus schema drift")
    cases = corpus.get("cases") or []
    require(corpus.get("required_fixture_count") == 8, "v0.2 fixture count must remain eight")
    require(len(cases) == 8, f"expected 8 artifact fixtures, found {len(cases)}")
    require(len({case.get("id") for case in cases}) == 8, "artifact fixture IDs are duplicated")
    require({case.get("information_shape") for case in cases} == EXPECTED_SHAPES, "information-shape coverage drift")
    validate_boundary(corpus.get("frozen_boundaries") or {})
    for case in cases:
        validate_case(case)
    return cases, corpus["frozen_boundaries"]


def validate_surface_case(case: dict[str, Any]) -> None:
    case_id = nonempty(case.get("id"), "surface case id")
    shape = nonempty(case.get("content_shape"), f"{case_id} content shape")
    for field in ("user_job", "primary_surface", "supporting_representation", "why", "avoid"):
        nonempty(case.get(field), f"{case_id} {field}")
    require(shape in EXPECTED_SURFACES, f"{case_id} has unknown content shape: {shape}")
    require(
        isinstance(case.get("primary_surface"), str),
        f"{case_id} must choose exactly one primary surface",
    )
    require(
        case["primary_surface"] == EXPECTED_SURFACES[shape],
        f"{case_id} chose {case['primary_surface']} for {shape}",
    )
    require(words(case["why"]) >= 10, f"{case_id} surface rationale is too shallow")
    require(words(case["avoid"]) >= 8, f"{case_id} lacks a useful overuse boundary")
    lowered = f"{case['why']} {case['avoid']}".lower()
    if shape == "finished_reusable_prose":
        for phrase in ("explanations", "plans", "code"):
            require(phrase in lowered, f"{case_id} writing-block boundary misses {phrase}")
    elif shape == "dependent_execution":
        for phrase in ("branch", "loop", "gate", "state change"):
            require(phrase in lowered, f"{case_id} flow boundary misses {phrase}")
    elif shape == "quantitative_data":
        require("real" in lowered, f"{case_id} spreadsheet lacks a real-data boundary")
    elif shape == "presentation_story":
        require("internal memo" in lowered, f"{case_id} slides lack an overuse boundary")
    elif shape == "live_interactive_state":
        require("static" in lowered, f"{case_id} live surface lacks a static-document boundary")
    elif shape == "visual_concept":
        require("decorative" in lowered, f"{case_id} visual generation lacks a decoration boundary")


def validate_surface_corpus(corpus: dict[str, Any]) -> list[dict[str, Any]]:
    require(corpus.get("schema_version") == "artifact-surface-selection/v0.2", "surface corpus schema drift")
    cases = corpus.get("cases") or []
    require(corpus.get("required_case_count") == 8, "surface corpus must remain eight cases")
    require(len(cases) == 8, f"expected 8 surface cases, found {len(cases)}")
    require(len({case.get("id") for case in cases}) == 8, "surface case IDs are duplicated")
    require({case.get("content_shape") for case in cases} == set(EXPECTED_SURFACES), "surface coverage drift")
    for case in cases:
        validate_surface_case(case)
    return cases


def validate_human_gate(human: dict[str, Any], cases_by_id: dict[str, dict[str, Any]]) -> str:
    require("status" not in human, "v0.2 human status must be computed")
    examples = human.get("examples") or []
    require(
        human.get("schema_version") == "artifact-comprehension-human-gate/v0.2.2",
        "targeted human gate schema drift",
    )
    require(human.get("required_example_count") == 1, "final human gate must remain one example")
    require(len(examples) == 1, f"expected 1 final human example, found {len(examples)}")
    require(
        {item.get("task_type") for item in examples} == {"implementation"},
        "human task coverage drift",
    )
    pending = failed = False
    for item in examples:
        case_id = str(item.get("pilot_case_id") or "")
        require(case_id in cases_by_id, f"human example references unknown fixture: {case_id}")
        require(item.get("pilot_position") in {"X", "Y"}, f"{item.get('id')} has invalid pilot position")
        nonempty(item.get("control_response"), f"{item.get('id')} control")
        ratings = item.get("ratings") or {}
        require(tuple(ratings.keys()) == HUMAN_RATING_FIELDS, f"{item.get('id')} rating fields drifted")
        preference = ratings.get("preferred_variant")
        require(preference in {"X", "Y", "TIE", None}, f"{item.get('id')} preference is invalid")
        pending = pending or preference is None
        if preference is not None:
            control = "Y" if item["pilot_position"] == "X" else "X"
            failed = failed or preference == control
            require(
                bool(str(ratings.get("notes") or "").strip()),
                f"{item.get('id')} needs a note explaining whether the representation earned its place",
            )
    if pending:
        return "HUMAN GATE PENDING"
    if failed:
        return "BEHAVIOR REFINEMENT REQUIRED"
    return "BEHAVIOR PASS"


def mutate_case(case: dict[str, Any], mutation: str) -> dict[str, Any]:
    if mutation == "text_wall":
        case["selected_representations"] = []
        case["representation_jobs"] = {}
    elif mutation == "force_matrix_on_nuance":
        case["selected_representations"].append("matrix")
        case["representation_jobs"]["matrix"] = "Flatten the argument into equal boxes."
    elif mutation == "decorative_chart_without_metrics":
        case["selected_representations"].append("bars")
        case["representation_jobs"]["bars"] = "Decorate the page with a chart."
        case["has_comparable_metrics"] = False
    elif mutation == "force_visual_brief_on_tiny":
        case["surface"] = "visual_brief"
    elif mutation == "duplicate_representation_job":
        keys = list(case["representation_jobs"])
        case["representation_jobs"][keys[1]] = case["representation_jobs"][keys[0]]
    elif mutation == "drop_material_caveat":
        case["selected_representations"].remove("caveats")
        case["representation_jobs"].pop("caveats")
    elif mutation == "imply_unsupported_certainty":
        case["certainty_claim"] = True
    elif mutation == "drop_restored_insight":
        case["example"] = "Category interest is supported, but willingness to pay remains untested. Continue with a paid test."
    elif mutation == "restore_system_jargon":
        case["example"] += " Run negative controls on artifact-only fixtures before the promotion decision."
    elif mutation == "flatten_dependency_flow":
        case["example"] = "# Pilot Path\n\n1. Protect what works.\n2. Test one format.\n3. Review it.\n4. Ask before promotion.\n\nStop before merge."
    else:
        raise CheckFailure(f"unknown case mutation: {mutation}")
    return case


def mutate_boundary(boundary: dict[str, Any], mutation: str) -> dict[str, Any]:
    if mutation == "invent_new_renderer":
        boundary["new_system_components"] = ["artifact-diversification-renderer"]
    elif mutation == "change_global_closeout":
        boundary["alters_global_closeout"] = True
    elif mutation == "create_new_task":
        boundary["creates_new_task"] = True
    else:
        raise CheckFailure(f"unknown boundary mutation: {mutation}")
    return boundary


def run_sabotage(
    sabotage: dict[str, Any], cases_by_id: dict[str, dict[str, Any]], boundary: dict[str, Any]
) -> list[str]:
    items = sabotage.get("cases") or []
    require(sabotage.get("required_sabotage_count") == 13, "sabotage count must remain thirteen")
    require(len(items) == 13, f"expected 13 sabotage cases, found {len(items)}")
    require(len({item.get("id") for item in items}) == 13, "sabotage IDs are duplicated")
    caught: list[str] = []
    for item in items:
        try:
            if item.get("target") == "BOUNDARY":
                validate_boundary(mutate_boundary(copy.deepcopy(boundary), str(item.get("mutation"))))
            else:
                target = str(item.get("target") or "")
                require(target in cases_by_id, f"sabotage target missing: {target}")
                validate_case(mutate_case(copy.deepcopy(cases_by_id[target]), str(item.get("mutation"))))
        except (CheckFailure, KeyError, TypeError, ValueError):
            caught.append(str(item.get("id")))
        else:
            raise CheckFailure(f"sabotage escaped: {item.get('id')} {item.get('mutation')}")
    return caught


def mutate_surface_case(case: dict[str, Any], mutation: str) -> dict[str, Any]:
    if mutation == "box_ordinary_reply":
        case["primary_surface"] = "writing_block"
    elif mutation == "dashboard_static_document":
        case["primary_surface"] = "briefing_room"
    elif mutation == "spreadsheet_without_data":
        case["primary_surface"] = "spreadsheet"
    elif mutation == "slides_for_internal_plan":
        case["primary_surface"] = "slides"
    elif mutation == "image_replaces_reasoning":
        case["primary_surface"] = "generated_visual"
    elif mutation == "multiple_primary_surfaces":
        case["primary_surface"] = ["writing_block", "native_artifact"]
    else:
        raise CheckFailure(f"unknown surface mutation: {mutation}")
    return case


def run_surface_sabotage(
    sabotage: dict[str, Any], cases_by_id: dict[str, dict[str, Any]]
) -> list[str]:
    items = sabotage.get("cases") or []
    require(sabotage.get("required_sabotage_count") == 6, "surface sabotage count must remain six")
    require(len(items) == 6, f"expected 6 surface sabotage cases, found {len(items)}")
    require(len({item.get("id") for item in items}) == 6, "surface sabotage IDs are duplicated")
    caught: list[str] = []
    for item in items:
        target = str(item.get("target") or "")
        require(target in cases_by_id, f"surface sabotage target missing: {target}")
        try:
            validate_surface_case(
                mutate_surface_case(copy.deepcopy(cases_by_id[target]), str(item.get("mutation")))
            )
        except (CheckFailure, KeyError, TypeError, ValueError):
            caught.append(str(item.get("id")))
        else:
            raise CheckFailure(f"surface sabotage escaped: {item.get('id')} {item.get('mutation')}")
    return caught


def human_review_markdown(human: dict[str, Any], cases_by_id: dict[str, dict[str, Any]]) -> str:
    lines = [
        "# Artifact Comprehension v0.2.2 — Morning Human Gate", "",
        "Status: **HUMAN GATE PENDING**", "",
        "This review tests only substantial artifact presentation. It does not test or alter ordinary replies, closeouts, Clear Depth, or the global three-prompt system.",
        "",
    ]
    for item in human["examples"]:
        pilot = cases_by_id[item["pilot_case_id"]]["example"]
        variants = {item["pilot_position"]: pilot}
        variants["Y" if item["pilot_position"] == "X" else "X"] = item["control_response"]
        lines.extend([
            f"## {item['id']} — {item['task_type']}", "",
            f"**Prompt:** {item['prompt']}", "", "### Variant X", "", variants["X"],
            "", "### Variant Y", "", variants["Y"], "",
        ])
    lines.extend([
        "## Rating Sheet", "",
        "| Example | Preferred X/Y/TIE | Why? |",
        "|---|---|---|",
        "| AHG-003F |  |  |", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-behavior", action="store_true", help="Fail until the v0.2.2 morning human gate passes.")
    parser.add_argument("--human-review", action="store_true", help="Print the one-example morning review.")
    parser.add_argument("--json", action="store_true", help="Print the computed receipt as JSON.")
    args = parser.parse_args()
    try:
        contract_checks = validate_contracts()
        changed = changed_paths()
        historical_status = validate_v01_human_verdict(load_json(V01_HUMAN))
        cases, boundary = validate_corpus(load_json(V02_CASES))
        cases_by_id = {case["id"]: case for case in cases}
        round_one_status = validate_v02_round1(load_json(V02_HUMAN_HISTORY))
        round_two_status = validate_v021_round2(load_json(V021_HUMAN_HISTORY))
        human = load_json(V02_HUMAN)
        behavior_status = validate_human_gate(human, cases_by_id)
        caught = run_sabotage(load_json(V02_SABOTAGE), cases_by_id, boundary)
        surface_cases = validate_surface_corpus(load_json(SURFACE_CASES))
        surface_by_id = {case["id"]: case for case in surface_cases}
        surface_caught = run_surface_sabotage(load_json(SURFACE_SABOTAGE), surface_by_id)
    except Exception as exc:  # noqa: BLE001 - one concise verifier surface.
        print("ARTIFACT COMPREHENSION SHADOW PILOT")
        print("STRUCTURAL FAIL")
        print(f"- {exc}")
        return 1
    result = {
        "pilot": "Artifact Comprehension v0.2",
        "scope": "workspace branch; substantial artifacts only",
        "v0.1_status": historical_status,
        "structural_status": "PASS",
        "v0.2_round_one_status": round_one_status,
        "v0.2.1_round_two_status": round_two_status,
        "v0.2.2_behavior_status": behavior_status,
        "fixtures": len(cases),
        "sabotage_caught": len(caught),
        "surface_cases": len(surface_cases),
        "surface_sabotage_caught": len(surface_caught),
        "frozen_global_behavior": True,
        "changed_paths": changed,
        "promotion_status": "BLOCKED pending separate explicit promotion approval",
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("ARTIFACT COMPREHENSION SHADOW PILOT")
        print("STRUCTURAL PASS")
        print(f"v0.1: {historical_status}")
        print(f"v0.2 round one: {round_one_status}")
        print(f"v0.2.1 round two: {round_two_status}")
        print(f"v0.2.2 morning review: {behavior_status}")
        print(f"- checks: {', '.join(contract_checks)}")
        print(f"- artifact fixtures: {len(cases)}/8")
        print(f"- sabotage: {len(caught)}/13 caught")
        print(f"- surface selection: {len(surface_cases)}/8; sabotage: {len(surface_caught)}/6 caught")
        print(f"- changed paths: {len(changed)}; forbidden surfaces: 0")
        print("- CLEAR DEPTH / 3 NEXT PROMPTS / MERGE / GLOBAL / HOOKS UNCHANGED")
    if args.human_review:
        print()
        print(human_review_markdown(human, cases_by_id))
    if args.require_behavior and behavior_status != "BEHAVIOR PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
