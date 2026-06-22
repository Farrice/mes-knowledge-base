---
description: "Phase 6 freshness — keep the map a living document with a quarterly light pass + 1–2× yearly deep rebuild, add new word-for-word quotes, flag new phrasing/worries/wishes, write a dated change-log at the top (which becomes its own asset), and optionally register a recurring refresh job via /schedule"
---

# /ctm-refresh

Keep the map alive — freshness is the edge. A Customer Truth Map is not finished, it's kept. Pull a fresh batch of recent quotes into an existing map, flag what's NEW, note what's GONE, and write a dated change-log entry at the top — over time that log is the competitive-intelligence asset competitors aren't tracking. "A map you refresh is worth ten times a map you build once and forget."

## Trigger
`/ctm-refresh`

## Workflow
`skills/customer-truth-map/workflows/ctm-refresh.md`

## Quick Use
Provide an existing map. Pick a cadence: quarterly light pass (recent quotes from 1–2 best sources) vs 1–2× yearly deep rebuild (full re-gather, new-vs-old comparison). Runs prompt P11. Same verbatim discipline as the build; never invent a "trend" quote.

## Pipeline
1 Gather the fresh batch (verbatim, source+date-tagged, via `/ctm-clean`) → 2 Merge, flag NEW (phrasing/worries/wishes) + note GONE (P11) → 3 Write the dated change-log entry (stacked, + a "what this signals" read) → 4 Optional: register a recurring job via `/schedule`

## Output
The updated map + the change-flags (NEW/GONE per category) + the dated change-log entry stacked at top + (if recurring) the `/schedule` routine proposal (cloud cron, user-confirmed).

## Stacks With
→ tool-wiring fallback chain for the fresh batch · `/ctm-triangulate` if a deep rebuild surfaces a new audience split
→ `/schedule` (recurring cloud job) · fact-verifier for new real-world claims
