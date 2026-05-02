---
description: Annual plan conversion + welcome sequences + subscriber chat bridges
---

# Sinem Retention Engine

Deploy Sinem Günel's retention engineering system — annual plan conversion, personalized welcome sequences, and subscriber chat bridges that convert "interesting" into "I trust these people."

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Moves 6-7)

2. Score intent: Score = 4.

3. Route: Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Current paid subscriber count and monthly/annual split
   - Current welcome sequence (if any)
   - Are you using Substack Chat? If so, how?
   - Monthly churn rate (if known)

5. Build the 3-layer retention system:

   **Layer 1 — Annual Plan Conversion**
   - Position annual as default (significant discount, 15-20% off)
   - Design pricing so monthly feels expensive by comparison
   - Create annual-only bonus pack to incentivize upgrade
   - Welcome sequence references the "full-year journey"

   **Layer 2 — Welcome Sequence**
   - Message 1 (immediate): Personal welcome + link to highest-value asset
   - Message 2 (day 3): "Here's what most members miss" — guide to hidden gems
   - Message 3 (day 7): Ask a genuine question about their challenges
   - Each message must be personalized, not generic template

   **Layer 3 — Subscriber Chat Bridge**
   - Welcome every new paid member in chat within 24 hours
   - Ask about their specific challenges
   - Point them to 1-2 resources based on their response
   - This converts "interesting" to "I trust these people"

6. Finalize:
```bash
python3 execution/chain_runner.py finalize "Retention engine — [publication]" \
    --expert sinem-gunel --skill substack-business-architecture \
    --workflow sinem-retention-engine --type Strategy \
    --intent 8 --expert-score 8 --adversarial 7 \
    --notes "3-layer: annual conversion + welcome sequence + chat bridge"
```
