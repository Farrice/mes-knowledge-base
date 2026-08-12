#!/usr/bin/env python3
"""Deterministic checks for the network-independent Notion Second Brain path."""

from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path

import log_performance
import memory_facade
import mirror_notion


passed: list[str] = []
failed: list[str] = []


def check(condition: bool, label: str) -> None:
    (passed if condition else failed).append(label)


def verify_local_baseline() -> None:
    with tempfile.TemporaryDirectory() as td:
        original = log_performance.LOCAL_LOG_PATH
        try:
            log_performance.LOCAL_LOG_PATH = Path(td) / "performance-log.jsonl"
            rows = [
                {"skill": "notion-test", "agent": "a", "quality_score": score,
                 "intent_alignment": 8, "expert_standard": 7,
                 "adversarial_resilience": 7, "status": "Keep"}
                for score in (6, 7, 8, 9)
            ]
            log_performance.LOCAL_LOG_PATH.write_text(
                "\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8"
            )
            baseline = log_performance.get_baseline(skill="notion-test", window=3)
            check(baseline["count"] == 3, "baseline uses the requested local window")
            check(baseline["avg_quality"] == 8, "baseline computes from the local ledger")
            check(baseline["source"] == "local_performance_ledger", "baseline declares its local source")
        finally:
            log_performance.LOCAL_LOG_PATH = original


def verify_local_notion_search() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "sovereign.db"
        con = sqlite3.connect(db)
        con.execute(
            "CREATE TABLE notion_mirror (page_id TEXT, db_id TEXT, db_name TEXT, "
            "title TEXT, content_excerpt TEXT, last_edited_at TEXT, mirrored_at TEXT, raw_json TEXT)"
        )
        con.execute(
            "INSERT INTO notion_mirror VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ("abc-123", "db", "session_memory", "Notion reliability repair",
             "Second brain decisions and pickup prompt", "2026-08-11", "2026-08-11", "{}"),
        )
        con.commit()
        con.close()
        original = memory_facade.SOVEREIGN_DB
        try:
            memory_facade.SOVEREIGN_DB = db
            result = memory_facade._query_notion_mirror("second brain reliability", 5)
            check(len(result["results"]) == 1, "Notion mirror is searchable without the network")
            check(result["results"][0]["source"] == "notion", "Notion result keeps source identity")
        finally:
            memory_facade.SOVEREIGN_DB = original


def verify_registry() -> None:
    expected = {
        "library_knowledge", "library_experts", "library_sources",
        "library_skills", "session_memory",
    }
    check(expected.issubset(mirror_notion.DB_REGISTRY), "nightly mirror includes the Simon Library")
    check("notion" in memory_facade.ALL_SOURCES, "facade exposes Notion as a first-class source")


def main() -> int:
    verify_local_baseline()
    verify_local_notion_search()
    verify_registry()
    print(f"Notion Second Brain reliability: {'PASS' if not failed else 'FAIL'}")
    print(f"- Passed: {len(passed)}")
    print(f"- Failed: {len(failed)}")
    for item in failed:
        print(f"FAIL: {item}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
