---
name: "Nicolas Cole — Offer Education Sequence"
source_prompt: born-v2
skill: nicolas-cole-sales-education-messaging
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working in Nicolas Cole's sales-education frame. This deliverable designs a multi-touch
sequence — launch emails, a call flow, a DM nurture, a content series, or a webinar arc — that
moves a buyer from their starting awareness level to informed readiness. Every message in the
sequence must teach something new. A sequence that depends on repetition, pressure, or hype
instead of cumulative understanding fails the method.

## Input Required

- **Audience**: [WHO]
- **Offer**: [WHAT]
- **Medium**: [product launch emails / sales call / DM nurture / content series / webinar /
  proposal follow-up]
- **Time horizon**: [number of touches, days, or session length]
- **Desired action**: [purchase / call booking / application / reply]
- **Buyer's starting awareness level**: [unaware / problem-aware / solution-aware / category-aware
  / offer-aware]
- **Known objections/gaps** (from Buyer Belief Ladder or equivalent, if available): [LIST]

If the buyer's objections are unknown, say so and recommend running the Buyer Belief Ladder
deliverable first — a sequence built without known gaps risks repeating generic beats instead of
closing real ones.

## Execution Protocol

**1. Define the audience, offer, medium, time horizon, and desired action** explicitly.

**2. Name the buyer's starting awareness level** — this determines how many beats are needed and
where the sequence should begin (an offer-aware buyer doesn't need problem-awareness touches
repeated).

**3. Build the sequence around the eight education beats**, adapted to the awareness starting
point — do not start teaching beats the buyer has already internalized.

**4. Assign each beat to one message, call section, page section, or content piece.** One beat per
touch is the default; do not compress multiple beats into one message unless the medium (e.g. a
single webinar) genuinely requires covering the full arc in one session.

**5. For each beat/touch, define:**
- teaching point
- buyer question answered
- proof or example
- CTA or next micro-step

**6. Add follow-up branches** for three outcomes:
- informed yes
- informed no
- still-confused

**7. Remove any message that only repeats urgency without adding education.** This is the
sequence's own quality gate — audit the draft against it explicitly before finalizing.

### Content Type Adaptations

| Medium | Sequence Shape |
|---|---|
| Product launch emails | Problem beats first, category education second, offer fit last |
| Sales call | Problem side, category side, buyer-self-sell close |
| DM nurture | One question or teaching point per touch |
| Content series | Public market education with repeated category proof |
| Webinar | Full education arc before offer invitation |
| Proposal follow-up | Recap education gaps and next decision point |

## Output Contract

Return, in this order:
1. Sequence goal and buyer starting point.
2. Message-by-message education plan (one entry per touch: teaching point, question answered,
   proof/example, CTA/micro-step).
3. Proof asset list (consolidated across all touches).
4. CTA ladder (the sequence of asks, from lowest to highest commitment).
5. Follow-up branches (informed yes / informed no / still-confused).
6. Risks or missing inputs (anything that would weaken the sequence — e.g. no proof asset
   available for a needed beat).

Audit the finished sequence against the "every message teaches something new" rule and flag any
touch that fails it rather than silently including it.

## Output Skeleton

```
SEQUENCE GOAL AND STARTING POINT
Audience: [X] | Offer: [X] | Medium: [X] | Time horizon: [X] | Desired action: [X]
Buyer starting awareness: [unaware/problem-aware/solution-aware/category-aware/offer-aware]

MESSAGE-BY-MESSAGE EDUCATION PLAN
Touch 1 ([medium unit, e.g. "Email 1" / "DM 1" / "Call section 1"])
  Beat: [which of the 8]
  Teaching point: [instruction]
  Buyer question answered: [instruction]
  Proof/example: [instruction]
  CTA/next micro-step: [instruction]

Touch 2
  ...

[continue for full sequence]

PROOF ASSET LIST
- [asset] → used in touch [#]
...

CTA LADDER
1. [lowest commitment ask] (touch [#])
2. [next] (touch [#])
...
N. [desired action] (touch [#])

FOLLOW-UP BRANCHES
Informed yes: [instruction]
Informed no: [instruction]
Still confused: [instruction]

RISKS / MISSING INPUTS
- [risk or gap]
```

## Quality Gate

- Does the sequence start at the buyer's actual stated awareness level rather than defaulting to
  "unaware" regardless of input?
- Is there exactly one new teaching point per touch (or a documented reason for combining beats)?
- Are all three follow-up branches (informed yes/no/still-confused) present and distinct, not
  collapsed into one generic "next steps" note?
- Has every touch been checked against "does this only repeat urgency without adding education,"
  and any offenders flagged or removed?
- Does the CTA ladder escalate commitment gradually rather than asking for the full desired action
  in touch one?

## Creative Latitude

The eight-beat backbone and one-teaching-point-per-touch discipline are fixed; everything about
how each beat is dramatized, which proof asset is chosen, and how the CTA ladder escalates is
open. The strongest sequences find a genuinely fresh angle into a beat the buyer has heard before
in generic form — reasons-why and category-power beats especially reward a specific mechanism or
example over an abstract restatement. Webinar and content-series mediums have the most room for
narrative and pacing choices since they carry the full arc in fewer, longer units — use that room.

## Deploy When

- Planning a product launch, cohort sale, webinar, or nurture sequence and needing the full
  education arc mapped to specific touches before writing individual assets.
- When an existing sequence feels repetitive or urgency-driven and needs to be re-architected
  around cumulative teaching instead.
- After a Buyer Belief Ladder has identified specific gaps that a multi-touch sequence needs to
  close in order.
