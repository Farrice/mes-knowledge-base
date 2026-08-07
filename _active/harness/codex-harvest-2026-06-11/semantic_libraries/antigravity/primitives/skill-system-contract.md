# Skill System Contract

## Purpose

Use this primitive when a capability should operate as an end-to-end Codex system: small focused components wired by an orchestrator into a durable workflow with clean context, handoffs, checkpoints, and proof.

This prevents two common failures:

- isolated skill calls that leave the user manually connecting every step
- mega-skills that load too much context and become hard to maintain
- expert soup where many components are named but no owner composes them

## When To Use

- A source teaches how to improve skills, workflows, agents, or operating systems.
- A task requires multiple skills or workflows in a sequence.
- The output of one step must become the input to the next.
- The user wants reliability, orchestration, scaffolding, order of operations, or smoother OS behavior.
- A workflow should run from one front-door command without manual copy/paste between steps.
- More than three experts, skills, workflows, or gates are plausible and need composition.
- A good output needs to become replayable through `/repeatability-spine`
  instead of depending on hidden chat context or luck.

## Build Shape Decision

Before creating or changing files, decide which shape fits:

| Shape | Use When | Output |
|---|---|---|
| Component skill | One focused reusable method is missing | `skills/<slug>/` or referenced existing skill |
| Reference | The source is useful context but not a new behavior | `references/` or `semantic_libraries/` doc |
| Workflow | A repeatable sequence can be invoked directly | `.agent/workflows/<command>.md` |
| Skill system | Multiple components need orchestration and handoffs | orchestrator workflow plus contract |
| Companion OS layer | The source changes how many workflows should operate | semantic primitive plus workflow updates |
| Expert composition primitive | Multiple experts are useful but risk becoming soup | `expert-composition-contract.md` plus `/expert-composition-governor` |
| No build | Source is thin, duplicate, or already covered | routing note or state update only |

## Required Contract Fields

Every skill system must define these fields before it is treated as deployed:

| Field | Requirement |
|---|---|
| Source evidence | Transcript, file, URL package, or local artifact path |
| Objective | One sentence describing the system outcome |
| Components | Skills, workflows, agents, scripts, references, and external tools involved |
| Step order | Ordered phases with dependencies |
| Inputs | What each step needs to run well |
| Outputs | What each step must produce for the next step |
| Handoff summary | Compact boundary summary, not full upstream context |
| Composition rule | Function owner, contribution slots, skipped experts, and integration rule when more than two components are active |
| Human checkpoint | Where approval, clarification, or review can stop the chain |
| Validation | Checks for routing, files, evidence, quality, and cold-start use |
| Behavior-changing proof | Before/after, cold-start run, applied scenario, or transformed artifact proving the capability changes real behavior |
| Result surface | How the user sees the final output or artifact |
| Context policy | What stays hot, what stays cold, and what is loaded only on demand |
| Reuse hook | Where the system should be reused, extended, or promoted |

## Default Handoff Shape

```markdown
## Skill System Handoff: [Step] -> [Next Step]
- **Source evidence**: [path or timestamp rows]
- **Component used**: [skill/workflow/script/agent]
- **Output produced**: [file/path/object]
- **Next input**: [what the next step receives]
- **Validation**: [pass/fail/check command]
- **Open risk**: [none or exact limitation]
```

## Context Policy

- Keep orchestrator instructions compact and explicit.
- Load only the component needed for the current step.
- Pass summaries and file paths between steps instead of full upstream output.
- Use the expert composition contract before loading many experts into context.
- Use deterministic scripts for extraction, counting, validation, registry sync, and cold-start checks.
- Do not preload all migrated command wrappers.

## Human Checkpoints

Use a checkpoint when:

- build shape is uncertain
- the next step changes system authority, routing, or public/client-facing output
- a paid, external, destructive, or delegated action would occur
- validation fails and the recovery path changes scope

Skip a checkpoint when:

- the work is local, reversible, already approved, and inside `/Users/farricecain/Codex Antigravity`
- the ambiguity changes polish but not execution path

## Validation Checklist

- Source package exists and separates observed, inferred, and unavailable evidence.
- Existing arsenal was routed before creating a new component.
- The contract includes all required fields.
- The expert composition contract is applied when multiple experts or skills are active.
- Command bridge exists when the system is command-invokable.
- Router search surfaces the system for natural queries.
- `validate_skill.py` passes for the command wrapper when applicable.
- Cold-start prompt can identify source evidence, components, route, checks, and first action without relying on hidden chat context.
- Behavior-changing proof exists when the system claims to enhance copy, workflow quality, strategy, creative output, or operating behavior.

## Pilot

The first pilot is `/source-to-skill-system`, grounded in `extractions/video-context/FD53kEpLh9c/`. It turns source material about better skill design into a Codex-native system design route.

## Last Updated

2026-05-09
