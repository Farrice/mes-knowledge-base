# Farrice Cain — PHOTOREAL character canon (living)

Sibling to the anime canon at `../anime-avatar/CANON.md` (trigger `frbpm`). Same person, two
registers. The anime lane is style-authored from a captioned dataset; **this lane is Soul-authored** —
identity comes from a trained model, not from stacked references. That difference decides every rule
below.

Method: `skills/mickmumpitz/workflows/01-character-lock-dataset.md` (consistency budget, signature-detail
anchors, honest-folder acceptance) + the Higgsfield `character-sheet` workflow's anti-AI realism module.

## The spine

| | |
|---|---|
| **Soul reference ID** | `8a838508-bd60-4510-ae22-d76be30fab35` (name: Farrice, type `soul_2`, status completed) |
| **Model** | `text2image_soul_v2` — 0.12 credits/image at 2k |
| **Cinematic sibling** | `soul_cinema_studio` — same price, adds `style_id` + 21:9 |
| **Hard constraint** | **At most ONE image reference** alongside the Soul ID. The anime lane's 2–3-ref chaining does not transfer. |

## The rule that governs every prompt

**Do not describe his face.** The Soul carries face geometry, skin, fade, mustache and goatee.
Describing them in the prompt fights the identity model and degrades likeness.

This is the same discipline as the anime canon arriving from the opposite direction: mickmumpitz holds
that LOCKED properties are *deliberately under-captioned* so they weld to the trigger. Here the Soul
is the trigger. Silence is what lets it work.

Prompts describe: **wardrobe · expression · pose/action · setting · lighting · framing.** Nothing else.

## Consistency budget

| LOCKED — never described in prompt | VARIABLE — varied AND named every time | FREE |
|---|---|---|
| Face geometry · warm brown skin · tapered natural fade · thin mustache + soul-patch goatee · photoreal unretouched register | Wardrobe (W1/W2/W3 below) · expression · pose & action · setting · lighting · framing & scale · headphones on-ears vs around-neck | Background incidental detail |

**Signature detail:** matte-black over-ear headphones with a thin cyan accent ring. Carried over from
the anime canon deliberately — it is what makes both registers read as one person rather than two
unrelated assets. First thing the acceptance test checks.

## Wardrobe families (captioned VARIABLE, never half-captioned)

- **W1 — anime-canon.** Black bomber jacket over white crew-neck tee, black slim-fit pants, clean white
  low-top sneakers. Welds the photoreal lane to `frbpm`.
- **W2 — elevated business-casual.** Charcoal merino overshirt over fine-gauge black knit, dark indigo
  denim, clean dark leather boots. The authority register: LinkedIn, client-facing, Parallax.
- **W3 — Kith / comic-collab aesthetic.** Boxy heavyweight cotton crewneck with a faded vintage
  comic-panel halftone graphic in muted primary red and blue, relaxed-fit cream cotton trousers, clean
  low-profile leather sneakers.

**W3 craft note.** Prompting a named licensed character ("Batman on the chest") returns a mangled
trademark, not the fit — image models render licensed graphics badly. W3 targets Kith's *design
grammar* (boxy heavyweight cotton, muted tonal palette, relaxed cuts, premium knits) plus comic
*language* (halftone print, faded primary red/blue, vintage panel graphics), with `no logos` in the
negative tail. For a specific real garment, supply a photo of it as the one permitted image reference —
a better picture, never a better adjective.

## Reusable prompt modules

**Realism (mandatory on every photoreal generation):**
> visible fine skin texture with natural pores, subtle asymmetry and texture irregularity,
> matte-to-natural complexion completely free of glare, shine or highlight blooms, no digital
> smoothing, no beauty filter, no AI-airbrushed look, naturally muted catchlights with no oversized
> specular glare in the iris, high-end but unretouched editorial photography

**Negative tail:**
> No text, no watermark, no logos, no extra people, no duplicate figures, no distorted anatomy

**Signature:**
> matte-black over-ear headphones resting around the neck with a thin cyan accent ring
> *(on-ears variant: "worn on the ears with a thin cyan accent ring")*

## Usage recipe

```bash
higgsfield generate create text2image_soul_v2 \
  --prompt "<framing>, <expression>, <wardrobe>, <signature>, <light: named source + direction>, \
            <environment>, <REALISM MODULE>. <NEGATIVE TAIL>." \
  --custom-reference-id 8a838508-bd60-4510-ae22-d76be30fab35 \
  --quality 2k --aspect-ratio 3:4 --wait
```

Light must be **named and placed** (source, direction, quality) — "beautiful lighting" is a silent
delegation to the model's defaults.

## The reference law (v1 — learned the expensive way, 9 images)

The single image reference is powerful enough to **override the Soul entirely**. What the reference
*is* decides whether you get your face or the reference's.

| Reference type | Result | Verdict |
|---|---|---|
| **Flat-lay / hanger product shot** | Model reproduces the product photo. **No person at all.** (K1 Matrix hoodie, K4 Crest overshirt) | ✗ never use alone |
| **On-model, front view, face visible** | Soul identity holds; garment fit, colourway, wash, brand tab, styling, backdrop and lighting all transfer (M1 Peanuts) | ✓ **the lane** |
| **On-model, back view, no face** | Reference wins completely — wrong person, wrong hair (M3 Knicks bomber) | ✗ never |

**The rule: the reference must contain a front-facing person wearing the garment.** Give the model a
body to dress, not a product to reproduce, and never a faceless one.

**What still drifts even in the good lane:** the *specific licensed graphic*. M1 kept the fit, the wash,
the KITH box tab and the whole Kith register, but invented a different character in place of the
Woodstock print. Fit and styling transfer; artwork does not. If exact artwork is load-bearing, that is
a compositing pass (garment graphic → subject → background), never a better prompt.

**Sourcing on-model references from kith.com** (Shopify):
```
/search/suggest.json?q=<term>&resources[type]=product&resources[limit]=8   → product handle
/products/<handle>.js                                                      → all image URLs
```
On-model shots are identifiable by filename: `..._LOOK_<n>_SHOT_<n>_...` or `Final_Mens_..._Ecomm_...`.
Append `&width=2000` to any Shopify CDN URL for full resolution. Most products are flat-lay only —
check before committing a garment to the lane.

## Known drift (v1, from calibration)

- **Cyan ring migrates.** In C1 the headphones rendered plain matte-black and the cyan appeared on the
  tee collar instead. Detail suppression, same class as the anime canon's A4 finding. Fix: feed
  `../anime-avatar/dataset/H1.png` (headphone anchor) as the single image reference on shots where the
  ring is load-bearing.

## Open — needs Farrice

- **Likeness verification.** Whether the Soul caught his actual likeness is his call, not a machine's.
  Until he confirms, treat the Soul as unverified.
- **Soul training inputs unknown.** The prior training session was not recoverable from episodic memory.
  If likeness is weak, retrain from `~/Desktop/02_Design_Assets/Farrice's AI Images/` (Secta AI headshots,
  ~50 frames — note these are AI-generated, which caps fidelity) plus the wedding photo
  `~/Downloads/05_Media_Files/174433_…273A0932.jpg`. True camera photos would beat both.
- **No true profile source.** Same gap the anime canon flagged. C4 tests whether the Soul invents or
  holds.

## Acceptance test

A character is locked when the **whole folder** holds, not when the best frame does. Scroll everything,
failures reported beside successes, every signature detail checked individually, face checked at wide
scale as well as close-up. "80% works but something's always weird" is not locked — it means an axis is
still un-authored.
