---
description: Free vs Paid newsletter business model architect
---

# Newsletter Biz Model

Design the revenue architecture for a newsletter — paid subscription vs. free→product funnel.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/04-newsletter-biz-model.md`
   - Read `skills/nicolas-cole-digital-products/SKILL.md` (for Vehicle Framework + $350 threshold)

2. Score intent (Chain Step 1): Score = 4 (deliverable: business model + revenue projections, audience: self, context: newsletter monetization, end state: chosen model with 90-day roadmap).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` + `nicolas-cole-digital-products` (stacked).

4. Gather input: Newsletter concept (must pass Two Rules first), target audience, existing products/services (if any).

5. Execute — The Fork question, revenue modeling, product architecture (if free path), implementation roadmap.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter business model — [free/paid]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-biz-model \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Business model fork with revenue projections"
```

**Execution prompts**: before producing the deliverable, check `skills/nicolas-cole-newsletter-flywheel/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
