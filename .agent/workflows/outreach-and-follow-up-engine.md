---
description: Build and execute a complete outreach pipeline
---

# Outreach & Follow-Up Engine

Execute the Nicolas Cole outreach and follow-up pipeline.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-client-acquisition/genius.md`
   - Read `skills/nicolas-cole-client-acquisition/workflows/outreach-and-follow-up-engine.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: outreach pipeline, audience: self, context: client acquisition, end state: filled pipeline).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-client-acquisition` skill, `outreach-and-follow-up-engine` workflow.

4. Gather input from user:
   - Their chosen ghostwriting service and price range
   - Description of personal network (who they know — family, friends, former colleagues, industry contacts)
   - Target prospect description (industry, company size, titles — "anyone who needs content" is fine)
   - Time available for daily outreach

5. Execute the workflow exactly as documented — produce Leaks & Faucets map, warm/cold outreach scripts, 5x follow-up sequences, daily schedule, and pipeline tracker.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Complete outreach pipeline with network map and follow-up sequences" \
    --expert nicolas-cole \
    --skill nicolas-cole-client-acquisition \
    --workflow outreach-and-follow-up-engine \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Leaks/Faucets map, warm scripts, cold outreach, 5x follow-up, pipeline tracker"
```

**Execution prompts**: before producing the deliverable, check `skills/nicolas-cole-client-acquisition/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
