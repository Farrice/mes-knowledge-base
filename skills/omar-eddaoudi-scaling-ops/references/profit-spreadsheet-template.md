# Profit-First Reverse Engineering Spreadsheet Template

> Per Omar's Spreadsheet Lock signature move: "Profit is always designed. It's not hoped for. You design it, then you reverse-engineer how you're going to acquire customers."

## Section 1: Pricing Anchor

| Field | Value | Notes |
|-------|-------|-------|
| MSRP / Front-end AOV | $___ | Must be ≥ $60 for sustainable e-com economics |
| Average Order Value (with bumps) | $___ | Include order bumps + upsells if priced in |
| Subscription LTV (if applicable) | $___ | Average customer lifetime value across tenure |
| Effective AOV (LTV-adjusted) | $___ | Use this for CAC math if subscription model |

## Section 2: Cost of Delivery (per unit)

| Cost Category | $ Per Unit | Notes |
|---------------|-----------|-------|
| Cost of Goods Sold (COGS) | $___ | Manufacturing + raw materials |
| Packaging | $___ | Box, inserts, protective material |
| Shipping (outbound) | $___ | Use blended rate if mixed methods |
| Returns reserve | $___ | Return rate × cost to refurbish/restock |
| Payment processing (~3%) | $___ | Stripe / PayPal fees |
| Fulfillment / 3PL (per order) | $___ | If using 3PL, blended per-order cost |
| Customer support reserve | $___ | Tickets per order × cost per ticket |
| **Total Cost of Delivery** | **$___** | **Sum of all above** |

## Section 3: Gross Profit Calculation

```
Effective AOV               $___
- Total Cost of Delivery    $___
═══════════════════════════════
= Gross Profit              $___
```

## Section 4: Net Profit Target (THIS DRIVES EVERYTHING)

| Field | Value | Notes |
|-------|-------|-------|
| Target Net Profit per Sale | $___ | Pay yourself first — what do YOU need? |
| Maximum Allowable CAC | Gross Profit − Net Profit Target = $___ | This is your CAC ceiling |
| Target ROAS | AOV ÷ Max CAC = ___x | Your campaign performance gate |

## Section 5: ROAS Gate Decision Matrix

| Scenario | Decision |
|----------|----------|
| ROAS ≥ Target | Scale spend, work on volume |
| ROAS at Target ± 10% | Hold spend, optimize creative |
| ROAS < Target by 10-25% | Diagnose: avatar match? awareness stage? hook? |
| ROAS < Target by >25% | Stop scaling. Re-research. Re-test single creative tier. |
| ROAS impossible to hit | Product / pricing / cost-structure problem — fix BEFORE more spend |

## Section 6: Veto Conditions (Don't Take The Brand / Don't Launch)

If ANY of these are true, return to product/pricing before any spend:

- [ ] Effective AOV < $60 with no LTV multiplier
- [ ] Cost of Delivery > 50% of AOV
- [ ] Gross Profit < $20 per sale
- [ ] Required CAC implies ROAS > 5x to hit profit target on cold traffic
- [ ] No path to retention / repeat purchase / subscription

## Worked Example (Skincare Brand)

| Field | Value |
|-------|-------|
| AOV | $80 |
| LTV multiplier | 1.4x → Effective AOV $112 |
| Cost of Delivery | $34 |
| Gross Profit | $78 (vs. effective AOV) |
| Target Net Profit | $30 |
| Max CAC | $48 |
| Target ROAS (AOV-based) | 1.67x |
| Decision | **VIABLE** — proceed to research stack |

## Anti-Pattern Examples

**Bad math pattern 1: "We'll make it up on volume"**
- AOV $35, COD $20, gross profit $15, target net $10 → max CAC $5
- $5 CAC on cold meta traffic ≈ impossible
- **Verdict**: Product/pricing problem. Don't launch.

**Bad math pattern 2: "We'll figure out the bonuses later"**
- AOV $120, COD $42 (incomplete — missing returns reserve and 3PL)
- Real COD probably $58-65, gross profit $55-62 not $78
- **Verdict**: Re-do math with complete COD before spend.

**Bad math pattern 3: "ROAS will improve over time"**
- True for blended ROAS via retention; NOT TRUE for cold acquisition CAC
- Cold CAC tends to INCREASE with scale, not decrease
- **Verdict**: Math against expected scale-state CAC, not launch CAC.
