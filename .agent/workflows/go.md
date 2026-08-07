---
description: The Maestro front door — compile any raw dump into an engine-backed, expert-loaded Mission Card, sign off on the preflight, run it per doctrine, close with a verdict
---

# /go - The Maestro Front Door (v3, 2026-07-21)

`/go "<messy thought>"` turns an underspecified dump into a routed, executed
deliverable — compiled by the SAME deterministic engines the Codex path uses
(no more prose-scored cards), expert stack LOADED not named, and a preflight
you sign off on before anything runs. One front door: `/orchestrate`'s state
and routing machinery now serve /go underneath; invoke /go, not /orchestrate.

v3 rebuild (Farrice 2026-07-21, felt-drift report): v2 compiled cards by
model self-scoring and named experts without loading them — measured result:
zero human feedback ever captured, 52 qualifying runs with 0 spawns, 33
orphan missions never closed. v3 fixes are mechanical, not aspirational.

## Stage -1 — CONTINUITY CHECK (before anything)

Run the real engine — never re-read the log by eye (apex W1, 2026-07-29: the
prose version scoped to "this session" and 41 cross-session missions sat open
unseen, 17 of them for 10-16 days):

```bash
python3 execution/pulse_dashboard.py --open
```

If the compiled intent matches an OPEN mission, present it in one line and ask:
**continue / adjust / park / new**. Continue = reload its contract
(`.agent/missions/<slug>/contract.json`) and resume at the right stage — never
recompile from scratch. **Park = run `/park <slug> "<reason>"`** — a first-class
close that writes the stopped line AND a resumable handoff (spec:
`.agent/workflows/park.md`); parking is a good outcome, not a failure.

**Finisher rule (Farrice, 2026-07-29): at 3+ open missions, the card asks him
to finish or park one before compiling a new one — one line, never a block,
"open it anyway" always works.** Only an explicit "new" starts a fresh compile.

## Stage 0 — MISSION COMPILE (engine-backed, silent)

1. **Run the real compiler** — never re-implement it in prose:
   ```bash
   python3 execution/codex_operator_preflight.py "<raw intent verbatim>" --plain
   ```
   This yields the deterministic layers: **Intent Lock** (clarity score 1-5,
   lane, risk reasons), **Co-Creative Launchpad** (predicted need, center,
   what good looks like, questions that change execution), and **scored Route
   Candidates**. These ship INTO the card as its reasoning surface — visible,
   correctable, never paraphrased into vibes.
2. **Questions gate**: if clarity ≤2 OR "questions that change execution" is
   non-empty, ask those questions FIRST (one round). A high DICE feel never
   suppresses an execution-changing question again.
3. **Goal spine**: read `.agent/cos/goals.json` — name the goal served.
   No match = `ORPHAN ⚑` (one line, compass never cage). Surface an active
   SPRINT when one exists.
   **Revenue-first (standing rule, Farrice 2026-07-29):** run
   `python3 execution/hooks/campaign_beacon.py`. If it shows open campaign
   missions AND this mission's `serves` is ORPHAN or ≠ the campaign goal,
   print one line above the card: `⚠ CAMPAIGN OPEN: #<n> <title> — this
   mission serves <x> instead. Confirm system work ahead of the campaign.`
   His approval at Stage 0.5 IS the answer; never block.
4. **Felt standard** (raw-intent-bridge Stage 0 discipline, kept from v2):
   when the dump carries vision language ("I want it to feel like…"), quote
   it VERBATIM in the card. The Intent line routes; the vision words are the
   creative payload — never compile them away.
5. **Pattern + Tier**: pick the PRIMARY shape from the doctrine Pattern Table
   (solo / solo+jam / fleet / proof-first / council / wargame / swarm /
   verify-fleet / wayfinder) with a one-line reason; classify blast radius
   (T1/T2/T3). **State `Expected spawns: <N>`** from the pattern — fleets and
   swarms name their fan-out here, and the close-out will compare measured
   spawns against this line (the 52-zero-spawn-misses fix).

## Stage 0.2 — EXPERT COMPOSITION (loaded, not named)

Run the composition engines; the card's `Loads:` is their output, not a guess:

```bash
python3 execution/expert_router.py route "<intent>"        # lead + domain
python3 execution/recommend_stack.py "<intent>"            # evidence-backed stack
```

Council/panel-shaped missions add `panel_cast` seating via `/assemble` (hybrid
panel → tiered roadmap) or `/convene` presets. The stack line names: lead
expert, supports, the v2 prompts whose Output Contracts govern the
deliverable, and the load tier. If the stack disagrees with the route
candidates, name the fork in one line and pick — that judgment is the
conductor's, but it happens ON TOP of engine output, never instead of it.

## Stage 0.5 — PREFLIGHT SIGN-OFF (always; Farrice 2026-07-21)

**Claude Code standard surface (Farrice 2026-07-21, same session): the
plan-review flow.** Enter plan mode, write the EXPANDED card into the plan
file — the full manifest: every file that will be loaded (in order), writing
rules in force, gates with their verifiable commands, expected spawns, and
every output path the operator can check afterward — then ExitPlanMode. The
operator's accept IS the sign-off; a rejection with notes is the adjust loop.
The compact card below is the fallback surface (Codex, or when plan mode is
unavailable). Either way: render, then **WAIT**. Fast-approve launches.
This replaces v2's T1-auto-run: every mission briefs back before execution —
the tier governs what may run AFTER approval (T2/T3 rules unchanged).

```
MISSION CARD — <slug>
Intent: <sharpened one-liner>            Serves: <goal-id | ORPHAN ⚑>
Felt standard: <verbatim vision words | omit>
Clarity: <n>/5 (<lane>)   Risks: <from intent lock | none>
Predicted need: <launchpad line>
What good looks like: <launchpad line>
Route: <chosen> (score <n>)  — runners-up: <top-2 alternates w/ scores>
Pattern: <doctrine row> — <reason>       Expected spawns: <N>
Loads: <lead + supports + v2 prompts + tier — from the engines>
Gates: <audit / prose / verify / jam / voice — whichever will fire>
Tier: <T1|T2|T3>   Cost: <$0 | flagged>  Deliverable paths: <where outputs land>
```

On approval, write two artifacts to `.agent/missions/<slug>/`:
- **`contract.json`** — the card as a small JSON contract (intent lock, route,
  stack, expected_spawns, deliverable_paths, gates, tier). This is the light
  version of Frontier Wave 4's Structured Mission Contracts — the shape its
  validator will later enforce.
- **`portable.md`** — ALWAYS (Farrice 2026-07-21): the compiled mission as a
  self-contained paste-anywhere prompt, generated by
  `python3 execution/raw_intent_run_packet.py "<intent>" --plain > .agent/missions/<slug>/portable.md`
  then topped with the card's felt-standard + loads lines. Your raw dump
  becomes leverage in ANY harness (Codex, claude.ai, a fresh session) — the
  meta-prompting deliverable /go was always meant to produce.

## Stage 1 — ROUTE

Hand the mission to exactly one conductor. Running two conductors requires two
genuinely separate deliverables — don't split one ask into a mini-mission.

| Mission shape | Conductor |
|---|---|
| Single content/copy piece | `/create` (+ v2 prompt contract + voice layer if Farrice-named) |
| Multi-deliverable mission | `/supercomputer` |
| Campaign (multi-asset, multi-platform) | `/jw-engine` |
| Fleet-shaped work (10+ units / 3+ workstreams) | Workflow engine per doctrine (scout → agents → gate) |
| Multi-domain panel → tiered roadmap | `/assemble` |
| Decision with real tradeoffs | `/convene` |
| Plan-for-cheaper-executor | `/wargame-run` |
| Full-auto, gates explicitly suppressed | `/autopilot` |
| System/harness repair or audit | `/system-audit` |
| Research question | `execution/research.py` / `/swarm` |
| Voice overlay on expert-pure output | `/voice-over` |

If two rows plausibly match, name the fork in one line and pick the stronger
match (the scored route candidates from Stage 0 are the tiebreaker evidence).
Never default to `/autopilot` as a catch-all.

## Stage 2 — RUN

**Lock gate (merge-discipline.md Law 0):** fleet / swarm / verify-fleet /
wargame-batch patterns, or long autonomous runs, claim the tree first:
`python3 execution/session_lock.py claim "<mission>"` (heartbeat between
waves, release at close). BLOCKED on a fresh foreign lock = take a lane
(EnterWorktree; bootstrap + merge-back are automatic) instead of waiting.
In a lane the lock gate auto-clears (session_lock.py knows — single writer
by construction). Solo/content conductors skip the claim.

Hand the RUN PACKET (= the approved card + contract.json path) to the chosen
conductor as its intent input, then let the conductor run its own sequence.
`/go` stages the engine; it does not re-implement what the conductor owns.
The packet's `Expected spawns` and `Deliverable paths` lines travel with it —
conductors are on notice that close-out checks both.

## Stage 2.5 — LOG (deterministic, both ends)

At compile AND at close, append one line to `.agent/missions.jsonl`:
```json
{"ts":"<iso>","mission":"<intent one-liner>","slug":"<slug>","serves":"<goal-id|orphan>","pattern":"<row>","tier":"T1|T2|T3","status":"compiled|running|done|stopped","expected_spawns":<N>,"measured_spawns":<N|null>,"verdict":"<good|marginal|off|null>","outcome":"<one line at close>"}
```
The pulse dashboard and COS read this log — an unlogged mission is invisible.
**An unclosed mission is a debt**: Stage -1 will surface it next /go.

## Stage 3 — DELIVER + CLOSE VERDICT + Next-Prompts

Deliver the output, then close the loop — this is where /go finally learns:

1. **Close the mission**: append the `done` line with `measured_spawns` (from
   the session ledger's spawn count) vs `expected_spawns`. A mission that
   promised a fleet and ran single-threaded gets named in one honest line.
2. **One-tap verdict**: ask Farrice — **good / marginal / off** — one word.
   **The ask is TEMPLATED, not optional (apex W2, 2026-07-29 — capture rate
   was 2/53, both "good", zero marginal/off ever):** the delivery message's
   LAST line is verbatim `Verdict on this one — good / marginal / off?` and
   the close line is not written until his word lands (or he ignores it —
   then log verdict:null with "unasked" vs "unanswered" distinguished; an
   unasked verdict is a session defect, an unanswered one is his call).
3. **Next-Prompts** (canonical order, unchanged): **Deepen** / **Adjacent** /
   **Next milestone** (read `.agent/cos/goals.json`, name the specific active
   goal — never generic). Skip only on explicit terse-mode.
4. **Mission report as a brief (2026-08-06)**: for substantive builds, offer the
   close-out as a brief-format build report in the Briefing Room — recipe in
   `.agent/workflows/briefs.md` § Mission reports (exemplar: night-shift-2026-08-06).

## Reuse, Not Duplication (v3 inversion)

- `codex_operator_preflight.py`, `co_creative_launchpad.py`,
  `raw_intent_run_packet.py`, `workflow_router.py`, `expert_router.py`,
  `recommend_stack.py` — these ARE Stage 0/0.2. v2's rule ("read for
  reference, don't ship their output") is REVERSED: prose re-implementation
  of engine logic is the defect that made v2 shallow.
- `/orchestrate` (orchestrate.md) remains on disk as the stateful engine
  layer its scripts document — but /go is the front door; don't invoke
  /orchestrate directly (its state reads are folded into Stage -1).

## Universal Harness (Claude Code + Codex — 2026-07-16, unchanged)

This file is the single source of truth for `/go` in BOTH harnesses. Codex
invokes it via `/go` in-workspace (AGENTS.md workflow rule) or the thin global
bridge `~/.codex/skills/go/SKILL.md` from projectless threads. Never fork a
Codex copy — thin trigger bridges only, per the global AGENTS.md contract.

Shared deterministic spine, identical on both sides: `.agent/cos/goals.json`
(goal spine), `.agent/missions.jsonl` (mission log), `chain_runner.py`
(finalize), `workflow_router.py` (route second opinion).

Codex adaptations — everything else runs as written:

- Fleet / swarm / verify-fleet patterns: plan, store, and receipt via
  `python3 execution/codex_dynamic_workflow.py` — real Codex subagents stay
  approval-gated per run (global AGENTS.md subagent boundary).
- Conductor Ladder model seating does not apply — Codex seats its own models;
  pattern + tier discipline is unchanged.
- GOLDEN RULE stands: one tool per working tree. `/go` on Codex needs a clean
  tree clearly assigned to Codex, or the Codex-owned worktree
  (`ANTIGRAVITY_CODEX_WRITE_ROOT`).
