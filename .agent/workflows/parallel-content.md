---
description: Generate 3-5 content pieces in parallel using different experts — LinkedIn posts, tweets, scripts, emails produced simultaneously
---

# /parallel-content — Parallel Content Sprint

Generate multiple content pieces simultaneously, each written by the most appropriate expert agent. All pieces share a common theme/topic but are independent deliverables.

## Usage

```
/parallel-content [topic or theme]
/parallel-content --formats "linkedin, twitter thread, email, tiktok script" [topic]
```

## When to Use

- Content day: batch-produce a week's worth of content
- Launch sequence: need multiple assets (email + social + video script) fast
- Repurposing: one idea expressed across multiple formats

## Steps

### 1. Define the Content Brief

From the user's topic, determine:
- **Core message**: The single idea all content pieces share
- **Formats needed**: Default to LinkedIn post + Twitter thread + email + short-form video script
- **Expert assignment**: Route each format to the best agent

Default expert routing:

| Format | Expert | Domain | Why |
|--------|--------|--------|-----|
| LinkedIn post | Lara Acosta | Personal Brand | LinkedIn mastery |
| Twitter/X thread | Shaan Puri | Content & Viral | Storytelling hooks |
| Email sequence | Cardinal Mason | Copywriting | Conversion copy |
| TikTok/Reel script | Seena Rez | Video & Media | Short-form virality |
| Blog/article | Nicolas Cole | Writing | Digital writing systems |

Present:
```
## Content Sprint Plan

**Theme**: [topic]
**Core message**: [1-line]

| # | Format | Expert | Deliverable |
|---|--------|--------|-------------|
| 1 | LinkedIn post | Lara Acosta | 1 post, hook + CTA |
| 2 | Twitter thread | Shaan Puri | 5-7 tweet thread |
| 3 | Email | Cardinal Mason | 1 conversion email |
| 4 | TikTok script | Seena Rez | 30-60s script |

Launch all [N] in parallel? Or adjust?
```

Wait for user approval.

### 2. Launch Parallel Content Agents

Spawn one Task tool sub-agent per content piece **in a single message**:

Each agent prompt:
```
You are [Expert Name], writing a [format] about: [topic]

**Core message**: [message]
**Target audience**: [audience from user context or FARRICE.md]

**Instructions**:
1. Read the expert's skill: skills/[skill-name]/SKILL.md
2. Read the expert's genius patterns: skills/[skill-name]/genius.md
3. Read the relevant workflow for this format
4. Apply the expert's methodology to produce the content
5. Write output to: .tmp/content-sprint/[format-slug].md

**Quality gate**: Would [Expert Name] be proud of this? Does it pass their quality test?
```

### 3. Collect and Polish

After all agents return:
- Read each content piece from `.tmp/content-sprint/`
- Light editing pass for voice consistency (all pieces should sound like Farrice, informed by expert methodology)
- Present all pieces in a unified view:

```markdown
# Content Sprint: [Topic]

**Date**: [date]
**Pieces generated**: [N]

---

## 1. LinkedIn Post (via Lara Acosta)

[Full post content]

---

## 2. Twitter Thread (via Shaan Puri)

[Full thread content]

---

## 3. Email (via Cardinal Mason)

[Full email content]

---

## 4. TikTok Script (via Seena Rez)

[Full script content]

---
```

### 4. Deliver

Save the complete sprint to `.tmp/content-sprint/sprint-[date].md`.

Offer next steps:
- Edit any piece individually
- Post directly (if social media plugins available)
- Generate more formats from the same theme
- Package as a deliverable

## Limits

- **Max 5 parallel content pieces** (quality degrades with more)
- Each sub-agent reads the expert's skill files fresh (clean context)
- Content is generated independently — no cross-referencing between pieces
