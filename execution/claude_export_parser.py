#!/usr/bin/env python3
"""claude_export_parser.py — parse a claude.ai web data export into normalized, redacted artifacts.

The export (delivered as single-use-URL zips, extracted under `.tmp/claude-export/raw/`) holds:
    raw/batch-*/conversations.json   large JSON arrays of conversation objects (streamed, not loaded)
    raw/batch-0000/projects/*.json   one file per Claude Project (custom instructions + docs)
    raw/batch-0000/memories.json     Claude's own distilled memory about the user (high value)
    raw/batch-0000/users.json        account metadata (PII — skipped)

This stage is deterministic, $0, PII-redacted, idempotent. It streams each conversations.json one
element at a time via `ijson` (the files are 500MB–870MB — a naive `json.load` would need ~10GB RAM),
normalizes every conversation/project/memory, writes one redacted markdown file per item under the
git-ignored `.tmp/` tree, and writes a small `index.json` (the map every downstream stage reads).

Crucially it captures `chat_messages[].attachments[].extracted_content` — pasted prompts and custom
instructions live there, and they are often the richest, most reusable material in the whole export.

Usage:
    python3 execution/claude_export_parser.py parse            # stream + normalize all batches
    python3 execution/claude_export_parser.py parse --max 50   # smoke test (cap conversations)
    python3 execution/claude_export_parser.py parse --force    # rewrite existing md files
    python3 execution/claude_export_parser.py stats            # distributions from index.json
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import claude_export_state as st  # noqa: E402
from episodic_ingest import redact  # noqa: E402  (reuse the proven PII masker)

try:
    import ijson  # streaming JSON — required for the multi-hundred-MB conversation files
    _HAVE_IJSON = True
except ImportError:  # pragma: no cover - graceful fallback path
    _HAVE_IJSON = False


# ── Defensive key-alias tables (export field names drift across versions) ──
CONV_TITLE_KEYS = ("name", "title", "summary")
CONV_MSGS_KEYS = ("chat_messages", "messages")
CONV_PROJECT_KEYS = ("project_uuid", "project", "project_id")
MSG_ROLE_KEYS = ("sender", "role", "author")
MSG_TS_KEYS = ("created_at", "timestamp", "created")
PROJECT_INSTR_KEYS = ("prompt_template", "custom_instructions", "instructions")
PROJECT_DOCS_KEYS = ("docs", "documents", "knowledge")
DOC_CONTENT_KEYS = ("content", "text", "body")
DOC_NAME_KEYS = ("filename", "file_name", "name", "title")


def _first(d: Dict[str, Any], keys, default=""):
    for k in keys:
        v = d.get(k)
        if v not in (None, ""):
            return v
    return default


def _role(msg: Dict[str, Any]) -> str:
    raw = str(_first(msg, MSG_ROLE_KEYS, "")).lower()
    if raw in ("human", "user"):
        return "human"
    if raw in ("assistant", "ai", "claude"):
        return "assistant"
    return raw or "unknown"


def _msg_text(msg: Dict[str, Any]) -> str:
    """Flatten a message to text, handling BOTH the flat `text` shape and the
    `content:[{type:'text',text:...}]` block shape, then appending any attachment
    `extracted_content` (pasted prompts/instructions) labeled by filename."""
    base = msg.get("text") or ""
    if not base:
        parts = []
        for block in (msg.get("content") or []):
            if isinstance(block, dict) and block.get("text"):
                parts.append(block["text"])
        base = "\n".join(parts)

    extras = []
    for att in (msg.get("attachments") or []):
        if isinstance(att, dict):
            content = att.get("extracted_content")
            if content and str(content).strip():
                name = att.get("file_name") or att.get("filename") or "attachment"
                extras.append(f"\n\n[attachment: {name}]\n{content}")
    # `files` entries occasionally carry extracted text too
    for fl in (msg.get("files") or []):
        if isinstance(fl, dict):
            content = fl.get("extracted_content")
            if content and str(content).strip():
                name = fl.get("file_name") or "file"
                extras.append(f"\n\n[file: {name}]\n{content}")

    return base + "".join(extras)


# ── Normalization ──

def normalize_conversation(raw: Dict[str, Any]) -> Dict[str, Any]:
    cid = raw.get("uuid") or raw.get("id") or ""
    messages: List[Dict[str, str]] = []
    word_count = 0
    char_count = 0
    has_attachments = False
    for m in (_first(raw, CONV_MSGS_KEYS, []) or []):
        if not isinstance(m, dict):
            continue
        if m.get("attachments") or m.get("files"):
            has_attachments = True
        text = _msg_text(m)
        messages.append({
            "role": _role(m),
            "text": text,
            "ts": str(_first(m, MSG_TS_KEYS, "")),
        })
        word_count += len(text.split())
        char_count += len(text)
    return {
        "id": cid,
        "source": "claude.ai",
        "title": str(_first(raw, CONV_TITLE_KEYS, "")),
        "created": str(raw.get("created_at", "")),
        "updated": str(raw.get("updated_at", "")),
        "project_id": (_first(raw, CONV_PROJECT_KEYS, None) or None),
        "messages": messages,
        "message_count": len(messages),
        "word_count": word_count,
        "char_count": char_count,
        "has_attachments": has_attachments,
    }


def normalize_project(raw: Dict[str, Any]) -> Dict[str, Any]:
    docs = []
    for d in (_first(raw, PROJECT_DOCS_KEYS, []) or []):
        if isinstance(d, dict):
            content = str(_first(d, DOC_CONTENT_KEYS, ""))
            docs.append({
                "filename": str(_first(d, DOC_NAME_KEYS, "doc")),
                "content": content,
                "char_count": len(content),
            })
    return {
        "id": raw.get("uuid") or raw.get("id") or "",
        "name": str(raw.get("name", "")),
        "description": str(raw.get("description", "")),
        "custom_instructions": str(_first(raw, PROJECT_INSTR_KEYS, "")),
        "knowledge_docs": docs,
        "created": str(raw.get("created_at", "")),
        "conversation_ids": [],  # populated from the reverse map if conversations carry project ids
    }


# ── Markdown writers (redaction happens HERE — the privacy backstop) ──

def write_conversation_md(conv: Dict[str, Any]) -> Path:
    st.CONV_MD_DIR.mkdir(parents=True, exist_ok=True)
    path = st.CONV_MD_DIR / f"{conv['id']}.md"
    lines = [
        "---",
        f"id: {conv['id']}",
        f"source: claude.ai",
        f"title: {redact(conv['title'])}",
        f"created: {conv['created']}",
        f"updated: {conv['updated']}",
        f"project_id: {conv['project_id'] or ''}",
        f"message_count: {conv['message_count']}",
        f"word_count: {conv['word_count']}",
        f"has_attachments: {conv['has_attachments']}",
        "---",
        "",
        f"# {redact(conv['title']) or '(untitled)'}",
        "",
    ]
    for m in conv["messages"]:
        lines.append(f"## {m['role']}" + (f"  ·  {m['ts'][:19]}" if m["ts"] else ""))
        lines.append("")
        lines.append(redact(m["text"]))
        lines.append("")
    path.write_text("\n".join(lines))
    return path


def write_project_md(proj: Dict[str, Any]) -> Path:
    st.PROJ_MD_DIR.mkdir(parents=True, exist_ok=True)
    path = st.PROJ_MD_DIR / f"{proj['id']}.md"
    lines = [
        "---",
        f"id: {proj['id']}",
        f"type: project",
        f"name: {redact(proj['name'])}",
        f"created: {proj['created']}",
        f"has_instructions: {bool(proj['custom_instructions'].strip())}",
        f"doc_count: {len(proj['knowledge_docs'])}",
        "---",
        "",
        f"# Project: {redact(proj['name']) or '(unnamed)'}",
        "",
        f"_{redact(proj['description'])}_" if proj["description"] else "",
        "",
        "## Custom Instructions",
        "",
        redact(proj["custom_instructions"]) or "_(none)_",
        "",
    ]
    if proj["knowledge_docs"]:
        lines.append("## Knowledge Documents")
        lines.append("")
        for d in proj["knowledge_docs"]:
            lines.append(f"### {redact(d['filename'])}  ({d['char_count']} chars)")
            lines.append("")
            lines.append(redact(d["content"]))
            lines.append("")
    path.write_text("\n".join(lines))
    return path


def write_memories_md(memories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Claude's built-in Memory export — already-distilled context. High signal."""
    st.MEM_MD_DIR.mkdir(parents=True, exist_ok=True)
    out = []
    for i, mem in enumerate(memories):
        # the export uses {"conversations_memory": "..."} but be defensive about the key
        text = ""
        if isinstance(mem, dict):
            for v in mem.values():
                if isinstance(v, str) and v.strip():
                    text += ("\n\n" if text else "") + v
        elif isinstance(mem, str):
            text = mem
        if not text.strip():
            continue
        mid = f"claude-memory-{i:02d}"
        path = st.MEM_MD_DIR / f"{mid}.md"
        path.write_text(
            f"---\nid: {mid}\ntype: claude_builtin_memory\n---\n\n"
            f"# Claude Built-in Memory ({mid})\n\n{redact(text)}\n"
        )
        out.append({"id": mid, "char_count": len(text), "md_path": str(path.relative_to(ROOT))})
    return out


# ── Streaming iterators ──

def iter_conversations(path: Path):
    """Yield conversation dicts one at a time. Streams with ijson; falls back to
    json.load only for small files (the real export is far too large for that)."""
    if _HAVE_IJSON:
        with open(path, "rb") as f:
            for conv in ijson.items(f, "item"):
                yield conv
    else:  # pragma: no cover - fallback; will be slow/RAM-heavy on the real files
        data = json.loads(path.read_text())
        for conv in (data if isinstance(data, list) else [data]):
            yield conv


# ── Orchestration ──

def parse(raw_dir: Path, force: bool, max_conv: Optional[int]) -> Dict[str, Any]:
    state = st.load_state()
    state["download"]["manifest_path"] = str((raw_dir / "manifest.json"))

    index: Dict[str, Any] = {
        "generated_at": st._now(),
        "source_files": [],
        "conversation_count": 0,
        "project_count": 0,
        "memory_count": 0,
        "conversations": [],
        "projects": [],
        "memories": [],
    }

    # 1. Conversations — stream every batch's conversations.json
    conv_files = sorted(glob.glob(str(raw_dir / "*" / "conversations.json")))
    if not conv_files:
        print(f"⚠️  no conversations.json under {raw_dir}/*/ — is the export extracted there?")
    parsed = 0
    for cf in conv_files:
        cfp = Path(cf)
        index["source_files"].append({"path": str(cfp), "shape": "conversations"})
        batch = cfp.parent.name
        n = 0
        for raw in iter_conversations(cfp):
            if max_conv and parsed >= max_conv:
                break
            conv = normalize_conversation(raw)
            if not conv["id"]:
                continue
            md = st.CONV_MD_DIR / f"{conv['id']}.md"
            if force or not md.exists():
                write_conversation_md(conv)
            index["conversations"].append({
                "id": conv["id"], "title": redact(conv["title"]),
                "created": conv["created"], "updated": conv["updated"],
                "project_id": conv["project_id"], "message_count": conv["message_count"],
                "word_count": conv["word_count"], "char_count": conv["char_count"],
                "has_attachments": conv["has_attachments"], "batch": batch,
                "md_path": str(md.relative_to(ROOT)),
            })
            st.mark(state, "parsed", conv["id"], {"batch": batch})
            n += 1
            parsed += 1
            if parsed % 500 == 0:
                print(f"  … {parsed} conversations parsed")
        print(f"  {Path(cf).parent.name}/conversations.json → {n} conversations")
        if max_conv and parsed >= max_conv:
            break
    index["conversation_count"] = len(index["conversations"])

    # 2. Projects — one <uuid>.json per project (batch-0000/projects/)
    proj_files = sorted(glob.glob(str(raw_dir / "*" / "projects" / "*.json")))
    for pf in proj_files:
        try:
            raw = json.loads(Path(pf).read_text())
        except (json.JSONDecodeError, OSError):
            continue
        proj = normalize_project(raw)
        if not proj["id"]:
            continue
        md = st.PROJ_MD_DIR / f"{proj['id']}.md"
        if force or not md.exists():
            write_project_md(proj)
        index["projects"].append({
            "id": proj["id"], "name": redact(proj["name"]),
            "has_instructions": bool(proj["custom_instructions"].strip()),
            "instruction_chars": len(proj["custom_instructions"]),
            "doc_count": len(proj["knowledge_docs"]),
            "md_path": str(md.relative_to(ROOT)),
        })
    index["project_count"] = len(index["projects"])

    # 3. Claude's built-in memories (small, high value)
    mem_files = sorted(glob.glob(str(raw_dir / "*" / "memories.json")))
    for mf in mem_files:
        try:
            mems = json.loads(Path(mf).read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if isinstance(mems, dict):
            mems = [mems]
        index["memories"].extend(write_memories_md(mems))
    index["memory_count"] = len(index["memories"])

    # write index + state — but NEVER let a --max smoke test clobber the canonical
    # full index (parse rebuilds the index fresh each run, so a capped run would truncate it).
    st.EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    if max_conv:
        print(f"  ⚠️  --max {max_conv} smoke test: index.json NOT overwritten (would truncate).")
    else:
        st.INDEX_PATH.write_text(json.dumps(index, indent=2))
        state["counts"] = {
            "conversations": index["conversation_count"],
            "projects": index["project_count"],
            "memories": index["memory_count"],
        }
        st.save_state(state)

    print("\n─── PARSE SUMMARY ───")
    print(f"  conversations: {index['conversation_count']}")
    print(f"  projects:      {index['project_count']} "
          f"({sum(1 for p in index['projects'] if p['has_instructions'])} with instructions)")
    print(f"  memories:      {index['memory_count']}")
    print(f"  index:         {st.INDEX_PATH.relative_to(ROOT)}")
    print(f"  transcripts:   {st.NORMALIZED_DIR.relative_to(ROOT)}/ (git-ignored)")
    print("  next: python3 execution/claude_export_triage.py heuristic")
    return index


def stats() -> int:
    if not st.INDEX_PATH.exists():
        print("No index.json — run `parse` first.")
        return 1
    idx = json.loads(st.INDEX_PATH.read_text())
    convs = idx["conversations"]
    wc = sorted(c["word_count"] for c in convs) or [0]

    def pct(p):
        return wc[min(len(wc) - 1, int(len(wc) * p))]

    print("─── CLAUDE EXPORT · CORPUS STATS ───")
    print(f"  conversations: {len(convs)}")
    print(f"  projects:      {idx['project_count']} "
          f"({sum(1 for p in idx['projects'] if p['has_instructions'])} with custom instructions, "
          f"{sum(1 for p in idx['projects'] if p['doc_count'])} with docs)")
    print(f"  memories:      {idx['memory_count']}")
    print(f"  with attachments: {sum(1 for c in convs if c['has_attachments'])} conversations")
    print(f"  total messages:   {sum(c['message_count'] for c in convs)}")
    print(f"  word_count → p50 {pct(0.5)} · p90 {pct(0.9)} · p99 {pct(0.99)} · max {wc[-1]}")
    single = sum(1 for c in convs if c["message_count"] <= 2)
    print(f"  single-exchange (<=2 msgs): {single}  ·  substantive (>2): {len(convs) - single}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse a claude.ai web export into normalized artifacts")
    ap.add_argument("command", nargs="?", default="parse", choices=["parse", "stats"])
    ap.add_argument("--raw-dir", default=str(st.RAW_DIR), help="dir holding batch-*/ export folders")
    ap.add_argument("--force", action="store_true", help="rewrite existing markdown files")
    ap.add_argument("--max", type=int, help="cap conversations parsed (smoke test)")
    args = ap.parse_args()

    if args.command == "stats":
        return stats()
    if not _HAVE_IJSON:
        print("⚠️  ijson not installed — large conversation files may exhaust RAM. "
              "Install with: python3 -m pip install ijson")
    parse(raw_dir=Path(args.raw_dir), force=args.force, max_conv=args.max)
    return 0


if __name__ == "__main__":
    sys.exit(main())
