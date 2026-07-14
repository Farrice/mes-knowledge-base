---
date: 2026-07-13
session: guide-library-backfill
tier: operator-guide
status: enriched
---

# How-I-Write OS — What We Built 2026-06-26 and How to Use It

> Ten writing masters from David Perell's "How I Write" series, each forged into a standalone skill, composed by one master conductor. ~137 workflow commands total — this guide is deliberately a MAP, not a catalog: the front door, the clusters, and how to find the right sub-command. Front door: `/how-i-write` · conductor spine: `skills/how-i-write-os/SKILL.md` + `genius.md` · routing table: `skills/how-i-write-os/references/composition-map.md`. Extend the OS; never rebuild a writing engine.

## ⚡ If you only read 10 lines

- One front door: `/how-i-write <objective + raw material>` — the OS diagnoses intent and composes the right subset itself. You almost never need to remember the 137.
- Inputs: **OBJECTIVE** (what the piece must do) + **FORMAT** (essay / founder-story / VSL / thread / ...) + **RAW MATERIAL** (notes, transcript, half-draft).
- The four laws: compose existing engines, never rebuild · smallest sufficient stack (3-6, never all 10) · **ONE author owns the body voice** · always end on the gate.
- Every run opens on the Runia story-vs-topic gate (`/runia-story-test`) and closes on `/stanton-clamp-audit` + `prose_classifier.py check` + `/really-real-writing` + `verify` if real claims.
- Existing good draft? Do NOT run the full stack — `/depth-audit` → `/depth-inject`, one surgical move.
- 12 named intents live in `references/composition-map.md`; the SKILL.md quick table maps each to its stack and body-voice owner.
- Lane collisions (Browder vs Orlean vs Wang; Connelly vs Harding vs Ocean vs Shukman) are resolved by the Lane Map in `genius.md` — one expert per altitude band.
- Every run returns the piece + a **Receipt**, including the mandatory "experts deliberately NOT used" line — the proof of restraint.
- Single tactic? Call the single expert directly (e.g. `/ward-saxon-punch` for one punchy line) — the conductor earns its overhead only for cross-altitude composition.
- Production engines keep their lanes: `/parallax` owns editions, `/copy-engine` owns converting copy, `/writers-room` owns draft-polish, `/linkedin-daily` owns cadence. The OS supplies craft *inside* them.

## Command table — the front doors that matter

| Command | Produces | Reach for it when |
|---|---|---|
| `/how-i-write <objective + material>` | Finished piece + Receipt, composed across 3-6 experts | The piece needs architecture + voice + line + gates |
| `/runia-story-test` | Story-vs-topic verdict (want → tension → change) | "Is there even a story here?" |
| `/stanton-premise-sentence` | One-line premise + spine | Attention architecture under almost any piece |
| `/hawley-theme-engine` | Theme + ending-first lock | Why the piece exists and where it lands |
| `/browder-drama-excavation` | High-stakes jeopardy from dry/dangerous material | Nonfiction that must grip AND survive scrutiny |
| `/orlean-telling-subject` | Curiosity-driven profile angle | An overlooked subject that must be seduced into mattering |
| `/wang-friction-map` | Analytical essay engine (stated story vs ground truth) | Threads, annual letters, dense analysis |
| `/connelly-rewrite` | Economy + momentum + the one telling detail | Default scene-voice for commercial/content work |
| `/harding-perception-engine` | Lyric perception, luminous description | Lyric-led prose |
| `/estrangement-engine` (Ocean) | Defamiliarized, anti-slop voice | Rupturing the AI-median sentence |
| `/shukman-concrete-doorway` | Contemplative wonder, total sincerity | Presence pieces; Shukman vetoes faked awe |
| `/albom-theme-first-engine` | One human truth, emotional architecture | The piece must *move*, not impress |
| `/ward-rhetorical-engine` | ONE classical device on the one load-bearing line | A line must be remembered |
| `/lulu-reality-architect` | Distribution/positioning conviction spine | Only when a market must move |

## The mental model

1. **The conductor owns no craft — its entire intelligence is restraint.** It diagnoses, selects, sequences, and gates. Every actual move is owned by a forged expert with a front-door command. If it starts writing a hook formula from scratch, something is wrong.
2. **Altitude order is load-bearing.** Architecture → mid-layer → scene/voice → line → distribution → truth. Inverting it yields gorgeous sentences with no spine.
3. **One author, one heartbeat.** Multi-author bodies homogenize into composite mush — the calibrated evidence: the Diandra Sandwich scored 4/10 disjointed while the single-author draft beat every multi-expert escalation. The other experts advise from the wings; they never take the pen.
4. **Lanes never collide by design.** Browder (thriller jeopardy) vs Orlean (curiosity journalism) vs Wang (analytical essay) in nonfiction; Connelly (economy) vs Harding (lyric maximalism) vs Ocean (estrangement) vs Shukman (wonder) in perception; Albom (emotion) vs Shukman (wonder). Pick exactly one per band.

## How to find the right sub-command (the map, not the catalog)

Three lookup layers, cheapest first:

1. **Don't look — use the front door.** `/how-i-write` runs the lookup for you: it classifies your FORMAT into one of 12 intents, pulls the named stack, and names the body-voice owner out loud before writing.
2. **The intent table** in `skills/how-i-write-os/SKILL.md` — 12 rows (essay, founder-story, high-stakes nonfiction, profile, Substack, analytical thread, manifesto, VSL, brand-voice, social, contemplative, ghostwrite), each with its ordered stack and `[VOICE]` owner. Thirty seconds to a named plan.
3. **The deep references** — `references/composition-map.md` (exact ordered stacks with sub-commands AND deliberate omissions) and `genius.md` (the Altitude Stack, the Lane Map, the Receipt format). Only needed when overriding the conductor's pick.

Quick selection logic for ambiguous intents: market to move? → Lulu, else omit · material dangerous/dry, overlooked, or analytical? → Browder / Orlean / Wang, exactly one · target feeling meaning, wonder, momentum, or strangeness? → Albom / Shukman / Connelly / Ocean, exactly one as `[VOICE]` · one line must be remembered? → Ward, one device · always open Runia, always close on the gate.

## Worked shape of a run

`/how-i-write a founder origin story for the MyBPM launch — material: <notes>` → intent row 2 → stack: Stanton brand-origin → Browder founder-warstory → **Albom** (body voice) → Ward close → gates. The Receipt then shows each move mapped to its expert, the advisors' single contributions, and the deliberately-omitted experts (Wang, Orlean, Shukman) with one-line reasons.

## When NOT to use the conductor

- One tactic → one expert: punchy close → `/ward-saxon-punch`; "is this a story?" → `/runia-story-test`; tighten → `/stanton-clamp-audit` or `/connelly-rewrite`.
- Refine an existing good draft → `/depth-audit` → `/depth-inject` (the Writing Depth Layer owns deepening; the felt verdict wins over any gate score).
- Polish a drafted LinkedIn post → `/writers-room` · LinkedIn from scratch → `/ghostwrite` (Lara/Cole) · daily cadence → `/linkedin-daily`.
- Actual Parallax edition → `/parallax` · converting body copy → `/copy-engine` · client ghostwriting → single voice expert via `/ghostwrite`, never a composite body.
- Pure system/non-deliverable asks → no chain, no conductor.

## Honest edges

- The ~137-command count is from the build record (2026-06-26); individual experts have since been enriched (Connelly 16 wf, Ocean 15 wf), so treat the number as an order of magnitude, not an inventory.
- Cosmetic: the skill-list slug shortener renders `how-i-write-os` as `how-i` — the canonical entry is the `/how-i-write` workflow, which is correct.
- Cross-domain Tier-3 workflows exist per expert (`/connelly-copy-detail`, `/lulu-pr-crisis`, `/wang-annual-letter`, `/browder-founder-warstory`) and are also embedded in copy-engine / writers-room / depth-layer — reachable via `/convene` too, so the conductor is never the only door.

## Composition options (never forced wiring)

| Stacks with | When it earns its cost |
|---|---|
| Voice OS (BLEND layer) | Any output under Farrice's own name — identity floor under the chosen body voice |
| `/deepen` + `/depth-*` (Writing Depth Layer) | Draft exists and needs 1-2 surgical layers, not a rebuild |
| `/stanton-produce`, `/parallax`, `/copy-engine` | The OS supplies craft layers inside these production engines |
| `/two-axis-verify` | Taste-bearing or client-facing pieces after the Layer-7 gates |
