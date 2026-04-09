# Evolution Log: Dan Martell Business Scaling — Delegation Timing Calculus

**Date**: 2026-04-09
**Skill**: dan-martell-business-scaling
**Workflow**: 03-buyback-audit
**Aspect**: Time-gated delegation → Revenue-gated delegation timing
**Status**: KEEP

## Hypothesis

Adding a "Delegation Timing Calculus" (Phase 0) before the time audit calculates the break-even revenue threshold for each potential delegation, producing a financially-sequenced scaling timeline. This prevents the two delegation killers: premature delegation (cash death — delegating at $4K/month what you can't afford until $8K) and late delegation (founder death — doing $10/hr work at $15K/month). The original workflow uses arbitrary time windows (Week 1-2, 3-4, Month 2-3) that ignore the founder's actual revenue stage.

The cognitive mechanism: instead of asking "what should you delegate first?" (which invites priority-by-annoyance), the calculus asks "at what revenue does this delegation become ROI-positive?" — forcing mathematical precision on a decision most founders make emotionally.

## Benchmark

**Prompt**: "Design a scaling roadmap for Farrice's Authority Flywheel from $0 to $20K/month — what to delegate when"

### Control (Original workflow — no Phase 0)

**Key outputs**:
- Time audit: correctly classifies tasks into $10/$100/$1K/$10K buckets
- Runner Test: calculates ROI for each delegation
- Delegation roadmap: Week 1-2 quick wins, Week 3-4 systems, Month 2-3 strategic
- Vacation-Readiness Score: honest assessment

**Diagnosis**: The time-gated roadmap suggests "delegate in Week 1-2" without checking if Farrice can afford delegation at $0 revenue. The Runner Test shows ROI but doesn't answer "can I afford this RIGHT NOW?" A critic immediately asks: "You're at $0/month — where does the money for a VA come from?" The roadmap is the same template whether you're at $0 or $15K.

- Intent Alignment: 6/10 (answers "what" but not "when")
- Expert Standard: 7/10 (Martell framework present but missing financial precision)
- Adversarial Resilience: 5/10 (can't survive "how do you pay for this?")
- **Composite: 6.0**

### Variant (Phase 0: Delegation Timing Calculus)

**Key outputs**:
- Break-even table: every function mapped to specific revenue threshold
- Status flags: TOO EARLY / NOW / OVERDUE for each delegation at current revenue
- Revenue-gated roadmap: $0-$3K (founder does everything), $3K-$8K (first VA), $8K-$15K (systems handoff), $15K-$25K (strategic replacement)
- Next 3 delegation triggers with specific revenue numbers
- Budget ceilings: 15% at Phase 2, 20% at Phase 3

**What changed**: At $0 revenue, the variant says "do everything yourself — only use AI tools." The first human delegation unlocks at ~$1.7K/month (sales follow-up). Content scheduling and onboarding cluster around $2.6-$2.9K, suggesting one VA hire when you cross $3K. Client delivery delegation doesn't make sense until $12K. This is actionable and financially safe.

- Intent Alignment: 9/10 (directly answers "what to delegate WHEN" with revenue triggers)
- Expert Standard: 8/10 (constraint-first + financial precision Martell actually teaches)
- Adversarial Resilience: 8/10 ("how do you pay for this at $0?" is answered: you don't)
- **Composite: 8.3**

## Delta

| Dimension | Baseline | Variant | Change |
|-----------|----------|---------|--------|
| Intent Alignment | 6 | 9 | +3 |
| Expert Standard | 7 | 8 | +1 |
| Adversarial Resilience | 5 | 8 | +3 |
| **Composite** | **6.0** | **8.3** | **+2.3** |

## What Made It Work

1. **Revenue as the gating variable, not time**: Weeks/months are arbitrary. Revenue milestones are financially grounded. A founder at $0 has different needs than one at $8K even if both are "Week 1."
2. **Three-status system (TOO EARLY/NOW/OVERDUE)**: Creates urgency for late delegation AND patience for early delegation. Both directions are dangerous; the calculus names both.
3. **Budget ceilings by phase**: 15% at $3-8K, 20% at $8-15K prevents the common mistake of over-delegating during early growth spurts.
4. **Break-even sorting = delegation sequence**: The order is mathematical, not emotional. Removes "delegate what annoys you most" bias.

## What This Doesn't Change

- genius.md: untouched (the Buyback methodology, Constraint Telescope, Vacation Test are all preserved)
- All other workflows: untouched
- The core time audit + Runner Test + Vacation Test structure: preserved within the workflow
- Only addition: Phase 0 calculus + revenue-gated roadmap phases replacing time-gated phases
