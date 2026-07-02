---
description: Full publication audit against the 10-criterion Quality Rubric
---

# Sinem Audit

Comprehensive publication audit against Sinem Günel's 10-criterion Quality Rubric. Scores every dimension of a Substack publication and prescribes specific fixes for each failing criterion.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Quality Rubric)

2. Score intent: Score = 4.

3. Route: Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Publication URL or name
   - Current subscriber count (free/paid)
   - Current revenue breakdown
   - About page copy (paste or link)
   - Last 3 post titles and formats
   - Notes activity (frequency, engagement)
   - Paid tier description (what's behind the paywall)

5. Audit against all 10 criteria:

   | # | Criterion | Score (1-10) | Diagnosis | Prescription |
   |---|-----------|-------------|-----------|--------------|
   | 1 | Infrastructure Framing | | | |
   | 2 | Positioning Clarity | | | |
   | 3 | Story-First Notes | | | |
   | 4 | Asset-Based Paid Tier | | | |
   | 5 | Campaign Structure | | | |
   | 6 | Recipient-First Outreach | | | |
   | 7 | Retention Engineering | | | |
   | 8 | Discovery-Trust Split | | | |
   | 9 | Multimedia Integration | | | |
   | 10 | Layered Revenue | | | |

6. Output:
   - Overall score (out of 100)
   - Top 3 critical fixes (highest impact, lowest effort)
   - Recommended workflow sequence for remediation
   - 30-day action plan

7. Finalize:
```bash
python3 execution/chain_runner.py finalize "Publication audit — [name]" \
    --expert sinem-gunel --skill substack-business-architecture \
    --workflow sinem-audit --type Audit \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "10-criterion rubric audit with scored diagnostics and prescriptions"
```
