# Farrice Content Signal Loop

This directory is the persistent state root for Farrice Cain's evidence-backed
content ideation system.

## Current deployment

- Creator: Farrice Cain
- Primary platform: LinkedIn
- Deployed: 2026-07-30
- Upstream skill system: Kieran Flanagan Content Signal Loop
- Winning-profile status: **PROVISIONAL**
- Reason: human taste verdicts and approved strategy exist, but live post
  analytics do not.

## State map

| Surface | Purpose |
|---|---|
| `audience-profile.md` | Durable audience tensions, triggers, and anti-triggers |
| `profiles/winning-content-linkedin.md` | Platform-specific transferable formulas |
| `evidence/source-inventory.md` | Local and external evidence register |
| `runs/ideas-2026-07-30-linkedin.md` | First evidence-backed ideation run |
| `queues/content-queue.md` | Human-authorized active production queue |

## Evidence law

1. Human approval is taste evidence, not performance evidence.
2. Approved strategy is direction evidence, not proof that a format wins.
3. External coverage is a current-attention signal unless a primary source
   independently establishes the factual claim.
4. A PROVISIONAL Winning Content Profile lowers confidence on every dependent
   idea.
5. No queue item is finished content. Promotion hands the idea to a separate
   creation workflow.

## Refresh triggers

- Add LinkedIn impressions, saves, substantive comments, profile views, and
  qualified conversations when real post analytics become available.
- Refresh trend-backed items when their `stale_after` date arrives.
- Review this state after every five published LinkedIn posts or monthly,
  whichever comes first.

