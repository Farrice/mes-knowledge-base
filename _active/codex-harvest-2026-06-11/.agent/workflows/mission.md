---
description: Mission OS - plan, validate, execute, and govern long-running agent work
---

# /mission - Mission OS

Run a Factory-inspired but Codex-native mission layer for client-facing, personal, research, and build work.

This workflow is additive. It does not replace the existing router, command menu, expert library, Chain, JCC scale commands, or Codex subagent rules. It wraps them in a stricter planning and validation contract so long-running work does not drift.

Mission is a backend governance mode for `/autopilot`. Use it directly when Farrice explicitly asks for mission control; otherwise let `/autopilot` select Mission Mode only when persistent state, validation contracts, handoffs, reusable knowledge, client-facing stakes, or multi-milestone execution are actually needed.

## Usage

```bash
/mission [objective]
/mission status [mission-slug]
/mission list
/mission resume [mission-slug]
/autopilot --mission [objective]
```

Aliases to recognize in conversation: mission, missions, mission control, mission mode, enter mission.

## Pre-Flight Reads

1. `CODEX.md`
2. `.agent/session-state.md` if present
3. `.agent/intent-memory/current.json` if present
4. `.agent/system-cohesion-state.json` if present
5. `semantic_libraries/antigravity/primitives/skill-system-contract.md` when the mission changes skills, workflows, routing, orchestration, or OS structure
6. `semantic_libraries/antigravity/primitives/expert-composition-contract.md` when the mission involves many experts, skills, agents, workflows, or gates
7. `agents/extraction-governor-agent/AGENT.md` when the source or capability boundary is unclear
8. `agents/knowledge-librarian/AGENT.md` when the mission may use, create, overlap, or update reusable knowledge
9. `skills/nate-b-jones-orchestration-intelligence/SKILL.md`
10. `skills/nate-b-jones-orchestration-intelligence/genius.md`

## Routing Stack

Run targeted routing before drafting the mission plan:

```bash
python3 execution/command_menu.py search "[objective]"
python3 execution/workflow_router.py search "[objective]"
python3 execution/expert_router.py route "[objective]"
python3 execution/expert_router.py compounds "[objective]"
python3 execution/context_retriever.py search "[objective]" --top 8
```

Run the Knowledge Librarian pulse when any of these are true:

- The mission starts from a book, video, article, transcript, course, prompt, framework, or expert source.
- The mission may create a new skill, workflow, agent, command bridge, client asset, or reusable SOP.
- The mission may create a skill system, orchestrator workflow, hot/cold routing policy, or source-to-skill capability.
- The mission may overlap with existing knowledge.
- Farrice is unsure what existing capability to use.
- The output should become part of the library rather than stay as a one-off answer.

```bash
python3 execution/knowledge_compiler.py stats
python3 execution/knowledge_compiler.py briefing
python3 execution/knowledge_compiler.py solutions "[objective]" --top 8
python3 execution/command_menu.py search "[objective]"
python3 execution/workflow_router.py search "[objective]"
python3 execution/expert_router.py route "[objective]"
python3 execution/context_retriever.py search "[objective]" --top 10
```

If the librarian pulse finds overlap, the mission charter must include a **Library Decision**:

- deploy existing asset,
- extend existing asset,
- create companion asset,
- create new standalone asset,
- mark as reference only,
- schedule cleanup later.

If `docs/solutions/` contains a relevant reusable solution, the Library Decision must name the path and state one of:

- apply directly,
- adapt into this mission's plan,
- ignore with reason,
- promote a new solution after completion.

Use `execution/mission_control.py` for local mission state:

```bash
python3 execution/mission_control.py create --name "[mission name]" --goal "[objective]" --mode client --librarian-required
python3 execution/mission_control.py create --name "[engineering mission]" --goal "[objective]" --mode code --librarian-required --artifact-contract engineering
python3 execution/mission_control.py status "[mission-slug]"
python3 execution/mission_control.py list
python3 execution/mission_control.py resume "[mission-slug]"
python3 execution/mission_control.py context "[mission-slug]"
python3 execution/mission_control.py add-assertion "[mission-slug]" --id VA1 --statement "..." --covered-by "A1" --validator "..." --pass-signal "..."
python3 execution/mission_control.py add-activation "[mission-slug]" --id A1 --owner "..." --workflow "..." --expected-artifact "..." --validation-assertion VA1
python3 execution/mission_control.py set-activation "[mission-slug]" --id A1 --status complete --evidence-path "..."
python3 execution/mission_control.py set-resume-packet "[mission-slug]" --fresh-session-packet "..." --next-command "..." --required
python3 execution/mission_control.py add-handoff "[mission-slug]" --role worker --summary "..." --commands "..." --issues "..." --next "..."
python3 execution/mission_control.py mark-librarian "[mission-slug]" --status complete --notes "..."
python3 execution/mission_control.py validate "[mission-slug]"
```

Mission state writes must be serialized. Do not run `add-handoff`, `mark-librarian`, or `set-status` at the same time for the same mission.

Mission also participates in the workspace-local intent memory and shared
cohesion spine. When a mission starts, resumes, changes route, records a
handoff, or finishes verification, update `.agent/intent-memory/current.json`
and `.agent/system-cohesion-state.json` so Autopilot, Mission, and validators
share one compact operating picture.

```bash
python3 execution/intent_memory.py capture --goal "[active intent]" --deliverable "[mission output]" --mode "Mission Mode" --chosen-route "mission" --mission-slug "[mission-slug]" --mission-state-path ".agent/missions/[mission-slug]/mission.json" --mission-status "[planned/active/validating/complete]" --support-gate "[gate]" --expert "[expert or none]" --next-move "[next move]"
python3 execution/intent_memory.py update --mission-slug "[mission-slug]" --mission-status "[status]" --next-move "[next move]"
python3 execution/intent_memory.py verify
python3 execution/system_cohesion_state.py update --intent-goal "[active intent]" --mission-slug "[mission-slug]" --mission-status "[status]" --route "mission" --support-gate "[gate]" --expert "[expert or none]" --activation "[activation queue item]" --verifier "[name=status]" --weekly-platter-status "[status]" --next-move "[next move]"
```

The cohesion state must track active intent, mission, chosen route, support gates, expert stack, activation queue, verifier status, weekly platter, and next move. Keep it compact; it is a resume and validation spine, not a second mission brief.

## Engineering Artifact Contract

For code, product, system, workflow, automation, or reusable operating-system missions, use the CE-inspired but Antigravity-native engineering artifact contract:

```bash
python3 execution/mission_control.py create --name "[mission name]" --goal "[objective]" --mode code --librarian-required --artifact-contract engineering
```

This does not replace Mission OS, the routers, Knowledge Librarian, Chain, or command bridge. It gives Mission OS a stricter durable artifact layer so software work can compound across sessions.

### Contract Artifacts

| Artifact | Path | Use |
|---|---|---|
| Strategy anchor | `docs/mission-artifacts/<slug>/strategy-anchor.md` | Tie the mission to the root strategy or a mission-local guiding bet before requirements drift. |
| Requirements | `docs/mission-artifacts/<slug>/requirements.md` | Capture stable requirement, actor, flow, and acceptance example IDs (`R1`, `A1`, `F1`, `AE1`). |
| Unit plan | `docs/mission-artifacts/<slug>/plan.md` | Break implementation into stable `U-ID` units. Never renumber old U-IDs after splits, deletions, or reordering. |
| Review ledger | `docs/mission-artifacts/<slug>/review.md` | Record scrutiny findings, user-outcome review, residual work, and acceptance decisions. |
| Solution capture | `docs/mission-artifacts/<slug>/solution-capture.md` | Capture solved problems while context is fresh; promote generalizable learnings to `docs/solutions/`. |
| Pulse | `docs/mission-artifacts/<slug>/pulse.md` | Record post-ship, post-delivery, or post-experiment signals; promote durable reports to `docs/pulse-reports/`. |

Use the contract when any of these are true:

- the mission changes code, workflows, routers, commands, skills, or operating infrastructure
- the work will likely resume across sessions
- another agent should be able to continue without chat history
- the mission creates a reusable lesson, fix pattern, or product signal
- the user asks to adapt, enhance, integrate, harden, or elevate the system

Skip the contract for tiny one-off edits, pure conversational advice, or outputs that do not need durable handoff.

## Operating Model

### 1. Mission Charter

Before execution, produce a charter with:

- Mission name
- Goal and audience
- Constraints and non-goals
- Existing assets to use
- Library Decision when the Knowledge Librarian fires
- Relevant `docs/solutions/` entries and reuse decision
- Artifact Contract when the work is engineering, product, system, workflow, automation, or reusable OS work
- Skill System Contract when the mission wires multiple components into an end-to-end system
- Expert Composition Contract when the mission risks expert soup or needs many experts to become one coherent output
- Features or workstreams
- Milestones
- Subject-agent roster
- Validation contract
- Budget, time, and approval constraints
- State path under `.agent/missions/[slug]/`

If the user gave a vague objective, sharpen with the smallest useful question set. If the user said to implement, do not over-ask; make conservative assumptions and proceed.

### 2. Validation Contract Comes First

Define correctness before execution begins.

For code or product work, include machine checks and behavior checks. For strategy, creative, client work, or personal systems, include expert sniff-checks with concrete acceptance criteria.

Each feature or workstream must point to at least one assertion in the validation contract. Unassigned assertions mean the plan is incomplete.

For engineering-contract missions, each `U-ID` in `docs/mission-artifacts/<slug>/plan.md` must point to at least one requirement or acceptance example, and each validation assertion must name the `U-ID` or artifact it covers.

### 3. Roles

Use three role classes:

- **Orchestrator**: owns scope, plan, state, routing, approvals, and milestone decisions.
- **Worker**: owns one feature or workstream at a time with clean context and a narrow output contract.
- **Validator**: reviews against the validation contract with fresh context.

Workers should be subject agents, not generic helpers. Select them from `agents/`, `skills/`, and workflow routing. If a needed subject agent does not exist, define the temporary role in the mission charter and log the gap.

Knowledge Librarian is not a generic worker. It is the library intelligence checkpoint. Use it before creating new system assets and again at the end of source-to-system missions to make sure the new work is discoverable and not shelfware.

### 4. Activation Queue And Execution Pattern

After the charter, execute all local, non-external, non-destructive workstreams by default. Mission may pause only for publishing, outreach, destructive edits, paid tools, external sharing, changes outside `/Users/farricecain/Codex Antigravity`, or an explicit approval checkpoint requested by Farrice.

Before or during execution, create a **Mission Activation Queue** in mission state. Each activation item must record:

- ID
- owner
- workflow or skill
- expected artifact
- status
- evidence path
- validation assertion
- blocker
- next action

The queue is the difference between "we planned the experts" and "the lanes actually fired." If a lane is skipped or blocked, record why. If a lane completes, record the proof artifact.

Default to serial write execution with targeted read-only parallelism.

- Only one writer edits the same code or artifact surface at a time.
- Parallelize discovery, source review, option generation, and independent validation when useful.
- Do not spawn Codex subagents unless the user explicitly asks for parallel agents or delegated agent work.
- When native subagents are not allowed or not needed, execute the subject-agent protocol locally by reading the relevant `AGENT.md` and skills.

### 5. Handoff Discipline

Every worker or local role pass must produce a structured handoff:

```markdown
## Handoff
- Mission:
- Role:
- Scope owned:
- Completed:
- Left undone:
- Files changed:
- Commands run:
- Exit codes or verification result:
- Issues found:
- Follow-up recommended:
- Contract assertions satisfied:
- Artifact contract updates:
```

Use `execution/mission_control.py add-handoff` to persist the compact state when the mission spans multiple steps or risks losing context.

### 6. Validators

Run two validator lenses at milestone boundaries:

- **Scrutiny validator**: tests, lint, type checks, artifact guard, code review, source verification.
- **User-outcome validator**: checks whether the work behaves or reads like the intended user/client experience, not merely whether files exist.

For frontend or app work, use browser testing or screenshots when practical. For source extraction, run registry validation and router discoverability checks. For strategic artifacts, run adversarial review or excellence gate.

For engineering-contract missions, also verify that:

- `requirements.md` contains the current requirement and acceptance IDs.
- `plan.md` preserves stable `U-ID` references and maps units to checks.
- `review.md` records the final scrutiny and user-outcome decision.
- `solution-capture.md` either promotes the learning to `docs/solutions/` or explicitly keeps it mission-local.
- `pulse.md` is filled when the work ships, is delivered, or generates operational signal.
- mission state contains validation assertions, activation evidence, execution receipt, and a fresh-session resume packet when the work needs cross-session continuity.

### 7. Fresh-Session Resume Packet

For deployment-style, client-facing, revenue, launch, or daily-operator missions, create a fresh-session packet before final closeout. It must name:

- the recommended session title
- source-of-truth paths
- next command
- approval boundaries
- which expert/workflow lanes must run or be locally simulated
- proof/gate requirements

Run `/mission resume [slug]` before closeout. If `.agent/session-state.md` conflicts with newer `.agent/intent-memory/current.json` or `.agent/system-cohesion-state.json`, prefer the newer structured state and warn that the session anchor is stale.

For missions that create approved packages, also run
`python3 execution/mission_control.py context [slug]` before closeout and in
fresh sessions. The context output is the operational package handoff: approved
load set, activation evidence, proof artifacts, support gates, expert stack,
handoff decisions, and package boundaries. Downstream workflows must include a
Mission Handoff Receipt before drafting or choosing execution.

### 8. Intervention Rules

Pause and re-plan when:

- A validation assertion is uncovered.
- A worker handoff reports unresolved blocking issues.
- Two retries fail on the same milestone.
- The mission scope expands beyond the charter.
- The task requires publishing, outreach, destructive edits, paid tools, or changes outside `/Users/farricecain/Codex Antigravity`.

## Output Schema

```markdown
# Mission: [Name]

## Mission Charter
- Goal:
- Audience:
- Constraints:
- Non-goals:
- Library Decision:
- Artifact Contract:
- State path:

## Plan
- Features/workstreams:
- Milestones:
- Subject agents:
- Command/workflow order:
- Librarian checkpoint:
- Artifact paths:

## Validation Contract
| Assertion | Covered by | Validator | Pass signal |
|---|---|---|---|

## Execution
[Execute all safe local workstreams now. Pause only for publishing, outreach, destructive edits, paid tools, external sharing, or explicit approval boundaries.]

## Mission Activation Queue
| ID | Owner | Workflow/Skill | Status | Expected Artifact | Evidence Path | Assertion | Blocker | Next Action |
|---|---|---|---|---|---|---|---|---|

## Execution Receipt
- Planned lanes:
- Executed lanes:
- Skipped or blocked lanes:
- Proof artifacts:
- Validators run:
- Resume command:

## Fresh Session Packet
- Source paths:
- Next command:
- Approval boundaries:
- State sources:

## Mission Control
- Current state:
- Next decision:
- Next command:
```

## Factory Missions Lessons Adopted

- Collaborative plan before execution.
- Features grouped into milestones.
- Validation contract before implementation.
- Worker and validator separation.
- Structured handoffs.
- Shared mission state.
- Serial writes with targeted read-only parallelism.
- Project-manager style human intervention.

## Compound Engineering Lessons Adapted

- Strategy and requirements become durable artifacts before execution.
- Implementation plans use stable unit IDs so later reviews and handoffs can refer to exact work units.
- Reviews produce a ledger, not only a final opinion.
- Fresh solved problems are captured immediately and promoted only when reusable.
- Product or workflow signals get a pulse report instead of disappearing into chat.

## Factory Missions Lessons Not Adopted Blindly

- No hard dependency on Factory, Droid, or `/enter-mission`.
- No broad parallel write swarm by default.
- No hidden state outside the Codex Antigravity workspace.
- No generic subagent spawning when a local subject-agent protocol is enough.
- No replacement of the existing Antigravity Chain, routers, registries, or command bridge.
- No wholesale Compound Engineering plugin install or duplicate command surface by default.

## Quality Gate

Before final output, score:

- Intent alignment: 1-10
- Harness completeness: 1-10
- Validation strength: 1-10
- Handoff clarity: 1-10

Any score below 7 means revise before delivery.
