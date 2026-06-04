---
description: Strike Team — 2-4 coordinated experts (preset of /convene)
---

# /strike — Focused Expert Strike

A fast, focused council: 3-4 diverse experts, no wide divergent pass, straight to deliberation
and synthesis. A **preset of the Collective Genius Council** (`/convene`).

> Superseded the old JCC stub (2026-06-02). The previous version forwarded to a
> `~/.claude/plugins/installed/jarvis-command-center/` plugin that does not exist. It now
> fronts the reliable Workflow engine.

## Execution
Invoke the **Workflow tool** with:
- `scriptPath`: `.agent/workflows/collective-genius-council.workflow.js`
- `args`: `{ "task": "<the user's mission>", "mode": "strike" }`

Returns: the deliberated synthesis (net-new principle + forks for you + next moves) and a
"How the Masters Thought" learning digest. Holds the grounding floor; $0 incremental.
For more breadth use `/convene --mode wide`; for max breadth `/deploy-council`.
