#!/usr/bin/env python3
"""Guard human-facing Markdown against visible metadata headers.

Readable Markdown deliverables should open like documents: the first meaningful
line should be human-readable content, usually an H1. Machine metadata belongs
in a sidecar `.metadata.json` file. This guard intentionally allows Markdown
surfaces that require frontmatter for routing or parsing, such as workflows,
skills, command bridges, agents, and DESIGN.md files.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


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
    "99-archive",
}

SYSTEM_PATH_PARTS = {
    ".agent",
    ".agents",
    ".claude",
    ".codex",
    "agents",
    "skills",
}

SYSTEM_FILENAMES = {
    "AGENT.md",
    "SKILL.md",
    "DESIGN.md",
}

MACHINE_READABLE_PARTS = {
    ".system_generated",
    "parallax-packages",
}

# Canon-layer routing vocabulary (execution/canon_audit.py +
# execution/hooks/superseded_read_guard.py). Frontmatter made of ONLY these keys,
# carrying a real canon status, is routing metadata and is allowed to stay visible.
CANON_KEYS = {"status", "superseded_by", "supersedes", "entry"}
CANON_STATUSES = {"canonical", "draft", "superseded", "archived", "active", "parked", "done"}

VISIBLE_METADATA_KEYS = {
    "artifact",
    "artifact type",
    "artifact-type",
    "artifact_type",
    "artifacttype",
    "audience",
    "author",
    "created",
    "date",
    "description",
    "domain",
    "edition_number",
    "externalexportrequested",
    "is artifact",
    "isartifact",
    "notes_published",
    "project",
    "publish_date",
    "publish_day",
    "renderingintent",
    "slug",
    "source",
    "sourcerole",
    "status",
    "tags",
    "title",
    "type",
    "updated",
    "userfacingsurface",
    "version",
}

KEY_VALUE_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9 _-]{1,48})\s*:\s*(.+?)\s*$")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_key(key: str) -> str:
    return key.strip().lower().replace("_", "").replace("-", "").replace(" ", "")


def sidecar_paths(path: Path) -> list[Path]:
    return [
        path.with_name(path.name + ".metadata.json"),
        path.with_suffix(path.suffix + ".metadata.json"),
        path.with_suffix(".metadata.json"),
    ]


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sidecar_data(path: Path) -> tuple[Path, dict[str, Any]]:
    for sidecar in sidecar_paths(path):
        if sidecar.exists():
            return sidecar, read_json(sidecar)
    return path.with_name(path.name + ".metadata.json"), {}


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
            continue
        if path.is_dir():
            files.extend(p for p in path.rglob("*.md") if p.is_file())
    return sorted(files)


def is_archived(path: Path) -> bool:
    return any(part.lower() in ARCHIVE_DIR_NAMES for part in path.parts)


def is_project_root_index(path: Path) -> bool:
    """`_active/<slug>/INDEX.md` and `projects/<slug>/INDEX.md` carry the project
    lifecycle stamp (`status:`, `entry:`) that `projects_index.py` aggregates into
    PROJECTS.md. Exactly this surface — never a deeper INDEX.md, which would let
    real metadata pollution back in under an exempt filename.
    """
    if path.name != "INDEX.md":
        return False
    parts = path.resolve().parts
    return len(parts) >= 3 and parts[-3] in {"_active", "projects"}


def is_allowed_frontmatter_path(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    if path.name in SYSTEM_FILENAMES:
        return True
    if is_project_root_index(path):
        return True
    if parts & SYSTEM_PATH_PARTS:
        return True
    if parts & MACHINE_READABLE_PARTS:
        return True
    return False


def is_readable_candidate(path: Path) -> bool:
    if path.suffix.lower() != ".md" or is_archived(path):
        return False
    return not is_allowed_frontmatter_path(path)


def frontmatter_end(lines: list[str]) -> int | None:
    if not lines or lines[0].strip() != "---":
        return None
    for index, line in enumerate(lines[1:80], start=1):
        if line.strip() == "---":
            return index
    return None


def parse_key_values(lines: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in lines:
        match = KEY_VALUE_RE.match(line)
        if not match:
            continue
        key = match.group(1).strip()
        values[key] = match.group(2).strip().strip('"')
    return values


def first_content_index(lines: list[str]) -> int:
    for index, line in enumerate(lines):
        if line.strip():
            return index
    return len(lines)


def top_key_value_indexes(lines: list[str]) -> list[int]:
    indexes: list[int] = []
    for index, line in enumerate(lines[:30]):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            break
        match = KEY_VALUE_RE.match(line)
        if not match:
            if indexes:
                break
            continue
        key = normalize_key(match.group(1))
        if key in {normalize_key(item) for item in VISIBLE_METADATA_KEYS}:
            indexes.append(index)
    return indexes


def top_json_metadata_end(lines: list[str]) -> int | None:
    start = first_content_index(lines)
    if start >= len(lines) or not lines[start].lstrip().startswith("{"):
        return None
    collected: list[str] = []
    for index in range(start, min(len(lines), start + 80)):
        collected.append(lines[index])
        candidate = "\n".join(collected)
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and any(normalize_key(key) in {normalize_key(item) for item in VISIBLE_METADATA_KEYS} for key in data):
            return index
        return None
    return None


def has_h1(lines: list[str]) -> bool:
    index = first_content_index(lines)
    return index < len(lines) and lines[index].lstrip().startswith("# ")


def issue_for(path: Path, kind: str, line: int, reason: str, metadata: dict[str, str] | None = None) -> dict[str, Any]:
    return {
        "path": str(path),
        "line": line,
        "kind": kind,
        "reason": reason,
        "metadata": metadata or {},
        "fixable": True,
    }


def is_canon_frontmatter(metadata: dict[str, str]) -> bool:
    """Canon-layer routing frontmatter, not document metadata.

    `status: canonical|draft|superseded|archived` (+ `superseded_by`/`supersedes`)
    is consumed by execution/canon_audit.py and by the
    execution/hooks/superseded_read_guard.py PostToolUse hook — it is how a stale
    doc stops winning greps. This module's own docstring already allows "Markdown
    surfaces that require frontmatter for routing or parsing"; this is one.

    Narrow by construction: the block must contain a canon `status:` AND carry
    nothing but canon keys. A doc that also declares `author:`/`date:` is still
    flagged, so real metadata pollution cannot hide behind a status line.
    """
    if not metadata:
        return False
    # normalize_key strips underscores (superseded_by -> supersededby), so the
    # canon vocabulary has to be normalized on both sides of the comparison.
    allowed = {normalize_key(k) for k in CANON_KEYS}
    keys = {normalize_key(k) for k in metadata}
    if not keys or not keys.issubset(allowed):
        return False
    status = (metadata.get("status") or metadata.get("Status") or "").strip().lower()
    return status in CANON_STATUSES


def scan_file(path: Path) -> list[dict[str, Any]]:
    if not is_readable_candidate(path):
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    lines = text.splitlines()
    issues: list[dict[str, Any]] = []

    end = frontmatter_end(lines)
    if end is not None:
        metadata = parse_key_values(lines[1:end])
        if not is_canon_frontmatter(metadata):
            issues.append(
                issue_for(
                    path,
                    "leading-frontmatter",
                    1,
                    "Human-facing Markdown must not start with visible YAML frontmatter; move metadata to a sidecar .metadata.json file.",
                    metadata,
                )
            )

    indexes = top_key_value_indexes(lines)
    if indexes:
        # Lines inside an allowed canon frontmatter block are that block, not a
        # second violation — don't report the same stamp twice.
        if end is not None and is_canon_frontmatter(parse_key_values(lines[1:end])):
            indexes = [i for i in indexes if i > end]
    if indexes:
        metadata = parse_key_values([lines[index] for index in indexes])
        issues.append(
            issue_for(
                path,
                "leading-key-value-metadata",
                indexes[0] + 1,
                "Human-facing Markdown must not start with visible key-value metadata; move metadata to a sidecar .metadata.json file.",
                metadata,
            )
        )

    json_end = top_json_metadata_end(lines)
    if json_end is not None:
        issues.append(
            issue_for(
                path,
                "leading-json-metadata",
                first_content_index(lines) + 1,
                "Human-facing Markdown must not start with a visible JSON metadata block; move metadata to a sidecar .metadata.json file.",
            )
        )

    return issues


def scan_paths(paths: list[Path]) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    for path in iter_markdown(paths):
        issues.extend(scan_file(path))
    return issues


def merge_sidecar(path: Path, migrated: dict[str, Any]) -> None:
    sidecar, data = sidecar_data(path)
    data.setdefault("userFacingSurface", "rendered-conversation-document")
    data.setdefault("sourceRole", "persistence-copy")
    data.setdefault("externalExportRequested", False)
    data["migratedFromVisibleMarkdownMetadata"] = True
    data["migratedAt"] = utc_now()
    existing = data.get("migratedVisibleMetadata")
    if isinstance(existing, dict):
        existing.update(migrated)
        data["migratedVisibleMetadata"] = existing
    else:
        data["migratedVisibleMetadata"] = migrated
    write_json(sidecar, data)


def remove_indexes(lines: list[str], indexes: set[int]) -> list[str]:
    return [line for index, line in enumerate(lines) if index not in indexes]


def ensure_title(lines: list[str], metadata: dict[str, Any]) -> list[str]:
    while lines and not lines[0].strip():
        lines = lines[1:]
    if has_h1(lines):
        return lines
    title = str(metadata.get("title") or metadata.get("Title") or "").strip()
    if title:
        return [f"# {title}", "", *lines]
    return lines


def fix_file(path: Path) -> bool:
    issues = scan_file(path)
    if not issues:
        return False

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    migrated: dict[str, Any] = {}

    end = frontmatter_end(lines)
    if end is not None:
        migrated.update(parse_key_values(lines[1:end]))
        lines = lines[end + 1 :]

    indexes = set(top_key_value_indexes(lines))
    if indexes:
        migrated.update(parse_key_values([lines[index] for index in indexes]))
        lines = remove_indexes(lines, indexes)

    json_end = top_json_metadata_end(lines)
    if json_end is not None:
        start = first_content_index(lines)
        try:
            data = json.loads("\n".join(lines[start : json_end + 1]))
            if isinstance(data, dict):
                migrated.update(data)
        except json.JSONDecodeError:
            pass
        lines = lines[:start] + lines[json_end + 1 :]

    lines = ensure_title(lines, migrated)
    merge_sidecar(path, migrated)
    path.write_text("\n".join(lines).lstrip() + "\n", encoding="utf-8")
    return True


def fix_paths(paths: list[Path]) -> list[Path]:
    fixed: list[Path] = []
    for path in iter_markdown(paths):
        if fix_file(path):
            fixed.append(path)
    return fixed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check or remove visible metadata headers from human-facing Markdown deliverables."
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to scan.")
    parser.add_argument("--fix", action="store_true", help="Move visible metadata to sidecar JSON and remove it from Markdown.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    paths = [Path(p) for p in args.paths] if args.paths else [Path(p) for p in DEFAULT_PATHS]

    if args.fix:
        fixed = fix_paths(paths)
        result = {
            "status": "fixed" if fixed else "pass",
            "fixed": [str(path) for path in fixed],
            "rule": "Human-facing Markdown must open as readable prose; machine metadata belongs in sidecar JSON.",
        }
        if args.json:
            print(json.dumps(result, indent=2))
        elif fixed:
            print(f"Fixed {len(fixed)} Markdown file(s):")
            for path in fixed:
                print(f"- {path}")
        else:
            print("No visible Markdown metadata headers found.")
        return 0

    issues = scan_paths(paths)
    result = {
        "status": "fail" if issues else "pass",
        "issues": issues,
        "rule": "Human-facing Markdown must open as readable prose; machine metadata belongs in sidecar JSON.",
    }
    if args.json:
        print(json.dumps(result, indent=2))
    elif not issues:
        print("No visible Markdown metadata headers found.")
    else:
        print(f"Found {len(issues)} Markdown readability issue(s):")
        for item in issues:
            print(f"- {item['path']}:{item['line']}: {item['reason']}")

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
