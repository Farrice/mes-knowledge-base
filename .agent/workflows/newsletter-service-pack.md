---
description: "Productize the newsletter flywheel as a bolt-on service with SOW, pricing, and delivery SOP"
---

# Newsletter Service Pack

Package the newsletter flywheel as a sellable service.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/09-newsletter-service-pack.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: productized service package, audience: potential clients, context: service design, end state: 3-tier package with SOW + SOP).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `newsletter-service-pack` workflow.

4. Gather input: Creator's pricing range, target clients, existing service offerings.

5. Execute — Service definition, 3-tier pricing, SOW template, delivery SOP, sales materials.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter service package" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-service-pack \
    --type Strategy \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "3-tier service with SOW, SOP, and sales materials"
```
