# Regression Fixture SAL-REF-01: Sales Reference Must Clear the Prose Surface

## Audit Evidence

The v1 sales body returned `FLAGGED` from `execution/prose_classifier.py` with a 5.0/10 AI score. The detected surface failures were six em dashes and repeated internal `you` anaphora.

## Failure Class

- **Reference quality:** prose surface and recognition.
- **Risk:** a structurally correct sales reference can still read templated or over-engineered.

## Expected Behavior

The v2 sales body must preserve every offer fact, proof limitation, and single CTA while removing mechanical punctuation and repeated sentence openings. It should return `CLEAN` or, at worst, a reviewed low-score warning rather than `FLAGGED`.

## Preservation Lock

- Keep `STORY FRAGMENT` and one bounded HVC example.
- Keep prices, timelines, deliverables, risk reversal, approval veto, and no-performance-proof boundary exact.
- Do not add testimonial language, urgency, demand, or process claims.
- Do not edit the sealed v1 target.

## Status

- V1 surface: `FLAGGED`.
- V2 current reference: `CLEAN`, AI score 0.3/10, 672 body words.
- Final status: `REPAIRED`.
