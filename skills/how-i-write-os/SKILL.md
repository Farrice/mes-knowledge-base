---
name: "How-I-Write OS — Master Writing Conductor"
description: "Compose any writing/content/marketing mission across the ten How I Write experts and the existing story-stack — a conductor that owns NO craft: diagnoses the intent, picks the smallest sufficient stack of forged experts (3-6, never all 10), sequences them by altitude (architecture to scene to line to truth), keeps ONE author on the body voice, and always ends on a truth/clamp/prose gate. Trigger words: how I write, write this, compose, essay, profile, founder story, manifesto, newsletter, VSL, brand voice, social post, contemplative piece, ghostwrite. Do NOT use for: pure speed copy (/copy-engine), deepening an existing good draft (/deepen, /depth-audit), research synthesis (execution/research.py), or actual Parallax editions (/parallax — supplies craft layers inside it, never rebuilds it)."
version: "1.0"
format: "conductor"
extracted_from: "Composition of 10 How I Write experts + story-stack (Runia → Hawley → Stanton → Albom → Browder/Orlean/Wang/Wright → Connelly/Harding/Ocean/Shukman → Ward → Lulu → really-real)"
expert: "How-I-Write OS (conductor over the How-I-Write roster + story-stack)"
domain: "Cross-cutting Writing × Composition × Reader Impact"
tier: system
---

# How-I-Write OS — Master Writing Conductor

A finished draft can still have no spine. Most writing fails not for lack of craft but for lack of *composition* — the wrong experts, in the wrong order, all reaching for the pen at once until the prose homogenizes into competent, hollow mush. The How-I-Write OS is the conductor that walks in before a word is written, reads what the piece actually needs, picks the *smallest sufficient* stack of experts who already own that craft, sequences them by altitude, keeps exactly one author on the body voice, and ends every run on a truth/clamp/prose gate. It owns no craft of its own. The ten "How I Write" experts and the existing story-stack already own all of it; this OS only decides *who plays, in what order, and how lightly.* Its entire intelligence is restraint.

## Role

The OS is a router, not an author. Given a writing/content/marketing intent and raw material, it: (1) runs the **Runia story-vs-topic gate** to confirm a story even exists; (2) looks up the intent's named stack in `references/composition-map.md`; (3) cuts that stack to the smallest sufficient set — 3 to 6 experts, never all 10; (4) sequences them top-down through the **altitude stack** (architecture → mid-layer → scene/voice → line → distribution → truth); (5) appoints ONE Layer-4 expert as the **body-voice owner** while every other expert advises from the wings; (6) closes on the mandatory gate; and (7) returns the finished piece plus an Output Receipt. Composing existing engines — never rebuilding — is the same law as `stanton-produce` and `writing-depth-layer`.

## Roster

The ten "How I Write" experts plus the story-stack they slot into. One lane each, one front-door command each. Full lane disambiguation (no collisions between near-adjacent experts) lives in `genius.md § The Lane Map`.

| Expert | Lane (what they own) | Front-door command |
|--------|----------------------|--------------------|
| **Tim Runia** *(story-stack gate)* | Story-vs-topic gate — does a story exist here (want → tension → change)? Runs FIRST, always. | `/runia-story-test` |
| **Noah Hawley** *(story-stack)* | Theme + ending-first — the reason the piece exists and where it lands, locked before prose. | `/hawley-theme-engine` |
| **Andrew Stanton** *(story-stack)* | Premise / spine / clamp — the one-line premise and the beat-to-beat attention architecture under the whole piece. | `/stanton-premise-sentence` |
| **Mitch Albom** | One human truth — theme-first emotional architecture; the feeling earned by restraint so it "cuts the flesh." | `/albom-theme-first-engine` |
| **Bill Browder** | High-stakes nonfiction — making dry/complex/dangerous material grip and rendering a real adversary through unassailable evidence. | `/browder-drama-excavation` |
| **Susan Orlean** | Curiosity-driven profile — the small overlooked subject that secretly carries a large theme; seducing a reader who thinks they don't need it. | `/orlean-telling-subject` |
| **Dan Wang** | Literary treatment of analysis — dense domain insight turned into voice-driven nonfiction that rewards a re-read. | `/wang-friction-map` |
| **Wright Thompson** | Lyric long-form immersion — reaching the universal through deeply-inhabited scene and interiority. | `/wright-interiority` |
| **Michael Connelly** | Economy + momentum + the ONE telling detail — the reader can't find a place to stop. The default scene-voice. | `/connelly-rewrite` |
| **Paul Harding** | Lyric perception — slowing attention to the pre-linguistic instant so the ordinary turns luminous. | `/harding-perception-engine` |
| **Ocean Vuong** | Estrangement / defamiliarization — rupturing the AI-median sentence so it passes the Species Test; the anti-slop voice. | `/estrangement-engine` |
| **Henry Shukman** | Contemplative wonder + presence — the largest feeling carried on the smallest true concrete particular, in total sincerity. | `/shukman-concrete-doorway` |
| **Ward Farnsworth** | Memorable line / rhetoric — diagnose, then deploy ONE device on the one line that must be remembered. | `/ward-rhetorical-engine` |
| **Lulu Cheng Meservey** | Distribution / positioning — the strategy + conviction spine when the piece must move a market. | `/lulu-reality-architect` |

The truth/clamp/prose **gate** that closes every run is the `really-real-*` family (`/really-real-writing`) + Stanton `/stanton-clamp-audit` + the deterministic `prose_classifier.py check` — a quality floor, not a roster seat.

## Intent → Stack (quick table)

Look up the intent, run the named stack in order. Every stack is bookended by the universal gates (OPEN = Runia story-test; CLOSE = really-real + clamp-audit + slop gate) — not repeated below. `[VOICE]` marks the single body-voice owner. The exact ordered stack with sub-commands and omissions lives in `references/composition-map.md`.

| # | Intent | Stack (smallest sufficient) | `[VOICE]` owner |
|---|--------|------------------------------|------------------|
| 1 | **Literary / personal essay** | Hawley → Shukman (ripeness) → **Shukman** (or Harding if lyric-description-led) → Ward (close only) | Shukman |
| 2 | **Founder origin story** | Stanton (brand-origin) → Browder (real jeopardy) → **Albom** (the one human truth) → Ward · +Lulu if positioned publicly | Albom |
| 3 | **High-stakes nonfiction / investigative** | Stanton (spine) → Browder (lane owner) → **Connelly** (or Wright immersive) → Ward · `verify`/truth-audit mandatory | Connelly |
| 4 | **Profile (person or brand)** | Orlean (telling-subject + go/no-go) → Orlean (card structure) → **Orlean** (yarn engine, Connelly renders scenes inside) → Ward | Orlean |
| 5 | **Substack / newsletter edition** | Hawley → Wang (analytical) OR Orlean (narrative) → **Connelly** (slingshot lede) → Ward · route actual editions to `/parallax` | Connelly |
| 6 | **Analytical thread / annual letter** | Wang (big-questions + friction) → Wang (annual-letter + texture-zoom) → **Wang** (musical pass) → Ward | Wang |
| 7 | **Manifesto / keynote** | Hawley (one idea) → Lulu (new reality + contrarian stake) → **Lulu** (conviction body) → Ward (sparingly) | Lulu |
| 8 | **VSL / converting copy** | Stanton (sales arc) → Browder (real jeopardy/proof) → Lulu (belief sequence) → **copy-engine** body (Connelly detail) → Ward · hard honesty-spine gate | copy-engine |
| 9 | **Brand voice / positioning** | Lulu (line-in-sand + new reality) → Ocean OR Harding OR Shukman (perceptual voice) → **chosen Layer-4** → Ward (tagline) · `oren-brand`/`build-bos` own the spine | the chosen voice expert |
| 10 | **Social post / hook** | Stanton (30-sec arc) → **ONE of** Connelly / Ocean / Shukman / Albom by goal → Ward (one device) · `linkedin-daily`/`diandra` own cadence | the chosen voice expert |
| 11 | **Contemplative / wonder piece** | Shukman (register + surrendered draft) → **Shukman** (concrete doorway) → Harding (optional luminous precision) · Shukman vetoes faked awe | Shukman |
| 12 | **Ghostwriting a client voice** | Albom (voice-DNA) OR Connelly (edge/economy) → **the single chosen expert holds the entire body** → Ward (à la carte) | the single chosen expert |

**Quick selection logic when the intent is ambiguous** (full version in the composition map): (1) Market to move? Yes → Lulu at Layer 6, else omit. (2) Material dangerous/dry, overlooked, analytical, or invented? → Browder / Orlean / Wang / (Pressfield·Wright), pick exactly one. (3) Target feeling meaning, wonder, momentum, or strangeness? → Albom / Shukman / Connelly / Ocean, pick exactly one as `[VOICE]`. (4) A single line must be remembered? Yes → Ward, one device. (5) Always open on Runia, close on the gate.

## How to Invoke

```
/how-i-write <objective + raw material>
```

- **Objective** = what you want to exist and for whom: "a founder origin story for the MyBPM launch," "a contemplative Substack essay on attention," "a VSL for the Authority Flywheel offer," "ghostwrite Jen's first-time-buyer post in her voice." The more DICE-sharp the objective (Deliverable, Audience, Context/constraints, End state, Specific language), the tighter the stack.
- **Raw material** = the seed: notes, transcript, an outline, a thought-bank fragment, a half-draft, source facts, the offer details. Paste it inline or point to a file path.

What the OS does, in order:

1. **Gate (Runia).** Run `/runia-story-test` on the raw material — does a story exist (want → tension → change)? If not, either `/runia-tension-dig` to find one or route to a non-narrative engine and say so.
2. **Diagnose + select.** Match the objective to an intent row above, pull its named stack from `references/composition-map.md`, then cut to the smallest sufficient set (3–6). Name the body-voice owner.
3. **Sequence + run.** Execute the experts top-down through the altitude stack. Load each expert's `genius.md` + the named workflow; apply the move *into* the prose. One author holds the body voice; the rest advise.
4. **Close on the gate.** `really-real-*` (truth) + `/stanton-clamp-audit` (no slack) + `prose_classifier.py check <file>` (no slop). A run without the gate is incomplete.
5. **Return.** The finished piece + the **Output Receipt** (see `genius.md`) — every move mapped to its expert, the body-voice owner named, and the "experts deliberately NOT used" line that proves restraint. Then finalize per The Chain (Step 6).

**If a draft already exists**, do not run the full stack on it. Route to `/depth-audit` (diagnosis) → `/depth-inject` (single surgical move) from the Writing Depth Layer first; refining slop on a misdiagnosed draft wastes the stack. The felt verdict wins over any gate score.

## Composition Rules (summary)

1. **Pick the smallest sufficient stack.** Start from the intent's named stack in `references/composition-map.md`; add a layer only when a deficit is *confirmed*, never speculatively. Most missions resolve on a **gate → architecture → one mid-layer → one voice-layer → one line-layer → truth-pass** spine of 4–5 experts.

2. **Compose existing engines — never rebuild.** Every craft move is owned by a forged expert with a front-door command. If you find yourself writing a hook formula or a restraint rule from scratch, stop — an expert owns it. (Same law as `stanton-produce`: "orchestrates existing engines; never rebuilds production." For actual Parallax editions use `/parallax`; for body copy use `/copy-engine`; for LinkedIn from scratch route to Lara via `/ghostwrite` — the OS supplies craft layers *inside* these, never replaces them.)

3. **Never run all 10 — restraint is the whole discipline.** A stack of 7+ means an adjacent lane was double-picked; consult the Lane Map and cut to one expert per altitude band. More experts ≠ better. The load-bearing repo lessons: *"More experts ≠ better for voice"* — the Diandra Sandwich scored 4/10 disjointed while the single-author draft beat every escalation (`feedback_diandra-hooks-only-separation.md`); and the multi-engine rebuild degraded already-elevated work to 3/10 while the system scored it 7.5–8.6 (`feedback_multi-engine-rebuild-degrades-elevated-content.md`).

4. **One author owns the body — preserve the spine.** Exactly one Layer-4 expert is the body-voice owner whose fingerprint the prose carries; every other expert *advises* (supplies a move, a line, a diagnosis) without taking the pen. Never let six experts homogenize the prose into composite mush. Architecture before scene before line before truth — inverting the order yields gorgeous sentences with no spine. When a draft is already good, preserve the spine and make small surgical passes; never rebuild what works.

5. **Always end on a truth/clamp/prose gate.** Layer 7 is mandatory: `really-real-*` (truth/compassion/reader-trust) + `/stanton-clamp-audit` (no slack moment) + `prose_classifier.py check` (no AI slop). For VSL/converting copy, add the hard honesty-spine gate. A run without the gate is not finished.

6. **Integrate moves invisibly; prove restraint.** Never name-drop experts inside the prose — moves are integrated silently, experts named only in the Output Receipt. The "experts deliberately NOT used" line is not optional; it is the proof of restraint that keeps the OS from sliding back into running all ten.

## Quick Reference

- **Composition / routing intelligence:** `skills/how-i-write-os/genius.md` — the altitude stack, the Lane Map (no collisions), the Composition Rules, and the Output Receipt format. No craft re-teaching.
- **References:** `skills/how-i-write-os/references/composition-map.md` — the intent → altitude-stack decision tree (12 intents), exact ordered stacks with sub-commands and deliberate omissions, plus the quick selection logic for ambiguous intents.
- **Sibling conductors (same posture):** `skills/writing-depth-layer/SKILL.md` (deepen an existing draft) · `stanton-produce` (end-to-end production conductor). This OS composes *who writes from scratch*; the Depth Layer composes *who deepens what already exists*.
