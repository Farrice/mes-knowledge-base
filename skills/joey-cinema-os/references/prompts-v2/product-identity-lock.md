---
name: "Joey — Product Identity Lock Package"
source_prompt: born-v2
skill: joey-cinema-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the KY transfer of Joey's identity discipline (KY — formally trained fashion designer, Control World Fashion Design Director, who imports real fashion-industry documentation into the AI pipeline). Joey's character physics map to products one-to-one: hero-angle lock ≈ face lock, turnaround sheet ≈ 3-panel character sheet, brand canon ≈ bible — and the KY method (spec sheets, technical flats, measurements, all angles, colors-to-avoid) replaces the character interview. Her line is the anti-slop standard: "you have to pay really close attention to the materials you're feeding into AI. Measurements... front profile, side profile, back profile." KY needed ~50 generations to land her hardest corset WITH full documentation — that number is the honest baseline for a hard asset, not a failure signal. Success metric: **a designer/owner recognizes their own product's construction in the output.**

## Input Required

- `[EXISTENCE_ANSWER]` — does this product physically exist, or are we designing it? Exists → real documentation is mandatory input; none in hand = STOP and gather. Concept → lock a written spec first (construction, materials, hardware, measurements, drape/finish behavior); unknowns marked `[TBD]`, never invented
- `[DOCUMENTATION]` — spec sheets, technical flats, measurements, material and hardware callouts, front/side/back/three-quarter photos (studied visual-only)
- `[BRAND_COLORS]` — hex values where available, plus any known wrong-answer drift colors
- `[DESTINATION]` — stills only vs seeding video (gray-flat is the default either way; it sets the take budget) and surface (Higgsfield MCP native / Fal wrapper — no @tags, prose only; fal seedance-1080p is HARD-BLOCKED, flag now if this product seeds video)
- `[PRODUCT_CLASS]` — garment / bottle-packaging / vehicle / jewelry-hardware (adaptations below)

## Execution Protocol

**Step 1 — Documentation ingest (the KY method).** Inventory before writing a single prompt: spec sheet · technical flats · all four angles · material callouts (fabric, finish, sheen behavior) · hardware callouts (zips, clasps, caps, badges) · construction notes (seams, pleats, boning, closures). Missing rows for an existing product → go get them or mark `[TBD]` and name the risk out loud. Real documentation beats vibe prompts.

**Step 2 — Per-product palette sheet, WITH the colors-to-avoid row.** The avoid-row is the "never" clause of color — locks exclude as much as they include. "Matte forest green — never neon green, never teal-shifted" holds over hundreds of renders; "green" drifts. Every hex tied to a material/surface; the avoid-row names real observed or predicted drift directions, not filler.

**Step 3 — Hero-angle lock (≈ face lock).** One product, large in frame — face size controls drift, and so does product size. **One subject only:** no props, no hands, no model, no competing objects (competing faces get deleted from character refs; competing objects get deleted here). Compose in construction language from the documentation — costume-designer register per the '33'-jersey exemplar: seams, drape, hardware, finish, zero AI-art keywords. Close with the LOCKED FLAT GRADE pulled **verbatim** from `skills/banana-pro-director/SKILL.md` § 18% GRAY SEAMLESS + FLAT GRADE (also embedded in this skill's `character-identity-lock.md` prompt), with exactly two product adaptations:
- Swap the skin-biology sentences for material truth: true natural material color against the neutral gray, real weave/grain/surface detail, matte by default
- **Material-true sheen exception** (from the amber-PVC-raincoat exemplar, `extractions/joey-cinema-os/reference-corpus/joey-3panel-sheet-amber-pvc-raincoat.md`): PVC, leather, glass, chrome, polished metal keep their specular character — "soft rolling specular highlights across the vinyl creases and the leather grain, never blown out, never hard glare" — while everything else stays matte. State the exception explicitly or the flat grade kills the material.

The three flat-close clauses survive every adaptation, verbatim: flat backdrop (one uniform 18% gray value, no gradient, no falloff) · shadowless illumination (matched fill all sides, no key side, no rim) · zero cast shadow (no contact shadow, no ambient occlusion). Missing any one → the plate comes back with modelling baked in, and baked lighting is inherited and amplified downstream.

**Step 4 — Turnaround sheet (≈ 3-panel sheet).** Only after the hero lock is generated and approved. One prompt, one frame, on the Mode 2A chassis: equal panels, thin clean separation, explicit position labels, the same product rendered identically in every panel. Default panels: **front / back / detail close-up** — the detail panel (hardware, label, texture at close range) is the product's "chest-up face lock." Garments on an invisible body use the ghost-mannequin headless logic from § THE HEADLESS CUT so silhouette reads with zero competing subject. Identity + construction described ONCE in the opening paragraphs; each panel describes only what differs. **The consistency clause is mandatory** — material and color identical in value and hue across every panel (rear panels drift without it). Flat grade stated as uniform across all panels; no aspect ratio in the prompt body.

**Step 5 — In-context plates LAST.** Product-in-environment/on-model/in-use plates only after hero + turnaround are locked and approved — same strict order as the character pipeline. Route through Mode 3 grammar (this skill's `scene-plate.md` prompt): the locked product references carry identity, the scene prompt carries framing and light. Lighting is applied exactly once, here. **Canonical-over-plate:** even when the product is visible in an environment plate, its canonical reference still rides along.

**Step 6 — Take budget, declared before generating.** Standard product with good documentation: 2-3 takes per asset. Complex construction (corsetry, layered garments, transparent/reflective materials): up to ~50 generations, budgeted knowingly. Iteration past ~3 fails on one prompt: stop patching, run the reset ritual (`prompt-repair.md`). "One-shot magic" is not the win condition; 8-10 takes → 2-3 is.

**Brand-neutral rule (applies even to the client's own marks):** inside prompt output, trademarks, logos, and product names go brand-neutral — "matte black bottle with a debossed three-letter wordmark," "three-stripe athletic sneakers." Models don't know names; names drift regardless of who owns them. Real logo/label art gets composited from the reference asset, never prompted by name.

Product-class adaptations: **garments/apparel** — full KY method, ghost-mannequin turnaround, validate in a moving scene last (fabric moves). **Bottles/packaging** — hero lock at label-readable scale; detail panel = cap/label/texture; glass and foil take the sheen exception; label art composited from cutout reference. **Vehicles** — turnaround = front 3/4, rear 3/4, detail (badge/wheel); livery is the identity load. **Jewelry/hardware** — hero lock at tele-detail scale; metal keeps specular by exception; palette sheet locks metal tone against gold/silver drift.

## Output Contract

- Documentation inventory table with explicit `[TBD]` gaps and named risks
- Palette sheet (palette + colors-to-avoid) as a saveable artifact for the owning project folder
- Hero-lock prompt + turnaround prompt (+ context-plate prompts where reached) — each preceded by its pre-prompt check (references FIRST), each in a single fenced code block
- Declared take budget per asset + surface routing note (Higgsfield vs Fal)
- No brand names, no aspect ratios, no style-keyword slop anywhere in prompt output

## Output Skeleton

```
PRODUCT IDENTITY LOCK — [product handle, chat-side only]

DOCUMENTATION INVENTORY:
  | input | have it? | notes / [TBD] |
  [spec sheet / flats / angles / materials / hardware / construction — risks named]

PALETTE SHEET:
  [PRODUCT] — PALETTE: [named lane] — [hex values, each tied to a material/surface]
  COLORS TO AVOID: [hex/named swatches — real drift directions]

— Pre-prompt check (references first) —
HERO-ANGLE LOCK:
  [single fenced code block: construction language from documentation → flat-grade close with the
   two product adaptations + material-true sheen exception]

— Pre-prompt check —
TURNAROUND SHEET (front / back / detail):
  [single fenced code block: construction once → per-panel differences → consistency clause →
   flat grade uniform across panels]

[IN-CONTEXT PLATES — only after hero + turnaround approved; route through scene-plate grammar]

TAKE BUDGET: [2-3 standard / up to ~50 hard asset, named knowingly] · SURFACE: [Higgsfield / Fal note]
```

## Quality Gate

- [ ] Hero plate carries zero lighting information — all three flat-close clauses verbatim, no white seamless on a video-bound asset?
- [ ] One subject per identity reference; detail panel tight enough to anchor identity downstream?
- [ ] Every construction claim traces to documentation or the locked spec — nothing invented, `[TBD]`s surfaced not filled?
- [ ] Colors-to-avoid row exists and names real drift directions?
- [ ] Take budget declared BEFORE any generation; the ~50-gen hard-asset number named up front, never discovered in overruns?
- [ ] Would the designer/owner recognize their own product's construction — or is this merely "a nice bottle"?

## Creative Latitude

The construction language is the craft: translate flats and measurements into prose a camera understands — drape behavior, seam placement, fabric weight, hardware finish — with the specificity of the amber-PVC-raincoat exemplar ("glossy, wet-looking vinyl with visible crinkle and fold creases... fuchsia-pink piping trim running along every edge"). The detail-panel choice is a taste call: pick the angle that makes THIS product unmistakable, not the generic one. Where the documentation reveals something beautiful (an unusual closure, a signature stitch), give it prompt real estate — the locks constrain the plate physics, never the product's story.

## Deploy When

- A real product/garment/vehicle/package must hold identity across a campaign, listing set, or video (MyBPM, TrendScale, client goods)
- A brand world needs its product locks before ad variants generate (`/jcin-ad-world` Step 2)
- Product identity drift traced upstream from failing scene/video prompts
- Invoked via `/jcin-product-lock`
