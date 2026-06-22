---
description: Phase 5 copy — turn an existing Customer Truth Map into 10 slot-assigned proven quotes plus 8 customer-register headlines, then hand off to a real copy engine for the finished long-form.
---

# /ctm-to-copy — Put the Map to Work: Copy

**This is the map's copy lever** ([../references/customer-truth-map-guide.md](../references/customer-truth-map-guide.md), Phase 5; verbatim prompt P7 in [../references/prompt-library.md](../references/prompt-library.md)). You already have a finished Customer Truth Map; this workflow mines it for the raw copy that is *already proven because a real person already said it* — pulls the 10 most powerful quotes, assigns each a slot, and writes 8 headlines in the customer's own register — then hands the result to a finishing engine rather than competing with it.

The job is **selection and assignment, not composition.** Every line this workflow emits traces back to a specific quote or pattern in the map; nothing is invented to fill a slot. When the finished long-form copy is the goal — the full sales page, the email sequence, the VSL — this workflow stops at the grounded raw material and hands off to `/copy-engine`, `/ghostwrite`, or `master-copywriter`, which take the proven lines and build the finished asset around them.

> **Honesty spine.** The quotes in the worked thread below are tagged `[illustrative]` to teach the moves. In a real run every quote is a **harvested** customer line pulled from the actual map — word-for-word, source-tagged, never paraphrased or invented to fit a slot. The verbatim-integrity gate is the veto: a single fabricated or smoothed quote fails the run regardless of everything else.

## Pre-Flight Gate

Load [../genius.md](../genius.md) if it is not already hot in this conversation. Do not assign a single slot before all six questions below are answered on paper. These are the Decision Framework from [../genius.md](../genius.md), scoped to the copy job.

1. **Is the map real and finished?** Is there an actual Customer Truth Map (six categories populated, patterns named, vivid/repeated quotes flagged)? No map → stop and run `/customer-truth-map` BUILD first; do not improvise a map from memory.
2. **One customer, one map?** The copy will only land if the map is narrow (the "solo bookkeeper who just lost a big client" test). Serving several? Pull from the *one* map that matches this page/campaign — do not blend maps into mush.
3. **Which page or campaign is this for?** P7 needs the target named (sales page / landing page / email / ad). The slot mix shifts by asset (see the Adaptations table); name it before pulling.
4. **Where are the flagged quotes?** The map's vivid/repeated flags are your shortlist for the 10. If they were never flagged, run `/ctm-map`'s flagging pass before pulling — the strongest copy comes from the lines a real person said with heat.
5. **FEEL + PAINS available?** The 8 headlines come *specifically* from the FEEL and PAINS sections in the customer's emotional register. Confirm both are populated; thin FEEL → headlines will drift toward jargon.
6. **Verbatim discipline armed?** Every pulled line must be a real map quote. The word-for-word rule is stated and will be re-issued the instant the AI starts smoothing grammar or paraphrasing a pain.

## Skill Acquisition

- **Always:** [../genius.md](../genius.md) (Pattern 8 quote-to-slot, the honesty spine, the rubric) + the finished map itself.
- **The map is missing or stale:** `/customer-truth-map` BUILD (cold start) or `/ctm-refresh` (stale) — do not write copy against a guessed map.
- **Slots are thin / quotes don't cover a needed beat:** `/ctm-map` to re-mine, or `/ctm-gaps` to confirm which pain leads (the widest gap is what the headline should answer).
- **Finishing the long-form:** hand off to `/copy-engine` (cold-start converting copy, Ground Once / Refine Free), `/ghostwrite` (LinkedIn / founder voice), or `master-copywriter` (agency-grade single asset) — supply them the slot table + headlines as the grounded input.
- **Real-world claims ride along:** the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) before any line asserts a stat, date, or named result.

## Execution

Two moves, in order. A worked example threads through both — audience: **first-time homebuyers in the San Fernando Valley who keep getting outbid** (drawn from the real worked map at [../references/worked-exemplar-jen-fthb.md](../references/worked-exemplar-jen-fthb.md)). The quotes below are tagged `[illustrative]`; a real run uses harvested lines.

### Step 1 — Pull the 10 + assign slots (P7, part one)
**Move.** Run prompt **P7 part one** against the map: pull the 10 quotes most powerful to use, *lightly edited only for sense* (bracket additions, never paraphrase), and assign each a single best slot — **headline · subhead · objection-handler · proof point** — keeping the customer's voice intact. Lightly edited means: trim a runaway clause, bracket a missing antecedent. It never means smoothing the grammar that carries the heat.

**Diagnostic:**
1. Is every one of the 10 a real, source-traceable map line — not a line I wrote that *sounds* like the customer?
2. Does each quote sit in the slot where its specific energy works hardest (a raw fear → objection-handler or headline; an "if only" wish → proof point of the outcome)?

**Template (the slot table — vary the rows, never the quotes):**

| # | Quote (harvested, lightly edited for sense only) | Slot | Why this slot |
|---|---|---|---|
| 1 | *"we keep losing to all-cash offers and I'm starting to think we'll never get a house"* `[illustrative]` | Headline | names the recurring defeat in their words |
| 2 | *"I don't even understand half the stuff I'm signing"* `[illustrative]` | Objection-handler | the pricing/process fear, answered in the body |
| 3 | *"the one time an agent actually explained it to me I almost cried"* `[illustrative]` | Proof point | the relief outcome, in a real voice |

Fill to 10. Each row carries its source tag in the working file even if hidden in the table.

**Worked pull (FTHB):** the headline slot goes to the outbid-defeat line because it is the most-repeated, highest-heat pain in the map; the "don't understand what I'm signing" line is assigned objection-handler, not headline, because it answers a fear rather than stops a scroll.

### Step 2 — 8 headlines from FEEL + PAINS (P7, part two)
**Move.** Run prompt **P7 part two**: using *only* the FEEL and PAINS sections, write 8 headline options for the named page/campaign in the customer's own words and emotional register. **No jargon, no hype.** Each headline must be reconstructable from a specific FEEL/PAIN line — not a clever line you imported.

**Diagnostic:**
1. Can I point at the exact FEEL or PAIN quote each headline is built on? (If not, it's invented — cut it.)
2. Would the customer recognize this as something happening in their own head, or does it read like marketing wrote it?

**Template (vary):** *[their pain stated flat, no spin]* · *[their wish, framed as a question they actually ask]* · *[their workaround named back to them].*

**Worked headlines (FTHB), each traced:**
- *"Stop losing the house to all-cash buyers."* ← PAIN: the outbid-defeat line.
- *"Finally understand everything you're signing."* ← PAIN: "don't understand half the stuff I'm signing."
- *"You're not bad at this. The market is brutal."* ← FEEL: the self-blame thread flagged vivid in the map.

Eight total, each with its source line noted beside it in the working file.

### Step 3 — Hand off (do not finish here)
**Move.** Package the slot table + the 8 headlines + their source tags and hand off to the finishing engine. This workflow does **not** write the full sales page — it supplies the proven raw material so the copy engine builds on customer-grounded lines instead of a blank page. State the handoff explicitly:

> *Grounded copy material ready (10 slot-assigned quotes + 8 traced headlines). Hand to `/copy-engine` for the full converting page, `/ghostwrite` for founder-voice social, or `master-copywriter` for a single agency-grade asset. Every supplied line is map-traceable; instruct the engine to keep the customer's wording in the load-bearing slots.*

## Content-Type Adaptations

The two moves are universal; the **slot mix and headline register** shift by asset. The map is the same; what you pull from it changes.

| Asset | How the pull changes |
|---|---|
| **Sales / landing page** | Full slot spread: 1 headline + 2–3 subheads + 3–4 objection-handlers + 2–3 proof points. Lead the headline with the widest-gap PAIN; stack proof-point quotes near the CTA. Hand to `/copy-engine`. |
| **Email** | Pull 2–3 quotes max: one subject-line candidate (a FEEL line), one body-opening pain, one proof line. Headlines become subject lines — whisper register, no hype. Hand to `/copy-engine` or `master-copywriter` for the sequence arc. |
| **LinkedIn / founder post** | One headline becomes the scroll-stop line 1 (densest PAIN in their words); one proof-point quote becomes the first-person turn. Skip objection-handlers. Hand to `/ghostwrite`. |
| **Ad / VSL** | Headline = highest-heat PAIN at max density; objection-handlers seed the rebuttal beats; proof-point quotes escalate. Hand to `master-copywriter` (DR mode). |
| **Outreach / DM** | Pull one objection-handler and one wish-as-proof; no headlines. The opener mirrors their exact PAIN line so it reads as recognition, not pitch. Hand to `/copy-engine` outreach. |
| **Testimonial / proof block** | Pull only proof-point and GAINS "if only" lines; assign each to the outcome it evidences. No headlines. Feeds any finishing engine's proof section. |

## Output Requirements

Return three artifacts, then stop:
1. **The slot table** — 10 harvested quotes, lightly edited for sense only, each assigned one slot (headline / subhead / objection-handler / proof point) with a one-line reason and its source tag.
2. **The 8 headlines** — built only from FEEL + PAINS, in the customer's register, no jargon/hype, each with the exact source line noted beside it.
3. **The handoff line** — the explicit pass to `/copy-engine` / `/ghostwrite` / `master-copywriter` with the instruction to keep customer wording in the load-bearing slots. Do not produce the finished long-form copy here.

## Quality Gate

Score against the [../genius.md](../genius.md) rubric; name the matching anchor for any dimension ≥8 (can't name it → lower it).
- **Verbatim Integrity (the veto)** — every one of the 10 quotes and every headline source line is a real, word-for-word, source-traceable map line. *Any fabricated, paraphrased, or grammar-smoothed quote is an automatic fail, regardless of every other score.*
- **Put-to-Work Fidelity** — each slot assignment is the strongest home for that quote's specific energy; nothing generic; the customer's voice survives the edit.
- **Narrowness** — pulled from one narrow map, not a blend; the headlines read as one customer's head, not a composite.
- **Gap Ranking** — the headline slot answers the widest-gap PAIN, not a minor one.
- **Hand-Off Discipline** — the workflow stops at grounded raw material and hands to a finishing engine; it does not impersonate `/copy-engine`.

**Self-check (one line):** *Could the customer read the headline and the slot quotes and say "that's exactly what I said" — because they did?* If yes, hand off. If no, the failing line goes back to the map (`/ctm-map`) for a real quote.
