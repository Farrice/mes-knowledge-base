---
slug: farrice-avatar
name: Farrice Avatar (frbpm)
status: active
tier: tight
family: character
brands: [farrice-parallax]
icps: [invisible-expert]
platforms: [linkedin, instagram, substack]
tags: [character-lock, identity, shonen-cel, not-a-style]
palette: "Cyan-on-black lighting accents over warm brown skin and matte black wardrobe. Two-step cel shadows, no gradient."
light: "Clean key-visual lighting with cyan rim accents. Anime cel logic, not photographic falloff."
texture: "Digital cel — sharp linework, flat fills, two-step shading. No grain, no material rendering."
subject_bias: "One specific person. This asset IS the subject; it does not describe a world."
era: "Modern shonen anime key visual, twilight register."
refuses: "Any deviation from the LOCKED identity column — tapered fade, thin mustache + soul-patch goatee, matte-black headphones with cyan ring. Text, logos, watermarks."
conditions: "Always pass 2-3 dataset refs closest to the target shot. Canon and usage recipe: _active/farrice-brand/05-assets/anime-avatar/CANON.md"
anti_conditions: "Never re-describe the locked features ad hoc — quote the CANON identity map. On drift, snip-and-refeed (mickmumpitz), never reword."
references: [reference-1.png, reference-2.png]
provenance: "Existing locked character. Canon lives in _active/farrice-brand/05-assets/anime-avatar/. Backfilled into card format 2026-08-09."
created: 2026-08-09
verified:
---

## Null run (what the asset does with no direction)

**NOT APPLICABLE, and the reason matters.** A null run characterizes a *style's* prior — what
it does when you say nothing. This entry is a **character lock**, not a style: it carries
identity, not aesthetic. Running it with an empty prompt tells you nothing you don't already
know from CANON.md.

It lives in the vault because it must be *retrievable by brand and platform* alongside styles,
but it plays a different role — it answers "who is in the frame," never "what does the frame
look like." A style card and a character card can and should be combined.

`verified` stays empty here for a different reason than the other two: the character is
already proven in production, but it has not been verified *through this vault's contract*
(portable string per model, confirmed by a dated run). Set it after the first vault-routed run.

## Portable string per model

| Model | String / reference plan |
|---|---|
| nano-banana-2 | **Primary** — `--reference` with 2-3 CANON dataset images nearest the target shot |
| flux-2 | Escalation when nano-banana-2 drifts on the headphone ring or fade line |
| recraft-v3 | Not suitable — character identity needs raster reference conditioning |

## Do not use for

Client work. This is Farrice's own likeness; it has no place in Jen, Proof-to-Market or any
client-facing asset.
