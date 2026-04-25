# /velocity-cac-ltv — Subscription Unit Economics Engine

> Engineer CAC/LTV subscription models with sub-4-month payback and 3.0-3.5x LTV-to-CAC ratios using Danny Yeung's IM8 economics playbook.

## When to Use
- Launching or optimizing a subscription product
- CAC payback period exceeds 4 months
- LTV-to-CAC ratio is below 3.0x
- Need to design a subscription tier structure from scratch

## Inputs Required
1. Product/service and pricing
2. Current CAC by channel (Meta, Google, organic, etc.)
3. Current average order value (AOV)
4. Current customer retention rates (monthly/quarterly)
5. Fulfillment/COGS per unit
6. Current subscription model (if any)

## Execution Steps

### Step 1: Baseline Economics Audit
Calculate current state:
```
Current CAC = Total acquisition spend / New customers
Current AOV = Total revenue / Total orders
Current Payback = CAC / (AOV × Margin)
Current LTV = (AOV × Avg orders per customer) × Margin
LTV:CAC Ratio = LTV / CAC
```

### Step 2: The 3-Month Subscription Design
Engineer the Danny Yeung quarterly subscription:

**Pricing Architecture**:
- Monthly price × 3 = baseline quarterly price
- Apply 10-15% discount for quarterly commitment
- Bundle digital access (masterclasses, expert content) to justify premium tier
- Single shipment saves 2x logistics costs

**Revenue Recognition**:
- Recognize full quarterly revenue upfront
- This smooths financial reporting
- For venture-backed: dramatically improves quarterly metrics

**Habitualization Window**:
- 3 months = sufficient time for customer to see results
- Products requiring behavior change NEED this minimum window
- Monthly subscriptions churn before results appear → 3-month solves this

### Step 3: CAC Engineering
Target: Sub-4-month payback on first purchase.

**Channel Mix** (Danny Yeung's actual allocation):
| Channel | Allocation | Role |
|---|---|---|
| Meta (Instagram/Facebook) | 85% | Primary acquisition |
| Google | 15% | Intent capture |
| TikTok | Expanding | Awareness + younger demo |
| Amazon | Separate | Marketplace presence only |

**Creative Volume Rule**:
- Minimum 50 live creatives at any time
- Scale to 1,500+ as budget allows
- 75% static / 25% video ratio
- Produce 10 new creatives per week minimum
- Kill underperformers within 72 hours

### Step 4: LTV Maximization
Target: 3.0-3.5x LTV:CAC ratio.

**Retention Engineering**:
1. **3-month subscription lock** — Customer uses product long enough to see results
2. **Digital access layer** — Expert masterclasses, Q&A sessions, exclusive content
3. **Community building** — Subscribers interact with each other and experts
4. **Upsell architecture** — Product bundles, complementary products, premium tiers

**AOV Expansion**:
- Bundle 2-3 products in quarterly box
- Offer "starter kit" with full product range
- Premium tier with digital access at 30-40% higher price
- Limited edition or seasonal additions

### Step 5: Unit Economics Validation
Run the complete model:
```
New CAC target = First purchase AOV × Margin × (1/4)
[Must payback within 4 months]

New LTV target = CAC × 3.5
[Minimum 3.0x, target 3.5x]

Contribution Margin = Revenue - COGS - Shipping - Payment Processing
[Must be positive on first order]

Break-even cohort timeline: Month 4 or earlier
```

## Output Format
```
## SUBSCRIPTION ECONOMICS MODEL — [Product/Brand]

### Current State
| Metric | Current | Target |
|---|---|---|
| CAC | $X | $X |
| AOV | $X | $X |
| Payback Period | X months | <4 months |
| LTV:CAC | X.Xx | 3.0-3.5x |

### 3-Month Subscription Design
[Tier structure, pricing, digital access bundle]

### Channel Allocation
[Budget split with creative volume targets]

### LTV Maximization Plan
[Retention, upsell, and community architecture]

### Financial Model
[12-month projection with cohort economics]
```

## Quality Gate
- Payback period must be under 4 months or action plan to get there
- LTV:CAC must target 3.0x minimum
- Must include digital access layer design (not just product)
- Creative volume plan must specify weekly production targets
- Must show the math — no hand-waving on economics
