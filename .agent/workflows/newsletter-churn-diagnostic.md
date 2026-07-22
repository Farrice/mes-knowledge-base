---
description: Diagnose why subscribers leave
---

# Newsletter Churn Diagnostic

Map subscriber loss to root cause and prescribe specific fixes.

## Steps

1. Load context (Chain Step 4):
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/15-newsletter-churn-diagnostic.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: churn diagnosis + prescription, audience: self, context: subscriber retention, end state: classified root cause with fix plan).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `newsletter-churn-diagnostic` workflow.

4. Gather input: Newsletter name, churn data (3-6 months), last 8-12 editions with tangible asset per edition, engagement metrics, unsubscribe survey data (if available).

5. Execute — Churn classification (faucet failure / faucet drift / delivery failure / audience mismatch), forensic audit, faucet test replay, diagnosis report with specific prescriptions.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter churn diagnostic — [newsletter name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-churn-diagnostic \
    --type Analysis \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "Churn classified as [type], prescription issued"
```

**Execution prompts**: before producing the deliverable, check `skills/nicolas-cole-newsletter-flywheel/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
