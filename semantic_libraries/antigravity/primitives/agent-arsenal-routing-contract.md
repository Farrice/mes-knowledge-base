# Agent Arsenal Routing Contract

## Purpose

Use this contract whenever an Antigravity agent, operator workflow, or expert
persona chooses how to answer a task. The goal is one coordinated expert brain:
router-first, stack-aware, quality-gated, traceable, and still lightweight.

This prevents two failures:

- fixed "go-to workflow" menus that hide the rest of the arsenal
- broad expert soup where too many people are invoked without a compounding reason

When more than three experts, skills, workflows, or gates are plausible, apply
`semantic_libraries/antigravity/primitives/expert-composition-contract.md`
before finalizing the route. Routing finds candidates; composition decides how
they work together.

## Core Rules

1. **Route before committing**: Run local routing before treating any workflow,
   expert, skill, or gate as the answer.
2. **Seed lists are not constraints**: Agent workflow lists are starting maps.
   They never override router results, stacking evidence, or objective fit.
3. **Stack only when it compounds**: Use pairings when the second expert changes
   the output, catches a known blind spot, or supplies a missing mechanism.
   If the stack crosses three or more experts, assign contribution slots through
   `/expert-composition-governor`.
4. **Keep the hot/cold boundary**: Do not preload the whole library. Load only
   the selected workflow, expert, skill, context chunk, gate, or handoff.
5. **Show the route**: User-facing agent outputs should expose enough of the
   routing decision to make the choice trustworthy.
6. **Respect subagent approval**: Real Codex subagents require explicit user authorization for delegation, parallel agents, or subagents.
7. **Use gates on risk**: Attach research, ground truth, red team, excellence,
   publishable-copy, or evolution gates when stakes justify them.
8. **Compose before presenting**: Multi-expert outputs need one owner, bounded
   specialist passes, and a Composition Ledger when stakes are high or the user
   has already flagged expert soup.

## Required Router Pass

For operator agents, run or emulate this local lookup before choosing the path:

```bash
python3 execution/command_menu.py search "[goal/context]"
python3 execution/workflow_router.py search "[goal/context]"
python3 execution/expert_router.py route "[goal/context]"
python3 execution/expert_router.py compounds "[goal/context]"
python3 execution/context_retriever.py search "[goal/context]" --top 8
python3 execution/tool_router.py route "[goal/context]"
```

Expert/persona agents do not become control-plane operators. They use the same
evidence when deciding whether to answer directly, pair with another expert, or
hand off to an operator.

## Stacking Evidence

Prefer pairings supported by at least one of these sources:

- `execution/expert_router.py` compound combinations
- skill `Stacking Guide`, `Skill Stacking`, `Cross-Expert Stacking`, or
  `Pairs With` sections
- `/extract-forge` tier-3 stacking workflow rules
- routing-intelligence ensemble feedback
- cascade/downstream relationships from `execution/cascade_detector.py`

Evidence-weighted stacking order:

1. Trigger-matched compound pairing with a clear effect
2. Skill-declared stacking guide that names the partner and use case
3. Positive routing-intelligence ensemble feedback
4. Shared reference, same-expert, or downstream cascade relationship
5. Operator judgment, used sparingly and named as an inference

## Visible Routing Trace

When an operator agent returns a path, include these fields unless the answer is
tiny or the user requested only the direct answer:

```markdown
## Routing Trace
- **Objective**:
- **Router candidates**:
- **Seed workflows considered**:
- **Stacking candidates**:
- **Composition**: [single owner, contribution slots, or `/expert-composition-governor` skip reason]
- **Chosen route**:
- **Gates**:
- **Skipped and why**:
- **Verification**:
- **First action**:
```

## Operator Agent Standard

Operator agents own a function. They may route into workflows, skills, experts,
context, tools, quality gates, or approved subagents, but they should not trap
the task inside their seed workflow list.

Required operator sections:

- `## Dynamic Routing Protocol`
- `## Seed Workflows`
- `## Stacking Candidates`
- `## Routing Interop`
- a visible routing trace in the output schema

## Expert Persona Standard

Expert/persona agents are expertise contexts, not control planes. Each agent
should include `## Routing Interop` explaining:

- when this expert should activate
- when this expert should pair with another skill or expert
- when the work should hand off to an operator agent
- when quality, research, red team, mission, or evolution support is required

## Copywriting Exemplar

The Copywriting Agent is the exemplar for this migration. It should route beyond
its old copy menu into offer, buyer-belief, proof, story, VSL, LinkedIn,
research, design, and publishable-copy paths based on the actual objective.

`/publishable-copy-gate` remains mandatory only when the copy is public,
revenue-critical, publishable, outreach, checkout, marketplace, or client-facing.

## Validation

Run:

```bash
python3 execution/verify_expert_composition_standard.py
python3 execution/agent_arsenal_router_audit.py --plan-only --operators --all-agents
python3 execution/generate_agent_stacking_registry.py
python3 execution/verify_agent_arsenal_routing.py
```

Then run the control-plane proof set from `CODEX.md`.

## Last Updated

2026-05-10
