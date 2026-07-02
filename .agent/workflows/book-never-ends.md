---
description: Audit any newsletter concept against Cole's Two Rules
---

# Book Never Ends

Two Rules quality gate for any newsletter concept.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/03-book-never-ends.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: audit report, audience: self, context: newsletter validation, end state: pass/fail with prescriptions, specific language: "Two Rules").

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `book-never-ends` workflow.

4. Gather input from user:
   - Newsletter description (any format — sentence, paragraph, pitch)

5. Execute the audit — Rule 1 (Book That Never Ends) + Rule 2 (Tangible Faucet) with structured report.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Two Rules audit — [concept name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow book-never-ends \
    --type Analysis \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Binary audit with fix prescriptions"
```
