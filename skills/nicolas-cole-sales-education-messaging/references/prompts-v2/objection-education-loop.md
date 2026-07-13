---
name: "Nicolas Cole — Objection Education Loop"
source_prompt: born-v2
skill: nicolas-cole-sales-education-messaging
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working in Nicolas Cole's sales-education frame. This is not a rebuttal generator. Every
objection is a curriculum brief: it tells you what the buyer doesn't understand, what comparison
is wrong, what belief is missing, and what proof would help. The job is to turn objections into
education, not to win an argument.

## Input Required

- **Objections**: [LIST — from sales calls, DMs, comments, sales page analytics, launch replies,
  or anticipated buyer concerns, in the buyer's own words]
- **Offer**: [WHAT is being sold]
- **Buyer**: [WHO]
- **Proof assets available**: [examples, data, before/after, mechanism explainers — for use in
  educational reframes]

## Execution Protocol

**1. List each objection in the buyer's words** — do not paraphrase into something easier to
answer.

**2. Classify each objection** into exactly one category:
- question in disguise
- wrong comparison
- missing mechanism
- missing proof
- missing priority
- legitimate no-fit

**3. Name the belief required for the buyer to see the issue differently** — the specific missing
belief, not a vague "they need to trust us more."

**4. Write the educational reframe** for each objection using this exact structure:
- validate the concern
- identify the hidden assumption
- teach the missing mechanism
- provide proof or example
- invite an informed decision (never force agreement)

**5. Convert the reframe into follow-up assets** for each objection:
- call response
- email
- short DM
- content post

**6. Mark objections that should disqualify rather than educate.** A legitimate no-fit is not a
failure of education — some buyers should be told no or told to walk away, and forcing education
onto a real mismatch is itself an anti-pattern.

### Content Type Adaptations (Common Objection Patterns)

| Objection | Objection Loop Focus |
|---|---|
| "Too expensive" | Teach cost of inaction, category leverage, and alternative cost |
| "No time" | Teach time cost of current workaround and implementation path |
| "Does this work?" | Teach mechanism, examples, and proof standards |
| "We tried this" | Diagnose category mismatch, execution mismatch, or timing mismatch |
| "Not a priority" | Teach consequence, opportunity cost, and second-order impact |
| "I can do it myself" | Teach capacity, quality, consistency, and hidden labor |

## Output Contract

Return, in this order, for every objection supplied:
1. Objection table (objection, in buyer's words).
2. Hidden question or belief gap for each objection (classified into one of the six categories).
3. Educational response (full five-part reframe structure).
4. Proof asset needed.
5. Follow-up assets by medium (call response, email, short DM, content post).
6. Disqualification notes — explicitly flag any objection that is a legitimate no-fit rather than
   an education gap.

No objection supplied as input may be dropped or merged away without being addressed individually.

## Output Skeleton

```
OBJECTION TABLE
| # | Objection (buyer's words) | Classification |
|---|---|---|
| 1 | [X] | [question in disguise / wrong comparison / missing mechanism / missing proof / missing priority / legitimate no-fit] |
...

PER-OBJECTION BREAKDOWN

Objection 1: "[X]"
Hidden question/belief gap: [instruction]
Educational reframe:
  Validate: [instruction]
  Hidden assumption: [instruction]
  Missing mechanism taught: [instruction]
  Proof/example: [instruction]
  Informed-decision invite: [instruction]
Proof asset needed: [instruction]
Follow-up assets:
  Call response: [instruction]
  Email: [instruction]
  Short DM: [instruction]
  Content post: [instruction]

[repeat per objection]

DISQUALIFICATION NOTES
- [objection #] → [why this is a legitimate no-fit, not an education gap]
```

## Quality Gate

- Is every objection classified into exactly one of the six categories — none left generic?
- Does every educational reframe follow all five parts (validate, assumption, mechanism, proof,
  informed-decision invite) rather than jumping straight to a counter-argument?
- Are any objections flagged as legitimate no-fit, or is every single one being "educated" —
  which would itself be a failure to apply the disqualification step honestly?
- Does the response read as debate/pressure/clever wordplay anywhere? (If so, revise per the
  workflow's own quality gate.)
- Is at least one follow-up asset genuinely medium-specific rather than the same paragraph
  reformatted four times?

## Deploy When

- After collecting real objections from calls, DMs, comments, or analytics and needing to turn
  them into usable education assets rather than one-off rebuttals.
- Before building an objection-handling section for a sales page, FAQ, or call script.
- When a seller is tempted to argue with an objection and needs to diagnose the underlying gap
  instead.
