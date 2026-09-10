# Signal Fidelity False-Alarm Stress Test

## Verdict

`PASS` for bounded prototype behavior. This does not establish a production
false-positive rate.

## Cases

| Stress case | Expected restraint | Result |
|---|---|---|
| Metaphor | Human review cue, no distortion claim | PASS |
| Productive ambiguity | Human review cue, no distortion claim | PASS |
| Sparse ineligible brief | `NOT_RUN`, no warnings or questions | PASS |
| Owner-approved reframing | Adaptation record, no distortion claim | PASS |
| Coordinated negative limit | Preserve both limits | PASS after bounded repair |
| Positive boundary breach | Do not mistake positive language for a preserved limit | PASS |

All valid packets remained exit code 0. No fixture could block execution.

## Defects Found And Repaired

### 1. Creative exact-match overreach

The original evaluator treated every must-survive item as a literal marker. That
would turn metaphor, ambiguity, and voice variation into avoidable distortion
warnings. The repair added an optional `match_policy`: `literal` for locked
terms, limits, proof labels, and exact claims; `manual` for creative meaning.
Manual items remain visible to the human owner but are not called distortion.

### 2. Ineligible sparse-work burden

An explicitly invoked sparse packet could produce missing-field warnings even
when the work should never have been selected. The repair added an optional
`selected_for_review: false` receipt that returns `NOT_RUN` with no questions.
It is not required on normal work and creates no automatic selector.

### 3. Coordinated-negation false negative

The first real-work replay missed “do not … add a new brand palette, or create a
parallel brand system” because exact markers did not understand one negation
governing two coordinated clauses across line wrapping. The first repair attempt
still split on newlines and failed. The second bounded repair normalizes line
wrapping and recognizes negation within one sentence for `limit` items only. A
paired positive-language control proves that “add a palette and create a parallel
system” still fails the boundary check.

Both the initial result and failed first repair are retained in machine-readable
receipts; the polished final result does not erase them.

## Burden

- Added user questions: `0`.
- Baseline/treatment word deltas: strategy `+15`, content `+9`, handoff `+22`.
- Average treatment expansion: `+15.3` words.
- Sparse ineligible work: no evaluation and no question burden.
- Manual creative review: one bounded owner judgment per selected creative item;
  production frequency remains `UNTESTED`.

## Remaining Risks

- Literal coverage is not semantic equivalence.
- Manual review could still become annoying if selection expands beyond rare,
  consequential transformations.
- Builder-controlled arms cannot prove independent comprehension or creative
  preference.
- Real operator preparation time and production false-positive rate remain
  `UNTESTED`.
