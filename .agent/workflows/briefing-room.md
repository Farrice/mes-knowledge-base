---
description: Open the Briefing Room — regenerate deliverables/research-briefs/index.html (sidebar filters, priority/category, pagination, quick-copy) and launch it in the browser
---

# /briefing-room — open the library

One move: rebuild the index (picks up any new briefs) and open it.

// turbo
```bash
python3 execution/brief_library.py --open
```

Full authoring/rendering doctrine (schema, section kinds, mission reports, context packs): `.agent/workflows/briefs.md`. Cards carry `path` (copy .md abs path — file-access tools) and `copy brief` (entire brief inline — chat LLMs). Brief JSONs may set `category` (string) + `priority` (1-3) for the sidebar; both optional.
