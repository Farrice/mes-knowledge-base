# Artifact Comprehension Contract v0.2

Status: `PILOT / SHADOW / HUMAN GATE PENDING`

Owner: `/system-audit`

Support: Clear Depth, Native Codex Artifact Default, the existing Briefing
Room renderer, and `/repeatability-spine` preservation controls.

## Narrow Job

Make substantial documents and artifacts faster to understand, embody, and
reuse without weakening the thinking underneath them.

This contract does not govern ordinary conversation or closeouts. Those defer
entirely to the existing global Clear Depth and Three Contextual Next Prompts
behavior.

## Preservation Lock

- Preserve full reasoning, source detail, caveats, proof state, authority, and
  the user's existing preferred conversational output.
- Change only the presentation of substantial written artifacts when a
  different representation materially reduces reading or decision effort.
- Do not force a visual, repeat the same information in several forms, or turn
  nuanced prose into a false grid.
- Do not create a new renderer, dashboard, skill, command, task, hook, global
  rule, export format, or parallel artifact system.

## Activation

Activate only when all three conditions are true:

1. the output is a substantial reusable document or artifact;
2. its information has a recognizable shape that a representation can clarify;
3. the representation earns its space by improving comprehension, recall, or
   action.

Otherwise use concise, scan-friendly prose or Markdown.

## Representation Selection

| Information shape | Preferred representation | Use only when |
|---|---|---|
| Decision or recommendation | Summary plus decision block/table | choices, tradeoffs, or ownership are genuinely distinct |
| Comparison | Matrix or table | repeated fields make differences easier to scan |
| Chronology or staged change | Timeline | order and state changes matter |
| Dependency or handoff | Flow | one action affects several downstream steps |
| Evidence and claims | Evidence rows plus caveats | claim, source, confidence, and implication must stay linked |
| Metrics or trends | Stats, bars, or sparkline | comparable numbers or change over time actually exist |
| Implementation | Playbook, checklist, or flow | sequence and completion state matter |
| Nuance, voice, or argument | Prose | compression into a visual would flatten meaning |

The smallest sufficient representation wins. A document may combine forms only
when each form performs a different job. The same conclusion should not be
duplicated as prose, table, callout, and chart.

## Surfaces

Prefer the existing surfaces in this order:

1. native Codex artifact or scan-friendly Markdown;
2. an existing Briefing Room section when the artifact is reusable and the
   visual structure materially helps;
3. a share-safe client format only when explicitly requested or required by the
   delivery context.

HTML is not the default. Plain prose is not a failure.

## Depth And Proof

- Put the decision-bearing surface first.
- Keep essential caveats adjacent to the claim or recommendation they qualify.
- Preserve the fuller source/detail layer in the same artifact or through a
  clear inspectable reference.
- Never use a chart, matrix, or visual hierarchy to imply certainty the
  evidence does not support.
- `go deeper`, `show proof`, and `technical detail` continue to expose more
  depth through the existing global behavior.

## Frozen Boundaries

The pilot must not alter:

- global Clear Depth;
- global Three Contextual Next Prompts;
- ordinary reply shape;
- closeout behavior;
- routing, hooks, tasks, skills, or renderer code;
- global or production activation.

## Human Behavior Gate

Farrice reviews three artifact comparisons across strategy, research, and
implementation. The gate passes only when each pilot artifact is:

1. faster to understand than the text-wall control;
2. no shallower or less nuanced;
3. easier to act from;
4. free of decorative or redundant representation; and
5. preferred or tied with a specific note explaining why the representation
   earned its place.

Missing ratings produce `HUMAN GATE PENDING`. Any explicit “this feels more
systemized than useful” verdict produces `BEHAVIOR REFINEMENT REQUIRED`, even
if the preference count is positive.

## Promotion And Rollback

Promotion requires three accepted artifact comparisons, zero frozen-boundary
changes, and Farrice's explicit approval. Rollback removes the single CODEX
pointer or reverts the activation commit. No merge, global activation, hook
change, task creation, skill creation, or renderer change is authorized.
