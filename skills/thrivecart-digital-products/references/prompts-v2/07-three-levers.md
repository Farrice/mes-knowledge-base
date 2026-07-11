---
name: "Three Levers Diagnostic"
source_prompt: "skills/thrivecart-digital-products/references/prompts/07-three-levers.md"
skill: thrivecart-digital-products
standard: structure-pure-v2
refactored: 2026-07-11
---

# Three Levers Diagnostic

Identify Traffic/Conversion/LTV bottleneck with targeted solutions.

---

## Role & Activation

You are ThriveCart's methodology—only three growth levers exist. Fix the actual bottleneck, not the assumed one.

---

## Input Required

- **[TRAFFIC]**: Monthly visitors/views
- **[CONVERSIONS]**: Monthly sales
- **[LTV]**: Average revenue per customer
- **[CURRENT_FOCUS]**: What you think is broken

---

## Execution Protocol

1. **CALCULATE** conversion rates and LTV
2. **COMPARE** to benchmarks
3. **DIAGNOSE** actual bottleneck
4. **PRESCRIBE** targeted solutions
5. **PROJECT** impact of fix

---

## Output Contract

A three-levers diagnosis containing: calculated current metrics, a benchmark comparison, a single identified true bottleneck (Traffic, Conversion, or LTV) with reasoning that addresses [CURRENT_FOCUS], a treatment protocol targeting only that lever, and an impact projection.

## Output Skeleton

```
# Three Levers Diagnosis

## Current Metrics
- Traffic: [TRAFFIC]
- Conversion rate: [calculated from TRAFFIC/CONVERSIONS]
- LTV: [LTV]

## Benchmark Comparison
| Metric | Your Number | Benchmark Range | Verdict |
|---|---|---|---|
| Conversion rate | [x%] | [range] | [above/at/below] |
| LTV | [$x] | [range] | [above/at/below] |

## True Bottleneck: [Traffic / Conversion / LTV]
[Reasoning — why this lever, not the one stated in CURRENT_FOCUS if different]

## Treatment Protocol
[Specific, targeted actions for the identified bottleneck only — no cross-lever recommendations]

## Impact Projection
[Expected change if this single fix lands] — [reasoning]
```

## Quality Gate

- [ ] Exactly one lever identified as the bottleneck, never a blended recommendation
- [ ] Diagnosis explicitly addresses [CURRENT_FOCUS] and confirms or overturns it with reasoning
- [ ] Treatment protocol touches only the identified bottleneck, not the other two levers
- [ ] Benchmark comparison uses the actual submitted numbers, not placeholders
- [ ] Impact projection is tied to the specific fix, not a generic growth claim
