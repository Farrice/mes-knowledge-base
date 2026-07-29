#!/usr/bin/env python3
"""PostToolUse(Read) guard: one-line redirect when a superseded doc is read.

Compass, never cage — never blocks the read, just tells the session (this one
or a cold-start one months from now) that the file it reached for has a
successor. Exit 0 always. Only speaks on .md files with frontmatter
status: superseded|archived.
"""
import json
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


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
        return 0
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    status = fm.get("status", "").lower()
    if status not in {"superseded", "archived"}:
        return 0
    successor = fm.get("superseded_by", "")
    msg = f"CANON GUARD (deterministic): {p.name} is {status.upper()}"
    msg += f" — build on `{successor}` instead." if successor else " — check the project CANON.md for the live doc."
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
