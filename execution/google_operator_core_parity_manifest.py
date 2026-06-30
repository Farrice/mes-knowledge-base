#!/usr/bin/env python3
"""Build a Codex-to-Google operator parity manifest.

The manifest is cold by design: it records gaps and review candidates without
turning every Codex command into a live Google route. Hot promotion remains
limited to the operator-core front doors verified by verify_google_operator_core.py.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


GOOGLE_ROOT = Path(__file__).resolve().parent.parent
CODEX_ROOT = Path("/Users/farricecain/Codex Antigravity")
OUT_DIR = GOOGLE_ROOT / "_active" / "operator-core-backport"
OUT_JSON = OUT_DIR / "codex-to-google-parity-manifest.json"
OUT_MD = OUT_DIR / "codex-to-google-parity-manifest.md"

HOT_ROUTES = [
    "mission",
    "source-to-skill-system",
    "orchestrate",
    "repeatability-spine",
    "knowledge-librarian",
    "expert-composition-governor",
    "extraction-governor-agent",
    "steering-compass",
    "system-audit",
]


def list_stems(root: Path, rel: str, glob: str = "*.md") -> set[str]:
    directory = root / rel
    if not directory.exists():
        return set()
    return {path.stem for path in directory.glob(glob) if path.is_file()}


def list_source_commands(root: Path) -> set[str]:
    skills = root / ".agents" / "skills"
    if not skills.exists():
        return set()
    result: set[str] = set()
    for path in skills.glob("source-command-*/SKILL.md"):
        result.add(path.parent.name.removeprefix("source-command-"))
    return result


def sorted_list(values: Iterable[str]) -> list[str]:
    return sorted(set(values))


def classify(source: set[str], target: set[str]) -> dict[str, list[str]]:
    missing = source - target
    collisions = source & target
    return {
        "missing_in_google": sorted_list(missing),
        "collision_review_candidates_google_authority": sorted_list(collisions),
    }


def build_manifest() -> dict[str, object]:
    codex_workflows = list_stems(CODEX_ROOT, ".agent/workflows")
    google_workflows = list_stems(GOOGLE_ROOT, ".agent/workflows")
    codex_commands = list_stems(CODEX_ROOT, ".claude/commands")
    google_commands = list_stems(GOOGLE_ROOT, ".claude/commands")
    codex_source_commands = list_source_commands(CODEX_ROOT)
    google_source_commands = list_source_commands(GOOGLE_ROOT)

    workflow_gap = classify(codex_workflows, google_workflows)
    command_gap = classify(codex_commands, google_commands)
    source_command_gap = classify(codex_source_commands, google_source_commands)

    cold_candidates = sorted_list(
        set(workflow_gap["missing_in_google"])
        | set(command_gap["missing_in_google"])
        | set(source_command_gap["missing_in_google"])
    )
    hot_status = {}
    for route in HOT_ROUTES:
        hot_status[route] = {
            "workflow": route in google_workflows,
            "claude_command": route in google_commands,
            "source_command": route in google_source_commands,
        }

    return {
        "schema_version": "google-operator-core-parity/v1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_root": str(CODEX_ROOT),
        "target_root": str(GOOGLE_ROOT),
        "policy": {
            "hot_promotion": HOT_ROUTES,
            "collision_rule": "Google remains authority; Codex collisions are review candidates, not overwrites.",
            "cold_rule": "Missing non-hot Codex surfaces stay cold-review candidates until intentionally promoted.",
            "forbidden_side_effects": [
                "no Codex Antigravity writes",
                "no global ~/.codex writes",
                "no external writes",
                "no real Codex subagents",
            ],
        },
        "counts": {
            "codex_workflows": len(codex_workflows),
            "google_workflows": len(google_workflows),
            "codex_claude_commands": len(codex_commands),
            "google_claude_commands": len(google_commands),
            "codex_source_commands": len(codex_source_commands),
            "google_source_commands": len(google_source_commands),
            "cold_candidates": len(cold_candidates),
        },
        "hot_status": hot_status,
        "workflow_gap": workflow_gap,
        "claude_command_gap": command_gap,
        "source_command_gap": source_command_gap,
        "cold_router_discoverable_candidates": cold_candidates,
    }


def render_markdown(manifest: dict[str, object]) -> str:
    counts = manifest["counts"]  # type: ignore[index]
    hot_status = manifest["hot_status"]  # type: ignore[index]
    lines = [
        "# Codex To Google Parity Manifest",
        "",
        f"- Generated: {manifest['generated_at']}",
        f"- Source: {manifest['source_root']}",
        f"- Target: {manifest['target_root']}",
        "- Policy: core routes hot; broader gaps cold; Google collisions remain authority.",
        "",
        "## Counts",
    ]
    for key, value in counts.items():  # type: ignore[union-attr]
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Hot Status"])
    for route, status in hot_status.items():  # type: ignore[union-attr]
        flags = ", ".join(f"{name}={value}" for name, value in status.items())
        lines.append(f"- /{route}: {flags}")
    lines.extend(
        [
            "",
            "## Cold Candidate Rule",
            "",
            "The JSON manifest contains the complete cold candidate list. These are discoverable for review but are not live-promoted until conflict checks, local route proof, and verifier coverage exist.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Codex-to-Google operator parity manifest.")
    parser.add_argument("--write", action="store_true", help="Write manifest JSON and Markdown into _active/operator-core-backport.")
    args = parser.parse_args()

    manifest = build_manifest()
    if args.write:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        OUT_JSON.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_MD.write_text(render_markdown(manifest), encoding="utf-8")
        print(str(OUT_JSON))
        print(str(OUT_MD))
    else:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
