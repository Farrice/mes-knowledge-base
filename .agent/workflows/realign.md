---
description: Alias to /resume realign mode; load a prior thread as background for new adjacent work
---

# /realign - Resume Context As Background

`/realign` is a thin workflow alias for the realign mode documented in
`.agent/workflows/resume.md`.

Use it when Farrice wants a past thread loaded as context for new work, not when
he wants to continue the old plan.

## Execution

1. Read `.agent/workflows/resume.md`.
2. Follow its `/realign mode` section.
3. Resolve the requested thread through `execution/handoff_store.py`.
4. Present the loaded facts, constraints, assets, and changed context as
   background only.
5. Ask for the new direction if the adjacent task is not already clear.

## Boundary

Do not anchor the new session to the old priority order. `/realign` imports
context, not obligation.
