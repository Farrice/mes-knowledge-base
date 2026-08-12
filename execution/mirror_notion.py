#!/usr/bin/env python3
"""
Mirror Notion — Sprint 3 Notion DB mirror to sovereign sqlite.

Pulls the operational databases and Simon Intellectual Library into the local
`notion_mirror` table so
sovereign memory has a queryable, workspace-filterable view of Notion
content without round-tripping the API.

Skipped DB: Captures (too volatile — high write rate, low retrieval value).

Usage:
    python3 execution/mirror_notion.py --dry-run        # counts + cost preview
    python3 execution/mirror_notion.py                  # incremental (last_edited_at since last mirror)
    python3 execution/mirror_notion.py --full           # full re-mirror
    python3 execution/mirror_notion.py --db projects    # single DB
    python3 execution/mirror_notion.py --stats          # mirror coverage report

Scheduled via ~/Library/LaunchAgents/com.antigravity.mirror-nightly.plist (daily 02:00).
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

# Make execution/ importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from notion_api import NotionAPI, NotionAPIError  # noqa: E402
from memory_store import DB_PATH  # noqa: E402


# Operational DBs plus the integration-owned Simon Intellectual Library.
# Captures remains excluded because it is high-volume and low retrieval value.
DB_REGISTRY = {
    "projects":  "cf93599a-a201-4e55-a6b9-f2f58ae6fd77",
    "knowledge": "5c63b25c-e040-4c6f-8a7b-906643090694",
    "content":   "ff77ee45-8ee8-4fce-996e-20c76fa65d9c",
    "personal":  "0911ef04-8117-463f-8b21-e7f6c1a1ef4a",
    "performance": "31f49875-a897-81db-b599-dee5e7961b5c",
    "library_knowledge": "38849875-a897-812c-b693-c7b35e7530a6",
    "library_experts": "38849875-a897-81d7-8ed5-f5731ce0d1c1",
    "library_sources": "38849875-a897-8115-85f2-f1a30e2291a4",
    "library_skills": "38849875-a897-813d-a451-fdb32c7121f2",
    "session_memory": "38849875-a897-81c0-950e-f6a48bb28a72",
}


def query_database_paginated(api: NotionAPI, database_id: str,
                             page_size: int = 100,
                             filter_body: Optional[dict] = None) -> List[dict]:
    """Wrapper around notion_api.query_database that handles pagination.

    The existing query_database() does NOT pass start_cursor, so we hit
    the endpoint directly with our own paginated body.
    """
    results: List[dict] = []
    start_cursor: Optional[str] = None
    while True:
        body: Dict = {"page_size": page_size}
        if filter_body:
            body["filter"] = filter_body
        if start_cursor:
            body["start_cursor"] = start_cursor
        data = api._request("POST", f"/databases/{database_id}/query", body)
        results.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        start_cursor = data.get("next_cursor")
        if not start_cursor:
            break
    return results


def extract_title(page: dict) -> str:
    """Pull a human-readable title from a Notion page object."""
    props = page.get("properties", {})
    for prop in props.values():
        if prop.get("type") == "title":
            title_arr = prop.get("title", [])
            if title_arr:
                return "".join(t.get("plain_text", "") for t in title_arr)
    return "(untitled)"


def extract_excerpt(page: dict, max_chars: int = 400) -> str:
    """Concatenate rich_text-bearing properties into an excerpt blob."""
    parts: List[str] = []
    props = page.get("properties", {})
    for name, prop in props.items():
        ptype = prop.get("type")
        if ptype == "rich_text":
            txts = prop.get("rich_text", [])
            if txts:
                content = "".join(t.get("plain_text", "") for t in txts)
                if content.strip():
                    parts.append(f"{name}: {content.strip()}")
        elif ptype == "select":
            sel = prop.get("select")
            if sel and sel.get("name"):
                parts.append(f"{name}: {sel['name']}")
        elif ptype == "multi_select":
            sels = prop.get("multi_select", [])
            if sels:
                parts.append(f"{name}: {', '.join(s.get('name', '') for s in sels)}")
        elif ptype == "number":
            num = prop.get("number")
            if num is not None:
                parts.append(f"{name}: {num}")
    excerpt = " | ".join(parts)
    if len(excerpt) > max_chars:
        excerpt = excerpt[: max_chars - 1] + "…"
    return excerpt


def upsert_page(conn: sqlite3.Connection, page: dict, db_id: str, db_name: str,
                now_iso: str) -> bool:
    """Insert or update a page in notion_mirror. Returns True if new row."""
    page_id = page.get("id")
    if not page_id:
        return False
    title = extract_title(page)
    excerpt = extract_excerpt(page)
    last_edited = page.get("last_edited_time", "")
    raw = json.dumps(page, ensure_ascii=False)

    existing = conn.execute(
        "SELECT page_id FROM notion_mirror WHERE page_id = ?", (page_id,)
    ).fetchone()

    conn.execute("""
        INSERT INTO notion_mirror
            (page_id, db_id, db_name, title, content_excerpt, last_edited_at, mirrored_at, raw_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(page_id) DO UPDATE SET
            db_id = excluded.db_id,
            db_name = excluded.db_name,
            title = excluded.title,
            content_excerpt = excluded.content_excerpt,
            last_edited_at = excluded.last_edited_at,
            mirrored_at = excluded.mirrored_at,
            raw_json = excluded.raw_json
    """, (page_id, db_id, db_name, title, excerpt, last_edited, now_iso, raw))
    return existing is None


def get_last_mirrored(conn: sqlite3.Connection, db_id: str) -> Optional[str]:
    """Latest last_edited_at we have for a given Notion DB. None if empty."""
    row = conn.execute(
        "SELECT MAX(last_edited_at) FROM notion_mirror WHERE db_id = ?", (db_id,)
    ).fetchone()
    return row[0] if row and row[0] else None


def mirror_db(api: NotionAPI, name: str, db_id: str, conn: sqlite3.Connection,
              full: bool = False, dry_run: bool = False) -> Dict:
    """Mirror one Notion DB. Returns stats dict."""
    filter_body: Optional[dict] = None
    if not full:
        last = get_last_mirrored(conn, db_id)
        if last:
            filter_body = {
                "timestamp": "last_edited_time",
                "last_edited_time": {"on_or_after": last},
            }

    try:
        pages = query_database_paginated(api, db_id, filter_body=filter_body)
    except NotionAPIError as e:
        return {"db": name, "error": f"{e.status} {e.code}: {e}", "fetched": 0, "new": 0, "updated": 0}

    now_iso = datetime.now(timezone.utc).isoformat()
    new = updated = 0
    if not dry_run:
        for page in pages:
            was_new = upsert_page(conn, page, db_id, name, now_iso)
            if was_new:
                new += 1
            else:
                updated += 1
        conn.commit()

    return {
        "db": name,
        "fetched": len(pages),
        "new": new,
        "updated": updated,
        "mode": "full" if full else "incremental",
    }


def mirror_all(full: bool = False, dry_run: bool = False,
               only: Optional[str] = None) -> List[Dict]:
    api = NotionAPI()
    conn = sqlite3.connect(str(DB_PATH))

    if only:
        if only not in DB_REGISTRY:
            print(f"Unknown DB '{only}'. Valid: {', '.join(DB_REGISTRY)}", file=sys.stderr)
            conn.close()
            return []
        registry = {only: DB_REGISTRY[only]}
    else:
        registry = DB_REGISTRY

    stats: List[Dict] = []
    for name, db_id in registry.items():
        result = mirror_db(api, name, db_id, conn, full=full, dry_run=dry_run)
        stats.append(result)
        marker = "✗" if result.get("error") else "✓"
        if result.get("error"):
            print(f"  {marker} {name:12s}  ERROR: {result['error']}")
        else:
            print(f"  {marker} {name:12s}  fetched={result['fetched']:4d}  "
                  f"new={result['new']:3d}  updated={result['updated']:3d}  ({result['mode']})")
        # Be polite to Notion (~3 req/sec limit)
        time.sleep(0.4)

    conn.close()
    return stats


def show_stats() -> None:
    """Mirror coverage report."""
    conn = sqlite3.connect(str(DB_PATH))
    total = conn.execute("SELECT count(*) FROM notion_mirror").fetchone()[0]
    by_db = conn.execute("""
        SELECT db_name, count(*), MAX(mirrored_at), MAX(last_edited_at)
        FROM notion_mirror GROUP BY db_name ORDER BY db_name
    """).fetchall()
    conn.close()

    print(f"Notion mirror coverage:")
    print(f"  Total pages: {total}\n")
    print(f"  {'DB':14s} {'count':>6s}  {'last mirror':30s}  {'latest edit':30s}")
    print(f"  {'-'*14} {'-'*6}  {'-'*30}  {'-'*30}")
    for name, cnt, mirrored, edited in by_db:
        print(f"  {name:14s} {cnt:>6d}  {mirrored or '—':30s}  {edited or '—':30s}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror Notion DBs to sovereign sqlite")
    parser.add_argument("--dry-run", action="store_true", help="Fetch + count only, no DB writes")
    parser.add_argument("--full", action="store_true", help="Full re-mirror (ignore incremental filter)")
    parser.add_argument("--db", help="Mirror only one DB by name")
    parser.add_argument("--stats", action="store_true", help="Show coverage report and exit")
    args = parser.parse_args()

    if args.stats:
        show_stats()
        return 0

    start = time.time()
    print(f"Mirroring Notion → {DB_PATH} (mode={'full' if args.full else 'incremental'}, dry_run={args.dry_run})")
    stats = mirror_all(full=args.full, dry_run=args.dry_run, only=args.db)
    elapsed = time.time() - start

    total_new = sum(s.get("new", 0) for s in stats)
    total_updated = sum(s.get("updated", 0) for s in stats)
    errors = [s for s in stats if s.get("error")]

    print(f"\nDone in {elapsed:.1f}s. new={total_new}, updated={total_updated}, errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
