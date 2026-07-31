---
description: Build a platform-specific profile from the creator's owned content evidence
---

# /content-winning-profile: Platform Winning Content Profile

Build or refresh a versioned profile of transferable patterns from one creator's owned content on one platform.

## Usage

```text
/content-winning-profile --creator "Farrice Cain" --platform LinkedIn --state-root [path]
```

## Steps

### 1. Load Skills

Read:

1. `skills/kieran-flanagan-audience-intelligence/SKILL.md`
2. `skills/kieran-flanagan-audience-intelligence/genius.md`
3. `skills/kieran-flanagan-audience-intelligence/workflows/05-winning-content-profile.md`
4. `skills/kieran-flanagan-audience-intelligence/references/prompts-v2/winning-content-profile.md`

### 2. Execute Workflow

Follow the workflow and born-v2 prompt exactly. Preserve performance, human-verdict, and unscored evidence as separate classes.

### 3. Save Output

Save to `[STATE_ROOT]/profiles/winning-content-[platform].md`.

Demo fallback: `.tmp/kieran-flanagan/[creator-slug]/profiles/winning-content-[platform].md`.

Never invent performance data or merge platforms.
