# THE FLOOR — Farrice photoreal generation standard (BINDING)

**Set 2026-08-07 by Farrice: "this should be the floor and standard."** The exemplars live in
`REFERENCE-BAR/` (10 images + the exact prompt that produced each, as `.txt` sidecars, plus
`INDEX.json` with full job params). Nothing ships below this bar. Produced by the Codex lane; the
recipe below is reverse-engineered from the actual job records, not reconstructed from memory.

**Check any new generation against `REFERENCE-BAR/` before delivering. If it doesn't hold that bar,
it isn't done — and the fix is one of the named clauses below, never a re-roll and never a vibe.**

## The mechanism that produces the floor

Not a Soul. A **Reference Element** — a persistent, named character object bound *inline in the
prompt* by a `<<<uuid>>>` token.

| | |
|---|---|
| **Model** | `gpt_image_2` |
| **Character element** | `Farrice-1` — `1e3e0cae-e3ba-47cc-a099-26456d94b103` (category `character`) |
| **Binding** | put `<<<1e3e0cae-e3ba-47cc-a099-26456d94b103>>>` **inside the prompt text** |
| **Quality / resolution** | `medium` / `2k` ← *not* `high`; the floor was set at medium |
| **Aspect** | `3:4` for identity/portrait work |
| **Control image** | one attached image used as **expression/pose control only** |

Why this beats the Soul lane: the Soul carries identity but caps at **one** image reference, so
identity and any second control compete for the same slot. A reference element carries identity
*in the prompt*, leaving the image slot free for pose, expression, or a garment.

## The five clauses (the actual craft — copy verbatim)

Every floor-quality frame contains all five. They are load-bearing, not decoration.

**1 — Identity preservation** (name the geometry, don't gesture at it):
> Preserve Farrice Cain as the exact same recognizable adult man from the character reference:
> true-to-life age and facial geometry, warm-brown skin with natural texture, authentic hairline and
> short tapered hair, thin mustache and soul-patch goatee.

**2 — Identity negative** (blocks the drift that made every earlier attempt fail):
> No beauty retouching, age shift, face substitution, stylization or collage.

**3 — Anti-fabricated-apparel** (this is why nothing reads fake):
> All garments are plain and unbranded with no logos, trademarks, graphic text or invented fashion
> products.

**4 — Control-image role** (stops the reference from hijacking identity — the K1/K4 failure):
> Use the attached image only as an expression target, never as a replacement identity.

**5 — Photographic spec** (named and placed, never adjectives):
> Plain black turtleneck and tailored black blazer, seamless warm-gray background, soft large key and
> gentle fill, natural 85mm perspective, realistic skin texture, no beauty-filter plasticity.

Then one sentence of **specific direction** — the only part that varies:
> Chest-up left three-quarter identity view, body and head turned about 30 degrees toward frame
> right, eyes into camera, calm relaxed expression.

Note the register: **degrees of rotation, named focal length, named light shape.** "Head rotated about
70 degrees toward frame left with the far eye still slightly visible" is why the profile works.

## Two lanes, and they do not mix

Clause 3 bans branded apparel outright — so the floor recipe **cannot** produce Kith looks. These are
complementary lanes, and picking the wrong one is how quality drops:

| Goal | Lane | Recipe |
|---|---|---|
| **Identity, headshots, authority, b-roll — max realism** | **FLOOR** | `gpt_image_2` + `<<<Farrice-1>>>` + five clauses + plain unbranded wardrobe |
| **Real branded garment (Kith etc.)** | **WARDROBE** | `gpt_image_2` + person ref + **real garment product photo** as second `--image`; drop clause 3, keep 1/2/4/5 |
| Cheap volume where likeness is not load-bearing | Soul | `text2image_soul_v2` + `6e8a9e71-…` — **below the floor; never for deliverables** |

## Wardrobe-lane result (5 frames, 2026-08-07) — `wardrobe-lane/`

Floor clauses + real garment reference. **Identity held on all five** — the reference element is
doing its job regardless of what the garment reference contains, which is exactly what the Soul lane
could never manage. Garment fidelity, however, is not uniform:

| Frame | Garment fidelity | Note |
|---|---|---|
| W1 Matrix hoodie | **High** | code print + KITH logo exact; wordmark letters still drift ("HE MATRI") |
| W2 Peanuts tee | **High** | bird, flower, grass band, box logo all correct |
| W5 Patchwork overshirt | Medium | colour and cut right, panel/topstitch layout simplified |
| W4 Crest overshirt | Medium | navy pinstripe right, embroidered star motifs dropped |
| W3 Knicks bomber | **Low — invented** | produced a generic NEW YORK varsity jacket, not the Ewing satin bomber |

**The pattern: bold high-contrast surface graphics transfer; subtle construction detail does not.**
Prints, wordmarks and colour blocking survive. Embroidery, patchwork panels and topstitching get
smoothed away. Licensed team apparel is the worst case — the model substitutes its own strong prior
(generic varsity/NBA) over the referenced garment.

Routing that follows from it:
- **Graphic-led pieces** (prints, code, artwork, box logos) → wardrobe lane, ships as-is.
- **Construction-led pieces** (embroidery, patchwork, tailoring detail) → wardrobe lane gets you the
  silhouette; exact detail needs a compositing pass.
- **Licensed team apparel** → do not trust the lane. Either composite or shoot it.

Small-text wordmarks are an open defect in both lanes — treat any legible garment text as
approximate until proven per-frame.

## Waste rules (why this document exists)

1. **Never generate a batch before one frame clears the bar.** One image, compared against
   `REFERENCE-BAR/`, then scale. 25 images were burned on an unvalidated identity.
2. **Validate the identity source against a real photograph first.** The original Soul was trained on
   SectaAI output — AI images of an AI approximation. Drift on drift, invisible until compared to a
   camera photo. *Look at the ground truth before generating, not after.*
3. **A constraint of one model is never a law of the medium.** `text2image_soul_v2` caps at one image
   reference; that was wrongly generalised into "no model can do branded garments," which `gpt_image_2`
   disproved immediately. Check `model get <id>` CONSTRAINTS across the roster before declaring
   anything impossible.
4. **Cheapest-first is a false economy.** 0.12/image looked thrifty against 7/image until the cheap
   model couldn't do the job at all. Price the *capability*, then the credit.

## Reuse

```bash
higgsfield generate create gpt_image_2 \
  --prompt "Photorealistic studio character reference portrait of <<<1e3e0cae-e3ba-47cc-a099-26456d94b103>>>, Farrice Cain. [CLAUSE 1] [CLAUSE 2] [CLAUSE 3] [CLAUSE 4] [CLAUSE 5] [one sentence of specific direction]" \
  --image <expression/pose control> \
  --quality medium --resolution 2k --aspect-ratio 3:4 --wait
```

Reference elements are managed through the Higgsfield MCP (`show_reference_elements`) — the CLI has no
`reference-element` command as of 1.1.22, so the element is created in the app/MCP and reused by ID here.
