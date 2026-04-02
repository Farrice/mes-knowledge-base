---
description: Write a SubStack post
---

# Solopreneur 10K Post

Produce a publish-ready SubStack post for Farrice's solopreneur audience.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/11-solopreneur-10k-post.md`
   - Read `FARRICE.md` for voice and brand alignment

2. Score intent (Chain Step 1): Score = 5 (deliverable: SubStack post + LinkedIn teasers, audience: multi-passionate solopreneurs, context: newsletter content, end state: publish-ready, specific: prompt-as-tangible format).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `solopreneur-10k-post` workflow.

4. Gather input: Topic/angle for this edition (or run `/trend-to-newsletter` to generate).

5. Execute — Topic→pain→prompt mapping, full post architecture, voice check, polish, LinkedIn teaser.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "SubStack post — [topic]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow solopreneur-10k-post \
    --type Content \
    --intent 9 --expert-score 9 --adversarial 8 \
    --notes "Full post with prompt tangible asset and LinkedIn teasers"
```
