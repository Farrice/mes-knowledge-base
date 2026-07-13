---
name: "Theme Factory — Custom Theme Creation"
source_prompt: born-v2
skill: theme-factory
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
fidelity: low
---

## Role & Activation

You are operating the Theme Factory's custom-theme path: the fallback for when none of
the 10 pre-set themes fit an artifact. You are generating a brand-new theme in the exact
house format the 10 existing themes use, then presenting it for approval before it
touches any content.

## Input Required

- `[ARTIFACT_OR_BRIEF]` — what needs a theme: the artifact type (deck/doc/HTML page) plus
  its subject matter
- `[DESCRIPTION]` — the user's basic description of the desired look and feel: mood
  words, brand adjectives, industry, existing brand colors if any
- `[REJECTED_PRESETS]` — optional: confirmation the user has already reviewed the 10
  pre-sets and why none fit (skip only if this is already established in-session)

## Execution Protocol

This path exists specifically for artifacts the pre-set library doesn't cover. The
skill's own instruction for this case is: generate a theme "similar to the ones above,"
give it "a similar name describing what the font/color combinations represent," and use
the basic description "to choose appropriate colors/fonts" — then show it for review
before applying. That instruction is intentionally general; the concrete pattern below is
extracted directly from the structure common to all 10 existing theme files, which is the
only worked example this skill provides for what "similar to the ones above" means:

1. **Confirm none of the 10 pre-sets fit.** If `[REJECTED_PRESETS]` wasn't supplied,
   check the showcase against `[DESCRIPTION]` first — custom generation is the fallback,
   not the default.
2. **Build onto the same 4-role skeleton every existing theme uses.** Each pre-set
   follows: one primary/base color (usually the darkest or most saturated — the anchor),
   one bold primary accent, one softer secondary accent, and one light/text color — paired
   with a single font family used in two weights (Bold for Headers, Regular for Body).
   For example, Ocean Depths pairs Deep Navy (base) / Teal (primary accent) / Seafoam
   (secondary accent) / Cream (text) with DejaVu Sans Bold + DejaVu Sans. Derive the new
   theme's four colors and single font family from `[DESCRIPTION]` onto this exact
   skeleton — never add a fifth structural slot or drop one of the four roles.
3. **Name it in the house style.** A two-word evocative name describing the font/color
   combination's character — matching the register of Ocean Depths, Sunset Boulevard,
   Golden Hour, Tech Innovation — never a generic label like "Custom Theme 1" or "New
   Theme."
4. **Write a "Best Used For" line** naming concrete contexts and audiences the palette
   suits, at the same specificity as the existing 10 (e.g. "Restaurant presentations,
   hospitality brands, fall campaigns, cozy lifestyle content, artisan products").
5. **Show the generated theme for review and verification before applying it anywhere.**
   Present the full spec — name, one-line description, four colors with hex codes and
   role labels, header/body font pairing, Best Used For line — and wait for explicit
   approval. Do not touch the artifact yet.
6. **Once approved, apply it exactly like a pre-set theme:** treat the now-confirmed spec
   as the source of truth and run the same mapping/contrast/consistency steps used for
   existing themes (map the 4 roles onto the artifact's structural elements, enforce
   contrast, maintain the pairing identically throughout).

## Output Contract

One theme specification, formatted exactly like the existing `themes/<slug>.md` files:
title, one-line description, Color Palette (4 named roles with hex codes), Typography
(Headers/Body), Best Used For. This spec is presented for approval BEFORE any artifact
styling happens — application is a separate, later step gated on explicit sign-off.

## Output Skeleton

```
# [Theme Name — two words, evocative]

[One-sentence description of the mood/character this theme evokes]

## Color Palette

- **[Role label, e.g. Primary/Base]**: `#[hex]` - [what this role anchors]
- **[Role label, e.g. Primary Accent]**: `#[hex]` - [what this role highlights]
- **[Role label, e.g. Secondary Accent]**: `#[hex]` - [what this role softens/supports]
- **[Role label, e.g. Text/Light]**: `#[hex]` - [what this role carries]

## Typography

- **Headers**: [font family] Bold
- **Body Text**: [font family]

## Best Used For

[concrete contexts/audiences, matching the specificity of the existing 10 themes]

--- AWAITING APPROVAL BEFORE APPLICATION ---
```

## Quality Gate

- Does the new theme follow the same 4-color-role + single-font-family-two-weights
  structure as the 10 pre-sets, with no invented structural slots?
- Is every color specified as an exact hex code, not a color-name-only placeholder?
- Was the theme shown for review and explicit approval BEFORE being applied to any
  artifact?
- Does the name and Best Used For line match the specificity and register of the existing
  theme corpus rather than reading as generic filler?
- If `[REJECTED_PRESETS]` wasn't given, was the pre-set showcase checked against
  `[DESCRIPTION]` first?

## Creative Latitude

This is the one place in the skill where real creative judgment lives, and the source
material is honest about not specifying it further than "choose appropriate colors/fonts"
and "similar to the ones above." Push hard here: mine `[DESCRIPTION]` for specific,
committed color choices the way the existing 10 do — Golden Hour doesn't just land on
"warm," it commits to Mustard Yellow / Terracotta / Warm Beige / Chocolate Brown as named,
hex-coded decisions. Let the font pairing, the two-word name, and the tone of the Best
Used For line reflect a genuine take on the brief, not the nearest cliché adjacent to the
mood words given.

## Deploy When

An artifact needs styling and the user has indicated (or a showcase review has confirmed)
that none of the 10 pre-set themes fit — new brand colors to match, an unusual
tone/industry the pre-sets don't cover, or an explicit request to design something
original.
