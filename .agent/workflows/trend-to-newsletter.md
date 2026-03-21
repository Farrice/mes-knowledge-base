---
description: "Trending topic → audience pain → underserved opportunity → newsletter content angle"
---

# Trend to Newsletter

Research engine that converts trends into newsletter edition concepts.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/06-trend-to-newsletter.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: 3 edition concepts, audience: self/subscribers, context: content research, end state: prioritized edition ideas).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `trend-to-newsletter` workflow.

4. Gather input: Newsletter domain, tangible asset type, audience profile.

5. Execute — Trend scan, pain mapping, cross-pattern matrix, tangible asset application.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Trend research — [domain]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow trend-to-newsletter \
    --type Research \
    --intent 8 --expert-score 8 --adversarial 7 \
    --notes "Trend scan with cross-pattern matrix"
```
