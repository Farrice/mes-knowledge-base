# Factory Missions vs Codex Antigravity Mission OS

## Bottom Line

Factory's Missions pattern is useful and worth adopting structurally, but not by replacing the Codex Antigravity system.

The right move is a Codex-native Mission OS: keep the existing Antigravity routers, command bridge, Chain, expert library, skills, workflow menu, and validation scripts, then add a `/mission` control layer that enforces planning, validation contracts, subject-agent routing, structured handoffs, and milestone state.

## What The Video Contributes

The source model has eight ideas worth preserving:

1. Mission-level entrypoint instead of ad hoc prompting.
2. Collaborative planning before execution.
3. Features grouped into milestones.
4. Validation contract written before implementation.
5. Orchestrator, worker, and validator role separation.
6. Structured handoffs after every worker pass.
7. Shared mission state so context is not lost.
8. Serial write execution with targeted read-only parallelism.

The strongest lesson is not "spawn more agents." The strongest lesson is "make the harness stricter before letting agents run longer."

## What We Already Had

Codex Antigravity already had much of the substrate:

| Factory Missions idea | Existing Codex Antigravity equivalent |
|---|---|
| Slash entrypoint | `.claude/commands/`, `.agent/workflows/`, `.agents/skills/source-command-*` |
| Orchestrator | Chain + `execution/*_router.py` + JCC workflows |
| Subject agents | `agents/*/AGENT.md` and expert skill library |
| Planning/decomposition | `/orchestration-blueprint`, `/campaign`, `/jcc-deploy`, Nate B. Jones DPVI |
| Routing | `command_menu.py`, `workflow_router.py`, `expert_router.py`, `context_retriever.py` |
| Validation | `chain_runner.py finalize`, `validate_skill.py`, artifact guard, tests, red-team workflows |
| Persistent state | `.agent/session-state.md`, now `.agent/missions/*` |

So the video is not a different universe. It is a clearer productized interface around patterns we were already assembling.

## What Was Missing

Three gaps mattered:

1. No clean `/mission` command that makes this the default operating surface.
2. No local mission state helper dedicated to mission charters, handoffs, and status.
3. No explicit rule that validation contracts must be written before execution and mapped to milestones.

Those are now addressed by the new `/mission` bridge and `execution/mission_control.py`.

## What We Should Not Copy Blindly

- Do not turn every job into a multi-agent swarm.
- Do not run broad parallel writers across the same artifact or code surface.
- Do not depend on Factory/Droid-specific runtime features.
- Do not bypass Codex's explicit subagent rule.
- Do not let the mission layer replace the existing router stack.
- Do not treat "subject agent" as a label only; it needs loaded `AGENT.md`, skill context, acceptance criteria, and a handoff contract.

## Recommended Adoption

Use `/mission` as the top-level command when the work is:

- client-facing and multi-deliverable,
- personal but important enough to track over days,
- a source-to-system build,
- a code/app change with multiple milestones,
- a business build with research, strategy, artifacts, and validation,
- any task where losing context would be expensive.

Use the existing smaller commands when the work is narrow. `/mission` should govern complex work, not add ceremony to simple work.

## New Command Surface

Use:

```bash
/mission [objective]
```

Behind the scenes this now maps to:

- `.agent/workflows/mission.md`
- `.claude/commands/mission.md`
- `.agents/skills/source-command-mission/SKILL.md`
- `execution/mission_control.py`

The mission helper can create, list, inspect, update, validate, and append handoffs for local mission state under `.agent/missions/`.

## Highest-Leverage Use Cases

1. Client delivery missions: discovery, diagnosis, strategy, asset build, QA, implementation plan, client handoff.
2. Personal operating missions: weekly planning, health/admin systems, learning sprints, content engine setup.
3. Source-to-system missions: YouTube/book/transcript into skill, workflows, command bridge, registry, validation, activation guide.
4. Productized service missions: offer, ICP, proof asset, outreach list, fulfillment SOP, delivery package.
5. Codebase modernization missions: audit, spec, feature milestones, serial implementation, validators, regression checks.
6. Research missions: source map, evidence extraction, synthesis, adversarial review, artifact package.

## Recommended First-Day Workflow

1. Run `/mission [objective]`.
2. Let the orchestrator build the charter, milestones, subject-agent roster, and validation contract.
3. Approve or adjust the plan.
4. Execute one milestone at a time.
5. Require every worker pass to produce a handoff.
6. Run scrutiny and user-outcome validation at milestone boundaries.
7. Use `/aar` after completion to capture reusable lessons.

## Verdict

Adopt the pattern, not the platform dependency.

Factory's approach is production-informed and matches the direction of serious agent systems: planning, validation, state, role separation, and traceable handoffs. Codex Antigravity already had the raw materials. The new `/mission` layer turns those materials into a cleaner operating surface without breaking the current system.
