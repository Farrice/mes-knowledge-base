---
name: reference-led-creative-system
description: "Turn Refero research and an existing brand or product context into three visibly inspectable visual directions, one reference lock, production assets, and a regression-safe replay path. Use for visual direction, taste exploration, landing pages, brand modes, campaigns, social assets, presentations, product surfaces, or any request to repeat the Performance Evidence Journal process without copying its style."
---

# Reference-Led Creative System

This is the reusable front door for the process that produced the Performance Evidence Journal. It preserves the method, not the journal aesthetic.

Runtime sequence:

`EXPLORE → SEE → CHOOSE → LOCK → APPLY → AUDIT`

## Ownership

- **Taste research owner:** the installed Refero `refero-design` skill and live Refero MCP styles/screens/flows.
- **Identity owner:** the user's existing brand or design system. Never create a parallel identity when one already exists.
- **Sequence owner:** this skill.
- **Optional media owner:** `/generate`, only when the reference lock requires generated bitmap media.
- **Preservation owner:** `/repeatability-spine` for golden examples, failed revisions, and replay guards.
- **Human taste owner:** Farrice or the explicitly named reviewer.

This skill does not replace Refero, Premium Minimal, `/generate`, a product design system, or a craft specialist. It wires them into one inspectable experience.

## Use When

- the user wants three unmistakably different visual directions;
- strong creative work must be repeated without losing its magic;
- Refero research should become visible options, a chosen lock, and production assets;
- a remote preview, mood board, or generated option may not display reliably;
- an existing direction must be applied to a new asset without visual drift;
- a revision must be audited against the reference lock and good example.

## Modes

| Mode | Use | Required result |
|---|---|---|
| `EXPLORE` | Several plausible territories exist | Three distinct directions, individual local previews, contact sheet, recommendation |
| `LOCK` | One direction is chosen or the user says to use the verdict | Reference lock, decision ledger, build target, explicit rejects |
| `APPLY` | A locked direction needs a production surface | Built asset plus visual QA and drift report |
| `AUDIT` | A revision feels weaker or the magic may be lost | Good-vs-current delta, preservation lock, nearest reversible repair |

## Required Reads

1. `references/skill-system-contract.md`
2. `references/visible-choice-contract.md`
3. `references/preservation-lock.md`
4. `references/golden-run-performance-evidence-journal.md` when the user invokes the journal example, lost magic, or repeatability
5. Installed Refero skill: `/Users/farricecain/.codex/plugins/cache/refero/refero/1.0.2/skills/refero-design/SKILL.md`
6. The current brand/design-system source of truth, when one exists
7. Only the matching execution prompt under `references/prompts-v2/`

## Workflow

### 1. Compile the creative brief

State the surface, audience, goal, feeling, objection, distinctive idea, existing identity constraints, required Refero layer, and output path. Ask only if a missing answer changes the route.

### 2. Research from distinct angles

- Use Refero styles first for visual direction.
- Search 3–5 angles: one broad aesthetic, one category/domain, one known-brand or best-in-class query, plus unusual adjacent angles when useful.
- Retrieve full styles in batches of 3–4.
- Use screens for concrete interface patterns and flows for multi-step journeys.
- Extract only decisions that can change the work: thesis, typography, palette roles, composition, density, media, surfaces, signature move, and rejects.

### 3. Build three directions

Each direction needs one primary reference, 1–2 bounded borrowed details, a media strategy, role rules, rejects, and token commitments. Directions must differ materially across at least four axes in the Visible Choice Contract.

### 4. Make the options visible

Create the direction manifest and run:

```bash
python3 skills/reference-led-creative-system/scripts/direction_pack.py capture \
  --manifest <manifest.json> --output-dir <run-directory>
python3 skills/reference-led-creative-system/scripts/direction_pack.py verify \
  --manifest <manifest.json> --output-dir <run-directory>
```

Show the local contact sheet and every individual local preview using absolute paths. Remote Refero URLs are provenance only. Do not request a visual choice while any direction is remote-only or unverified.

### 5. Recommend and checkpoint

Recommend exactly one direction with strategic-fit and system-impact reasoning. Stop for the visual verdict unless the user explicitly says to use the recommendation. A name-only choice is valid only after the user could actually see the options.

### 6. Lock before building

Write the reference lock: primary source, traits to preserve, bounded borrowing, role rules, media plan, explicit rejects, token commitments, and build target. Existing brand-system constraints outrank borrowed reference styling.

### 7. Apply to the smallest useful surfaces

Build one or two representative surfaces before expanding the system. Reuse canonical tokens/components when they exist. Use `/generate` only for genuinely required bitmap media and honor its craft and cost gates.

### 8. Audit and preserve

Compare implementation evidence to the lock. Resolve P0/P1/P2 drift. Preserve the good example, QA receipt, manifest, and replay prompt. Do not promote a house style from one successful run.

## Output Contract

- compact research receipt;
- three named, materially different directions;
- locally visible individual previews plus one contact sheet;
- one recommendation and explicit tradeoffs;
- selected reference lock and decision ledger;
- one or two built surfaces when authorized;
- visual QA and regression receipt;
- paste-ready replay prompt.

## Quality Gate

Reject the run if:

- the user cannot see every option;
- any choice surface relies only on a remote image URL;
- the three directions are minor variations;
- references are averaged into a generic middle;
- source token, component, or media roles are repurposed;
- an existing brand system is replaced without authorization;
- implementation starts before a build target or reference lock exists;
- the system reproduces Performance Evidence Journal styling when the new brief calls for a different world;
- visual QA is claimed without rendered evidence;
- a local verifier pass is described as human taste, market, or performance proof.

## First Command

```text
/reference-led-creative-system EXPLORE — [what to design], [audience], [goal], [existing brand constraints], [desired output surfaces]
```

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Reference-Led Creative System — Apply Locked Direction** — `skills/reference-led-creative-system/references/prompts-v2/apply-locked-direction.md`
- **Reference-Led Creative System — Audit And Recover** — `skills/reference-led-creative-system/references/prompts-v2/audit-and-recover.md`
- **Reference-Led Creative System — Lock And Build** — `skills/reference-led-creative-system/references/prompts-v2/lock-and-build.md`
- **Reference-Led Creative System — Three Visible Directions** — `skills/reference-led-creative-system/references/prompts-v2/three-visible-directions.md`

<!-- END:execution-prompts -->
