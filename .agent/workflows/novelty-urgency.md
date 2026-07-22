# /novelty-urgency

Step 3 — add honest time-compression when a real window exists, and strip fake urgency when it doesn't.

## Trigger
`/novelty-urgency`

## Workflow
`skills/kallaway-illusion-of-novelty/workflows/novelty-urgency.md`

## Quick Use
Provide:
1. The topic / reveal
2. Anything that just happened or is about to stop happening (optional)
3. A draft to scan for fake urgency (optional)

## Output
Honest-window audit → urgency lines if real, or an explicit SKIP recommendation; plus a fake-urgency detector pass flagging bolted-on deadlines.

## Stacks With
→ `/novelty-forge` (urgency is step 3 of the full build)

**Execution prompts**: before producing the deliverable, check `skills/kallaway-illusion-of-novelty/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
