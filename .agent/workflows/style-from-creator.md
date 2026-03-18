---
description: Clone any creator's content style by analyzing their published work — reverse-engineer voice, structure, and patterns into a style card
---

# /style-from-creator — Creator Voice Cloner

Analyze a creator's published content to extract their style DNA. Produces a style card that can be used by the content engine to write in their voice.

## Usage

```
/style-from-creator [creator name] [links or file paths to their content]
/style-from-creator "Alex Hormozi" --platform LinkedIn
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-audience-intelligence/SKILL.md`
2. `skills/kieran-flanagan-audience-intelligence/genius.md`
3. `skills/kieran-flanagan-audience-intelligence/workflows/03-style-from-creator.md`

### 2. Execute Workflow
Follow the workflow in `03-style-from-creator.md` using the loaded genius context.

### 3. Save Output
Save the derived style card to `.tmp/kieran-flanagan/style-card-[creator].md`.
