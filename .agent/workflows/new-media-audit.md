---
description: Scored audit + structural rebuild plan
---

# /new-media-audit — New Media Strategy Audit

Diagnose whether an organization, brand, or founder is operating on old-media or new-media physics. Produces a scored audit covering OODA loop speed, oral/written culture mapping, Joe Rogan CEO test, and structural rebuild prescription.

**When to use**: Growth has stalled despite "doing social media." A competitor is winning narrative control. Communication feels corporate, safe, and forgettable. You suspect old-media instincts are holding you back.

## Usage

```
/new-media-audit [organization/brand/person]
/new-media-audit "My SaaS company" --industry "fintech" --competitors "Competitor A, Competitor B"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/andreessen-horowitz-new-media/SKILL.md`
2. `skills/andreessen-horowitz-new-media/genius.md`
3. `skills/andreessen-horowitz-new-media/workflows/01-new-media-audit.md`

### 2. Gather Context
From user input, determine:
- The organization/brand/person being audited
- Current communication channels and practices (ask if not provided)
- Industry and competitive landscape
- Any recent crises or missed narrative opportunities

### 3. Execute Workflow
Follow every step in `01-new-media-audit.md`:
- Step 1: Old/New Media Classification (score every practice)
- Step 2: OODA Loop Speed Measurement (measure in hours)
- Step 3: Oral/Written Culture Map (classify every platform)
- Step 4: Joe Rogan CEO Test (score 1-10 with diagnosis)
- Step 5: Structural Rebuild Prescription

### 4. Optional: Deep Research Layer
If Perplexity budget allows (check `.agent/perplexity-usage.json`):

**Query**: "How are the top-performing brands in [industry] using new media channels? Which founder/CEO personal brands are winning audience attention? Include specific channel strategies and content types."

Integrate findings into the competitive OODA loop benchmark.

### 5. Save Output
Save to `research_outputs/[date]-new-media-audit-[org-slug].md`

## Output Structure

```
# New Media Strategy Audit: [Organization]

## Executive Diagnosis (1-sentence verdict)
## Old/New Media Score: [X] (Old/New/Dangerous Hybrid)
## Practice-by-Practice Classification Table
## OODA Loop Speed: [X hours]
## Oral/Written Culture Map
## Joe Rogan CEO Score: [X/10]
## Structural Rebuild Plan (Week 1 → 7-Day Sprint → 30-Day)
## Prioritized Fix List (by impact/effort)
```

**Execution prompts**: before producing the deliverable, check `skills/andreessen-horowitz-new-media/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
