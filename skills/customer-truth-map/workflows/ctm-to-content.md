---
description: Phase 5 content — turn an existing Customer Truth Map into 15 grounded content ideas (each tied to its source quote) plus one widest-gap long-form outline, then hand off to a real content engine.
---

# /ctm-to-content — Put the Map to Work: Content

**This is the map's content lever** ([../references/customer-truth-map-guide.md](../references/customer-truth-map-guide.md), Phase 5; verbatim prompt P8 in [../references/prompt-library.md](../references/prompt-library.md)). You already have a finished Customer Truth Map; this workflow turns its pains, jobs, and gaps into 15 content ideas that each carry the **specific quote or pattern they're built on** — so no idea is invented on "a slow Tuesday" — then outlines one long-form piece from the single widest gap and hands the result to a real content engine.

The discipline is **one quote per idea, no exceptions.** An idea without a named source line is a guess wearing a costume; this workflow refuses to ship it. When the goal is finished, published content — the viral post, the Substack edition, the daily series — this workflow stops at the grounded idea bank and hands off to `/novelty-forge`, `/parallax`, or `/diandra-*`, supplying them the held belief and the real language so they engineer the piece on proven ground instead of from scratch.

> **Honesty spine.** The quotes in the worked thread below are tagged `[illustrative]` to teach the moves. In a real run every idea is anchored to a **harvested** customer line from the actual map — word-for-word, source-tagged, never paraphrased. The verbatim-integrity gate is the veto: an idea built on a fabricated or smoothed quote fails the run regardless of how good the idea sounds.

## Pre-Flight Gate

Load [../genius.md](../genius.md) if it is not already hot in this conversation. Do not generate a single idea before all six questions below are answered on paper. These are the Decision Framework from [../genius.md](../genius.md), scoped to the content job.

1. **Is the map real and finished?** Six categories populated, patterns named, vivid/repeated quotes flagged? No map → run `/customer-truth-map` BUILD first; never brainstorm content from a remembered audience.
2. **Are pains, jobs, and gaps all present?** P8 builds on all three. If `/ctm-jobs` and `/ctm-gaps` haven't run, run them — ideas grounded only in raw pains miss the outcome-level angles where the best content lives.
3. **Is there a `/ctm-gaps` shortlist?** The long-form outline is built from the **single widest-gap row**. Confirm the gap table exists and is gap-width-ranked; the widest row is the input here.
4. **One customer, one map?** Content for a blurry audience lands on no one. Pull from the one narrow map that matches this channel.
5. **Which channel(s)?** Posts, emails, short videos — the idea mix and the downstream engine shift by channel (see the Adaptations table). Name them before generating.
6. **Verbatim discipline armed?** Every idea must name a real map line. The word-for-word rule is re-issued the instant the AI generates an idea it can't trace to a quote.

## Skill Acquisition

- **Always:** [../genius.md](../genius.md) (Pattern 9 grounded-idea generation, Signature Move 5 "one quote per idea", the rubric) + the finished map.
- **The gap table is missing:** `/ctm-gaps` (you need the ranked widest-gap shortlist) and, upstream of it, `/ctm-jobs` for the outcome-level angles.
- **The map is stale:** `/ctm-refresh` — content built on last year's language reads dated.
- **Finishing the content:** hand off to `/novelty-forge` (the front door for manufacturing the *feeling* of novelty on a saturated topic — supply it the held belief + real language), `/parallax` (Substack editions), or `/diandra-*` (hooks-only amplifiers; never wire Diandra into the body). Supply the idea + its source quote as grounded input.
- **Real-world claims in an idea:** the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) before any piece asserts a stat, study, or named event.

## Execution

Two moves, in order. A worked example threads through both — audience: **first-time homebuyers in the San Fernando Valley who keep getting outbid** (from the real worked map at [../references/worked-exemplar-jen-fthb.md](../references/worked-exemplar-jen-fthb.md)). The quotes below are tagged `[illustrative]`; a real run uses harvested lines.

### Step 1 — 15 grounded ideas, each with its source (P8, part one)
**Move.** Run prompt **P8 part one** against the map: generate 15 content ideas (posts / emails / short videos) that speak to problems the customer *actually raised*, and for each, include the **specific quote or pattern from the map it's built on** — so each idea is provably grounded in real language, not invented. An idea with no source line attached does not count toward the 15; replace it with one that does.

**Diagnostic:**
1. Can I point at the exact map quote (or named pattern) under each idea? (No source → cut and regenerate.)
2. Does the idea speak to a problem the customer raised in *their* terms, or to a topic I think is interesting?

**Template (vary the rows, never the source quotes):**

| # | Content idea | Source quote / pattern (harvested) | Format |
|---|---|---|---|
| 1 | "Why you keep losing to cash offers (and the 3 things that actually beat them)" | *"we keep losing to all-cash offers"* `[illustrative]` — most-repeated PAIN | Post |
| 2 | "The forms nobody explains to first-time buyers" | *"I don't even understand half the stuff I'm signing"* `[illustrative]` | Short video |
| 3 | "You're not bad at this — read this before you give up" | FEEL pattern: self-blame thread flagged vivid | Email |

Fill to 15. Lean on the flagged vivid/repeated quotes and the `⚠ WORKAROUND` lines from the DO category — workarounds make the sharpest content because they're a problem someone cared about enough to solve badly.

**Worked note (FTHB):** the strongest ideas cluster on the outbid-defeat pain and the "don't understand what I'm signing" fear because both are flagged repeated in the map — frequency in the map predicts resonance in the feed.

### Step 2 — The widest-gap long-form outline (P8, part two)
**Move.** Run prompt **P8 part two**: take the *single widest-gap row* from the `/ctm-gaps` table and outline one piece of long-form content that (a) **names the problem in the customer's own words**, (b) **validates the frustration with their current fix**, and (c) **points toward a better way of thinking about it.** Three beats, in that order — recognition before reframe.

**Diagnostic:**
1. Does the opening name the problem in a real harvested line, not my paraphrase of it?
2. Does the middle validate the *current fix's* shortfall (the Gap column), so the reader feels seen before they're sold?

**Template (the three-beat outline — vary the content, keep the spine):**
- **Open — name it in their words:** lead with the widest-gap PAIN as a near-verbatim line. *[FTHB: "You've put in five offers. You've lost five times. Here's what nobody told you about why."]*
- **Middle — validate the current fix's failure:** walk the Current Fix from the gap table and show exactly where it leaves them wanting (the Gap). *[FTHB: the "just offer more / waive contingencies" advice, and why it's a trap for a first-timer.]*
- **Turn — a better way to think about it:** the reframe drawn from the JTBD outcome, not a product pitch. *[FTHB: "winning isn't about the highest number — it's about being the offer the seller trusts to close."]*

### Step 3 — Hand off (do not finish here)
**Move.** Package the 15 sourced ideas + the long-form outline and hand off to the finishing engine. This workflow does **not** write the published piece — it supplies grounded ideas + real language so the content engine builds on proven ground. State the handoff explicitly:

> *Grounded content bank ready (15 sourced ideas + 1 widest-gap outline). Hand to `/novelty-forge` (pass it the held belief + the real language as the held-constant "old"), `/parallax` (Substack edition from the outline), or `/diandra-*` (hooks only). Every idea is map-traceable; instruct the engine that the source quote is the grounding, not a suggestion.*

## Content-Type Adaptations

The two moves are universal; the **idea mix and downstream engine** shift by channel. The map is the same; what you draw from it changes.

| Channel | How the generation changes |
|---|---|
| **Short-form video** | Bias ideas toward single-PAIN hooks and `⚠ WORKAROUND` reveals (one vivid line = one clip). The outline becomes a script beat-sheet. Hand to `/novelty-forge` (hook zone) → `/diandra-*` for hook amplification. |
| **LinkedIn / X** | Ideas built on FEEL lines (self-recognition stops the scroll); the widest-gap outline becomes a long post or thread. Hand to `/novelty-forge` (LinkedIn-post row) or `/ghostwrite`. |
| **Email / newsletter** | Ideas cluster into a sequence arc; the long-form outline anchors one flagship edition. Subject lines pull from FEEL. Hand to `/parallax` or `master-copywriter` for the arc. |
| **Substack / long-form** | Fewer, deeper ideas; the widest-gap outline *is* the edition spine — the three beats become sections. Hand to `/parallax` with the source quotes inline. |
| **Daily content series** | The 15 ideas seed a publishing calendar; each day carries its source quote as the brief. Hand to `/diandra-content-engine` (hooks) with the grounded ideas as the bank. |
| **Carousel / educational** | Ideas drawn from the DO category and pains→jobs; each slide answers one mapped pain. The outline becomes the slide flow. Hand to the content engine with the quote-per-slide grounding. |

## Output Requirements

Return three artifacts, then stop:
1. **The 15-idea bank** — each idea paired with the specific harvested quote or named pattern it's built on, and a format tag (post / email / short video). No idea without a source line.
2. **The widest-gap outline** — one long-form outline with the three beats (name it in their words → validate the current-fix failure → point to a better way), the source quote inline at the opening.
3. **The handoff line** — the explicit pass to `/novelty-forge` / `/parallax` / `/diandra-*` with the held belief + real language supplied. Do not produce the finished, published piece here.

## Quality Gate

Score against the [../genius.md](../genius.md) rubric; name the matching anchor for any dimension ≥8 (can't name it → lower it).
- **Verbatim Integrity (the veto)** — every one of the 15 ideas and the outline's opening is anchored to a real, word-for-word, source-traceable map line. *Any idea built on a fabricated or paraphrased quote is an automatic fail, regardless of every other score.*
- **Put-to-Work Fidelity** — every idea carries its source quote/pattern; nothing generic; the outline names the problem in the customer's actual words.
- **Gap Ranking** — the long-form outline is built from the *single widest-gap* row, not a convenient one; the validate-beat uses the real Current Fix.
- **Do-Category Mining** — at least some ideas surface the `⚠ WORKAROUND` lines as content (the sharpest unmet-need signals).
- **Hand-Off Discipline** — the workflow stops at the grounded idea bank and hands to a content engine; it does not impersonate `/novelty-forge` or `/parallax`.

**Self-check (one line):** *Could a skeptic open the map, find the exact quote under every idea, and confirm the long-form opens on a line a real person actually wrote?* If yes, hand off. If no, the unsourced idea goes back to the map (`/ctm-map` / `/ctm-gaps`) for a real line.
