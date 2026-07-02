---
description: Infinite idea engine
---

# Newsletter Ideation

Generate 10+ newsletter edition concepts using the infinite repeatability engine.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/10-newsletter-ideation.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: 10+ edition concepts + 4-week calendar, audience: self, context: content planning, end state: backlog filled).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `newsletter-ideation` workflow.

4. Gather input: Newsletter tangible asset, domain, audience, any constraints or themes to explore.

5. Execute — Evolution engine inventory, variation types, cross-matrix, calendar mapping.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter ideation — 10+ concepts" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-ideation \
    --type Content \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Ideation sprint with cross-matrix and calendar"
```
