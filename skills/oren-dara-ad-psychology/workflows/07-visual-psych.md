---
description: Add the visual psychology layer most strategists skip — use-of-multiples scroll-stops, Z/F grid eye-trails, visual value-props, and opinion-based comparison framing.
---

# `/adpsy-visual-psych` — Visual Psychology Layer

> Dara: "creative strategists will focus on the messaging or the written hook and not as much on like, oh, what can you do psychologically visually?"

The Kettle & Fire lesson: the winning value prop wasn't taste — it was **space savings**, and only the visual could say it ("this much boxed bone broth versus one jar"). Devices from the source: **use of multiples** ("one of those really easy hacks that stops the scroll"), **grid formats** ("your eye actually trails in a Z or F format — it has this natural hooking effect"), and **visual comparison**.

## Pre-Flight Gate

- Is there a concept/message already chosen (from 01–06)? This workflow layers visual mechanics onto a concept — it doesn't originate one.
- Full static build → this feeds `/dara-static-engine` Layer 2; don't duplicate its 1-second gate here, invoke it.

## Skill Acquisition

Read `genius.md` (Tactic 5) + `references/source-quotes.md` Tactic 5 block + frame notes in `extractions/oren-dara-ad-psychology/visual-context.md` (the stacked-boxes frame is the calibration image).

## Input Required

- **[THE CONCEPT]**: message, persona, chosen tactic
- **[PRODUCT PHYSICALITY]**: what it looks like, sizes, multiples potential, what the category shelf looks like
- **[VALUE-PROP CANDIDATES]**: including any *spatial/physical* ones (space, quantity, fit, size difference)

## Execution

1. **Hunt the visual value prop.** Before styling anything, ask: is there a value prop only the eye can get instantly (space savings, quantity-per-dollar, fit difference, before/after)? If yes, it may outrank the messaging — that's the Kettle & Fire discovery.
2. **Apply the multiples test.** Would stacking/multiplying the product (or the competitor's bulk) stop the scroll? Spec the arrangement: what's multiplied, what's singular, what the contrast says.
3. **Apply the grid/eye-trail test.** For grid-shaped content: place the hook where the Z/F trail starts (top-left), payoff along the trail. Fashion translation (Oren): fit-of-the-tee comparisons.
4. **Frame comparisons legally.** Visual side-by-sides stay opinion/experience-based — "we're not technically making any claims… it was opinion-based." Reactions and appearances, not measured superiority claims.
5. **Audit an existing concept** (alternate mode): score the concept's current visual layer — does anything work psychologically before the copy is read? Name the missing device.
6. **Hand off**: static render → `/dara-static-engine` (its Layer 2 hierarchy + 1-second gate apply); comparison grids → `/dara-comparison-callout`; trigger-level audit → `meg-heckman-buyer-trigger-os` 50ms gate.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Multi-SKU/apparel | Grid statics; fit comparisons |
| Consumables | Multiples of servings vs competitor bulk; space/count contrasts |
| Video | Multiples as a hook frame (first 1s), then normal sequence |
| Organic repost | The visual device should read WITHOUT sound |

## Output Requirements

Visual Psychology Spec: visual value-prop verdict (found/none, ranked vs messaging) · device specs (multiples arrangement / grid trail map / comparison framing) · legal framing note · handoff line. In audit mode: present-layer score + the one missing device.

Execution prompt: `references/prompts-v2/07-visual-psych-spec.md`

## Quality Gate

Rubric: visual psychology ≥7 (at least one deliberate device; visual carries meaning pre-copy). Automatic fail: decoration described as psychology (a device must change what the eye does or knows), or a comparison that makes measurable claims without measurement.
