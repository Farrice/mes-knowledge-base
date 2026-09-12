---
description: "The ONE task door (both harnesses, 2026-09-11) — mirror the raw ask, compile it with the real engines, shape-check it (task / job / decision / deliberation), route it to one owner, run it with only the three code-defined taste gates, close with a run receipt. No sign-off beat unless --preflight."
---

# /autopilot — The Task Door

**Why this file changed (2026-09-11, Farrice: "I like autopilot but it felt like it never did
what it was supposed to").** Three doors — `/go`, `/raw-intent-bridge`, `/autopilot` — called
the same two engines (`codex_operator_preflight.py`, `raw_intent_run_packet.py`) behind three
different ceremonies. Stacked in one message they made the model pick the lightest one and
skip the board. `/go`'s always-on preflight sign-off was a tax on task-shaped work. The bridge
was a competing door. Now: **task-shaped asks come through here. Job-shaped asks go to `/job`.
Deliberation goes to `/convene`.** `/go` survives as this door with `--preflight` on; the bridge's
Stage 0 lives here as Stage 0.

## Invocation

```
/autopilot <raw ask>              mirror → shape check → compile → route → gates → run → receipt
/autopilot --preflight <raw ask>  same, but print the MISSION CARD and WAIT for approval (= /go)
/autopilot --plan <raw ask>       stop at a decision-complete plan, nothing runs
/autopilot --menu <raw ask>       ranked options (backend: /orchestrate)
```

Both harnesses. Codex reaches it via `$autopilot` (global bridge `~/.codex/skills/autopilot/SKILL.md`,
thin pointer to this file). Never fork a Codex copy.

## Stage 0 — MIRROR (from the bridge; 1–3 visible lines)

Build the Translation Card before anything routes: **Anchor** (which project / client / system —
match project memory, never guess across projects) · **Deliverable** · **Audience** · **Felt standard**
(his vision words, verbatim — the creative payload, never paraphrased) · **Sharpened line**
(`<verb> <deliverable> for <anchor> using <owning OS/expert> — <felt standard, compressed>`, with
route-findable keywords). Reply opens with the mirror plus ONE push-back if a real fork is live.
Anchor or deliverable unfillable from the ask + disk → exactly ONE question, then proceed. Never
feed flow-speech to the compiler (scar 2026-07-02: warehouse-rave MyBPM merch routed to
`/albom-gravedigger-angle`).

## Stage 1 — SHAPE CHECK (deterministic, before compiling)

| Signal | Shape | Do |
|---|---|---|
| several deliverables / systems / days; lanes that depend on each other; "handle it", "end to end" | **Job** | Stop here. `/job "<ask>"` — the JOB PLAN is the packet. Never run a job through this door. |
| "should I", "which", "or" — one packet would answer it | **Decision** | `/job` with `recipes/decision-packet.md` (one lane, one packet). |
| "what do the experts think", tradeoffs across domains, council | **Deliberation** | `/convene`. |
| one owner, one deliverable, fits a session | **Task** | continue below. |

The hook already prints `MODE JOB-HANDOFF` and `JOB PRE-WORK` on job-shaped asks; obey it over
this table. `python3 execution/recipe_cards.py match "<ask>"` is the tiebreaker.

## Stage 2 — COMPILE (engines, never prose)

```bash
python3 execution/codex_operator_preflight.py "<sharpened line>" --plain   # intent lock · launchpad · scored routes
python3 execution/raw_intent_run_packet.py "<sharpened line>" --mode auto --plain   # packet · first safe action · run prompt
```

Modes when the lane is obvious: `--mode revenue | creative | system`. The packet must carry:
predicted need · center · success standard · constraints · missing inputs · questions that change
execution · chosen route · support gates · composition slots · context plan · execution decision ·
first safe action · verification plan · operator run prompt. **Questions gate:** clarity ≤2 OR
"questions that change execution" non-empty → ask that one round FIRST. A high DICE feel never
suppresses an execution-changing question.

Goal spine: read `.agent/cos/goals.json`; name the goal served or `ORPHAN ⚑` (one line, never a
block). `python3 execution/hooks/campaign_beacon.py` — an open campaign the ask does not serve
gets one line above the work, never a stop.

## Stage 3 — ROUTE (one owner)

The packet's route, second-opinioned by `python3 execution/workflow_router.py` and the routing
bindings (`directives/routing-bindings.md`). **Skill on match = must load**: name the SKILL.md
loaded in one line before producing (redirectable). Never this door as a catch-all; never two
conductors for one deliverable. Owner rules that stand: broken / drifted / not-firing / parity
complaints → `/system-audit` · caliber-drift or "lost the good part" → `/repeatability-spine` ·
more than three plausible experts → `/expert-composition-governor` as a support gate · steering
and next-prompt coaching → `/steering-compass`. Outcome classes and their primary routes are the
table in `execution/outcome_recipes.py` (source of truth; never extend it in prose).

## Stage 4 — GATES (code, not judgment; the only allowed halts)

```bash
python3 execution/gates.py check --dice <1-5> [--est-cost <dollars>] [--services <csv>] [--deliverable <path>] [--expert-score <n>]
```

Exit 0 = run end to end. Exit 2 = a gate fired; the output names it with its remediation.
Inputs not provided report "not evaluated" — never a silent pass.

| Gate | Fires when | Remediation |
|---|---|---|
| **G1 Intent** | DICE ≤ 2 | one question round on the missing dimensions, then proceed |
| **G2 Cost** | est-cost > $5 OR a service returns needs-approval/denied from `cost_gate.py check` (hook-enforced on Claude Code; manual on Codex) | ask once; after his yes `python3 execution/cost_gate.py approve --service <id>`; denied = surface, never retry |
| **G3 Prose/taste** | Expert Standard ≥ 7 AND `prose_classifier.py check` FLAGGED | surface exactly ONE taste call; real-world claims also run `python3 execution/claim_audit.py check <path>` |

Every other mid-flight halt (routing ambiguity, format, model, minor scope) is suppressed by
design. Compass doctrine: only the cost gate and the factual veto block.

## Stage 5 — RUN

Name one execution status before work starts:

| Status | Meaning |
|---|---|
| `Running now` | safe, workspace-local, verifier-backed; start after the mirror |
| `Needs judgment` | a taste / scope / intent point is his; ask it (one line) |
| `Blocked by risk` | external write, paid tool, destructive cleanup, global `~/.codex` edit, publishing, connector write, real subagent without a run-specific grant |
| `Blocked by configuration` | the route or a planned verifier does not resolve to a callable local target — repair the owner surface first |
| `Plan only` | `--plan`, `--menu`, or an explicit no-execution posture |

Then the Chain as usual: load the expert (minimum two skill files for content), produce, ground
(VERIFIED / LIKELY / UNCONFIRMED), finalize (`chain_runner.py finalize`). First action local and
reversible. Writes in a lane (GOLDEN RULE). Seats: Fable conducts; read-only research on Sonnet
seats carrying "no Chain, no finalize, no Notion, no Next Moves, return only the artifact"; on
Codex the model is the pen and real subagents stay run-authorized and read-only. Two rejected
takes on one artifact = back to the input, never a third variant.

## Stage 6 — RECEIPT + CLOSE

```bash
python3 execution/run_receipt.py --query "<raw ask>" --route "<route>" --status "<status>" --changed "<what changed>" --passed "<checks>" --failed "<failures>" --judgment "<judgment needed>" --next-action "<next>"
python3 execution/friction_ledger.py log --kind failed-route --summary "<what happened>" --next-action "<repair route>"   # only when routing/hook/proof friction appeared
```

Substantive runs also file the mission (`python3 execution/work_catalog.py add <slug> --title
"<intent>" --serves <goal>`) so the pulse board and the finisher rule see it. Close per
`directives/steering-loop.md`: Next Moves (Deepen / Adjacent / Act) + one Operator Lesson when
something shipped; skipped on answers, diagnostics, corrections. Last line on a deliverable:
`Verdict on this one — good / marginal / off?`

## `--preflight` (the /go card, opt-in)

Print the MISSION CARD (Intent · Serves · Felt standard · Clarity · Predicted need · What good looks
like · Route + runners-up · Pattern + Expected spawns · Loads · Gates · Tier · Cost · Deliverable
paths) and **WAIT**. On approval write `.agent/missions/<slug>/contract.json` and `portable.md`
(`python3 execution/raw_intent_run_packet.py "<intent>" --plain > …/portable.md`). The card spec,
the continuity check (`pulse_dashboard.py --open`, continue / adjust / park / new), expert
composition (`expert_router.py route`, `recommend_stack.py`), and the mission-log lines live in
`.agent/workflows/go.md` — read it only on `--preflight`. On Claude Code the plan-review flow is
the card's surface; on Codex the compact card is.

## Subagent boundary (Codex; verifier-pinned language)

Real Codex subagents need explicit run-specific authorization. When authorized they are
read-only diagnostics by default: no further subagents, and the main thread owns all edits,
synthesis, and integration. The pinned rules, verbatim (lowercase on purpose — the verifier
matches them literally):

- add to fan-out list only if farrice has explicitly authorized it for this run
- otherwise run the research angles sequentially in the main thread
- an authorization packet names worker count, read-only scope, deny list, halt condition, and no further subagents

On Claude Code the equivalent is the `/job` dispatch seat: a read lane on Sonnet with a brief
file and a result contract, never a judge seat.

## Backends, not doors

`/orchestrate` (ranked options; `--menu`) · `/mission` (Mission OS — a live door in its own right,
his call 2026-09-11; same store as `/job`) · `/swarm` (research fan-out patterns; on Codex via
`codex_dynamic_workflow.py`) · `/supercomputer`, `/jw-engine`, `/create` (conductors this door
routes TO). Capability stewardship, the plugin-packaging ladder (`plugin_readiness_audit.py`), and
the friction ledger are companion layers inside the run, never new doors.

## Contract vocabulary (the Intent-To-Outcome contract, by stage)

The verifiers pin these names; each maps to one stage above, never to a new beat.

| Name | Lives in | What it is |
|---|---|---|
| **Intent-To-Outcome** | the whole door | the contract: raw ask in, receipted outcome out, one owner |
| **Co-Creative Launchpad** | Stage 2 (`codex_operator_preflight.py`) | intent lock + launchpad + scored routes |
| **Execution Decision** | Stage 5 | the one status named before work starts |
| **Run Prompt** | Stage 2 packet | the operator run prompt the packet ends with |
| **Run Receipt** | Stage 6 (`run_receipt.py`) | what changed · passed · failed · judgment · next |
| **Friction Ledger** | Stage 6 (`friction_ledger.py`) | failed-route / hook / proof friction, one line each |
| **Capability Graph** | Stage 3 (`capability_graph.py`, when present) | what the harness can actually call for this route |
| **Outcome Recipes** | Stage 3 (`outcome_recipes.py`) | outcome class → primary route table (source of truth) |
| **Plugin Packaging Ladder** | companion (`plugin_readiness_audit.py`) | packaging readiness, deferred unless asked |

`Running now` means safe workspace-local execution: first action local and reversible, in a lane.

## Proof standard (control-plane changes only)

```bash
python3 execution/verify_codex_claude_parity.py
python3 execution/verify_google_operator_core.py
python3 execution/verify_system.py --errors-only
python3 execution/run_receipt.py --verify
```

A route, hook, verifier, and visible behavior that disagree = not repaired.
