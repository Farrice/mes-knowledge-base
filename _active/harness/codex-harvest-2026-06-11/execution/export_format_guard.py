#!/usr/bin/env python3
"""Flag unrequested export formats for written deliverables.

Written work should default to rendered conversation documents.
Markdown may be used as a local source/persistence copy, but .docx, HTML/browser pages,
Canva/Google Docs/PDF-style exports should only appear when the user explicitly
asked for them.

This guard focuses on local files that are likely to be written deliverables:
document-artifacts/readable-artifacts folders and common deliverable
directories. Archived exports are ignored so old deprecated assets can be kept
without polluting the active sprint surface.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_PATHS = (
    "_active",
    "brain",
    "deliverables",
    "research_outputs",
    "strategy_briefs",
)

BLOCKED_SUFFIXES = {
    ".docx",
    ".html",
    ".htm",
}

ARCHIVE_DIR_NAMES = {
    "archive",
    "_archive",
    "archived",
    "deprecated",
}

APPROVAL_KEYS = {
    "explicitExportRequest",
    "explicit_export_request",
    "userRequestedExport",
    "user_requested_export",
}


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(p for p in path.rglob("*") if p.is_file())
    return sorted(files)


def is_written_artifact_area(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    if "document-artifacts" in parts:
        return True
    if "readable-artifacts" in parts:
        return True
    return False


def is_archived(path: Path) -> bool:
    return any(part.lower() in ARCHIVE_DIR_NAMES for part in path.parts)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def approval_paths(path: Path) -> list[Path]:
    return [
        path.with_name(path.name + ".metadata.json"),
        path.with_suffix(path.suffix + ".metadata.json"),
        path.with_suffix(".metadata.json"),
        path.parent / ".export-approval.json",
    ]


def has_explicit_approval(path: Path) -> bool:
    for approval_path in approval_paths(path):
        if not approval_path.exists():
            continue
        data = read_json(approval_path)
        if any(data.get(key) is True for key in APPROVAL_KEYS):
            return True
        exports = data.get("approvedExports")
        if isinstance(exports, list) and path.suffix.lower().lstrip(".") in {
            str(item).lower().lstrip(".") for item in exports
        }:
            return True
    return False


def should_flag(path: Path) -> bool:
    if path.suffix.lower() not in BLOCKED_SUFFIXES:
        return False
    if is_archived(path):
        return False
    if not is_written_artifact_area(path):
        return False
    return not has_explicit_approval(path)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag .docx/HTML exports in written artifact areas unless explicitly approved."
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to scan.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON.",
    )
    args = parser.parse_args()

    paths = [Path(p) for p in args.paths] if args.paths else [Path(p) for p in DEFAULT_PATHS]
    flagged = [p for p in iter_files(paths) if should_flag(p)]

    if args.json:
        print(
            json.dumps(
                {
                    "status": "fail" if flagged else "pass",
                    "flagged": [str(path) for path in flagged],
                    "rule": "Written deliverables must not create .docx or HTML exports without explicit request metadata.",
                },
                indent=2,
            )
        )
    elif not flagged:
        print("No unrequested written export formats found.")
    else:
        print(f"Found {len(flagged)} unrequested written export format(s):")
        for path in flagged:
            print(f"- {path}")
        print("\nAdd explicit sidecar approval only when the user requested that export:")
        print('  {"explicitExportRequest": true, "approvedExports": ["docx"]}')

    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
