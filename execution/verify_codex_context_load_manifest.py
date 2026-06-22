#!/usr/bin/env python3
"""Verify Codex Context Load Manifest behavior for critical Antigravity routes."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT = REPO_ROOT / ".codex" / "tools" / "codex_orchestration_preflight.py"


GOLDENS = [
    {
        "name": "system pain routes to system-audit",
        "intent": "Codex is not firing the right workflows and is missing the full skill loading stack",
        "mode": "system",
        "workflow": "system-audit",
        "must_include": [
            ".agent/workflows/system-audit.md",
            ".agents/skills/source-command-system-audit/SKILL.md",
            "/Users/farricecain/.codex/skills/system-audit/SKILL.md",
        ],
    },
    {
        "name": "lost magic routes to repeatability-spine",
        "intent": "The revision got worse and lost the magic from the good version",
        "mode": "system",
        "workflow": "repeatability-spine",
        "must_include": [
            ".agent/workflows/repeatability-spine.md",
            ".agents/skills/source-command-repeatability-spine/SKILL.md",
            "/Users/farricecain/.codex/skills/repeatability-spine/SKILL.md",
        ],
    },
    {
        "name": "source system routes to source-to-skill-system",
        "intent": "Turn this source material into a reusable connected skill system and workflow bridge",
        "mode": "system",
        "workflow": "source-to-skill-system",
        "must_include": [
            ".agent/workflows/source-to-skill-system.md",
            ".agents/skills/source-command-source-to-skill-system/SKILL.md",
            "/Users/farricecain/.codex/skills/source-to-skill-system/SKILL.md",
        ],
    },
    {
        "name": "knowledge pulse routes to knowledge-librarian",
        "intent": "Run a knowledge pulse and show prior decisions plus sleeping giants",
        "mode": "system",
        "workflow": "knowledge-librarian",
        "must_include": [
            ".agent/workflows/knowledge-librarian.md",
            ".agents/skills/source-command-knowledge-librarian/SKILL.md",
            "/Users/farricecain/.codex/skills/knowledge-librarian/SKILL.md",
        ],
    },
    {
        "name": "linkedin content loads real owner skill files",
        "intent": "Create a LinkedIn content packet for health and wellness brands from zero proof",
        "mode": "deliverable",
        "workflow": "content-sprint",
        "must_include": [
            "skills/lara-acosta-linkedin-mastery/SKILL.md",
            "skills/lara-acosta-linkedin-mastery/genius.md",
            "skills/lara-acosta-linkedin-mastery/workflows/high-performance-content-engine.md",
        ],
    },
]


def _load_preflight() -> Any:
    spec = importlib.util.spec_from_file_location("codex_orchestration_preflight", PREFLIGHT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {PREFLIGHT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _paths(packet: dict[str, Any]) -> set[str]:
    manifest = packet["context_load_manifest"]
    return {str(item.get("path")) for item in manifest.get("must_read_before_output", [])}


def main() -> int:
    preflight = _load_preflight()
    failures: list[str] = []

    for case in GOLDENS:
        packet = preflight.build_packet(case["intent"], case["mode"])
        manifest = packet["context_load_manifest"]
        workflow = manifest["owner_workflow"]
        paths = _paths(packet)

        if workflow != case["workflow"]:
            failures.append(f"{case['name']}: expected /{case['workflow']}, got /{workflow}")

        for required in case["must_include"]:
            if required not in paths:
                failures.append(f"{case['name']}: missing manifest path {required}")

        if manifest["status"] != "PASS":
            missing = ", ".join(item["path"] for item in manifest.get("missing_required", []))
            warnings = "; ".join(manifest.get("warnings", []))
            failures.append(f"{case['name']}: manifest {manifest['status']} missing=[{missing}] warnings=[{warnings}]")

    if failures:
        print("FAIL verify_codex_context_load_manifest")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"PASS verify_codex_context_load_manifest ({len(GOLDENS)} golden routes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
