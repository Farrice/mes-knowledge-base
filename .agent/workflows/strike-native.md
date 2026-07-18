---
description: Strike Team (native) — Wave-4 pilot of the /strike pattern as a Workflow-engine script
---

# /strike-native — Native-Script Strike Pilot

Wave-4 Frontier Elevation pilot. Same **shape** as `/strike` (2-4 expert sub-agents on one
multi-faceted task, straight to synthesis) but implemented as a **native Workflow-engine script**
(`execution/workflow_scripts/strike_native.js`) instead of prose orchestration
(`.claude/agents/_archived/swarm-orchestrator.md` / `collective-genius-council.workflow.js`
mode=`strike`).

## When to use

- You want to A/B the native-script strike pattern against the prose-JCC strike on the SAME
  mission (see `.tmp/wave4-strike-pilot/COMPARISON-PLAN.md` for the judging protocol).
- You already know the 2-4 experts and their focus — this workflow skips convene/diverge/select
  (unlike `collective-genius-council.workflow.js`, which casts its own roster). Use `/strike` or
  `/convene` instead when you want the roster picked FOR you.
- Not yet the default route — `/strike` stays canonical until the comparison declares a winner
  (migrate-on-evidence, per the comparison plan).

## Execution

Invoke the **Workflow tool** with:
- `scriptPath`: `execution/workflow_scripts/strike_native.js`
- `args`:
  ```json
  {
    "mission": "<the multi-faceted task>",
    "experts": [
      { "name": "<Expert Name>", "skillPath": "skills/<expert-skill-dir>", "focus": "<their slice of the mission>" }
    ],
    "synthesis": "<what the final deliverable is, e.g. 'a launch brief' or 'a positioning memo'>"
  }
  ```
  `experts` must have 2-4 entries — the script throws outside that band (route to `/convene --mode wide` instead).

## Phases

1. **Brief** — one cheap (sonnet, low-effort) agent turns the mission + each expert's `focus`
   into a per-expert task brief (schema-forced JSON) — briefing only, no takes written here.
2. **Strike** — parallel, one agent per expert. Each loads its OWN `SKILL.md` + `genius.md` from
   `skillPath`, produces its take, labels every factual claim VERIFIED/LIKELY/UNCONFIRMED, lists
   its gaps, and writes `{name, take, claims, gaps}` to
   `.tmp/strike-native/<slug>/experts/<expert-slug>.json`.
3. **Synthesize** — one agent compounds the takes into the named deliverable — **preserves
   dissent** (never averages disagreement away), carries claim labels through unchanged, and
   writes the deliverable to `.tmp/strike-native/<slug>/deliverable.md`.

## Returns

```json
{
  "mission": "...",
  "deliverable": "<real path written to disk>",
  "dissents": [{ "tension": "...", "positions": [{ "expert": "...", "position": "..." }] }],
  "claims": [{ "text": "...", "label": "VERIFIED|LIKELY|UNCONFIRMED", "source": "..." }],
  "gaps": ["..."],
  "per_expert_paths": [{ "name": "...", "path": "..." }],
  "quarantine_root": ".tmp/strike-native/<slug>",
  "protected_tree_clean": true
}
```

Deliverable paths, not self-report: every path in the return was written to disk by the agent
that reports it (schema-forced), not asserted in prose. `quarantine_root` /
`protected_tree_clean` / `gaps` are shaped for `execution/mission_validator.py` (built in
parallel elsewhere in Wave 4) but this script never imports or calls it.

## Related

`/strike` (prose path, canonical until evidence says otherwise) · `/convene` (full council,
casts its own roster) · `directives/orchestration-doctrine.md` (Pattern Table — Strike is a
2-4-expert composing pattern under "Council") · `.tmp/wave4-strike-pilot/COMPARISON-PLAN.md`
(judging protocol).
