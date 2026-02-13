---
description: Validate MES 3.0 extraction outputs using mechanical rubric + Oren CEV taste check
---

# MES 3.0 Extraction Validation

Opt-in quality gate for extraction outputs. Combines mechanical checks with taste judgment. Run after extraction is complete, before conversion to skill.

## When to Use

- After any Standard or Deep tier extraction
- Light tier: skip unless output feels questionable
- When converting a backlog of older extractions

---

## Validation Process

### Check 1: Practitioner Mode (Mechanical)

For each crown jewel prompt, verify:

| Criterion | Pass | Fail |
|-----------|------|------|
| Prompt executes methodology | Produces deliverable directly | Explains how to do something |
| Example output is an actual deliverable | Contains the finished work product | Describes what the output would look like |
| Prompt is self-contained | Deployable without reading the extraction | Requires context from other documents |
| Input requirements are specific | User knows exactly what to provide | Vague or missing inputs |
| Output specification is exact | User knows exactly what they'll get | Generic "analysis" or "insights" |

**If any prompt fails**: Rewrite it. Don't flag — fix.

### Check 2: Extraction Completeness (Mechanical)

| Component | Required (Standard/Deep) | Required (Light) |
|-----------|-------------------------|-------------------|
| Content Assessment | ✅ | ✅ |
| Executive Summary | ✅ | Optional |
| Genius Patterns (with all 4 fields each) | ✅ | ✅ (fewer patterns OK) |
| Hidden Knowledge | ✅ | Optional |
| Methodology | ✅ | ❌ |
| Implementation Pathway | ✅ | ❌ |
| Crown Jewel Prompts (min 3) | ✅ | ✅ (min 1) |
| ESO / AGENT.md | Deep only | ❌ |

### Check 3: Oren CEV Taste Check

Deploy Oren's CEV Critique Matrix against the extraction as a whole. Read `skills/oren-taste-development/references/prompts/cev-critique-matrix.md` and execute with:

**Input:**
- **Item**: The complete extraction report + crown jewel prompts
- **Context**: "MES 3.0 extraction intended for deployment as an Antigravity skill"
- **Depth**: Standard

**Evaluate across CEV:**

**Composition**
- Is the extraction well-structured and internally consistent?
- Do the genius patterns feel distinctly identified (not overlapping or redundant)?
- Are the prompts architecturally sound?

**Effectivity**
- Would a practitioner deploying these prompts get genuinely useful outputs?
- Does the extraction capture what makes this expert *specifically* different?
- Is anything important missing or underserved?

**Vibes**
- Does the extraction feel alive or formulaic?
- Do the prompts produce work that feels like it came from the expert, or like it came from a template?
- Is the creative latitude actually leveraged, or just stated?

**CEV Verdict:** Pass / Needs Work / Fail

### Check 4: Deduplication

Before converting to a skill:

1. List all existing Antigravity skills in the same domain
2. For each overlap identified, answer: **Does this new extraction add distinct value?**
   - If yes → proceed, note the compound/stacking opportunities
   - If no → flag for Farrice's decision (merge into existing skill vs. standalone)

---

## Validation Output

```markdown
## Extraction Validation Report

**Source**: [Expert — Material]
**Tier**: [Light / Standard / Deep]

### Practitioner Mode: [PASS / FIXED]
[Any prompts that were rewritten, with brief note on what was wrong]

### Completeness: [PASS / GAPS]
[Any missing components]

### CEV Taste: [PASS / NEEDS WORK / FAIL]
- Composition: [Score 1-10] — [one line why]
- Effectivity: [Score 1-10] — [one line why]
- Vibes: [Score 1-10] — [one line why]
[Specific recommendations if not passing]

### Deduplication: [CLEAR / OVERLAP DETECTED]
[Overlapping skills and recommendation]

### Overall: [READY FOR DEPLOYMENT / NEEDS REVISION / FLAG FOR REVIEW]
```

---

## Decision Tree

```
Extraction complete
    │
    ├── All checks pass? → Convert to skill
    │
    ├── Practitioner mode fails? → Auto-fix, re-validate
    │
    ├── CEV < 6 on any dimension? → Revise extraction
    │
    └── Dedup overlap? → Flag for Farrice
```
