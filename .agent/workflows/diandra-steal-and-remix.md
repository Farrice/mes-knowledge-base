---
description: Content sourcing flywheel
---

# `/diandra-steal-and-remix` — The Content Sourcing Flywheel

Finds viral LinkedIn posts in your niche → extracts the structural mechanic that made them work → produces 3 original remixes in your voice using Diandra's body-first method.

**This is NOT copying. This is studying mechanics — like an architect studying load-bearing principles, not stealing blueprints.**

## When to Use
- You don't know what to write about and need inspiration grounded in REAL performance data
- You want to study what formats/structures are winning on LinkedIn right now
- You want to build a library of proven mechanics you can deploy anytime
- You want to shortcut content-market fit by learning from what's already working

## Usage

```
/diandra-steal-and-remix [niche or topic]
/diandra-steal-and-remix "B2B SaaS marketing"
/diandra-steal-and-remix --url [specific viral post URL to study]
/diandra-steal-and-remix --library   (browse previously saved mechanics)
```

---

## Phase 1: Outlier Discovery

**Actor**: Orchestrator + research tools

### If niche/topic provided:

1. Run 3 parallel `search_web` queries:
   - `"[niche] viral LinkedIn post 2026 high engagement"`
   - `"site:linkedin.com [niche] thought leader post"`
   - `"[niche] best LinkedIn posts examples engagement"`

2. Use `read_url_content` on top 5-8 results to extract post content

3. Present 5-7 outlier candidates:

```markdown
## Outlier Posts Found: [Niche]

| # | Creator | Hook (first 2 lines) | Est. Engagement | Format | Why It Worked |
|---|---------|---------------------|-----------------|--------|---------------|
| 1 | [name] | [hook preview] | [likes/comments] | Text | [1-line] |
| 2 | [name] | [hook preview] | [likes/comments] | Carousel | [1-line] |
| ... |

**Pick 1-3 posts to study. Reply with numbers.**
```

### If `--url` provided:

1. Use `read_url_content` to extract the full post
2. Save to `.tmp/diandra-steal-and-remix/source.md`
3. Skip to Phase 2

**WAIT FOR USER SELECTION.**

---

## Phase 2: Pattern Extraction (3 Parallel Sub-Agents)

**Actor**: 3 parallel sub-agents via Task tool

For each selected post, spawn 3 analysts **in a single message**:

### Sub-Agent 1: Hook Analyst
```
You are a content strategist analyzing a viral LinkedIn post.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
   — Focus on Pattern 1 (Attention Redirection), Pattern 6 (Body-First Writing)

## SOURCE CONTENT
[Full text of the viral post]

## YOUR ANALYSIS
Focus ONLY on the hook — the first 1-3 lines:

1. **Hook type**: Entity name / Bold claim / Story open / Contrarian / Data shock / Question / Pattern interrupt
2. **Hook template**: Write the structural pattern with blanks (e.g., "[Brand] just [action]. Here's what everyone is missing:")
3. **Diandra pattern match**: Is this a brandjack, newsjack, namejack, hot take, or pure content?
4. **"See more" optimization**: Does the hook work in LinkedIn's truncated preview? What makes someone tap?
5. **Specificity level**: How specific is the hook? (Generic = bad. Name + number + claim = good.)

Write to: .tmp/diandra-steal-and-remix/analysis-hook.md
```

### Sub-Agent 2: Framework Analyst
```
You are a content architect analyzing a viral LinkedIn post.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
   — Focus on Pattern 5 (4-Bucket Funnel), Pattern 7 (Steal Protocol)

## SOURCE CONTENT
[Full text of the viral post]

## YOUR ANALYSIS
Focus ONLY on the structure:

1. **Bucket classification**: Growth / Authority / Conversion / Personal — which bucket is this post serving?
2. **Skeleton with blanks**: Write the numbered/sequenced framework as a template:
   Line 1: [Hook type: ___]
   Lines 2-3: [Setup: ___]
   Lines 4-8: [Value delivery pattern: ___]
   Final lines: [CTA type: ___]
3. **Body-first evidence**: Was this likely written body-first? (Check if hook is extracted from body content)
4. **Pacing**: Short punchy lines? Long narrative? Alternating? Where does it accelerate/decelerate?
5. **White space strategy**: How is formatting used for readability on mobile?

Write to: .tmp/diandra-steal-and-remix/analysis-framework.md
```

### Sub-Agent 3: Engagement Analyst
```
You are a viral content analyst studying WHY this post performed.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
   — Focus on Pattern 2 (Boomerang Effect), Pattern 9 (Engagement as Distribution)

## SOURCE CONTENT
[Full text of the viral post]

## YOUR ANALYSIS
Focus ONLY on engagement mechanics:

1. **Primary emotion**: What emotion fires first? Curiosity / Recognition / Outrage / Aspiration / Validation / FOMO
2. **Comment triggers**: What specific elements invite comments? Open questions? Controversial claims? Lists?
3. **Share triggers**: Why would someone reshare? Identity signal / Useful / Controversial / Status / Saving for later
4. **Boomerang potential**: If an entity is referenced, did the boomerang effect likely activate?
5. **Audience tribe**: Which specific professional identity does this post activate?
6. **CTA effectiveness**: How does it drive action? Does the CTA match the bucket?

Write to: .tmp/diandra-steal-and-remix/analysis-engagement.md
```

---

## Phase 3: Mechanic Blueprint Synthesis

**Actor**: Orchestrator
**Prerequisite**: All 3 analyses received

Read all 3 analysis files and produce the unified mechanic blueprint:

```markdown
## Mechanic Blueprint: [Post Description]

**Source**: [URL or creator name]
**Platform**: LinkedIn
**Estimated Performance**: [likes, comments if visible]
**Bucket**: [Growth / Authority / Conversion / Personal]

### The Hook
- **Type**: [from hook analyst]
- **Template**: "[pattern with blanks]"
- **Diandra Match**: [brandjack / newsjack / namejack / hot take / pure content]

### The Framework
- **Pattern**: [from framework analyst]
- **Skeleton**:
  Line 1: [Hook template]
  Lines 2-3: [Setup template]
  Lines 4-8: [Value template]
  Final: [CTA template]
- **Pacing**: [description]

### The Engagement Engine
- **Primary emotion**: [from engagement analyst]
- **Comment driver**: [what invites responses]
- **Share trigger**: [why people spread it]
- **Boomerang**: [if applicable]

### Remix Instructions
- **KEEP** (the mechanic): [hook structure, framework pattern, pacing, CTA style]
- **REPLACE** (the content): [their topic, examples, voice, entity, data]
- **ADAPT** (for your brand): [apply your expertise, your ICP's pain, your voice]
```

Save to `.tmp/diandra-steal-and-remix/mechanic-blueprint.md`.

**Present to user.** This alone is valuable as a reusable template.

> [!IMPORTANT]
> **APPROVAL CHECKPOINT.** Ask: "This is the mechanic we'll remix. Want to proceed with 3 original remixes, or adjust the blueprint first?"

---

## Phase 4: Remix Sprint (3 Parallel Sub-Agents)

**Actor**: 3 parallel sub-agents via Task tool

Spawn 3 remixes **in a single message**, each using a different approach:

### Sub-Agent 1: Same Mechanic, Your Topic
```
You are Diandra Escobar's Writing Engine.

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
2. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/workflows/09-linkedin-writing-engine.md

## MECHANIC BLUEPRINT
[Full blueprint from Phase 3]

## CONTEXT
Read /Users/farricecain/Google Antigravity/FARRICE.md for voice and positioning.

## YOUR TASK
Create a remix using the SAME structural mechanic but about a topic from Farrice's world:
1. Pick the topic from Farrice's interests that BEST fits this mechanic
2. Write the BODY FIRST — follow Diandra's body-first method exactly
3. Follow the skeleton template from the blueprint
4. Mine the body for the hook
5. Use Farrice's voice — anti-guru, systems AND soul, training arc metaphors
6. Match CTA to the same bucket as the original

Write to: .tmp/diandra-steal-and-remix/remix-1-same-mechanic.md
```

### Sub-Agent 2: Same Mechanic, Different Angle
```
[Same skill acquisition + blueprint + context]

## YOUR TASK
Create a remix using the SAME structural mechanic but approaching from a CONTRARIAN angle:
- If the original was tactical → go philosophical
- If the original was data-driven → go story-driven
- If the original was serious → find the humor or vulnerability
- If the original praised an entity → find the critique

The SKELETON stays the same. The CONTENT flips the perspective.
Apply Farrice's voice and expertise.

Write to: .tmp/diandra-steal-and-remix/remix-2-different-angle.md
```

### Sub-Agent 3: Same Mechanic, Different Jack Type
```
[Same skill acquisition + blueprint + context]

## YOUR TASK
Create a remix using the SAME structural mechanic but a DIFFERENT jack type:
- If the original was a brandjack → make it a hot take
- If the original was a namejack → make it a brandjack
- If the original was pure content → make it a newsjack

The SKELETON stays the same. The ENTITY TYPE changes.
Research a real entity that fits (use search_web if needed).
Apply Farrice's voice and expertise.

Write to: .tmp/diandra-steal-and-remix/remix-3-different-jack.md
```

---

## Phase 5: Content Bank Deposit

**Actor**: Orchestrator

### Save the mechanic to the library:

Check if `.tmp/mechanic-library/` exists. If not, create it.

Append to `.tmp/mechanic-library/index.md`:

```markdown
## [Date] — [Mechanic Name]
- **Source**: [creator/URL]
- **Blueprint**: [link to blueprint file]
- **Hook Template**: "[template with blanks]"
- **Skeleton**: [1-line summary]
- **Best For**: [bucket type]
- **Times Used**: 0
```

Copy the blueprint to `.tmp/mechanic-library/[slug]-blueprint.md`.

---

## Phase 6: Quality Gate + Deliver

### Quality Checks:

| Criterion | Check |
|-----------|-------|
| Originality | Is each remix genuinely original content? (Same structure ≠ same content) |
| Body-First | Were all remixes written body-first? |
| Voice Fidelity | Does each remix sound like the creator, not the source? |
| Mechanic Integrity | Does the structural skeleton match the blueprint? |
| Specificity | ≥2 specific details per remix (not vague generalizations)? |
| Anti-Copy | Would source creator recognize their structure? Yes = good. Their content? No = good. |

### Deliver

```markdown
# 🔍 STEAL & REMIX: [Source Description]

**Source**: [creator/URL]
**Date**: [date]

---

## MECHANIC BLUEPRINT (Reusable)
[Full blueprint — the structural template you can use anytime]

---

## REMIX 1: Same Mechanic, Your Topic
**Topic**: [topic]
[Full post — hook + body + CTA]

---

## REMIX 2: Contrarian Angle
**Angle**: [flip description]
[Full post — hook + body + CTA]

---

## REMIX 3: Different Jack Type
**Jack Type**: [new type]
[Full post — hook + body + CTA]

---

## MECHANIC LIBRARY
Blueprint saved to mechanic library. Run `/diandra-steal-and-remix --library` to browse.

## PROVENANCE
- Source studied: [URL/creator]
- Skills: Diandra Escobar genius.md + workflows 09, 12
- Remixes: 3 original pieces | Mechanic: 1 reusable blueprint
```

Save to `.tmp/diandra-steal-and-remix/remix-[slug]-[date].md`.

---

## Output Files

```
.tmp/diandra-steal-and-remix/
  source.md
  analysis-hook.md
  analysis-framework.md
  analysis-engagement.md
  mechanic-blueprint.md
  remix-1-same-mechanic.md
  remix-2-different-angle.md
  remix-3-different-jack.md
  remix-[slug]-[date].md   (assembled final package)

.tmp/mechanic-library/
  index.md
  [slug]-blueprint.md
```

**Execution prompts**: before producing the deliverable, check `skills/diandra-escobar-linkedin-growth/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
