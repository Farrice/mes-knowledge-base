---
thread: expert-assembly-os
status: ready
resume_hint: E2E-test /panel-sync reload on the pinned sailing panel, then MyBPM Week 1 /assemble run
unfinished: /panel-sync reconvene path untested; coverage scoring edge cases; plugin packaging deferred
branch: main
pin: true
---

# Expert Assembly OS — Build v1 Shipped (hybrid casting + /assemble + /panel-sync)

## Purpose
- **Next session should do:** (1) E2E-test the `/panel-sync` reload path on the pinned sailing panel (thread `assemble-competitive-sailing-rigging-optimization-for-a-3`) — the one untested seam; (2) first revenue-adjacent run: `/assemble --domains "streetwear launch ops,offer positioning,short-form content" "Design the MyBPM Week 1 launch sequence"`.
- **Not in scope:** rebuilding any engine piece (extend never rebuild), plugin packaging (deferred until real-usage proof), re-running the archive mining (lineage fully recovered).

## Load First
- `guides/2026-07-15-expert-assembly-os.md` — the operator guide: commands, mental model, honest edges.
- `.agent/workflows/assemble.md` + `.agent/workflows/panel-sync.md` — the front-door contracts.
- `.tmp/assemble/competitive-sailing-rigging-optimization-for-a-3/panel.json` — the pinned panel /panel-sync must reload (personas in `personas/`, 3 files, all lint-PASS).
- `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md` — the solution card (architecture + wire map).

## Current State
- **Objective:** Farrice's claude.ai GENIUS-LEVEL EXPERT ASSEMBLY SYSTEM reborn production-grade in Claude Code.
- **What is already done:** Full lineage recovered from `_archive/claude-export-2026-07-01.tar.gz`; `panel_cast.py` (coverage-aware hybrid casting) + `persona_stat_lint.py` (deterministic no-fake-stats gate) + `expert-assembly.workflow.js` (8 phases, Conductor Ladder seating: Sonnet grind / session model on converge+synthesize); front doors, router keywords, routing-binding row + enforcer allowlist, PRODUCTION_CORE entry, skill dir with persona-synthesis prompt + roadmap schema + lineage receipts; PoC A/B (persona beat vanilla); E2E run wf_b0c91bb5-606: 17/17 agents, 0 errors, grounding PASS; Chain finalize logged (anchored 9/9/8, FG 9); operator guide filed in guides/ + INDEX updated + sync stamped; project memory saved.
- **What is uncertain or stale:** `/panel-sync` reconvene path untested end-to-end; keyword coverage scoring is crude (one stopword bug fixed, more edge cases likely — pre-flight casts with `panel_cast.py` CLI); Ground phase is quick-depth only.
- **Latest proof/receipt:** commits `26adc893f` + `94d30a0ee` on main (pushed); outcome at `.tmp/assemble/competitive-sailing-rigging-optimization-for-a-3/outcome.md` (grounding PASS); digest `knowledge/assembly-sessions/2026-07-15-…md`; rubric line in `knowledge/assembly-rubric.md`.

## Suggested Skills / Workflows
- `/panel-sync` — the untested seam; testing it IS the work.
- `/assemble` — the front door for the MyBPM run.
- `python3 execution/panel_cast.py "<task>" --domains "a,b,c"` — $0 pre-flight of any cast.
- `/jam` — offer after the MyBPM roadmap lands (taste-bearing forks).

## Exact Next Prompt
```text
/panel-sync --session "competitive-sailing-rigging-optimization-for-a-3" "Stress-test Fork B (boundary authority): what's the printed default rule when matrix and feel disagree in a partially-logged condition?" — verify the same three personas (Ingrid Solberg, Oz Lindqvist, Mara Solstad) reload from .tmp/assemble/.../personas/ and stay in voice. If reload works, then run: /assemble --domains "streetwear launch ops,offer positioning,short-form content" "Design the MyBPM Week 1 launch sequence"
```

## Acceptance Criteria
- /panel-sync reloads the exact pinned panel (names match panel.json), personas stay in voice, and produces a converge answer on Fork B — no re-forging.
- MyBPM run seats roster experts (expect Meg Heckman / content roster) for strong domains and forges at most 1 composite; outcome.md passes grounding; roadmap rows all have observable success criteria.

## Risk Notes
- Two live sessions co-edited this tree today (GOLDEN RULE: one tool per working tree) — check `git status` is clean before starting.
- Personas are composites: never let a persona-originated "fact" ship without research.py grounding.
- Runs cost ~1.2M subagent tokens — one panel per real decision.
