---
description: "Phase 5 copy — turn an existing Customer Truth Map into 10 slot-assigned proven quotes plus 8 customer-register headlines, then hand off to a real copy engine for the finished long-form"
---

# /ctm-to-copy

Put the map to work: copy. Mine a finished map for raw copy that's already proven because a real person said it — pull the 10 most powerful quotes, assign each a slot, write 8 headlines in the customer's own register, then hand off. The job is selection and assignment, not composition.

## Trigger
`/ctm-to-copy`

## Workflow
`skills/customer-truth-map/workflows/ctm-to-copy.md`

## Quick Use
Provide a finished map + the named page/campaign (sales page / landing / email / ad). Runs prompt P7. Every emitted line traces to a specific map quote; nothing invented to fill a slot.

## Pipeline
1 Pull the 10 + assign slots (headline/subhead/objection-handler/proof point) → 2 Write 8 headlines from FEEL + PAINS only → 3 Hand off (do not finish here)

## Output
The slot table (10 harvested quotes, slot + reason + source tag) + 8 traced headlines + the explicit handoff line. Does NOT produce the finished long-form.

## Stacks With
→ finishing engines: `/copy-engine` (converting page), `/ghostwrite` (founder voice), master-copywriter (agency-grade asset)
→ upstream `/ctm-map`, `/ctm-gaps` (widest gap = the headline) · fact-verifier for claims
