---
description: From talking points through creation through enrichment
---

# /content-orchestrate — Full Content Production Session

Run a complete content production session coordinated by the Kieran Flanagan Content Operations Manager. Chains audience intelligence, content engine, and enrichment skills in the right order with human checkpoints.

## Usage

```
/content-orchestrate [session goal: create | ideate | research | enrich | bundle | full-sprint]
/content-orchestrate ideate --platform LinkedIn --window 28d --state-root [path]
/content-orchestrate full-sprint --platform LinkedIn --pieces 3
/content-orchestrate create --talking-points .tmp/kieran-flanagan/talking-points.md
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-ops/SKILL.md`
2. `skills/kieran-flanagan-content-ops/genius.md`
3. `skills/kieran-flanagan-content-ops/workflows/01-content-orchestrate.md`

### 2. Execute Workflow
Follow the workflow in `01-content-orchestrate.md` using the loaded genius context. This workflow will chain other Kieran Flanagan skills as needed.

### 3. Save Output
Save session output to `.tmp/kieran-flanagan/session-[date]/`.

For Ideate mode, use the supplied persistent state root when present:

```text
[STATE_ROOT]/runs/ideas-[date]-[platform].md
[STATE_ROOT]/queues/content-queue.md
```

Queue state may be created or changed only after explicit human selection.

**Execution prompts**: before producing the deliverable, check `skills/kieran-flanagan-content-ops/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
