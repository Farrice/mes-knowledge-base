---
description: Generate a personalized cold outreach message
---

# Cold Outreach Generator

Deploy Nicolas Cole's Free Consulting Pitch Generator for a specific prospect.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-client-acquisition/genius.md`
   - Read `skills/nicolas-cole-client-acquisition/references/prompts/free-consulting-pitch-generator.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: outreach message, audience: specific prospect, context: cold pitch, end state: conversation started, specific persona: Nicolas Cole).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-client-acquisition` skill, `free-consulting-pitch-generator` prompt.

4. Gather input from user:
   - Prospect name and business description
   - Website URL or description
   - Social media presence description
   - Email opt-in / funnel details (if available)
   - User's ghostwriting service

5. Execute the prompt — produce primary outreach message + 5 follow-up messages.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Personalized cold outreach + 5x follow-up for prospect" \
    --expert nicolas-cole \
    --skill nicolas-cole-client-acquisition \
    --workflow cold-outreach-gen \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "Prospect-specific outreach with problem diagnosis"
```
