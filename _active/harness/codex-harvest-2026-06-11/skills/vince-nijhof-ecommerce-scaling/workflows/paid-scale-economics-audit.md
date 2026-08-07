---
description: Audit whether paid acquisition can scale profitably with current economics
---

# Paid Scale Economics Audit

> **Expert**: Vince Nijhof | **Tier**: Foundation
> **Produces**: Paid-scale finance diagnosis and fix plan

## Inputs Required

1. AOV, COGS, gross margin, shipping, payment fees
2. Current ROAS/CPA by channel
3. OPEX and team cost
4. Repeat purchase, email, subscription, LTV data
5. Inventory cycle, supplier terms, payout timing

## Skill Acquisition

Load:

- `genius.md`
- `references/ecommerce-economics.md`

## Execution

1. **Calculate contribution margin**: Include variable costs, not just gross margin.
2. **Compare break-even and scaling ROAS**: Identify current gap.
3. **Inspect AOV room**: Bundles, volume discounts, upsells, subscriptions.
4. **Inspect LTV support**: Repeat purchase, email, replenishment, retention offers.
5. **Inspect OPEX drag**: Fixed cost per day at current and target revenue.
6. **Inspect cash timing**: Inventory, payment terms, payout delay, stockouts.
7. **Produce scale ceiling**: What spend level breaks the business, and why?

## Content Type Adaptations

| Context | Adaptation |
|---------|------------|
| New brand | Use assumptions and sensitivity bands |
| Existing brand | Use actual trailing 30/60/90 data |
| Subscription product | Weight churn, payback window, refill behavior |
| Heavy product | Stress-test shipping and warehouse complexity |

## Output Requirements

Produce:

```markdown
PAID SCALE ECONOMICS AUDIT

Verdict: [Scale Ready / Fix AOV / Fix Margin / Fix LTV / Fix Cash / Pause Spend]

Economics Table:
| Metric | Current | Target | Issue | Fix |

Scale Ceiling:
- Current safe daily spend:
- Likely break point:
- Constraint:

30-Day Fix Plan:
1. [highest-impact fix]
2. [second fix]
3. [third fix]
```

## Quality Gate

- Do not use ROAS as the only conclusion.
- Name whether the constraint is acquisition, offer, product, ops, cash, or retention.
- Include one pessimistic scenario.

