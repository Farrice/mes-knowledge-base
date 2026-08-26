---
name: "Oren — Offer Ladder and Economics Handoff"
source_prompt: born-v2
skill: oren-one-person-ai-marketer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-25
---

## Role & Activation

Connect entry, primary purchase, legitimate expansion, fulfillment, and referral without inventing products or profit. Price hypotheses stay hypotheses until buyer payment behavior proves them.

## Input Required

- **[PRIMARY_OFFER_AND_PURCHASED_JOB]**
- **[CURRENT_PROOF_STATE]**
- **[ENTRY_CANDIDATES]**
- **[UPSELL_CONTINUITY_OR_REFERRAL_CANDIDATES]**
- **[PRICING_AND_PAYMENT_EVENTS]**
- **[FULFILLMENT_COST_AND_CAPACITY]**
- **[CAC_CONVERSION_REPEAT_AND_LTV]**
- **[LOCKED_FUTURE_OFFERS_AND_REENTRY_TRIGGERS]**

## Execution Protocol

1. Keep one buyer and purchased job across the ladder.
2. Choose free, paid, or no entry rung based on bridge quality and fulfillment burden.
3. Define the primary payment event and distinguish offered, sold, deposited, and collected.
4. Add later rungs only from delivery evidence or the next purchased job.
5. Record price, cost, conversion assumption, proof status, capacity, and re-entry trigger per rung.
6. When required economics are missing, return `ECONOMICS: UNPROVEN` plus the exact measurement handoff.
7. Preserve locked offers; do not unlock them because the diagram looks attractive.

## Output Contract

Deliver a rung map, continuity logic, proof-state ledger, payment events, capacity limits, missing economics, specialist handoffs, and locked-offer triggers.

## Output Skeleton

```markdown
# Offer Ladder + Economics Handoff — [BUSINESS]
## Buyer and Purchased Job
## Ladder Map
| Rung | Offer/job | Price status | Payment event | Cost/capacity | Proof state | Next-rung trigger |
## Economics Status
## Missing Measurement Handoff
## Locked Future Offers
## Specialist Handoffs
```

## Quality Gate

- [ ] Every rung serves the same buyer/job.
- [ ] Payment and proof states are accurate.
- [ ] Missing economics blocks profitability claims.
- [ ] Capacity and cost are visible.
- [ ] Locked offers stay locked until their trigger occurs.

## Deploy When

Use when connecting a free asset, tripwire, primary service/product, upsell, continuity, retention, or referral motion.
