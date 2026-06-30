#!/usr/bin/env python3
"""Verify the Repeatability Spine route, contract, seed evidence, and guards."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import command_menu  # noqa: E402
import routing_governor  # noqa: E402
import workflow_router  # noqa: E402


REPEATABILITY_QUERIES = (
    "I cannot repeat the magic revisions keep failing",
    "the revision got worse and lost the good part",
    "AI Misfire LinkedIn post revision got flat",
    "the route picked the wrong workflow",
    "the patch introduced a regression",
)

REQUIRED_FILES = (
    "semantic_libraries/antigravity/primitives/repeatability-spine-contract.md",
    "docs/mission-artifacts/repeatability-spine/seed-ai-misfire-examples.md",
    ".agent/workflows/repeatability-spine.md",
    ".claude/commands/repeatability-spine.md",
    ".agents/skills/source-command-repeatability-spine/SKILL.md",
)

CONTRACT_REQUIRED_TEXT = (
    "Good example",
    "Failed example",
    "Failure class",
    "Original route",
    "Loaded context",
    "Expert stack",
    "Preservation lock",
    "Revision intent",
    "Changed surface",
    "Validation",
    "Regression guard",
    "Result surface",
    "Reuse hook",
)

SEED_REQUIRED_TEXT = (
    "brain/hybrid-ai-misfire-avatar-content-v1/LINKEDIN-POSTS-V3-VOICE-PROOF.md",
    "brain/hybrid-ai-misfire-avatar-content-v1/archive/readable-artifacts/today-post-copy-ready.txt",
    "brain/hybrid-ai-misfire-avatar-content-v1/V2-TO-V3-CONTENT-AUDIT.md",
    "generic/needy audit outreach",
    "Get Audit Customers Fast",
    "pending external conversation evidence",
)

WORKFLOW_REQUIRED_TEXT = (
    "Preservation Lock",
    "creative revision degradation",
    "wrong workflow/routing",
    "code/workflow regression",
    "/publishable-copy-gate",
    "/system-audit",
    "/self-evolve",
    "/skill-anneal",
    "Replay prompt",
)

PUBLISHABLE_COPY_REQUIRED_TEXT = (
    "Preservation Lock",
    "strongest voice/proof/tension",
)

AUTOPILOT_REQUIRED_TEXT = (
    "/repeatability-spine",
    "repeatability",
    "revision",
)

SYSTEM_AUDIT_REQUIRED_TEXT = (
    "/repeatability-spine",
    "repeatability",
)

CODEX_REQUIRED_TEXT = (
    "/repeatability-spine",
    "verify_repeatability_spine.py",
)


def read_rel(path: str) -> str:
    full = ROOT / path
    if not full.exists():
        raise AssertionError(f"Missing required file: {path}")
    return full.read_text(encoding="utf-8", errors="ignore")


def routes_from_command_menu(query: str) -> list[str]:
    workflows = command_menu.build_index()
    return [workflow.name for _, workflow in command_menu.search(workflows, query, 10)]


def routes_from_workflow_router(query: str) -> list[str]:
    return [workflow["name"] for _, workflow in workflow_router.search_workflows(query, 10)]


def require_text(label: str, text: str, snippets: tuple[str, ...]) -> None:
    missing = [snippet for snippet in snippets if snippet not in text]
    if missing:
        raise AssertionError(f"{label} missing text: {', '.join(missing)}")


def check_files_and_text() -> list[str]:
    for path in REQUIRED_FILES:
        read_rel(path)

    require_text(
        "repeatability contract",
        read_rel("semantic_libraries/antigravity/primitives/repeatability-spine-contract.md"),
        CONTRACT_REQUIRED_TEXT,
    )
    require_text(
        "repeatability seed",
        read_rel("docs/mission-artifacts/repeatability-spine/seed-ai-misfire-examples.md"),
        SEED_REQUIRED_TEXT,
    )
    require_text(
        "repeatability workflow",
        read_rel(".agent/workflows/repeatability-spine.md"),
        WORKFLOW_REQUIRED_TEXT,
    )
    require_text(
        "publishable copy gate",
        read_rel(".agent/workflows/publishable-copy-gate.md"),
        PUBLISHABLE_COPY_REQUIRED_TEXT,
    )
    require_text("autopilot workflow", read_rel(".agent/workflows/autopilot.md"), AUTOPILOT_REQUIRED_TEXT)
    require_text("system audit workflow", read_rel(".agent/workflows/system-audit.md"), SYSTEM_AUDIT_REQUIRED_TEXT)
    require_text("CODEX.md", read_rel("CODEX.md"), CODEX_REQUIRED_TEXT)
    return ["files and required text present"]


def check_routing() -> list[str]:
    results = []
    for query in REPEATABILITY_QUERIES:
        menu = routes_from_command_menu(query)
        router = routes_from_workflow_router(query)
        decision = routing_governor.evaluate(query, menu, router)
        if not menu or menu[0] != "repeatability-spine":
            raise AssertionError(f"command_menu should rank /repeatability-spine first for {query!r}, got {menu[:5]}")
        if not router or router[0] != "repeatability-spine":
            raise AssertionError(f"workflow_router should rank /repeatability-spine first for {query!r}, got {router[:5]}")
        if decision.detected_lane != "repeatability" or decision.chosen_route != "repeatability-spine":
            raise AssertionError(
                f"governor should choose repeatability-spine for {query!r}, "
                f"got lane={decision.detected_lane} route={decision.chosen_route}"
            )
        results.append(f"repeatability route: {query}")

    broad = "things are not working"
    broad_menu = routes_from_command_menu(broad)
    broad_router = routes_from_workflow_router(broad)
    broad_decision = routing_governor.evaluate(broad, broad_menu, broad_router)
    if broad_menu[0] != "autopilot" or broad_router[0] != "autopilot" or broad_decision.chosen_route != "autopilot":
        raise AssertionError("Broad system-failure query must remain on /autopilot")
    results.append("broad system failure remains /autopilot")
    return results


def main() -> int:
    results = []
    results.extend(check_files_and_text())
    results.extend(check_routing())
    print("REPEATABILITY SPINE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
