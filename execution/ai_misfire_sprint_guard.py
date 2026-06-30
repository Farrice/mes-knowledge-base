#!/usr/bin/env python3
"""Guard the active AI Misfire revenue suite against stale-source contamination."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ACTIVE_INTENT = "2026-05-10-full-revenue-suite-rebuild"

ACTIVE_DOCS = {
    "revenue-control-room.md",
    "marketing-void-demo-pack.md",
    "offer-checkout-fulfillment-pack.md",
    "lead-gen-marketplace-pack.md",
}

ALLOWED_MARKDOWN = ACTIVE_DOCS | {"README.md"}

STALE_PATTERNS = {
    "archive/": "Active source must not link into archive.",
    "stale-pre-rebuild": "Active source must not reference the stale quarantine path.",
    "full-cash-sprint-pack": "Active source must not reference the old full cash sprint pack.",
    "ai-misfire-attention-demo-pack": "Active source must not reference the previous attention pack.",
    "ai-misfire-copy-punch-pass": "Active source must not reference the previous copy punch pass.",
    "ai-misfire-today-deployment-pack": "Active source must not reference the previous today deployment pack.",
    "ai-misfire-demo-deployment-pack": "Active source must not reference the previous demo deployment pack.",
    "ai-misfire-lead-gen-action-queue": "Active source must not reference the previous lead-gen queue.",
    "ai-misfire-offer-and-checkout-copy": "Active source must not reference the previous offer pack.",
}

ROOT_STALE_RE = re.compile(r"^(?:\d{2}-.+\.md|.+\.csv)$", re.IGNORECASE)
PUBLISHABLE_RE = re.compile(r"<!--\s*publishable:([a-z0-9_-]+):start\s*-->", re.IGNORECASE)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def is_archived(path: Path) -> bool:
    return any(part.lower() in {"archive", "_archive", "archived", "deprecated"} for part in path.parts)


def sidecar(path: Path) -> Path:
    return path.with_name(path.name + ".metadata.json")


def line_number(text: str, needle: str) -> int:
    index = text.lower().find(needle.lower())
    if index < 0:
        return 1
    return text.count("\n", 0, index) + 1


def scan(root: Path) -> list[dict]:
    flagged: list[dict] = []
    document_dir = root / "document-artifacts"

    if not document_dir.exists():
        return [{"path": str(document_dir), "reason": "Missing active document-artifacts directory."}]

    active_markdown = sorted(
        path for path in document_dir.glob("*.md") if path.is_file() and not is_archived(path)
    )
    active_names = {path.name for path in active_markdown}

    unexpected = sorted(active_names - ALLOWED_MARKDOWN)
    for name in unexpected:
        flagged.append(
            {
                "path": str(document_dir / name),
                "reason": "Unexpected active Markdown source. Quarantine old generated packs before shipping.",
            }
        )

    missing = sorted(ACTIVE_DOCS - active_names)
    for name in missing:
        flagged.append(
            {
                "path": str(document_dir / name),
                "reason": "Required rebuilt revenue-suite source is missing.",
            }
        )

    if len(active_names - {"README.md"}) > 4:
        flagged.append(
            {
                "path": str(document_dir),
                "reason": "Active suite must contain no more than four non-index Markdown sources.",
                "count": len(active_names - {"README.md"}),
            }
        )

    for path in active_markdown:
        text = read_text(path)
        lower = text.lower()
        if ACTIVE_INTENT not in text:
            flagged.append(
                {
                    "path": str(path),
                    "reason": "Active source is missing the current intent marker.",
                    "required": ACTIVE_INTENT,
                }
            )
        metadata_path = sidecar(path)
        metadata = read_json(metadata_path)
        if metadata.get("activeIntent") != ACTIVE_INTENT:
            flagged.append(
                {
                    "path": str(metadata_path),
                    "reason": "Sidecar metadata is missing the current activeIntent.",
                    "actual": metadata.get("activeIntent"),
                    "required": ACTIVE_INTENT,
                }
            )
        for pattern, reason in STALE_PATTERNS.items():
            if pattern in lower:
                flagged.append(
                    {
                        "path": str(path),
                        "line": line_number(text, pattern),
                        "reason": reason,
                        "match": pattern,
                    }
                )

    for path in sorted(root.iterdir()):
        if path.is_file() and ROOT_STALE_RE.match(path.name):
            flagged.append(
                {
                    "path": str(path),
                    "reason": "Stale root working file remains active; move it into quarantine.",
                }
            )

    for path in active_markdown:
        if path.name == "README.md":
            continue
        text = read_text(path)
        if path.name != "revenue-control-room.md" and not PUBLISHABLE_RE.search(text):
            flagged.append(
                {
                    "path": str(path),
                    "reason": "Publishable source pack needs explicit publishable section markers.",
                }
            )

    return flagged


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check the rebuilt AI Misfire revenue suite for stale-source contamination."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="brain/ai-misfire-founding-proof-sprint-v1",
        help="AI Misfire sprint root to scan.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    root = Path(args.path)
    flagged = scan(root)
    result = {
        "status": "fail" if flagged else "pass",
        "flagged": flagged,
        "activeIntent": ACTIVE_INTENT,
        "rule": "AI Misfire active suite must use only the four rebuilt sources and current intent marker.",
    }

    if args.json:
        print(json.dumps(result, indent=2))
    elif not flagged:
        print("AI Misfire sprint active suite is clean.")
    else:
        print(f"Found {len(flagged)} AI Misfire sprint issue(s):")
        for item in flagged:
            location = item["path"]
            if item.get("line"):
                location = f"{location}:{item['line']}"
            print(f"- {location}: {item['reason']}")

    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
