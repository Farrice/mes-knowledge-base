---
description: Design the full 4-layer revenue architecture for a publication
---

# Sinem Revenue Architect

Design the complete 4-layer revenue architecture for any Substack publication. This is the master strategy workflow that maps the path from free content through high-ticket offers.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md`
   - Read `agents/sinem-gunel/AGENT.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: complete revenue architecture, audience: creator/business owner, context: Substack monetization strategy, end state: 4-layer revenue map with pricing, offers, and conversion pathways).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Current publication and subscriber count
   - What do you sell (or want to sell) beyond the publication?
   - Current revenue breakdown (if any)
   - Target monthly revenue goal
   - Existing assets: courses, templates, frameworks, coaching offers?

5. Design the 4 layers:

   **Layer 1 — Free Content (Discovery)**
   - Purpose: Attract and build trust. NOT to monetize.
   - Define: Publishing cadence, content pillars, Notes strategy
   - Metric: Free subscriber growth rate

   **Layer 2 — Paid Subscriptions (Commitment)**
   - Purpose: Convert trust into commitment. Revenue < 10% of total.
   - Define: What goes behind the paywall (tangible assets, not "more content")
   - Apply: Asset-Based Paywall design (Move 4)
   - Pricing: Monthly vs. annual structure (annual as default)
   - Metric: Free-to-paid conversion rate, annual plan %

   **Layer 3 — Digital Products (Leverage)**
   - Purpose: Productize expertise into scalable assets ($50-$500 range)
   - Define: What products serve the same reader but solve specific problems
   - Stack with: Nicolas Cole's Vehicle Selection for product type choice
   - Metric: Product revenue as % of total, units sold per month

   **Layer 4 — High-Ticket Offers (Maximum Value)**
   - Purpose: Serve the most committed readers at highest value ($1,000+)
   - Define: Coaching, consulting, cohorts, or custom services
   - Design: How the publication qualifies leads for these offers
   - Metric: Revenue per high-ticket client, pipeline conversion rate

6. Build the conversion pathway map:
   - How does a reader move from Layer 1 → 2 → 3 → 4?
   - What triggers each transition?
   - Where are the natural upgrade moments?

7. Apply the <10% Rule:
   - Subscription revenue should be <10% of total business revenue
   - If subscriptions are the primary revenue, the architecture is incomplete
   - Diagnose and prescribe the missing layers

8. Cross-expert stacking (optional):
   - Stack with Nicolas Cole (`/design-digital-product-offer`) for Layer 3 product design
   - Stack with Vincent Hu for Layer 4 high-ticket conversion

9. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Revenue architecture — [publication name]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-revenue-architect \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "4-layer revenue map with <10% rule diagnostic and conversion pathway"
```
