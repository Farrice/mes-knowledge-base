---
description: Build complete unit economics + CAC/ROAS gate document before any media spend
---

# 01 — Profit-First Brand Architecture

> Per Omar's Spreadsheet Lock: "Profit is always designed. It's not hoped for. You sit with a spreadsheet and you reverse-engineer how you're going to acquire customers."

This is the foundation workflow — the first workflow Omar runs on every brand engagement, before any creative or media spend decisions.

## Pre-Flight Gate

Run this workflow when:
- ✅ New brand pre-launch (mandatory before media spend)
- ✅ Existing brand considering significant scale (>3x current spend)
- ✅ Stuck brand diagnosing why scale is unprofitable
- ✅ Client engagement opening — "should I take this brand?"

Skip / defer when:
- ❌ Brand already has documented unit economics from last 90 days
- ❌ Pre-product (no MSRP / no COGS data yet) — return when you have actuals
- ❌ Service business with no per-unit cost structure (use service P&L instead)

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Patterns 1-2: PFRE, the math discipline)
- `skills/omar-eddaoudi-scaling-ops/references/profit-spreadsheet-template.md` (the actual template)

Optional cross-reference:
- `skills/omar-eddaoudi-scaling-ops/references/awareness-pyramid-mapping.md` (CAC ceiling math by stage)

## Execution

### Step 1: Inventory the Pricing Reality

Capture from the brand:
- MSRP per unit
- Average Order Value (with bumps/upsells if priced in)
- Subscription model? If yes, average customer LTV across tenure
- Bundle / kit pricing if applicable

Output to spreadsheet Section 1.

### Step 2: Build the Cost-of-Delivery Stack

Work through every cost on a per-unit basis:
- Cost of Goods Sold (raw + manufacturing)
- Packaging (box + inserts + protective)
- Outbound shipping (blended rate)
- Returns reserve (return rate × cost to refurbish)
- Payment processing (Stripe/PayPal ~3%)
- 3PL / fulfillment per-order
- Customer support reserve

**Critical**: Do NOT skip any line. The most common source of profit-math failure is incomplete COD.

Output to spreadsheet Section 2.

### Step 3: Calculate Gross Profit

```
Effective AOV − Total COD = Gross Profit per Sale
```

If gross profit < $20 per sale, flag immediately. Most ad-driven ecom needs $25+ gross profit to support cold acquisition.

Output to spreadsheet Section 3.

### Step 4: Set Net Profit Target (the Anchor)

Ask the operator: "What net profit per sale do you NEED to hit to make this business worth running?"

Common answers:
- Lifestyle business: $15-30/sale
- Scale-stage venture: $20-50/sale
- Aggressive growth (reinvesting): $5-15/sale (acceptable if path to LTV exists)

This number becomes the ANCHOR for all CAC math.

### Step 5: Derive Max CAC + ROAS Gate

```
Maximum Allowable CAC = Gross Profit − Net Profit Target
Target ROAS = AOV ÷ Max CAC
```

This ROAS becomes the gate for every campaign decision.

### Step 6: Run the ROAS Gate Decision Matrix

Test scenarios against the matrix:
- ROAS at target ± 10% → optimize creative
- ROAS off by 10-25% → diagnose (avatar / awareness / hook)
- ROAS off by 25%+ → STOP scaling, re-research
- ROAS impossible → product / pricing / cost-structure problem

### Step 7: Run the 5 Veto Conditions

Final gate check — if ANY of these are true, return to product/pricing before any spend:
- [ ] Effective AOV < $60 with no LTV multiplier
- [ ] Cost of Delivery > 50% of AOV
- [ ] Gross Profit < $20 per sale
- [ ] Required CAC implies ROAS > 5x on cold traffic
- [ ] No path to retention / repeat purchase / subscription

### Step 8: Produce the Decision Document

Write `profit-architecture-decision.md` with:
1. Filled spreadsheet (all 6 sections)
2. Go / no-go decision with rationale
3. CAC ceiling + ROAS gate
4. Pre-launch optimization recommendations (if any)
5. Recommended next workflow (`/omar-research-stack` if VIABLE, or product/pricing fix loop)

## Content Type Adaptations

| Brand Type | Adaptation |
|-----------|------------|
| Single-SKU ecom | Use template as-is |
| Multi-SKU / collection | Run template per hero SKU; blended COD across catalog |
| Subscription DTC | LTV multiplier critical — model 6/12/24-month cohorts |
| High-ticket info product | COD = delivery infrastructure + community + guarantee reserve |
| Service business | Substitute "client lifetime value" for "AOV"; "service delivery cost" for "COD" |
| Wholesale + DTC hybrid | Run template on DTC channel only; wholesale uses different math |

## Output Requirements

The deliverable must include:
- ✅ Complete spreadsheet (all 6 sections populated)
- ✅ Explicit max CAC number in dollars
- ✅ Explicit target ROAS multiple
- ✅ Go / no-go decision with rationale
- ✅ Identified failure modes (if any) with specific fixes
- ✅ Recommendation for next workflow

## Quality Gate

Score against `genius.md` Quality Rubric Criterion 1 (Profit Math Defensibility). Pass condition: 8+/10.

**Veto**: If any line item in COD is "we'll figure it out later," reject and return to data collection.

**Anti-pattern check**: Does the deliverable include "we'll make it up on volume" or "ROAS will improve over time" without specific math? If yes → fail, rewrite with hard numbers.

**Worked example check**: Does the math hold up under 3x scale stress test? CAC tends to inflate at scale, not compress. Test against scale-state CAC, not launch CAC.
