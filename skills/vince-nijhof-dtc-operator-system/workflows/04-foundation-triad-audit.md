---
description: Pre-marketing scale gate — audit cash flow, inventory, and supply chain readiness before pouring spend
---

# `/vince-foundation-triad-audit` — Foundation Triad Readiness Gate

Vince's pre-scale audit. Three things must be solid BEFORE pouring spend on ads. Skip this and scale will compound the broken thing — out-of-stock kills momentum, cash flow gaps kill scaling decisions, supply chain failures kill the brand reputation.

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **Pattern 4: The Foundation Triad Gate (Flow + Inventory + Supply Chain)**
- **Signature Move 3: The Foundation Triad Audit Before Spend Increase**

## When to Run

- Brand is about to increase ad spend ≥30% month-over-month
- New brand pre-launch (full triad must be solid before first $1K of ads)
- Existing brand experiencing scaling-related issues (out-of-stock, payment delays, shipping complaints rising)
- Quarterly operational health check
- Acquired brand assessment (before applying Oak Brand Group playbook)
- Post-AAR after a scale event went poorly

## Pre-Flight Gate

| Question | If NO → |
|---|---|
| Does the brand exist (not pre-launch concept)? | Pre-launch needs different workflow — this assumes operational reality |
| Is there at least 1 month of operational data? | Need cash flow + inventory + shipping data points |
| Is the operator willing to halt scale if triad fails? | If founder won't accept "stop scaling" as outcome, this workflow's findings will be ignored — set expectation first |

## Input Required

- **Cash flow data**: 90-day P&L, cash on hand, outstanding receivables, payment terms with suppliers
- **Inventory data**: SKU-level stock levels, sell-through velocity, reorder lead times, % of catalog out-of-stock or low-stock
- **Supply chain data**: shipping carrier performance, fulfillment center capacity, return rate, customer complaints related to shipping
- **Planned scale increase**: target spend, target revenue, time horizon
- **Current performance**: blended ROAS, CAC, AOV, repeat purchase rate

## Execution

You are Vince Nijhof's operations partner running the pre-scale gate. You don't recommend "scale carefully" — you give a binary GO / HALT verdict on each pillar with the specific operational risk if violated.

### Pillar 1: CASH FLOW

Audit checklist:
1. **Runway**: How many months of current burn does cash cover? (Minimum: 3 months for safe scale, 6 months for aggressive scale)
2. **Ad spend coverage**: Can the brand absorb 60-90 day delay between ad spend and revenue collection (typical for DTC at scale)? (Checkout → Stripe payout → ad reimbursement cycle)
3. **Supplier payment terms**: Are suppliers on Net 30 / Net 60 / payment-on-order? (POOR-on-order with no credit line = scale will outrun cash)
4. **Receivables**: Any large outstanding receivables (especially Amazon, retail, B2B)? Can these be factored if needed?
5. **Credit facilities**: Line of credit available? AmEx Plat / Capital On Tap / Wayflyer / 8fig / etc. tested limits?
6. **Tax reserves**: Has the brand reserved for VAT/sales tax/income tax obligations from prior period?

Verdict: 🟢 SAFE / 🟡 SCALE WITH CONDITIONS / 🔴 HALT

If 🔴: do NOT increase spend. Fix cash flow first (extend supplier terms, secure credit line, factor receivables, raise capital).

### Pillar 2: INVENTORY

Audit checklist:
1. **Hero SKU stock cover**: Does the top-performing SKU have ≥45 days of stock at PROJECTED scale velocity (not current)?
2. **Reorder lead time vs. stock cover**: If lead time is 60 days, you need 60+15 buffer = 75+ days minimum cover
3. **% of catalog at risk**: How many SKUs are at <30 days cover? (If >20% of catalog → fragility)
4. **Allocation flexibility**: Can stock be re-allocated across channels if Meta scale spikes a specific SKU?
5. **Pre-order buffer**: Can you accept pre-orders if stock-out occurs? (Hard mode but better than lost demand)
6. **3PL capacity**: Does your fulfillment partner have headroom for the projected order volume? (Especially Q4 or peak season scale)

Verdict: 🟢 SAFE / 🟡 SCALE WITH CONDITIONS / 🔴 HALT

If 🔴: do NOT increase spend. Vince's exact quote: "We immediately feel it" when out-of-stock — Amazon ranking drops, blended ROAS tanks, customer complaints spike. The cost of stock-out at scale is exponentially higher than the cost of carrying extra inventory.

### Pillar 3: SUPPLY CHAIN

Audit checklist:
1. **Carrier performance**: On-time delivery rate? Damaged-in-transit rate? Lost shipment rate?
2. **Fulfillment center capacity**: Pick/pack/ship capacity at projected scale? Especially peak hours?
3. **Returns / RMA process**: Return rate trending? Process scalable? Refund cycle time customer-acceptable?
4. **Customer service capacity**: Tickets-per-hour capacity vs. projected order volume? Self-serve options reducing ticket load?
5. **International shipping**: If selling cross-border, are duties/customs handled smoothly? VAT compliance in place?
6. **Reverse logistics**: For categories with high returns (apparel, beauty), is the returns flow not creating worse-than-no-sale outcomes?

Verdict: 🟢 SAFE / 🟡 SCALE WITH CONDITIONS / 🔴 HALT

If 🔴: do NOT increase spend. Supply chain failures are the slowest to fix and the most damaging to brand reputation (1-star reviews compound, Trustpilot rating tanks, customer LTV drops).

### Composite Verdict

| Pillar | Verdict | Critical Issues |
|---|---|---|
| Cash Flow | 🟢/🟡/🔴 | [...] |
| Inventory | 🟢/🟡/🔴 | [...] |
| Supply Chain | 🟢/🟡/🔴 | [...] |

**SCALE DECISION**:
- All 🟢 → SCALE GREEN-LIGHT (proceed with planned spend increase)
- Any 🟡 → SCALE WITH CONDITIONS (proceed with named guardrails)
- Any 🔴 → SCALE HALT (do not increase spend until issue resolved)

### Step Final: Recommended Actions

For each non-green pillar, output the specific fix:
- What needs to be fixed
- Who owns the fix
- Timeline to fix
- KPI / milestone that confirms fix is in place
- Re-audit trigger (when to re-run this workflow)

## Output Schema

```markdown
# [Brand] — Foundation Triad Audit ([Date])

## Context
- **Planned scale increase**: $[X] → $[Y] over [N] days
- **Current state**: [Revenue, blended ROAS, brand stage]
- **Audit owner**: [Who ran this]

## Pillar 1: Cash Flow
- Runway: [N months]
- Ad spend coverage cycle: [...]
- Supplier terms: [...]
- Receivables: [...]
- Credit facilities: [...]
- Tax reserves: [...]
- **Verdict**: 🟢/🟡/🔴
- **Critical issues**: [if any]

## Pillar 2: Inventory
- Hero SKU stock cover: [days at projected velocity]
- Reorder lead time vs. cover: [...]
- % of catalog at risk: [...]
- Allocation flexibility: [...]
- 3PL capacity: [...]
- **Verdict**: 🟢/🟡/🔴
- **Critical issues**: [if any]

## Pillar 3: Supply Chain
- Carrier performance: [...]
- Fulfillment capacity: [...]
- Returns / RMA: [...]
- Customer service capacity: [...]
- International / VAT: [...]
- Reverse logistics: [...]
- **Verdict**: 🟢/🟡/🔴
- **Critical issues**: [if any]

## SCALE DECISION
**[GREEN-LIGHT / WITH CONDITIONS / HALT]**

[Reasoning in 2-3 sentences]

## Recommended Actions (for any non-green pillar)

### [Pillar]: [Issue]
- Fix: [Specific action]
- Owner: [Name / role]
- Timeline: [Days to fix]
- Confirmation milestone: [...]
- Re-audit trigger: [When to re-run this workflow]

## What Happens If You Ignore This
[For each non-green pillar, name the specific failure mode at scale: "If you scale to $X without fixing inventory, the hero SKU will go out-of-stock in N days, Meta will tank the account, and you'll lose [Z] in lost demand + acquisition cost."]
```

## Quality Gate

Score against `genius.md` rubric. Critical for this workflow:
- **Foundation Triad Awareness** (9+ required): all 3 pillars audited with specific data, not vibes
- **Operational Realism** (9+ required): recommendations match brand stage and operational capability
- **System vs. Tactic** (8+ required): re-audit trigger defined, not one-time check

If Foundation Triad Awareness < 6 → automatic veto. The workflow exists FOR this dimension.

## Content Type Adaptations

| If brand is at stage... | Adjust audit thresholds by... |
|---|---|
| **Pre-launch / 0-$500K** | Triad must be 100% green before first ad dollar; no conditions allowed |
| **$500K-$2M** | 🟡 acceptable on cash flow if credit line in place; inventory + SC must be 🟢 |
| **$2M-$10M** | All 🟢 required for >50% spend increase; conditions OK for 20-50% |
| **$10M+ omnichannel** | Audit per channel — Meta-only triad ≠ omni triad; each channel adds complexity |
| **Acquired brand assessment** | Triad is the buy/walk decision input — 🔴 doesn't necessarily mean walk, but pricing reflects fix cost |
| **Post-crisis recovery** | Re-audit weekly during recovery phase, not quarterly |

## Pairs With

- `/vince-creative-pod-architect` — pod architecture decisions assume foundation triad is green
- `/vince-omni-channel-readiness` — omni-channel expansion gates on this audit
- `/vince-portfolio-acquisition-blueprint` — acquisition target evaluation includes this audit
- Danny Yeung `dtc scaling` — partner workflow for post-audit operational pivots
