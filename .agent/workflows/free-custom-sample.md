---
description: Voice-matched content that IS the pitch
---

# Free Custom Sample

Deploy Nicolas Cole's Free Custom Sample Creator for a specific prospect.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-client-acquisition/genius.md`
   - Read `skills/nicolas-cole-client-acquisition/references/prompts/free-custom-sample-creator.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: custom content sample, audience: specific prospect, context: prospecting, end state: sample delivered).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-client-acquisition` skill, `free-custom-sample-creator` prompt.

4. Gather input from user:
   - User's ghostwriting service (LinkedIn posts, newsletters, articles, etc.)
   - Prospect name and business/role description
   - Any of the prospect's existing content (for voice matching)
   - Target topic or angle (optional)

5. Execute the prompt — produce a complete, publish-ready content sample in the prospect's voice + delivery outreach message.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Voice-matched custom sample + delivery message for prospect" \
    --expert nicolas-cole \
    --skill nicolas-cole-client-acquisition \
    --workflow free-custom-sample \
    --type Content \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Voice-matched content sample demonstrating capability through output"
```
