---
description: Build complete 3-layer launch creative portfolio (UGC + Static + Founder ads) with Andromeda-friendly diversity for new brand launch or scale-phase ramp
---

# 07 — Three-Layer Launch Portfolio

> Per Omar: "I always like to start with the bare minimum and these are three categories: UGC, Static, and Founder ads. And you have diversity across this entire portfolio. Now you launch it and you measure what works."

The launch portfolio system. Refuses single-ad-type launches. Engineers Andromeda-friendly variation across types and angles.

## Pre-Flight Gate

Run this workflow when:
- ✅ New brand launch (mandatory once research/avatars are done)
- ✅ Major scale-phase ramp (going from $1K/day to $5K+/day)
- ✅ Existing portfolio has hit a creative ceiling, need full refresh
- ✅ Repositioning launch (new hero positioning needs new creative testbed)

Skip when:
- ❌ Avatars / triggers / hooks not yet built (run `/omar-avatar-trigger-map` first)
- ❌ Profit math not validated (run `/omar-profit-architecture` first)
- ❌ Single-ad-type test (running just UGC test is fine but doesn't need this workflow)

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Pattern 7: 3LAI, Pattern 8: Awareness Pyramid, Pattern 13: Visual Hierarchy)
- `skills/omar-eddaoudi-scaling-ops/references/avatar-template-1page.md` (the avatars these ads target)
- `skills/omar-eddaoudi-scaling-ops/references/neural-trigger-categories.md` (triggers per ad)
- `skills/omar-eddaoudi-scaling-ops/references/visual-composition-grid.md` (static composition discipline)
- `skills/omar-eddaoudi-scaling-ops/references/awareness-pyramid-mapping.md` (stage-matched coverage)

## Execution

### Step 1: Define Portfolio Scope

Lock the parameters:
- Number of avatars to target (typically 2-4 from `/omar-avatar-trigger-map`)
- Awareness stages to cover at launch (typically all 5, but new brands may start with stages 2-4)
- Budget allocation (split across 3 layers)
- Timeline (launch + first iteration cycle = typically 2-3 weeks)

### Step 2: Build the UGC Layer (5-10 variations)

Per avatar, brief UGC creators with:
- 1-page avatar
- Top 3 emotional triggers
- Specific hooks from the hook bank (assign 2-3 hooks per creator)
- Format requirements (typically 9:16 for Reels/Stories + 1:1 alternates)

Variation requirements:
- Different creators (matching avatars demographically)
- Different angles within same brand (problem-led / benefit-led / mechanism-led / lifestyle-led / surprise-benefit-led)
- Different hooks per creator
- Different durations (15s / 30s / 60s)

Goal: 5-10 UGC ads minimum. Each addresses a specific avatar × trigger × hook combination.

UGC role in portfolio: builds mental imagery of using product, peer-relatability.

### Step 3: Build the Static Layer (10+ variations)

Apply `/omar-static-composition` discipline (or run that workflow inline):
- 4-line grid composition
- Focal point = product
- Visual hierarchy 3-element rule
- Self-test audit per static

Variation engineering:
- Multiple compositions (not just color swaps — different layouts)
- 3 color palette shifts per composition (achromatic / analogous / complementary)
- Different hooks across statics
- Different proof elements deployed (review counts / publications / certifications / testimonials)

Goal: 10+ statics minimum. Andromeda diversity = different visual mass distributions.

Static role in portfolio: high-frequency scroll-stopping, low-cost variation production.

### Step 4: Build the Founder Layer (3-5 variations)

The founder layer is what UGC alone cannot deliver — premium trust signal answering "who's behind this?"

Per founder ad, brief includes:
- Story angle (origin / mission / mechanism / personal stake / values)
- Length (typically 60s-90s for founder content; can extend to 2-3 min for premium)
- Setting (production-quality matters — bedroom-camera erodes premium positioning)
- Hook (typically curiosity-led: "I built this for myself because...")

Variation requirements:
- Different stories (don't just re-shoot the same content)
- Different angles within founder POV (origin vs. process vs. why-not-others)
- Different length variations for testing

Goal: 3-5 founder ads. For premium brands, this is non-negotiable.

Founder role in portfolio: trust beyond UGC, premium positioning anchor.

### Step 5: Map Coverage to Awareness Pyramid

Cross-reference portfolio against awareness pyramid:
- Most-aware: which ads are offer-led / retargeting?
- Product-aware: which ads are comparison / mechanism?
- Solution-aware: which ads are category positioning / founder explainer?
- Problem-aware: which ads are problem-agitation / education?
- Unaware: which ads are pattern-interrupt / identity / story-led?

Identify gaps. If you have 0 ads at a stage, plan supplementary creative.

### Step 6: Andromeda Diversity Check

Meta's Andromeda algorithm rewards portfolio diversity. Per ad type, audit:
- Visual mass diversity (different focal points, different color palettes, different aspect ratios)
- Hook diversity (different opening lines, different trigger categories)
- Angle diversity (problem / benefit / mechanism / lifestyle / surprise)

Anti-pattern: 10 ads that all look like the same ad with text variations. Andromeda reads them as duplicates.

### Step 7: Build the Launch Schedule

Sequence:
- Week 1: Launch all 3 layers simultaneously, equal budget split
- Week 1 mid-week check: identify ads with statistical significance (typically 50+ clicks or $50+ spend)
- Week 2: Pause clear losers, increase spend on early winners
- Week 2 end: identify Iteration 1 candidates
- Week 3: Build iteration 1 (2x as many variations of winners + 2-3 new bets)

### Step 8: Build the Iteration Roadmap

Per Pattern 9 (Iteration Anchor Principle): each iteration builds on previous winners.

Iteration 1 brief template:
- Top 3 winning ads from launch
- For each: build 5 variations (different hooks, different visuals while preserving winning skeleton)
- Add 2-3 NEW bets based on learnings (e.g., "winners deployed Trust trigger, none deployed Fear yet — test Fear")

### Step 9: Deliverable

Produce `launch-portfolio-[brand]-[date].md`:
1. Portfolio scope (avatars, stages, budget, timeline)
2. UGC ad list (5-10 ads with brief per ad)
3. Static ad list (10+ ads with composition rationale per ad)
4. Founder ad list (3-5 ads with story angle per ad)
5. Awareness pyramid coverage map
6. Andromeda diversity audit
7. Launch schedule (week-by-week)
8. Iteration 1 roadmap

## Content Type Adaptations

| Brand Type | Adaptation |
|-----------|------------|
| Premium ecom (high AOV) | Founder layer is non-negotiable; budget split UGC/Static/Founder = 30/40/30 |
| Mass-market ecom | UGC dominant; Founder optional; budget split = 50/40/10 |
| Subscription DTC | Add subscription-specific ads (cancellation prevention messaging in UGC) |
| High-ticket info / coaching | Founder layer dominant; budget split = 20/20/60 |
| B2B service | Founder layer carries trust; UGC = client testimonials; Static = case-study based |
| Fashion / apparel | Static + UGC dominant; founder optional; emphasize lifestyle imagery |

## Output Requirements

The deliverable must include:
- ✅ Minimum 18-25 ads total (5 UGC + 10 Static + 3 Founder is floor; 10+5+5 is ideal)
- ✅ Per-ad brief specifying avatar × trigger × hook × format
- ✅ Awareness pyramid coverage map
- ✅ Andromeda diversity audit
- ✅ Launch schedule with iteration cycle
- ✅ Iteration 1 roadmap (built on launch winners)

## Quality Gate

Score against `genius.md` Quality Rubric Criteria 4 (Premium Aesthetic Consistency), 5 (Objection Pre-Handling), 6 (Awareness-Stage Match), 8 (Iteration Loop Closure). Pass condition: 7+/10 average across criteria.

**Veto**:
- Single ad type only → reject, build all 3 layers
- Pyramid coverage gap with no remediation plan → require unaware/problem-aware bridge content
- No iteration roadmap → reject (without iteration loop, this is a launch but not a system)

**Anti-pattern check**:
- "We'll do founder ads later" — no, founder layer is launch-day requirement for premium brands
- All ads target same avatar/stage → portfolio coverage failure, expand
- Statics that are color swaps of one design → Andromeda fails, redesign
- No objection pre-handling in any ad → revisit research-stack output and embed top objections
