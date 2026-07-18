---
description: Free vs Paid newsletter business model architect with revenue projections
---

# Newsletter Business Model — The Fork

Design the revenue architecture after validating the newsletter concept. Paid = the product itself. Free = education funnel to a product.

## Prerequisites
- Load `nicolas-cole-newsletter-flywheel` skill
- Newsletter concept must PASS the Two Rules Audit (`/book-never-ends`)

## Process

### Step 1: The Fork Question
Ask one question: **"Is this newsletter the product, or is it the path to a product?"**

Present the two architectures side by side:

| Dimension | Paid Newsletter | Free Newsletter |
|-----------|----------------|-----------------|
| **Revenue source** | Subscriptions ($5-50/mo) | Digital product ($49-$350) or service |
| **Skill requirement** | ONE: make the newsletter great | THREE: newsletter + product + funnel |
| **Operational load** | Recurring creation obligation | Front-loaded product creation |
| **Scaling path** | More subscribers = more revenue | More subscribers = more product sales |
| **Risk** | Churn if quality dips | Conversion if funnel breaks |
| **Best for** | Deep domain experts with infinite material | Coaches/consultants with a specific transformation |

### Step 2: Revenue Modeling
For the chosen path, build a napkin-math revenue model:

**Paid Path**:
- Projected free subscribers (Month 6): ___
- Average conversion to paid: 2-5%
- Monthly price: $___
- Projected MRR: subscribers × conversion × price
- Annual projection: MRR × 12

**Free Path**:
- Projected subscribers (Month 6): ___
- Average product conversion: 1-3%
- Product price: $49-$350
- Monthly product revenue: subscribers × conversion × price
- Upsell to higher-ticket: service at $___/mo

### Step 3: Product Architecture (Free Path Only)
If free newsletter → product, design:
1. **The $350 Product**: What tangible digital product does the newsletter sell? (Connects to `nicolas-cole-digital-products` Vehicle Framework)
2. **The Education-to-Purchase Arc**: How does each newsletter issue move the reader closer to buying?
3. **The CTA Strategy**: Soft weekly CTAs vs. periodic launch sequences

### Step 4: Output
Deliver:
- **Recommended model** with reasoning
- **Revenue projection** (conservative, moderate, optimistic)
- **90-day implementation roadmap** for the chosen model
- **Handoff point**: If free → product, hand off to `/design-offer` for product design

## Output Schema

```markdown
# Newsletter Business Model — [Newsletter Name]

## The Fork Decision
Product or path-to-product: [PAID / FREE] — Reasoning: [...]

## Revenue Model (napkin math)
[Paid or Free path table filled with projected numbers]

## Product Architecture (Free path only)
- The $350 Product: [name + description]
- Education-to-Purchase Arc: [...]
- CTA Strategy: [...]

## Recommendation
[Chosen model + reasoning]

## Revenue Projection
Conservative / Moderate / Optimistic: [3 scenarios]

## 90-Day Implementation Roadmap
[Week-by-week]

## Handoff
[Next workflow, e.g. /design-offer]
```

## Quality Gate

- [ ] The Fork question is answered with ONE clean verdict (product vs. path-to-product), not left ambiguous?
- [ ] Revenue projections use napkin-math ranges (conservative/moderate/optimistic), not a single unhedged number?
- [ ] Free path includes a named $350-ceiling product, not a vague "eventually sell something"?
- [ ] The chosen model's skill requirement is stated honestly (paid = 1 skill; free = 3 skills)?
- [ ] Handoff point named for the next concrete action?
