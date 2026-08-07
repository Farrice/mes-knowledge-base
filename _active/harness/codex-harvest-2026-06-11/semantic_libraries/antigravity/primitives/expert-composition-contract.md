# Expert Composition Contract

Use this primitive whenever a task could benefit from multiple experts, skills, workflows, agents, or gates.

## Purpose

Prevent expert soup while preserving the full power of the Antigravity arsenal.

Expert soup happens when many experts are named or invoked but no single owner composes their contributions into one coherent output. The result is often structurally correct but patched together, over-scored, generic, or hard for the user to trust.

## Core Rule

One owner, bounded experts, explicit handoffs.

Every multi-expert task must have:

- one function owner,
- one integration owner,
- a small number of specialist passes,
- a handoff contract for each specialist,
- a Composition Ledger proving what each expert changed,
- a final output that reads or behaves as one system, not a pile of frameworks.

## Expert Soup Signals

Trigger this contract when any of these appear:

- More than three experts or skills are being considered.
- Experts are listed but their exact contribution is unclear.
- The output says "applied X, Y, Z" but does not show changed lines, decisions, or artifacts.
- The work is correct but not elegant, interwoven, or high-quality.
- Multiple commands could apply and the router gives adjacent but not decisive routes.
- The user says "expert soup," "too many agents," "not interwoven," "hammer instead of scalpel," "true end-to-end access," or "use the full arsenal."
- The task crosses functions: strategy plus copy plus design plus research plus delivery.

## Composition Process

### 1. Intent And Outcome Lock

State the actual job in one sentence:

```text
The output must help [audience] do/feel/decide [outcome] under [constraints].
```

Do not choose experts until this is clear.

### 2. Function Owner

Pick one owner by output type:

| Output Type | Function Owner |
|---|---|
| Writing, essays, narrative, voice | Writing Agent |
| Public/revenue copy | Copywriting Agent |
| Content/media package | Content & Media Agent |
| Offer or monetization | Revenue Offer Agent |
| Positioning or messaging | Messaging Positioning Agent |
| Research or source truth | Research Intelligence Agent |
| Client delivery, audit, SOP | Client Delivery Agent |
| System/workflow/OS change | Mission / System Audit / Evolution |
| Visual/product/design | Creative Design Agent |

If no owner is obvious, route through `/orchestrate` or `/autopilot` first.

### 3. Contribution Slots

Assign experts to slots, not prestige roles.

| Slot | Question | Max Count |
|---|---|---:|
| Spine | What owns the structure? | 1 |
| Differentiator | What makes this non-obvious or ownable? | 1 |
| Mechanism | What proves or operationalizes the idea? | 1 |
| Craft | What improves quality, taste, or usability? | 1 |
| Risk Gate | What can break trust, accuracy, or conversion? | 1 |

If two experts want the same slot, choose one and skip the other with a reason.

### 4. Specialist Handoff

Each specialist may return only:

- diagnosis,
- top 1-3 changes,
- exact artifact, line, section, or decision affected,
- what must be preserved,
- downstream risk.

They do not rewrite the whole output unless they are the function owner.

### 5. Integration Pass

The integration owner composes the output in one voice or one system design.

Integration rules:

- Preserve the spine.
- Accept only changes that improve the outcome.
- Remove duplicated expert logic.
- Translate specialist language into user-facing language.
- Keep the result legible to the target user.

### 6. Composition Ledger

Every high-stakes multi-expert deliverable must include this compact ledger:

```markdown
## Composition Ledger
| Slot | Expert/Asset | Contribution Accepted | Evidence Of Change | Skipped/Rejected |
|---|---|---|---|---|
| Spine | [owner] | [decision] | [line/artifact/section] | [none/reason] |
| Differentiator | [expert] | [decision] | [line/artifact/section] | [none/reason] |
| Mechanism | [expert] | [decision] | [line/artifact/section] | [none/reason] |
| Craft | [expert] | [decision] | [line/artifact/section] | [none/reason] |
| Risk Gate | [expert] | [decision] | [line/artifact/section] | [none/reason] |

**Owner:** [function owner]
**Integration rule:** [why this order]
**Expert soup check:** PASS / REVISE / REWORK
**Skipped experts:** [name + why]
```

## Score Discipline

Do not award quality from expert count.

Quality can only be raised by:

- a better decision,
- a better artifact,
- a clearer mechanism,
- a stronger line,
- a safer claim,
- a tighter workflow,
- a verified route,
- user or market calibration.

## Relationship To Other Contracts

| Contract | Relationship |
|---|---|
| Skill System Contract | Use when the composition becomes a repeatable OS or workflow. |
| Agent Arsenal Routing Contract | Use before composition to find candidates and stacking evidence. |
| High-Taste Writing OS | Domain-specific implementation for writing/copy/content quality. |
| Publishable Copy Gate | Runs after composition when the output is public or revenue-facing. |
| Mission OS | Governance layer for persistent, multi-milestone, or system-changing composition. |

## Fail Conditions

Revise before final if:

- no function owner is named,
- experts overlap without slot decisions,
- more than five experts are active without a special reason,
- the final output sounds stitched together,
- the ledger only names experts but not changed evidence,
- router results are ignored without explanation,
- the user has to manually infer why each expert was used.

## Validation

Run:

```bash
python3 execution/verify_expert_composition_standard.py
python3 execution/verify_agent_arsenal_routing.py
python3 execution/verify_autopilot_routing.py
```

For domain-specific outputs, also run the relevant artifact, prose, research, or copy guards.
