#!/usr/bin/env python3
"""Guard written deliverables against misleading artifact-surface language.

The observable contract is:
- Rendered Conversation Document: readable content shown directly in chat.
- Local Markdown Source: saved `.md` persistence copy.
- External Export: .docx, HTML, Canva, Google Docs, Notion, PDF, or similar.

This guard keeps active written source areas from calling Markdown files the
readable surface, using native-artifact wording without explicit verification,
or omitting sidecar metadata that states how the source should be used.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


DEFAULT_PATHS = (
    "_active",
    "brain",
    "deliverables",
    "research_outputs",
    "strategy_briefs",
)

ARCHIVE_DIR_NAMES = {
    "archive",
    "_archive",
    "archived",
    "deprecated",
}

TEXT_SUFFIXES = {
    ".md",
    ".json",
}

REQUIRED_METADATA = {
    "userFacingSurface": "rendered-conversation-document",
    "sourceRole": "persistence-copy",
}

NATIVE_TOOL_VERIFICATION_KEYS = {
    "nativeArtifactToolVerified",
    "nativeRendererToolInvoked",
    "codexArtifactToolInvoked",
}

MISLEADING_PATTERNS = (
    (
        re.compile(r"\bnative\s+Codex\s+artifact\s+source(?:s| files?)?\b", re.IGNORECASE),
        "Do not label a Local Markdown Source as a Codex-created artifact surface.",
    ),
    (
        re.compile(r"\bnative\s+artifact\s+(?:source|files?)\b", re.IGNORECASE),
        "Do not label a Local Markdown Source as a tool-created artifact surface.",
    ),
    (
        re.compile(r"\bopen\s+the\s+native\s+artifact\b", re.IGNORECASE),
        "Do not point the user to a tool-created surface unless that tool was invoked.",
    ),
    (
        re.compile(r"\bopen\s+the\s+native\s+controlled\s+demo\s+artifact\b", re.IGNORECASE),
        "Do not describe a Markdown source as a tool-created controlled demo surface.",
    ),
    (
        re.compile(r"\bopen\s+the\s+native\b[^\n]*\bartifact\b", re.IGNORECASE),
        "Do not point to a saved source copy as a tool-created surface.",
    ),
    (
        re.compile(r"\breadable\s+artifact\s+source\b", re.IGNORECASE),
        "Do not blend readable-surface language with source-copy language.",
    ),
    (
        re.compile(r"\brenderingIntent\"\s*:\s*\"native-codex-artifact\"", re.IGNORECASE),
        "Replace aspirational renderingIntent metadata with explicit surface fields.",
    ),
    (
        re.compile(r"\bopen\s+(?:the\s+)?raw\s+Markdown\b", re.IGNORECASE),
        "Do not make raw Markdown the primary review path.",
    ),
)

NATIVE_ARTIFACT_LANGUAGE_RE = re.compile(
    r"\bnative\s+(?:Codex\s+)?artifact\b|\bCodex\s+native\s+artifact\b",
    re.IGNORECASE,
)


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


def iter_markdown(paths: Iterable[Path]) -> list[Path]:
    return sorted(path for path in paths if path.suffix.lower() == ".md")


def is_archived(path: Path) -> bool:
    return any(part.lower() in ARCHIVE_DIR_NAMES for part in path.parts)


def is_written_artifact_area(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    return "document-artifacts" in parts or "readable-artifacts" in parts


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def sidecar_paths(path: Path) -> list[Path]:
    return [
        path.with_name(path.name + ".metadata.json"),
        path.with_suffix(path.suffix + ".metadata.json"),
        path.with_suffix(".metadata.json"),
    ]


def sidecar_data(path: Path) -> tuple[Path | None, dict]:
    for sidecar in sidecar_paths(path):
        if sidecar.exists():
            return sidecar, read_json(sidecar)
    return None, {}


def has_native_tool_verification(path: Path) -> bool:
    _, data = sidecar_data(path)
    return any(data.get(key) is True for key in NATIVE_TOOL_VERIFICATION_KEYS)


def line_number(text: str, start: int) -> int:
    return text.count("\n", 0, start) + 1


def scan_language(files: Iterable[Path]) -> list[dict]:
    flagged: list[dict] = []
    for path in files:
        if is_archived(path) or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = read_text(path)
        if not text:
            continue
        for regex, reason in MISLEADING_PATTERNS:
            for match in regex.finditer(text):
                flagged.append(
                    {
                        "path": str(path),
                        "line": line_number(text, match.start()),
                        "reason": reason,
                        "match": match.group(0),
                    }
                )
        if path.suffix.lower() == ".md" and NATIVE_ARTIFACT_LANGUAGE_RE.search(text):
            if not has_native_tool_verification(path):
                match = NATIVE_ARTIFACT_LANGUAGE_RE.search(text)
                assert match is not None
                flagged.append(
                    {
                        "path": str(path),
                        "line": line_number(text, match.start()),
                        "reason": "Tool-created artifact language needs verified tooling; otherwise use Rendered Conversation Document or Local Markdown Source.",
                        "match": match.group(0),
                    }
                )
    return flagged


def scan_required_metadata(markdown_files: Iterable[Path]) -> list[dict]:
    flagged: list[dict] = []
    for path in markdown_files:
        if is_archived(path) or not is_written_artifact_area(path):
            continue
        sidecar, data = sidecar_data(path)
        if sidecar is None:
            flagged.append(
                {
                    "path": str(path),
                    "reason": "Active written source is missing sidecar metadata.",
                    "required": {
                        **REQUIRED_METADATA,
                        "externalExportRequested": False,
                    },
                }
            )
            continue
        for key, expected in REQUIRED_METADATA.items():
            if data.get(key) != expected:
                flagged.append(
                    {
                        "path": str(sidecar),
                        "reason": f"Sidecar metadata needs {key}: {expected!r}.",
                        "actual": data.get(key),
                    }
                )
        if "externalExportRequested" not in data:
            flagged.append(
                {
                    "path": str(sidecar),
                    "reason": "Sidecar metadata needs externalExportRequested.",
                    "actual": None,
                }
            )
    return flagged


def scan(paths: list[Path]) -> list[dict]:
    files = iter_files(paths)
    flagged = scan_language(files) + scan_required_metadata(iter_markdown(files))
    try:
        from artifact_frontmatter_guard import scan_paths as scan_markdown_readability

        for issue in scan_markdown_readability(paths):
            flagged.append(
                {
                    "path": issue["path"],
                    "line": issue.get("line"),
                    "reason": issue["reason"],
                    "match": issue.get("kind", "markdown-readability"),
                }
            )
    except Exception as exc:
        flagged.append(
            {
                "path": "execution/artifact_frontmatter_guard.py",
                "reason": f"Markdown readability guard could not run: {exc}",
                "match": "guard-error",
            }
        )
    return flagged


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag misleading written-deliverable surface language and missing source metadata."
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to scan.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    paths = [Path(p) for p in args.paths] if args.paths else [Path(p) for p in DEFAULT_PATHS]
    flagged = scan(paths)

    result = {
        "status": "fail" if flagged else "pass",
        "flagged": flagged,
        "rule": "Written deliverables must render in conversation first; Markdown is a Local Markdown Source with explicit sidecar metadata.",
    }

    if args.json:
        print(json.dumps(result, indent=2))
    elif not flagged:
        print("No misleading artifact-surface language or missing source metadata found.")
    else:
        print(f"Found {len(flagged)} artifact surface issue(s):")
        for item in flagged:
            location = item["path"]
            if item.get("line"):
                location = f"{location}:{item['line']}"
            print(f"- {location}: {item['reason']}")

    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
