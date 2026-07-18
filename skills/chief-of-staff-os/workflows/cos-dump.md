---
description: "/dump — anytime raw-thought capture with outsourced sorting: throw a tangled blob (ideas, tasks, worries, content sparks) at any hour; the counsel detangles it visibly, routes every piece to its home, and hands content sparks to the right engine. 30-second feel."
---

# /dump — Anytime Capture & Detangle

The pressure valve between briefings. Farrice blends things and does too much in one
thing — this command exists so he NEVER has to pre-sort a thought to capture it.
Whatever arrives (one line or a wall of voice-transcript), take it whole.

## Pre-Flight

Read `skills/chief-of-staff-os/genius.md` if not already hot (Detangle Rule + Capture
Discipline). No `cos_prep.py status` needed — this runs any time, marks nothing.

## Workflow

**Step 1 — Take it whole.** No questions first. Append verbatim to
`.agent/cos/journal/YYYY-MM-DD.md` under `## Raw` (create with header if missing).

**Step 2 — Detangle, visibly** (the Detangle Rule in genius.md). Name the separate
things back to him, numbered, each with its destination:

```
4 things in here:
1. Content spark (the gym-mirror line) → thought-bank ✓
2. Task for Jen's listing → open loop for tomorrow's brief ✓
3. New-offer itch → parked (Incumbency Rule) ✓
4. The sleep thing → Health context updated ✓
```

**Step 3 — Route each piece** per Capture Discipline (genius.md): content sparks →
`python3 execution/cos_prep.py capture --route inbox --text "..."` · durable facts →
`memory_store.py store --tier semantic` + life-context restamp · tasks/unresolved →
journal `## Open loops` · new-offer ideas → journal `## Parked` (one CFO sentence,
no debate) · goal-relevant → `goals.json`.

**Step 4 — Offer the handoff, don't do the work.** If a content spark has legs, name
its ONE next container: "`/linkedin-daily`", "`/parallax`", "`/writers-room` if it's a
draft". One line, his call, session over. A dump session NEVER becomes a work session.

## Output Schema

A `/dump` session produces exactly two visible artifacts plus the routing side-effects
— never a longer report:

1. **The verbatim journal append** — `.agent/cos/journal/YYYY-MM-DD.md` `## Raw`,
   his words unedited, timestamped by entry order (no summarizing, no cleanup).
2. **The numbered detangle reply** — the exact shape shown in Step 2: `N things in
   here:` followed by one numbered line per piece, each ending in `→ destination ✓`.
   Zero pieces silently merged, zero pieces silently dropped — the count in the
   header must match the count of numbered lines.
3. **The one-line handoff offer** (only if a piece has legs) — a single named
   container (`/linkedin-daily`, `/parallax`, `/writers-room`, etc.), never a
   started draft, never a second question.

Nothing else renders. No "here's what I'm thinking" preamble, no restated summary of
the raw dump beyond the numbered list itself.

## Quality Gate

Verbatim in journal · every piece named + routed (nothing silently absorbed) · zero
work performed beyond routing · ≤30-second feel for small dumps, ≤2 min for walls.
