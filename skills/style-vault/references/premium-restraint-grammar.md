# Premium Restraint — a derived grammar card

**What this is:** decision rules derived from direct observation of a reference brand's public
storefront on 2026-08-09, written in our own decomposable vocabulary so they can be swept, banked
and applied to Farrice's register.

**What this is not:** their assets. No campaign photography, product styling, layouts, logos or
fashion codes are stored, reproduced or fed to a generator. Per the Design Contract
(`_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md`): *"This is a taste
principle only."* The reference brand is named nowhere below on purpose — once the grammar is
extracted, the name adds nothing and invites copying.

**Why derive rather than farm:** what makes the reference read premium is restraint plus
consistency plus material honesty. None of those survive being copied — a copied frame is a
knockoff, and a knockoff reads *less* premium, not more. Rules transfer. Frames don't.

---

## What was actually observed

Four surfaces, direct observation, 2026-08-09:

| # | Surface | What was on screen |
|---|---|---|
| 1 | Error page hero | Aerial of dark conifer forest, a concrete balustrade bridge cutting the lower third, one small figure in red for scale. Desaturated green-black, visible grain. |
| 2 | Newsletter modal | Seated model three-quarter turned, weathered mottled concrete wall, window to green foliage camera-right. Tonal grey/taupe/ecru tailoring. Soft directional daylight, no hard shadow. |
| 3 | Product grid | Garments on flat light-grey seamless, hung on a **visible thin black hanger**, dead-on flat elevation, effectively shadowless, garment ~70% of frame. |
| 4 | Editorial card | Full-body model against weathered vertical wood planks, cracked stone paving underfoot. Faded denim, grey wool, one saturated shoe note. Small serif type, upper-left. |

Everything below is read off those four. Where I am inferring rather than observing, it says so.

---

## The eight rules

### 1. One tonal family per frame, one deviation maximum

Observed in all four: wardrobe, ground and wall sit in a single family (greys/taupes, or
browns/greens), and **exactly one element departs** — a red figure, a saturated shoe, a green
window. The deviation is small in area and high in saturation.

> **Rule:** name the tonal family, then name the single deviation and cap it at roughly 5% of
> frame area. Two deviations reads as styling. Zero reads as flat.

### 2. Light is always one source, always soft, never neutral in direction

Observed: daylight through a window (2), overhead diffuse (3), open shade (4). Never a hard key,
never a rim, never a visible fixture. But it is always *placed* — you can say which side it comes
from.

> **Rule:** one source, diffused, direction stated. Falloff is wraparound, shadows are soft-edged
> and present. "Soft" never means "flat" — a shadowless frame reads as e-comm, which is rule 6's
> job, not editorial's.

### 3. The ground plane is a real, worn material

Cracked stone paving, poured concrete, weathered plank. Never seamless, never clean, never
implied. The floor carries as much material information as the subject.

> **Rule:** the surface underfoot is named and aged. If you cannot say what it is made of and how
> it has worn, the frame will read as rendered.

### 4. Backdrops are *walls*, not sets

Mottled concrete, vertical planks, forest. Textured vertical planes with real history. No
gradients, no studio sweeps, no styled vignettes, no props arranged for the camera.

> **Rule:** one wall, one material, visible age. Nothing is placed in the frame to be looked at
> except the subject.

### 5. Grade is warm, low-contrast, lifted

Blacks are lifted to charcoal rather than crushed. Highlights roll rather than clip. A consistent
warmth sits across the whole frame. Grain is present and fine.

> **Rule:** lifted black point, rolled highlights, one warm bias, fine grain. This is the single
> most transferable rule — it is a grade, so it applies across photography, illustration and
> render alike.

### 6. E-comm is a separate, stricter register — and honesty is the flex

The product shots break every editorial rule deliberately: flat grey seamless, no shadow, no
model, no environment. The tell is the **visible black hanger** — most premium brands retouch it
out. Leaving it in reads as archival and honest rather than merchandised, and it is doing real
work.

> **Rule:** keep the two registers strictly separate and never blend them. In the product register,
> leave one honest artifact in frame (the hanger, the fold, the pin). Removing every trace of how
> the object was held is what makes catalogue photography feel like advertising.

### 7. Type is a two-family system with no overlap

Observed: letterspaced all-caps sans for navigation and UI; a serif for product names, prices and
editorial headers. The wordmark is a hard black rectangle with white slab lettering — a container,
not a flourish.

> **Rule:** sans for anything functional, serif for anything named. Never a third family, never a
> weight used for emphasis where a size would do. Type sits *on* the image at small scale in a
> corner — it never centres, never scales up, never gets a scrim behind it.

### 8. Layout: generous margin, zero ornament

Equal gutters, no borders, no drop shadows, no rounded corners, no cards. White space carries the
premium signal; nothing is decorated to look expensive.

> **Rule:** if an element needs a border, a shadow or a corner radius to read, the spacing is
> wrong. Fix the spacing.

---

## Ported into the vault lexicon

These extend `LEXICON` in `execution/style_vault.py` so future sweeps can *reach* this register.
Nothing here names the reference brand — they are physical descriptions.

```python
"light": [
    "single diffused daylight through a window camera-right, wraparound falloff, soft-edged shadow",
    "open shade, no visible source, even and directionless with soft ground shadow",
]
"surface": [
    "weathered vertical wood planks and cracked stone paving",
    "mottled poured concrete with water staining and age",
]
"palette_logic": [
    "one tonal family of warm neutrals with a single saturated deviation under 5% of frame",
    "lifted charcoal black point, rolled highlights, consistent warm bias",
]
"composition": [
    "subject occupying two-thirds, remaining third a single textured wall",
    "flat-on product elevation on light grey seamless, one honest handling artifact left in frame",
]
```

## The travel test

Grace Liu's closer, applied here: **name three invisible decisions.** For this grammar they are —
the deviation colour was capped by area, the black point was lifted rather than crushed, and the
hanger was left in. None of the three is visible as a decision in the final frame, which is
exactly why the result reads as restraint rather than as a style.

If a generation made none of those three choices, it is wearing the look without the grammar.
