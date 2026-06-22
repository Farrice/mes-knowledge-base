---
description: Phase 5 positioning + offers — turn an existing Customer Truth Map into 3-5 gap-aimed positioning angles and 3 offer extensions, each tied to the exact pain/wish it answers, then hand off to BOS/positioning.
---

# /ctm-to-offer — Put the Map to Work: Positioning & Offers

**This is the map's positioning lever** ([../references/customer-truth-map-guide.md](../references/customer-truth-map-guide.md), Phase 5; verbatim prompt P9 in [../references/prompt-library.md](../references/prompt-library.md)). You already have a finished Customer Truth Map *and* a ranked gap table; this workflow turns the underserved gaps into 3–5 sharp positioning angles — each with one sentence that makes a prospect feel understood — and 3 ways to adjust or extend the offer, each tied to the **exact pain or wish it responds to** and flagged simple vs. major. Then it hands the result to a real positioning engine.

The discipline is **every angle aims at a specific gap; every offer move names the exact pain/wish it answers.** Positioning invented in your own language is the guessing tax wearing a strategy hat; this workflow refuses it. When the goal is a finished positioning system — the full Brand OS, the messaging hierarchy, the productized offer — this workflow stops at the gap-grounded angles + offer moves and hands off to `/build-bos` or the positioning skills, supplying the underserved gap and the customer's real language as the foundation.

> **Honesty spine.** The quotes in the worked thread below are tagged `[illustrative]` to teach the moves. In a real run every angle and every offer move is anchored to a **harvested** customer line and a real gap-table row — word-for-word, source-tagged, never paraphrased. The verbatim-integrity gate is the veto: a positioning angle built on a fabricated or smoothed quote fails the run regardless of how sharp it sounds.

## Pre-Flight Gate

Load [../genius.md](../genius.md) if it is not already hot in this conversation. Do not draft a single angle before all six questions below are answered on paper. These are the Decision Framework from [../genius.md](../genius.md), scoped to the positioning/offer job.

1. **Is the map real and finished?** Six categories populated, patterns named, vivid/repeated flagged? No map → run `/customer-truth-map` BUILD first; never position against a remembered audience.
2. **Is there a `/ctm-gaps` shortlist?** This is the primary input. P9 angles each aim at a *specific gap*; you cannot run this without the gap-width-ranked table. Missing → run `/ctm-gaps` (and `/ctm-jobs` upstream of it).
3. **Are the jobs available?** The offer extensions answer outcome-level jobs, not surface pains — a feature solves "I keep forgetting"; an *offer* answers "stay on their radar without feeling pushy." Confirm `/ctm-jobs` ran.
4. **One customer, one map?** Positioning for a blurry audience is positioning for no one. Pull from the single narrow map.
5. **What's the current offer?** The 3 extensions adjust an *existing* offer toward a gap. Name the current offer so simple-vs-major can be judged honestly.
6. **Verbatim discipline armed?** Every angle's "feel understood" sentence and every offer move must trace to a real map line and a real gap row. The word-for-word rule is re-issued the instant the AI invents a pain to justify an angle.

## Skill Acquisition

- **Always:** [../genius.md](../genius.md) (Pattern 6 pain→job reframe, Pattern 7 widest-gap-first, the rubric) + the finished map + the `/ctm-gaps` table.
- **The gap table is missing:** `/ctm-gaps` (the ranked shortlist *is* the input) and `/ctm-jobs` (the outcome-level jobs the offer extensions answer).
- **The map is stale:** `/ctm-refresh` — positioning against last year's language misses where the market moved.
- **Finishing the positioning:** hand off to `/build-bos` (full Brand OS) or the positioning skills (e.g., April Dunford-style positioning, `oren-brand`, `daniel-priestley`) — supply the underserved gap + the customer's real language as the grounded foundation.
- **Real-world claims in an angle/offer:** the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) before any positioning asserts a market fact, competitor claim, or stat.

## Execution

Two moves, in order. A worked example threads through both — audience: **first-time homebuyers in the San Fernando Valley who keep getting outbid**; current offer: a buyer's-agent service (from the real worked map at [../references/worked-exemplar-jen-fthb.md](../references/worked-exemplar-jen-fthb.md)). The quotes below are tagged `[illustrative]`; a real run uses harvested lines.

### Step 1 — 3–5 positioning angles, each aimed at a gap (P9, part one)
**Move.** Run prompt **P9 part one** against the map + gap table: draft 3–5 sharp positioning angles, each aimed at a *specific underserved gap* from the table, and for each, write **one sentence you could say to a prospect that would make them feel understood** — in the customer's register, drawn from a real map line. An angle not anchored to a gap row does not count; replace it with one that is.

**Diagnostic:**
1. Which exact gap-table row does this angle aim at — and is it one of the widest rows, where a better message lands hardest?
2. Is the "feel understood" sentence reconstructable from a real harvested line, or is it a clever line I imported?

**Template (vary the rows, never the gap/quote anchors):**

| # | Positioning angle | Gap it aims at (from `/ctm-gaps`) | "Feel understood" sentence (from a real map line) |
|---|---|---|---|
| 1 | "The agent who makes sellers trust *your* offer" | Gap: buyers keep losing to cash; current advice = "offer more" | *"You don't have the most money in the room — so we make you the offer they trust to close."* `[illustrative]` |
| 2 | "We explain every form before you sign" | Gap: process opacity; current fix = Google + anxiety | *"You'll never sign a page you don't fully understand again."* `[illustrative]` |

Three to five total. Each anchored to a gap row and a real line.

**Worked note (FTHB):** the strongest angle aims at the *widest* gap (outbid-defeat vs. the "just offer more" current fix), because the widest gap is where a sharper message lands hardest — Pattern 7.

### Step 2 — 3 offer extensions, each tied to a pain/wish + simple-vs-major (P9, part two)
**Move.** Run prompt **P9 part two**: suggest 3 ways to adjust or extend the offer to close a gap the customer clearly cares about. For each, **note the exact pain or wish from the map it responds to**, and be honest about whether it's **simple to add** or a **major undertaking.** An extension with no named pain/wish, or no honest effort flag, is incomplete.

**Diagnostic:**
1. Which specific pain or "if only" wish does this extension answer — quoted from the map?
2. Have I flagged effort *honestly* — not labeled a major build "simple" to make the list look easy?

**Template (vary):**
- **Extension:** *[what to add/adjust]* — **answers:** *[exact pain/wish line from the map]* — **effort:** Simple | Major.

**Worked extensions (FTHB):**
- **Add a pre-offer "forms walkthrough" call** — answers: *"I don't even understand half the stuff I'm signing"* `[illustrative]` — **effort: Simple** (a scheduled call, no new infra).
- **Build a "seller-trust packet" the buyer brings to every offer** — answers: *"we keep losing to all-cash offers"* `[illustrative]` — **effort: Major** (a repeatable asset + lender coordination).
- **Offer a flat "we'll explain it weekly" check-in** — answers GAINS: *"the one time an agent actually explained it I almost cried"* `[illustrative]` — **effort: Simple.**

### Step 3 — Hand off (do not finish here)
**Move.** Package the angles + offer extensions + their gap/pain anchors and hand off to the positioning engine. This workflow does **not** build the full Brand OS or messaging hierarchy — it supplies gap-grounded angles + real language so the positioning engine builds on proven ground. State the handoff explicitly:

> *Grounded positioning material ready (3–5 gap-aimed angles + 3 pain-tied offer extensions, effort-flagged). Hand to `/build-bos` for the full Brand OS or the positioning skills for the messaging hierarchy. Every angle is gap-traceable and every offer move names its exact pain/wish; instruct the engine to keep the customer's wording in the "feel understood" lines.*

## Content-Type Adaptations

The two moves are universal; the **emphasis and downstream engine** shift by deliverable. The map + gap table are the same; what you build from them changes.

| Deliverable | How the build changes |
|---|---|
| **Full Brand OS** | All 3–5 angles + all 3 offer moves feed forward; the widest-gap angle becomes the core positioning thesis. Hand to `/build-bos` with the gap table attached. |
| **One-liner / elevator** | Compress to the single widest-gap angle + its "feel understood" sentence. Hand to a positioning skill / `name-framework`. |
| **Sales-page positioning** | Angles become section headers; the "feel understood" lines become subheads; offer extensions become the offer stack. Hand to `/copy-engine` for the page after `/build-bos` sets the frame. |
| **Productized offer / new tier** | Lead with the offer extensions; each new tier answers one mapped pain/wish; simple-vs-major sets the build roadmap. Hand to `design-digital-product-offer` / `offer-stack`. |
| **Pitch / proposal** | The "feel understood" sentences become the opening recognition; the widest-gap angle frames the value. Hand to `draft-proposal`. |
| **Repositioning an existing offer** | Compare current positioning against the widest gaps; angles surface the under-claimed strength. Hand to a repositioning skill (`oren-repositioning`). |

## Output Requirements

Return three artifacts, then stop:
1. **The angle table** — 3–5 positioning angles, each aimed at a named `/ctm-gaps` row, each with one "feel understood" sentence traced to a real map line.
2. **The offer-extension list** — 3 adjustments/extensions, each naming the exact pain or wish (quoted) it responds to and flagged Simple vs. Major honestly.
3. **The handoff line** — the explicit pass to `/build-bos` / positioning skills with the underserved gap + real language supplied. Do not build the finished Brand OS or messaging hierarchy here.

## Quality Gate

Score against the [../genius.md](../genius.md) rubric; name the matching anchor for any dimension ≥8 (can't name it → lower it).
- **Verbatim Integrity (the veto)** — every "feel understood" sentence and every offer-extension pain/wish is anchored to a real, word-for-word, source-traceable map line. *Any angle or offer move built on a fabricated or paraphrased quote is an automatic fail, regardless of every other score.*
- **Gap Ranking** — every angle aims at a specific `/ctm-gaps` row; the lead angle aims at one of the *widest* gaps; nothing aims at an invented gap.
- **Job Depth** — offer extensions answer outcome-level jobs (positioning/offer-grade), not just surface features.
- **Put-to-Work Fidelity** — the "feel understood" lines carry the customer's voice; effort flags are honest (no major build mislabeled simple).
- **Hand-Off Discipline** — the workflow stops at gap-grounded angles + offer moves and hands to a positioning engine; it does not impersonate `/build-bos`.

**Self-check (one line):** *Could the customer hear the "feel understood" sentence and think "they actually get it" — because the line came from their own words and the gap is real?* If yes, hand off. If no, the failing angle goes back to the gap table (`/ctm-gaps`) for a real anchor.
