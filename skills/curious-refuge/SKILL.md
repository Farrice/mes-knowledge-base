---
name: "Curious Refuge (Caleb Ward): AI Film Pre-Production"
description: "The pre-production layer of AI filmmaking — reference-asset architecture, the shot-list floor, board-to-plate channel assignment, prompted coverage, voice casting and the ADR seam where AI hands off to a human"
version: "1.0"
format: "completion-engine"
workflows: 3
---

# Curious Refuge (Caleb Ward): AI Film Pre-Production

> Caleb Ward — co-founder (with Shelby Ward) and CEO of **Curious Refuge**, an AI filmmaking school
> and a **Promise company** (the same Promise where Dave Clark is CCO). Courses: AI Filmmaking,
> AI Advertising, Advanced AI Filmmaking 2.0, AI Animation 2.0, AI Documentary, AI VFX, AI Screenwriting.
> Extracted from four videos, all 2026, all watched in full. Credential ledger with verification
> status: [references/source-notes.md](references/source-notes.md).
>
> **What he adds that nobody else in the house does:** the **files that have to exist before you
> generate.** Everyone else teaches the prompt or the look. Ward teaches the reference-asset
> architecture — character sheets, location angle banks, style anchors, voice beds — and the order of
> operations that makes shot 7 belong in the same film as shot 1.

## The one-line thesis

> *"If you just rely to going to the AI video tools alone, you're going to see that there's just some
> severe lapses in continuity."* — [FILM26] 08:22

**Continuity is a planning artifact, not a model capability.** When a shot comes back wrong, you change
the reference assignment — not the adjectives.

## The core claim

A pre-production package is not a mood board. It is a set of **reusable identity assets** built once at
high quality and referenced into every generation, plus a shot list saying which asset goes where.
Reference assets get maximum quality because their cost amortises across the whole film; shot plates get
only what the next step consumes. Generation is the last step and the cheapest to redo.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---|---|---|
| 01 | [Pre-Production Package](workflows/01-preproduction-package.md) | Story spine + tension shape + shot list + **reference-asset manifest** + generation budget | Starting any narrative AI piece longer than a clip, or you have to quote a cost before you start |
| 02 | [Storyboard → Plate → Coverage Chain](workflows/02-storyboard-to-plate.md) | Shot conversion sheet: board-or-brief call, three-channel reference assignment, CCR direction, specify-vs-cover, chain plan, accept/salvage criteria | The shot list exists and it's time to generate — or generations keep coming back "wrong" and nobody can say which part |
| 03 | [Voice & Performance Direction](workflows/03-voice-and-performance-direction.md) | Voice-bed casting, per-line director's notes, consistency rung per character, stem handoff, **the ADR seam** | Anyone speaks; the same character sounds like a different person shot to shot; deciding whether to hire voice actors |

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load before any workflow. 28 patterns, 10 signature
  moves, a 15-row quality rubric assembled entirely from his own dated on-camera verdicts, and the voice
  profile.
- **Source notes & fidelity ledger**: [references/source-notes.md](references/source-notes.md) — every
  source dated, every self-reported credential flagged, and an explicit list of what this corpus does
  **not** carry.

## Doctrine: tool-independence

**The core method names files, channels, rungs and seams — never products.** It survives the next model
release because none of it is about a model. Every tool name, model version, price, resolution and button
path from the four 2026 sources is quarantined in
**[references/era-bound-mechanics.md](references/era-bound-mechanics.md) — "verify before use."** No
workflow and no execution prompt depends on a line of it. That appendix is unusually large here precisely
because the corpus is unusually current: this material will rot fast at the tool layer and not at all at
the discipline layer.

## The load-bearing decisions

1. **The shot list is the floor; the storyboard is optional.** *"You need to at the very least have a
   shot list, if not a storyboard."* [FILM26] 08:13
2. **The composition question** — board the shot when composition is load-bearing, brief it when only the
   *idea* of the shot matters: *"it was the idea of the shot and not the individual composition being
   exactly right."* [ANIME26] 15:47
3. **Rough on purpose** — the sketch protects your own decision-space: *"your brain doesn't get so locked
   in on some of the supporting details."* [FILM26] 09:04
4. **Three channels, three references** — *"use the composition from image number one… and keep the
   character as at character number one."* [FILM26] 11:40. Unassigned channel = unauthorised drift.
5. **One identity per character sheet** — two characters on one sheet *"would be very confusing."*
   [ANIME26] 07:16
6. **Locations get two angles, built before you need them.** [ANIME26] 08:40
7. **Never judge a prompt on one output** — *"the actual problem is just you didn't generate enough
   images."* [FILM26] 07:44
8. **Salvage before you reject** — half a second counts. [ANIME26] 13:03 · [FILM26] 15:44
9. **Easiest shot first** — it becomes the reference anchor. [ANIME26] 09:21
10. **Voice last, ADR inverted** — the AI authors the timing, the human matches it. [ANIME26] 09:02
11. **Budget in generations** — iterations × unit cost × runtime. *"This is not a free creative medium."*
    [ANIME26] 12:14
12. **IP hygiene at the moodboard**, where it's free. [FILM26] 03:06

## Signature moves (short list)

Four-panel dynamic character sheet · channel-assignment prompt · location angle bank · CCR ordering
(camera, character, rig) · the 15-second voice bed cast with emotional range · the rolling reference cut ·
the parallel model bake-off · board above / plates below · easiest shot first · the salvage pass.

## Routing

- **Anything before generation starts on a narrative piece** → workflow 01
- **Turning a shot list into generations; diagnosing "which part is wrong"** → workflow 02
- **Dialogue, VO, voice drift, hiring voice actors** → workflow 03
- **Judging a batch that already came back** → `references/prompts-v2/continuity-audit.md`
- **Why the finished piece reads flat; look cards, cadence, grade, provenance, release QC** → NOT this
  skill. `skills/dave-clark/` — same building, the layer above. When they disagree: **Clark owns the look
  and the cut; Ward owns the asset architecture and the order of operations.** Clark says *board the shot*;
  Ward says *board it only when composition is load-bearing* — settle it per shot with the composition
  question.
- **Ad-shaped / platform-optimised AI video** → `skills/pj-accetturo-ai-video/`
- **Still-image art direction, style handles, prompt syntax** → `skills/nick-st-pierre/`,
  `skills/rory-flynn/`, `/art-direct`. Ward consumes their output as his style anchor and character sheet;
  he does not teach that layer.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Curious Refuge (Caleb Ward) — Continuity & Consistency Audit** — `skills/curious-refuge/references/prompts-v2/continuity-audit.md`
- **Curious Refuge (Caleb Ward) — Pre-Production Package** — `skills/curious-refuge/references/prompts-v2/preproduction-package.md`
- **Curious Refuge (Caleb Ward) — Shot Conversion Sheet** — `skills/curious-refuge/references/prompts-v2/shot-conversion-sheet.md`
- **Curious Refuge (Caleb Ward) — Voice & Performance Direction Plan** — `skills/curious-refuge/references/prompts-v2/voice-performance-plan.md`

<!-- END:execution-prompts -->
## Fidelity note

**Three workflows and four prompts, not eight.** The master-hunt brief proposed a pitch-trailer workflow;
**no 2025–26 source in this corpus teaches pitch-trailer structure**, and the one trailer-build video on
the channel predates the multi-shot-coverage shift that [ANIME26] documents — so building it would have
imported era-bound mechanics into the core. It was dropped and replaced by voice & performance direction,
which is the densest verified material in the corpus. *"Hybrid AI + live pipelines"* is built only to the
extent the corpus carries it: the ADR seam and the finishing handoff, not live-action plate photography.
Ward's press credentials (100M+ views, NYT/Forbes/Hollywood Reporter/CNBC/USA Today, Netflix/Adobe/Sony
collaborations) are **self-reported on his own site and not independently confirmed** — they appear in no
prompt's Role & Activation. Full ledger: [references/source-notes.md](references/source-notes.md).
