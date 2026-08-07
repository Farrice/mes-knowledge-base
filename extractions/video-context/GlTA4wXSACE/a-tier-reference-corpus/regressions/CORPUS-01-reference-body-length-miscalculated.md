# Regression Fixture CORPUS-01: Reference Length Must Measure the Asset Body

## Audit Evidence

The six v1 reference files landed inside the brief ranges only when `Expected Behavior` and `Reference Receipt` were included. The actual `Reference Asset` body counts were:

| Case | Required body | V1 body |
|---|---:|---:|
| FND-01 | 650–900 | 538 |
| SAL-01 | 650–900 | 521 |
| HLT-01 | 450–650 | 359 |
| TEC-01 | 350–500 | 302 |
| EDU-01 | 700–900 | 606 |
| OPS-01 | 450–650 | 354 |

## Failure Class

- **Corpus quality:** format and practitioner usefulness.
- **Root cause:** word count was taken across the complete reference file instead of the body between `Reference Asset` and `Reference Receipt`.

## Expected Behavior

Every current reference body must independently satisfy its brief's word range. Headers, expected-behavior notes, receipts, and metadata do not count.

## Preservation Lock

- Preserve all six v1 files and their pre-replay SHA-256 seal as the immutable judgment targets.
- Create separate v2 current references; do not rewrite v1 after seeing replay outputs.
- Preserve decision, facts, truth constraints, source labels, voice, and objective.
- Add no router route, expert, or domain adapter.

## Status

- V1 replay targets: frozen.
- V2 current references: sealed separately in `current-reference-seal.json`.
- Validated body counts: 726, 672, 505, 414, 798, and 512 words.
- Final status: `REPAIRED`.
