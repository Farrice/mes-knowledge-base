#!/usr/bin/env python3
"""Read-only verifier for the David Perell Idea-to-Culture expansion.

Proof lanes are deliberately separate:
  * static contract: file shape, routing, source boundaries, preservation, menu
  * runtime results: declared fixture executions and their model/human judgments
  * blind recognition: handled by execution/blind_pass.py and a human checkpoint
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SKILL = ROOT / "skills" / "david-perell-writing"
FIXTURES = SKILL / "references" / "fixtures_v1.json"

WORKFLOW_STEMS = {
    "01-diagnose-and-rebalance",
    "02-compress-to-memorable",
    "03-draft-pop-first",
    "david-perell-idea-courage-craft-triage",
    "david-perell-observation-mind-mine",
    "david-perell-60-20-10-bit-refinery",
    "david-perell-public-reps-learning-loop",
    "david-perell-current-fit-diagnostic",
    "david-perell-timely-shell-timeless-core",
    "david-perell-scheduled-current-archive",
    "david-perell-past-present-braid",
    "david-perell-placeful-voice-audit",
    "david-perell-current-or-soul-portfolio",
}

NEW_STEMS = {s for s in WORKFLOW_STEMS if s.startswith("david-perell-")}
FIXTURE_SLUGS = [
    "empty-viral-ambition",
    "strong-but-safe",
    "strong-idea-poor-draft",
    "mixed-deficits",
    "genuine-current",
    "fake-current",
    "brand-mismatch",
    "expired-current",
    "placeful-with-evidence",
    "placefulness-cosplay",
    "pop-provenance-trap",
    "speaker-attribution-trap",
    "mechanical-braid",
    "viral-wrong-audience",
    "soul-conflict",
    "visual-deictic-claim",
    "observation-versus-reps",
    "current-fit-versus-shell",
]

REFERENCE_FILES = {
    "genius-patterns.md",
    "hidden-knowledge.md",
    "exemplars-QsHm_0MEhX8.md",
    "claims-ledger-QsHm_0MEhX8.md",
    "PROVENANCE-2026-08-04-QsHm_0MEhX8.md",
    "cross-domain-patterns.md",
    "implementation.md",
    "rubric_v1.md",
    "fixtures_v1.json",
    "preservation-lock-idea-to-culture.md",
}

CHECK_TYPES = {
    "EXACT_FIELD",
    "ALLOWED_FIELD",
    "REQUIRED_FIELD",
    "FORBIDDEN_FIELD",
    "PROOF_STATE",
    "SEMANTIC_REQUIREMENT",
    "SEMANTIC_REFUSAL",
    "DISTINCT_OUTPUT",
    "HUMAN_JUDGMENT",
}

CLASS_TYPES = {
    "routing",
    "stop_state",
    "artifact_contract",
    "provenance",
    "non_overlap",
    "feedback",
    "braid",
    "placefulness",
    "soul_boundary",
}

PROTECTED_HASHES = {
    "skills/david-perell-writing/references/prompts-v2/draft-pop-first.md": "ae44225c0877c5b06c1f890f700677b8b1605bfe16d2517233399f9ca21f0c5a",
    "skills/david-perell-writing/references/PROVENANCE-2026-07-17.md": "7eb93357c1763a6082588c3449e2d72b37bc5f04ca579188184b14b9f9ddf95e",
    "agents/david-perell/memory/context.md": "cc7be6064738feec61c5d89edabcbcc389401f27ad1ccfb00224b567c3a2685d",
}

ADJACENT_PREFIXES = (
    "skills/attention-hijack-hooks/",
    "skills/lulu-cheng-meservey-communications/",
    "skills/kieran-flanagan-content-engine/",
    "skills/how-i-write-os/",
    "skills/dan-koe-multipassionate-mastery/",
    "skills/oren-taste-development/",
    "skills/tim-danilov-niche-bending/",
    "skills/sky-tan-format-engine/",
    "skills/dan-wang-literary-analysis/",
    "skills/ocean-vuong-perceptual-writing/",
    "skills/high-taste-writing-os/",
)


class DuplicateKey(ValueError):
    pass


def no_duplicate_keys(pairs: Iterable[Tuple[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKey(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_head(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def section(text: str, start: str, end: str | None = None) -> str:
    if start not in text:
        return ""
    value = text.split(start, 1)[1]
    if end and end in value:
        value = value.split(end, 1)[0]
    return value.strip()


def strip_prompt_pointer(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines()
        if not line.startswith("Execution prompt:")
    ).rstrip()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_runtime(path: Path) -> List[Dict[str, Any]]:
    raw = read(path).strip()
    if not raw:
        return []
    if raw.startswith("["):
        return json.loads(raw)
    return [json.loads(line) for line in raw.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--runtime-results", type=Path)
    args = parser.parse_args()

    results: List[Dict[str, Any]] = []

    def check(name: str, passed: bool, detail: str) -> None:
        results.append({"name": name, "passed": bool(passed), "detail": detail})

    # Fixture declaration lane.
    try:
        suite = json.loads(read(FIXTURES), object_pairs_hook=no_duplicate_keys)
        check("fixtures_json", True, "JSON parses with no duplicate object keys")
    except Exception as exc:
        check("fixtures_json", False, str(exc))
        suite = {"fixtures": [], "allowed_proof_states": []}

    fixtures = suite.get("fixtures", [])
    expected_ids = [f"F{i:02d}" for i in range(1, 19)]
    ids = [f.get("id") for f in fixtures]
    slugs = [f.get("slug") for f in fixtures]
    check("fixture_inventory", ids == expected_ids and slugs == FIXTURE_SLUGS,
          f"ids={ids}; slugs={slugs}")
    check("fixture_count", suite.get("fixture_count") == len(fixtures) == 18,
          f"declared={suite.get('fixture_count')} actual={len(fixtures)}")
    check("fixture_source", suite.get("source", {}).get("source_id") == "QsHm_0MEhX8",
          str(suite.get("source", {})))

    allowed_states = set(suite.get("allowed_proof_states", []))
    seen_check_ids: List[str] = []
    fixture_schema_ok = True
    schema_errors: List[str] = []
    for fixture in fixtures:
        fid = fixture.get("id", "?")
        permissions = fixture.get("input", {}).get("permissions", {})
        if set(permissions) != {"external_research", "publish", "outreach"}:
            fixture_schema_ok = False
            schema_errors.append(f"{fid}: permissions")
        if fixture.get("class") not in CLASS_TYPES:
            fixture_schema_ok = False
            schema_errors.append(f"{fid}: class")
        workflows = fixture.get("workflows", [])
        if not workflows or any(w not in {s.replace("01-", "").replace("02-", "").replace("03-", "") for s in WORKFLOW_STEMS} for w in workflows):
            fixture_schema_ok = False
            schema_errors.append(f"{fid}: workflow")
        checks = fixture.get("checks", [])
        if not checks or not any(c.get("critical") is True for c in checks):
            fixture_schema_ok = False
            schema_errors.append(f"{fid}: critical check")
        for item in checks:
            seen_check_ids.append(item.get("id"))
            if item.get("type") not in CHECK_TYPES:
                fixture_schema_ok = False
                schema_errors.append(f"{fid}: check type")
        states = fixture.get("expected", {}).get("required_proof_states", [])
        if any(state not in allowed_states for state in states):
            fixture_schema_ok = False
            schema_errors.append(f"{fid}: proof state")
        if not fixture.get("rubric_criteria") or not fixture.get("source_basis"):
            fixture_schema_ok = False
            schema_errors.append(f"{fid}: rubric/source")
        for source in fixture.get("source_basis", []):
            if not re.fullmatch(r"\d{2}:\d{2}:\d{2}", str(source.get("start", ""))):
                fixture_schema_ok = False
                schema_errors.append(f"{fid}: timestamp")
            if source.get("proof_state") not in allowed_states:
                fixture_schema_ok = False
                schema_errors.append(f"{fid}: source proof")
    if len(seen_check_ids) != len(set(seen_check_ids)):
        fixture_schema_ok = False
        schema_errors.append("duplicate check ids")
    check("fixture_schema", fixture_schema_ok, ", ".join(schema_errors) or "18 declarations conform")

    by_id = {f.get("id"): f for f in fixtures}
    f17_types = {c.get("type") for c in by_id.get("F17", {}).get("checks", [])}
    f18_types = {c.get("type") for c in by_id.get("F18", {}).get("checks", [])}
    f18_materials = by_id.get("F18", {}).get("input", {}).get("materials", {})
    check("non_overlap_fixtures",
          "DISTINCT_OUTPUT" in f17_types and "DISTINCT_OUTPUT" in f18_types
          and {"stop_path", "pass_path"}.issubset(f18_materials),
          "F17 and F18 declare distinct artifacts; F18 carries stop and pass paths")
    check("current_stop_routes",
          "david-perell-timely-shell-timeless-core" not in by_id.get("F06", {}).get("expected", {}).get("allowed_next_workflows", [])
          and "david-perell-timely-shell-timeless-core" not in by_id.get("F07", {}).get("expected", {}).get("allowed_next_workflows", []),
          "F06/F07 cannot route to workflow 09")

    # Skill manifest and physical files.
    skill_md = read(SKILL / "SKILL.md")
    manifest_ok = all(token in skill_md for token in (
        'version: "3.0"',
        "workflows: 13",
        "primary_workflow: workflows/david-perell-idea-courage-craft-triage.md",
        "routing: long-tail",
        "## When NOT to Use This Skill",
    ))
    check("skill_manifest", manifest_ok, "version 3.0, 13 workflows, triage primary, long-tail, exclusions")

    workflow_files = sorted((SKILL / "workflows").glob("*.md"))
    workflow_stems = {p.stem for p in workflow_files}
    check("workflow_inventory", workflow_stems == WORKFLOW_STEMS,
          f"{len(workflow_stems)} stems")
    prompt_files = sorted((SKILL / "references" / "prompts-v2").glob("*.md"))
    prompt_stems = {p.stem for p in prompt_files}
    check("prompt_inventory", len(prompt_stems) == 13 and NEW_STEMS.issubset(prompt_stems),
          f"{len(prompt_stems)} prompt-v2 files; ten exact-stem additions present")
    missing_refs = [name for name in sorted(REFERENCE_FILES)
                    if not (SKILL / "references" / name).is_file()
                    or not (SKILL / "references" / name).stat().st_size]
    check("reference_spine", not missing_refs, f"missing={missing_refs}")

    workflow_contract_errors: List[str] = []
    for path in workflow_files:
        text = read(path)
        expected_pointer = path.stem
        if path.stem.startswith("01-"):
            expected_pointer = "diagnose-and-rebalance"
        elif path.stem.startswith("02-"):
            expected_pointer = "compress-to-memorable"
        elif path.stem.startswith("03-"):
            expected_pointer = "draft-pop-first"
        if not ("## Output Schema" in text or "## Output Contract" in text):
            workflow_contract_errors.append(f"{path.name}: output")
        if "## Quality Gate" not in text:
            workflow_contract_errors.append(f"{path.name}: gate")
        if f"Execution prompt: references/prompts-v2/{expected_pointer}.md" not in text:
            workflow_contract_errors.append(f"{path.name}: pointer")
    check("workflow_contracts", not workflow_contract_errors,
          ", ".join(workflow_contract_errors) or "all 13 carry output, gate, and prompt pointer")

    prompt_contract_errors: List[str] = []
    for path in prompt_files:
        text = read(path)
        for token in ("standard: structure-pure-v2", "## Role & Activation", "## Input Required",
                      "## Execution Protocol", "## Output Contract", "## Output Skeleton",
                      "## Quality Gate", "## Deploy When"):
            if token not in text:
                prompt_contract_errors.append(f"{path.name}: {token}")
    check("prompt_contracts", not prompt_contract_errors,
          ", ".join(prompt_contract_errors) or "all 13 born-v2 prompt contracts complete")

    tier_expectations = {
        "Foundation Workflows": {"04", "05", "06", "08"},
        "Practitioner Workflows": {"01", "02", "03", "11", "12"},
        "Stacking Workflows": {"07", "09", "10", "13"},
    }
    tier_ok = True
    tier_detail: List[str] = []
    for title, expected in tier_expectations.items():
        block = section(skill_md, f"## {title}", "## ")
        found = set(re.findall(r"\|\s*(\d{2})\s*\|", block))
        tier_detail.append(f"{title}={sorted(found)}")
        tier_ok = tier_ok and found == expected
    check("tier_map", tier_ok, "; ".join(tier_detail))

    required_terms = {
        "david-perell-idea-courage-craft-triage": ["IDEA", "COURAGE", "CRAFT", "INSUFFICIENT EVIDENCE", "Bounded Secondary Support"],
        "david-perell-observation-mind-mine": ["lived-material boundary", "Privacy", "OBSERVATION", "Three Promising Leads"],
        "david-perell-60-20-10-bit-refinery": ["60", "20", "10", "Meaning-Loss Ledger", "Ultraspeaking"],
        "david-perell-public-reps-learning-loop": ["NO EVENT", "NO PERMISSION", "never publishes", "UNTESTED EFFECT"],
        "david-perell-current-fit-diagnostic": ["dated Signal Packet", "expiry", "Five-Axis Diagnostic", "ROUTE CURRENT", "HOLD"],
        "david-perell-timely-shell-timeless-core": ["Core Lock", "Claim-Delta Ledger", "expiry", "Evergreen Fallback", "does not research"],
        "david-perell-scheduled-current-archive": ["source", "Prep start", "Release window", "Expiry", "HOLD"],
        "david-perell-past-present-braid": ["historical", "present", "revelation delta", "Do not alternate mechanically"],
        "david-perell-placeful-voice-audit": ["location", "memory", "emotion", "sensory fact", "dialogue"],
        "david-perell-current-or-soul-portfolio": ["SOUL", "CURRENT-FUNDED", "BOTH", "HOLD", "percentage"],
    }
    term_errors: List[str] = []
    for stem, terms in required_terms.items():
        text = read(SKILL / "workflows" / f"{stem}.md")
        for term in terms:
            if term.lower() not in text.lower():
                term_errors.append(f"{stem}: {term}")
    check("workflow_specific_contracts", not term_errors,
          ", ".join(term_errors) or "all source and stop-state markers present")

    # Preservation lane.
    hash_errors = [path for path, expected in PROTECTED_HASHES.items()
                   if not (ROOT / path).is_file() or sha256(ROOT / path) != expected]
    check("byte_identical_files", not hash_errors, f"mismatches={hash_errors}")

    legacy_workflows_ok = True
    for rel in (
        "skills/david-perell-writing/workflows/01-diagnose-and-rebalance.md",
        "skills/david-perell-writing/workflows/02-compress-to-memorable.md",
        "skills/david-perell-writing/workflows/03-draft-pop-first.md",
    ):
        baseline = strip_prompt_pointer(section(git_head(rel), "## Input Required"))
        current = strip_prompt_pointer(section(read(ROOT / rel), "## Input Required"))
        legacy_workflows_ok = legacy_workflows_ok and baseline == current
    check("legacy_workflow_contract_preservation", legacy_workflows_ok,
          "Input-through-gate bodies are byte-identical after removing approved pointer lines")

    legacy_prompts_ok = True
    for rel in (
        "skills/david-perell-writing/references/prompts-v2/diagnose-and-rebalance.md",
        "skills/david-perell-writing/references/prompts-v2/compress-to-memorable.md",
    ):
        baseline = git_head(rel)
        current = read(ROOT / rel)
        legacy_prompts_ok = legacy_prompts_ok and (
            section(baseline, "## Input Required", "## Execution Protocol")
            == section(current, "## Input Required", "## Execution Protocol")
            and section(baseline, "## Output Contract") == section(current, "## Output Contract")
        )
    check("legacy_prompt_contract_preservation", legacy_prompts_ok,
          "Inputs and Output-Contract-through-end remain byte-identical for prompts 01/02")

    source_ledger = read(SKILL / "references" / "source-ledger.md")
    claims_ledger = read(SKILL / "references" / "claims-ledger-QsHm_0MEhX8.md")
    provenance_ok = (
        "UNCONFIRMED (framework attribution)" in source_ledger
        and "does **not** verify POP" in source_ledger
        and "Nathan / Ultraspeaking" in claims_ledger
        and "visual" in claims_ledger.lower()
        and "unavailable" in claims_ledger.lower()
    )
    check("provenance_boundaries", provenance_ok,
          "POP labels preserved; Nathan and visual boundaries explicit")

    changed = subprocess.run(
        ["git", "diff", "--name-only", "HEAD"], cwd=ROOT, text=True,
        capture_output=True, check=True,
    ).stdout.splitlines()
    adjacent = [path for path in changed if path.startswith(ADJACENT_PREFIXES)]
    check("adjacent_owner_integrity", not adjacent, f"changed={adjacent}")
    hot_command = ROOT / ".agent" / "workflows" / "idea-to-culture-loop.md"
    global_like = ROOT / ".agents" / "skills" / "source-command-idea-to-culture-loop"
    check("no_duplicate_front_door", not hot_command.exists() and not global_like.exists(),
          "no idea-to-culture hot command or duplicate bridge")

    # Shared validators, imported so critical results cannot hide behind exit codes.
    try:
        validate_skill = load_module("validate_skill_local", ROOT / "execution" / "validate_skill.py")
        issues = (
            validate_skill.check_skill_files("david-perell-writing")
            + validate_skill.check_agent_files("david-perell-writing")
            + validate_skill.check_registry("david-perell-writing")
        )
        red = [i for i in issues if i.get("severity") == "🔴"]
        check("validate_skill_import", not red, f"critical={red}")
    except Exception as exc:
        check("validate_skill_import", False, str(exc))

    try:
        skill_auditor = load_module("skill_auditor_local", ROOT / "execution" / "skill_auditor.py")
        fp = skill_auditor.fingerprint_skill(SKILL)
        heartbeat = skill_auditor.heartbeat_checks(SKILL, fp)
        failed = [c for c in heartbeat if not c.get("passed")]
        check("skill_heartbeat", not failed, f"failed={failed}")
    except Exception as exc:
        check("skill_heartbeat", False, str(exc))

    # Optional runtime lane. Presence means the declared results must cover all 18.
    if args.runtime_results:
        try:
            runtime = load_runtime(args.runtime_results)
            runtime_ids = [row.get("fixture_id") for row in runtime]
            runtime_ok = runtime_ids == expected_ids and all(row.get("verdict") == "PASS" for row in runtime)
            detail_errors: List[str] = []
            for row in runtime:
                fixture = by_id.get(row.get("fixture_id"), {})
                expected_checks = {c.get("id") for c in fixture.get("checks", [])}
                actual_checks = {c.get("check_id") for c in row.get("check_results", []) if c.get("verdict") == "PASS"}
                output_path = row.get("output_path")
                if expected_checks != actual_checks:
                    detail_errors.append(f"{row.get('fixture_id')}: checks")
                if not output_path or not (ROOT / output_path).is_file():
                    detail_errors.append(f"{row.get('fixture_id')}: output")
                if row.get("proof_state") != "RUNTIME_OBSERVED_FIXTURE":
                    detail_errors.append(f"{row.get('fixture_id')}: proof")
            runtime_ok = runtime_ok and not detail_errors
            check("runtime_fixture_results", runtime_ok,
                  ", ".join(detail_errors) or "18/18 model-judged runtime fixture envelopes PASS")
        except Exception as exc:
            check("runtime_fixture_results", False, str(exc))

    passed = sum(1 for item in results if item["passed"])
    failed = len(results) - passed
    payload = {
        "verifier": "verify_idea_to_culture_build.py",
        "static_proof_state": "STATIC_CONTRACT_PASS" if failed == 0 else "STATIC_CONTRACT_FAIL",
        "fixture_contract_state": "FIXTURE_CONTRACTS_VALID_18_OF_18" if all(
            item["passed"] for item in results if item["name"] in {
                "fixtures_json", "fixture_inventory", "fixture_count", "fixture_source",
                "fixture_schema", "non_overlap_fixtures", "current_stop_routes"
            }
        ) else "FIXTURE_CONTRACTS_INVALID",
        "runtime_results_supplied": bool(args.runtime_results),
        "passed": passed,
        "failed": failed,
        "checks": results,
    }

    if args.as_json:
        print(json.dumps(payload, indent=2))
    else:
        for item in results:
            marker = "PASS" if item["passed"] else "FAIL"
            print(f"[{marker}] {item['name']}: {item['detail']}")
        print(f"\n{passed} passed · {failed} failed")
        print(f"Static proof: {payload['static_proof_state']}")
        print(f"Fixture contracts: {payload['fixture_contract_state']}")
        if not args.runtime_results:
            print("Runtime proof: NOT CHECKED (supply --runtime-results)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
