---
description: "Phase 1 (Steps 1–2) of the Customer Truth Map — narrow the customer, name 15–20 problems in their own voice tagged assumed vs evidenced, pick the 2–3 to research deeply, and build a sourced list of where they talk with candor scores and a capture tool per source"
---

# /ctm-scope

Narrow the target and map the sources. Before a single quote is gathered, decide WHO the map is for (narrow enough to be useful), WHICH problems are worth the dig, and WHERE the customer actually talks unprompted. Produces the brief `/ctm-gather` executes against.

## Trigger
`/ctm-scope`

## Workflow
`skills/customer-truth-map/workflows/ctm-scope.md`

## Quick Use
Provide the customer + problem. Grounds first (memory_facade + Recall) so you build on what's already held; runs prompts P1 (name the problems) and P2 (find where they talk).

## Pipeline
Step 0 Ground (free, required) → Step 1 Narrow + list 15–20 problems (`[assumed]`/`[evidenced]`), pick 2–3 → Step 2 Map specific sources with candor 1–5, unprompted/prompted flag, capture tool

## Output
Grounding receipt + narrowed one-sentence customer definition + the tagged problem list (2–3 flagged for deep research) + the source table (URL/handle, candor, type, capture tool; own-data weighted). The input brief to `/ctm-gather`.

## Stacks With
→ hands off to `/ctm-gather` (executes the source list)
→ `tool-wiring.md` Layer 0/1 for the source-tool mapping
