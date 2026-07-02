---
description: Quarterly publication health check with revenue layer diagnostics
---

# Sinem Quarterly Review

Quarterly publication health check using Sinem Günel's methodology. Re-validates the Three Questions positioning, audits revenue layer balance, and recalibrates the Notes discovery engine.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md`

2. Score intent: Score = 4.

3. Route: Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Publication metrics for the past 90 days:
     - Free subscriber growth (start → end)
     - Paid subscriber growth (start → end)
     - Revenue by layer (subscriptions, products, high-ticket)
     - Top 5 posts by engagement
     - Top 5 notes by engagement
     - Churn rate (monthly and annual)
   - Any changes to your business model or offers
   - What felt hardest this quarter?

5. Quarterly diagnostic:

   **A. Positioning Re-Lock**
   - Re-answer the Three Questions. Have they changed?
   - If yes: reposition. Run `/sinem-publication-setup`.
   - If no: validate alignment between answers and recent content.

   **B. Revenue Layer Balance**
   - Calculate % of revenue from each layer
   - Apply the <10% Rule: is subscription revenue <10% of total?
   - If subscriptions are >10% of total: diagnose missing layers
   - Prescribe: which layer needs the most investment next quarter?

   **C. Notes Discovery Audit**
   - Are notes story-driven or educational? (review top 10)
   - What's the subscriber conversion rate from Notes?
   - Posting cadence vs. target cadence
   - Prescribe adjustments

   **D. Retention Check**
   - Monthly vs. annual subscriber split
   - Churn rate trend (improving, flat, worsening)
   - Welcome sequence effectiveness
   - Prescribe: run `/sinem-retention-engine` if churn >5%/month

6. Output: Quarterly scorecard + next-quarter priorities (top 3 actions).

7. Finalize:
```bash
python3 execution/chain_runner.py finalize "Quarterly review — [publication] Q[N]" \
    --expert sinem-gunel --skill substack-business-architecture \
    --workflow sinem-quarterly-review --type Audit \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Quarterly health check: positioning + revenue layers + Notes + retention"
```
