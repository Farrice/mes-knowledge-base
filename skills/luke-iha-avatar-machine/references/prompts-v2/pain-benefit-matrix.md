---
name: "Luke Iha — Pain & Benefit Matrix"
source_prompt: born-v2
skill: luke-iha-avatar-machine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working **Luke Iha's** Pain Matrix method — the diagnostic core of the Avatar Machine. The governing rule: **never describe a market with a single adjective.** Decompose it into 10 orthogonal dimensions (independent axes that don't collapse into each other — a market can be high-stigma AND high-visibility at once), score each 1–10, and read the **marketing consequence** off the score. The score is the input; the consequence is the output. A matrix of numbers with no consequences attached is an auto-fail.

## Input Required

- `[MARKET]` — the target market (required; infer from product if only a product is given)
- `[PRODUCT/OFFER]` — optional, sharpens which consequences matter
- `[GROUNDING SOURCE]` — a research dossier if available (each score should trace to real signal), or "none — flag ungrounded dimensions `[MODELED]`"
- `[MARKET TYPE]` — optional hint: health/physical · relationship/dating · MMO/biz-opp · pet/parent(other) — changes which dimensions dominate

## Execution Protocol

1. **Score all 10 Pain dimensions, 1–10:**
   1. **Source** (Physiological ↔ Psychological) — mind vs. body root. Low: emphasize tangible markers, science, expert proof, mechanism. High: relatable stories, tackle limiting beliefs/self-talk head-on.
   2. **Causal Clarity** (Low ↔ High) — market consensus on root cause. Low: investigate the "why," simplify cause to a single point. High: contradict mainstream to create curiosity; focus on solutions, not cause.
   3. **Visibility** (Low ↔ High) — how visible to others. Low: validate the invisible struggle, never imply "it's all in their head." High: fast visible results, before/after, social/confidence benefits.
   4. **Urgency** (Low ↔ High) — time pressure felt. Low: drive into the pain state via story, collapse the timeline of inaction, social proof. High: emotional triggers, instant relief, scarcity.
   5. **Social Stigma** (Low ↔ High) — shame/judgment attached. Low: direct approach. High: empathy + non-judgment, make the problem feel *shared*, confidential/safe framing.
   6. **Measurability** (Low ↔ High) — can progress be quantified. Low: vivid concrete imagery of the solved life. High: concrete measurable results, clear timelines.
   7. **Frequency** (Low ↔ High) — how often experienced. Low: honor the rare-but-significant event, guide through transformation. High: immediate relief + long-term benefit.
   8. **Locus of Control** (Internal ↔ External) — who controls the outcome. Internal: "not your fault," externalize blame onto other solutions, position the product as the change-maker. External: empathize with victimization, open unexpected new pathways for control.
   9. **Emotional Intensity** (Low ↔ High) — depth of feeling. Low: use stories to generate emotion, connect to broader life consequences, direct solutions. High: tread carefully — never invalidate the pain while offering the solution.
   10. **First Person** (Self ↔ Other) — who's primarily affected. Self: focus on their pain, frame self-care as permission. Other (pet/child): highlight the bond, reciprocity framing.

2. For **each** dimension, write a **Specific Consequence** — the concrete marketing implication of that exact score, pulled from the low/high play above and made specific to this market. A consequence that just restates the score ("high urgency means urgency matters") is a failure — it must name the *move*.

3. Output as a table: `Dimension | Rating | Specific Consequence`.

4. **Leverage summary** — name the 2–3 highest-leverage dimensions (usually the extremes) and the headline strategy they dictate for this market.

5. **Benefit Matrix** — re-plot the same 10 axes for the *solved* state. Note the biggest Pain→Benefit gaps per axis — those gaps are the transformation being sold.

6. **Ejection Trigger flag** — flag any dimension combination that implies a landmine phrase (e.g., high-psychological + pain market → never say "it's in your head"; high internal-locus + external-blame market → don't invalidate their sense of agency).

## Output Contract

- A 10-row Pain Matrix table, every row with a real, market-specific consequence — no blanks, no "N/A," no restated scores.
- A leverage summary naming the 2–3 dimensions that matter most and why.
- A 10-row Benefit Matrix table (same structure) plus explicit gap callouts.
- At least one Ejection Trigger flag derived from the score pattern.

## Output Skeleton

```
## Pain Matrix — [Market]
| Dimension | Rating (1–10) | Specific Consequence |
|---|---|---|
| Source (Physio↔Psych) | | |
| Causal Clarity | | |
| Visibility | | |
| Urgency | | |
| Social Stigma | | |
| Measurability | | |
| Frequency | | |
| Locus of Control | | |
| Emotional Intensity | | |
| First Person | | |

Leverage summary: [2–3 highest-leverage dims + headline strategy]

## Benefit Matrix — [Market] (solved state)
| Dimension | Rating (1–10) | Specific Consequence |
|---|---|---|
[same 10 rows]

Pain→Benefit gaps (the transformation): [list, biggest gaps first]

Ejection Trigger flags: [phrase(s) to never say, tied to the dimension pattern that implies them]
```

## Quality Gate

- [ ] All 10 Pain dimensions scored 1–10 with a distinct, market-specific consequence each — none blank, none restating the number?
- [ ] Dimensions treated as genuinely orthogonal (no collapsing two into one narrative)?
- [ ] Benefit Matrix mirrors all 10 axes and names the Pain→Benefit gaps?
- [ ] At least one Ejection Trigger flag derived from the actual score pattern (not generic)?
- [ ] Every score traces to grounding evidence or is explicitly flagged `[MODELED]`?

## Deploy When

- First diagnostic pass on a new market, before any hook or story work.
- Feeding `/avatar-manifold` stage 2, or standalone when a fast diagnostic is needed without the full package.
- Auditing whether an existing brief actually plots the market or just labels it.
