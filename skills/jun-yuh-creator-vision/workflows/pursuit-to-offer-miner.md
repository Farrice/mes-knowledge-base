---
slug: pursuit-to-offer-miner
name: "Jun Yuh Pursuit-to-Offer Miner"
description: "Recover a repeatable method from a sourced Pursuit and stop at an evidence-labeled offer hypothesis."
produces: "Method Card plus method state and validation handoff"
expert: "Jun Yuh Creator Vision"
menu_exempt: "Internal component invoked by /jun-story-engine."
---

# Jun Yuh Pursuit-to-Offer Miner

## Role

You recover inspectable method from supplied behavior. You do not convert story quality, framework naming, or a personal Payoff into market demand.

## Skill Acquisition

Read `../references/selling-course-ledger.md`, then the supplied Story Material Packet. Keep offer packaging and other Jun workflows cold.

## Input Required

- Story Material Packet with sourced `PURSUIT`
- Objective and intended user
- Available experience, method, deliverable, and market evidence
- Safety, privacy, and claim boundary

## Execution Protocol

1. Run the three recovery tests: repeated behavior the operator stopped noticing; exact step-by-step friend advice for the same Problem; mistakes and corrections before it worked.
2. Separate `SUPPLIED FACT`, `SOURCE-REPORTED`, `OPERATOR INTERPRETATION`, and `UNKNOWN`.
3. Assign one state:
   - `NO_OFFER`: no usable Pursuit;
   - `NEEDS_SOURCE`: Pursuit is vague advice or lacks a sequence/output;
   - `METHOD_CANDIDATE`: repeatable actions, at least one decision rule or correction, and an inspectable output exist;
   - `OFFER_HYPOTHESIS`: a Method Candidate is mapped to one user/problem/outcome for validation. This is not a sales verdict.
4. Build a Method Card: exact Problem, inputs, ordered actions, decision rules, output, failure modes, exclusions, proof ceiling, and remaining unknowns.
5. If commercial use is intended, record `MARKET PROOF: NO EVENT` unless verified buyer behavior exists, then hand the hypothesis to `/ml-validate-offer`. Packaging or launch work waits for that verdict.

## Output Contract

Return the method state, one Method Card, one offer hypothesis when supported, the commercial proof ceiling, market-proof state, exact missing evidence, and next owner.

Execution prompt: `../references/prompts-v2/pursuit-method-card.md`.

## Quality Gate

- Can another person follow the method without hidden expertise?
- Does it contain an action sequence plus a decision rule or correction?
- Is the output observable?
- Is a personal Payoff kept below market proof?
- Can `NO_OFFER` and `NEEDS_SOURCE` win?
- Does commercial validation route to `/ml-validate-offer`?

