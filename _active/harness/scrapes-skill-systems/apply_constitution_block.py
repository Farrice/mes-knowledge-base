#!/usr/bin/env python3
"""One-time: insert the shared-scrapes-skill-systems markers into CLAUDE.md and
AGENTS.md right after the shared-agent-skills block, then let the compiler fill
them.

Run from the repo root inside a lane:
    python3 _active/harness/scrapes-skill-systems/apply_constitution_block.py
    python3 execution/constitution_compiler.py sync
"""
from pathlib import Path

NAME = "shared-scrapes-skill-systems"
ANCHOR = "<!-- END:shared-agent-skills -->"

for target in ("CLAUDE.md", "AGENTS.md"):
    path = Path(target)
    text = path.read_text()
    if NAME in text:
        print(f"{target}: markers already present")
        continue
    if ANCHOR not in text:
        raise SystemExit(f"{target}: anchor block missing")
    text = text.replace(
        ANCHOR,
        ANCHOR + f"\n<!-- BEGIN:{NAME} -->\n(pending sync)\n<!-- END:{NAME} -->",
        1,
    )
    path.write_text(text)
    print(f"{target}: markers inserted")

print("now run: python3 execution/constitution_compiler.py sync")
