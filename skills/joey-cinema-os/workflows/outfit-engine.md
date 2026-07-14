---
description: "/jcin-outfit-engine — outfit builds and swaps on locked characters: Mode 1A vs 1B fork criteria, the Mode 5 two-reference swap, technical-flat ingestion for designed garments, and group-coordinated lineup variants"
---

# Outfit Engine (Joey Cinema OS)

Wardrobe is where Control World earns its "how is this consistent?" comments: KY designs real garments (flats, measurements, hardware callouts), the pipeline puts them on locked characters, and the same seams read identically from character sheet to club scene to red carpet. Three tools do this work — Mode 1A (prompt-written styling), Mode 1B (Soul Cinema two-step: design the fit, then cast it), and Mode 5 (two-reference swap) — and picking the wrong one is the most common way an outfit session burns credits. This workflow is the fork logic plus the locked execution paths.

## Pre-Flight Gate

> **🔒 Gate — locked character first, always.** Outfit work runs on a character whose identity is already locked (Mode 0 face lock or confirmed canonical reference). Unbuilt character → STOP, kick to `/jcin-character-lock`, come back. The worldbuilder refuses unbuilt characters; so does this workflow. Second check — the garment's own existence question: *is this a designed/real garment (documentation exists) or a described outfit (we're writing it)?* Designed garment → Step 2 technical-flat ingestion is mandatory. Described outfit → skip to the fork.

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 1, 4–6, 15–16; Signature Moves (References First, One Variable Per Shot); Anti-Patterns
2. `skills/banana-pro-director/SKILL.md` § **MODE 1A** (canonical prompt structure + variation strategy), § **MODE 1B** (two-step flow, both canonical prompt structures, the lighter Step 1B.1 close), § **MODE 5 — OUTFIT REPLACEMENT** (the locked lean prompt + fixed reference order), § **READING REFERENCE IMAGES**, § **THE PRE-PROMPT CONFIRMATION RULE**, § **UNIVERSAL PROMPT RULES**
3. `extractions/joey-cinema-v3/visual-context.md` § "Translating real fashion designs into AI" (the ~50-gen expectation) + the 3-panel triptych format note
4. If a bible exists for this world: its Outfit Bible section + per-character palette sheets

## Input Required

- The locked character reference(s) — confirmed present, listed by visual descriptor
- The outfit: full description head-to-toe, OR wardrobe reference image, OR designer documentation (flats/specs/angles)
- For swaps: the outfit-source image and the identity-source image, both uploaded
- Per-character palette sheet if this is a bible world (coordinated lineups need it)

## Execution

### Step 1 — Route through the fork
One decision, three lanes. Present the fork to the user when it's genuinely close (banana-pro asks; so do we) — otherwise route and say why.

| Situation | Lane |
|---|---|
| Relatively simple outfit; full prompt control gets there in one shot; styling must read on THIS character's specific body | **Mode 1A** — Banana Pro full-styling prompt |
| Custom/complex fit; wardrobe should be designed separately from casting; faster iteration and variety wanted | **Mode 1B** — Soul Cinema two-step |
| The outfit already exists in an image on some other body, and we want it on our character unchanged | **Mode 5** — two-reference swap |
| Outfit needs to change mid-video, or read in an environment | Not this workflow — lock the outfit here first, then `/jcin-scene-shot` |

The push-back rule from § MODE 1B applies in reverse too: single-shot build with extreme control over how the fit reads on the body → 1A; clean separation of outfit design from casting → 1B.

### Step 2 — Technical-flat ingestion (designed garments only)
For a real or designed garment, feed documentation, not adjectives: technical flats per pattern piece, spec-sheet measurements, hardware callouts ("customized 'K' hardware in stainless steel"), construction notes (pleat manipulation, boning, closures), and front/side/back/three-quarter views. Study visual-only; translate to costume-designer language in the prompt (drape behavior, seam placement, fabric weight — never brand names, per the brand rule in § READING REFERENCE IMAGES). Declare the honest budget: hardest pieces run to ~50 generations; say so before the first one. Corsetry, sheer layers, and structured hoods are the known hard cases.

### Step 3 — Mode 1A path (Banana Pro full styling)
Compose on the canonical Mode 1A prompt structure in § MODE 1A — identity/wardrobe descriptor + pose direction, then the flat shadowless close exactly as written there (gray locked default; flatness never comes off). Wardrobe described head-to-toe with every garment, fabric, fit, structural detail, accessory. Pre-prompt check first, references FIRST in the bullet list, one fenced code block out.

Building a series of bases? Apply the § MODE 1A **variation strategy** verbatim: backdrop locked, vary exactly one parameter per shot (pose → framing → expression → lighting direction), face/skin/core identity never varies.

### Step 4 — Mode 1B path (Soul Cinema two-step — never skip Step 1)
1. **Step 1B.1 — outfit on the bland neutral model.** Use the locked model spec and canonical Step 1B.1 prompt structure in § MODE 1B: slim gender-matched model, normal hair, neutral model face, straight-on relaxed stance, gray seamless, and the **lighter outfit-reference close** — not the full flat-grade paragraph, not the cinema stack. The outfit is the only subject. User saves the result; that image IS the outfit reference.
2. **Step 1B.2 — composite onto the locked character.** Two references (character canonical + the Step 1B.1 output) and the short locked Step 1B.2 prompt from § MODE 1B, unmodified. Do not add styling description (read from image 2), character description (read from image 1), cinema stack, or framing. The lean prompt is the mechanism — padding it degrades the transfer.

Each step gets its own pre-prompt check in the two-step format shown in the section ("Step 1 of 2 / Step 2 of 2").

### Step 5 — Mode 5 path (two-reference outfit swap)
Deliver the **canonical Mode 5 prompt from § MODE 5 exactly as locked — do not modify a word.** The discipline around it is the workflow:
- **Reference order is fixed: @image1 = outfit/pose source, @image2 = character/identity source.** Reversing it breaks the swap. Confirm both roles in the pre-prompt check before shipping.
- No cinema stack, no per-character modifiers, no IP adjustments — the references carry all identity load; the lean prompt is the entire point
- Output lands on gray seamless by design; a different environment = Mode 5 first, then a Mode 3 scene plate on top of the locked result
- Note the surface: the @image indexing is the Banana Pro swap grammar — on Fal wrappers there are no tags at all, so Mode 5 doesn't port; run swaps on Higgsfield

### Step 6 — Group-coordinated lineup variants
For an ensemble in coordinated wardrobe (group photos, stage looks, campaign lineups):
1. Each character's outfit gets built individually first (Steps 3–5) — never prompt a group into new wardrobe cold
2. Coordination lives in the **palette sheets**, not in a shared prompt: pull each character's palette lane + colors-to-avoid and design fits that rhyme across lanes (shared accent hex, shared material family) while each stays inside her lane
3. The group shot itself is a Mode 3 scene plate consuming the locked per-character references — canonical-over-plate, one reference per subject, one face per identity reference
4. Variant passes obey One Variable Per Shot: same lineup, vary formation OR expression OR framing — never two at once

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Music-video wardrobe changes | One locked outfit reference per look; wardrobe changes happen at cuts, never mid-shot; each look validated in a scene before the video prompt cites it |
| Brand/merch on avatars (MyBPM) | Garment is the product — run `/jcin-product-lock` for the garment's own turnaround first, then Mode 1B to cast it; brand-neutral descriptors even for the client's own marks |
| Client lookbook | Mode 1B default (design lane separate from casting lane); one base per look, then the § MODE 1A variation ladder for angles |
| Ad-set wardrobe variants (Dara/Omar stacks) | Mode 5 swaps multiply a winning composition across avatars fast — outfit stays, identity swaps; keep the winning pose source as @image1 across the whole batch |
| Single hero portrait, maximum control | Mode 1A, full styling written, GPT-2 detail pass (Mode 4) only if the user asks and confirms the credit cost |

## Output Requirements

- Named lane (1A / 1B / 5) with one-line fork rationale
- Pre-prompt check(s) — references listed FIRST — then each prompt in its own fenced code block, sequentially labeled for multi-step lanes
- For designed garments: documentation inventory + declared take budget (~50 for hardest)
- For lineups: the palette-lane coordination note (which lanes, which shared accent)
- Universal rules hold everywhere: no names, no brands, no ages, no aspect ratios, no @image placeholders in 1A/1B prompt bodies (attachment happens in the UI; Mode 5's @image grammar is the locked exception)

Execution prompt: references/prompts-v2/character-identity-lock.md — honor its Output Contract.

## Quality Gate

> **🛡️ Anchor before shipping** — `genius.md § Quality Rubric` (Identity persistence, Reference discipline, Prompt economy) + § Anti-Patterns.
- Character was locked before any outfit work — no exceptions slipped through
- Correct lane chosen and defensible in one line; 1B never skipped its Step 1; Mode 5 prompt shipped unmodified with reference order confirmed
- Step 1B.2 and Mode 5 prompts contain zero re-description of what the references show
- Designed garments: construction language traces to flats/specs; a designer would recognize the piece
- Series/lineup work varies exactly one parameter per shot; identity markers never drift
- Flat close intact on every 1A base (three clauses: flat backdrop, shadowless light, zero cast shadow); lighter close on 1B.1 — the full stack appears nowhere in studio character work
- Three failed takes on any one prompt → routed to `/jcin-prompt-doctor` instead of a fourth patch

## Locked-Language Index (pull verbatim — never paraphrase)

Every lane consumes locked blocks from `skills/banana-pro-director/SKILL.md`. This index is the pull map; the blocks themselves stay in the source.

| Lane / step | Locked block to pull | Source section |
|---|---|---|
| 1A prompt body | Canonical Mode 1A prompt structure (flat close included) | § MODE 1A |
| 1A series | Variation strategy list (the four one-variable rungs) | § MODE 1A |
| 1B.1 | Model spec + canonical Step 1B.1 prompt (lighter close) | § MODE 1B |
| 1B.2 | Canonical Step 1B.2 composite prompt | § MODE 1B |
| Mode 5 | The locked lean swap prompt — shipped unchanged | § MODE 5 |
| Any pre-prompt check | Bullet format, references first | § THE PRE-PROMPT CONFIRMATION RULE |
| Reference reads | Wardrobe/jewelry/body-marker extraction lists + naming/brand/age rules | § READING REFERENCE IMAGES |
| Sheet after the base | 3-panel chassis + headless variant language | § MODE 2A (via `/jcin-character-lock`) |

## Common Pitfalls
- **Skipping Step 1B.1 and compositing cold.** The two-step exists because the outfit must exist as a clean visual object before casting; jumping straight to the character makes Soul Cinema invent half the garment. Recovery: build the fit on the bland neutral model first, every time.
- **Padding the Mode 5 prompt.** Adding styling, character description, or the cinema stack to the locked swap prompt creates conflicting instructions and degrades the transfer — the lean prompt IS the mechanism. Recovery: ship it verbatim from § MODE 5; if the output needs more, the fix is better references, not more words.
- **Swapping the @image order.** @image1 outfit, @image2 identity — reversed, the swap breaks silently and the session burns takes chasing a prompt problem that's an attachment problem. Recovery: the pre-prompt check names both roles before anything runs.
- **Describing a designed garment from memory.** "A corset top with denim" loses the boning, the waistband illusion, the hardware — the details that make it KY's garment instead of AI slop. Recovery: flats + measurements + all angles in as references; construction language in the prompt.
- **Coordinating a lineup inside one mega-prompt.** Group wardrobe written cold in a single prompt drifts every character at once. Recovery: lock each fit individually, coordinate through palette lanes, compose the group as a Mode 3 plate consuming locked references.
- **Varying two parameters between takes.** Pose AND lighting changed at once means a failed take teaches nothing. Recovery: One Variable Per Shot — the variation ladder in § MODE 1A, one rung at a time.
