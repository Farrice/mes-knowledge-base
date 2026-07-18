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

---

## Head-to-head RULING (2026-07-18, Opus judge, both arms firewalled — evidence at strategy_briefs/2026-07-18-authority-flywheel-positioning-strike.md vs .tmp/strike-prose/)

**HYBRID — prose orchestration stays the DEFAULT strike route** (82k tokens / 179s, zero
fabrications, plus an epistemic catch the native arm missed). **Use /strike-native only
when genuine expert INDEPENDENCE on a load-bearing dissent is the point** — its isolated
agents scored 5/5 independence vs prose's 3/5 (persona-channeling bleed: shared
vocabulary, too-neat self-reconciliation) at 4.5× token cost. The migrate rule required a
completeness-AND-fabrication double win; native didn't clear it.

**Stolen back into the prose path (do these when running prose strikes):** (1) force a
structured claims-with-source table, not inline labels; (2) persona-vocabulary firewall —
each expert take must use its own method vocabulary, never share coined terms across
takes. Cross-validation note: both firewalled arms independently resolved the dissent the
same way (surface/audience-stage) — the analysis itself is sound.
