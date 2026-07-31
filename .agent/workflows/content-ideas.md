---
description: Generate evidence-backed idea cards from audience, owned winners, and fresh signals
---

# /content-ideas: Content Signal Ideation

Produce Proven, Trending, and Convergence idea cards. Stop for human selection before queue mutation or content creation.

## Usage

```text
/content-ideas --platform LinkedIn --window 28d --state-root [path]
```

## Steps

### 1. Load Skills

Read:

1. `skills/kieran-flanagan-content-engine/SKILL.md`
2. `skills/kieran-flanagan-content-engine/genius.md`
3. `skills/kieran-flanagan-content-engine/workflows/09-content-signal-ideation.md`
4. `skills/kieran-flanagan-content-engine/references/prompts-v2/content-signal-ideation.md`

### 2. Load Assets

Resolve the audience profile, requested platform's Winning Content Profile, optional talking points, and current queue/tombstones from the supplied state root.

### 3. Execute Workflow

Run the bounded trend scan and produce idea cards. Every card must name a platform, audience truth, evidence status, creator bridge, and confidence.

### 4. Save Output

Save to `[STATE_ROOT]/runs/ideas-[date]-[platform].md`.

Do not add ideas to the queue and do not draft finished content.
