---
slug: turrell-light-gallery
name: Turrell Light Gallery
status: active
tier: tight
family: photographic
brands: [farrice-parallax]
icps: [invisible-expert]
platforms: [substack, web]
tags: [architectural, light-as-subject, film, editorial-cover]
palette: "Muted violet #8A74A0, desaturated teal #698B8B, warm amber #D28A00 against raw concrete grey. Colour arrives as LIGHT, never as pigment on a surface."
light: "Layered planes of coloured light through a rectangular aperture; dusk ambient. Beams are visible volumes (dust in air), not glows."
texture: "Medium-format film grain, formwork marks in concrete, hairline cracks, mineral deposits, imperfect poured floor. Shadow colour-shift and slight chromatic aberration."
subject_bias: "Architecture and volume. Bodies appear only for scale — small, dark, motion-blurred, never the subject."
era: "Contemporary gallery documentation shot on 1990s-era film stock."
refuses: "Faces. Text-safe crops on the short edge. Anything glossy, digital-clean, or symmetrical. It will not render a warm domestic interior."
conditions: "Needs an architectural container and an aperture. Works when the brief's subject is a THRESHOLD, a reveal, or an idea arriving."
anti_conditions: "Do not use for people-forward content, product shots, or anything needing a friendly register. Reads cold and institutional on social."
references: [reference-1.png]
provenance: "Proven on the Parallax cover (v3, kept). Backfilled into card format 2026-08-09."
created: 2026-08-09
verified:
---

## Null run (what the asset does with no direction)

**NOT YET RUN.** Everything characterized above is read off the existing `prompt.md`, which
states these properties explicitly — that is inference from a description, not evidence from
an output. The null run (this style against a neutral one-character probe, nothing else) has
not been performed, which is why `verified` is empty and the card reports GAP.

## Probe run (what survives contact with direction)

Pending. The delta between null and probe is this asset's real strength; until both are run,
its tier (`tight`) is an assumption based on how specific the prompt string is.

## Portable string per model

| Model | String / reference plan |
|---|---|
| nano-banana-2 | Pass `reference-1.png` via `--reference`; prompt carries subject + aperture only, let the reference carry palette and grain |
| flux-2 | Full prompt string from `prompt.md`; escalate here when the reference fights the composition |
| recraft-v3 | Not suitable — this style is photographic and depends on grain; recraft is the vector lane |

## Do not use for

Anything with a face as the subject. The style is about light in a room; a person in it
becomes a silhouette, and a silhouette cannot carry an ICP's emotional state. For
audience-facing scene work, seed a different card.
