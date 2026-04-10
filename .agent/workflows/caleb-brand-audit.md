---
description: 360° brand diagnostic
---

# /caleb-brand-audit — 360° Brand Health Diagnostic

Audit any personal brand against all 24 Caleb Ralston patterns, score the full quality rubric, and route to the exact fix workflow for each weakness.

## Usage

```
/caleb-brand-audit [brand/person name]
/caleb-brand-audit "My brand"
/caleb-brand-audit   # (audits user's own brand)
```

## Steps

### 1. Load Skills
// turbo
Read these files:
1. `skills/caleb-ralston-personal-brand/genius.md` — need all 24 patterns + quality rubric
2. `skills/caleb-ralston-personal-brand/workflows/caleb-brand-audit-360.md`

### 2. Collect Content Samples
Ask the user to share or point to their last 5-10 content pieces (links, screenshots, or text). If unavailable, work from description of their current brand state.

### 3. Execute 360° Audit
Follow the 5-phase workflow:
1. **Pattern Audit** — score all 24 patterns across 7 sections
2. **Quality Rubric** — score 5 pieces against the 9-dimension rubric
3. **Weakness Diagnosis** — identify top 3-5 weaknesses ranked by impact
4. **Fix Route Map** — map each weakness to its treatment workflow
5. **30-Day Recovery Calendar** — prioritized weekly actions

### 4. Produce Brand Health Report
Generate the full report per the output template in the workflow.

### 5. Route to Fixes
Offer to immediately deploy the highest-priority fix workflow:
- Trust weak? → "Want me to run `/caleb-brand-build` Phase 2?"
- Content misaligned? → "Want me to run `/caleb-content-sprint` with corrected strategy?"
- Packaging stale? → "Want me to run `/wrapping-paper-library`?"
- No revenue path? → "Want me to run `/caleb-brand-build` Phase 6?"

### 6. Save Output
Save to `deliverables/brand-audit-[name-slug]-[date].md`

### 7. Finalize
```bash
python3 execution/chain_runner.py finalize "360 Brand Audit for [name]" \
    --expert caleb-ralston \
    --skill caleb-ralston-personal-brand \
    --workflow caleb-brand-audit \
    --type Analysis \
    --intent 9 --expert-score 8 --adversarial 8 \
    --notes "[top weaknesses found, fix routes recommended]"
```
