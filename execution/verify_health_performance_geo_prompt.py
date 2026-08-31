#!/usr/bin/env python3
"""Verify the Angle Map automation prompt keeps its market and tool contracts.

This guard exists because the daily brief drifted into a narrow GLP-1 lane even
though the intended job is broad health-performance market-domain creative
strategy. It also prevents retired social-listening instructions from surviving
in a second section after the governing tool ladder changes.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
# 2026-08-08: library moved into the knowledge arena (commit 91a30ab40 sweep).
PROMPT = ROOT / "_active" / "knowledge" / "health-performance-ip-library" / "AUTOMATION_PROMPT.md"
DIRECTOR_BRIEF = (
    ROOT
    / "_active"
    / "knowledge"
    / "health-performance-ip-library"
    / "daily"
    / "2026-08-28-angle-map-director-brief.md"
)
DIRECTOR_FIXTURES = ROOT / "execution" / "fixtures" / "angle-map-director-brief" / "cases.json"


# The prompt version evolves (3.4 -> 3.5 -> ...); the guard is that a Version
# line exists and still declares the engine identity, not that one frozen
# number stays pinned. 2026-08-08: v4.0 deliberately renamed the identity to
# "Content Factory" (GEO daily brief + insight brief fused into one listening
# engine); the anti-GLP-1-capture clauses below are the real guard and are
# unchanged.
VERSION_PATTERN = re.compile(
    r"^Version:\s*\d+(\.\d+)*\s+(Market-Domain Creative Intelligence|Content Factory)",
    re.MULTILINE,
)

REQUIRED_PHRASES = {
    "market_domain_mandate": "### Market-Domain Mandate",
    "not_glp1_monitor": "The engine is not a GLP-1 monitor",
    "ten_candidate_signals": "at least ten candidate signals",
    "eight_non_glp1": "At least eight must be non-GLP-1-specific",
    "glp1_one_signal": "GLP-1 is one category signal",
    "repetition_penalty": "Apply a repetition penalty before picking",
    "market_intelligence_read": "Market Intelligence Read",
    "creative_depth_gate": "### Creative Strategist Depth Gate",
    "market_lane_first": "1. **Market Domain And Avatar Pressure Lane**",
    "source_truth_later": "5. **Source Truth Lane**",
    "non_glp1_acceptance": "at least eight angle candidates were non-GLP-1-specific",
    "social_listening_ladder": "## Social Listening Tool Ladder",
    "research_facade_first": "1. **research.py facade** (`execution/research.py`)",
    "recovered_reddit_likely": "Reddit thread text fetches come LIKELY-grade (not VERIFIED)",
    "manual_url_check": "standing manual URL-check step",
    "verified_promotion": "label receipt `VERIFIED`",
    "discard_mismatch": "`DISCARD` if quote was invented",
    "lane_research_first": "3. **Social Listening Lane** (`research.py`-first",
    "lane_likely_boundary": "Research-recovered Reddit verbatim remains `LIKELY`",
    "lane_manual_check": "manual raw-URL check confirms quote, voice, and context",
    "apify_retired": "Apify retired per fleet decision",
    "director_shadow_contract": "## Director Brief Shadow Contract (ACTIVE, NOT PROMOTED)",
    "director_same_research": "Render one additional reader-facing brief from the completed research state",
    "director_full_authority": "full `0-11` listening brief remains the authoritative research",
    "director_word_budget": "The Director Brief must be `900-1200` words",
    "director_five_sections": "use only these five sections",
    "director_friday_link": "On Friday, link the separate weekly synthesis",
    "director_no_second_pass": "second research pass",
}

BANNED_PHRASES = {
    "apify_first_hyphenated": "Apify-first",
    "apify_first_plain": "Apify first",
    "apify_reddit_actor": "via Apify reddit actor",
    "scraper_actor_transcripts": "transcripts via sc-* actors",
}


def validate_prompt(text: str) -> list[str]:
    """Return contract violations; an empty list means the prompt is safe."""
    errors: list[str] = []

    if not VERSION_PATTERN.search(text):
        errors.append("missing a valid Version line for the engine identity")

    for name, phrase in REQUIRED_PHRASES.items():
        if phrase not in text:
            errors.append(f"missing {name}: {phrase}")

    lowered = text.lower()
    for name, phrase in BANNED_PHRASES.items():
        if phrase.lower() in lowered:
            errors.append(f"retired instruction {name}: {phrase}")

    glp1_count = lowered.count("glp-1")
    market_count = lowered.count("market")
    if market_count <= glp1_count:
        errors.append(
            "prompt appears GLP-1-heavy; "
            f"market_count={market_count}, glp1_count={glp1_count}"
        )

    return errors


DIRECTOR_SECTIONS = [
    "The answer",
    "Market read",
    "Creative direction",
    "Production handoff",
    "Action board",
]

DIRECTOR_FORBIDDEN = {
    "hidden process log": "context load packet",
    "routing trace": "route proof",
    "gate log": "gate status",
    "candidate-angle table": "candidate angle table",
    "living-doc delta": "living-doc deltas",
    "forced production bundle": "five hooks",
    "forced carousel": "carousel outline",
    "forced video": "short video script",
}


def validate_director_brief(text: str, mode: str = "daily") -> list[str]:
    """Return reader-facing brief violations; empty means the shadow shape holds."""
    errors: list[str] = []
    word_count = len(text.split())
    if not 900 <= word_count <= 1200:
        errors.append(f"director brief must be 900-1200 words; found {word_count}")

    headings = re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    if headings != DIRECTOR_SECTIONS:
        errors.append(
            "director brief must use exactly the five reader-facing sections; "
            f"found {headings}"
        )

    answer_match = re.search(
        r"^## The answer\s*$\n(?P<body>.*?)(?=^## Market read\s*$)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not answer_match:
        errors.append("missing bounded The answer section")
    elif len(answer_match.group("body").split()) > 150:
        errors.append("The answer section exceeds 150 words")

    market_match = re.search(
        r"^## Market read\s*$\n(?P<body>.*?)(?=^## Creative direction\s*$)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not market_match:
        errors.append("missing bounded Market read section")
    else:
        signal_count = len(re.findall(r"^###\s+", market_match.group("body"), flags=re.MULTILINE))
        if not 1 <= signal_count <= 3:
            errors.append(f"Market read must contain 1-3 signal blocks; found {signal_count}")
        for label in ("**Signal:**", "**Meaning:**", "**Use:**"):
            if market_match.group("body").count(label) != signal_count:
                errors.append(f"each market block must contain {label}")

    lowered = text.lower()
    for name, phrase in DIRECTOR_FORBIDDEN.items():
        if phrase in lowered:
            errors.append(f"reader-facing brief contains {name}: {phrase}")

    if text.count("https://") < 3:
        errors.append("director brief needs at least three live source links")
    if text.count("**Recommended territory:**") != 1:
        errors.append("director brief must contain exactly one recommended territory")

    for field in (
        "**Objective:**",
        "**Desired response:**",
        "**Required material:**",
        "**First deliverable:**",
        "**Quality bar:**",
        "**Do not:**",
    ):
        if field not in text:
            errors.append(f"production handoff missing {field}")

    for pack in ("**Production Pack:**", "**Evidence Pack:**", "**System Receipt:**"):
        if pack not in text:
            errors.append(f"action board missing {pack}")

    if mode == "friday" and "**Weekly synthesis:**" not in text:
        errors.append("Friday director brief must link the separate weekly synthesis")

    return errors


def _mutate_director(text: str, mutation: str) -> str:
    if mutation == "remove_http":
        return text.replace("https://", "source://")
    if mutation == "append_hidden_process":
        return f"{text}\n\nContext Load Packet: internal trace\n"
    if mutation == "duplicate_territory":
        return f"{text}\n\n**Recommended territory:** A second lead.\n"
    if mutation == "force_format_volume":
        return f"{text}\n\nAlso deliver five hooks, a carousel outline, and a short video script.\n"
    raise ValueError(f"unknown director fixture mutation: {mutation}")


def run_director_fixture_tests() -> list[str]:
    """Run pass, fail, and sabotage cases declared in the fixture manifest."""
    failures: list[str] = []
    if not DIRECTOR_FIXTURES.exists():
        return [f"missing director fixture manifest: {DIRECTOR_FIXTURES}"]

    manifest = json.loads(DIRECTOR_FIXTURES.read_text(encoding="utf-8"))
    for case in manifest["cases"]:
        case_path = ROOT / case["path"]
        if not case_path.exists():
            failures.append(f"{case['name']}: missing fixture source {case_path}")
            continue
        case_text = case_path.read_text(encoding="utf-8")
        if mutation := case.get("mutation"):
            case_text = _mutate_director(case_text, mutation)
        errors = validate_director_brief(case_text, case.get("mode", "daily"))
        expectation = case["expect"]
        if expectation == "PASS" and errors:
            failures.append(f"{case['name']}: expected PASS, got {errors}")
        elif expectation == "FAIL":
            required_error = case["error_contains"]
            if not any(required_error in error for error in errors):
                failures.append(
                    f"{case['name']}: expected failure containing {required_error!r}, got {errors}"
                )
    return failures


def run_self_test(text: str) -> list[str]:
    """Sabotage both prompt and output contracts and prove they reject drift."""
    failures: list[str] = []

    missing_ladder = text.replace(
        REQUIRED_PHRASES["research_facade_first"],
        "1. **legacy social facade**",
        1,
    )
    missing_errors = validate_prompt(missing_ladder)
    if not any("missing research_facade_first" in error for error in missing_errors):
        failures.append("did not reject a missing research.py-first ladder")

    stale_tool = f"{text}\nApify-first\n"
    stale_errors = validate_prompt(stale_tool)
    if not any("retired instruction apify_first_hyphenated" in error for error in stale_errors):
        failures.append("did not reject a reintroduced Apify-first instruction")

    failures.extend(run_director_fixture_tests())

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify the Angle Map automation prompt contract."
    )
    parser.add_argument(
        "--prompt",
        type=Path,
        default=PROMPT,
        help="Prompt path to validate (defaults to the governing workspace prompt).",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Also run prompt and Director Brief negative controls.",
    )
    parser.add_argument(
        "--director-brief",
        type=Path,
        help="Optional Director Brief path to validate.",
    )
    parser.add_argument(
        "--mode",
        choices=("daily", "friday"),
        default="daily",
        help="Director Brief validation mode.",
    )
    args = parser.parse_args()
    prompt = args.prompt

    if not prompt.exists():
        print(f"FAIL: missing prompt: {prompt}")
        return 1

    text = prompt.read_text(encoding="utf-8")
    errors = validate_prompt(text)
    if errors:
        print("FAIL: Angle Map automation prompt contract violations:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.self_test:
        self_test_failures = run_self_test(text)
        if self_test_failures:
            print("FAIL: verifier negative-control failures:")
            for failure in self_test_failures:
                print(f"- {failure}")
            return 1
        print("PASS: prompt and Director Brief negative controls rejected all sabotages.")

    if args.director_brief:
        if not args.director_brief.exists():
            print(f"FAIL: missing Director Brief: {args.director_brief}")
            return 1
        director_errors = validate_director_brief(
            args.director_brief.read_text(encoding="utf-8"),
            args.mode,
        )
        if director_errors:
            print("FAIL: Director Brief contract violations:")
            for error in director_errors:
                print(f"- {error}")
            return 1
        print(f"PASS: Director Brief holds the {args.mode} reader-facing contract.")
        print(f"Director Brief: {args.director_brief}")

    glp1_count = text.lower().count("glp-1")
    market_count = text.lower().count("market")
    print("PASS: Angle Map prompt has market and social-listening guardrails.")
    print(f"Prompt: {prompt}")
    print(f"market_count={market_count}; glp1_count={glp1_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
