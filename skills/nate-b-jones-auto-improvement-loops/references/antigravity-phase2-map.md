# Antigravity Phase 2 ↔ Karpathy Patterns Map

Direct mapping from Nate's 18 genius patterns to Antigravity's existing Phase 2 infrastructure. Used by Workflow 08 (Phase 2 Karpathy Audit) as the starting frame.

## Current Phase 2 Infrastructure

| File | Purpose | Karpathy Analog |
|------|---------|-----------------|
| `directives/evolution-direction.md` | Human-authored direction + history log | **program.md** (GP-8) ✅ |
| `execution/skill_benchmark.py` | Fixed-budget evaluation harness | **The scorer + time budget** (GP-1 partial) ✅ |
| `execution/evolution_tracer.py` | Evolution attempt logging | **Trace infrastructure** (GP-6) ⚠️ check depth |
| `.agent/workflows/skill-evolution.md` | The evolution loop workflow | **The meta-agent loop** (GP-4) ⚠️ check split |
| `.agent/workflows/harness-evolve.md` | Harness-specific variant | Auto-agent variant (GP-3) ✅ |
| Performance Log (Notion DB) | Ratchet scoring + history | Experiment log (GP-17) ✅ |

## Pattern-by-Pattern Status

| Pattern | Phase 2 Status | Gap |
|---------|---------------|-----|
| GP-1 Karpathy Triplet | **Partial** — single-file constraint exists in evolution-direction.md; metric exists (composite score); time budget implicit | Add explicit Triplet section to evolution-direction.md header (Light Path C fix) |
| GP-2 Iteration rate | **Low** — 100+ KEPT cycles over weeks, not overnight batches | Consider overnight batch mode for bulk evolution cycles |
| GP-3 Auto-research vs Auto-agent | **Both covered** — skill-evolution.md (auto-agent) + knowledge_compiler.py stages (auto-research-like) | None — distinction is clear |
| GP-4 Meta/Task split | **Implicit** — currently same Claude instance generates + evaluates | Document whether split is happening or not; if single-agent, flag as risk |
| GP-5 Model empathy | **Implicit** — Claude evaluating Claude (aligned by default) | Document the constraint explicitly |
| GP-6 Traces over scores | **Unknown** — need to inspect evolution_tracer.py output depth | Primary audit target of WF 08 |
| GP-7 Emergent behaviors | **Unknown** — has Phase 2 invented patterns? | Inventory what Phase 2 does vs what it was told |
| GP-8 Program.md | **Yes** — evolution-direction.md is the analog | Already aligned; reinforce in audit |
| GP-9 Local hard takeoff | **Yes** — Phase 2 IS a local hard takeoff on skill quality | Observe: 100+ KEPT cycles in ~2 weeks = classic takeoff trajectory |
| GP-10 Prerequisites | **Mostly yes** — context layer ✅, trace ⚠️, eval ✅, sandbox (git worktree? revert?) ✅, governance ✅ | Verify sandbox + trace depth |
| GP-11 Small team | **Yes** — solo operator (Farrice) | N/A — already optimal |
| GP-12 Safety — metric gaming | **At risk** — if meta-agent learns to write variants that game composite score | Add held-out benchmark test |
| GP-12 Safety — drift | **At risk** — no explicit regression check across unchanged skills | Add cross-skill regression audit |
| GP-12 Safety — contamination | **Low risk** — evolution tasks are separate from benchmark tasks | Verify isolation |
| GP-12 Safety — cascade | **At risk** — KEPT variant in skill A could silently break skill B | Add downstream impact check |
| GP-13 Activity vs outcome | **Good** — composite score correlates to intent/expert/adversarial/factual | Consider Revenue Tracker link as outcome metric |
| GP-14 Concentrated judgment | **Yes** — user reviews variant before KEEP; direction.md is human-authored | Preserve this; do not automate promotion |
| GP-15 Labs vs open source | N/A | N/A |
| GP-16 Earn-the-right | **Yes implicitly** — skills are internal-facing; no customer system evolves | Document as explicit constraint |
| GP-17 Auditability | **Yes** — git commits per KEPT variant, Notion log, evolution-direction.md history table | Excellent — preserve |
| GP-18 Reddit proof point | N/A | Phase 2 IS the Reddit proof point (applied to Antigravity skills) |

## Prescribed Upgrades (from WF 08)

The following concrete changes emerge from this map:

### Priority 1 — Trace Depth Upgrade
- **Finding**: Score-only logging produces random mutations
- **Action**: Inspect `evolution_tracer.py`; ensure each attempt logs full reasoning trajectory (hypothesis, variant diff, benchmark output with reasoning, failure points)
- **If missing**: Upgrade tracer to capture trajectories before next evolution cycle

### Priority 2 — Meta/Task Split Documentation
- **Finding**: Single-agent self-improvement fails predictably
- **Action**: Clarify whether `/skill-evolution` uses one Claude instance or spawns a separate sub-agent for variant generation vs. benchmarking
- **If single**: Refactor to explicit sub-agent split, OR document that single-agent mode is intentional for this context (small scope per cycle)

### Priority 3 — Karpathy Triplet Header
- **Finding**: Triplet is implicit, not explicit
- **Action**: Add to top of `evolution-direction.md`:
  ```
  ## The Karpathy Triplet (for this system)
  - Editable Surface: single workflow file per cycle (one `.md` file)
  - Metric: composite quality score (Intent + Expert + Adversarial + Factual), min 7.0 + no dim <6
  - Time Budget: 10 min per benchmark run, max 3 cycles per skill before pausing
  ```

### Priority 4 — 4-Mode Safety Additions
- **Gaming**: Add held-out benchmark task the variant has never seen
- **Drift**: Add cross-skill regression suite
- **Contamination**: Verify eval tasks aren't in variant generation context
- **Cascade**: Track downstream skill dependencies; flag if KEPT variant touches shared references

### Priority 5 — Emergent Behavior Inventory
- **Action**: Read last 30 evolution entries; identify any patterns the system invented (not in original workflow spec)
- **Catalog**: Add discovered patterns to `emergent-behaviors-catalog.md`
- **Pre-load**: Build explicit affordances for the top 3

---

## Integration Constraints

- **Do not modify genius.md files of existing skills** (constraint from `evolution-direction.md`)
- **Single file per cycle rule preserved** (already aligned with GP-1)
- **Human in the loop preserved** (GP-14)
- **Git commit every KEPT variant preserved** (GP-17)
- **Auto-revert DISCARD preserved** (GP-12 revert capability)

---

## Anti-Pattern Avoidance Check

Phase 2 currently avoids:
- ✅ Customer-facing first targets (evolves internal skills only)
- ✅ No-human-in-loop promotion
- ✅ Unversioned changes
- ⚠️ Possibly: score-only logging (audit target)
- ⚠️ Possibly: single-agent self-improvement (audit target)
- ⚠️ Possibly: no held-out benchmark (safety gap)

These three are the primary targets for Workflow 08 output.
