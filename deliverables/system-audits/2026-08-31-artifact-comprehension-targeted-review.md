# Artifact Comprehension v0.2.1 — Targeted Human Gate

Status: **ROUND 2 COMPLETE / BEHAVIOR REFINEMENT REQUIRED**

Ratings: AHG-002R `Y` accepted. AHG-003R: neither passed; `X` was the fallback,
while Y's flow was the only high-value element. Implementation continues in the
single-example morning review.

AHG-001 is accepted and unchanged. This rerun tests only whether the two
revised artifacts preserve more insight without bringing back the text wall.

## AHG-002R — Research

**Prompt:** Summarize the demand evidence without overstating buyer validation.

### Variant X

#### What changes

Category interest is supported; willingness to pay for this exact offer remains
untested.

| Claim | Support | Confidence | Implication |
|---|---|---|---|
| Buyers discuss the problem | Interview set | Verified | Continue |
| They will buy this package | No payment event | Untested | Run a paid test |

**Caveat:** Attention is not purchase behavior.

### Variant Y

#### Demand signal

**Verdict:** People recognize the problem. We still have no proof they will pay
for this offer.

| Signal | What it proves | What it does not prove | Action |
|---|---|---|---|
| The problem appears in interviews | The pain is real | This package will sell | Keep testing |
| No one has paid | Nothing about demand yet | Willingness to pay | Run one paid test |

**Bottom line:** Interest earns another test, not a claim of demand.

## AHG-003R — Implementation

**Prompt:** Show how to build and validate the pilot while preserving the stop
boundary.

### Variant X

#### Pilot path

**Goal:** Make substantial artifacts easier to absorb without touching the
output system that already works.

1. Lock the global behavior.
2. Test artifact formats.
3. Try to break them.
4. Get human ratings.

**Only then:** Decide whether to promote.

**Stop:** No merge, hooks, or global activation.

### Variant Y

#### Shadow pilot plan

End state: workspace proof, stopped before promotion.

1. Freeze the successful global behavior.
2. Build artifact-only fixtures.
3. Run negative controls.
4. Collect human artifact ratings.

**Flow:** Fixtures → sabotage proof → human gate → explicit promotion decision

Stop before merge, hooks, or global activation.

## Reply Shape

- `AHG-002R: X/Y/TIE — [why]`
- `AHG-003R: X/Y/TIE — [why]`
