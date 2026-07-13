---
name: "AI Carousel Content Engine — Publish Pack"
source_prompt: born-v2
skill: ai-carousel-content-engine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building the publish pack — the final packaging stage of the AI Carousel Content Engine, where a reviewed carousel becomes something that can actually ship: to Instagram, LinkedIn, a client, or a weekly content pipeline (workflow 07). This stage assumes the carousel has already passed review (`/carousel-review`); it packages a finished asset, it does not fix a broken one.

## Input Required

- `[CAROUSEL_SCRIPT]` — the reviewed, finished slide-by-slide copy (needed for the cover line and caption).
- `[TITLE]` and `[AUDIENCE]`.
- `[DELIVERY_TARGETS]` — which of: Instagram, LinkedIn, client delivery, weekly content pipeline. Each has distinct notes (see below); do not produce generic notes that ignore this.
- `[OWNED_CONTENT_LINK]` — the article, guide, offer, lead magnet, or client conversation this carousel should route back to (Genius Pattern 5: Owned-Content Loop). If none exists, flag this as a gap rather than inventing a link.
- `[CTA_PREFERENCE]` — save/share/comment/click, or a client-specific action, if one is already decided.

## Execution Protocol

**Step 1 — Draft the caption from the carousel's own cover line, not from scratch.** The caption should open on (or echo) the slide 1 title, then name the gap the carousel closes — most people leave the underlying idea trapped in its original form (long article, raw conversation, unstructured insight); this carousel turns it into something save-able, share-able, and usable. Close with a save/engage prompt tied to the real use case ("save this for your next content sprint," not a bare "like and follow").

**Step 2 — Write platform notes per target, not one generic note.** Per workflow 07 and the engine's own defaults:
- *Instagram*: favor stronger visual contrast and a shorter caption than the other channels.
- *LinkedIn*: use the caption to add behind-the-scenes context (why this was made, what it's for) and a softer CTA than a hard sales ask.
- *Client delivery*: the handoff bundle must include `carousel-script.md`, `gpt-image-2-prompt.json`, and `review-checklist.md` together — a caption alone is not a client deliverable.
- *Weekly content pipeline*: note where this carousel sits in the cadence and what source feeds the next one, if that's known.

**Step 3 — Build CTA options, not a single locked CTA**, unless `[CTA_PREFERENCE]` already decided one. Offer a save-for-later option, an engagement-bait option (comment a keyword for the workflow/resource), and a direct-to-owned-content option (read the full piece on the owned site). Every CTA option must resolve to `[OWNED_CONTENT_LINK]` or an equivalent real pathway — a CTA with no owned-content pathway is a named failure condition (Quality Rubric).

**Step 4 — Restate the audience line explicitly** in the pack so whoever ships this (Farrice, a client, a VA) doesn't have to reconstruct who it's for from the caption alone.

## Output Contract

A publish pack containing: a caption draft (opens on/echoes the cover line, names the gap closed, closes with a specific save/engage prompt), platform notes for each `[DELIVERY_TARGETS]` entry (not a single generic note), a CTA options list (2-3 options, each tied to a real pathway), and an explicit audience line. If client delivery is a target, the pack must name the full handoff bundle (script + design prompt + review checklist), not just the caption.

## Output Skeleton

```
# Publish Pack — [TITLE]

## Caption Draft
[Opens on/echoes the slide 1 hook line, names the gap this carousel closes, closes with a specific save/engage prompt]

## Platform Notes
- Instagram: [contrast/caption-length note specific to this carousel]
- LinkedIn: [behind-the-scenes context + soft CTA note specific to this carousel]
- Client delivery: [confirms handoff bundle = carousel-script.md + gpt-image-2-prompt.json + review-checklist.md]
- Weekly pipeline: [cadence placement note, if applicable]

## CTA Options
- [Save-for-later option]
- [Engagement-bait option, e.g. comment a keyword]
- [Direct-to-owned-content option, tied to OWNED_CONTENT_LINK]

## Audience
[AUDIENCE]
```

## Quality Gate

- Does the caption draft actually reference the carousel's own cover line rather than reading as a generic template caption?
- Does every requested delivery target in `[DELIVERY_TARGETS]` get its own distinct note, rather than one note reused across all of them?
- Does every CTA option resolve to a real, named pathway (`[OWNED_CONTENT_LINK]` or equivalent), with none left as a dead-end "follow for more"?
- If client delivery is a target, does the pack explicitly name the full handoff bundle rather than just the caption?
- If `[OWNED_CONTENT_LINK]` was not supplied, does the pack flag that gap rather than inventing a link?

## Creative Latitude

The caption is a copywriting task, not a fill-in-the-blank — earn the same standard as any other piece of Farrice's copy: specific, source-grounded, no generic "viral carousel" language (a named failure condition). Push the CTA options toward what would actually work for this audience and mission rather than defaulting to the three stock options in the skeleton — if a client-specific action (book a call, join a waitlist, reply with a word) fits better than save/comment/click, use it. Platform notes should reflect genuine judgment about how this specific carousel's content and tone shift across Instagram vs. LinkedIn, not a copy-pasted general rule.

## Deploy When

- A carousel has passed review and needs to be packaged for actual publishing or client handoff — the last stage before the asset leaves the production pipeline.
