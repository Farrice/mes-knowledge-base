#!/usr/bin/env python3
"""Verify the Farrice Content OS bridge, state home, and routing integration."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "workflow": ROOT / ".agent" / "workflows" / "farrice-content-os.md",
    "codex_skill": ROOT / ".agents" / "cold-skills" / "source-command-wrappers" / "source-command-farrice-content-os" / "SKILL.md",
    "source_command": ROOT / ".claude" / "commands" / "farrice-content-os.md",
    "state_index": ROOT / "_active" / "farrice-content-os" / "INDEX.md",
    "context_index": ROOT / "_active" / "farrice-content-os" / "context-index.md",
    "research_ledger": ROOT / "_active" / "farrice-content-os" / "research-ledger.md",
    "brandjack_board": ROOT / "_active" / "farrice-content-os" / "brandjack-board.md",
    "hook_lab": ROOT / "_active" / "farrice-content-os" / "hook-lab.md",
    "calendar": ROOT / "_active" / "farrice-content-os" / "content-calendar.md",
    "engagement_list": ROOT / "_active" / "farrice-content-os" / "engagement-list.md",
    "content_card_template": ROOT / "_active" / "farrice-content-os" / "templates" / "content-card-template.md",
    "first_output_template": ROOT / "_active" / "farrice-content-os" / "content-packs" / "first-output-package-template.md",
    "cold_start_fixture": ROOT / "_active" / "farrice-content-os" / "content-packs" / "cold-start-fixture.md",
    "service_offer": ROOT / "_active" / "farrice-content-os" / "service-package" / "ai-content-os-offer-skeleton.md",
    "diandra_system": ROOT / ".agent" / "workflows" / "diandra-linkedin-system.md",
    "diandra_content": ROOT / ".agent" / "workflows" / "diandra-content-engine.md",
    "diandra_growth": ROOT / ".agent" / "workflows" / "diandra-growth-sprint.md",
    "diandra_remix": ROOT / ".agent" / "workflows" / "diandra-steal-and-remix.md",
    "writers_room": ROOT / ".agent" / "workflows" / "writers-room.md",
    "high_taste": ROOT / ".agent" / "workflows" / "high-taste-writing-os.md",
    "voice_first": ROOT / ".agent" / "workflows" / "voice-first-content.md",
    "anti_slop": ROOT / ".agent" / "workflows" / "anti-slop-audit.md",
    "publishable_gate": ROOT / ".agent" / "workflows" / "publishable-copy-gate.md",
}

WORKFLOW_TERMS = [
    "Diandra",
    "Context Lock",
    "Brandjack Opportunity Board",
    "Hook Room",
    "One composer owns the final voice",
    "Content Card Interface",
    "_active/farrice-content-os",
    "/writers-room",
    "/high-taste-writing-os",
    "/voice-first-content",
    "/anti-slop-audit",
    "/publishable-copy-gate",
    "35%",
    "local-first",
]

STATE_TERMS = {
    "context_index": ["FARRICE.md", "_active/farrice-brand", "writers-room", "Missing Context Ledger"],
    "research_ledger": ["No research claim advances without", "Unavailable-State Notes"],
    "brandjack_board": ["Brandjack", "Newsjack", "Namejack", "Originality Note"],
    "hook_lab": ["At least 10 hook candidates", "Top 3", "Anti-Slop"],
    "calendar": ["7", "Authority", "copy_gate", "service_ready"],
    "content_card_template": ["raw_source", "hook_candidates", "taste_evidence", "engagement_plan"],
    "first_output_template": ["20 content cards", "7 Growth", "At least 3 Growth cards"],
    "cold_start_fixture": ["FCO-FIXTURE-001", "research --brandjack", "status: captured"],
    "service_offer": ["Offer One-Liner", "20-post sprint", "Hook Lab", "Proof Plan"],
}

ROUTING_QUERIES = [
    "Farrice content OS raw concepts voice taste brandjacking hooks",
    "content done end to end Farrice writers room anti slop Diandra",
    "brandjack research hook room personal branding content operating system",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def run(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def main() -> int:
    failures: list[str] = []

    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")

    if FILES["workflow"].exists():
        content = read(FILES["workflow"])
        for term in WORKFLOW_TERMS:
            if term not in content:
                failures.append(f"workflow missing term: {term}")

    for label, terms in STATE_TERMS.items():
        path = FILES[label]
        if not path.exists():
            continue
        content = read(path)
        for term in terms:
            if term not in content:
                failures.append(f"{label} missing term: {term}")

    skill = read(FILES["codex_skill"]) if FILES["codex_skill"].exists() else ""
    if ".agent/workflows/farrice-content-os.md" not in skill:
        failures.append("codex skill missing workflow command template")

    source_command = read(FILES["source_command"]) if FILES["source_command"].exists() else ""
    if ".agent/workflows/farrice-content-os.md" not in source_command:
        failures.append("source command missing workflow bridge")

    for query in ROUTING_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        combined = menu + "\n" + router
        if "/farrice-content-os" not in combined:
            failures.append(f"routing query did not surface /farrice-content-os: {query}")

    if failures:
        print("Farrice Content OS verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Farrice Content OS verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
