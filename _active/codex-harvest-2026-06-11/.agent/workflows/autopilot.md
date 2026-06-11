---
description: Intent-to-outcome front door for route choice, safe execution, proof, and risk-gated judgment
---

# /autopilot - Intent-To-Outcome Front Door

Turn raw thoughts, goals, drafts, sources, client work, system work, or "what
should I use?" moments into a co-creative launchpad, chosen route, support
gates, safe local execution, verification, and a run receipt. Autopilot is no
longer a planning-only surface. It is the default operating kernel for Codex
Antigravity.

Operator Cockpit V2 is the stricter pre-action surface for non-trivial work. It
wraps Autopilot preflight with an Intent Confidence Packet, status cockpit,
local friction capture, retrieval home, proof plan, and global mirror
checkpoint:

```bash
python3 execution/operator_cockpit.py --intent "[raw request]" --plain
```

## Core Shift

Farrice supplies raw intent, taste, constraints, and judgment. The harness first
builds a shared Co-Creative Launchpad Packet, then chooses the route, composes
workflows and skills, runs safe workspace-local work after a visible trace,
verifies the outcome, and reports proof. Autopilot pauses only for true risk
gates, execution-changing ambiguity, explicit plan/menu mode, or taste judgment
that needs Farrice's call.

## Usage

```bash
/autopilot [raw context]
/autopilot --run [context]
/autopilot --plan [context]
/autopilot --menu [context]
/autopilot --delegate [context]
/autopilot --package [context]
```

Mode behavior:

| Mode | Behavior |
|---|---|
| default | Trace, choose one route, run safe local work, verify, and close with a run receipt. |
| `--run` | Same as default, with explicit run intent. |
| `--plan` | Produce a decision-complete plan and stop. This preserves the old review-first behavior. |
| `--menu` | Route to `/orchestrate` and stop at ranked options. |
| `--delegate` | Allows real Codex subagent planning; actual subagent spawning still follows Codex approval rules. |
| `--package` | Route through `/plugin-readiness-audit` before recommending plugin packaging. |

## Execution Decision

Every Autopilot run must emit one of these statuses:

| Status | Meaning |
|---|---|
| `Running now` | Safe workspace-local work can start after the trace. |
| `Needs judgment` | Farrice must decide a taste, scope, or intent point before execution. |
| `Blocked by risk` | External, paid, destructive, global, Google Antigravity, publishing, connector-write, or real-subagent action is present. |
| `Plan only` | The user asked for `--plan`, `--menu`, or another explicit no-execution posture. |

safe workspace-local execution is allowed when the work is inside
`/Users/farricecain/Codex Antigravity`, non-destructive, additive or reversible,
clear enough to route, and does not involve publishing, outreach, paid tools,
external writes, global mirrors, Google Antigravity edits, destructive cleanup,
or real Codex subagents; real Codex subagents require explicit authorization.

When blocked, Autopilot must include a copy-paste **Run Prompt**. Nothing should
die as a recommendation.

## Pre-Flight Reads

Read only what is needed, in this order:

1. `CODEX.md`
2. `agents/operator-autopilot/AGENT.md`
3. `.agent/intent-memory/current.json` if present
4. `.agent/system-cohesion-state.json` if present
5. `.agent/autopilot-state.md` if present
6. `.agent/session-state.md` if present
7. `.agent/workflows/orchestrate.md`
8. `.agent/workflows/mission.md` when Mission Mode triggers
9. `semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md` for the shared launchpad standard before routing or execution
10. `semantic_libraries/antigravity/primitives/skill-system-contract.md` for skill systems or OS upgrades
11. `semantic_libraries/antigravity/primitives/repeatability-spine-contract.md` for failed revisions or regressions
12. `semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md` for self-improvement or maintenance
13. `semantic_libraries/antigravity/primitives/operating-alignment-contract.md` for system-level orchestration, global/workspace alignment, expert-firepower, automation, or output-consistency repair
14. `semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md` when the user references Josh, Coach Cooz, source extraction wins, or "magic moments" as the quality bar

## Continuity Spine

Autopilot must preserve long-running measurable work instead of treating each
turn as a fresh recommendation. When the request starts, resumes, repairs, or
upgrades a system goal, attach or update a **Goal Packet** using
`semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md`.

The Goal Packet records the target, scope, criteria, permitted side effects,
proof artifact, measurable stop, turn cap, evaluator, wake-up check, human
checkpoint, and rollback/archive rule. `/goal` owns that packet for long-running
work, `/mission` owns governed multi-step execution, and `/end-session` captures
what fired, what passed, what failed, the next route, and the resume prompt.

Workspace state is the compact continuity spine for the run. When Autopilot
starts a meaningful goal, resumes a prior goal, changes the chosen route, or
finishes verification, update `.agent/intent-memory/current.json` and
`.agent/system-cohesion-state.json` through the helpers instead of editing the
state by hand.

```bash
python3 execution/intent_memory.py capture --goal "[active intent]" --deliverable "[outcome]" --mode "[mode]" --chosen-route "[route]" --support-gate "[gate]" --expert "[expert or none]" --next-move "[next move]"
python3 execution/intent_memory.py update --next-move "[next move]" --support-gate "[gate]" --next-verification "[verification command]"
python3 execution/intent_memory.py verify
python3 execution/system_cohesion_state.py update --intent-goal "[active intent]" --route "[route]" --support-gate "[gate]" --expert "[expert or none]" --activation "[activation queue item]" --verifier "[name=status]" --weekly-platter-status "[status]" --weekly-platter-path "[path]" --next-move "[next move]"
```

The shared state must stay small and current: active intent, chosen route,
support gates, expert stack, activation queue, verifier status, weekly platter,
and next move. If a field is unknown, record the honest next action rather than
manufacturing freshness.

## Routing Pass

Run the deterministic router stack before execution:

```bash
python3 execution/autopilot_runtime_preflight.py "[raw context]"
python3 execution/command_menu.py search "[raw context]"
python3 execution/workflow_router.py search "[raw context]"
python3 execution/routing_governor.py evaluate "[raw context]"
python3 execution/expert_router.py route "[raw context]"
python3 execution/expert_router.py compounds "[raw context]"
python3 execution/recommend_stack.py "[raw context]" --json
python3 execution/context_retriever.py search "[raw context]" --top 8
```

`execution/autopilot_runtime_preflight.py` is the canonical trace renderer. It
classifies the Execution Decision, outcome recipe, capability graph policy,
support gates, verifiers, Run Prompt, friction ledger hook, and run receipt
command.

If meta-intent is `operating-alignment`, `/system-audit` owns the run. Treat
`/virtuoso`, `/expert-composition-governor`, `/routing-intelligence`,
`/health-check`, `/repeatability-spine`, and `/self-evolve` as support gates,
not competing owners. The Autopilot Trace and Run Receipt should expose
`meta_intent`, `composition_owner`, support gates, subagent boundary, verifier
status, and feedback hook.

For complex, full-arsenal, subagent, cross-pollination, plugin/tool-blending, or
agent-elevation work, also run the Virtuoso composer:

```bash
python3 execution/virtuoso_orchestration.py "[raw context]" --json
```

Use `--delegate-intent` only when the user has asked for subagents, delegated
agents, parallel agents, or swarm-style work. Use `--log-routing` only after the
chosen route is actually used, so routing intelligence records real ensemble
evidence instead of decorative recommendations.

### Virtuoso Trace

When triggered, Autopilot output must include a compact **Virtuoso Trace**:

- **Route / Owner**: one primary route and one integration owner.
- **Stack**: one evidence-backed recommended stack or a skip reason.
- **Composition Ledger**: Spine, Differentiator, Mechanism, Craft, and Risk Gate.
- **Delegation**: selected subagent packets, activation boundary, and main-thread integration owner.
- **Plugin/tool surface**: tool clusters and operator-core/plugin readiness.
- **Routing evidence**: ensemble logging status and routing ID when logged.
- **Verification**: verifier plan plus first safe action.

## Intent Compiler

Every meaningful request becomes:

- predicted need
- flashlight center and edges
- goal
- outcome type
- audience/user
- success criteria
- constraints and risk gates
- chosen route
- support gates
- artifact shape
- verification commands
- next decision

For non-trivial work, the Intent Confidence Packet must also name:

- non-trivial reason
- confidence score
- unanswered execution-changing questions
- arsenal policy
- proof plan
- retrieval home
- pause/run decision

If unanswered questions remain, Autopilot may perform safe read-only discovery
but must pause before meaningful mutation or delivery.

The Co-Creative Launchpad Packet must be produced before the route is treated
as executable. Use
`semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`
and `execution/co_creative_launchpad.py` to surface predicted need, center,
edges, what good looks like, missing inputs, execution-changing questions,
route bias, pause/run decision, and handoff. Ask only when the answer changes
route, artifact, scope, risk, taste, or proof; otherwise state assumptions and
run.

Autopilot must pick one best route unless Farrice explicitly asks for options.
Use `/orchestrate` only for `--menu`, "show options", "rank paths", or a real
strategic fork.

## Capability Graph

Autopilot consults the live capability graph so Farrice does not have to hold
the command library in working memory.

```bash
python3 execution/capability_graph.py --json
python3 execution/harness_status.py --plain
python3 execution/outcome_recipes.py --list
```

The graph maps outcomes to workflows, skills, agents, support gates, verifiers,
and plugin readiness. Classifications are:

- `Use Now`
- `Harden`
- `Package Later`
- `Cold Reference`
- `Archive Candidate`

## Outcome Recipes

Use prebuilt recipes for common outcomes:

| Outcome | Primary Route | Required Gates |
|---|---|---|
| system repair | `/system-audit` | `/routing-intelligence`, `/health-check`, friction ledger |
| source-to-skill build | `/source-to-skill-system` | `/knowledge-librarian`, `/extraction-governor-agent` |
| plugin packaging | `/plugin-readiness-audit` | capability graph, fresh-thread proof |
| revenue sprint | `/first-10k` | `/revenue-offer-agent`, `/client-acquire`, `/publishable-copy-gate` |
| content package | `/content-media-agent` | `/high-taste-writing-os`, `/publishable-copy-gate`, `/excellence-gate` |
| research synthesis | `/research-intelligence-agent` | `/research-swarm`, `/deep-research-gemini`, `/ground-truth-agent` |
| client audit | `/client-delivery-agent` | `/research-intelligence-agent`, `/red-team-agent` |
| design/build | `/creative-design-agent` | `/quality-judge`, visual verification |
| mission continuation | `/mission` | mission handoff receipt, `/end-session` |
| repeatability repair | `/repeatability-spine` | preservation lock, regression guard |

## Excellence Gates

Attach gates by outcome type:

- Public/client/revenue copy: `/publishable-copy-gate`
- Broad strategy: `/red-team-agent` plus `/ground-truth-agent`
- Creative or taste-sensitive work: `/high-taste-writing-os` or `/excellence-gate`
- Source-to-system work: `/knowledge-librarian` plus `/extraction-governor-agent`
- Plugin packaging: `/plugin-readiness-audit`
- Failed revisions: `/repeatability-spine`

## Mission Package Continuation Rule

When a request continues, resumes, deploys, references, or repairs an active
mission or approved package, resolve mission context before choosing the final
route:

```bash
python3 execution/mission_control.py context "[mission-slug]"
```

Include a Mission Handoff Receipt naming the mission, approved package files
loaded, proof artifacts used, support gates, skipped package items, and preserved
boundaries.

## Friction Ledger

Every recurring extra pass, failed route, weak output, missing prompt, unclear
approval, stale recommendation, or verifier failure must be logged instead of
becoming a vague feeling that the system is broken.

```bash
python3 execution/friction_ledger.py log --kind failed-route --summary "[what happened]" --next-action "[repair route]"
python3 execution/friction_ledger.py report
python3 execution/friction_ledger.py verify
```

Recurring friction feeds `/self-evolve` or `/skill-anneal`.

## Delegation Readiness

Real Codex subagents are never implied by expert/persona selection. For
`--delegate`, "use subagents", or parallel-agent requests, run:

```bash
python3 execution/subagent_readiness.py --dry-run --json
python3 execution/verify_subagent_readiness.py
```

The main Codex thread remains the integration owner. Any real subagent work
needs a Delegation Receipt naming the worker, reason used, exact slice, context
read, accepted/rejected output, risk notes, and integration owner.

## Run Receipts

Every meaningful execution ends with a run receipt:

```bash
python3 execution/run_receipt.py --query "[raw context]" --route "[route]" --status "[Running now|Needs judgment|Blocked by risk|Plan only]" --changed "[what changed]" --passed "[checks]" --failed "[failures]" --judgment "[judgment needed]" --next-action "[next]"
python3 execution/run_receipt.py --verify
```

The receipt must include what ran, what changed, what passed, what failed, what
needs Farrice judgment, and what to run next.

## Plugin Packaging Ladder

Never recommend a plugin because a workflow sounds important. Use:

```bash
python3 execution/plugin_readiness_audit.py --stdout [candidate routes]
```

Packaging ladder:

1. helper/script
2. workflow
3. Codex skill wrapper
4. plugin candidate
5. plugin

No plugin recommendation until fresh-thread reliability, verifier coverage, and
repeated-use evidence exist.

## Output Schema

```markdown
# Autopilot: [Short Mission Name]

## Intent Lock
- **Goal interpreted as**:
- **Deliverable**:
- **Audience/User**:
- **Success criteria**:
- **Clarity Score**:
- **Confidence**:
- **Ambiguity Map**:
- **Clarifier**:

## Co-Creative Launchpad
- **Predicted need**:
- **Center**:
- **Edges**:
- **What good looks like**:
- **Missing inputs**:
- **Questions that change execution**:
- **Route bias**:
- **Pause or run**:
- **Handoff**:

## Autopilot Trace
- **Loaded**:
- **Candidates**:
- **Governor**:
- **Outcome Recipe**:
- **Recommended Stack**:
- **Owner**:
- **Support Gates**:
- **Skipped**:
- **Tool Routing**:
- **Context Sources**:
- **Mission Package**:
- **Composition**:
- **Copy Gate**:
- **Research Stack**:
- **Read-only checks performed**:
- **Verification planned**:

## Execution Decision
- **Status**: [Running now | Needs judgment | Blocked by risk | Plan only]
- **Safe local policy**:
- **Risk reasons**:
- **Approval needed**:
- **First action**:

## Chosen Path
- **Mode**:
- **Primary route**:
- **Owner**:
- **Recommended stack**:
- **Composition**:
- **Support gates**:
- **Why this path**:

When more than three experts, skills, workflows, or gates are plausible, the
Composition field must name `/expert-composition-governor` and
`expert-composition-contract.md` as the integration rule. If no multi-expert
composition is justified, say so explicitly instead of hiding the decision.

## Capability Graph
- **Outcome**:
- **Artifact**:
- **Plugin ladder**:
- **Refresh command**:

## Execution Plan
- **Step 1**:
- **Step 2**:
- **Step 3**:
- **Verification**:
- **Assumptions**:

## Run Prompt
```text
[copy-paste runnable prompt when blocked or useful]
```

## Run Receipt
- **Create**:
- **Verify**:

## 3 Next Prompts
1. **Use Now**
   - **When to use:** [condition that makes immediate continuation right]
   - **Why this is recommended:** [leverage or intent alignment]
   - **Prompt:** `[copy-paste continuation prompt]`
   - **Expected output:** [artifact/result]
   - **Quality bar:** [acceptance standard]
   - **Skip if:** [risk or distraction condition]
   - **Suggested skills/workflows:** [exact routes]
2. **Harden**
   - **When to use:** [condition that makes validation/repair right]
   - **Why this is recommended:** [risk reduced]
   - **Prompt:** `[copy-paste continuation prompt]`
   - **Expected output:** [proof/patch/report]
   - **Quality bar:** [trust standard]
   - **Skip if:** [overkill condition]
   - **Suggested skills/workflows:** [exact routes]
3. **Expand**
   - **When to use:** [condition that makes reusable expansion right]
   - **Why this is recommended:** [compounding upside]
   - **Prompt:** `[copy-paste continuation prompt]`
   - **Expected output:** [capability/artifact/workflow]
   - **Quality bar:** [keep-or-kill standard]
   - **Skip if:** [focus risk]
   - **Suggested skills/workflows:** [exact routes]

## Friction Ledger
- **Log if needed**:
- **Verify**:

## Approval/Risk Gate
- **Status**:
- **Approval needed**:
- **Boundary**:

## Operator Lesson
- **What I noticed**:
- **Better system move**:
- **Next-time prompt**:
- **Agent/Workflow I'd use**:
- **Subagent worth it?**:
- **Reuse hook**:
```

## State Snapshot

After completing the run, update `.agent/autopilot-state.md` with only:

- date
- session title or short label
- raw goal summary
- clarity score
- mode selected
- primary route
- gates used
- execution decision
- verifiers run
- outcome or next action

Also update intent memory and cohesion state when the active intent, chosen
route, support gates, expert stack, verifier status, or next move changes.

## Quality Gate

Before final delivery, confirm:

- Intent Lock reduced ambiguity.
- Autopilot chose one route unless options were requested.
- Execution Decision is correct.
- Safe local work ran after trace when allowed.
- Risky work blocked with a Run Prompt.
- `--plan` and `--menu` stopped before execution.
- Required gates fired by outcome type.
- Capability graph, friction ledger, and run receipt hooks were present.
- Verification commands were run or named with an honest blocker.
- No global mirror, Google Antigravity edit, publishing, paid tool, destructive
  cleanup, or real subagent run happened without explicit approval.
