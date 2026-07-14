---
description: "Phase 4 Step 1 engine — reframe each PAIN from the map into a Job-to-be-Done (\"When [situation], I want to [motivation], so I can [desired outcome]\"), then surface 1–2 unconsidered angles per job. Jobs point at outcomes, where positioning and offers live, not just features. Outputs a jobs list mapped to source pains"
---

# /ctm-jobs

Reframe pains into Jobs-to-be-Done. Take the PAINS section of the map and reframe each pain into the deeper progress the customer is trying to make, then propose angles you hadn't considered. People don't want your product; they hire it to make progress — and the outcome is where durable positioning lives.

## Trigger
`/ctm-jobs`

## Workflow
`skills/customer-truth-map/workflows/ctm-jobs.md`

## Quick Use
Provide the saved map's PAINS section (real, source-tagged). Runs prompt P5. The `so I can [outcome]` clause is load-bearing — must name a state, not a feature.

## Pipeline
1 Pull PAINS + run P5 → 2 Write each job in canonical format → 3 Propose 1–2 unconsidered angles per job → 4 Map every job back to its source pain

## Output
A jobs list (each in "When… I want… so I can…" format, outcome-level) + 1–2 angles per job + source-pain mapping + honesty confirmation. Feeds `/ctm-gaps`, then `/ctm-to-offer` / `/ctm-to-content`.

## Stacks With
→ upstream `/ctm-map`, downstream `/ctm-gaps` `/ctm-to-offer` `/ctm-to-content`
→ owns rubric criterion 6 (Job Depth)
