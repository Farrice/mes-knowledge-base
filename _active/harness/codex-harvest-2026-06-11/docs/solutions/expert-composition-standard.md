# Expert Composition Standard

Use this pattern when a task needs many experts, skills, workflows, or gates and the output risks becoming expert soup.

## Problem

Large expert libraries fail when the system treats expertise as additive decoration. It names many experts, applies broad passes, and then delivers an output that is patched together, overconfident, or still generic.

The real failure is missing composition.

## Working Solution

Use one owner and bounded specialists.

1. Lock the real outcome.
2. Pick one function owner.
3. Assign experts to contribution slots.
4. Limit each specialist to diagnosis, top changes, affected lines/sections, preservation notes, and risk.
5. Let the owner integrate the result into one voice, artifact, or workflow.
6. Include a Composition Ledger showing what changed and which experts were skipped.

## Operating Standard

The standard is:

```text
One owner, bounded experts, explicit handoffs.
```

When the system sees more than three plausible experts, skills, workflows, or gates, it should not load everything and hope the output improves. It should first route through `/expert-composition-governor`.

## Contribution Slots

| Slot | Job |
|---|---|
| Spine | Owns the core structure or strategy. |
| Differentiator | Makes the output non-obvious or ownable. |
| Mechanism | Proves, operationalizes, or explains how it works. |
| Craft | Improves taste, usability, prose, design, or polish. |
| Risk Gate | Protects truth, trust, safety, conversion, or delivery quality. |

## Prevention Rule

Expert count is not quality. A multi-expert output is not complete until it has one owner, slot decisions, skipped-expert reasons, and evidence of integration.

## Routing Rule

Use `/expert-composition-governor` when the user says expert soup, too many agents, full arsenal, true end-to-end access, not interwoven, hammer instead of scalpel, or when more than three experts/skills are plausible.

## Verification

Run:

```bash
python3 execution/verify_expert_composition_standard.py
```

The verifier checks the primitive, route, Codex skill bridge, source command, CODEX integration, Autopilot/Mission/Orchestrate integration, routing governor, and representative route queries.
