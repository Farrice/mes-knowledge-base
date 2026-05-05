---
description: Audit current ad portfolio against awareness pyramid, identify stage coverage gaps, and produce stage-matched scaling roadmap with creative requirements
---

# 08 — Awareness Pyramid Scaling Audit

> Per Omar: "If you're going after the entirety of the pyramid, that's where you're able to scale much more efficiently keeping your CAC at bay because you're always converting people from one stage to the other."

The diagnostic + roadmap workflow for brands hitting CAC ceilings. Maps current portfolio against Schwartz's 5-stage awareness pyramid, identifies stage gaps, prescribes creative roadmap to break the ceiling.

## Pre-Flight Gate

Run this workflow when:
- ✅ CAC inflating as spend increases (the canonical CAC-ceiling symptom)
- ✅ Planning scale-phase ramp (going from $X/day to $Y/day where Y >> X)
- ✅ Hit a spend plateau and don't know why
- ✅ Quarterly portfolio health check for mature brands

Skip when:
- ❌ Brand not yet at first scale (new brands typically need full launch portfolio first; run `/omar-launch-portfolio`)
- ❌ Profit architecture broken (CAC inflation may be price/cost problem, not pyramid problem; run `/omar-profit-architecture` first)

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Pattern 8: Awareness Pyramid Scaling Theory)
- `skills/omar-eddaoudi-scaling-ops/references/awareness-pyramid-mapping.md` (the canonical reference)
- `skills/omar-eddaoudi-scaling-ops/references/avatar-template-1page.md` (avatars typically span stages)

## Execution

### Step 1: Inventory Current Ad Portfolio

Pull from ad account:
- All active ads (last 30 days)
- Per ad: hook, body copy, CTA, format, performance data (ROAS, CTR, CPM, CPC)
- Per ad: dominant trigger deployed (from NMTM)
- Spend distribution by ad

### Step 2: Tag Each Ad to Awareness Stage

For each ad, classify dominant stage:

| Ad Type / Hook Pattern | Likely Stage |
|------------------------|--------------|
| Offer + urgency + retargeting | Most-aware |
| Comparison + mechanism + DR | Product-aware |
| Founder explainer + category positioning | Solution-aware |
| Problem agitation + education + quiz | Problem-aware |
| Pattern-interrupt + identity + story | Unaware |

If an ad spans multiple stages, classify by DOMINANT stage (primary intended audience).

### Step 3: Build the Coverage Matrix

| Stage | # Ads | % of Portfolio | % of Spend | % of Conversions | Average ROAS | CAC |
|-------|-------|----------------|------------|------------------|--------------|-----|
| Most-aware | __ | __% | __% | __% | __ | $__ |
| Product-aware | __ | __% | __% | __% | __ | $__ |
| Solution-aware | __ | __% | __% | __% | __ | $__ |
| Problem-aware | __ | __% | __% | __% | __ | $__ |
| Unaware | __ | __% | __% | __% | __ | $__ |

### Step 4: Diagnose Coverage Pattern

Common patterns and what they mean:

**Most-Aware Heavy** (>50% spend on most-aware):
- Symptom: CAC inflating fast as spend increases
- Diagnosis: You're exhausting most-aware crowd
- Prescription: Build product-aware + solution-aware layers urgently

**Bottom-Heavy / Education-Only**:
- Symptom: Lots of clicks, weak conversion
- Diagnosis: No conversion-stage creative
- Prescription: Build product-aware + most-aware layers

**Single-Stage Cluster**:
- Symptom: Hit a ceiling at one stage of spend
- Diagnosis: Pyramid coverage gap
- Prescription: Build adjacent stages

**Stage Mismatch** (high-stage creative on low-stage traffic):
- Symptom: High CTR but low conversion
- Diagnosis: Most-aware copy on unaware audience
- Prescription: Audit creative-traffic match

### Step 5: Calculate the CAC Ceiling Math

Run the CAC inflation projection:

```
Current state:
- Total spend: $___ /day
- Most-aware % of spend: __%
- Average CAC: $___

3x scale projection (most-aware-only):
- Most-aware pool exhaustion → CAC inflation curve
- Estimated CAC at 3x spend: $___ (typically 1.5-2x current)
- ROAS at 3x: __ (compared to current __)

3x scale projection (pyramid-distributed):
- New stages absorb spend
- Estimated CAC at 3x spend: $___ (typically 1.1-1.3x current)
- ROAS at 3x: __ (compared to current __)
```

Show the math difference. This justifies the pyramid investment.

### Step 6: Build the 5-Phase Scaling Roadmap

Phase 1 (Week 1-2): Stabilize Most-Aware
- Audit current most-aware creative for refresh
- Build retargeting + DPA + offer-led set
- Goal: Lock in floor CAC

Phase 2 (Week 3-4): Build Product-Aware Layer
- Comparison ads against named competitors
- Mechanism explainers
- Goal: Add 25% of spend at slightly elevated CAC

Phase 3 (Week 5-6): Build Solution-Aware Layer
- Founder ads explaining "why this approach"
- Category-positioning content
- Goal: Add 25% of spend, feeds product-aware

Phase 4 (Week 7-8): Build Problem-Aware Layer
- Problem-agitation educational content
- Quiz / lead magnet funnels
- Goal: Add 20% of spend, feeds solution-aware

Phase 5 (Week 9-12): Build Unaware Layer
- Story-led identity content
- Pattern-interrupt problem-naming hooks
- Goal: Add 10% of spend, feeds entire pyramid

### Step 7: Stage-Matched Creative Briefs

For each stage that needs new creative, produce a brief:
- Avatar match (which avatars live at this stage)
- Trigger match (which of their triggers fits this stage)
- Hook ideation (3-5 hooks per stage from existing hook bank)
- Format requirements (UGC / Static / Founder mix per stage)
- Volume target (typically 3-5 ads per stage minimum)

### Step 8: Build the Stage-Bridge Strategy

Stage bridges are connective creative that converts an audience from one stage to the next:
- Unaware → Problem-aware: pattern-interrupt that names a problem they hadn't articulated
- Problem-aware → Solution-aware: educational content showing solution categories
- Solution-aware → Product-aware: category-positioning + founder explainer
- Product-aware → Most-aware: comparison + mechanism + offer hint

Brief each bridge ad explicitly.

### Step 9: Deliverable

Produce `pyramid-audit-[brand]-[date].md`:
1. Current portfolio coverage matrix (with performance data)
2. Coverage pattern diagnosis
3. CAC ceiling math (current vs. projected at scale)
4. 5-phase scaling roadmap
5. Stage-matched creative briefs (per stage that needs new creative)
6. Stage-bridge strategy (4 bridge briefs)
7. Volume targets per stage (per week)
8. Success metrics + check-in cadence

## Content Type Adaptations

| Brand Stage | Adaptation |
|-------------|-----------|
| First scale ($1K-$5K/day) | Focus on Phases 1-3; defer Phase 5 unless Phase 4 saturates |
| Growth ($5K-$25K/day) | Run all 5 phases; pyramid coverage critical |
| Mature ($25K+/day) | Quarterly audit; refresh stage creative every quarter |
| Subscription DTC | Add cohort-aware analysis (LTV by acquisition stage) |
| High-ticket | Phases compressed — Phase 1 + 3 (founder) typically dominate |
| B2B | Replace consumer awareness language with B2B equivalents (decision-stage maturity instead of product-awareness) |

## Output Requirements

The deliverable must include:
- ✅ Coverage matrix with all 5 stages, % spend, % conversions, ROAS, CAC
- ✅ Coverage pattern diagnosis (which of the 4 common patterns applies)
- ✅ CAC ceiling math (current vs. 3x projection in both scenarios)
- ✅ 5-phase scaling roadmap (week-by-week)
- ✅ Stage-matched creative briefs for gaps
- ✅ Stage-bridge strategy with 4 bridge ad briefs
- ✅ Success metrics (CAC stability target, ROAS target per stage)

## Quality Gate

Score against `genius.md` Quality Rubric Criterion 6 (Awareness-Stage Match) + Criterion 8 (Iteration Loop Closure). Pass condition: 8+/10 each.

**Veto**:
- Audit identifies pyramid gap but doesn't prescribe specific creative for the gap → reject
- Roadmap skips a stage → reject (full pyramid coverage required for sustainable scale)
- No CAC ceiling math → reject (the math is the justification for the work)

**Anti-pattern check**:
- "Pyramid coverage doesn't matter for our brand" — wrong, it's universal pyramid math
- Stage diagnosis without performance data → unreliable, get the data first
- Roadmap with no week-by-week sequencing → reject, sequence required for execution
- Stage-bridge strategy missing → critical gap, bridges drive the pyramid flow
