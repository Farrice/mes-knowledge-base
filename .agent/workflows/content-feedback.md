---
description: Analyze published content performance and propose specific improvements
---

# /content-feedback — Content Performance Feedback Loop

Ingest content performance data and analyze it against the content that was created. Identifies winning and losing patterns, then proposes specific updates to system assets (profiles, style cards, talking points).

## Usage

```
/content-feedback [path to content + performance data]
/content-feedback --platform LinkedIn --period "last 30 days"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-ops/SKILL.md`
2. `skills/kieran-flanagan-content-ops/genius.md`
3. `skills/kieran-flanagan-content-ops/workflows/02-content-feedback.md`

### 2. Execute Workflow
Follow the workflow in `02-content-feedback.md` using the loaded genius context.

### 3. Save Output
Save performance report to `.tmp/kieran-flanagan/feedback-report-[date].md`.
