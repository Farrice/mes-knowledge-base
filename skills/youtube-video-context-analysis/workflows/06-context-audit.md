---
description: "Audit a video context package for evidence separation, claims, contradictions, and uncertainty"
---

# Context Audit

Use this after a context package exists.

## Inputs

- `extractions/video-context/<video-id>/video-context-ledger.md`
- `extractions/video-context/<video-id>/video-context-ledger.json`
- `analysis.md`
- `uncertainty-report.md`

## Audit Steps

1. Identify important spoken claims.
2. Check whether frames or OCR support, contradict, or fail to verify each claim.
3. Flag inferred context that should not be treated as observation.
4. List missing evidence that would change the conclusion.
5. Produce a concise repair or reuse recommendation.

## Output Schema

A "Context Audit — [video title / id]" report:

```
## Claims Identified
1. [claim, timestamp/row cited]

## Claim-by-Claim Findings
### [claim]
- Status: [supported / contradicted / fails to verify]
- Evidence lane(s) cited: [observed_spoken / observed_visual / observed_onscreen_text — row references]
- Note: [what the cross-check actually showed]

## Inference Flagged As Fact
- [instance, row/location] — [why it reads as observation when it is synthesis]

## Missing Evidence That Would Change The Conclusion
- [gap] — [what claim it affects and how]

## Repair / Reuse Recommendation
[ready as-is / needs specific additional evidence / flag this claim as unreliable — stated plainly]
```

The audit must not introduce new claims beyond what the ledger already contains — it checks the package, it does not extend it.

## Quality Gate

Every contradiction note must cite the evidence lane it comes from. Before handoff, confirm: "fails to verify" is kept distinct from "contradicted," every inference-presented-as-fact instance is flagged with its original ledger location, and the missing-evidence list is limited to gaps that actually affect trust in a claim (not a generic wishlist).
