---
description: Full character identity pipeline in strict Mode 0→1→2A order — existence question, text spec mirror-back, face lock (tool fork), outfit base (1A/1B fork), 3-panel sheet with garment-matched headless variant, optional scene validation shot
---

# `/jcin-character-lock` — Character Identity Pipeline

Builds one character into a locked identity asset set: canonical face reference → base outfit reference → 3-panel character sheet. Strict order, no skipping, no combining — every downstream scene plate and video shot anchors to what this workflow produces. One character per run; a roster runs this workflow once per character.

## Pre-Flight Gate

- [ ] **Existence Question first** (genius.md signature move): does this character already exist, or are we developing them? Existing = reference image(s) in hand → skip Mode 0, study-and-lock instead. New = the full 0→1→2A ladder runs.
- [ ] **Bible check:** if a bible exists for this world, load the character's visual lock + "never" clauses from it — the spec below starts from canon, not from scratch. No bible on a recurring character → flag once, proceed.
- [ ] **Surface:** Higgsfield UI/MCP assumed (Banana Pro, GPT-2, Soul Cinema are Higgsfield tools). Generation is Farrice's action or a cost-gated call — this workflow's job ends at the code block.
- [ ] **Sheet only after base:** if the ask is "character sheet" for a character with no approved base outfit reference, the ladder still runs from the first missing rung. Never build a sheet from nothing.

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 1-6 (reference/asset physics), anti-patterns
2. `skills/banana-pro-director/SKILL.md` — the executing grammar. Sections used, by name: THE WORKFLOW — STRICT ORDER (Step 0), THE PRE-PROMPT CONFIRMATION RULE, MODE 0 — FACE LOCK, MODE 1A, MODE 1B, MODE 2A — 3-PANEL CHARACTER SHEET (incl. THE HEADLESS CUT), MODE 3 (validation shot only). Its canonical prompt structures and the flat-grade close are LOCKED verbatim — use them as written, never paraphrase.

## Execution

Every prompt in this workflow gets the pre-prompt confirmation (references listed FIRST) per Banana Pro's PRE-PROMPT CONFIRMATION RULE — full check on new mode/wardrobe/character, skipped on minor iterations of a just-approved prompt.

### Step 1 — Route on the Existence Question

- **Exists, refs in hand:** user drops reference image(s). Study and lock — face, bone structure, skin tone, hair color/texture, identity markers, proportions. Mirror the locked spec back in plain language, wait for confirmation, then jump to Step 3 (outfit base).
- **Exists partially:** enter the ladder at the first missing rung — face ref but no base outfit → Step 3; approved base but no sheet → Step 4. Never redo an approved rung.
- **New:** proceed to Step 2.

**Pre-prompt check anatomy (every full check in this workflow, per Banana Pro):** clean bullets only, in this order — **References attached** (always first; every uploaded ref by short visual descriptor, or "none — pure text composition") → **Character** → **Outfit/styling** → **Backdrop** → **Framing** (only if non-default) → one short close ("Sound good?"). A ref uploaded but missing from the list means the prompt is being composed wrong — the list exists so the user catches it before the prompt ships.

### Step 2 — Text spec, then face lock (Mode 0)

**Stage 1 — text spec mirror-back.** The user describes the character in their own words. Mirror back a locked spec covering the fields in Banana Pro Step 0 (age register by build not number, face, hair with every nuance, body, makeup register, default energy, identity markers). Iterate freely until the user says locked. Pull "never" clauses in from the bible or ask for them now — a lock without its wrong-answer drift named won't hold.

**Stage 2 — tool fork.** Ask which tool, using Banana Pro's fork language (MODE 0 — Tool fork):
- **Banana Pro single-pass** (recommended default) — balanced fidelity, reasonable credits → Step 0.A canonical prompt
- **GPT-2 single-pass** (highest fidelity, chest-up only) — for tricky identity markers. This is **Higgsfield GPT-2**, not OpenAI GPT Image 2 — opposite verdicts, never conflate. **State the credit warning once per conversation, then drop it.**
- **Soul Cinema two-pass** (cheap iteration) — throw face variations at the wall → Step 0.1 lean plate, then Step 0.2 Banana Pro 3:4 lock

All paths: 18% gray seamless, flat shadowless grade, locked baseline wardrobe (plain black camisole / ribbed tank), zero lighting information — the plate must carry nothing the scene will fight. Deliver the canonical Step 0.A / 0.B / 0.1+0.2 prompt structure verbatim with the spec slotted in. User generates, approves — that image is the canonical face reference.

### Step 3 — Outfit base (Mode 1, fork 1A/1B)

First image of any character/outfit pairing is a single full-body outfit reference on the gray seamless. Get the wardrobe spec (every garment, accessory, styling choice; wardrobe reference images studied visual-only), mirror back, then ask the fork per Banana Pro Mode 1:
- **Mode 1A (Banana Pro):** simple outfit, full prompt control, one shot → canonical Mode 1A prompt structure
- **Mode 1B (Soul Cinema two-step):** complex/custom fit designed separately from casting → Step 1B.1 outfit on neutral model, then Step 1B.2 two-reference composite. The 1B.2 prompt stays minimal — Soul Cinema reads outfit from image 2 and character from image 1; adding description double-weights it.

Building a wardrobe library: vary exactly one parameter per shot (pose / framing / expression / light direction); face, skin, identity markers never vary.

### Step 4 — 3-panel character sheet (Mode 2A)

Only after the base is approved. Default is the 3-panel — never ask, never offer the 6-panel (legacy, explicit request only; if named, flag the pixel-budget cost once and proceed on their go-ahead).

**Headless variant decision — read the neckline, then pick** (Banana Pro, THE HEADLESS CUT):
- Structured/closed neckline at or above the collarbone (crew, tank, turtleneck, jacket) → **Variant A ghost mannequin** — locked left-panel language, hollow neckline
- No real neckline (strapless, halter, slip, plunge) → **Variant B clean neck cut** — locked left-panel language, mannequin termination

Compose via the Canonical Mode 2A prompt structure: identity and wardrobe paragraphs once, per-panel paragraphs describe only what differs (LEFT headless front / CENTER rear with head / RIGHT tight chest-up face lock — chest-up, not waist-up). **The skin-tone consistency clause is mandatory** — skin identical in value and hue across face, arms, and body in every panel; rear panels drift darker without it. Gray backdrop and flat grade uniform across all three cells. One prompt, one code block, one image.

### Step 5 — Optional scene validation shot (Mode 3)

Offer, don't push: one Mode 3 character-in-environment plate using the new canonical refs — because **seeing the sheet is different from seeing them in a space.** A character who holds on gray can still crack under real light, real distance, real atmosphere. Route through `/jcin-scene-shot` Part A (references carry identity; the plate prompt narrates only the moment). If identity cracks here, fix the sheet — not the scene prompt.

## Content Type Adaptations

| Subject | How the ladder flexes |
|---|---|
| Human character (default) | As written above |
| Product / garment / vehicle | Same physics, different workflow — route to `/jcin-product-lock`: face lock ≈ hero-angle lock, 3-panel ≈ turnaround, KY technical flats replace the text spec |
| Brand mascot / creature | Ladder as written; one face per reference is critical — delete competing faces from every ref (face size controls drift) |
| Client-brand avatar (Jen, TrendScale) | Text spec starts from the client bible/ICP doc; "never" clauses include brand-off traits; save refs under the client's project |
| Music-video roster (CTRL-style) | Run per member, one at a time; shared wardrobe era goes in the bible, not in each spec; sheet per member per era |
| Ad-set talent | Full ladder still runs — an avatar reused across an ad set without a sheet re-rolls identity every variant |

## Output Requirements

- Each prompt delivered per Banana Pro's rule: pre-prompt check (references first) → green light → one fenced code block
- Asset ledger at the end: canonical face ref, base outfit ref(s), 3-panel sheet — named, with the approved generation noted as the anchor, plus suggested `@tag` names for the Seedance layer (`@<name>_ref`)
- No names, brands, ages, or platform names anywhere in prompt output; no aspect ratios in the prompt body (set in the Higgsfield UI)
- Locks recorded back to the bible if one exists (new "never" clauses discovered during the build get written home)

Execution prompt: references/prompts-v2/character-identity-lock.md — honor its Output Contract.

## Quality Gate

Anchor against the genius.md rubric before handing assets downstream:

- [ ] Strict order held: no outfit before face lock, no sheet before approved base, nothing combined (anti-pattern: skipping the existence question)
- [ ] Identity references: exactly ONE face, as large as the format allows; garment panel face-free; competing faces deleted (pattern 4)
- [ ] Plates flat: 18% gray, zero baked lighting/shadow — white seamless only on explicit request, flatness never comes off (anti-pattern: baking lighting into a reference plate)
- [ ] 3-panel by default; headless variant matched to the garment; skin-tone consistency clause present verbatim
- [ ] Flattering-realism ceiling intact — matte fights plastic, fine-and-even fights ugly, ties resolve toward flattering
- [ ] GPT-2 credit warning delivered once, not repeated; tool fork asked, not assumed
- [ ] Rubric — identity persistence: target ≥7 (holds across a full scene without re-rolls); validation shot is how you check it
- [ ] Any prompt past ~3 failed iterations was reset, not patched

Identity that cracks downstream is fixed HERE, at the asset layer — never by re-describing the face in a scene or video prompt.
