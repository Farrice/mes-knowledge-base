---
description: Monthly content system audit
---

# /content-review-cycle — Monthly Content System Review

Run the monthly review cycle that audits the entire content system — all profiles, style cards, talking points, hook formulas, and topic clusters — and proposes targeted improvements. The self-improving skill that upgrades all other skills.

## Usage

```
/content-review-cycle --period "June 2025"
/content-review-cycle --previous-review .tmp/kieran-flanagan/review-may-2025.md
```

**Note**: This workflow should run monthly — no more frequently. Weekly adjustments create instability.

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-ops/SKILL.md`
2. `skills/kieran-flanagan-content-ops/genius.md`
3. `skills/kieran-flanagan-content-ops/workflows/03-content-review-cycle.md`

### 2. Execute Workflow
Follow the workflow in `03-content-review-cycle.md` using the loaded genius context.

### 3. Save Output
Save monthly review to `.tmp/kieran-flanagan/review-[month]-[year].md`.
