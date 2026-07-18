---
description: "/cos status — read-only state of the union: goals, commitments, streaks, dues, top threads on one page. No capture, no marks."
---

# /cos status — State of the Union

## Pre-Flight

`python3 execution/cos_prep.py status` · read `.agent/cos/goals.json`, `.agent/cos/decisions.md` (open commitments), latest `.agent/cos/briefs/*.md`. Optionally `python3 execution/handoff_store.py threads` for the live top-5.

## Workflow

Render ONE page, no more:

```
# State of the Union — YYYY-MM-DD

## Goals
| Goal | Status | Last reviewed |
(from goals.json — plain language, one line each)

## Open commitments        (from decisions.md — item · review date · verdict due?)
## This week               (streak · daily done? · board due/overdue · check-ins due)
## Top threads             (top 5 from handoff_store)
## The one thing           (single CEO-seat sentence: what matters most right now)
```

Read-only: no journal writes, no marks, no memory writes. If something surfaces that he wants to act on → "That's a session: `/cos daily` (capture it) or `/cos weekly` (board it)."

## Output Schema

Exactly the five sections shown in the Workflow template above, in that order, and
nothing appended after "The one thing":

1. **Goals** — a table pulled verbatim from `goals.json` fields (name, status,
   last_reviewed) rendered in plain language, never re-summarized or re-interpreted.
2. **Open commitments** — from `decisions.md` only; each line is `item · review date ·
   verdict due?` — an empty section renders "no open commitments," never omitted.
3. **This week** — streak count, daily-done boolean, board due/overdue flag, any
   check-ins due — four data points, sourced from `cos_prep.py status` JSON, no more.
4. **Top threads** — top 5 from `handoff_store.py threads`, ranked as returned; fewer
   than 5 real threads means fewer lines, never padded to 5.
5. **The one thing** — exactly one CEO-seat sentence, no seat attribution needed (this
   is a status page, not an advisory), grounded in whatever is most time-sensitive
   across the four sections above it.

Length ceiling: one screen. If the render exceeds ~1 page, cut Top threads to 3 before
cutting anything else — threads are the least time-sensitive section.

## Quality Gate

≤1 page · every line sourced from real state files (no invention) · zero writes.
