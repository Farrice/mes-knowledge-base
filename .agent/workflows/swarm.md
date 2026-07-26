---
description: Deterministic swarm conductor — plan gate, then unattended pattern execution (heavy/research today; council/mission/browser via pointers)
supersedes: swarm-commander tier-1.5 simulation (2026-07-07)
---

# /swarm Workflow — Conductor v2

> **Session 1 of Swarm Apex** (`_active/swarm-apex-2026-07-07/PLAN.md`). This replaces the
> SEQUENTIAL-SIMULATION behavior of swarm-commander (its own docs call it "80-95% of
> parallelism benefits" — it isn't) with a real conductor: deterministic scaffolding
> (`execution/swarm_conductor.py`) → ONE plan gate → unattended native-Workflow execution
> → honest receipt. swarm-commander's grounding discipline (🟢/🟡/🔴 tags, the Grounding
> Pass) is PRESERVED — it now lives inside the pattern scripts' worker contracts, not in
> a sequential prompt-engineering simulation.

## Usage

```
/swarm [Your objective here]
/swarm --pattern heavy|research [Your objective here]
/swarm --effort low|medium|high [Your objective here]
```

If `--pattern` is omitted, infer it: a decision/positioning/strategy call with dissent
worth preserving → `heavy`; a real-world factual question → `research`. If ambiguous, ask
(one round, DICE-scored per The Chain Step 2).

---

## The Flow (5 Steps)

### 1. Score intent (DICE)

Score 1-5 per The Chain Step 1 (Deliverable, Audience, Context, End-state, Specific
language). Score ≤3 → sharpen once (missing DICE dimensions only, one round max). Score
≥4 → proceed silently.

### 2. Plan

Run the deterministic scaffolder and surface its FULL printed output verbatim — the
mission file path, the fan-out mapping used, the roster table (heavy) or subtopic count
(research), any degradation notes, and the **PLAN GATE** line — to Farrice:

```bash
python3 execution/swarm_conductor.py plan --brief "<the outcome wanted>" \
    --pattern heavy|research --effort low|medium|high --slug <kebab-slug> \
    [--domains "d1,d2"] [--deliverable <path>]
```

This writes `.tmp/swarm/<slug>/mission.md` — the Manus-style `todo.md` recitation
surface every worker and the synthesizer re-read — and prints the exact native-Workflow
invocation (`scriptPath` + JSON `args`) the orchestrator fires next.

**PLAN GATE is compass, not cage** (see Binding Constraints below): if Farrice has
already said "go without gate" for this class of work, or says it now, skip the pause —
launch immediately — but the mission.md file still gets written first. It is never
skipped, only the wait is.

### 3. Launch (on "go")

**Claim the tree first** (merge-discipline.md Law 0): `python3 execution/session_lock.py
claim "swarm: <slug>"` — a fresh foreign lock blocks the launch, not the plan. Workers
write only to their printed `outDir` under `.tmp/` (Law 1); the conductor merges serially.

Fire the printed `scriptPath` with the printed `args` via the native Workflow tool,
`run_in_background` (unattended — no babysitting, no manual polling).

- `heavy` routes to `.agent/workflows/swarm-heavy.workflow.js` (LIVE) — consumes
  `{slug, brief, fanOut, roster, missionPath, outDir}` exactly as the conductor prints
  them; the roster is decided at plan time by `swarm_conductor.py`, never re-cast at
  execution time. Diverge → Aggregate (dissent-preserving) → Verify (adversarial) →
  Assemble (Answer / Forks / Claim ledger / Task trace).
- `research` routes to `.agent/workflows/swarm-research.workflow.js` (LIVE) — consumes
  `{slug, question, depth, missionPath, outDir}`; the script derives subtopic count from
  depth itself (standard=6, deep=10 — matching the conductor's fan-out mapping exactly).
  Decompose → Sweep → Gap check (deep runs may trigger one followup sweep) → Verify →
  Synthesize (Single Truth / labeled narrative / source inventory / task trace).

Both scripts return `{deliverablePath, taskTrace, forks|gaps, tokensSpent, agentCount}` —
use `tokensSpent` and `agentCount` as the REAL numbers for step 4's receipt.

### 4. Surface + receipt

On completion, read the workflow's returned result object and surface to Farrice:
the deliverable (or its content if no file was written), preserved dissent / forks,
and claim/verification counts (VERIFIED/LIKELY/UNCONFIRMED). Then write the honest
receipt with REAL measured numbers — never estimates:

```bash
python3 execution/swarm_conductor.py receipt --slug <slug> --status pass|partial|fail \
    --agents <measured sub-agents spawned> --tokens <measured tokens spent> \
    --deliverable <path> [--notes "..."]
```

This lands the run in `.agent/run-receipts/` in the standard schema (owner `swarm`)
with a per-run **Economics** section (agents spawned, tokens spent — the one honest
move Grok makes, done better here because it's receipt-carrying, not a vibe), and
flips the mission file's `status` to `done`/`failed`.

### 5. Finalize

This IS a deliverable — run Chain Step 6 finalize (`chain_runner.py finalize`) and put
the deliverable path in the retrieval block, same as any other production output. A
swarm run does not get a lighter finalize pass than a single-expert one.

---

## Pattern Table

| Pattern | What it does | When |
|---|---|---|
| `heavy` (LIVE — `swarm-heavy.workflow.js`) | N independent expert trajectories on ONE problem (deterministic fan-out: 4/8/12 by effort), each through a distinct lens, reflective aggregation that PRESERVES dissent (never blends to mush), adversarial claim verification on the merged answer | Hard decisions, positioning, strategy calls — anywhere a single-leader-agent blend would hide real disagreement |
| `research` (LIVE — `swarm-research.workflow.js`) | Query decomposition into subtopics (6/6/10 by effort → standard/standard/deep), parallel word-ceilinged source-locked search workers, gap-driven followup sweep (deep only), claim inventory with VERIFIED/LIKELY/UNCONFIRMED labels, honest receipt + visible task-trace | Any real-world factual question — **never answer research from training memory** |
| `council` | Cross-domain deliberation with informed dissent | Use the existing `/convene` (presets `/council` `/roundtable` `/strike` `/campaign` `/deploy`) directly — `collective-genius-council.workflow.js` already does this natively; `/swarm` does not re-wrap it |
| `mission` | Manus-style planner + general-executor steps, multi-day resume | **Not yet built** — Session 3 of Swarm Apex. Saying so honestly beats faking it |
| `browser` | Playwright worker type, AX-tree default, deterministic domain gating | **Not yet built** — Session 4 of Swarm Apex. Until then, browser tasks go through `directives/browser-automation-safety.md` directly, not through `/swarm` |

---

## Binding Constraints (quoted from `_active/swarm-apex-2026-07-07/PLAN.md` — do not paraphrase)

> Constraints that BIND this design: no `.claude/agents/` named subagents (generic
> Agent-tool dispatch with Tier-3 expert file injection only) · no new orchestration hub
> (conductor composes) · 12-worker cap + 4-field envelope · word-ceilinged worker reports
> (density > completeness) · never pin Opus · plan-gate = compass not cage.

Concretely, every pattern run obeys:

- **12-worker cap** — no fan-out exceeds 12, ever (`heavy` high=12 is the ceiling).
- **Plan gate is compass, not cage** — Farrice can say "go without gate" and skip the
  pause; the mission.md still gets written, it's just not waited on.
- **Grounding tags mandatory** — every factual claim in every worker output carries
  🟢 GROUNDED / 🟡 SUPPLEMENTED / 🔴 PROJECTED (swarm-commander's Grounding Pass ethos,
  now enforced inside the pattern scripts rather than a standalone sequential phase).
- **Workers are word-ceilinged** — density > completeness; ≤500 tokens per worker report.
- **Never pin Opus** — sub-agents inherit or run Sonnet; on "not available," degrade a
  tier, don't stall.
- **PATH DECISION surfaced on strategy-shaped briefs** — `swarm_conductor.py plan`
  auto-detects strategy-shaped language (positioning/pricing/offer/pivot/brand/etc.) and
  writes the `_active/path-decision-2026-07-01/README.md` Incumbency Rule guard directly
  into the mission's Constraints section. Do not drop it from the deliverable.

## DEPTH CONTRACT (mandatory on every research-shaped brief — added 2026-07-26)

Root cause of the 2026-07-25 shallow-research incident: an ad-hoc research swarm ran
single-pass, snippet-fed, with self-verified evidence — and shipped as decision-grade
because no floor bound it. Any brief whose workers gather external evidence MUST carry
these four guards, written into the brief itself (the depth tiers live in
`execution/research_depth.py` — read them, don't restate them):

1. **Fetch mandate** — workers read FULL pages (WebFetch / `tvly extract`), never build
   claims from search snippets. JS-rendered or login-gated primary sources route to the
   Playwright lane (`deep-research-swarm.workflow.js`), never get dropped silently.
2. **Round minimum** — at least one gap-check + follow-up round after the initial sweep
   (standard=1, deep=2, max=3). Single-pass research is reconnaissance, label it so.
3. **Per-question floor** — sources/domains per the depth contract, checked after the
   run with `python3 execution/research_quality_gate.py validate <report> --depth <tier>
   --receipt`. A Research-type finalize without that PASSING receipt gets Factual
   Grounding capped at 6 by `chain_runner.py` (deterministic, not advisory).
4. **Independent verification** — every load-bearing claim is attacked by an agent that
   did NOT find it (refute-default). Finder-verified claims count as UNCONFIRMED.

A research deliverable that has not passed the depth gate ships with a
`⚠️ RECON-GRADE — not decision-grade` banner at the top of the artifact. Shallow work
may exist; unlabeled shallow work may not.

---

## Fallback (Codex / no native Workflow tool)

If the native Workflow tool is unavailable on the current surface (e.g. Codex), do NOT
silently simulate it. Still run `swarm_conductor.py plan` for the deterministic
scaffolding (mission file, fan-out, roster), then fall back to
`skills/swarm-commander/` sequential persona simulation for the actual execution — and
SAY SO explicitly in the output: **"Running degraded (no native Workflow tool on this
surface): sequential simulation via swarm-commander, not true parallel fan-out."**
Degraded and reported, never degraded and hidden.

---

## Notes

- Mission files persist at `.tmp/swarm/<slug>/mission.md` — never committed, but not
  ephemeral either; `swarm_conductor.py status` lists every mission on disk.
- `--verbose` (legacy swarm-commander flag) still applies inside the fallback path only:
  shows each agent's full output before synthesis. The native pattern scripts already
  stream phase-by-phase progress via the Workflow tool's own logging.
- Extractions, `/convene` presets, and single-artifact `/make`-style requests are NOT
  `/swarm` jobs — this conductor is for multi-trajectory fan-out specifically.
