---
description: "Riley Brown's 'act in the future' — promote a useful one-off into a recurring or scheduled automation in plain language, replacing Zapier-style workflow building. The trigger-mindset is the technique; the human-gate terminus stays intact."
---

# /riley-automations — Act in the Future (One-Off → Automation)

Riley's Pattern 15 (cross-video confirmed): "Anything useful now, ask yourself, would this be useful on a recurring basis or at a very specific time?... AI, because it's just like talking to a human, will just set up the automation." His demo: "daily best video hook outline every morning at 9am" — his sidebar shows a real "Create morning episode automation" thread. This collapses the specialist skill of automation-building into a spoken sentence. **The trigger-mindset is the reusable technique**, not any particular scheduler.

## Pre-Flight Gate

Load `genius.md` first. Fire when:
- A one-off just proved useful and the answer to "would this be useful recurring or scheduled?" is yes.
- The task is already a **named skill/workflow** (run `/riley-turn-it-into-a-skill` first if not) — you automate a skill, not a raw prompt.
- Any outbound step in the automation still ends in a **draft/link behind approval** — recurring ≠ auto-send.

## Skill Acquisition

- `genius.md` — Pattern 15 (act in the future), 9 (draft terminus stays)
- `references/source-quotes.md` — quote on recurring automations
- Antigravity infra: `directives/steering-loop.md` Forge Radar (flag the build); launchd analogs (`com.antigravity.evolution-auto`); `execution/*` cron patterns

## Execution

1. **Name the trigger.** Recurring (daily/weekly) or specific-time? What fires it (schedule, an inbox event, a new scrape)? Riley's framing: "act in the future."
2. **Confirm it wraps a named skill.** The automation calls a frozen workflow (e.g. `/scrape-creator` → hook-outline every morning), not an ad-hoc prompt. If it's not yet a skill, stop and `/riley-turn-it-into-a-skill`.
3. **Keep the human-gate.** Any produce/outbound step still terminates in an editable draft/link — the automation *prepares*, Farrice *ships*. A morning hook-outline lands as a draft to review, never an auto-post.
4. **Wire it deterministically, not on AI-memory.** Per feedback memory (AI-memory-dependent observability is banned), back the schedule with a deterministic mechanism (cron/launchd/scheduled task), not "the agent will remember." Surface the build in one Forge-Radar line; ship only with an in-session proof-of-concept.
5. **Prove it once.** Run the automation's body manually end-to-end; confirm the artifact + link land. Only then schedule.
6. **Log the loop.** Note what recurs, where the output lands, and the review step. Corrections to the underlying skill compound (Pattern 3).

## Content Type Adaptations

| Automation | Adaptation |
|---|---|
| Daily hook-outline | `/scrape-creator` a source every morning → draft outline for review |
| Weekly competitor watch | `/riley-ad-spy` on a rotating competitor → new-ad digest |
| Recurring booking sweep | `/scheduling-links` for a standing guest cadence |
| Inbox rhythm | `/riley-inbox-drafts` on a schedule → drafts to review (never auto-send) |

## Output Requirements

- A recurring/scheduled automation wrapping a **named** skill, backed by a deterministic scheduler.
- Human-gate terminus intact (drafts/links, not auto-execution).
- A one-time manual proof-of-concept run before scheduling.
- Forge-Radar flag (one line) for the build.

Execution prompt: references/prompts-v2/durable-asset-forge.md — honor its Output Contract.

## Quality Gate

Wraps a named skill (not a raw prompt)? · Deterministically scheduled (not AI-memory-dependent)? · Every outbound step still human-gated? · Proven once manually before going live? · The recurring output lands somewhere reviewable with a link?
