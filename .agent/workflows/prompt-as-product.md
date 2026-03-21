---
description: "Create tangible prompts that extend coaching ability — the 'extension of you' newsletter engine"
---

# Prompt as Product

Create coaching prompts as the newsletter's tangible faucet asset.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/08-prompt-as-product.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: 5 coaching prompts in newsletter format, audience: newsletter subscribers, context: tangible asset creation, end state: deploy-ready prompts).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `prompt-as-product` workflow.

4. Gather input: Creator's expertise domain, target audience, 5-10 core coaching questions they use, specific topic for this batch.

5. Execute — Expertise decomposition, prompt architecture, quality gate, newsletter integration format.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Coaching prompts — [domain]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow prompt-as-product \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "5 coaching prompts with newsletter integration"
```
