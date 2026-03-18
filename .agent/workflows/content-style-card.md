---
description: Build a platform-specific style card that defines voice, structure, hooks, and formatting conventions for AI-generated content
---

# /content-style-card — Platform Style Card Builder

Generate a style card that defines how content should sound, look, and flow on a specific platform. This is the "voice DNA" that makes AI content sound genuinely human.

## Usage

```
/content-style-card [platform] [creator name or style reference]
/content-style-card LinkedIn "Farrice Cain"
/content-style-card Newsletter --from-samples [file path to sample posts]
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-audience-intelligence/SKILL.md`
2. `skills/kieran-flanagan-audience-intelligence/genius.md`
3. `skills/kieran-flanagan-audience-intelligence/workflows/02-content-style-card.md`

### 2. Execute Workflow
Follow the workflow in `02-content-style-card.md` using the loaded genius context.

### 3. Save Output
Save the style card to `.tmp/kieran-flanagan/style-card-[platform].md`.
