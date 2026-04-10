---
description: Pair newsletter output with LinkedIn/ghostwriting proof
---

# Newsletter Social Proof

Convert newsletter editions into LinkedIn posts, portfolio proof, and case studies.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/12-newsletter-social-proof.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: 3 LinkedIn posts + portfolio proof, audience: LinkedIn + prospects, context: cross-platform content, end state: weekly content calendar).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `newsletter-social-proof` workflow.

4. Gather input: Published or ready-to-publish newsletter post, whether user offers ghostwriting/content services.

5. Execute — 3 LinkedIn variants, ghostwriting portfolio proof, content calendar integration.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Social proof amplification — [newsletter edition]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-social-proof \
    --type Content \
    --intent 8 --expert-score 8 --adversarial 7 \
    --notes "3 LinkedIn variants + portfolio proof + calendar"
```
