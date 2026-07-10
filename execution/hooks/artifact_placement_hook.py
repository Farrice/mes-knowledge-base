#!/usr/bin/env python3
"""artifact_placement_hook.py — PostToolUse advisory (Write only).

Pure-path heuristic, no artifact_router import (must run <100ms). When a Write
lands a content file directly at the root of _active/<project>/ or
projects/<project>/ — the exact loose-artifact failure prevented by
docs/solutions/2026-07-07-project-artifacts-loose-plus-empty-scaffold.md — it
prints a one-paragraph advisory naming the likely canonical subfolder and the
fix command. NEVER blocks, never exits nonzero, silent on canonical placements.
"""

from __future__ import annotations

import json
import sys

PINNED_NAMES = {"INDEX.md", "README.md", "CLAUDE.md", "RISKS.md",
                "GEMINI.md", "AGENTS.md", "CODEX.md", ".gitignore"}

CONTENT_SUFFIXES = {".md", ".txt", ".html", ".htm", ".pdf", ".png", ".svg",
                    ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov", ".docx",
                    ".csv", ".json"}

EXPORT_SUFFIXES = {".pdf", ".docx", ".html", ".htm"}
ASSET_SUFFIXES = {".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov"}


def suggest_folder(name: str) -> str:
    lower = name.lower()
    dot = lower.rfind(".")
    suffix = lower[dot:] if dot != -1 else ""
    if suffix in EXPORT_SUFFIXES:
        return "90-exports"
    if suffix in ASSET_SUFFIXES:
        return "05-assets"
    if any(k in lower for k in ("research", "analysis", "market", "benchmark", "landscape")):
        return "02-research"
    if any(k in lower for k in ("transcript", "raw", "source", "intake", "capture")):
        return "01-source"
    if any(k in lower for k in ("draft", "wip", "working", "variant")):
        return "03-working-drafts"
    if suffix == ".md":
        return "04-deliverables"
    return "01-source"


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    if payload.get("tool_name") != "Write":
        return 0

    file_path = (payload.get("tool_input") or {}).get("file_path") or ""
    if not file_path:
        return 0

    parts = file_path.replace("\\", "/").split("/")
    name = parts[-1] if parts else ""
    if name in PINNED_NAMES or name.startswith("."):
        return 0

    dot = name.rfind(".")
    suffix = name[dot:].lower() if dot != -1 else ""
    if suffix not in CONTENT_SUFFIXES:
        return 0

    # depth check: file must sit exactly one level under _active/<p> or projects/<p>
    project = None
    for anchor in ("_active", "projects"):
        if anchor in parts:
            i = parts.index(anchor)
            if i + 2 == len(parts) - 1:  # anchor, project, file  (file is last)
                project = parts[i + 1]
            break
    if project is None:
        return 0

    folder = suggest_folder(name)
    msg = (
        "ARTIFACT PLACEMENT (deterministic): this file was written loose at the "
        f"root of {project}/. Canonical policy is only-populated numbered "
        f"subfolders — it likely belongs in {folder}/. File it with "
        f"`python3 execution/project_filer.py plan --project {project}` then "
        f"`apply`, or move it directly: `mv \"{file_path}\" \"$(dirname \"{file_path}\")/{folder}/\"`."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
