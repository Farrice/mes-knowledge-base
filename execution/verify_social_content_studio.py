#!/usr/bin/env python3
"""Deterministic offline verifier for the Social Content Studio skill system."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "extractions/video-context/hoVC2W0p0Zg"
SKILL = ROOT / "skills/kieran-flanagan-content-intelligence"
WORKFLOW = SKILL / "workflows/social-content-studio.md"
PROMPT = SKILL / "references/prompts-v2/social-content-studio.md"
CONTRACT = SKILL / "references/social-content-studio-skill-system-contract.md"
DELTA = SKILL / "references/social-content-studio-source-delta.md"
WRAPPER = ROOT / ".agent/workflows/social-content-studio.md"
COMMAND_SKILL = ROOT / ".agents/skills/source-command-social-content-studio/SKILL.md"
PILOT_ROOT = ROOT / "_active/farrice-brand/content/social-content-studio"
PILOT = PILOT_ROOT / "PILOT-REVIEW-PACK.md"
MANIFEST = PILOT_ROOT / "approval-manifest.json"
BEHAVIOR = PILOT_ROOT / "behavior-proof.md"
GENERIC_INPUT = ROOT / "tests/fixtures/social_content_studio/generic-input.json"
GENERIC_OUTPUT = ROOT / "tests/fixtures/social_content_studio/generic-output.md"
FAILURE_CONTROLS = ROOT / "tests/fixtures/social_content_studio/failure-controls.json"
CODEX_INVENTORY = ROOT / "semantic_libraries/antigravity/indexes/full-library-inventory.json"


failures: list[str] = []
receipts: list[str] = []


def require(condition: bool, label: str, detail: str = "") -> None:
    if condition:
        receipts.append(label)
    else:
        failures.append(f"{label}: {detail or 'failed'}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def run(*args: str) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )
    return result.returncode, result.stdout + result.stderr


def ranked_routes(output: str) -> list[str]:
    return re.findall(r"^\s*\d+\.\s+`?(/[-a-z0-9]+)`?", output, flags=re.MULTILINE)


def validate_manifest(data: object) -> list[str]:
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["manifest is not an object"]
    if data.get("candidate_count") != 12:
        problems.append("candidate_count must be 12")
    if len(data.get("selected_ids") or []) != 3:
        problems.append("selected_ids must contain three items")
    expected = {
        "voice_taste": "HUMAN_REVIEW_PENDING",
        "publication": "NO_PERMISSION",
        "paid_tools": "NO_PERMISSION",
        "source_package": "GROUNDED",
        "capability": "TRANSFERRED",
        "engagement": "NO_EVENT",
        "demand": "NO_EVENT",
        "revenue": "NO_EVENT",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            problems.append(f"{key} must be {value}")
    return problems


def verify_files() -> None:
    required = (
        SOURCE / "metadata.json",
        SOURCE / "transcript.vtt",
        SOURCE / "transcript.txt",
        SOURCE / "transcript_segments.json",
        SOURCE / "video-context-ledger.md",
        SOURCE / "video-context-ledger.json",
        SOURCE / "frame-notes.md",
        SOURCE / "uncertainty-report.md",
        SOURCE / "analysis.md",
        SOURCE / "mastery-extraction.md",
        WORKFLOW,
        PROMPT,
        CONTRACT,
        DELTA,
        WRAPPER,
        COMMAND_SKILL,
        PILOT,
        MANIFEST,
        BEHAVIOR,
        GENERIC_INPUT,
        GENERIC_OUTPUT,
        FAILURE_CONTROLS,
        CODEX_INVENTORY,
        PILOT_ROOT / "authority-post.md",
        PILOT_ROOT / "linkedin-carousel.md",
        PILOT_ROOT / "short-video.md",
        PILOT_ROOT / "quality-receipt.md",
    )
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    require(not missing, "required files", ", ".join(missing))


def verify_source() -> None:
    code, output = run("execution/verify_video_context_source_package.py", str(SOURCE.relative_to(ROOT)))
    require(code == 0, "source package verifier", output.strip())
    try:
        metadata = json.loads(text(SOURCE / "metadata.json"))
        segments = json.loads(text(SOURCE / "transcript_segments.json"))
        ledger = json.loads(text(SOURCE / "video-context-ledger.json"))
    except json.JSONDecodeError as exc:
        failures.append(f"source JSON parse: {exc}")
        return
    require(metadata.get("id") == "hoVC2W0p0Zg", "source video id")
    require(metadata.get("duration") == 9432, "full-course duration")
    require(len(metadata.get("chapters") or []) == 11, "full chapter coverage")
    require(len(segments) == 4529, "timestamped transcript segments", str(len(segments)))
    require(len(ledger) == 4529, "spoken evidence ledger", str(len(ledger)))
    require(len(list((SOURCE / "frames").rglob("*.jpg"))) == 59, "reviewed frame count")
    require("No OCR engine was run" in text(SOURCE / "uncertainty-report.md"), "visual/OCR evidence boundary")
    mastery = text(SOURCE / "mastery-extraction.md")
    require("## Content Assessment" in mastery, "MES content assessment")
    require(10 <= len(re.findall(r"^### \d+\.", mastery, flags=re.MULTILINE)) <= 20, "MES transferable patterns")
    require("## Hidden Knowledge Revealed" in mastery and mastery.count("- **") >= 5, "MES hidden mechanisms")
    for section in ("### Week 1", "### Week 2", "### Week 3", "### Week 4"):
        require(section in mastery, f"MES cognitive archaeology: {section}")
    for section in ("### 24-Hour Quickstart", "### 7-Day Sprint", "### 30-Day Transformation"):
        require(section in mastery, f"MES adoption path: {section}")
    require("Source-derived" in mastery and "Enhancement" in mastery, "MES source-versus-enhancement labels")


def verify_contract_and_prompt() -> None:
    contract = text(CONTRACT)
    for token in (
        "Source evidence",
        "Objective",
        "Components",
        "Step order",
        "Human checkpoints",
        "Behavior-changing proof",
        "Context policy",
        "Composition Ledger",
        "Agentic Engineering Packet",
    ):
        require(token in contract, f"contract field: {token}")

    prompt = text(PROMPT)
    for section in (
        "## Role & Activation",
        "## Input Required",
        "## Execution Protocol",
        "## Output Contract",
        "## Output Skeleton",
        "## Quality Gate",
        "## Deploy When",
    ):
        require(section in prompt, f"born-v2 section: {section}")
    for token in (
        "Prepare Brain",
        "Person → Tension → Path",
        "10–15",
        "3–5",
        "HUMAN_REVIEW_PENDING",
        "NEEDS_SOURCE",
        "PROVISIONAL",
        "Zero publishing",
    ):
        require(token in prompt, f"prompt invariant: {token}")

    workflow = text(WORKFLOW)
    require("Missing Context Packet" in workflow, "missing-context fail-safe")
    require("Never reactivate `higgsfield-content-factory`" in workflow, "retired Higgsfield veto")
    require("Publishing, scheduling, profile editing, outreach" in workflow, "external-action boundary")
    require("/social-content-studio" in text(SKILL / "SKILL.md"), "Kieran command surface")
    require("source-command-social-content-studio" in text(COMMAND_SKILL), "compatibility command skill")
    delta = text(DELTA)
    for token in (
        "Prepare Brain",
        "Person → Tension → Path",
        "Refusal file",
        "Surplus-selection distinction",
        "Five-stage run",
        "First-week adoption",
        "Portable Model and Tool Adapter Map",
    ):
        require(token in delta, f"source delta: {token}")
    require("references/prompts-v2/social-content-studio.md" in text(SKILL / "SKILL.md"), "generated prompt pointer")
    try:
        inventory = json.loads(text(CODEX_INVENTORY))
    except json.JSONDecodeError as exc:
        failures.append(f"Codex inventory JSON: {exc}")
    else:
        studio = [row for row in inventory.get("workflows", []) if row.get("name") == "social-content-studio"]
        require(len(studio) == 1 and studio[0].get("bridge_status") == "hot bridge", "generated Codex registry entry")


def verify_pilot() -> None:
    pilot = text(PILOT)
    candidates = set(re.findall(r"\bSCS-\d{2}\b", pilot))
    require(len(candidates) == 12, "pilot surplus contains 12 unique candidates", str(sorted(candidates)))
    require(pilot.count("## Review Artifact") == 3, "pilot contains three review artifacts")
    for token in (
        "Context Lock",
        "Content Spine",
        "Refusal File",
        "Selected Week",
        "Evidence and Claim Ledger",
        "HUMAN_REVIEW_PENDING",
        "NO EVENT",
        "DM ANGLE",
    ):
        require(token in pilot, f"pilot invariant: {token}")

    try:
        manifest = json.loads(text(MANIFEST))
    except json.JSONDecodeError as exc:
        failures.append(f"approval manifest JSON: {exc}")
        return
    manifest_problems = validate_manifest(manifest)
    require(not manifest_problems, "approval manifest", "; ".join(manifest_problems))
    require(
        manifest.get("review_artifacts") == ["authority-post.md", "linkedin-carousel.md", "short-video.md"],
        "approval manifest names three review artifacts",
    )

    broken = dict(manifest)
    broken["publication"] = "APPROVED"
    broken["candidate_count"] = 2
    require(bool(validate_manifest(broken)), "manifest negative control catches unsafe state")

    behavior = text(BEHAVIOR)
    require(behavior.count("IMPROVED") >= 5, "behavior proof improves at least five dimensions")
    for token in ("PRESERVED", "TRANSFERRED", "HUMAN_REVIEW_PENDING", "NO EVENT"):
        require(token in behavior, f"behavior proof state: {token}")


def verify_generic_cold_start() -> None:
    try:
        generic = json.loads(text(GENERIC_INPUT))
    except json.JSONDecodeError as exc:
        failures.append(f"generic input JSON: {exc}")
        return
    require(all(generic.get(key) for key in ("seed", "platform", "context")), "generic cold-start required inputs")
    output = text(GENERIC_OUTPUT)
    require("_active/farrice-brand" not in output, "generic cold start has no Farrice path dependency")
    require(len(set(re.findall(r"\bGEN-\d{2}\b", output))) == 10, "generic cold start generates 10 candidates")
    require(output.count("SELECTED") == 3, "generic cold start selects three")
    require("HUMAN_REVIEW_PENDING" in output and "NO_EVENT" in output, "generic proof ceilings")


def verify_failure_controls() -> None:
    try:
        controls = json.loads(text(FAILURE_CONTROLS))
    except json.JSONDecodeError as exc:
        failures.append(f"failure controls JSON: {exc}")
        return
    cases = {case.get("name"): case for case in controls.get("cases", [])}
    expected = {
        "missing_audience_and_offer": "MISSING_CONTEXT_PACKET",
        "unsupported_claim": "NEEDS_SOURCE",
        "stale_performance_evidence": "PROVISIONAL",
        "direct_publish_request": "NO_PERMISSION",
        "paid_higgsfield_request": "NO_PERMISSION",
    }
    require(set(cases) == set(expected), "five failure-control fixtures")
    for name, state in expected.items():
        require(cases.get(name, {}).get("expected") == state, f"failure control: {name}")
    require(
        cases.get("missing_audience_and_offer", {}).get("must_name") == ["audience", "offer"],
        "missing-context fixture names the gaps",
    )
    require(cases.get("paid_higgsfield_request", {}).get("adapter_only") is True, "Higgsfield stays adapter-only")


def verify_routing() -> None:
    code, direct = run("execution/command_menu.py", "search", "/social-content-studio")
    require(code == 0 and ranked_routes(direct)[:1] == ["/social-content-studio"], "direct command routes first", direct[:400])

    code, natural = run(
        "execution/command_menu.py", "search", "turn one idea into a week of on-brand social content"
    )
    require(code == 0 and ranked_routes(natural)[:1] == ["/social-content-studio"], "natural-language command routes first", natural[:400])

    code, lean = run("execution/command_menu.py", "search", "build a lean AI content brain")
    require(code == 0 and "/social-content-studio" in ranked_routes(lean)[:3], "lean-brain route is top-three", lean[:500])

    code, workflow = run(
        "execution/workflow_router.py", "search", "turn one idea into a week of on-brand social content"
    )
    require(
        code == 0 and any("/social-content-studio" in line for line in workflow.splitlines()[:6]),
        "workflow router surfaces studio",
        workflow[:500],
    )

    for query in ("summarize this video", "give me three generic ideas", "library pulse", "publish this social post now"):
        code, output = run("execution/command_menu.py", "search", query)
        require(code == 0 and ranked_routes(output)[:1] != ["/social-content-studio"], f"negative route: {query}", output[:400])


def main() -> int:
    verify_files()
    if not failures:
        verify_source()
        verify_contract_and_prompt()
        verify_pilot()
        verify_generic_cold_start()
        verify_failure_controls()
        verify_routing()

    if failures:
        print("Social Content Studio: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Social Content Studio: PASS ({len(receipts)} checks)")
    print("- source GROUNDED: 4,529 segments + 59 reviewed frames")
    print("- command RUNNABLE: prompt, workflow, wrapper, routing, and failure controls")
    print("- Farrice pilot TRANSFERRED: 12 candidates -> 3 review artifacts")
    print("- taste HUMAN_REVIEW_PENDING; publishing, engagement, demand, revenue NO EVENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
