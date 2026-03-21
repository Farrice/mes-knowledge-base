---
description: "Monthly newsletter health check — re-validate Two Rules, diagnose tangible asset health, prescribe adjustments"
---

# Newsletter Review Cycle

Monthly audit for any active newsletter.

## Steps

1. Load context (Chain Step 4):
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/13-newsletter-review-cycle.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: diagnostic report + next month calendar, audience: self, context: newsletter performance review, end state: prioritized fixes).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `newsletter-review-cycle` workflow.

4. Gather input: Newsletter name, last 4-8 editions with tangible assets, available metrics (open rate, click rate, churn rate), any subscriber feedback.

5. Execute — Two Rules re-validation, metric diagnosis, domain evolution scan, tangible asset health score, prescriptions, next month calendar.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter review cycle — [newsletter name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-review-cycle \
    --type Analysis \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "Monthly audit with Two Rules re-validation"
```
