# /gw-crit

A complete, deployment-ready CRIT prompt (Context / Role / Interview / Task) built around any real problem, with the interview inversion and delta-seeking task wording baked in.

## Trigger
`/gw-crit`

## Workflow
`skills/geoff-woods-ai-thought-partner/workflows/01-crit.md`

## Quick Use
Provide:
1. The problem or goal, in your own raw words (messy is fine)
2. The stakes — what solving it unlocks
3. The deliverable you want out of the AI
4. Enough domain texture to cast a specific expert role

## Output
A paste-ready CRIT prompt with four labeled blocks (Context dumped verbose, Role cast as a vivid nuanced expert, the verbatim interview-inversion line, a Task that requests the non-obvious delta), a 20% verdict on the target, an optional red-team trailer, and the "bad answer, iterate" handoff.

## Stacks With
→ `/gw-thought-partner` (builds a CRIT with you live, then runs the interview in-conversation)
→ `/gw-feedback-loop` (iterate the first output the CRIT produces)
→ `/gw-20-percent` (run first if you're unsure the target is a real 20%)
→ `/gw-persona-flip` (add the Challenger when iteration plateaus)

**Execution prompts**: before producing the deliverable, check `skills/geoff-woods-ai-thought-partner/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
