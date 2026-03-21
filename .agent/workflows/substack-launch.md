---
description: "Zero-to-first-post SubStack launch — positioning, naming, about page, first 3 posts planned"
---

# SubStack Launch

Complete SubStack launch sequence from zero.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/05-substack-launch.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: complete SubStack launch package, audience: subscribers, context: SubStack, end state: name + about page + 3 posts planned).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `substack-launch` workflow.

4. Gather input: Validated newsletter concept (Two Rules passed), tangible asset defined, business model chosen.

5. Execute — Name, about page, 3-post proof sequence, pre-launch checklist, LinkedIn announcement.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "SubStack launch package — [newsletter name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow substack-launch \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 8 \
    --notes "Complete launch package with name, about page, 3 posts, checklist"
```
