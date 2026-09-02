---
name: five-reference-jen-design-systems
problem_signature: "turn five visually distinct social reference packs into repeatable Jen design systems without flattening them into one brand template"
domain: system
tags: [design-system, carousel, jen-santulan, visual-proof, reference-harvest]
date: 2026-09-02
status: active
session: "01a0635d-e158-7013-8701-872e10079486"
---

## Problem

Five social carousel packs were all desirable, but combining their palettes and motifs would erase the contrast Farrice liked. Describing each as a mood was also too weak to reproduce reliably from new content.

## Root Cause

The reusable unit was being framed as a template or brand palette. The references actually worked through distinct editorial grammars: content job, type tension, photo treatment, hierarchy, repeated furniture, slide rhythm, and strict clutter limits.

## Approach That Worked

1. Preserve five independent engines. Give them one bounded Jen layer for identity, voice, accessibility, provenance, fair-housing safety, and human approval only.
2. Convert each reference into both blind-designer prose and machine tokens, then prove transfer by rendering Jen/Valley imagery without loading the original slides.
3. Pair the full-resolution assets with a compressed self-contained visual atlas. The first atlas was 18 MB; resized embedded review copies reduced it to 2.5 MB while preserving the original 1080×1350 proofs.

## Dead Ends

macOS Quick Look rendered four of five SVG slides, then failed silently on the last. A local headless-browser screenshot recovered it. The first quality receipt also used a 1–5 intent score in a 1–10 field; the work was not changed to manufacture a pass, but the receipt was rerun with the documented rubric anchors.

## Verification

`verify.py` passed five systems, 27 hashed source slides, 15 transfer proofs, and exact 1080×1350 output. JSON parsing, Python compilation, export-format guard, `git diff --check`, full contact-sheet review, and selected full-resolution slide review passed. Jen taste approval, a full production carousel, Canva editability, and audience response remain untested.

## Weaker-Model Trap

A weaker pass will merge the five references into “warm editorial,” save only colors and fonts, or copy their surface decoration. It will also call a generated mood board proof. Require separate system IDs, content-job routing, allowed variation, failure signs, source hashes, and transfer images using a different subject.

## Pointers

- `_active/clients/jen-santulan/foundation/social-design-systems/README.md`
- `_active/clients/jen-santulan/foundation/social-design-systems/SYSTEM-ATLAS.html`
- `_active/clients/jen-santulan/foundation/social-design-systems/systems.json`
- `_active/clients/jen-santulan/foundation/social-design-systems/render.py`
- `_active/clients/jen-santulan/foundation/social-design-systems/verify.py`
