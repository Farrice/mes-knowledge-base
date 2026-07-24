---
description: Draft and stage social posts for scheduling (Typefully for X; Buffer-style flow) — Riley Brown pattern; needs Farrice's Typefully API key to go live
---

# /post-scheduler — Draft → Staged Social Post

Riley Brown's pattern #6: content gets created in the agent, staged in a scheduler as a **draft**, and Farrice approves/schedules from the scheduler UI. Same human-gate philosophy as `/inbox-drafts`: the agent stages, the human ships.

> **ACTIVATION REQUIRED (one-time, free, ~3 min of Farrice's hands)**
> 1. Typefully account (free tier) → Settings → API → create key → add `TYPEFULLY_API_KEY=` to root `.env`
> 2. That's it — Typefully's `POST /v1/drafts` covers create-draft + schedule. Buffer's public API is closed to new apps (verified 2026-07); Typefully is the route for X. LinkedIn/Instagram staging continues through existing flows (content into `_active/farrice-brand/` pipeline or client production sheets) until a scheduler with an open API earns a slot.

## Usage

```
/post-scheduler [content or content ref] [--when "next Tuesday 9am" | --draft]
```

## Steps

1. **Content in**: take the finished post (from any content workflow — this workflow never writes copy itself; voice/quality gates happen upstream).
2. **Caption/format pass**: platform-fit check (X: line breaks, hook line first, no hashtag salad). Riley's move: when caption style matters, borrow cadence from a scraped reference via `/scrape-creator` — "use a caption just like [creator]."
3. **Stage**: `curl -s -X POST https://api.typefully.com/v1/drafts -H "X-API-KEY: $TYPEFULLY_API_KEY"` with content + optional `schedule-date`. Default is **draft, unscheduled** unless Farrice gave an explicit time.
4. **Hand back the link**: Typefully draft URL. Farrice reviews, schedules, or kills from there.
5. If `TYPEFULLY_API_KEY` is missing → stop at step 2, deliver the platform-ready text + the activation note above. Never fake a staged post.

## Quality Gate

- Nothing auto-publishes. Draft-first is the default; explicit schedule time is the only exception, and it's echoed back for confirmation.
- Post text passed its upstream voice/slop gates before arriving here.
