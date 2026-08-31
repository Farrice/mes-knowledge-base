#!/usr/bin/env python3
"""memory_facade.py — one retrieval interface over every memory store.

Audit 2026-04-24 Fix 7 (deferred then; shipped 2026-06-12). The system had
five memory silos, each queried (or not) by a different code path — the
textbook "5 memories, none load at the right moment" failure. This facade
gives The Chain ONE call at Tier 1.5b:

    python3 execution/memory_facade.py "<task intent>" --top 10
    python3 execution/memory_facade.py "<task intent>" --json --sources sovereign,automem

Stores unified (in rank order):
    sovereign   .memory/sovereign.db — vector retrieval via memory_retrieve
                (pinned voice rules first), with a deterministic FTS5/LIKE
                fallback when embeddings are unavailable (no network/key)
    automem     Claude Code user auto-memory (~/.claude/projects/.../memory/)
                — frontmatter descriptions + MEMORY.md index, keyword-scored
    wiki        knowledge/ — via knowledge/compiled/manifest.json (filename/
                domain/expert match); pointers, not full documents
    agents      agents/*/memory/context.md — matched when the query names an
                agent; pointers + first lines
    episodic    ~/.config/superpowers/conversation-index/db.sqlite — full
                conversation history (superpowers episodic-memory). Read-only
                SQL over the `exchanges` table, project-scoped to this repo by
                default; the "auto-remember past sessions" layer.
    solutions   docs/solutions/*.md — Solution Recorder cards (hard-won fixes
                captured via execution/solution_recorder.py), frontmatter-
                scored on name+problem_signature+tags.
    notion      Local mirror of the Notion databases in sovereign.db. This is
                queried without a network round-trip; mirror_notion.py owns
                freshness and the nightly external sync.

Design rules:
    - Read-only. The facade never writes to any store.
    - Degrade store-by-store: a broken store yields zero results and a note
      in `degraded`, never an exception. (Silent-skip is the banned pattern;
      every skip is REPORTED in the payload.)
    - Existing single-store entry points (memory_retrieve.py etc.) remain
      valid; this wraps, it does not replace.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
SOVEREIGN_DB = ROOT / ".memory" / "sovereign.db"
WIKI_MANIFEST = ROOT / "knowledge" / "compiled" / "manifest.json"
AGENTS_DIR = ROOT / "agents"
SOLUTIONS_DIR = ROOT / "docs" / "solutions"
AUTOMEM_DIR = Path(os.environ.get(
    "ANTIGRAVITY_AUTOMEM_DIR",
    str(Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory"),
))

# episodic — full conversation-history index written by the superpowers
# episodic-memory plugin (mechanical SessionStart hook; ~23k exchanges for this
# repo). Scoped to this repo's project key by default; override with
# ANTIGRAVITY_EPISODIC_PROJECTS (comma-separated project keys, or "all" for
# cross-project recall).
EPISODIC_DB = Path(os.environ.get(
    "ANTIGRAVITY_EPISODIC_DB",
    str(Path.home() / ".config" / "superpowers" / "conversation-index" / "db.sqlite"),
))
_episodic_env = os.environ.get("ANTIGRAVITY_EPISODIC_PROJECTS", "").strip()
if _episodic_env.lower() == "all":
    EPISODIC_PROJECTS: Optional[List[str]] = None
elif _episodic_env:
    EPISODIC_PROJECTS = [p.strip() for p in _episodic_env.split(",") if p.strip()]
else:
    EPISODIC_PROJECTS = ["-" + str(ROOT).strip("/").replace("/", "-").replace(" ", "-")]

ALL_SOURCES = ("sovereign", "notion", "automem", "wiki", "agents", "episodic", "solutions", "prompts", "catalog")

_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how",
    "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "what",
    "when", "with", "i", "my", "we", "our", "you", "your", "do", "does",
}


def _tokens(text: str) -> List[str]:
    return [t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(t) > 2 and t not in _STOPWORDS]


def _query_catalog(query: str, top_k: int) -> Dict[str, Any]:
    """The work catalog (2026-08-20): the librarian's permanent census. Lets any
    session find prior work by half-remembered phrase BEFORE rebuilding it."""
    try:
        import work_catalog as wc
        q_tokens = _tokens(query)
        results = []
        for r in wc.load_catalog().values():
            hay = " ".join([str(r.get("title") or ""), r.get("k", ""),
                            " ".join(r.get("tags") or []), r.get("arena") or ""])
            score = _overlap_score(q_tokens, hay)
            if score > 0:
                snippet = str(r.get("title") or r.get("k"))[:200]
                if r.get("resume"):
                    snippet += f"  [{r['resume']}]"
                elif r.get("path"):
                    snippet += f"  [{r['path']}]"
                results.append({
                    "source": "catalog", "via": r.get("kind") or "row",
                    "score": score + (0.5 if r.get("merit") else 0),
                    "id": r.get("k"), "pinned": False,
                    "snippet": snippet,
                    "path": r.get("brief") or r.get("path") or "",
                })
        results.sort(key=lambda x: x["score"], reverse=True)
        return {"results": results[:top_k]}
    except Exception as e:  # noqa: BLE001
        return {"results": [], "degraded": f"catalog: {e}"}


def _overlap_score(query_tokens: List[str], text: str) -> float:
    """Fraction of query tokens present in text (0..1). Cheap, deterministic."""
    if not query_tokens:
        return 0.0
    hay = set(_tokens(text))
    hits = sum(1 for t in query_tokens if t in hay)
    return round(hits / len(query_tokens), 3)


# ──────────────────────────────────────────────────────────────────
# sovereign — vector path with deterministic FTS5 fallback
# ──────────────────────────────────────────────────────────────────
def _query_sovereign(query: str, workspace: Optional[str], top_k: int) -> Dict[str, Any]:
    # Primary: the existing vector retrieval (pinned rules + cosine ranking).
    try:
        sys.path.insert(0, str(ROOT / "execution"))
        from memory_retrieve import retrieve_context
        ctx = retrieve_context(query, workspace=workspace, top_k=top_k)
        results = [{
            "source": "sovereign",
            "via": r.get("source_tier", "vector"),
            "score": float(r.get("score", 0.0)),
            "id": r.get("id", ""),
            "pinned": bool(r.get("pinned")),
            "snippet": (r.get("content") or "")[:300],
            "path": str(SOVEREIGN_DB),
        } for r in ctx.get("results", [])]
        if results:
            return {"results": results, "degraded": None}
    # memory_embed raises SystemExit (not Exception) on a missing API key —
    # catch both so a keyless environment degrades to FTS instead of dying.
    except (Exception, SystemExit) as exc:
        vec_error = str(exc)[:120]
    else:
        vec_error = "vector path returned 0 results"

    # Fallback: FTS5 (then LIKE) directly against sovereign.db — no network.
    try:
        q_tokens = _tokens(query)
        if not SOVEREIGN_DB.exists() or not q_tokens:
            return {"results": [], "degraded": f"sovereign: {vec_error}; no db/tokens for fallback"}
        con = sqlite3.connect(f"file:{SOVEREIGN_DB}?mode=ro", uri=True)
        rows: List[tuple] = []
        try:
            match = " OR ".join(q_tokens[:8])
            rows = con.execute(
                "SELECT m.id, m.content, m.pinned, m.freshness FROM memories_fts f "
                "JOIN memories m ON m.rowid = f.rowid WHERE memories_fts MATCH ? LIMIT ?",
                (match, top_k * 2),
            ).fetchall()
        except sqlite3.Error:
            like = f"%{q_tokens[0]}%"
            rows = con.execute(
                "SELECT id, content, pinned, freshness FROM memories "
                "WHERE content LIKE ? ORDER BY freshness DESC LIMIT ?",
                (like, top_k * 2),
            ).fetchall()
        finally:
            con.close()
        results = []
        for rid, content, pinned, freshness in rows:
            results.append({
                "source": "sovereign",
                "via": "fts_fallback",
                "score": _overlap_score(q_tokens, content) * (1.2 if pinned else 1.0),
                "id": rid,
                "pinned": bool(pinned),
                "snippet": (content or "")[:300],
                "path": str(SOVEREIGN_DB),
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k],
                "degraded": f"sovereign vector path unavailable ({vec_error}); used FTS fallback"}
    except Exception as exc:
        return {"results": [], "degraded": f"sovereign: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# notion — network-free search over the nightly local mirror
# ──────────────────────────────────────────────────────────────────
def _query_notion_mirror(query: str, top_k: int) -> Dict[str, Any]:
    try:
        q_tokens = _tokens(query)
        if not SOVEREIGN_DB.exists() or not q_tokens:
            return {"results": [], "degraded": None}
        toks = q_tokens[:8]
        clauses = ["lower(coalesce(title, '') || ' ' || coalesce(content_excerpt, '')) LIKE ?" for _ in toks]
        params: List[Any] = [f"%{t}%" for t in toks]
        params.append(max(top_k * 20, 80))
        sql = (
            "SELECT page_id, db_name, title, content_excerpt, last_edited_at "
            "FROM notion_mirror WHERE " + " OR ".join(clauses) +
            " ORDER BY last_edited_at DESC LIMIT ?"
        )
        con = sqlite3.connect(f"file:{SOVEREIGN_DB}?mode=ro", uri=True)
        try:
            con.execute("PRAGMA query_only=ON")
            rows = con.execute(sql, params).fetchall()
        finally:
            con.close()
        results = []
        for page_id, db_name, title, excerpt, edited in rows:
            hay = f"{title or ''} {excerpt or ''}"
            results.append({
                "source": "notion",
                "via": "local_mirror",
                "score": _overlap_score(q_tokens, hay),
                "id": page_id,
                "pinned": False,
                "snippet": f"[{db_name}] {title or '(untitled)'} — {(excerpt or '')[:220]}",
                "path": f"https://www.notion.so/{str(page_id).replace('-', '')}",
                "last_edited_at": edited,
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except sqlite3.OperationalError as exc:
        return {"results": [], "degraded": f"notion mirror unavailable: {str(exc)[:120]}"}
    except Exception as exc:
        return {"results": [], "degraded": f"notion mirror: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# automem — Claude Code user auto-memory (frontmatter descriptions)
# ──────────────────────────────────────────────────────────────────
def _query_automem(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not AUTOMEM_DIR.is_dir():
            return {"results": [], "degraded": f"automem dir missing: {AUTOMEM_DIR}"}
        q_tokens = _tokens(query)
        results = []
        for f in AUTOMEM_DIR.glob("*.md"):
            if f.name == "MEMORY.md":
                continue
            try:
                head = f.read_text(errors="ignore")[:1200]
            except OSError:
                continue
            desc = ""
            m = re.search(r"^description:\s*(.+)$", head, re.MULTILINE)
            if m:
                desc = m.group(1).strip()
            score = _overlap_score(q_tokens, f.stem.replace("-", " ").replace("_", " ") + " " + desc + " " + head)
            if score > 0:
                results.append({
                    "source": "automem",
                    "via": "frontmatter",
                    "score": score,
                    "id": f.stem,
                    "pinned": False,
                    "snippet": desc[:300] if desc else head.split("---")[-1].strip()[:300],
                    "path": str(f),
                })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"automem: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# wiki — knowledge/ manifest pointers
# ──────────────────────────────────────────────────────────────────
def _query_wiki(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not WIKI_MANIFEST.exists():
            return {"results": [], "degraded": "wiki manifest missing — run knowledge_compiler.py inventory"}
        manifest = json.loads(WIKI_MANIFEST.read_text())
        q_tokens = _tokens(query)
        results = []
        for entry in manifest.get("files", []):
            path = entry.get("path", "")
            hay = " ".join([
                Path(path).stem.replace("-", " ").replace("_", " "),
                str(entry.get("domain") or ""), str(entry.get("expert") or ""),
                str(entry.get("title") or ""),
            ])
            score = _overlap_score(q_tokens, hay)
            if score > 0:
                results.append({
                    "source": "wiki",
                    "via": "manifest",
                    "score": score,
                    "id": Path(path).stem,
                    "pinned": False,
                    "snippet": f"[{entry.get('domain', '?')} / {entry.get('expert', '?')}] "
                               f"{entry.get('words', '?')} words",
                    "path": path,
                })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"wiki: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# prompts — crown-jewel practitioner prompt registry (.agent/prompt-index.json,
# built by prompt_library.py). Mirrors _query_wiki's shape: cheap index scan,
# term overlap on title/skill/gist, returns pointers not content. Added
# 2026-07-10 so Chain Step-4 loading surfaces battle-tested prompts alongside
# memory hits (Farrice: "the structural practitioner-level execution gave me
# outstanding outputs"). Embedded example stats inside old prompts are style,
# never fact — the factual-grounding standard applies at deploy time.
# ──────────────────────────────────────────────────────────────────
PROMPT_INDEX = ROOT / ".agent" / "prompt-index.json"


def _query_prompts(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not PROMPT_INDEX.exists():
            return {"results": [], "degraded": "prompt index missing — run prompt_library.py build"}
        index = json.loads(PROMPT_INDEX.read_text())
        q_tokens = _tokens(query)
        results = []
        for e in index.get("entries", []):
            if e.get("kind") == "legacy-prompt":
                continue  # legacy dirs mirror the skill-prompt files — skip dupes
            hay = " ".join([e.get("title", ""), e.get("skill", "").replace("-", " "),
                            e.get("gist", "")])
            score = _overlap_score(q_tokens, hay)
            if score > 0:
                results.append({
                    "source": "prompts",
                    "via": "prompt-index",
                    "score": score,
                    "id": Path(e.get("path", "")).stem,
                    "pinned": False,
                    "snippet": f"[{e.get('skill', '?')}] {e.get('title', '')[:80]} — "
                               f"{e.get('gist', '')[:100]}",
                    "path": e.get("path", ""),
                })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"prompts: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# agents — per-agent memory/context.md, matched when query names the agent
# ──────────────────────────────────────────────────────────────────
def _query_agents(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not AGENTS_DIR.is_dir():
            return {"results": [], "degraded": "agents dir missing"}
        q_tokens = set(_tokens(query))
        results = []
        for ctx_file in AGENTS_DIR.glob("*/memory/context.md"):
            agent = ctx_file.parts[-3]
            name_tokens = set(_tokens(agent.replace("-", " ")))
            if not (name_tokens & q_tokens):
                continue
            try:
                head = ctx_file.read_text(errors="ignore")[:400]
            except OSError:
                continue
            results.append({
                "source": "agents",
                "via": "name_match",
                "score": round(len(name_tokens & q_tokens) / max(len(name_tokens), 1), 3),
                "id": agent,
                "pinned": False,
                "snippet": head.strip()[:300],
                "path": str(ctx_file),
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"agents: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# episodic — full conversation history (superpowers episodic-memory index).
# Read-only SQL against the `exchanges` table ONLY; never the vec_exchanges
# virtual table (needs the vec0 extension, unloadable in plain python3). The
# project filter uses idx_project to narrow ~133k rows to this repo's ~23k
# before the LIKE text scan.
# ──────────────────────────────────────────────────────────────────
def _query_episodic(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not EPISODIC_DB.exists():
            return {"results": [], "degraded": f"episodic db missing: {EPISODIC_DB}"}
        q_tokens = _tokens(query)
        if not q_tokens:
            return {"results": [], "degraded": None}
        toks = q_tokens[:6]
        params: List[Any] = []
        scope_sql = ""
        if EPISODIC_PROJECTS:
            placeholders = ",".join("?" for _ in EPISODIC_PROJECTS)
            scope_sql = f"project IN ({placeholders}) AND "
            params.extend(EPISODIC_PROJECTS)
        clauses = ["user_message LIKE ? OR assistant_message LIKE ?" for _ in toks]
        for t in toks:
            params.extend([f"%{t}%", f"%{t}%"])
        params.append(max(top_k * 20, 60))
        sql = (
            "SELECT id, session_id, user_message, assistant_message, timestamp, archive_path "
            f"FROM exchanges WHERE {scope_sql}(" + " OR ".join(clauses) + ") "
            "ORDER BY timestamp DESC LIMIT ?"
        )
        con = sqlite3.connect(f"file:{EPISODIC_DB}?mode=ro", uri=True)
        try:
            con.execute("PRAGMA query_only=ON")
            rows = con.execute(sql, params).fetchall()
        finally:
            con.close()
        results = []
        for rid, sid, umsg, amsg, ts, apath in rows:
            results.append({
                "source": "episodic",
                "via": "exchanges_like",
                "score": _overlap_score(q_tokens, (umsg or "") + " " + (amsg or "")),
                # dedup on the unique exchange id, never session_id (multiple
                # exchanges share a session and must not collapse to one)
                "id": rid or sid or ts,
                "pinned": False,
                "snippet": (umsg or "").strip()[:300],
                "path": apath or str(EPISODIC_DB),
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"episodic: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# solutions — docs/solutions/*.md frontmatter (Solution Recorder cards,
# 2026-07-07). Mirrors _query_wiki's shape: cheap frontmatter scan, term
# overlap on name+problem_signature+tags, stdlib only (no yaml dependency —
# regex extraction keeps this source degrading the same way wiki/agents do).
# ──────────────────────────────────────────────────────────────────
def _query_solutions(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not SOLUTIONS_DIR.is_dir():
            return {"results": [], "degraded": f"solutions dir missing: {SOLUTIONS_DIR}"}
        q_tokens = _tokens(query)
        results = []
        for f in SOLUTIONS_DIR.glob("*.md"):
            if f.name == "index.md":
                continue
            try:
                text = f.read_text(errors="ignore")
            except OSError:
                continue
            fm_match = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
            if not fm_match:
                continue
            fm_text = fm_match.group(1)
            name_m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
            sig_m = re.search(r"^problem_signature:\s*(.+)$", fm_text, re.MULTILINE)
            tags_m = re.search(r"^tags:\s*(.+)$", fm_text, re.MULTILINE)
            name = name_m.group(1).strip() if name_m else f.stem
            sig = sig_m.group(1).strip().strip('"').strip("'") if sig_m else ""
            tags = tags_m.group(1).strip() if tags_m else ""
            score = _overlap_score(q_tokens, f"{name} {sig} {tags}")
            if score > 0:
                results.append({
                    "source": "solutions",
                    "via": "frontmatter",
                    "score": score,
                    "id": f.stem,
                    "pinned": False,
                    "snippet": (sig or name)[:300],
                    "path": str(f.relative_to(ROOT)),
                })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"solutions: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# facade
# ──────────────────────────────────────────────────────────────────
def recall(
    query: str,
    top_k: int = 10,
    workspace: Optional[str] = None,
    sources: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Unified recall across all memory stores.

    Returns {query, results, degraded, by_source}. Ordering: sovereign
    pinned rules first (voice rules / banned moves must always surface),
    then everything else by score. Dedup by (source, id).
    """
    use = [s for s in (sources or ALL_SOURCES) if s in ALL_SOURCES]
    per_store = max(3, top_k)
    merged: List[Dict[str, Any]] = []
    degraded: List[str] = []
    by_source: Dict[str, int] = {}

    for name, fn in (
        ("sovereign", lambda: _query_sovereign(query, workspace, per_store)),
        ("notion", lambda: _query_notion_mirror(query, per_store)),
        ("automem", lambda: _query_automem(query, per_store)),
        ("wiki", lambda: _query_wiki(query, per_store)),
        ("agents", lambda: _query_agents(query, per_store)),
        ("episodic", lambda: _query_episodic(query, per_store)),
        ("solutions", lambda: _query_solutions(query, per_store)),
        ("prompts", lambda: _query_prompts(query, per_store)),
        ("catalog", lambda: _query_catalog(query, per_store)),
    ):
        if name not in use:
            continue
        out = fn()
        if out.get("degraded"):
            degraded.append(out["degraded"])
        by_source[name] = len(out.get("results", []))
        merged.extend(out.get("results", []))

    seen = set()
    deduped = []
    for r in merged:
        key = (r["source"], r["id"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)

    pinned = [r for r in deduped if r.get("pinned")]
    rest = sorted([r for r in deduped if not r.get("pinned")],
                  key=lambda r: r["score"], reverse=True)
    final = (pinned + rest)[:top_k]

    # Read instrumentation: only the rows that actually reached the caller.
    # Bumping inside _query_sovereign would over-count — that path returns
    # per_store candidates, many of which dedup/top_k then drops.
    _bump_sovereign_access([r["id"] for r in final
                            if r.get("source") == "sovereign" and r.get("id")])

    payload = {
        "query": query,
        "workspace": workspace,
        "result_count": len(final),
        "results": final,
        "by_source": by_source,
        "degraded": degraded or None,
    }
    _log_fire(payload)
    return payload


def _bump_sovereign_access(ids: List[str]) -> None:
    """Record that these sovereign rows were actually surfaced to a caller.

    Before this (2026-08-21), `memories.access_count` / `last_accessed` sat
    frozen at their one-time backfill values for every row in the table, so
    nothing downstream — decay, pruning, "which memories does the system
    actually use" — could tell a hot row from a dead one. Reads were the only
    signal never captured.

    Telemetry only, and deliberately cheap: short busy timeout so a locked db
    (harvest/distill writing) is skipped rather than waited on, and every
    exception swallowed. A failed bump must never degrade a recall.
    """
    if not ids or not SOVEREIGN_DB.exists():
        return
    try:
        con = sqlite3.connect(str(SOVEREIGN_DB), timeout=0.5)
        try:
            con.execute("PRAGMA busy_timeout = 500")
            placeholders = ",".join("?" * len(ids))
            con.execute(
                "UPDATE memories SET access_count = COALESCE(access_count, 0) + 1, "
                f"last_accessed = ? WHERE id IN ({placeholders})",
                [datetime.now(timezone.utc).isoformat(), *ids],
            )
            con.commit()
        finally:
            con.close()
    except Exception:
        pass


def _log_fire(payload: Dict[str, Any]) -> None:
    """Append a fire record to .agent/memory-facade-fires.jsonl.

    Without this the facade's "fires before every expert output" claim was
    unverifiable (2026-07-02 audit — the banned AI-memory-dependent
    observability pattern). Telemetry only; never raises, never blocks.
    """
    try:
        log_path = ROOT / ".agent" / "memory-facade-fires.jsonl"
        entry = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "query": payload["query"][:120],
            "result_count": payload["result_count"],
            "by_source": payload["by_source"],
            "degraded": payload["degraded"],
        }
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _print_human(payload: Dict[str, Any]) -> None:
    print(f"\n{'=' * 64}")
    print(f"  MEMORY FACADE — {payload['result_count']} results for: {payload['query'][:60]}")
    print(f"  sources: {payload['by_source']}")
    if payload.get("degraded"):
        for d in payload["degraded"]:
            print(f"  ⚠ degraded: {d}")
    print(f"{'=' * 64}")
    for r in payload["results"]:
        pin = " [PINNED]" if r.get("pinned") else ""
        print(f"\n  [{r['source']}/{r['via']}] {r['id']}{pin}  (score {r['score']})")
        print(f"    {r['snippet'][:200]}")
        print(f"    -> {r['path']}")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Unified memory recall (audit Fix 7)")
    ap.add_argument("query", help="Task intent / search query")
    ap.add_argument("--top", type=int, default=10, help="Max results (default 10)")
    ap.add_argument("--workspace", default=None, help="Sovereign workspace filter")
    ap.add_argument("--sources", default=None,
                    help=f"Comma-separated subset of {','.join(ALL_SOURCES)} (default: all)")
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()

    sources = args.sources.split(",") if args.sources else None
    payload = recall(args.query, top_k=args.top, workspace=args.workspace, sources=sources)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        _print_human(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
