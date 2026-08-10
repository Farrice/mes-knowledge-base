---
slug: evidential-still-life
name: Evidential Still Life
status: active
tier: tight
family: photographic
brands: [farrice-parallax, proof-to-market]
icps: [supplement-performance-founder]
platforms: [linkedin, substack]
tags: [teardown, carousel, rigor-artifact, raking-light, true-black, document-as-subject]
palette: "Neutral steel greys and paper white, background to unbroken black. One warm saturated note (the antagonist object) and nothing else. Roughly 8% of frame carries colour."
light: "One hard source raking low from camera left. Every highlight agrees with it — a hard specular point on wet surfaces, anisotropic streaks along the brush direction of the steel. No contradicting reflection anywhere."
texture: "Luminance-dependent grain: coarse in the shadow side, near-absent in the lit paper. Paper fibre, brushed-steel micro-scratches, wet-edge cockle. Optical falloff at the corners."
subject_bias: "One document and one antagonist object. It refuses a third element and it refuses a person — a body in frame turns evidence into a scene."
era: "Contemporary editorial still life shot on 1990s-era film stock."
refuses: "Wide shots. Colour beyond the single warm note. Any second light source. Clean or pristine anything. A styled or merchandised read — it must look found."
conditions: "Needs a rigor artifact the buyer recognises (COA, spec sheet, lab report, invoice) AND an antagonist object that physically damages it. The argument must be visible as damage, not adjacency."
anti_conditions: "Do not use where the message is aspirational or warm. It is an indictment format — it makes a case against something. Wrong for launch, celebration or founder-story content. Also wrong for a person-forward brand."
references: [reference-1.png, reference-2.png, reference-3.png]
provenance: "Built 2026-08-10 across six rounds against the Transparent Labs teardown. Final (v6-03, reference-3) is the 9b-coherent plate: WHEY PROTEIN ISOLATE — MILK CHOCOLATE, real published panel (28g/32g serving), the SKU the quoted reviews belong to. v1 rejected (fake tension, no capture layer). v2 scored 8/10 from Farrice (realism gate applied). v3 selected after adding subsurface scattering, specular agreement and luminance-dependent noise. 4 variants generated, 1 selected — reference-1 = v3-02, reference-2 = v3-04."
created: 2026-08-10
verified: 2026-08-10
---

## Null run

Not run as a bare null — this card was built from a directed brief rather than characterised from
an inherited asset. What stands in for it: **three rounds against the same fixed subject**, which
isolated the asset's behaviour more usefully than an empty prompt would have. The behaviour is
stable and stated in the frontmatter.

Honest limit: because it was never run against a *neutral* probe, the `tight` tier is inferred
from how completely the prompt determines the output, not measured against a null baseline. Run a
null before extending this card to a second brand.

## Probe run (what survives contact with direction)

Very little drifts. Across four variants at the same prompt, the constants held: raking light,
true black background, cockled wet paper, single warm note, empty lower third. What varied was
the document's own layout and the melt's position — which is the useful kind of variance, since
it means scene detail can be redirected without losing the look.

## What the three rounds actually taught

1. **v1 failed on capture, not on concept.** The tension was already right; the frames read as AI
   because no camera, no atmosphere, no imperfection and no black point were named.
2. **v2 (8/10) fixed realism but garbled the text.** The fix that mattered most was **prop
   provenance** — "a Certificate of Analysis with a crooked staple" instead of "a grid of
   numerals on matte paper." A described abstraction renders as an abstraction.
3. **v3 fixed the text, and this was the surprise.** I expected to need a compositing pass for
   typography. Naming the document's *real internal structure* — assay table, PASS column, lot
   number, NMT/NLT specs, APPROVED BY — was enough for the model to produce plausible, correct
   body copy at this density. **The compositing pass is not required at this text load.** It
   still will be for a full page of paragraph text.

## Layer 9 — contextual correctness (BINDING for this card)

This style always contains a legible document, so **the document's rows must be its real
contents** — sourced from the teardown/deliverable it accompanies, written into the prompt as
literal strings (headers and cell values), and **read back on the selected output at zoom**
before shipping. The v3 rounds proved the model garbles only what it is left to invent. A wrong
number in a legible cell is a factual-veto matter: the image is asserting a fact.

**And 9a — the FORM must come from a fetched real specimen, never from memory** (v4 scar: right
doses, but "Heavy Metals NMT 10 ppm" as one generic row — a founder clocks that instantly). For
supplement COAs the researched form is: per-element heavy metals (Arsenic/Cadmium/Lead/Mercury),
a METHOD column (HPLC · ICP-MS · USP <2021>/<2022>), µg-per-serving units, and "Below LOQ" /
"Absent" result formats, closed by the accredited-lab line. Specimen source logged in the sweep
log.

**And 9b — image, document, and copy must be ONE SKU** (v5 scar: a correctly-formed pre-workout
COA under chocolate ice cream, when the "tastes just like chocolate ice cream" reviews were the
whey isolate's — three assets, two products, zero coherence). Read the teardown to identify the
exact SKU the quoted evidence belongs to; the document carries that product's name, flavor,
serving size and real published panel; the antagonist object plays that SKU's own story.
Doctrine: `skills/style-vault/references/realism-floor.md` § ninth layer + 9a + 9b.

## Portable string per model

| Model | String / reference plan |
|---|---|
| gpt-image-2 | **Primary, verified.** Full `prompt.md` at `quality: high`, `imageCount: 4`, 4:5. Selection is mandatory, not optional |
| nano-banana-2 | Untested here. Pass `reference-1.png` and strip the prompt to document + antagonist + damage; let the reference carry light and grade |
| recraft-v3 | Not suitable — photographic, and depends on grain and specular behaviour |

## Do not use for

Anything where the brand is the hero. This format makes a case *against* a state of affairs, and
the object in frame is always the thing being indicted. For Jen's listings or any warm/aspirational
register, seed a different card.
