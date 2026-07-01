#!/usr/bin/env python3
"""claude_export_ingest.py — normalized claude.ai conversations → sovereign episodic tier.

Structurally a sibling of `episodic_ingest.py` (which bridges Claude Code/Codex CLI history).
This one bridges the *web* export: it reads the parser's `index.json`, writes ONE deterministic
episodic `milestone` record per conversation into `.memory/sovereign.db`, and (optionally) ingests
Claude's built-in memory and the project custom-instruction prompts.

Design rules (identical to the rest of the memory stack):
    - Deterministic by default: NO LLM, NO embedding at ingest time (zero surprise spend).
      Embedding is a later, explicit, cost-gated step (`memory_embed.py backfill --dry-run`).
    - Idempotent: dedup by conversation uuid in `source_ids`, tagged `metadata.source="claude_export"`.
    - PII-redacted: reuse `episodic_ingest.redact` (email/phone/6+digit) — the parser already
      redacted the markdown; this redacts the summary content too (belt and suspenders).
    - Workspace-scoped: every row tagged `workspace="claude-export"` so a future distill run can be
      scoped to this corpus and NOT flood the weekly 50–200-row clustering job (see R4 in the plan).
    - Local-only: never calls Notion. Curated insight reaches Notion later via the existing
      `notion_api.py capture` path, never raw transcripts.

Usage:
    python3 execution/claude_export_ingest.py preview                 # dry-run (default), zero writes
    python3 execution/claude_export_ingest.py run                     # write episodic rows
    python3 execution/claude_export_ingest.py run --max 100           # smoke test
    python3 execution/claude_export_ingest.py run --only-bucket knowledge-grade
    python3 execution/claude_export_ingest.py run --include-projects  # + 112 project prompts (procedural)
    python3 execution/claude_export_ingest.py run --no-memory         # skip Claude built-in memory

After a run, complete the L2 loop (cost-gated — thousands of rows):
    python3 execution/memory_embed.py backfill --dry-run
    python3 execution/memory_embed.py backfill --max-rows 500
    python3 execution/memory_review.py list        # (only if you ran a scoped distill; see plan R4)
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import claude_export_state as st  # noqa: E402
from memory_store import DB_PATH, store_memory  # noqa: E402
from episodic_ingest import redact, _is_substantive  # noqa: E402  (reuse proven helpers)

INGEST_SOURCE = "claude_export"
WORKSPACE = "claude-export"
SUMMARY_CAP = 240  # chars, matches episodic_ingest sizing


def ingested_conversation_ids() -> set:
    """Conversation ids already promoted into sovereign (dedup on re-run) — mirrors
    episodic_ingest.ingested_session_ids but keyed on the claude_export source tag."""
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    try:
        rows = con.execute(
            "SELECT source_ids FROM memories WHERE tier='episodic' AND metadata LIKE ?",
            (f'%"{INGEST_SOURCE}"%',),
        ).fetchall()
    finally:
        con.close()
    seen = set()
    for (sids,) in rows:
        try:
            for s in json.loads(sids or "[]"):
                seen.add(s)
        except (json.JSONDecodeError, TypeError):
            continue
    return seen


def _load_index() -> Dict[str, Any]:
    if not st.INDEX_PATH.exists():
        raise FileNotFoundError(
            f"{st.INDEX_PATH} missing — run `python3 execution/claude_export_parser.py parse` first")
    return json.loads(st.INDEX_PATH.read_text())


def _triage_bucket_map() -> Dict[str, str]:
    """conversation_id → bucket, if triage has run (else empty)."""
    tix = st.TRIAGE_DIR / "triage-index.json"
    if not tix.exists():
        return {}
    data = json.loads(tix.read_text())
    out: Dict[str, str] = {}
    for bucket, items in (data.get("buckets") or {}).items():
        for it in items:
            out[it["id"]] = bucket
    return out


def _read_conv_md(md_path: str) -> List[Dict[str, str]]:
    """Pull role-labeled turns back out of a normalized md file (for the summary)."""
    p = ROOT / md_path
    if not p.exists():
        return []
    turns: List[Dict[str, str]] = []
    role = None
    buf: List[str] = []
    for line in p.read_text().splitlines():
        if line.startswith("## "):
            if role is not None:
                turns.append({"role": role, "text": "\n".join(buf).strip()})
            role = line[3:].split("·")[0].strip()
            buf = []
        elif role is not None:
            buf.append(line)
    if role is not None:
        turns.append({"role": role, "text": "\n".join(buf).strip()})
    return turns


def summarize_conversation(meta: Dict[str, Any], bucket: Optional[str]) -> Dict[str, Any]:
    """One deterministic episodic record per conversation — no LLM."""
    turns = _read_conv_md(meta["md_path"])
    intent = ""
    for t in turns:
        if t["role"] == "human" and _is_substantive(t["text"]):
            intent = t["text"]
            break
    if not intent and turns:
        intent = turns[0]["text"]
    outcome = ""
    for t in reversed(turns):
        if t["role"] == "assistant" and t["text"]:
            outcome = t["text"]
            break

    intent = redact(intent)[:SUMMARY_CAP]
    outcome = redact(outcome)[:SUMMARY_CAP]
    title = redact(meta.get("title", ""))[:120]
    content = (
        f"claude.ai · {meta.get('created', '')[:10]} · {meta.get('message_count', 0)} msgs"
        f"{' · ' + bucket if bucket else ''}\n"
        f"Title: {title}\n"
        f"Intent: {intent}\n"
        f"Outcome: {outcome}"
    )
    metadata = {
        "source": INGEST_SOURCE,
        "conversation_id": meta["id"],
        "title": title,
        "created": meta.get("created", ""),
        "message_count": meta.get("message_count", 0),
        "word_count": meta.get("word_count", 0),
        "project_id": meta.get("project_id"),
        "triage_bucket": bucket,
        "has_attachments": meta.get("has_attachments", False),
        "md_path": meta["md_path"],
    }
    return {"content": content, "metadata": metadata, "source_ids": [meta["id"]]}


def _ingest_builtin_memory(index: Dict[str, Any], dry_run: bool, summary: Dict[str, Any]) -> None:
    """Claude's own distilled memory — the single highest-value context artifact.
    Stored as episodic/milestone with high_value flag (not auto-promoted to semantic —
    the human-review gate owns that)."""
    for mem in index.get("memories", []):
        mid_key = mem["id"]
        if mid_key in ingested_builtin():
            continue
        p = ROOT / mem["md_path"]
        text = redact(p.read_text()) if p.exists() else ""
        # strip frontmatter/heading, keep the body
        body = text.split("---", 2)[-1].strip()
        content = f"Claude built-in memory ({mid_key}) — user profile & context\n{body[:1800]}"
        summary["builtin_memory"] += 1
        if dry_run:
            print(f"[would ingest builtin-memory] {mid_key} · {len(body)} chars")
            continue
        store_memory(
            tier="episodic", category="milestone", content=content,
            metadata={"source": INGEST_SOURCE, "kind": "builtin_memory", "id": mid_key,
                      "high_value": True, "md_path": mem["md_path"]},
            source_ids=[mid_key], workspace=WORKSPACE, silent=True,
        )
        print(f"[ingested builtin-memory] {mid_key}")


def ingested_builtin() -> set:
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    try:
        rows = con.execute(
            "SELECT source_ids FROM memories WHERE metadata LIKE ?",
            ('%"builtin_memory"%',),
        ).fetchall()
    finally:
        con.close()
    seen = set()
    for (sids,) in rows:
        try:
            for s in json.loads(sids or "[]"):
                seen.add(s)
        except (json.JSONDecodeError, TypeError):
            continue
    return seen


def _ingest_projects(index: Dict[str, Any], dry_run: bool, summary: Dict[str, Any]) -> None:
    """Project custom-instruction prompts → procedural/template rows (searchable, reusable).
    These are ALSO surfaced as skill candidates by the triage menu; ingesting them here just
    makes them retrievable through memory_facade."""
    already = ingested_conversation_ids()
    for p in index.get("projects", []):
        if not p.get("has_instructions"):
            continue
        pid = p["id"]
        if pid in already:
            continue
        md = ROOT / p["md_path"]
        body = redact(md.read_text()) if md.exists() else ""
        content = f"Claude Project prompt: {redact(p['name'])}\n{body[:1600]}"
        summary["projects"] += 1
        if dry_run:
            print(f"[would ingest project] {redact(p['name'])[:60]} · {p['instruction_chars']} chars")
            continue
        store_memory(
            tier="procedural", category="template", content=content,
            metadata={"source": INGEST_SOURCE, "kind": "project_prompt", "project_id": pid,
                      "name": redact(p["name"]), "md_path": p["md_path"]},
            source_ids=[pid], workspace=WORKSPACE, silent=True,
        )
        print(f"[ingested project] {redact(p['name'])[:60]}")


def run(dry_run: bool, max_conv: Optional[int], only_bucket: Optional[str],
        include_projects: bool, include_memory: bool) -> Dict[str, Any]:
    index = _load_index()
    state = st.load_state()
    already = ingested_conversation_ids()
    bucket_map = _triage_bucket_map()

    convs = index["conversations"]
    if only_bucket:
        convs = [c for c in convs if bucket_map.get(c["id"]) == only_bucket]
    # Skip genuinely empty conversations (abandoned/image/voice chats with no text —
    # ~14% of the export). Nothing to remember; keeps the episodic tier clean.
    non_empty = [c for c in convs if c.get("word_count", 0) > 0]
    skipped_empty = len(convs) - len(non_empty)
    candidates = [c for c in non_empty if c["id"] not in already]
    # newest first; cap if requested
    candidates.sort(key=lambda c: c.get("created", ""), reverse=True)
    if max_conv:
        candidates = candidates[:max_conv]

    summary = {
        "total_conversations": len(index["conversations"]),
        "eligible": len(non_empty), "skipped_empty": skipped_empty,
        "already_ingested": len([c for c in non_empty if c["id"] in already]),
        "to_ingest": len(candidates), "written": 0, "dry_run": dry_run,
        "only_bucket": only_bucket, "projects": 0, "builtin_memory": 0,
    }

    for c in candidates:
        rec = summarize_conversation(c, bucket_map.get(c["id"]))
        if dry_run:
            if summary["written"] < 8:  # sample preview only
                print(f"[would ingest] {c['id'][:12]} · {c.get('message_count', 0)} msgs · "
                      f"{bucket_map.get(c['id']) or 'untriaged'}")
                print(f"    {rec['content'][:150].replace(chr(10), ' / ')}")
            summary["written"] += 1
            continue
        mid = store_memory(
            tier="episodic", category="milestone", content=rec["content"],
            metadata=rec["metadata"], source_ids=rec["source_ids"],
            workspace=WORKSPACE, silent=True,
        )
        if mid:
            summary["written"] += 1
            st.mark(state, "ingested", c["id"], {"memory_id": mid})
            if summary["written"] % 500 == 0:
                print(f"  … {summary['written']} conversations ingested")

    if include_memory:
        _ingest_builtin_memory(index, dry_run, summary)
    if include_projects:
        _ingest_projects(index, dry_run, summary)

    if not dry_run:
        st.save_state(state)

    print("\n─── CLAUDE EXPORT INGEST SUMMARY ───")
    print(f"  corpus: {summary['total_conversations']} conversations"
          f"{' · bucket=' + only_bucket if only_bucket else ''}")
    print(f"  eligible (non-empty): {summary['eligible']} · skipped empty: {summary['skipped_empty']} "
          f"· already ingested: {summary['already_ingested']}")
    print(f"  conversations {'to ingest' if dry_run else 'written'}: {summary['written']}"
          f"{' (dry-run)' if dry_run else ''}")
    if include_projects:
        print(f"  project prompts (procedural): {summary['projects']}")
    if include_memory:
        print(f"  builtin memory: {summary['builtin_memory']}")
    if not dry_run and summary["written"]:
        print("  next: python3 execution/memory_embed.py backfill --dry-run   # cost-gate before embedding")
    return summary


def main() -> int:
    ap = argparse.ArgumentParser(description="Ingest claude.ai export → sovereign episodic tier")
    ap.add_argument("command", nargs="?", default="preview", choices=["preview", "run"])
    ap.add_argument("--max", type=int, help="cap conversations ingested (smoke test)")
    ap.add_argument("--only-bucket", help="ingest only this triage bucket (needs triage-index.json)")
    ap.add_argument("--include-projects", action="store_true",
                    help="also ingest 112 project custom-instruction prompts as procedural rows")
    ap.add_argument("--no-memory", action="store_true", help="skip Claude built-in memory ingest")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    dry = args.command == "preview"
    summary = run(dry_run=dry, max_conv=args.max, only_bucket=args.only_bucket,
                  include_projects=args.include_projects, include_memory=not args.no_memory)
    if args.json:
        print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
