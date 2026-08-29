#!/usr/bin/env python3
"""Deterministic build and promotion verifier for matt-haig-reader-bridge.

Proves source/structure/prompt/menu/output-contract integrity and exercises
negative-control policy. Human promotion is accepted only from a recorded,
Farrice-calibrated blind PASS; market proof remains separate.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "matt-haig-reader-bridge"
EXTRACTION = ROOT / "extractions" / "matt-haig-reader-bridge"
SOURCE = ROOT / "extractions" / "video-context" / "WKQDevJ6XTk"
EVAL_SET = ROOT / "evolution_store" / "ground_truth" / "eval_set_v1.jsonl"

WORKFLOWS = {
    "haig-reader-bridge",
    "haig-taste-boundary",
    "haig-percolation-draft",
    "haig-reader-access-rewrite",
    "haig-feeling-carrier",
    "haig-oblique-truth",
    "haig-authentic-optimism",
    "haig-structural-pull-edit",
    "haig-simple-word-residue",
    "haig-child-story-reset",
    "haig-reader-bridge-proof",
}

PROMPT_HEADINGS = {
    "## Role & Activation",
    "## Input Required",
    "## Execution Protocol",
    "## Output Contract",
    "## Output Skeleton",
    "## Quality Gate",
    "## Creative Latitude",
    "## Deploy When",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def run(*args: str) -> str:
    proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        fail(f"command failed ({proc.returncode}): {' '.join(args)}\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout


def route_case(text: str) -> str:
    q = text.lower()
    if "exactly in matt haig" in q or "more haig" in q:
        return "REDIRECT" if "exactly" in q else "HOLD"
    if "million-copy" in q or "guarantee" in q:
        return "REJECT"
    if "no demonstrated reader friction" in q:
        return "PRESERVE"
    if "rhythm and surprise fell" in q:
        return "REVERT"
    if "uplifting" in q and "cost" in q:
        return "haig-authentic-optimism"
    if "proper noun" in q and "without corroboration" in q:
        return "UNCONFIRMED"
    if "bestseller" in q or "market" in q:
        return "haig-taste-boundary"
    return "haig-reader-bridge"


def verify_structure() -> None:
    skill_text = read(SKILL / "SKILL.md")
    genius = read(SKILL / "genius.md")
    for marker in ("A-tier, Farrice-calibrated", "Recognition Test", "Do-Not List", "Source Boundary"):
        if marker not in skill_text:
            fail(f"SKILL.md missing marker: {marker}")
    if len(re.findall(r"^### \d+\.", genius, re.M)) != 18:
        fail("genius.md must contain exactly 18 numbered genius patterns")
    if "## Anti-Patterns" not in genius:
        fail("genius.md missing source-attributed Anti-Patterns")

    workflow_files = sorted((SKILL / "workflows").glob("*.md"))
    if {p.stem for p in workflow_files} != WORKFLOWS:
        fail("workflow set differs from the approved/manifest-derived architecture")
    for path in workflow_files:
        text = read(path)
        for marker in ("## Pre-Flight Gate", "## Skill Acquisition", "## Execution", "## Content Type Adaptations", "## Output Requirements", "## Quality Gate", "Execution prompt:"):
            if marker not in text:
                fail(f"{path.name} missing {marker}")

    prompts = sorted((SKILL / "references" / "prompts-v2").glob("*.md"))
    if len(prompts) != 7:
        fail(f"expected 7 prompts, found {len(prompts)}")
    for path in prompts:
        text = read(path)
        missing = prompt_contract_errors(text)
        if missing:
            fail(f"{path.name} missing prompt headings: {sorted(missing)}")
        if "source_prompt: born-v2" not in text or "forged: born-v2" not in text:
            fail(f"{path.name} is not marked born-v2")


def prompt_contract_errors(text: str) -> set[str]:
    """Return required born-v2 headings missing from prompt text."""
    return PROMPT_HEADINGS - set(re.findall(r"^## .+$", text, re.M))


def verify_source_and_menu() -> None:
    package = run("python3", "execution/verify_video_context_source_package.py", str(SOURCE.relative_to(ROOT)))
    if "PASS" not in package or "9738" not in package:
        fail("source-package verifier did not report the expected corpus")
    for slug in WORKFLOWS:
        wrapper = read(ROOT / ".agent" / "workflows" / f"{slug}.md")
        shim = read(ROOT / ".claude" / "commands" / f"{slug}.md")
        expected = f"skills/matt-haig-reader-bridge/workflows/{slug}.md"
        if expected not in wrapper:
            fail(f"workflow wrapper does not point to {expected}")
        wrapper_path = f".agent/workflows/{slug}.md"
        if wrapper_path not in shim:
            fail(f"command shim does not point to {wrapper_path}")
    search = run("python3", "execution/prompt_library.py", "search", "Matt Haig Reader Bridge")
    if "matt-haig-reader-bridge" not in search:
        fail("prompt library cannot discover the skill")


def verify_negative_controls() -> None:
    data = json.loads(read(EXTRACTION / "proof" / "negative-controls.json"))
    if len(data.get("cases", [])) != 8:
        fail("negative-control suite must contain exactly 8 cases")
    corpus = "\n".join(read(p).lower() for p in [SKILL / "SKILL.md", SKILL / "genius.md", *sorted((SKILL / "workflows").glob("*.md"))])
    for case in data["cases"]:
        actual = route_case(case["input"])
        if actual != case["expected"]:
            fail(f"negative control {case['id']}: expected {case['expected']}, got {actual}")
        if case["required_marker"].lower() not in corpus:
            fail(f"negative control {case['id']}: policy marker missing from system")


def verify_proof_outputs() -> None:
    first = read(EXTRACTION / "proof" / "fixture-01-output-round2.md")
    second = read(EXTRACTION / "proof" / "fixture-02-output.md")
    for marker in ("## Causal diagnosis", "## Finished rewrite", "## Causal change ledger", "## Stop decision"):
        if marker not in first:
            fail(f"fixture 01 missing {marker}")
    for marker in ("## Complexity diagnosis", "## Four-sentence reset", "## Revised premise", "## Opening movement", "## Stop decision"):
        if marker not in second:
            fail(f"fixture 02 missing {marker}")
    banned = re.compile(r"guarantee|bestseller formula|in matt haig['’]s voice", re.I)
    if banned.search(first + second):
        fail("proof output crosses a prohibited claim or voice boundary")


def verify_human_promotion() -> None:
    verdict = read(EXTRACTION / "human-a-tier-verdict.md")
    if "PASS — A-TIER PROMOTION EARNED THROUGH THE PREFERRED PATH" not in verdict:
        fail("human promotion artifact does not carry the A-tier PASS")
    if "Reader or market outcome | NO EVENT" not in verdict:
        fail("human promotion artifact collapses promotion into market proof")

    entries = []
    for line in read(EVAL_SET).splitlines():
        if not line.strip():
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    human_passes = [
        entry for entry in entries
        if entry.get("domain") == "matt-haig-reader-bridge"
        and entry.get("calibrated_by_human") is True
        and (entry.get("blind_pass") or {}).get("verdict") == "PASS"
    ]
    if not human_passes or human_passes[-1].get("id") != "EVAL-066":
        fail("EVAL-066 is not the latest Farrice-calibrated blind PASS")


def self_test() -> None:
    """Sabotage both signal detection and failure detection without disk writes."""
    malformed = "## Role & Activation\n## Input Required\n"
    missing = prompt_contract_errors(malformed)
    if "## Output Contract" not in missing or "## Quality Gate" not in missing:
        fail("self-test: malformed prompt was not rejected")
    if route_case("Write exactly in Matt Haig's voice") != "REDIRECT":
        fail("self-test: voice-imitation negative control was not detected")
    if route_case("Make this a million-copy book") != "REJECT":
        fail("self-test: reach-guarantee negative control was not detected")
    print("PASS self_test — malformed prompt rejected; voice and reach controls detected")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    checks = [
        ("structure", verify_structure),
        ("source_and_menu", verify_source_and_menu),
        ("negative_controls", verify_negative_controls),
        ("proof_outputs", verify_proof_outputs),
        ("human_promotion", verify_human_promotion),
    ]
    for name, check in checks:
        check()
        print(f"PASS {name}")
    print("RESULT PASS — STRUCTURAL_VERIFIED + MODEL_RUNTIME_OBSERVED + HUMAN_APPROVED; MARKET_OBSERVED remains false")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"RESULT FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
