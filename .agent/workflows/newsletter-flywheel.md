---
description: End-to-end newsletter flywheel
---

# Newsletter Flywheel

Execute the full newsletter content flywheel.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/01-newsletter-flywheel.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: newsletter post, audience: subscribers, context: SubStack content creation, end state: publish-ready post with 3 variants).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `newsletter-flywheel` workflow.

4. Gather input from user:
   - Topic or raw idea for this edition
   - Newsletter tangible asset (if already defined; if not, run `/tangible-faucet` first)
   - Any specific angle or constraint

5. Execute the workflow exactly as documented — produce 3 variant posts, editor pick, polished output.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter post — [topic]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-flywheel \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "Full flywheel: research → 3 variants → editor pick → polish"
```
