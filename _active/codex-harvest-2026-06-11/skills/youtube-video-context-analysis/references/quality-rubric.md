# Video Context Quality Rubric

Score outputs against these criteria before reuse.

| Criterion | Pass Standard |
|---|---|
| Evidence separation | Observed spoken, visual, OCR, inference, and uncertainty are not mixed |
| Timestamp usefulness | Important rows have usable timestamps |
| Transcript cleanliness | VTT artifacts are removed and prose is readable |
| Visual honesty | No visual claim appears without frame, OCR, human note, or vision output |
| Uncertainty reporting | Missing captions, frame failures, OCR gaps, and network/tool limits are explicit |
| Reuse value | Analysis points to extraction, strategy, creative, content, or audit use |
| Contradiction readiness | The package lets a later workflow compare claims to visual proof |

## Failure Conditions

- Claims that the system saw visuals when frames/OCR are unavailable.
- No `uncertainty-report.md`.
- No ledger JSON for machine reuse.
- No clear path from analysis to downstream extraction or creative work.

