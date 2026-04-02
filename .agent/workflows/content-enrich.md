---
description: Enrich any content draft
---

# /content-enrich — Content Enrichment Engine

Take a draft and layer in data, statistics, expert quotes, and real-world stories that elevate its authority. Transforms surface-level content into substantive posts that demonstrate expertise.

## Usage

```
/content-enrich [path to draft or paste content]
/content-enrich .tmp/atomize/linkedin-1-thesis.md --type data+stories
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-engine/SKILL.md`
2. `skills/kieran-flanagan-content-engine/genius.md`
3. `skills/kieran-flanagan-content-engine/workflows/03-content-enrich.md`

### 2. Execute Workflow
Follow the workflow in `03-content-enrich.md` using the loaded genius context.

### 3. Save Output
Save enriched content to `.tmp/kieran-flanagan/enriched-[original-name].md`.
