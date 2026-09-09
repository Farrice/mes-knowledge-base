---
version: alpha
name: MyBPM White Signal v2
description: Editorial New York restraint meets the mineral residue of an after-hours concrete room. The system borrows Kith's product-first quiet and Swiss-grid control, then makes it MyBPM through blackout structure, sublevel language, and a single acid signal.

colors:
  primary: "#0A0A0A"
  neutral: "#FFFFFF"
  surface: "#F7F7F4"
  secondary: "#5A5A56"
  tertiary: "#D7FF2F"
  border: "#D8D8D2"

typography:
  hero-display:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 112px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -0.05em
  headline-lg:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.04em
  headline-md:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -0.03em
  headline-sm:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  body-lg:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
  label-caps:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.18em
  caption:
    fontFamily: "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45

rounded:
  sm: 0px
  md: 0px
  lg: 0px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  xxl: 128px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 16px
  input:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 16px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  badge-signal:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 8px
  divider:
    backgroundColor: "{colors.border}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    size: 1px
---

## Overview

MyBPM White Signal v2 is a product-first storefront for premium EDM streetwear. Its cultural tension is deliberate: the controlled quiet of a Kith-like New York editorial shopfront against the physical afterimage of bass moving through concrete. White is the gallery; black is the architecture; acid is the signal that tells the right person where to act.

The brand should still feel specific without a logo. Large compressed statements, precise product grids, blackout campaign chapters, and lightly mineral surfaces carry the identity. The emotional target is belonging first and energy second—not festival spectacle.

## Colors

`colors.neutral` is Signal White, the default commerce canvas for navigation, product grids, product pages, and reading. `colors.primary` is Sublevel Ink, used for type, structural bands, and the strongest button. `colors.surface` is Mineral White, a selective editorial plane with barely visible marble veining. `colors.secondary` is Concrete Caption for supporting text only. `colors.tertiary` is Frequency Acid and is restricted to a single action, status, or proof point per viewport. `colors.border` is Quiet Joint, the hairline that makes the grid legible without card chrome.

## Typography

Inter is the sole family so the store stays fast, contemporary, and coherent across Shopify. `typography.hero-display` and `typography.headline-lg` carry short campaign statements; `typography.headline-md` and `typography.headline-sm` organize commerce and editorial chapters. `typography.body-lg`, `typography.body-md`, and `typography.body-sm` handle narrative, product information, and metadata. `typography.label-md`, `typography.label-caps`, and `typography.caption` provide the technical drop language. Never place more than two weights in one viewport.

## Layout

Use a fluid 12-column desktop grid with a 1440px working maximum, four product columns, and a 4px-to-8px grid gap. Mobile uses two product columns and near-edge-to-edge imagery. The spacing scale—`spacing.xs`, `spacing.sm`, `spacing.md`, `spacing.lg`, `spacing.xl`, and `spacing.xxl`—creates contrast between dense commerce and slower editorial chapters. The header stays visually quiet so product imagery owns the first read.

## Elevation & Depth

The system is flat by default: no decorative shadows and no floating cards. Depth comes from full-bleed photography, black-to-white chapter changes, `colors.border` hairlines, and one restrained Mineral White surface. Marble is rendered as very low-contrast linear and radial gradients; it must remain subordinate to product photography.

## Shapes

The geometric register is sharp. `rounded.sm`, `rounded.md`, and `rounded.lg` are all zero because square product frames and square controls feel more editorial and less app-like. `rounded.full` is reserved for accessibility-only states or a future circular media control, never commerce buttons or badges.

## Components

`components.button-primary` is black on white; its `components.button-primary-hover` state becomes Frequency Acid with black text. `components.button-secondary` is a white field with black type and a structural border supplied by the implementation. `components.input` remains white and square. `components.card` has no internal padding so the image grid reads continuously. `components.badge-signal` uses acid only for verified drop status or the main conversion cue. `components.divider` carries Quiet Joint as the one-pixel grid line.

## Do's and Don'ts

- Do keep Signal White as the dominant page area across home, collection, and product pages.
- Do use Mineral White on one editorial transition at a time; the texture should disappear at a glance and reward closer inspection.
- Do reserve Frequency Acid for one action or proof signal per viewport.
- Do make campaign photography full-bleed and product photography consistent at a 4:5 portrait ratio.
- Don't reproduce Kith logos, copy, proprietary modules, or page layouts; borrow only transferable principles such as curation, restraint, density, and hierarchy.
- Don't use brown, cream, beige, generic neon gradients, lasers, equalizers, or psychedelic interface effects.
- Don't add shadows, rounded cards, or app-like pills to manufacture “premium.”
- Don't promote a product into the hero edit until its sample, data, and image proof clear the launch gate.
