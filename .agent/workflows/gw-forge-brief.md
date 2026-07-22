# /gw-forge-brief

A forge-ready build brief extracted from raw intent — dominoes gate first ("agentic is the 18th domino"), then a CRIT interview captures the tacit process, ending in a markdown spec with the recommended forge-os lane.

## Trigger
`/gw-forge-brief`

## Workflow
`skills/geoff-woods-ai-thought-partner/workflows/11-forge-brief.md`

## Quick Use
Provide:
1. The raw intent — "I want to build a thing that..." in your own messy words
2. The trigger — what live frustration or repeated task surfaced this
3. Frequency + value — how often it happens, what it's worth when it goes right
4. What already exists — current process, data, docs, tools

## Output
Dominoes verdict (BUILD-WORTHY / PREMATURE / NOT-A-BUILD) → CRIT interview capturing the tacit process → extracted spec → recommended lane (prompt / workflow / skill / agent / plugin) → the forge-ready markdown build brief → the one open question for your judgment.

## Stacks With
→ `/forge` (hand the brief straight in: `/forge <lane> <brief>` — this workflow feeds forge-os, it does not build)
→ `/gw-crit` (the Context-Role-Interview-Task engine this runs on)
→ `/extract-forge` (when source material exists to ground a skill, not a bare-concept build)
→ `/create-agent` (downstream, once a BUILD-WORTHY agent brief clears and data is centralized)

**Execution prompts**: before producing the deliverable, check `skills/geoff-woods-ai-thought-partner/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
