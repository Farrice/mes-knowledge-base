---
description: Design product-led static ads using 4-line grid composition, focal point optics, color contrast engineering, and visual hierarchy 3-element rule
---

# 04 — Static Ad Composition System

> Per Omar: "Just take any high-performing ad creative that you have at your disposal and draw these four lines on top of it. What do you see? Almost all of them, specifically the ones from big brands, follow these lines to guide their composition."

The end-to-end visual design system for ecommerce static ads. Treats ad design as a photographic problem governed by optical physics, not a graphic-design problem governed by taste.

## Pre-Flight Gate

Run this workflow when:
- ✅ Designing a new product-led static ad
- ✅ Refreshing under-performing static creative
- ✅ Building static variations from a template
- ✅ Designing landing-page hero composition (same principles apply)

Skip when:
- ❌ Designing video ad (use video-storyboard process instead — this workflow is static-specific)
- ❌ Designing pure-typography ad (no product visual) — this workflow assumes product as focal point
- ❌ No avatar / no research yet (run `/omar-avatar-trigger-map` first — composition without psychology is decoration)

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Patterns 9-13: Composition Physics, Focal Point Optics, Color Contrast, Authority Hijacking, Visual Hierarchy)
- `skills/omar-eddaoudi-scaling-ops/references/visual-composition-grid.md` (the technical reference)

Recommended cross-reference:
- `skills/omar-eddaoudi-scaling-ops/references/avatar-template-1page.md` (the avatar this ad is for)
- `skills/omar-eddaoudi-scaling-ops/references/neural-trigger-categories.md` (trigger this ad deploys)

## Execution

### Step 1: Brief Lock-In

Before opening Figma, confirm:
- **Avatar**: Which 1-page avatar is this ad for?
- **Trigger**: Which of their top 3 triggers does this ad deploy?
- **Hook**: Which hook from the hook bank is this ad executing?
- **Awareness stage**: What stage of the pyramid is this targeting?
- **Format**: 1:1 (Meta feed) / 4:5 (Meta feed vertical) / 9:16 (Stories) / 1.91:1 (Meta link)?

If any field is undefined → halt. Composition without strategic anchor produces decoration.

### Step 2: Set Up the 4-Line Grid

In your design tool:
1. Create canvas at correct format dimensions
2. Add guides at 33% and 66% horizontal
3. Add guides at 33% and 66% vertical
4. Lock guides

You now have 4 lines + 4 power-point intersections (top-left, top-right, bottom-left, bottom-right of the inner third) and 1 center point.

### Step 3: Place the Focal Point

The focal point MUST be the product. Place product on or near a power-point intersection:
- Top-left or top-right → eye scans top first (Western reading pattern)
- Bottom-left or bottom-right → secondary placement, often used when copy is at top
- Center → use only for symmetric hero compositions; otherwise weakest placement

Engineering the focal point:
- Highest contrast in the scene
- Brightest area or sharpest focus
- Convergence lines pointing at it (real or implied)
- Negative space surrounding it
- If using human element, a hand holding the product directs eye automatically

### Step 4: Place the Secondary Element

The secondary element supports the primary by adding context. Common forms:
- Headline that names what the product does
- Key benefit callout
- Mechanism mention

Placement: Smaller than primary. Usually above or below primary. Aligned to one of the grid lines.

Weight rules:
- Smaller than focal point
- Lower contrast than focal point (or equal but smaller)
- Should NOT compete for first-glance attention

### Step 5: Place Tertiary Elements (Proof)

Tertiary elements seal the deal but don't dominate. Common forms:
- Star rating + review count
- "As seen in [publications]"
- Certifications / badges
- Customer testimonial pull-quote

Placement: Edges of canvas, low-saturation, smallest visual weight. Cluster together rather than scatter.

### Step 6: Color Contrast Engineering

Apply primary + secondary palette strategy:
- Brand primary colors anchor the design
- Add secondary palette for variation: achromatic (B/W/gray + brand) OR analogous OR complementary inverse
- Adjust based on aesthetic intent:
  - Achromatic + brand color → premium / editorial feel
  - Analogous → mood-driven, family resemblance
  - Complementary inverse → high-energy, scroll-stop power

For variation production: 3 secondary palette shifts × 1 base composition = 3 ads from one design.

### Step 7: Authority Hijacking (if deploying)

If this ad uses authority for trust transfer:
- Tier of authority: Niche micro-influencer > niche publication > niche practitioner > celebrity
- Slot placement: Tertiary by default. Promote to secondary or primary if authority IS the hook.
- Selection check: Would the avatar recognize this person without context?

### Step 8: Run the Self-Test Hierarchy Audit

The discipline:
1. Look at the design for exactly 1 second, then look away
2. Write down: 1st thing you saw, 2nd thing, 3rd thing
3. Compare to engineered intent
4. If misaligned → rearrange, re-test
5. Pass condition: order matches intent on 3 consecutive 1-second tests

Common audit failures + fixes:
- Headline read first instead of product → shrink headline or boost product visual mass
- Offer badge dominating → shrink to tertiary or remove
- Two elements competing → force one to dominate by size or contrast
- Nothing pops → increase contrast on intended primary

### Step 9: Variation Production

Once base composition passes audit:
- 3 color palette shifts → 3 variations
- 2-3 hook variations using same composition → 6-9 variations from one base
- Test for Andromeda diversity (different visual mass distribution, different focal-point intersections)

### Step 10: Deliverable

Produce:
- Final static(s) at correct format dimensions
- Composition rationale doc explaining: avatar / trigger / hook / focal point logic / hierarchy intent
- Variation set (minimum 3 from one base composition)

## Content Type Adaptations

| Format | Adaptation |
|--------|-----------|
| 1:1 (square) | All 4 power points usable; default product placement top-left or center |
| 4:5 (Meta vertical) | Use top-right or top-left power point; tertiary at bottom |
| 9:16 (Stories / Reels) | Composition layered top-to-bottom: product top, secondary middle, tertiary bottom |
| 1.91:1 (Meta link) | Use horizontal extension; product on left third, copy on right two-thirds |
| Carousel (multi-frame) | First frame = focal point dominance; subsequent frames build hierarchy progressively |
| Video thumbnail | Same principles, but increase contrast 20% (thumbnails compete with feed) |
| Email hero | Same principles, but secondary element more prominent (email reading pattern is content-first) |

## Output Requirements

The deliverable must include:
- ✅ Final composition(s) at correct dimensions
- ✅ Composition rationale doc (avatar / trigger / hook / focal point / hierarchy)
- ✅ Self-test audit log (3 consecutive passes)
- ✅ Minimum 3 variations from base composition
- ✅ Authority deployment notes (if applicable)
- ✅ Recommended split-test plan (which variations test against which)

## Quality Gate

Score against `genius.md` Quality Rubric Criteria 3 (Visual Hierarchy Discipline) + 4 (Premium Aesthetic Consistency) + 7 (Authority Specificity). Pass condition: 8+/10 on each applicable.

**Veto**:
- Self-test fails 3 attempts → composition broken, redesign
- Focal point ≠ product on product ad → redesign
- No grid alignment → redo with grid

**Anti-pattern check**:
- Multiple competing focal points → force dominance
- Loud background → mute background; preserve saturation only on product
- Big offer badge dominating → remove or shrink to tertiary
- Generic stock photography "professional" → replace with niche-specific authority

**Iteration check**: Are you building on a previous winning composition or starting from scratch? Iteration loop closure (Quality Rubric Criterion 8) requires explicit reuse of winning composition skeletons.
