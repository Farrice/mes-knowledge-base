---
description: Free newsletter → $350 product pipeline
---

# Newsletter-to-Product

Design the product your free newsletter naturally sells.

## Steps

1. Load context (Chain Step 4):
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/14-newsletter-to-product.md`
   - Read `skills/nicolas-cole-digital-products/SKILL.md` (Vehicle Framework, $350 threshold)

2. Score intent (Chain Step 1): Score = 5 (deliverable: product design + funnel + revenue projection, audience: newsletter subscribers, context: monetization, end state: 90-day build roadmap).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` + `nicolas-cole-digital-products` (compound stack).

4. Gather input: Newsletter name, tangible asset type, Two Rules status (must PASS), top 5 performing editions, creator expertise areas.

5. Execute — Product seed identification, Vehicle Framework application, newsletter→product funnel architecture, revenue projection, 90-day build roadmap.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter-to-product pipeline — [product name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-to-product \
    --type Strategy \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "Compound stack: newsletter flywheel + digital products"
```

**Execution prompts**: before producing the deliverable, check `skills/nicolas-cole-newsletter-flywheel/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
