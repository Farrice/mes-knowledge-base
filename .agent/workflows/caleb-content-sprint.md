---
description: Weekly content production engine
---

# /caleb-content-sprint — Weekly Content Production Engine

One command → one week of platform-native, quality-gated content. Run this weekly once your brand is built.

## Usage

```
/caleb-content-sprint --week "[date range]"
/caleb-content-sprint   # (defaults to current week)
```

## Steps

### 1. Load Skills
// turbo
Read these files:
1. `skills/caleb-ralston-personal-brand/genius.md`
2. `skills/caleb-ralston-personal-brand/workflows/caleb-content-sprint.md`

### 2. Pre-Sprint Check
Confirm the user has these in place (if not, route to `/caleb-brand-build`):
- Customer Pain Map
- Platform Strategy
- Format Niche
- Wrapping Paper Library
- Brand Foundation

### 3. Execute Sprint
Follow the 6-step sprint workflow:
1. **Mine wrapping paper** — pull 2-3 fresh formats from library + quick scroll
2. **Map customer pain** — select this week's content concepts (5-7 pieces)
3. **Draft content** — write platform-native pieces with 4C intros
4. **Accordion test** — create short-form versions for untested concepts
5. **Quality gate** — score every piece against all 9 quality tests
6. **Distribution map** — assign pieces to platforms with timing

### 4. Produce Output
Generate the Content Sprint output per the template in the workflow:
- Wrapping paper used
- Content pieces with drafts
- Distribution calendar
- Metrics to watch

### 5. Save Output
Save to `deliverables/content-sprint-[date].md`

### 6. Finalize
```bash
python3 execution/chain_runner.py finalize "Content Sprint for week of [date]" \
    --expert caleb-ralston \
    --skill caleb-ralston-personal-brand \
    --workflow caleb-content-sprint \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 8 \
    --notes "[concepts tested, wrapping paper innovations]"
```
