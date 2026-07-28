#!/usr/bin/env python3
"""
Sprint 2: Backfill voice rules from Claude Code auto-memory into sovereign memory.

Reads `~/.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback_*.md`
files and stores each as a PINNED semantic/rule memory. Pinning makes voice rules
immune to Ebbinghaus decay so they always surface in retrieval.

Idempotent: re-runs skip already-imported files (matched by metadata.source_file).

Usage:
    python3 execution/backfill_voice_rules.py --dry-run    # preview, no writes
    python3 execution/backfill_voice_rules.py              # commit imports
    python3 execution/backfill_voice_rules.py --refresh    # delete existing imports + re-import all
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add execution/ to sys.path so we can import memory_store
sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_store import DB_PATH, get_db, pin_memory, store_memory  # noqa: E402

MEMORY_DIR = Path.home() / ".claude/projects/-Users-farricecain-Google-Antigravity/memory"


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    """Parse YAML-style frontmatter delimited by --- markers.

    Returns (frontmatter_dict, body_after_frontmatter). Tolerates missing frontmatter.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}, text

    fm: Dict[str, str] = {}
    for line in lines[1:end_idx]:
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()

    body = "\n".join(lines[end_idx + 1:]).strip()
    return fm, body


def find_existing_imports() -> Dict[str, str]:
    """Return {source_file_path: memory_id} for already-imported voice rules."""
    if not DB_PATH.exists():
        return {}
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT id, metadata FROM memories WHERE tier = 'semantic' AND category = 'rule'"
    ).fetchall()
    conn.close()

    existing = {}
    for row in rows:
        try:
            meta = json.loads(row["metadata"])
            src = meta.get("source_file")
            if src and meta.get("pinned_reason") == "voice_rule":
                existing[src] = row["id"]
        except (json.JSONDecodeError, TypeError):
            continue
    return existing


def delete_existing_imports(existing: Dict[str, str]) -> int:
    """Delete previously-imported voice rules (for --refresh mode)."""
    if not existing:
        return 0
    conn = sqlite3.connect(str(DB_PATH))
    placeholders = ",".join("?" * len(existing))
    conn.execute(
        f"DELETE FROM memories WHERE id IN ({placeholders})",
        list(existing.values()),
    )
    conn.commit()
    deleted = conn.total_changes
    conn.close()
    return deleted


def collect_feedback_files() -> List[Path]:
    """All feedback_*.md files in the Claude Code auto-memory directory."""
    if not MEMORY_DIR.exists():
        print(f"❌ Memory directory not found: {MEMORY_DIR}", file=sys.stderr)
        return []
    return sorted(MEMORY_DIR.glob("feedback_*.md"))


def build_proposed_import(path: Path) -> Optional[Dict]:
    """Build the proposed memory entry for one feedback file."""
    try:
        text = path.read_text()
    except OSError as e:
        print(f"  ⚠️  read failed: {path.name} ({e})", file=sys.stderr)
        return None

    fm, body = parse_frontmatter(text)
    name = fm.get("name", path.stem.replace("feedback_", "").replace("-", " ").title())
    description = fm.get("description", "")
    fm_type = fm.get("type", "feedback")

    # Compose content: description as hook + full body
    # If description is the same as the body's opening, just use body
    if description and not body.startswith(description[:60]):
        content = f"**{description}**\n\n{body}"
    else:
        content = body or description or name

    return {
        "tier": "semantic",
        "category": "rule",
        "content": content,
        "metadata": {
            "source_file": str(path),
            "source_type": fm_type,
            "pinned_reason": "voice_rule",
            "feedback_name": name,
            "feedback_description_short": description[:200] if description else "",
        },
    }


def backfill(dry_run: bool = False, refresh: bool = False) -> int:
    """Main backfill. Returns exit code (0 = OK)."""
    files = collect_feedback_files()
    if not files:
        print("No feedback_*.md files found.")
        return 1

    existing = find_existing_imports()

    if refresh and not dry_run:
        deleted = delete_existing_imports(existing)
        print(f"♻️  Refresh mode: deleted {deleted} prior voice rule import(s)")
        existing = {}

    proposed = []
    for f in files:
        entry = build_proposed_import(f)
        if not entry:
            continue
        entry["_path"] = str(f)
        entry["_exists"] = str(f) in existing
        proposed.append(entry)

    new_count = sum(1 for p in proposed if not p["_exists"])
    skip_count = sum(1 for p in proposed if p["_exists"])

    print(f"Found {len(proposed)} feedback file(s): {new_count} NEW, {skip_count} SKIP (already imported)")
    print()

    if dry_run:
        for p in proposed:
            marker = "SKIP" if p["_exists"] else "WOULD IMPORT"
            print(f"  [{marker}] {p['metadata']['feedback_name']}")
            preview = p["content"].replace("\n", " ")[:140]
            print(f"      Content: {preview}{'...' if len(p['content']) > 140 else ''}")
        print()
        print("(dry run — no writes)")
        return 0

    imported = 0
    pinned = 0
    skipped = 0
    for p in proposed:
        if p["_exists"]:
            skipped += 1
            print(f"  SKIP (exists):     {p['metadata']['feedback_name']}")
            continue
        mid = store_memory(
            tier=p["tier"],
            category=p["category"],
            content=p["content"],
            metadata=p["metadata"],
            silent=True,
        )
        if not mid:
            print(f"  ❌ STORE FAILED:    {p['metadata']['feedback_name']}")
            continue
        imported += 1
        pin_memory(mid)
        pinned += 1
        print(f"  ✅ IMPORTED + PIN: {p['metadata']['feedback_name']} → {mid}")

    print()
    print(f"Done: imported={imported}, pinned={pinned}, skipped={skipped}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill voice rules from Claude Code feedback memory.")
    parser.add_argument("--dry-run", action="store_true", help="Preview what would be imported")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Delete all prior voice rule imports and re-import from scratch",
    )
    args = parser.parse_args()

    # Ensure DB exists (will create on first store)
    if not DB_PATH.exists():
        print(f"Note: SQLite DB does not yet exist at {DB_PATH} — will create on first write.")

    # Trigger schema creation if needed
    get_db().close()

    return backfill(dry_run=args.dry_run, refresh=args.refresh)


if __name__ == "__main__":
    sys.exit(main())
