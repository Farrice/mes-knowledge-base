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

## Quality Gate

≤1 page · every line sourced from real state files (no invention) · zero writes.
