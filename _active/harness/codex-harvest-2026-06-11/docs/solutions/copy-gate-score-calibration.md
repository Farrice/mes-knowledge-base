# Copy Gate Score Calibration

Use this pattern when public, revenue, outreach, or offer copy receives a high internal quality score but the user says it still feels generic, flat, confusing, or not deployable.

## Problem

Copy gates can become ceremonial: the output gets formatted, experts are named, and a scorecard assigns 9+ ratings without proving that the copy creates attention, tension, buyer recognition, or action. This is especially costly when the user is starting from zero proof or momentum and needs the public asset to carry real acquisition weight.

## Working Solution

Treat user rejection as calibration data, not taste noise.

- Record the user's score or qualitative baseline in the next Copy Gate Result.
- Name the exact failure addressed: weak hook, vague buyer language, low tension, no proof mechanism, generic CTA, or borrowed-authority misuse.
- Cap scores below 9 unless there is live market/user proof.
- Do not treat static prose checks as sufficient. They can catch some structure problems, but they cannot prove scroll-stopping force.
- Require one concrete revision trail per dimension instead of "expert stack applied" language.

## Guard Pattern

For current active revenue-copy artifacts, a valid Copy Gate Result should include:

- `Verdict: PASS`
- current intent marker
- user-calibrated baseline
- failure addressed
- score discipline
- expert deployment evidence
- manual prose/slop review, not classifier-only
- a `Revision Applied` column

Flag the gate if average scores are inflated or if any 9+ score appears without live market/user proof.

## Prevention Rule

When the user says public/revenue copy is generic, over-scored, or falsely passed, log the incident and lower the system's confidence before rewriting. Do not answer with a more polished version of the same scorecard.
