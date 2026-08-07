---
description: One-shot Farrice-voice (or product-context) overlay on any expert-pure output — side-by-side, never destructive
---

# /voice-over — The Overlay Pass

Take ANY artifact (an expert-pure draft, a v2-prompt output, a client piece) and render Farrice's voice — or a named product/brand context — OVER it as a separate take. The expert-pure original is never modified: replication stays measurable, the overlay stays deployable.

## Usage
- `/voice-over <file>` — overlay Farrice's voice (default dial: BLEND)
- `/voice-over <file> --dial MIRROR|BLEND|STRETCH` — explicit dial
- `/voice-over <file> --context <brand>` — overlay a product/brand context (e.g. mybpm, jen) instead of personal voice

## Steps

### 1. Load the layer (never skip)
- Personal voice: `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode per `skills/voice-os/SKILL.md` (default BLEND — "better version of me," never blanket mimicry)
- Brand context: the brand's CLAUDE.md / ground doc (e.g. `_active/mybpm/mybpm-merch-os-run-1/01-ground.md`, `_active/clients/jen-listings/CLAUDE.md`)

### 2. Read the source artifact fully
Identify what carries the EXPERT'S signature (structure, methodology, signature moves, argument architecture) vs. what carries SURFACE VOICE (word choice, rhythm, register, asides).

### 3. Overlay — voice moves, embodiment stays
Rewrite surface voice into the loaded layer while preserving the expert's structural and methodological signature intact. The point of the extraction was their thinking at their level or better; the overlay changes who is SPEAKING, not who was THINKING.

### 4. Deliver side-by-side (never overwrite)
Write the overlay as a sibling file: `<original-name>.voiced.md` (or `.<context>.md`). Present both takes. Prose gate: `python3 execution/prose_classifier.py check <overlay-file>` before delivery.

### 5. Optional jam
If Farrice gives felt verdicts on the pair, bank them to `.agent/jam/taste-ledger.jsonl` (domain: voice-overlay). These dials feed the weekly taste ratchet — scoped by the Embodiment Purity Guard.

## Hard rules
- NEVER modify the expert-pure original.
- NEVER dilute the expert's methodology to make the voice fit — if voice and method conflict, flag the tension, don't average it.
- This workflow composes `skills/voice-os/` — extend that skill, never fork its rules here.
