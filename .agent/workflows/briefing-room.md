---
description: Open the Briefing Room — regenerate deliverables/research-briefs/index.html (sidebar filters, priority/category, pagination, quick-copy) and launch it in the browser
---

# /briefing-room — open the library

One move: rebuild the index (picks up any new briefs) and open it — through the live server when it's running (buttons write for real + side-window auto-reload), static file otherwise.

The rebuild now verifies every card twice before it reports success: its
relative target must exist beside the static Room, and its repo-relative target
must exist beneath the active live-server root. The explicit `verify` command
also checks every context-pack path using portable repo-relative identity. A
failed route blocks the new index instead of shipping a clickable 404.

// turbo
```bash
if curl -s --max-time 2 http://127.0.0.1:8765/ping | grep -q pulse; then open "http://127.0.0.1:8765/room"; else python3 execution/brief_library.py --open; fi
```

Want it live? `python3 execution/pulse_serve.py --open` first (localhost only, idle-exits after 2h).

Integrity-only check: `python3 execution/brief_library.py verify`.

Portable handoff (selected briefs, no live server or repository required):

```bash
python3 execution/brief_export.py <slug> [<slug> ...] --output /path/to/new-bundle --zip
python3 execution/verify_brief_export.py /path/to/new-bundle.zip
```

Private mode is the default and includes safely allowed context sources. For an
outward-facing HTML-only package, add `--audience share`; it uses the existing
share-safe renderer and still requires a human prose review before sending.

Full authoring/rendering doctrine (schema, section kinds, mission reports, context packs): `.agent/workflows/briefs.md`. Cards carry `path` (copy .md abs path — file-access tools) and `copy brief` (entire brief inline — chat LLMs). Brief JSONs may set `category` (string) + `priority` (1-3) for the sidebar; both optional.
