---
name: "Dave Clark: Cinematic AI Direction"
description: "The taste layer above tool craft — why AI video reads flat vs cinematic, hybrid pipeline architecture, and shot-list-before-prompt direction discipline from the CCO of Promise"
version: "1.0"
format: "completion-engine"
workflows: 3
---

# Dave Clark: Cinematic AI Direction

> Co-Founder & Chief Creative Officer, Promise. Two decades directing film and commercials
> (Coca-Cola, Snapchat, HP, Warner Bros., Intel) before generative tools existed. *Borrowing Time*,
> *Dismal Swamp*, *Battalion*, *Another* (Cannes Next 2024), *NinjaPunk*, *My Friend Zeph*, *Hardcore 94*.
>
> **What he adds that nobody else in the house does:** the judgment layer *above* prompt craft. Everyone else
> teaches syntax. Clark is the one who can name — mechanically, in a DP's vocabulary — why the image you just
> generated is dead, and the one shipping AI work through platform QC and studio chain-of-title.

## The one-line thesis

> *"To me, the future of AI is just filmmaking… the goal is for AI to become an afterthought."*
> — Marché du Film, 2025-06-24

If the AI is the interesting part, the film has failed.

## The core claim

**Flatness is almost never a prompting failure. It is a directing failure wearing a prompting costume.**

Six of the eight causes of flat AI video are decided *before* generation or *after* it — in selection, coverage,
cadence, lighting specification, capture layer, and whether anything is at stake. Only two are prompt problems,
and none of the eight is a model-choice problem. Swapping generators moves two of them slightly and the other
six not at all. That is why prompt-craft skills plateau at "impressive clip" and never reach "watchable film."

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---|---|---|
| 01 | [Flat-to-Cinematic Audit](workflows/01-flat-to-cinematic-audit.md) | Shot-level diagnosis: why it reads flat, the fix per defect, and what's not worth fixing | Something "looks AI", a client says "make it more cinematic", or a reel is technically clean and dead |
| 02 | [Hybrid Pipeline Plan](workflows/02-hybrid-pipeline-plan.md) | Layer map + persistence register + delivery spec + provenance plan + risk register | The piece is longer than a clip, mixes live action with generated material, or has to clear QC |
| 03 | [Shot List → Generation Brief](workflows/03-shot-list-to-generation-brief.md) | Directed shot list as camera reports, with look card, cadence plan and generation protocol | Starting anything longer than one image, or previous attempts came out as a slideshow |

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load before any workflow. Carries the flat-vs-cinematic axis,
  18 patterns, 11 signature moves, the quality rubric, and the observed visual signature.
- **Source notes & fidelity ledger**: [references/source-notes.md](references/source-notes.md) — every source dated,
  every unverified claim flagged.

## Doctrine: model-independence

**Everything in the core method is model-independent.** It survives Runway → Veo → Sora → whatever ships next
quarter, because none of it is about a model. It is about direction, selection, coverage, cadence, light,
colour space and provenance.

**Tool-specific mechanics are quarantined in `genius.md` Appendix A — "Era-Bound Mechanics (2023–24), verify
before use."** No workflow and no execution prompt in this skill depends on a single line of that appendix.
If swapping the generator invalidates an output, the output was wrong.

## The eight causes of flat, in likelihood order

1. **One generation deep** — a selection problem, not a prompting one
2. **Metronome cutting** — uniform clip length is the loudest AI tell there is
3. **Unmotivated light** — you can't point at where it's coming from; shadows lifted grey
4. **Clean air** — nothing physically between camera and subject, so the planes collapse
5. **No capture layer** — digitally immaculate, therefore never photographed
6. **No coverage** — every shot a new setup, so nothing reads as a scene
7. **Adjective prompting** — "cinematic, moody, epic" is a wish, not a direction
8. **Nothing at stake** — you can't say what it's about in a sentence

Escalations for real delivery: **drift** · **edit survivability (colour space, bit depth)** · **provenance**.

## Signature moves (short list)

Rule of Five · Composite the take (don't pick it) · Mask the fidelity back in · Retime rather than accept the
clip length · The coverage pair · The global capture layer · Phenomenon over category · Extend, don't crop ·
Externalise what must persist · Spec the delivery before you generate · Direct the performance, synthesise
the colour.

## Routing

- **Diagnosing bad AI video / "make it more cinematic"** → workflow 01
- **Longer-form, hybrid, or QC-bound work** → workflow 02
- **Anything before generation starts** → workflow 03
- **Prompt syntax and style codes** → NOT this skill. `skills/cinema-worldbuilder-pro/`, `/art-direct`,
  `/creative-prompt`. Clark is deliberately upstream of prompt syntax.
- **Ad-shaped AI video** → `skills/pj-accetturo-ai-video/` (PJ optimises for the platform; Clark optimises for
  the release print — when they disagree, the deliverable decides)

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Dave Clark — Flat-to-Cinematic Audit** — `skills/dave-clark/references/prompts-v2/flat-to-cinematic-audit.md`
- **Dave Clark — Hybrid Pipeline Plan** — `skills/dave-clark/references/prompts-v2/hybrid-pipeline-plan.md`
- **Dave Clark — Shot List & Generation Brief** — `skills/dave-clark/references/prompts-v2/shot-list-generation-brief.md`

<!-- END:execution-prompts -->
## Fidelity note

Three prompts, not twelve. One per deliverable the corpus can honestly carry. Clark never published a
flat-vs-cinematic framework, never gives a lighting ratio, f-stop, colour temperature or grading value, and
never publishes a lens table — so none appear here. The eight-cause diagnostic is **Clark-derived**, assembled
by this extraction from his stated practice plus the observed signature of his 2025 director reel, with
per-check source tags. Full ledger: [references/source-notes.md](references/source-notes.md).
