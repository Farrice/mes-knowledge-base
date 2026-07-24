---
description: "Riley × Lara/Diandra — scrape a top LinkedIn creator's non-sponsored winners into an exemplar corpus, hand it to the LinkedIn ghostwriting engine, and stage the posts. Riley supplies verified examples; Lara supplies the craft."
---

# /riley-lara-amplifier — Scraped LinkedIn Corpus → Ghostwritten Posts

Riley's retrieval layer feeding a voice engine (Pattern 8 + Cross-Expert Stacking Map, `vision.md`). Instead of prompting a LinkedIn voice from scratch, scrape the creator's actual winners and give the ghostwriting engine *examples* — Riley's core fix for the content-verification gap. Lara Acosta / Diandra own the LinkedIn craft; Riley owns the exemplar supply.

## Pre-Flight Gate

Load `genius.md` first. Proceed if:
- There's a specific LinkedIn creator/voice to source (yours, a client's, or a reference).
- The output ships under a real name → voice alignment applies (VOICE-CARD if Farrice's).
- You'll stage, not auto-post (draft terminus).

## Skill Acquisition

- `genius.md` — Patterns 1, 4 (creator-to-skill), 8 (chaining)
- Chain partners: `skills/lara-acosta-linkedin-growth/`, `diandra-escobar-linkedin-growth/` (hook-architect), `/ghostwrite`
- Live infra: `/scrape-creator`

## Execution

1. **Scrape the corpus (Riley's input layer).** `/scrape-creator` on the LinkedIn creator → non-sponsored winners into the Social Intelligence DB. Exclude sponsored with evidence.
2. **Extract the voice signature.** `/riley-creator-analyzer` grounds each winner in a hook lens (Diandra hook-architect for LinkedIn) → recurring hook/pacing/CTA moves in specifics.
3. **Brief the ghostwriter.** Hand Lara/Diandra's engine the signature + the exemplar corpus (not a vibe description) — this is the whole point: examples over instructions. One author per body (feedback memory) — never stitch multiple engines into one post.
4. **Generate posts** in the sourced voice via `/ghostwrite` or the Diandra/Lara workflow. Reader-contract dials + slop check.
5. **Stage for scheduling.** `/riley-distribution-ops` — draft the posts; the human schedules. Nothing auto-posts.
6. **Correct into the file.** If a post drifts from the voice, write the correction into the sourced skill so it compounds (Pattern 3).

## Content Type Adaptations

| Source | Adaptation |
|---|---|
| Own account (Farrice) | VOICE-CARD BLEND is the spine; scraped corpus deepens, never overrides |
| Client LinkedIn | scrape their best + their competitors'; brief Lara on the delta |
| Reference creator | source their voice as a *skill*, deploy on your topics (creator-to-skill) |

## Output Requirements

- A scraped, non-sponsored exemplar corpus (the retrieval layer).
- A voice signature in specifics, lens-grounded.
- Ghostwritten posts from a **single** engine, voice-matched, slop-checked.
- Posts staged, not published.

Execution prompt: references/prompts-v2/exemplar-grounded-voice-pipeline.md — honor its Output Contract.

## Quality Gate

Grounded in scraped examples (not a prompted vibe)? · One author per body? · Voice-matched + slop-checked? · Sponsored excluded with evidence? · Staged behind approval? · Corrections written into the sourced skill?
