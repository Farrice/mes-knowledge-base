---
description: "The surpass-Riley analysis pass — take a scraped creator corpus and write a per-post 'why it works' verdict grounded in a named hook lens, excluding sponsored posts with retained evidence. Riley's workflow stops at raw data; this adds the judgment."
---

# /riley-creator-analyzer — Why-It-Works Analysis Pass

Riley scrapes and asks the agent *"tell me why he's such an effective short form creator."* His workflow stops at a table of raw data + a why-effective note. This is the **surpass move** (`/scrape-creator` step 2): a per-post "why it works" verdict grounded in an existing hook lens rather than freehand opinion — because taste is the load-bearing input (Hidden Knowledge #3), and a lens makes the taste legible and reusable.

## Pre-Flight Gate

Load `genius.md` first. Proceed if:
- A scraped corpus already exists in the Social Intelligence DB (run `/riley-scrape-to-skill` step 1 first if not).
- You can name the lens the verdicts will use (kallaway / diandra / jenny-hoyos / sky-tan) — don't freehand.
- The intent is *understanding a winner*, not producing content yet (that's downstream).

## Skill Acquisition

- `genius.md` — Patterns 1 (examples-over-instructions), 5 (authenticity filter); Rubric (Example-groundedness, Epistemic honesty)
- Live infra: `.agent/workflows/scrape-creator.md` step 2 (the analysis layer + lens options)
- Hook lenses: `skills/kallaway-*` (content psychology), `diandra-hook-architect` / `diandra-rehook-teardown`, `jenny-hoyos-viral-os` (retention), `sky-tan-format-engine` (short-form format)

## Execution

1. **Read back the batch** (`Batch` property = the scrape tag). Order by observed engagement.
2. **Exclude sponsored, keep the evidence.** Riley: "the top 10 videos that has the most engagement that are not sponsored... those can be boosted. So it's like fake." State each exclusion — boosted posts poison the pattern set.
3. **Per-post verdict, lens-grounded.** For each non-sponsored winner, write into the `Analysis` property: the hook mechanism (named against the lens), why it likely stops the scroll, the retention/format move, and the CTA/loop. Cite the lens ("Kallaway pattern-interrupt", "Diandra rehook") — not "it's engaging."
4. **Synthesize the voice signature** (what recurs across the winners): opening move, pacing, CTA shape, distinctive tics — the reusable pattern, in specifics, not adjectives.
5. **Flag epistemic status.** Engagement ≠ proof of *why*; label the verdict as an informed read of the copy/structure, not measured causation.
6. **Route forward (options, not steps).** Pattern-rich? Mark `Extract Candidate` and graduate to `/riley-scrape-to-skill` step 3. Copy-lens deepening? `luke-iha-vicious-hooks`. Buyer-trigger read? `meg-heckman`.

## Content Type Adaptations

| Corpus | Lens |
|---|---|
| Short-form video (Reels/Shorts/TikTok) | jenny-hoyos (retention) + sky-tan (format) |
| LinkedIn text | diandra-hook-architect + lara-acosta |
| Educational/explainer | kallaway (illusion-of-novelty, pattern-interrupt) |
| Competitor ads (from `/riley-ad-spy`) | route to `/riley-ad-spy` step 4 instead — different verdict frame (durability) |

## Output Requirements

- Per-post `Analysis` verdicts, each grounded in a **named** lens, written to Notion.
- Sponsored exclusions listed with reason.
- A synthesized voice signature in specifics (recurring moves, not adjectives).
- Verdicts labeled as informed reads, not measured causation.

Execution prompt: references/prompts-v2/creator-why-it-works-analysis.md — honor its Output Contract.

## Quality Gate

Every verdict cites a named lens (not freehand)? · Sponsored excluded with evidence? · Signature stated in specifics a stranger could execute? · Epistemic status flagged? · Did real taste do the judging, or did it default to "engaging = good"?
