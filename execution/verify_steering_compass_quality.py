#!/usr/bin/env python3
"""Verify Insightful Momentum steering quality."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
GLOBAL_AGENTS = Path("/Users/farricecain/.codex/AGENTS.md")
GLOBAL_END_SESSION = Path("/Users/farricecain/.codex/skills/end-session/SKILL.md")

ACTIVE_REFERENCES = [
    "semantic_libraries/antigravity/primitives/high-floor-operator-os.md",
    "semantic_libraries/antigravity/primitives/collaborative-steering-compass.md",
    "semantic_libraries/antigravity/references/no-lazy-path-gate.md",
    "semantic_libraries/antigravity/references/frontier-followup-patterns.md",
    "semantic_libraries/antigravity/primitive-map.md",
]

REQUIRED_FIELDS = [
    "followup_title",
    "suggestion_family",
    "frontier_pattern",
    "when_to_use",
    "operator_insight",
    "hidden_gap_opportunity",
    "capability_revealed",
    "prompt",
    "entails",
    "expected_output",
    "quality_bar",
    "skip_if",
    "suggested_skills",
]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def fail(message: str) -> None:
    raise AssertionError(message)


def payload(objective: str) -> dict[str, Any]:
    proc = run([sys.executable, "execution/contextual_next_prompts.py", "--objective", objective, "--json"])
    if proc.returncode != 0:
        fail(f"contextual_next_prompts failed for {objective!r}: {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def check_active_references() -> None:
    for rel in ACTIVE_REFERENCES:
        path = ROOT / rel
        if not path.exists():
            fail(f"Missing active steering reference: {rel}")
        text = path.read_text(encoding="utf-8")
        if "Insightful Momentum" not in text and "No-Lazy-Path" not in text and "High-Floor" not in text:
            fail(f"Active steering reference is not load-bearing: {rel}")
    workflow = (ROOT / ".agent/workflows/steering-compass.md").read_text(encoding="utf-8")
    for rel in ACTIVE_REFERENCES:
        if rel not in workflow and rel.split("/", 1)[1] not in workflow:
            fail(f"steering-compass workflow does not point at {rel}")


def check_prompt_payload(objective: str, expected_work_type: str) -> None:
    data = payload(objective)
    if data.get("work_type") != expected_work_type:
        fail(f"{objective!r} expected work_type {expected_work_type}, got {data.get('work_type')}")
    prompts = data.get("prompts", [])
    if [item.get("name") for item in prompts] != ["Use Now", "Harden", "Expand"]:
        fail(f"{objective!r} did not preserve Use Now/Harden/Expand")
    rendered = json.dumps(data).lower()
    forbidden = ["continue the strongest next step"]
    found = [term for term in forbidden if term in rendered]
    if found:
        fail(f"{objective!r} contains generic continuation language: {', '.join(found)}")
    for item in prompts:
        missing = [field for field in REQUIRED_FIELDS if field not in item]
        if missing:
            fail(f"{objective!r} {item.get('name')} missing fields: {', '.join(missing)}")
        if len(str(item.get("followup_title", "")).split()) < 5:
            fail(f"{objective!r} {item.get('name')} has weak followup_title")
        for field in ("operator_insight", "hidden_gap_opportunity", "capability_revealed"):
            if len(str(item.get(field, "")).split()) < 6:
                fail(f"{objective!r} {item.get('name')} has weak {field}")
        if not item.get("suggested_skills"):
            fail(f"{objective!r} {item.get('name')} has no suggested workflows")


def check_markdown_fields() -> None:
    proc = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--objective",
            "improve 3 Next Prompts so they teach, reveal capabilities, and push creative momentum",
        ]
    )
    if proc.returncode != 0:
        fail(f"contextual_next_prompts markdown failed: {proc.stderr.strip()}")
    text = proc.stdout
    for needle in (
        "## 3 Next Prompts",
        "Suggested follow-ups",
        "What it entails",
        "Output/Capability Move",
        "Operator Insight",
        "Hidden Gap/Opportunity",
        "Capability Revealed",
        "Suggested skills/workflows",
    ):
        if needle not in text:
            fail(f"Markdown output missing {needle!r}")


def check_artifact_followup_shape() -> None:
    data = payload("DWA Faceless Affiliate Strategy Playbook")
    if data.get("work_type") != "artifact_followup":
        fail(f"DWA playbook expected artifact_followup, got {data.get('work_type')}")
    titles = " ".join(item.get("followup_title", "") for item in data.get("prompts", [])).lower()
    for needle in ("content assets", "reusable", "launch"):
        if needle not in titles:
            fail(f"artifact followups missing {needle!r}: {titles}")
    routes = [item.get("route") for item in data.get("prompts", [])]
    if routes != ["creative-assembly", "source-to-skill-system", "campaign-architect"]:
        fail(f"DWA playbook followups chose weak routes: {routes}")

    portfolio = payload("Creative Strategist portfolio")
    portfolio_titles = " ".join(item.get("followup_title", "") for item in portfolio.get("prompts", [])).lower()
    for needle in ("presentation script", "slides", "webpage"):
        if needle not in portfolio_titles:
            fail(f"portfolio followups missing {needle!r}: {portfolio_titles}")
    portfolio_routes = [item.get("route") for item in portfolio.get("prompts", [])]
    if portfolio_routes != ["creative-assembly", "design-brief", "design-first-build"]:
        fail(f"portfolio followups chose weak routes: {portfolio_routes}")

    opportunity = payload("Blue Ocean Voids")
    opportunity_titles = " ".join(item.get("followup_title", "") for item in opportunity.get("prompts", [])).lower()
    for needle in ("specific opportunities", "arbitrage paths", "strategic deck"):
        if needle not in opportunity_titles:
            fail(f"opportunity followups missing {needle!r}: {opportunity_titles}")
    opportunity_routes = [item.get("route") for item in opportunity.get("prompts", [])]
    if opportunity_routes != ["business-intelligence", "deep-research", "campaign-architect"]:
        fail(f"opportunity followups chose weak routes: {opportunity_routes}")

    prompt = payload("Generate content assets for X using the provided Meta Prompt")
    prompt_titles = " ".join(item.get("followup_title", "") for item in prompt.get("prompts", [])).lower()
    for needle in ("content assets for x", "reusable prompt workflow", "test sprint"):
        if needle not in prompt_titles:
            fail(f"prompt followups missing {needle!r}: {prompt_titles}")
    prompt_routes = [item.get("route") for item in prompt.get("prompts", [])]
    if prompt_routes != ["creative-assembly", "convert-prompt", "auto-experiment"]:
        fail(f"prompt followups chose weak routes: {prompt_routes}")

    dashboard = payload("Analytics dashboard with revenue metrics")
    dashboard_titles = " ".join(item.get("followup_title", "") for item in dashboard.get("prompts", [])).lower()
    for needle in ("insight brief", "metric quality", "executive dashboard"):
        if needle not in dashboard_titles:
            fail(f"dashboard followups missing {needle!r}: {dashboard_titles}")

    website = payload("AI website prototype")
    website_titles = " ".join(item.get("followup_title", "") for item in website.get("prompts", [])).lower()
    for needle in ("usable prototype", "ux", "launchable product"):
        if needle not in website_titles:
            fail(f"website followups missing {needle!r}: {website_titles}")


def check_frontier_payload_fields() -> None:
    data = payload("Creative Strategist portfolio")
    families = {item.get("suggestion_family") for item in data.get("prompts", [])}
    if not families.intersection({"Transform", "Ship", "Compound", "Deepen"}):
        fail(f"missing useful suggestion families: {families}")
    rendered = json.dumps(data).lower()
    for needle in ("output-first", "manus/genspark", "capability", "information-gap"):
        if needle not in rendered:
            fail(f"frontier payload missing {needle!r}")


def check_session_closeout_shape() -> None:
    data = payload("end-session closeout after global operator steering bridge repair")
    if data.get("work_type") != "session_closeout":
        fail(f"end-session closeout expected session_closeout, got {data.get('work_type')}")
    titles = " ".join(item.get("followup_title", "") for item in data.get("prompts", [])).lower()
    for needle in ("fresh-session smoke test", "global end-session mirrors", "unrelated blocked closeout"):
        if needle not in titles:
            fail(f"end-session followups missing {needle!r}: {titles}")
    routes = [item.get("route") for item in data.get("prompts", [])]
    if routes != ["repeatability-spine", "system-audit", "repeatability-spine"]:
        fail(f"end-session followups chose weak routes: {routes}")
    markdown = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--objective",
            "end-session closeout after global operator steering bridge repair",
            "--format",
            "compact",
        ]
    )
    if markdown.returncode != 0:
        fail(f"end-session markdown failed: {markdown.stderr.strip()}")
    if markdown.stdout.count("**Prompt:**") != 3:
        fail("compact end-session markdown must contain exactly three Prompt lines")
    for needle in (
        "Output/Capability Move",
        "Operator Insight",
        "Hidden Gap/Opportunity",
        "Capability Revealed",
        "**Use Now**",
        "**Harden**",
        "**Expand**",
    ):
        if needle in markdown.stdout:
            fail(f"compact end-session markdown leaks retired label {needle!r}")
    if "/end-session" in markdown.stdout:
        fail("compact completed closeout routes back into /end-session")


def check_execute_next_unchanged() -> None:
    proc = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--stage",
            "execute-next",
            "--objective",
            "run the safe local next action",
        ]
    )
    if proc.returncode != 0:
        fail(f"execute-next failed: {proc.stderr.strip()}")
    text = proc.stdout
    for needle in ("## Local Next Action", "patch_and_verify", "First command", "Verifier"):
        if needle not in text:
            fail(f"execute-next output missing {needle!r}")


def check_router_probe() -> None:
    proc = run(
        [
            sys.executable,
            "execution/workflow_router.py",
            "search",
            "three next prompts should teach insights reveal capabilities and push creative momentum",
        ]
    )
    if proc.returncode != 0:
        fail(f"workflow_router failed: {proc.stderr.strip()}")
    first = ""
    for line in proc.stdout.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            first = stripped.split()[0].lstrip("/")
            break
    if first != "steering-compass":
        fail(f"router expected /steering-compass, got /{first or 'none'}")


def check_global_bridge() -> None:
    if not GLOBAL_AGENTS.exists():
        fail(f"Missing global AGENTS: {GLOBAL_AGENTS}")
    text = GLOBAL_AGENTS.read_text(encoding="utf-8")
    # The global bridge intentionally carries the compact current contract.
    # Rich renderer fields remain verified below in the end-session skill and
    # contextual_next_prompts.py; requiring them here fossilizes old headings.
    for needle in (
        "Three Contextual Next Prompts",
        "exactly three",
        "ranked, session-specific",
        "If the best next action is safe, local, and already authorized, execute it",
        "Compact Operator Lesson",
        "Operator move:",
        "Global Execution Bias Contract",
        "Patch + Verify",
    ):
        if needle not in text:
            fail(f"Global AGENTS missing {needle!r}")
    if not GLOBAL_END_SESSION.exists():
        fail(f"Missing global end-session skill: {GLOBAL_END_SESSION}")
    end_session = GLOBAL_END_SESSION.read_text(encoding="utf-8")
    for needle in (
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/end-session.md",
        "thin compatibility wrapper",
        "contextual_next_prompts.py",
    ):
        if needle not in end_session:
            fail(f"Global end-session skill missing {needle!r}")


def main() -> int:
    checks = [
        check_active_references,
        lambda: check_prompt_payload(
            "improve 3 Next Prompts so they teach, reveal capabilities, and push creative momentum",
            "system_operator",
        ),
        lambda: check_prompt_payload("build a client-facing content system", "revenue_client"),
        check_artifact_followup_shape,
        check_frontier_payload_fields,
        check_session_closeout_shape,
        check_markdown_fields,
        check_execute_next_unchanged,
        check_router_probe,
        check_global_bridge,
    ]
    failures: list[str] = []
    for check in checks:
        try:
            check()
        except Exception as exc:  # noqa: BLE001 - verifier reports all failures.
            failures.append(f"{getattr(check, '__name__', 'check')}: {exc}")
    if failures:
        print("STEERING COMPASS QUALITY VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("STEERING COMPASS QUALITY VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
