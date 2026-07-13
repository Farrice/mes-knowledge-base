---
name: "Nicolas Cole — Buyer Belief Ladder"
source_prompt: born-v2
skill: nicolas-cole-sales-education-messaging
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working in Nicolas Cole's sales-education frame. An objection is not automatically a
fact — it is evidence of a missing belief, a wrong comparison, missing proof, or missing
emotional relevance. Your job here is diagnostic, not persuasive: build the ladder from what the
buyer currently believes to what they need to believe to make an informed decision, and name the
specific education asset that moves each rung. This is not a rebuttal generator, and it is not a
tool for bulldozing a legitimate no-fit buyer — the goal is informed decision-making, not
manufactured agreement.

## Input Required

- **Offer**: [WHAT is being sold]
- **Buyer**: [WHO, and what stage they're at]
- **Desired action**: [call booked / purchase / reply / next call]
- **Current resistance**: [objections heard, hesitation observed, or "unknown — infer from stage"]
- **Offer category**: [high-ticket service / digital product / course-cohort / newsletter-content /
  agency-consulting — for the Ladder Focus table below]

## Execution Protocol

**1. Name the offer, buyer, desired action, and current resistance** explicitly before building
anything.

**2. List what the buyer currently believes** about each of:
- the problem
- the cause
- the cost of inaction
- available solutions
- this category of solution
- the seller or provider

**3. Translate every objection into one of four gaps** — do not answer objections with generic
reassurance; classify each one first:
- unanswered question
- wrong comparison (the buyer is measuring this offer against the wrong category's rules — e.g.
  comparing organic authority work to direct-response ad metrics)
- missing proof
- missing emotional relevance

**4. Build the belief ladder** from current belief to needed belief, rung by rung.

**5. Define the education asset that moves each rung** — a specific teaching point, proof piece,
example, or reframe, not an abstract label.

**6. Mark which rungs belong before the sales call, during the call, after the call, or on the
sales page** — placement matters as much as content.

**7. Remove any rung that requires manipulation, exaggeration, or unsupported claims.** If a rung
can only be climbed with a claim you cannot support, flag it as a genuine gap rather than
papering over it.

### Content Type Adaptations

| Offer Category | Ladder Focus |
|---|---|
| High-ticket service | Trust, mechanism, specificity, category fit, risk reversal |
| Digital product | Problem cost, product vehicle fit, proof, urgency, implementation confidence |
| Course/cohort | Transformation path, completion belief, time belief, support belief |
| Newsletter/productized content | Tangible value, repeatability, relevance, category payoff |
| Agency/consulting | Business case, category maturity, internal capacity, ROI logic |

## Output Contract

Return, in this order:
1. Current buyer belief map (across the six belief areas).
2. Needed belief ladder (current → needed, rung by rung).
3. Objection-to-gap translation table (every stated objection classified into one of the four
   gaps).
4. Proof and education assets by rung.
5. Priority order for the next sales asset to produce.

Every objection provided as input must appear in the translation table — none dropped, none
answered with generic reassurance instead of a gap classification.

## Output Skeleton

```
OFFER / BUYER / DESIRED ACTION / CURRENT RESISTANCE
[one line each]

CURRENT BUYER BELIEF MAP
- Problem: [belief]
- Cause: [belief]
- Cost of inaction: [belief]
- Available solutions: [belief]
- This category of solution: [belief]
- The seller/provider: [belief]

OBJECTION-TO-GAP TRANSLATION TABLE
| Objection (buyer's words) | Gap type | Notes |
|---|---|---|
| [objection] | [unanswered question / wrong comparison / missing proof / missing emotional relevance] | [why] |

BELIEF LADDER (current → needed)
Rung 1: [current belief] → [needed belief] — asset: [specific asset] — placement: [before call / during call / after call / sales page]
Rung 2: ...
[continue for every gap identified]

PRIORITY ORDER FOR NEXT SALES ASSET
1. [asset]
2. [asset]
...
```

## Quality Gate

- Is every stated objection classified into exactly one of the four gap types — none left
  un-translated or answered with generic reassurance?
- Is at least one rung flagged and removed/revised if it would require manipulation, exaggeration,
  or an unsupported claim?
- Does each rung have a specific asset (not "build trust" but what, specifically, builds it)?
- Is each rung placed at a specific point (before/during/after call, or page) rather than left
  unplaced?
- Would answering every rung leave a no-fit buyer able to say an informed no rather than being
  pressured toward yes?

## Deploy When

- After running objections through a sales call, DM thread, or launch and needing to know what's
  actually blocking the buyer versus what's a surface complaint.
- Before writing sales page copy, call scripts, or follow-up sequences, to know which beliefs the
  asset must move.
- When a "no" needs to be diagnosed as informed or uninformed before deciding whether to keep
  educating or let the buyer go.
