"""Regression proof for worktree memory identity and isolation. No providers."""
import importlib.util
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))
import memory_facade as mf
import worktree_lane as wl

def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True)

@pytest.fixture
def checkouts(tmp_path):
    main = tmp_path / "main"
    main.mkdir()
    git(main, "init", "-q")
    git(main, "-c", "user.name=Audit", "-c", "user.email=audit@example.invalid",
        "commit", "--allow-empty", "-qm", "fixture")
    lane = tmp_path / "lane"
    git(main, "worktree", "add", "-qb", "test-lane", str(lane))
    return main, lane

@pytest.fixture
def db(tmp_path, monkeypatch):
    path = tmp_path / "history.sqlite"
    with sqlite3.connect(path) as con:
        con.execute("""CREATE TABLE exchanges (
            id TEXT PRIMARY KEY, project TEXT, session_id TEXT,
            user_message TEXT, assistant_message TEXT, timestamp TEXT, archive_path TEXT
        )""")
        con.executemany("INSERT INTO exchanges VALUES (?,?,?,?,?,?,?)", [
            ("main-hit", "canonical", "s1", "Scrapes source", "", "2026-09-01", ""),
            ("lane-hit", "lane", "s2", "Scrapes repair", "", "2026-09-02", ""),
            ("foreign-hit", "other", "s3", "Scrapes private foreign", "", "2026-09-03", ""),
        ])
    monkeypatch.setattr(mf, "EPISODIC_DB", path)
    return path

def test_real_worktree_shares_main_identity_but_retains_lane(checkouts):
    main, lane = checkouts
    main_keys = mf.episodic_projects(main, override="")
    lane_keys = mf.episodic_projects(lane, override="")
    assert lane_keys[0] == main_keys[0]
    assert len(main_keys) == 1
    assert len(lane_keys) == 2
    assert lane_keys[1].endswith("-lane")

def test_explicit_scope_overrides_are_not_broadened(checkouts):
    assert mf.episodic_projects(checkouts[1], "chosen,chosen, second") == ["chosen", "second"]
    assert mf.episodic_projects(checkouts[1], "ALL") is None
    assert mf.episodic_projects(checkouts[1], ", ,") == mf.episodic_projects(checkouts[1], "")

def test_scoped_retrieval_includes_main_lane_excludes_unrelated(db, monkeypatch):
    monkeypatch.setattr(mf, "EPISODIC_PROJECTS", ["canonical", "lane"])
    result = mf._query_episodic("Scrapes", 10)
    assert {r["id"] for r in result["results"]} == {"main-hit", "lane-hit"}
    assert result["degraded"] is None

def test_unindexed_scope_is_distinct_from_no_query_match(db, monkeypatch):
    monkeypatch.setattr(mf, "EPISODIC_PROJECTS", ["unindexed"])
    assert "no indexed exchanges" in mf._query_episodic("Scrapes", 5)["degraded"]
    monkeypatch.setattr(mf, "EPISODIC_PROJECTS", ["canonical"])
    result = mf._query_episodic("nonexistentword", 5)
    assert result == {"results": [], "degraded": None}

def test_missing_store_is_unavailable_not_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(mf, "EPISODIC_DB", tmp_path / "missing.sqlite")
    assert "missing" in mf._query_episodic("Scrapes", 5)["degraded"]
    assert not mf.EPISODIC_DB.exists()

def test_explicit_all_scope_remains_supported(db, monkeypatch):
    monkeypatch.setattr(mf, "EPISODIC_PROJECTS", None)
    assert len(mf._query_episodic("Scrapes", 10)["results"]) == 3

def test_parity_detects_old_lane_and_accepts_repaired_scope(tmp_path, db):
    roots = []
    for name, scopes in [("main", ["canonical"]), ("lane", ["wrong-lane-key"])]:
        root = tmp_path / name
        (root / "execution").mkdir(parents=True)
        (root / "execution/memory_facade.py").write_text(
            f"from pathlib import Path\nEPISODIC_DB=Path({str(db)!r})\nEPISODIC_PROJECTS={scopes!r}\n"
        )
        roots.append(root)
    main, lane = roots
    assert "excluded" in wl.episodic_parity(lane, main)[0]
    (lane / "execution/memory_facade.py").write_text(
        f"from pathlib import Path\nEPISODIC_DB=Path({str(db)!r})\nEPISODIC_PROJECTS=['canonical','lane']\n"
    )
    assert wl.episodic_parity(lane, main) == []
