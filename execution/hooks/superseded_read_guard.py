#!/usr/bin/env python3
"""PostToolUse(Read) guard: one-line redirect when a stale doc is read.

Compass, never cage — never blocks the read, just tells the session (this one
or a cold-start one months from now) that the file it reached for is not the
live one. Exit 0 always.

Two branches:

1. FRONTMATTER — `status: superseded|archived`, redirect to `superseded_by`.

2. RECORD (2026-08-07) — the filename LEADS with YYYY-MM-DD-, so it is a
   session record, not truth. This is the mechanical answer to the
   canonical-stamp trap: a stamped snapshot became an over-powerful attractor
   and every later session cited the frozen file instead of the accumulated
   whole. Proof at the time: CANON.md marked a 2026-07-28 profile doc
   canonical while the real work was the 2026-08-06 rebuild.

   Path-only, so it costs nothing and works on any file — including one with
   no frontmatter at all, which is 279 of 298 docs in the folder that caused
   this. It names the living doc in the same folder wherever one exists.
"""
import json
import os
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
RECORD_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[-_]")

PINNED = {"INDEX.md", "README.md", "CLAUDE.md", "RISKS.md", "CANON.md",
          "CAMPAIGN.md", "MOVED.md", "AGENTS.md", "CODEX.md", "GEMINI.md",
          "START-HERE.md"}


def _living_siblings(p: Path, limit: int = 3) -> list[str]:
    """Undated .md files beside this record — the things to read instead."""
    try:
        sibs = [c.name for c in p.parent.iterdir()
                if c.is_file() and c.suffix == ".md"
                and c.name not in PINNED
                and not RECORD_RE.match(c.name)]
    except OSError:
        return []
    sibs.sort(key=lambda n: os.path.getmtime(p.parent / n), reverse=True)
    return sibs[:limit]


def record_branch(p: Path) -> int:
    if not RECORD_RE.match(p.name):
        return 0
    stamp = p.name[:10]
    living = _living_siblings(p)
    msg = (f"RECORD (deterministic): {p.name} is a dated record from {stamp} "
           f"— a receipt of one session, not the current truth.")
    if living:
        msg += " The living doc" + ("s here are: " if len(living) > 1 else " here is: ")
        msg += ", ".join(f"`{n}`" for n in living) + "."
    else:
        msg += (" Nothing undated sits beside it, so there is no living doc in "
                "this folder yet — read START-HERE.md before building on this.")
    print(msg)
    return 0


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    if payload.get("tool_name") != "Read":
        return 0
    fp = payload.get("tool_input", {}).get("file_path", "")
    if not fp.endswith(".md"):
        return 0
    p = Path(fp)
    if not p.exists():
        return 0
    try:
        head = p.read_text(errors="replace")[:1500]
    except OSError:
        return 0
    m = FM_RE.match(head)
    if not m:
        # No frontmatter is the common case (279 of 298 docs in the folder that
        # prompted this). The record rule still applies — it is path-only.
        return record_branch(p)
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    status = fm.get("status", "").lower()
    if status not in {"superseded", "archived"}:
        # An explicit successor outranks the date rule; otherwise fall through.
        return record_branch(p)
    successor = fm.get("superseded_by", "")
    msg = f"CANON GUARD (deterministic): {p.name} is {status.upper()}"
    msg += f" — build on `{successor}` instead." if successor else " — check the project CANON.md for the live doc."
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
