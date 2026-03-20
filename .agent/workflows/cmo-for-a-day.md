---
description: "Generate a 'CMO for a Day' public pitch post that doubles as authority-building content and prospect outreach"
---

# CMO for a Day

Deploy Nicolas Cole's Pitch-in-Public Content Engine.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-client-acquisition/genius.md`
   - Read `skills/nicolas-cole-client-acquisition/references/prompts/pitch-in-public-content-engine.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: public content post, audience: prospect + similar prospects, context: authority building + prospecting, end state: published content).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-client-acquisition` skill, `pitch-in-public-content-engine` prompt.

4. Gather input from user:
   - Prospect name / business type / specific business to analyze
   - User's ghostwriting service
   - Platform for publication (LinkedIn, Twitter/X, blog, newsletter)
   - Any observations already gathered about the prospect

5. Execute the prompt — produce a complete, publish-ready content piece with share strategy.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Pitch-in-public content piece" \
    --expert nicolas-cole \
    --skill nicolas-cole-client-acquisition \
    --workflow cmo-for-a-day \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "Public prospect analysis post with authority + outreach dual function"
```
