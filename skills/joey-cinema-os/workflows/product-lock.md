---
description: "/jcin-product-lock — product-grade identity lock for products, garments, vehicles, and packaging: hero-angle lock → turnaround sheet → in-context plates, built on real documentation (the KY technical-flats method) with a per-product palette sheet and an honest take budget"
---

# Product Lock (Joey Cinema OS — the KY transfer)

Joey's character discipline transfers to products one-to-one: hero-angle lock ≈ face lock, turnaround sheet ≈ 3-panel character sheet, brand canon ≈ bible, and the KY method (spec sheets, Adobe technical flats, measurements, all angles, colors-to-avoid) is the client-product version of the character interview. KY needed ~50 generations to land her hardest corset accurately — with full construction documentation in hand. That number is the honest baseline for a hard asset, not a failure signal. This workflow builds the permanent product assets so every downstream generation is a cheap read of expensive, locked context.

## Pre-Flight Gate

> **🔒 Gate — the Existence Question, product edition.** Before anything: *does this product physically exist, or are we designing it?*
> - **Exists** → real documentation is mandatory input. No spec sheets, no flats, no product photos from multiple angles = STOP and gather them. Vibe-prompting a real product is the anti-slop line KY drew: "you have to pay really close attention to the materials you're feeding into AI. Measurements... front profile, side profile, back profile."
> - **Concept product** → lock a written spec first (construction, materials, hardware, measurements, drape/finish behavior) exactly as banana-pro-director locks a text spec before a Mode 0 face lock. Mark unknowns `[TBD]` — never invent construction detail. Invented canon becomes locked canon becomes prompt drift.
> - Confirm the execution surface: Higgsfield MCP (native, @tags work) or Fal wrapper (no @tags, prose descriptors only; **fal seedance-1080p is HARD-BLOCKED** — irrelevant for stills but flag it now if this product seeds video).

## Skill Acquisition

Load in this order — the locked blocks live in the sources, never re-implement them here:
1. `skills/joey-cinema-os/genius.md` — patterns 1–6 (reference/asset physics), 15–17 (canon discipline), 21 (credit economy); Quality Rubric; Anti-Patterns
2. `skills/banana-pro-director/SKILL.md` § **18% GRAY SEAMLESS + FLAT GRADE** (the LOCKED FLAT GRADE close + "the three things that must appear in every flat close"), § **MODE 2A — 3-PANEL CHARACTER SHEET** (panel logic, consistency clause), § **READING REFERENCE IMAGES** (brand rule, no-invention rule), § **THE PRE-PROMPT CONFIRMATION RULE**
3. `extractions/joey-cinema-v3/visual-context.md` § "Translating real fashion designs into AI" + § "The Bible system, restated" (the CTRL SOL palette-sheet artifact format)
4. Exemplar: `extractions/joey-cinema-os/reference-corpus/joey-3panel-sheet-amber-pvc-raincoat.md` — material-true sheen exceptions done right

## Input Required

- Real documentation: spec sheets, technical flats (Illustrator-grade line drawings if they exist), measurements, material and hardware callouts, front/side/back/three-quarter photos
- Brand color values (hex if available) and any known wrong-answer drift colors
- Where the asset is headed (stills only vs seeding video — decides nothing about the plate, gray-flat is the default either way, but it sets the take budget)
- Approval to spend: this workflow produces prompts; generation runs behind the cost gates

## Execution

### Step 1 — Documentation ingest (the KY method)
Inventory what exists before writing a single prompt. Real documentation beats vibe prompts — a designer should recognize their own construction in the output.

| Input | Have it? | Notes / `[TBD]` |
|---|---|---|
| Spec sheet (measurements, fit) | | |
| Technical flats (line drawings per piece) | | |
| All angles: front / side / back / three-quarter | | |
| Material callouts (fabric, finish, sheen behavior) | | |
| Hardware callouts (zips, clasps, caps, badges) | | |
| Construction notes (seams, pleats, boning, closures) | | |

Missing rows for an existing product → go get them or mark `[TBD]` and name the risk out loud. Study every reference visual-only per § READING REFERENCE IMAGES.

### Step 2 — Per-product palette sheet, WITH the colors-to-avoid row
Build the aesthetic lock in the CTRL SOL artifact format (visual-context.md, t=12:25): product images + **COLOR PALETTE** grid + **COLORS TO AVOID** swatch row. The avoid-row is the "never" clause of color — locks exclude as much as they include. "Matte forest green — never neon green, never teal-shifted" holds over hundreds of renders; "green" drifts.

```
[PRODUCT NAME] — PALETTE SHEET
PALETTE: [named lane, e.g. "warm neutrals"] — [hex values, each tied to a material/surface]
COLORS TO AVOID: [hex/named swatches — the observed or predicted drift directions]
```

### Step 3 — Hero-angle lock (≈ face lock)
One product, large in frame, exactly as face size controls drift: the hero angle is the single canonical identity reference. **One subject only** — no props, no hands, no model, no competing objects (competing faces get deleted from character refs; competing objects get deleted here).

Compose the prompt with construction language from the documentation (costume-designer register — the '33'-jersey exemplar: seams, drape, hardware, finish — zero AI-art keywords), then close with the LOCKED FLAT GRADE from banana-pro-director § **18% GRAY SEAMLESS + FLAT GRADE** — paste the block, do not paraphrase it, with two product adaptations only:
- Swap the skin-biology sentences for material truth: true natural material color against the neutral gray, real weave/grain/surface detail, matte by default
- **Material-true sheen exception** (from the amber-PVC-raincoat exemplar): PVC, leather, glass, chrome, polished metal keep their specular character while everything else stays matte — state the exception explicitly or the flat grade kills the material

The section's three mandatory clauses survive every adaptation, verbatim: flat backdrop (one uniform 18% gray value, no gradient, no falloff), shadowless illumination (matched fill all sides, no key side, no rim), zero cast shadow (no contact shadow, no ambient occlusion). If any one is missing, the plate comes back with modelling baked in — and baked lighting is "inherited and amplified" by every downstream generation.

Run the pre-prompt check first (references listed FIRST, always), deliver the prompt in one fenced code block.

### Step 4 — Turnaround sheet (≈ 3-panel character sheet)
Only after the hero lock is generated and approved. One prompt, one frame, multiple orthogonal views on the Mode 2A chassis (§ MODE 2A): equal panels, thin clean separation, explicit position labels, the same product rendered identically in every panel. Default panels: **front / back / detail close-up** (the detail panel is the identity anchor — hardware, label, texture at close range, the product's "chest-up face lock"). Garments on an invisible body use the headless ghost-mannequin logic from § THE HEADLESS CUT so silhouette reads with zero competing subject.

Non-negotiables lifted from the Mode 2A rules:
- Identity + construction described ONCE in the opening paragraphs, applied to all panels; each panel describes only what differs (angle, framing)
- **Consistency clause is mandatory** — material and color identical in value and hue across every panel (the product version of the skin-tone consistency clause; rear panels drift without it)
- Flat grade stated as uniform across all panels; no aspect ratio in the prompt body

### Step 5 — In-context plates LAST
Scene plates (product in environment, on model, in use) only after hero + turnaround are locked and approved — same strict order as the character pipeline. Route through `/jcin-scene-shot` / Mode 3 grammar: the locked product references carry identity, the scene prompt carries framing and light. Lighting is applied exactly once, here. Canonical-over-plate: even when the product is visible in an environment plate, its canonical reference still rides along.

### Step 6 — Take budget, declared before generating
| Asset difficulty | Honest budget |
|---|---|
| Standard product, good documentation | 2–3 takes per asset |
| Complex construction (corsetry, layered garments, transparent/reflective materials) | up to ~50 generations, budgeted knowingly |
| Iteration past ~3 fails on one prompt | stop patching — route to `/jcin-prompt-doctor` (reset ritual) |

State the budget in the delivery. "One-shot magic" is not the win condition; 8–10 takes → 2–3 is.

### Brand-neutral language rule (applies even to the client's own marks)
Inside prompt output, the client's own trademarks, logos, and product names go brand-neutral: "matte black bottle with a debossed three-letter wordmark," "three-stripe athletic sneakers." Models don't know names; names drift. Chat with Farrice/the client can use real names freely — the prompt never does. Real logo/label art gets composited from the reference asset, not prompted by name.

## Content Type Adaptations

| Product class | Adaptation |
|---|---|
| Garments / apparel (MyBPM) | Full KY method — flats + measurements + fit-in-motion notes; ghost-mannequin turnaround; validate in a moving scene last ("sheet ≠ scene — fabric moves") |
| Bottles / packaging (TrendScale-class) | Hero lock at label-readable scale; detail panel = cap/label/texture; glass and foil take the material-true sheen exception; label art composited from cutout reference, never re-prompted |
| Vehicles | Turnaround = front 3/4, rear 3/4, detail (badge/wheel); livery and markings are the identity load — canonical ref required in every downstream scene even when the car reads in the plate |
| Jewelry / hardware | Hero lock is a 12° (180–200mm) tele-detail-scale read; metal keeps specular by exception; palette sheet locks metal tone against gold/silver drift |
| Listing props / interiors (Jen) | Rooms are plates, not products — route to Mode 3; this workflow applies only to a repeated hero object (a signature staging piece) that must hold identity across a listing set |

## Output Requirements

- Documentation inventory table with explicit `[TBD]` gaps and named risks
- Palette sheet (palette + colors-to-avoid) as a saved artifact in the owning project folder
- Hero-lock prompt, turnaround prompt, and any context-plate prompts — each preceded by its pre-prompt check (references first), each delivered in a single fenced code block
- Declared take budget per asset + surface routing note (Higgsfield vs Fal)
- No brand names, no aspect ratios, no style-keyword slop anywhere in prompt output

Execution prompt: references/prompts-v2/product-identity-lock.md — honor its Output Contract.

## Quality Gate

> **🛡️ Anchor before shipping** — `genius.md § Quality Rubric` + § Anti-Patterns. Score Reference discipline, Prompt economy, Credit economy; name the anchor for any 8+.
- Hero plate carries **zero lighting information** — the three flat-close clauses present verbatim; no shadow, no falloff, no white seamless on a video-bound asset
- One subject per identity reference; detail panel tight enough to anchor identity downstream
- Every construction claim in the prompt traces to documentation or the locked spec — nothing invented, `[TBD]`s surfaced, not filled
- Colors-to-avoid row exists and names real drift directions, not filler
- Prompt re-describes nothing an attached reference already shows (cut unless load-bearing for composition)
- Take budget declared before any generation; hardest-asset budget (~50) named knowingly, never discovered in overruns
- A designer/owner would recognize their own product's construction in the output — if the output is merely "a nice bottle," the lock failed

## Common Pitfalls
- **Skipping straight to in-context shots.** The lifestyle plate is what the client asked to see, so the hero lock feels like a detour. It isn't — every context shot generated without a lock re-rolls product identity from scratch. Recovery: stop, build hero + turnaround, regenerate the context shots against them.
- **Prompting the client's brand by name because "it's their own brand."** The trademark exemption doesn't exist at the model layer — names drift regardless of who owns them. Recovery: brand-neutral descriptor in the prompt, real label art composited from the cutout reference.
- **A beautiful lit hero shot as the identity reference.** Gorgeous, and poisoned — the baked key light fights every scene downstream. Recovery: regenerate on the flat grade; keep the lit version as a finished deliverable, never as a reference.
- **Treating the ~50-gen budget as failure.** KY's hardest corset took ~50 with full documentation. Discovering that number mid-run reads as disaster; declaring it up front reads as production. Recovery: budget it in Step 6 before the first take.
- **Palette sheet without the avoid-row.** A palette that only includes is half a lock — the drift colors are the ones the model reaches for. Recovery: name the wrong answers explicitly, hex or named swatches.
