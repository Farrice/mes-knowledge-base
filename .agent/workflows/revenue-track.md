---
description: Track revenue outcomes from deliverables — connect quality scores to money
---

# /revenue-track — Revenue Attribution Pipeline

Connect deliverable quality scores to actual business outcomes. A 7/10 that converts at 3% is more valuable than a 10/10 that converts at 0%.

## Usage

```
/revenue-track                           # Show pipeline (what needs outcome tracking)
/revenue-track log "deliverable" --revenue 500 --outcome "client signed"
/revenue-track report                    # ROI report by skill/expert
/revenue-track report --skill <name>     # Filter by skill
```

## Steps

### 1. Check Pipeline

See which recent deliverables need outcome data:

```bash
python execution/revenue_tracker.py pipeline
```

This scans the Performance Log for entries without revenue attribution.

### 2. Log an Outcome

When a deliverable generates revenue, a lead, or measurable feedback:

```bash
python execution/revenue_tracker.py log "Ken's Fasting Digital Product" \
    --revenue 147 --outcome "3 sales in first week" \
    --expert luke-iha --skill luke-iha-creative-strategy \
    --client ken --type revenue
```

Outcome types: `revenue`, `lead`, `conversion`, `feedback`, `engagement`

### 3. View ROI Report

See which skills and experts actually generate money:

```bash
python execution/revenue_tracker.py report
python execution/revenue_tracker.py report --expert luke-iha
python execution/revenue_tracker.py report --skill storybrand
```

### 4. Use the Data

- **Revenue per quality score**: Does 8/10 correlate to more revenue than 7/10?
- **Top ROI skills**: Which skills should get priority evolution cycles?
- **Dead skills**: High quality, zero revenue = calibration problem
- **Revenue-first routing**: For future work, route to skills with proven revenue track record

## Integration Points

- **Performance Log**: Revenue data enriches existing quality entries in Notion
- **Feedback Ratchet**: Revenue becomes a 4th quality dimension
- **Skill Evolution**: Revenue-generating skills get priority for improvement
- **Gap Report**: Identifies domains with quality but no revenue

## What to Track

| Deliverable Type | Revenue Signal | When to Log |
|-----------------|---------------|-------------|
| Client work | Invoice paid | On payment |
| Digital product | Sales | Weekly |
| Fiverr gig | Gig completed | On completion |
| Pitch/proposal | Deal signed | On signing |
| Content | Leads generated | Weekly |
| LinkedIn posts | DMs/inquiries | Weekly |
