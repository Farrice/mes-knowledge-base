---
description: 5 strategies from Nicolas Cole
---

# No-Portfolio Client Landing

Execute the Nicolas Cole no-portfolio client landing methodology.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-client-acquisition/genius.md`
   - Read `skills/nicolas-cole-client-acquisition/workflows/no-portfolio-client-landing.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: strategy set, audience: self, context: no portfolio/proof, end state: client pipeline).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-client-acquisition` skill, `no-portfolio-client-landing` workflow.

4. Gather input from user:
   - Their chosen ghostwriting service
   - How much time per day they can invest
   - Any existing personal content (social posts, blog, newsletter — even with zero audience)
   - Whether they've ever done writing for others (even informally, even free)

5. Execute the workflow exactly as documented — produce ranked strategies, Week 1 action plan, templates, and psychology briefing.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "No-portfolio client landing strategy" \
    --expert nicolas-cole \
    --skill nicolas-cole-client-acquisition \
    --workflow no-portfolio-client-landing \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "5 strategies ranked and customized to user situation"
```
