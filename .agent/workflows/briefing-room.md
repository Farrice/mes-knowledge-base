---
description: Open the Briefing Room — regenerate deliverables/research-briefs/index.html (sidebar filters, priority/category, pagination, quick-copy) and launch it in the browser
---

# /briefing-room — open the library

One move: rebuild the index (picks up any new briefs) and open it — through the live server when it's running (buttons write for real + side-window auto-reload), static file otherwise.

// turbo
```bash
if curl -s --max-time 2 http://127.0.0.1:8765/ping | grep -q pulse; then open "http://127.0.0.1:8765/room"; else python3 execution/brief_library.py --open; fi
```

Want it live? `python3 execution/pulse_serve.py --open` first (localhost only, idle-exits after 2h).

Full authoring/rendering doctrine (schema, section kinds, mission reports, context packs): `.agent/workflows/briefs.md`. Cards carry `path` (copy .md abs path — file-access tools) and `copy brief` (entire brief inline — chat LLMs). Brief JSONs may set `category` (string) + `priority` (1-3) for the sidebar; both optional.
