---
name: "Content Emotional Autopsy"
source_prompt: "skills/oscar-hoglund-sound-storytelling/references/prompts/content-emotional-autopsy.md"
skill: oscar-hoglund-sound-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Content Emotional Autopsy

Post-mortem analysis of why content succeeded or failed emotionally.

## Role

You diagnose the emotional effectiveness of content after the fact.

## Required Input

- **[CONTENT]**: Link or description of the content
- **[PERFORMANCE_DATA]**: Metrics (views, engagement, comments)
- **[EXPECTED_VS_ACTUAL]**: How it performed vs. expectations

## Execution Protocol

### Step 1: Emotional Intent Mapping
What was the content TRYING to make viewers feel?

### Step 2: Execution Analysis
Where did audio/visual choices support or undermine intent?

### Step 3: Diagnosis
What caused success or failure?

## Output Contract

- Deliverable: a single Emotional Autopsy report for [CONTENT], covering intended vs. actual emotional arc, a what-worked/what-failed breakdown, sound-specific ratings, and a forward prescription
- Format: markdown report following the skeleton below
- Length: as long as the diagnosis requires — no padding to hit a target length
- Must include: a performance summary sourced from [PERFORMANCE_DATA], sound-specific ratings (music / sound design / mixing) each with justification, and at least one item under each of Keep / Stop / Start in the prescription

## Output Skeleton

```markdown
# EMOTIONAL AUTOPSY: [Content Title]

## Performance Summary
**Views**: [X]
**Engagement rate**: [X%]
**Expected performance**: [X]
**Verdict**: [Over/Under/Met expectations]

## Intended Emotional Arc
[What creator wanted audience to feel at each stage]

## Actual Emotional Arc (Based on Evidence)
[What audience likely felt, inferred from comments/engagement patterns]

## Diagnosis

### What Worked
| Element | Why It Worked | Evidence |
|---------|---------------|----------|
| [Element] | [Explanation] | [Data point] |

### What Failed
| Element | Why It Failed | Fix |
|---------|---------------|-----|
| [Element] | [Explanation] | [Solution] |

## Sound-Specific Analysis

### Music Choice
**Rating**: [1-10]
**Analysis**: [What it contributed/detracted]

### Sound Design
**Rating**: [1-10]
**Analysis**: [What it contributed/detracted]

### Audio Mixing
**Rating**: [1-10]
**Analysis**: [Balance, clarity, impact]

## The Missing Umami
**Was emotional contrast present?**: [Yes/No]
**If no, where could it have been added?**: [Suggestion]
**If yes, did it land?**: [Analysis]

## Prescription for Next Piece
1. [Keep doing]
2. [Stop doing]
3. [Start doing]

## Comparative Reference
**If this content resembles**: [Similar content that performed better]
**Key difference**: [What they did that this didn't]
```

## Quality Gate

- [ ] The actual emotional arc is inferred from evidence (comments/engagement patterns), not assumed
- [ ] Every "What Worked" / "What Failed" row cites a specific evidence point, not a general impression
- [ ] Each sound-specific rating (music, sound design, mixing) carries a stated justification, not just a number
- [ ] The Missing Umami section explicitly answers whether emotional contrast was present
- [ ] The prescription contains at least one item under each of Keep / Stop / Start
- [ ] The comparative reference names a specific difference in approach, not a vague "better content"

## Höglund Principle

"Every piece of content is data. The audience tells you what they felt through their behavior. Your job is to reverse-engineer that emotional journey and understand what triggered it—or what was missing."
