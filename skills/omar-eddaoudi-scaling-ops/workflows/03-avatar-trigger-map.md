---
description: Build 2-4 condensed-juice 1-page avatars + neural marketing trigger map per avatar + 20-hook bank ready for ad production
---

# 03 — Avatar + Neural Trigger Map

> Per Omar: "I see all these reports being like 70 pages long but nobody reads them. I just need one page with all this condensed data. It's like condensed juice."

Translates customer research into the bridge artifact between research and creative production. After this workflow, copywriters can write hooks without re-doing research.

## Pre-Flight Gate

Run this workflow when:
- ✅ Customer Research Stack (`/omar-research-stack`) is complete
- ✅ About to brief creative team (UGC creators, copywriters, designers)
- ✅ Existing avatars feel theoretical / aren't being used by team
- ✅ CAC inflation suggests avatar is wrong or stale

Skip when:
- ❌ Research stack not yet complete (run `/omar-research-stack` first)
- ❌ Avatars updated within 90 days with no significant data shift

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Patterns 5-6: Avatar-as-Condensed-Juice + NMTM)
- `skills/omar-eddaoudi-scaling-ops/references/avatar-template-1page.md`
- `skills/omar-eddaoudi-scaling-ops/references/neural-trigger-categories.md`
- `skills/omar-eddaoudi-scaling-ops/references/awareness-pyramid-mapping.md` (avatars often live at different awareness stages)

## Execution

### Step 1: Determine Avatar Count

Use brand stage as anchor:
- Pre-launch / early scale ($0-$50K/mo) → 2 avatars
- Growth ($50K-$500K/mo) → 3 avatars
- Scale ($500K+/mo) → 4 avatars
- Mature ($5M+/yr) → 4 avatars (don't expand past 4)

### Step 2: Cluster Customer Research Into Avatar Groups

From research stack synthesis, identify natural clusters:
- Different demographic patterns (age, life-stage, income)
- Different problem framings (root cause vs. symptom)
- Different language patterns (technical vs. emotional)
- Different awareness stages (most-aware vs. unaware bands)

Each avatar should have:
- A distinct dominant problem framing
- A distinct emotional trigger profile
- A distinct verbatim language signature

If two clusters produce similar avatars → merge. You probably had one avatar, not two.

### Step 3: Build Each Avatar to 1-Page Constraint

Use the template structure:
- Name + descriptor (real-feeling, not "Avatar 1")
- Who they are (2-3 sentences max)
- Problem in their own words (verbatim)
- What they've tried (with reasons it failed — verbatim)
- Their language (5-10 verbatim phrases from research)
- What would make them buy today (single sentence)
- What's stopping them (single sentence — dominant pre-purchase objection)
- Top 3 emotional triggers (rank-ordered)

**Hard constraint**: 1 page MAX. If you exceed, cut. Avatar utility is INVERSELY proportional to length.

### Step 4: Run Avatar Quality Checks

Per avatar, validate:
- [ ] Could a copywriter who never met this customer write a hook from this avatar?
- [ ] Are 5+ phrases verbatim from research data?
- [ ] Does the avatar have a unique pre-purchase objection?
- [ ] Are top 3 triggers different from other avatars' triggers?

If any avatar fails any check → rebuild that avatar.

### Step 5: Build NMTM Per Avatar

For each avatar, complete the 6-trigger matrix:
- Fear / Desire / Social Proof / Cognitive Bias / Urgency / Trust
- Specific trigger × Intensity (1-10) × Ad deployment example × Funnel stage best fit

Identify TOP 3 triggers per avatar (intensity × stage-fit). These become the primary creative levers.

### Step 6: Map Avatars Across Awareness Pyramid

Place each avatar at their dominant awareness stage:
- Most-aware avatars → offer-led + retargeting creative
- Product-aware → comparison + mechanism creative
- Solution-aware → category positioning + founder ads
- Problem-aware → problem-agitation + education
- Unaware → pattern-interrupt + identity content

If all avatars cluster at one stage → flag. You're missing pyramid coverage.

### Step 7: Generate Hook Bank Per Avatar

Use the hook bank prompt (in NMTM reference) per avatar:
- 20 hooks per avatar
- Distribution: 7-7-6 across top 3 triggers
- Each hook tagged with trigger, format (static/video), and rationale

Total deliverable: 40-80 hooks across 2-4 avatars.

### Step 8: Compile Avatar + Trigger Deliverable

Produce `avatars-and-triggers.md`:
1. Avatar count rationale (why 2 / 3 / 4)
2. One page per avatar
3. NMTM matrix per avatar
4. Awareness-stage map
5. Hook bank (organized by avatar)
6. Identified pyramid coverage gaps (if any)

## Content Type Adaptations

| Avatar Type | Adaptation |
|-------------|-----------|
| B2C ecom standard | Use template as-is |
| B2B service | Add "decision-making role" + "approval process" sections |
| High-ticket coaching/info | Add "transformation desired" + "identity threat from inaction" sections |
| Subscription product | Add "cancellation triggers" — cancellation reasons reveal hidden objections |
| Marketplace platform | Build BOTH supply-side and demand-side avatars (different incentive structures) |

## Output Requirements

The deliverable must include:
- ✅ 2-4 avatars (matched to brand stage), each on 1 page max
- ✅ NMTM matrix per avatar with TOP 3 triggers identified
- ✅ Awareness-pyramid placement per avatar
- ✅ Hook bank: 20 hooks per avatar, tagged by trigger
- ✅ Pyramid coverage gap analysis (if applicable)
- ✅ Recommended next workflow (typically `/omar-launch-portfolio` for new brands or `/omar-static-composition` for visual production)

## Quality Gate

Score against `genius.md` Quality Rubric Criteria 2 (Customer Language Authenticity) + 6 (Awareness-Stage Match). Pass condition: 8+/10 on each.

**Veto**:
- Avatar exceeds 1 page → reject and condense
- No verbatim customer language in avatar → reject, return to research stack
- Top 3 triggers identical across multiple avatars → you have one avatar, merge

**Anti-pattern check**:
- Generic demographic-tier avatar ("28-35 women interested in wellness") → rebuild with research-grounded specifics
- Universal triggers ("they want to feel good") → re-derive trigger specificity from research
- Hook bank skipped or done off the cuff → re-do via NMTM-driven brief, not vibes
- All avatars cluster at one awareness stage → flag pyramid gap, plan unaware/problem-aware bridge content
