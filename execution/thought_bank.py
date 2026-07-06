#!/usr/bin/env python3
"""thought_bank.py — deterministic capture spine for the thought-bank.

Built 2026-07-06 because the thought-bank (Farrice's first-person raw-thought
stream — distinct from episodic conversation capture) had exactly ONE entry
since 2026-05-05: capture depended on the model remembering to route a piece
there mid-conversation. That's the exact pattern banned by feedback
`ai-memory-dependent-observability` — infra must never depend on a human (or
Claude) remembering a step; every deterministic backstop needs a physical
write path.

This CLI is that write path. It is the ONE writer of
`_active/farrice-brand/thought-bank/inbox/YYYY-MM-DD.md` going forward
(`cos_prep.py capture --route inbox` now delegates here — see that file).

Subcommands:
    capture "<text>" [--theme T] [--source S]
                                Append a timestamped entry to today's inbox
                                file AND mirror it into the sovereign episodic
                                tier (tier=episodic, category=milestone) so it
                                flows into the existing weekly distill ->
                                flagged_review -> memory_review.py pipeline
                                like every other episodic record. Idempotent
                                per (day, normalized-first-60-chars) — re-running
                                the same capture is a silent no-op, not a dup.
    list [--days N]            Print entries captured in the last N days
                                (default 7), most recent first.
    stats                      Inbox totals: files, entries, themes, sources,
                                date range.

No LLM calls. Stdlib + the existing `memory_store.store_memory_silent` helper
(same insert path `memory_review.py` uses to promote reviewed rules — no new
schema). The sovereign-memory mirror is best-effort: if `.memory/sovereign.db`
is unavailable for any reason, the inbox file write still succeeds (the
markdown file is the source of truth Farrice reads; the DB mirror is the
plumbing that feeds distillation).

Usage:
    python3 execution/thought_bank.py capture "the gym-mirror line" --theme presence-vs-screens
    python3 execution/thought_bank.py list --days 3
    python3 execution/thought_bank.py stats
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
INBOX = REPO_ROOT / "_active" / "farrice-brand" / "thought-bank" / "inbox"

sys.path.insert(0, str(REPO_ROOT / "execution"))

DEDUPE_RE = re.compile(r"<!-- thought_bank:dedupe=([0-9a-f]+) -->")
HEADER_RE = re.compile(r"^## (\d{2}:\d{2}) — (.*)$")
THEME_RE = re.compile(r"^\*Theme: (.+)\*$")
SOURCE_RE = re.compile(r"^\*Source: (.+)\*$")


def _today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _normalize(text: str, n: int = 60) -> str:
    """Whitespace-collapsed, lowercased prefix — the dedupe key."""
    return " ".join(text.strip().lower().split())[:n]


def _dedupe_hash(text: str) -> str:
    import hashlib
    return hashlib.sha1(_normalize(text).encode("utf-8")).hexdigest()[:16]


def _first_n_words(text: str, n: int = 8) -> str:
    words = text.strip().split()
    if not words:
        return "(untitled)"
    snippet = " ".join(words[:n])
    if len(words) > n:
        snippet += "…"
    return snippet


def _inbox_path(day: str) -> Path:
    return INBOX / f"{day}.md"


def existing_dedupe_hashes(day: Optional[str] = None) -> set:
    """Dedupe hashes already present in the given day's inbox file (default today)."""
    day = day or _today()
    path = _inbox_path(day)
    if not path.exists():
        return set()
    return set(DEDUPE_RE.findall(path.read_text()))


def is_duplicate(text: str, day: Optional[str] = None) -> bool:
    """True if this text (by normalized-first-60-chars) was already captured
    for the given day. Used by the nightly backstop scan to avoid double-writes
    when the model already ran `capture` mid-conversation."""
    return _dedupe_hash(text) in existing_dedupe_hashes(day)


def capture(text: str, theme: str = "", source: str = "manual",
            mirror_to_sovereign: bool = True, silent: bool = False) -> Dict:
    """Append one entry to today's inbox file; mirror into sovereign episodic
    tier so weekly distill picks it up. Returns a result dict; never raises on
    the sovereign-mirror failure path (best-effort)."""
    text = text.strip()
    if not text:
        raise SystemExit("Error: empty capture text")

    day = _today()
    if is_duplicate(text, day):
        if not silent:
            print(f"Already captured today (dedupe match) — skipping: {_first_n_words(text)}")
        return {"file": str(_inbox_path(day)), "day": day, "skipped": "duplicate"}

    INBOX.mkdir(parents=True, exist_ok=True)
    path = _inbox_path(day)
    if not path.exists():
        path.write_text(f"# Inbox — {day}\n\n")

    stamp = datetime.now().strftime("%H:%M")
    lines = [f"## {stamp} — {_first_n_words(text)}\n\n", f"{text}\n"]
    if theme:
        lines.append(f"*Theme: {theme}*\n")
    lines.append(f"*Source: {source}*\n")
    lines.append(f"<!-- thought_bank:dedupe={_dedupe_hash(text)} -->\n\n")

    with path.open("a") as f:
        f.write("".join(lines))

    memory_id = None
    if mirror_to_sovereign:
        try:
            from memory_store import store_memory_silent  # noqa: E402
            memory_id = store_memory_silent(
                tier="episodic",
                category="milestone",
                content=f"[thought-bank] {text[:800]}",
                metadata={
                    "source": "thought_bank",
                    "theme": theme,
                    "capture_source": source,
                    "day": day,
                },
            )
        except Exception:
            memory_id = None  # inbox write already succeeded; DB mirror is best-effort

    if not silent:
        print(f"Captured to {path.relative_to(REPO_ROOT)}"
              + (f" (sovereign mirror: {memory_id})" if memory_id else " (sovereign mirror: skipped)"))

    return {"file": str(path), "day": day, "timestamp": f"{day} {stamp}",
             "theme": theme, "source": source, "memory_id": memory_id}


def _parse_day_entries(path: Path) -> List[Dict]:
    entries: List[Dict] = []
    cur: Optional[Dict] = None
    for line in path.read_text().splitlines():
        m = HEADER_RE.match(line)
        if m:
            if cur:
                entries.append(cur)
            cur = {"time": m.group(1), "title": m.group(2), "theme": "", "source": ""}
            continue
        if cur is None:
            continue
        tm = THEME_RE.match(line.strip())
        if tm:
            cur["theme"] = tm.group(1)
            continue
        sm = SOURCE_RE.match(line.strip())
        if sm:
            cur["source"] = sm.group(1)
            continue
    if cur:
        entries.append(cur)
    return entries


def list_entries(days: int = 7) -> List[Dict]:
    if not INBOX.exists():
        return []
    cutoff = datetime.now().date() - timedelta(days=days)
    out: List[Dict] = []
    for path in sorted(INBOX.glob("*.md")):
        try:
            day = datetime.strptime(path.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if day < cutoff:
            continue
        for e in _parse_day_entries(path):
            e["day"] = path.stem
            out.append(e)
    out.sort(key=lambda e: (e["day"], e["time"]), reverse=True)
    return out


def cmd_list(days: int) -> int:
    entries = list_entries(days)
    if not entries:
        print(f"No thought-bank entries in the last {days} day(s).")
        return 0
    print(f"Thought-bank — last {days} day(s), {len(entries)} entr{'y' if len(entries) == 1 else 'ies'}:\n")
    for e in entries:
        tag = f" [{e['theme']}]" if e["theme"] else ""
        src = f" ({e['source']})" if e["source"] else ""
        print(f"  {e['day']} {e['time']}{tag}{src} — {e['title']}")
    return 0


def cmd_stats() -> int:
    if not INBOX.exists():
        print("Thought-bank inbox is empty (no directory yet).")
        return 0
    files = sorted(INBOX.glob("*.md"))
    all_entries: List[Dict] = []
    for path in files:
        for e in _parse_day_entries(path):
            e["day"] = path.stem
            all_entries.append(e)

    themes: Dict[str, int] = {}
    sources: Dict[str, int] = {}
    for e in all_entries:
        if e["theme"]:
            themes[e["theme"]] = themes.get(e["theme"], 0) + 1
        if e["source"]:
            sources[e["source"]] = sources.get(e["source"], 0) + 1

    days_sorted = sorted(p.stem for p in files)
    print(f"Files:        {len(files)}")
    print(f"Entries:      {len(all_entries)}")
    print(f"Date range:   {days_sorted[0] if days_sorted else '—'} → {days_sorted[-1] if days_sorted else '—'}")
    if themes:
        print("Themes:")
        for t, c in sorted(themes.items(), key=lambda kv: -kv[1]):
            print(f"  {t}: {c}")
    if sources:
        print("Sources:")
        for s, c in sorted(sources.items(), key=lambda kv: -kv[1]):
            print(f"  {s}: {c}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Deterministic thought-bank capture spine")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("capture", help="Append a timestamped entry to today's inbox")
    c.add_argument("text", help="The raw thought text")
    c.add_argument("--theme", default="", help="Theme tag (matches thought-bank/themes/*.md slugs)")
    c.add_argument("--source", default="manual", help="Where this came from (dump, cos-daily, backstop-episodic-scan, manual...)")
    c.add_argument("--no-sovereign-mirror", action="store_true", help="Skip the sovereign.db mirror write")

    l = sub.add_parser("list", help="List recent entries")
    l.add_argument("--days", type=int, default=7)

    sub.add_parser("stats", help="Inbox totals")

    args = p.parse_args()

    if args.cmd == "capture":
        capture(args.text, theme=args.theme, source=args.source,
                mirror_to_sovereign=not args.no_sovereign_mirror)
        return 0
    if args.cmd == "list":
        return cmd_list(args.days)
    if args.cmd == "stats":
        return cmd_stats()
    return 1


if __name__ == "__main__":
    sys.exit(main())
