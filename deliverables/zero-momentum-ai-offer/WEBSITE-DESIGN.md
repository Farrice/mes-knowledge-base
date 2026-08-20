---
version: alpha
name: Parallax Service Website
description: "A conversion-focused extension of Parallax for a B2B service website, not an enlarged newsletter cover. Swiss information discipline meets the quiet operational confidence of an aircraft checklist: modern neo-grotesk typography, compact proof, and one controlled violet signal."

colors:
  ink: "#1C1C1E"
  violet: "#7B61FF"
  violet-on-light: "#6D50F3"
  violet-on-dark: "#8F79FF"
  warm-white: "#F5F0EB"
  primary: "{colors.ink}"
  accent: "{colors.violet}"
  neutral: "{colors.warm-white}"
  surface: "{colors.ink}"
  on-surface: "{colors.warm-white}"
  on-accent: "{colors.warm-white}"

typography:
  hero-display:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 68px
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: -0.035em
  headline-lg:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: -0.025em
  headline-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
  body-lg:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.62
  body-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
  label-md:
    fontFamily: "SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.06em
  label-sm:
    fontFamily: "SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.08em
  caption:
    fontFamily: "SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45

rounded:
  none: 0px
  sm: 2px
  md: 4px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 88px

components:
  button-primary:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.warm-white}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-white}"
  button-secondary:
    backgroundColor: "{colors.warm-white}"
    textColor: "{colors.ink}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 16px
  input:
    backgroundColor: "{colors.warm-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px
  card:
    backgroundColor: "{colors.warm-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
---

## Overview

This extension translates Parallax into a functioning B2B service website. It retains the recognizable wordmark, three type roles, ink, warm white, and a single violet signal. It rejects the earlier mistake of treating every section like a newsletter cover.

The visitor should feel that a precise operator built the page: calm enough to read, dense enough to trust, and direct enough to act. Swiss information discipline controls alignment and hierarchy. An aircraft checklist supplies the second anchor: statuses are legible, exceptions are explicit, and no action occurs without a named owner.

## Colors

Warm White is the primary reading canvas. Ink carries text and one demonstration surface. Canonical Violet is reserved for non-text signals, rules, and focus treatment. Two same-hue accessibility variants carry small text and controls: `#6D50F3` on Warm White and `#8F79FF` on Ink. Derived borders and muted text may use these colors with opacity; no new hue enters the system.

## Typography

Helvetica Neue carries both headlines and reading copy, creating one clean neo-grotesk voice across the page. The system falls back through Helvetica, Arial, and the platform sans-serif, so the page no longer depends on a remote font request. SF Mono or the platform monospace is reserved for operational metadata. Display scale is capped at 68px so the headline leads a website rather than becoming a poster.

## Layout

The page uses a centered 12-column grid, 1184px maximum width, 32px desktop gutters, and 20px mobile gutters. Standard sections use 88px vertical padding, reducing to 64px on tablet and 56px on mobile. The hero is content-driven and capped near 720px; it does not claim an arbitrary full viewport.

The default density is “one screen, one decision,” not “one screen, one sentence.” Each section must resolve a visitor question and reveal enough of the next section to maintain scroll continuity. Reading columns stay below 64 characters.

## Elevation & Depth

The system is flat. Depth comes from inversion: Warm White page, Ink demonstration panel, Warm White final call-to-action within an Ink band. Borders use the current foreground color at low opacity. No shadows, gradients, blur, glow, or faux glass.

## Shapes

Corners are architectural and nearly square. Two pixels are allowed for buttons to improve touch affordance. Panels, rows, inputs, and information blocks remain square.

## Components

The sticky header contains a compact wordmark, three anchor links, and one primary CTA. The hero pairs a clear offer statement with a functioning workflow demonstration rather than a decorative illustration. Proof appears as one compact strip. Process uses three stages. Scope uses a readable two-column comparison. FAQ uses native disclosure elements. The final CTA states exactly what the visitor should bring and keeps the missing booking destination honest.

## Do's and Don'ts

- Do show useful content below the fold in the initial laptop viewport.
- Do cap standard section padding at 96px desktop and 72px mobile.
- Do use Violet for one primary action or active state per viewport.
- Do let the workflow demonstration carry the visual interest.
- Do keep proof state and exclusions visible without making them the headline.
- Don't create empty release zones, giant text walls, or poster-like section reveals.
- Don't repeat the same claim in a hero, proof band, section headline, and CTA.
- Don't add cards when a rule, row, or two-column alignment communicates the relationship.
