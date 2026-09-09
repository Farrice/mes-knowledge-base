---
description: The Library — the librarian's permanent catalog of everything ever worked on, with Worth-Resuming shelf, search, triage nudges, and the weekly shelf report
---

# /catalog — The Library (2026-08-20)

The intelligence database behind the Readout OS. Every work thread the sweep
has EVER seen (not just the last fourteen days), plus deliverables, extractions,
knowledge, guides, solutions and briefs — one permanent ledger, one surface.

## Open it

```bash
open "http://127.0.0.1:8765/library"
```

Shelves: **★ Worth resuming** (merit + dormant — the lost-merit fix) · Live
threads · Librarian-recommends-killing (collapsed nudges, your word only) ·
The stacks (everything, tag facets + search) · Graveyard.

## Find something half-remembered

```bash
python3 execution/work_catalog.py find "supplement teardown thing"
```

Also a `memory_facade` source (`--sources catalog`) — any session can ask the
library before rebuilding what already exists.

## How it stays current — AUTOMATIC (Farrice's ruling 2026-08-20)

- **Every session end** (Claude Code AND Codex, same Stop hook): the session's
  work is filed in the catalog, and if real work shipped without a narrative,
  the hook asks the session ONCE to deposit three lines (Purpose · Current
  State · Remaining Priority) via `handoff_store save`. Single-fire, never loops.
- **Every sweep** (nightly launchd, refresh button, manual): census → catalog
  merge — the safety net for crashed sessions.
- **Sundays 07:00** (`com.antigravity.shelf-report`): the weekly shelf report
  renders into the Briefing Room; the session-start digest carries the library
  one-liner whenever items are worth resuming.
- **Triage** (`brief_synthesis.py triage`): judged resume | shelve | kill calls
  with a one-line why, validated fail-closed (no digits/paths in judged prose),
  rendered as chips + nudges. Recommendations only — never auto-acts.

## Data

`.agent/catalog/catalog.jsonl` (latest-wins per key; merit sticky: good
verdict · finalize ≥8 · pinned) · `.agent/catalog/triage.json` (judged calls)
· weekly brief at `deliverables/research-briefs/library-shelf-report/`.
Merge manually: `python3 execution/work_catalog.py merge`.
