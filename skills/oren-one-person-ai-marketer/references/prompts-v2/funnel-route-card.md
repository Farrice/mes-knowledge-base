---
name: "Oren — Funnel Route Card"
source_prompt: born-v2
skill: oren-one-person-ai-marketer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-25
---

## Role & Activation

Choose the minimum funnel route that matches buyer commitment, explanation burden, trust, capacity, evidence, economics, and permission. Templates and tools do not choose the route.

## Input Required

- **[BUYER_JOB_OFFER_LOCK]**
- **[PRICE_OR_COMMITMENT]**
- **[AWARENESS_AND_TRUST]**
- **[EXPLANATION_BURDEN]**
- **[ATTENTION_SOURCE]**
- **[SALES_AND_FOLLOW_UP_CAPACITY]**
- **[PROOF_AND_ECONOMICS]**
- **[PERMISSION_BOUNDARY]**

## Execution Protocol

1. Reject route selection if the buyer/job/offer lock is incomplete.
2. Score lead magnet, tripwire, webinar, VSL, DM, direct-call, and hybrid 0–2 on buyer fit, commitment fit, explanation fit, proof fit, capacity fit, economics visibility, and permission safety.
3. Block tripwire when economics are missing; block DM sends without permission; hand full VSL writing to its owner.
4. Select one primary route and no more than one support route.
5. Break a tie in favor of fewer handoffs and lower operator burden.
6. State prerequisites, rejected alternatives, risks, and one next action.

## Output Contract

Return one decision, its scored reasoning, rejected alternatives, prerequisites, and open risk. Do not return a generic list of funnel types.

## Output Skeleton

```markdown
# Funnel Route Card — [OFFER]
## Lock and Proof State
## Selected Primary Route
## Supporting Route (or NONE)
## Score Table
| Route | Buyer | Commitment | Explanation | Proof | Capacity | Economics | Permission | Total |
## Rejected Alternatives
## Prerequisites
## One Next Action
## Open Risk
```

## Quality Gate

- [ ] One primary route is selected.
- [ ] Rejections are buyer/capacity/evidence reasons, not preference.
- [ ] Tripwire, DM, VSL, and economics boundaries hold.
- [ ] The next action is executable without hidden context.

## Deploy When

Use before building pages, lead magnets, webinars, VSLs, DM sequences, or call flows.
