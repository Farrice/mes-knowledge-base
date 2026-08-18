#!/usr/bin/env python3
"""artifact_placement_hook.py — PostToolUse advisory (Write / Edit / NotebookEdit).

Pure-path heuristic, no artifact_router import (must run <100ms). When a Write
lands a content file directly at the root of _active/<project>/ or
projects/<project>/ — the exact loose-artifact failure prevented by
docs/solutions/2026-07-07-project-artifacts-loose-plus-empty-scaffold.md — it
prints a one-paragraph advisory naming the likely canonical subfolder and the
fix command. NEVER blocks, never exits nonzero, silent on canonical placements.
"""

from __future__ import annotations

import datetime
import json
import os
import re
import sys

# MUST stay in sync with project_filer.EXEMPT_NAMES — verify_project_filer.py
# asserts it. Each of these is a contract with another tool: CANON.md is written
# at the project root by canon_audit, CAMPAIGN.md is read by exact path by
# campaign_beacon, MOVED.md is a relocation pointer that must not move.
PINNED_NAMES = {"INDEX.md", "README.md", "CLAUDE.md", "RISKS.md",
                "GEMINI.md", "AGENTS.md", "CODEX.md", ".gitignore",
                "CANON.md", "CAMPAIGN.md", "MOVED.md"}

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


RECORD_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[-_]")
_VERSION_RE = re.compile(
    r"(-v\d+(\.\d+)?|-final|-draft|-copy|-new|-old|-latest|-master|"
    r"-pop|-clean|-polished|-\d{1,2})$", re.I)


def _slot(stem: str) -> str:
    s = stem.lower()
    while True:
        nxt = _VERSION_RE.sub("", s)
        if nxt == s:
            return nxt
        s = nxt


def slot_collision(file_path: str, name: str) -> str | None:
    """Is this a new undated file competing with a living doc already here?

    The living-vs-record rule (2026-08-07): an undated filename claims the
    LIVING slot, and there is one living doc per slot. Writing a second
    undated file for the same slot is how one project accumulated fourteen
    parallel copies of the same profile — none of them marked, none of them
    obviously current. Say it at the moment it happens; never block.
    """
    if RECORD_RE.match(name) or not name.lower().endswith((".md", ".txt")):
        return None
    d = os.path.dirname(file_path)
    stem = name[: name.rfind(".")]
    slot = _slot(stem)
    try:
        siblings = os.listdir(d)
    except OSError:
        return None
    rivals = []
    for s in siblings:
        if s == name or s in PINNED_NAMES or not s.lower().endswith((".md", ".txt")):
            continue
        if RECORD_RE.match(s):
            continue
        if _slot(s[: s.rfind(".")]) == slot:
            rivals.append(s)
    if not rivals:
        return None
    today = datetime.date.today().isoformat()
    return (
        "LIVING SLOT (deterministic): "
        + ", ".join(f"`{r}`" for r in sorted(rivals)[:3])
        + f" already claim the '{slot}' slot in this folder. An undated filename "
        "means LIVING — one per slot, updated in place. Editing passes and minor "
        "wording do not earn v2/v3/final files. Create a separate document only "
        "when purpose, audience, approval state, or evidence materially changes; "
        f"then lead it with `{today}-` as a milestone record. Never auto-delete."
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    # Edit-on-a-new-path is the most common agent file-creation route; a
    # Write-only matcher left that channel completely uncovered.
    if payload.get("tool_name") not in ("Write", "Edit", "NotebookEdit"):
        return 0

    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
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

    # Living-slot check runs ANYWHERE under _active/ or projects/, not just at
    # a project root — competing versions accumulate inside buckets, which is
    # exactly where the fourteen profile copies were.
    if "_active" in parts or "projects" in parts:
        collision = slot_collision(file_path, name)
        if collision:
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": collision,
            }}))
            return 0

    # Depth check: file must sit exactly one level under _active/<p> or projects/<p>.
    # Resolve the LAST occurrence of the anchor — nested repo copies exist (e.g.
    # _active/harness/codex-harvest-2026-06-11/_active/...) and first-occurrence matching
    # anchored on the outer one, computed the wrong project, and went silent.
    project = None
    project_dir = None
    for anchor in ("_active", "projects"):
        if anchor not in parts:
            continue
        i = len(parts) - 1 - parts[::-1].index(anchor)
        if i + 2 == len(parts) - 1:  # anchor, project, file  (file is last)
            project = parts[i + 1]
            project_dir = "/".join(parts[: i + 2])
            break
    if project is None:
        return 0

    folder = suggest_folder(name)
    # No bare-`mv` fallback: directives/artifact-placement.md forbids it because
    # bare moves orphan every inbound link. The enforcement mechanism must not
    # teach the violation it exists to prevent.
    msg = (
        "ARTIFACT PLACEMENT (deterministic): this file was written loose at the "
        f"root of {project}/. Canonical policy is only-populated numbered "
        f"subfolders — it likely belongs in {folder}/. File it with: "
        f"`python3 execution/project_filer.py plan --project \"{project_dir}\" --out /tmp/p.json` "
        f"then `apply --plan /tmp/p.json --dry-run` to review, then `apply --plan /tmp/p.json`. "
        "Never bare `mv` — it orphans inbound links."
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
