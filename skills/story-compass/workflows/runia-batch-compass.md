---
description: "Process 5-10 ideas at once — rapid compass sentence generation for content calendars and batching"
---

# /runia-batch-compass — The Compass Batch Processor

Rapidly process 5-10 raw ideas through the compass framework. Built for content calendar planning, batch production days, and idea bank curation. Every idea gets tested and either promoted to story-ready or tagged with what's missing.

## Pre-Flight Gate

Load `skills/story-compass/genius.md` — Pattern 1 (Topic-to-Story Binary), Pattern 6 (Compass Sentence), Quick Reference section.

## Input Required

- **5-10 raw ideas**: Topics, concepts, experiences, observations — in any form
- **Content type** (optional): What format these will become (videos, posts, etc.)
- **Time constraint** (optional): Speed mode for fast batching vs. quality mode for deeper work

## Execution

### Step 1: Rapid Story Test (All Ideas)

For each idea, run the quick binary test:

| # | Idea | Want? | Tension? | Change? | Verdict |
|---|------|-------|----------|---------|---------|
| 1 | [idea] | ✓/✗ | ✓/✗ | ✓/✗ | Story / Topic / Needs work |
| 2 | [idea] | ✓/✗ | ✓/✗ | ✓/✗ | Story / Topic / Needs work |
| ... | | | | | |

### Step 2: Tier the Results

**Tier A — Story-Ready** (all three elements present):
Generate compass sentence immediately.

**Tier B — Needs One Dig** (missing tension OR change):
Quick dig — one question per missing element. If found → compass. If not → move to Tier C.

**Tier C — Still a Topic** (missing two+ elements):
Tag what's missing. Park for deeper exploration later, or kill.

### Step 3: Produce Compass Sentences (Tier A + promoted Tier B)

For each story-ready idea, write the compass sentence:

```
IDEA: [original idea]
COMPASS: "I wanted ___, but ___, until ___."
STRENGTH: [1-10]
BEST SUITED FOR: [content type recommendation]
```

### Step 4: Rank by Strength

Order all compass sentences by strength score. Recommend the top 3-5 for immediate production.

## Output Requirements

```
BATCH RESULTS:

TIER A — STORY-READY:
1. [Idea] → "I wanted ___, but ___, until ___." [Strength: X/10]
2. [Idea] → "I wanted ___, but ___, until ___." [Strength: X/10]
...

TIER B — PROMOTED (after quick dig):
3. [Idea] → "I wanted ___, but ___, until ___." [Strength: X/10]
...

TIER C — PARKED:
- [Idea] — Missing: [tension/change/both] — [brief prescription]
...

PRODUCTION RECOMMENDATION:
Top picks for immediate production: #[X], #[Y], #[Z]
Rationale: [why these compass sentences are strongest]
```

## Quality Gate

- [ ] Every idea assessed (no skips)
- [ ] Tier assignments are honest (don't force a topic into a story)
- [ ] Compass sentences are one line each
- [ ] Strength scores are calibrated (don't rate everything 8+)
- [ ] Production recommendations are actionable
