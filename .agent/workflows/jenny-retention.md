# /jenny-retention

Retention triage report for an underperforming short — hook vs. body vs. progression failure, with specific timestamped fixes.

## Trigger
`/jenny-retention`

## Workflow
`skills/jenny-hoyos-shorts/workflows/03-diagnose-retention.md`

## Quick Use
Provide:
1. The video (script, transcript, or beat-by-beat with rough timestamps)
2. Viewed-vs-swiped % (from YouTube Studio; approximate is fine)
3. Retention data — average % and graph shape (slope / cliffs / early exodus)
4. Video length in seconds

## Output
Hook verdict, graph signature (A. early exodus / B. point drops / C. slow slope), cause table, timestamped fix list, and a relaunch call (fix-format vs. kill-idea).

## Stacks With
→ `/jenny-hook` (routes here when the hook fails, viewed-vs-swiped <70%)
→ `/jenny-loop-rewatch` (when retention reads above 100%, the missing lever is loop design)
→ `/jenny-script-short` (apply the prescribed fixes to a rewrite)

**Execution prompts**: before producing the deliverable, check `skills/jenny-hoyos-shorts/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
