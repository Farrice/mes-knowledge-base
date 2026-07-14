---
description: "/jcin-voice-lock — voice/persona consistency payloads: pull or produce the bible's quoted Speech/Movement/Stillness/Suno descriptors, format them for their downstream slots (Sound Bed, Subject Lock, vocal casting), and build the per-character aesthetic lane sheet"
---

# Voice Lock (Joey Cinema OS)

"Voice consistency is not a fully recognized thing yet" — no model natively solves it, and Joey didn't wait for one. His workaround changed the game for Control World: a bible carrying how each character speaks, the timbre of their voice, their language and cadences, fed into every prompt so Seedance 2.0 produces consistent voices per character. Voice consistency is a context problem, and this workflow builds the context payloads: the four quoted descriptors per character, slot-formatted so they paste verbatim into the blocks that consume them. If a descriptor can't be pasted verbatim into its downstream slot, it's written wrong.

## Pre-Flight Gate

> **🔒 Gate — bible or build, and the boundary check.**
> 1. Does a bible exist for this world? **Yes** → this is an extraction/formatting pass. **No** → either kick to `/jcin-world-canon` for the full build, or (single character, time-boxed) run the mini character interview here per story-bible-builder Step 3 — one character at a time, never batched — and file the section back into the owning project so the lock is permanent, not session-local.
> 2. **Boundary: character voice ≠ Farrice's voice layer.** These payloads describe fictional/brand personas for generation prompts. VOICE-CARD.md and the voice-os dial govern Farrice's own writing. Separate systems, separate documents — never merge them, never let a character descriptor leak into Farrice-voiced copy or vice versa. If the ask is actually about Farrice's voice, route to `/voice-os` and stop here.

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 15–19 (names drift, "never" clauses, [TBD], prompt-ready payloads, the stranger test); § Hidden Knowledge (voice consistency)
2. `skills/story-bible-builder/references/character-section-format.md` — the exact per-character shape and its Rules block (quoted descriptors, no names inside quotes, one-line visual block)
3. `skills/story-bible-builder/SKILL.md` § **TWO WAYS THE BIBLE GETS USED** (Mode 2 slot mapping) + § **HOUSE PRINCIPLES** (never invent, push on the vague, locks exclude)
4. `skills/cinema-worldbuilder-pro/SKILL.md` § **CANONICAL BLOCKS — REFERENCE** (Subject Lock, Sound Bed) + § **OPTIONAL HANDOFFS** (story bible pairing — the receiving end of these payloads)
5. `extractions/joey-cinema-v3/visual-context.md` § "Voice consistency via a 'Control Bible'" + the CTRL SOL palette-sheet artifact (t=12:25)

## Input Required

- The bible (or the character's raw material: interviews, scripts, the user's description of who this persona is)
- Which characters need payloads this session
- Which downstream tools will consume them (Seedance dialogue, Suno music, stills expression work) — sets which of the four descriptors are in scope
- Existing palette sheets, if any

## Execution

### Step 1 — Pull or produce the four quoted descriptors
Per character, in the character-section-format shape. Produce only what's missing; never overwrite locked bible language — the user's phrasing stays verbatim (their bible, their voice).

| Descriptor | Must capture | Downstream slot |
|---|---|---|
| **Speech** | register, texture, cadence, volume, vocabulary | Sound Bed / dialogue direction |
| **Movement** | gesture quality, gait, combat posture if relevant, tics | Subject Lock |
| **Stillness** | what they do at rest — hands, weight, expression, breath | Subject Lock |
| **Suno** (music scope only) | singing register, timbre, style, signature move | vocal casting for music prompts |

Craft rules, all hard:
- **All four live in quotes** — they are engineered to drop verbatim into future prompts
- **Never the character's name inside the quoted descriptor.** Refer by trait ("low-register voice," "cocked-hip stance"). Names drift models; names live in the section header only
- **Write the visible/audible.** "Cool voice" is not a voice profile — push to register + texture + cadence ("low contralto, dry, clipped sentence-ends, speaks under the room's volume"). Emotion renders in muscle and breath, not adjectives
- **Locks exclude as much as they include.** Each descriptor carries its "never" clause where drift is known ("— never breathy, never sing-song")
- **Never invent.** Unknown timbre → `[TBD]`, flagged to the user. Invented canon becomes locked canon becomes prompt drift

### Step 2 — The verbatim slot test
Paste each descriptor into a skeleton of its receiving block and read it back:
- Speech → `Sound Bed: Diegetic only — [SPEECH DESCRIPTOR], no music, no dialogue except what is physically spoken in frame.`
- Movement + Stillness → `Subject Lock — @tag: [orientation/pose...] [MOVEMENT or STILLNESS DESCRIPTOR as the state language] ... face, hair, wardrobe, and silhouette identical throughout.`
If the sentence breaks, has a name in it, or needs rewording to fit — the descriptor is written wrong. Fix the descriptor, not the slot.

### Step 3 — Per-character color/aesthetic lane sheet
The other half of persona consistency (KY: "even something simple as a color palette sheet for each girl really helps with the consistency between all these characters"). Build in the CTRL SOL artifact format:

```
[CHARACTER] — AESTHETIC LANE
COLOR PALETTE: [named lane, e.g. SOFT SUMMER] — swatch grid / hex values
COLORS TO AVOID: [swatch row — the wrong-answer drift colors]
[one line: material/texture lane if locked — e.g. "matte knits and vinyl, never satin"]
```

Distinct lanes per character are what keep an ensemble readable — each character stays inside her lane, coordination happens across lanes (shared accent), never by collapsing them.

### Step 4 — Assemble the payload card
One card per character, the session's hand-off artifact:

```
VOICE LOCK — [Character] (name appears here ONLY)
Speech:    "..."            → paste into Sound Bed / dialogue direction
Movement:  "..."            → paste into Subject Lock (motion state)
Stillness: "..."            → paste into Subject Lock (at-rest state)
Suno:      "..."            → paste into vocal casting        [if music scope]
Aesthetic lane: palette + colors-to-avoid                     → World Plate grade / wardrobe decisions
[TBD]s outstanding: [list or "none"]
```

File new/updated sections back into the bible at the owning project path. A payload card that lives only in chat is unfinished work.

### Step 5 — The stranger test
Final read: could a stranger who has never heard of this story write a scene with this character — voice, movement, palette — using only these payloads, and get it right? Anything they'd have to guess is a gap; fill it or mark `[TBD]`.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Seedance dialogue/performance shots | Speech feeds Sound Bed; Movement/Stillness feed Subject Lock; the worldbuilder's grammar does the rest — hand payloads over per its § OPTIONAL HANDOFFS pairing |
| Music production (Suno) | Suno descriptor is the casting instrument — register, timbre, style, signature move; per-track prompts cite it verbatim; no song names or lyrics leak into video Sound Beds (diegetic only there) |
| Brand persona / mascot (MyBPM-class) | Same four descriptors work for a brand avatar; Speech doubles as the character's spoken-content register in UGC-style videos; lane sheet keys to the brand palette with an avoid-row against the brand's known drift |
| Stills-only worlds | Movement/Stillness still matter — they set default pose energy and expression register in Banana Pro prompts; Speech/Suno drop out of scope |
| Ensemble scenes | Pull every present character's payloads plus the bible's ensemble dynamics for Cross-Frame Rules; one Subject Lock per character, each carrying its own Movement/Stillness language |

## Output Requirements

- One payload card per character in the Step 4 format — four quoted descriptors (or explicit scope-outs), lane sheet, `[TBD]` list
- Zero character names inside any quoted descriptor; names in headers only
- Every descriptor passes the verbatim slot test as delivered
- New canon filed back into the bible file, not left in chat; user's locked phrasing preserved verbatim
- The Farrice-voice boundary stated once in the delivery when any ambiguity existed in the ask

Execution prompt: references/prompts-v2/world-bible.md — honor its Output Contract.

## Quality Gate

> **🛡️ Anchor before shipping** — `genius.md § Quality Rubric` (Identity persistence, Reference discipline) + § Anti-Patterns ("inventing canon to fill a gap; locks without 'never' clauses").
- Every quoted descriptor is paste-ready: quoted, name-free, slot-shaped, visible/audible language only
- "Never" clauses present wherever drift is known; at least one per character unless the user explicitly has none
- Nothing invented — every claim traces to the bible, the source material, or the user's own words; `[TBD]`s surfaced, not filled
- Lane sheet has a real colors-to-avoid row, not decoration
- The stranger test passes, or its failures are listed as named gaps
- No bleed across the boundary: no VOICE-CARD language in character payloads, no character language proposed for Farrice's own writing

## Common Pitfalls
- **Names inside the quotes.** "Sol speaks in a low contralto" pastes a drift vector into every downstream prompt. Recovery: trait-referenced only inside quotes ("low contralto, dry, clipped"); the name lives in the card header and nowhere else.
- **Adjective profiles.** "Warm, confident voice" survives the slot test grammatically and fails it functionally — no model can render "confident." Recovery: push to register, texture, cadence, volume, vocabulary; emotion in breath and muscle.
- **Waiting for the model feature.** Voice profiles keep being announced; consistency keeps being a context problem today. Recovery: build the payloads now — bible descriptors into every prompt is the working mechanism.
- **Batch-interviewing characters.** Three personas in one pass produces three shallow locks. Recovery: one character at a time, iterate until the user locks it, then the next — depth beats count.
- **Session-local canon.** Payloads that live only in the chat evaporate, and next week's session re-invents the voice slightly differently — which is drift by another door. Recovery: file every new or sharpened section back into the bible file before closing.
- **Merging the voice systems.** A character's Speech descriptor drifting into a LinkedIn draft, or VOICE-CARD cadence rules shaping a K-pop persona — both corrupt both. Recovery: the boundary check in the gate runs on every ambiguous ask; route Farrice-voice work to `/voice-os`.
