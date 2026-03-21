---
description: "Map newsletter to revenue — free→$350 product pathway or paid subscription with pricing"
---

# Newsletter Monetize

Design the complete revenue architecture for a newsletter.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/07-newsletter-monetize.md`
   - Read `skills/nicolas-cole-digital-products/SKILL.md` (Vehicle Framework)

2. Score intent (Chain Step 1): Score = 4 (deliverable: revenue architecture, audience: self, context: newsletter monetization, end state: pricing + projections).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` + `nicolas-cole-digital-products`.

4. Gather input: Newsletter concept (validated), current subscribers (if any), existing products.

5. Execute — Path A or B, revenue modeling, CTA architecture, projections.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Revenue architecture — [model type]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-monetize \
    --type Strategy \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "Revenue architecture with projections"
```
