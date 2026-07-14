---
description: "The surpass layer — take a built surface map down to identity-level depth by composing existing skills (not reimplementing them): hand beliefs/pains to /mcraney-deep-canvass, add the identity layer with consumer-posture-research, run fact-verifier on any real-world claim — returning a depth-enriched map (surface language + belief layer + posture/identity + verified claims)"
---

# /ctm-deepen

Drive the map to identity-level depth — how the Customer Truth Map exceeds its own source. A surface map tells you what the customer SAYS; this drives it down to what belief makes them resist, what identity makes the words mean what they mean, and whether the facts riding alongside are true. It composes skills we already have — never reimplements them.

## Trigger
`/ctm-deepen`

## Workflow
`skills/customer-truth-map/workflows/ctm-deepen.md`

## Quick Use
Provide a finished surface map of one narrow customer. Pick which layer(s) the downstream job needs (don't bolt on all three reflexively). Belief/posture layers annotate real harvested lines; they never replace language with inference.

## Pipeline
1 Belief layer — compose `/mcraney-deep-canvass` on THINK + PAINS (belief, resistance hierarchy, processing routes) → 2 Posture/identity layer — compose `consumer-posture-research` on DO + SAY → 3 Verified-claim layer — compose `fact-verifier` on every real-world claim (VERIFIED / LIKELY / UNCONFIRMED)

## Output
The depth-enriched map: surface language (carried intact) + belief layer + posture/identity layer + verified-claim layer (with use-rules on non-VERIFIED claims) + a layer-coverage note (which added, which honestly skipped and why).

## Stacks With
→ composes: `/mcraney-deep-canvass`, `consumer-posture-research` (+ dai-media consumer posture), `fact-verifier`
→ upstream `/customer-truth-map` BUILD (or `/ctm-refresh` if stale) · feeds resistance-aware copy + identity-aware positioning
