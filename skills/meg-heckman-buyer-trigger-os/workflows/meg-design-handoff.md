---
description: "/meg-design-handoff — convert a LEAD concept (from /meg-trigger-audit or /meg-concept-sprint) into execution-ready artifacts: trigger-grounded image-generation prompt + composition brief (for Satori stacking) + typography brief (for Kittl stacking). Trigger before taste — Meg decides WHAT, execution experts decide HOW it looks."
---

# Design Handoff

A LEAD concept earns that verdict by surviving the trigger audit. This workflow's only job: translate that trigger into instructions a generation tool or print designer can execute without losing the buyer. Every line of the image prompt encodes psychology, not aesthetics. The "Still Synced" prompt is the proof-of-pattern: buyer scene first, niche-specific avoid-list, micro-text that does identity work. Anything less ships decoration.

## Pre-Flight

Read these files before executing:
1. `skills/meg-heckman-buyer-trigger-os/genius.md` (Six Triggers, Design Mechanics, 50ms Gate)
2. The LEAD output from `/meg-trigger-audit` or the TEST SLATE output from `/meg-concept-sprint` — both required to populate the intake fields below

> **🔒 Pre-Flight Gate**: Every intake field in Step 1 must be populated before any prompt is written. A missing social moment or unspecified emotion layers means the concept was never fully resolved upstream — send it back. A handoff on an incomplete concept produces a prettier poster.

---

## Workflow

### Step 1: Concept Intake (Gate — all five fields required)

The following five fields travel from the upstream workflow. If any are absent or underspecified, return to the originating step with a precise ask — do not extrapolate.

| Field | What it must contain | Fail condition |
|---|---|---|
| **Identity statement** | First-person sentence: "I ___" — what wearing this says | Demographic description instead of a self-claim |
| **Familiar/twist pair** | Both halves named explicitly; twist is conceptual, still in-world | One half missing; twist requires explanation |
| **Buyer behavioral moment** | A person in a scene, not a category ("leaving a 3:17 AM warehouse set whose body still feels locked to the kick pattern") | "EDM fans," "people who hike," demographic shorthand |
| **Emotion layers** | 2–3 named: humor + belonging + pride; surface humor alone fails | Single-layer read; "it's funny" |
| **Social moment** | The specific future reaction: who says "that is SO you," who receives it as a gift, who tags whom | "Someone might share it" — no specific person named |

**If any field fails:** write the field name and the exact ask, return to `/meg-concept-sprint` or `/meg-trigger-audit`, and halt. No handoff on incomplete concepts.

---

### Step 2: Image-Generation Prompt Construction

The exemplar is the "Still Synced" prompt from the MyBPM proof set. It encodes the trigger, not the look. Every prompt written here follows the same five-part anatomy — in order.

**Exemplar (from `extractions/meg-heckman/video-context-7MNa2YTPGs4/meg-heckman-buyer-trigger-os-harvest.md`, MyBPM Prompt Upgrade section):**

> *"Create a premium black streetwear T-shirt for MyBPM called 'Still Synced'. The buyer is the person leaving a 3:17 AM warehouse set whose body still feels locked to the kick pattern after the lights come up. Center the design around a precise pulse-grid graphic: thin electric-blue BPM lines, magenta phase-shift markers, and a subtle green heartbeat trace that feels like music data becoming body memory. Integrate small text: 'MY.BPM' and 'STILL SYNCED / 03:17 AM'. The visual should feel like modern rave identity, not generic EDM decoration: restrained, wearable, high-contrast, and collectible. Use one main graphic system with enough negative space to look premium on a real shirt. Avoid DJ decks, crowd silhouettes, festival clichés, random neon chaos, and overcomplicated fractals."*

**Five-part anatomy — follow this order, never invert it:**

**(a) Buyer scene first** — the opening sentence names the person in their behavioral moment. Not the product, not the aesthetic — the person, what just happened to their body or mind, what they're still carrying. The scene encodes the trigger; everything else executes it.

**(b) One main graphic system + negative space** — name the single graphic element, its sub-components, and the quality constraint. "One main graphic system with enough negative space to look premium on a real shirt" is the 50ms gate in execution language. Three graphic systems = three things quietly = audit fail.

**(c) Integrated micro-text as identity claim** — the words on the garment are the identity statement made visible. Spec the brand name + claim line + in-world anchor (timestamp, code, shorthand) explicitly: what the words are and what they complete conceptually. The exemplar's "STILL SYNCED / 03:17 AM" is a body-memory record, not a label.

**(d) Niche-specific avoid-list** — name 4–8 visual clichés belonging to this exact niche. Generic avoid-lists produce generic results. The EDM list earned its specificity from the Familiar Bank: DJ decks, crowd silhouettes, festival clichés, random neon chaos, overcomplicated fractals. Build the equivalent from the niche's existing bestsellers.

**(e) In-world aesthetic anchors** — 3–4 adjectives that locate the visual in the niche's vocabulary without mimicking a specific brand. "Modern rave identity, not generic EDM decoration: restrained, wearable, high-contrast, collectible" replaces vibe-words with concrete position claims.

**Prompt quality check before proceeding:**
- First sentence is the buyer scene, not a style direction
- Avoid-list contains THIS niche's clichés, not a generic list
- Micro-text is spelled out and carries an identity claim
- Exactly one graphic system is named
- No prompt poetry: concrete nouns beat vibes ("pulse-grid graphic" beats "energy field")

---

### Step 3: Composition Brief (→ Satori Stacking)

Translates the 50ms gate into placement and hierarchy decisions. Does not re-describe the concept.

**Focal hierarchy** — name the single element that reads first in 50 milliseconds. Everything else is supporting structure. Two competing elements means the 50ms gate fails before the file opens.

**Eye-flow note** — where the eye moves after the focal element: identity claim in micro-text, secondary glyph reinforcing the twist, or negative space. Three beats maximum (land → move → rest).

**Garment placement and scale** — center-chest / left-chest / full-back / sleeve-panel; approximate scale relative to the chest box. Two checks: does it read at arm's length on a hanger (retail gate)? Does it read in a 150px feed thumbnail (social gate)?

**Print-method constraint** — single-color, two-color, DTG, screen, embroidered patch. When a design's visual complexity exceeds the method's fidelity, revise the prompt — don't work around it in production.

---

### Step 4: Typography Brief (→ Kittl Stacking)

The words ARE the identity statement; the type mood is a second layer of it.

**The words and their role** — list every text element and its trigger function: brand name (who we are), claim line (what wearing this says), in-world anchor (timestamp, code, shorthand signaling sub-identity belonging). Each text element must do trigger work; decorative type is a poster move.

**Type mood matched to emotion layers** — match the typographic register to the concept's primary emotion layer, not the niche's generic aesthetic. High-contrast precision signals "collectible"; condensed block signals "badge"; hand-drawn signals "DIY pride." Match the emotion, not the genre.

**Legibility constraint** — reads in a 150px feed thumbnail. Declare: is the micro-text read-at-distance or worn-for-yourself? Both are valid; both require a sizing decision.

**Type treatment integration** — standalone element, integrated into the graphic system, or embedded in negative space. "STILL SYNCED / 03:17 AM" is a body-memory record embedded in the graphic world — not type on top of a design.

---

### Step 5: Routing Note (Visual Tool Pre-Flight)

Prompts are the deliverable. Generation runs only with approval — declare cost-gate status at the top of the brief.

| Concept type | Route | Gate |
|---|---|---|
| Photoreal person / body scene | Higgsfield Soul | Cost-gated |
| Stylized graphic / streetwear mock | fantastic-posters skill (`skills/fantastic-posters/`) | Cost-gated |
| Poster-print / standalone art | fantastic-posters skill | Cost-gated |
| Brand logo / mark exploration | Kittl via typography brief | No generation cost |

The prompt pack must survive routing: concrete scene descriptions transfer across tools; vibe-poetry is model-dependent and breaks on swap. Write for the buyer, not a specific model's tendencies.

**Cover note (add to brief header):** "Generation is COST-GATED. These prompts are the deliverable. Run generation only after Farrice approves. Tool route: [Higgsfield Soul / fantastic-posters / Kittl]."

---

### Step 6: Variant Strategy (2–4 Variants)

The buyer scene is locked. The person does not change. Variants explore how the TWIST is rendered — different visual expressions of the same identity claim.

**Variation axes (pick 2–3 per set, change one per variant):**
- **Graphic system** — same scene, different visual metaphor (pulse-grid vs waveform vs circuit trace)
- **Color system** — same graphic, different palette shifting the aesthetic anchor (warehouse-dark vs clinical-white vs oxidized-metal)
- **Micro-text treatment** — same claim, different integration (embedded vs standalone vs ghosted)
- **Density** — same elements, compressed (sticker gate) vs breathed-out (poster-print)

**What does NOT vary:** buyer behavioral moment, identity statement, niche-specific avoid-list. Those are the trigger. Variants render it differently; they do not test different triggers.

Label each variant by axis, not quality rank:
```
VARIANT A — [graphic system: pulse-grid]
VARIANT B — [graphic system: waveform / color: oxidized-metal]
VARIANT C — [density: sticker-compressed]
VARIANT D — [micro-text: typographic standalone]
```

---

## Format Adaptations

| Format | Adaptation |
|--------|-----------|
| T-shirt (center-chest) | Full workflow as-is; scale note: 9–11 inch wide graphic is the standard chest-box |
| Hoodie (chest + sleeve) | Two placement passes in the composition brief; sleeve treatment usually strips the graphic to micro-text only |
| Sticker / small format | 50ms gate tightens: the focal element must read at 2 inches; micro-text becomes optional ornamentation, not primary identity carrier |
| Poster-print | Negative space expands; type can carry more weight; focal hierarchy loosens to allow secondary narrative; cost-gate still applies |
| Brand logo / mark exploration | The NAME does the trigger work first (Sloth Hiking Club IS the joke); score the name as an identity statement before generating any mark; type brief precedes image brief |

---

## Output Format

```
DESIGN HANDOFF — [brand/project] — [concept title] — [date]

⚠️  GENERATION IS COST-GATED — prompts are the deliverable — run generation only after Farrice approves
Tool route: [Higgsfield Soul / fantastic-posters / Kittl]

INTAKE CONFIRMATION
Identity statement: "I ___"
Familiar/twist: ___ / ___
Buyer behavioral moment: ___
Emotion layers: ___ + ___ + ___
Social moment: ___
[GATE: PASS — all five fields confirmed / BLOCKED — missing: ___, return to /___]

IMAGE PROMPT (primary)
[Full prompt following the five-part anatomy; buyer scene is sentence one]

COMPOSITION BRIEF (→ Satori)
Focal hierarchy: ___
Eye-flow: land → move → rest
Placement + scale: ___
Print-method constraint: ___

TYPOGRAPHY BRIEF (→ Kittl)
Text elements + trigger role: ___
Type mood: ___
Legibility constraint: ___
Integration treatment: ___

VARIANTS (2–4)
VARIANT A — [axis]:
[prompt]
VARIANT B — [axis]:
[prompt]
(...)

NEXT: /fantastic-posters or /higgsfield after approval · /meg-listing-copy once visual is confirmed
```

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: review against `genius.md § Anti-Patterns` before delivering.
- Intake gate ran: all five fields confirmed before any prompt was written.
- Every prompt opens with the buyer scene, not the style direction.
- Avoid-list names THIS niche's clichés — not a generic list.
- Micro-text is an identity claim, not decoration — each text element's trigger role is declared.
- 50ms constraints are encoded in the composition brief: one focal element named, competing elements flagged.
- Variants vary the rendering axis, not the buyer scene — the person is locked.
- Generation is flagged as cost-gated on the brief cover.
- No handoff was issued on a concept missing any of the five intake fields.

## Common Pitfalls

- **Style-first prompts.** The prompt opens with the aesthetic mood instead of the buyer scene. Result: a beautiful decoration generator. Recovery: move the buyer scene to sentence one, every time.
- **Generic avoid-lists.** "Avoid clichés" produces the median result for the niche. Recovery: pull the avoid-list from the Familiar Bank and existing category bestsellers; name the 4–8 specific visual moves that every competitor is already running.
- **Variant sprawl that varies the person.** The buyer behavioral moment shifts across variants to test different identity claims — that is a new sprint, not a variant set. Recovery: lock the opening scene, vary only the visual rendering axis.
- **Prompt poetry that no image model parses.** "Energy that resonates with post-set euphoria" gives the model nothing concrete to execute. Recovery: concrete nouns beat vibes — "thin electric-blue BPM lines, magenta phase-shift markers" is parseable; "vibrant rave energy" is not.
- **Skipping the intake gate.** If the concept's emotion layers are vague or the social moment is generic, the handoff produces a prompt with no trigger inside it. Recovery: the intake gate is not a formality; a blocked handoff is the correct output when upstream work is incomplete.
