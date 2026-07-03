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

## Quality Gate

Every contradiction note must cite the evidence lane it comes from.

