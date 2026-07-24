---
description: "Riley Brown's unglamorous ops tier — stage social posts as drafts (Typefully), generate constraint-encoded booking links (Cal.com), and keep files organized. The distribution layer that makes the content tier compound. Everything stages behind approval; nothing auto-publishes."
---

# /riley-distribution-ops — Scheduling · Booking Links · File Hygiene

The operations tier the roster lacks (Riley's video workflows #6 Buffer/Typefully, #7 Google Drive, #8 Cal.com). Same human-gate philosophy throughout (Pattern 9): the agent *stages*, the human *ships*. Two of these need a one-time free key; when a key is missing, deliver the ready artifact + activation note — **never fake a staged post or a live link.**

## Pre-Flight Gate

Load `genius.md` first. Pick the sub-move:
- **Schedule a post** → `/post-scheduler` (needs `TYPEFULLY_API_KEY`).
- **Booking link with shaped availability** → `/scheduling-links` (needs `CALCOM_API_KEY`).
- **File hygiene** → organize `deliverables/` / Drive by convention.

Content/voice/quality gates happen **upstream** — this workflow never writes copy itself.

## Skill Acquisition

- `genius.md` — Patterns 9 (draft terminus), 11 (zero-plugin API bootstrap), Exemplar 5 (Cal.com constraint link)
- Live infra: `.agent/workflows/post-scheduler.md`, `.agent/workflows/scheduling-links.md`
- `references/source-quotes.md` — quotes 13 (Cal.com bootstrap), 14 (draft terminus)

## Execution

### A. Stage a social post — `/post-scheduler`
1. Take the finished post from any upstream content workflow (voice/slop gates already passed).
2. Platform-fit pass (X: hook line first, line breaks, no hashtag salad). Riley's caption move: borrow cadence from a scraped reference via `/scrape-creator` when asked ("use a caption just like [creator]").
3. Stage as **draft, unscheduled** by default (`Typefully POST /v1/drafts`); an explicit time is the only exception and is echoed back for confirmation. Riley: "I did say to create a draft, so it's not actually scheduled."
4. Hand back the Typefully draft URL. Missing key → deliver platform-ready text + activation note.

### B. Constraint-encoded booking link — `/scheduling-links`
1. Shape availability from intent — Riley's podcast logic: "the only days that should be available are in September and October... stick with this Tuesday, Thursday schedule." Strategic shaping is the point (near-term for hot topics, far-out for evergreen guests).
2. Create the event-type via Cal.com API v2; **verify by GET before handing over** — a link that 404s in a guest's inbox is the failure mode. His zero-plugin bootstrap: "get an API key paste it in and say create a skill that fully controls cal.com."
3. Open the link headless (Playwright, read-only) and confirm visible availability matches intent ("No availability in August... it created a custom link").
4. `--with-email` → draft the outreach carrying the link via `/inbox-drafts` (draft only, never send).

### C. File hygiene
Organize outputs into populated, convention-named subfolders (`deliverables/[client]/…`), no loose root files, never empty scaffold (per project-org memory). Riley's #7 was "less visual but more practical" — the point is durable order, not a demo.

## Content Type Adaptations

| Sub-move | Adaptation |
|---|---|
| X/Twitter post | Typefully draft; hook-first formatting |
| LinkedIn/IG | no open scheduler API — stage into `_active/farrice-brand/` pipeline or a client production sheet |
| High-value guest booking | tightly shaped window + matching outreach draft |
| Recurring booking need | promote to an automation via `/riley-automations` |

## Output Requirements

- Posts staged as **drafts** (Typefully URL returned); explicit schedule time echoed for confirmation only.
- Booking links **verified live** with correct availability before delivery; availability restated in plain language.
- Files in convention-named subfolders.
- Missing key → ready artifact + activation note, never a faked link/post.

Execution prompt: references/prompts-v2/distribution-staging-package.md — honor its Output Contract.

## Quality Gate

Nothing auto-publishes (draft-first default)? · Booking link verified live (not assumed)? · Availability shaping stated back plainly? · Outreach draft (if any) passes voice + slop gates and is draft-only? · No faked staged assets when a key is absent?
