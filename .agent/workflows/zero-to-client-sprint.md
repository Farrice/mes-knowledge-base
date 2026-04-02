---
description: removal list through first 3 paying clients
---

# Zero-to-Client Sprint

Execute the Nicolas Cole client acquisition sprint.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-client-acquisition/genius.md`
   - Read `skills/nicolas-cole-client-acquisition/workflows/zero-to-client-sprint.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: sprint plan, audience: self, context: ghostwriting client acquisition, end state: paying clients).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-client-acquisition` skill, `zero-to-client-sprint` workflow.

4. Gather input from user:
   - Current time available per day for client acquisition
   - What ghostwriting services they already practice (even on themselves)
   - Brief description of current situation (employed, freelancing, brand new, etc.)

5. Execute the workflow exactly as documented — produce a complete 30-day sprint plan.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "30-day client acquisition sprint plan" \
    --expert nicolas-cole \
    --skill nicolas-cole-client-acquisition \
    --workflow zero-to-client-sprint \
    --type Strategy \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "Full sprint plan with removal list, service selection, credibility assets, outreach sequences"
```
