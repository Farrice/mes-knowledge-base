---
name: fashion-coupids
description: "The FASHION CAMPAIGN CHAIN — the stage order, stage deliverables and finishing doctrine for AI-directed fashion, apparel and accessory campaigns. Fashion Coupids (Jen): intent (purpose/audience/emotion/constraints) → culture read → brand read → one-sentence metaphor concept → loose moodboard+storyboard → art direction, styling, shot list, camera and the real-life visualization check → generate/composite/unify/place. Carries the four-move production spine (RESEARCH → GENERATE → COMPOSITE → UNIFY), the hero-object fidelity pass (the product always renders wrong — budget a compositing pass, never a better prompt), the fixed retouch order product→subject→background, the one series-level grade matched to the brand palette, fixed iteration axes (lighting·environment·pose·styling), and Keep/Kill/Push selection. Use when a brand, drop, collection or product needs a coherent campaign SET rather than one good image; when generated frames look fine individually but don't read as one body of work; when a brief arrives as a mood and needs to become a concept; or before any generation spend on a lookbook or campaign. Trigger phrases: fashion campaign, lookbook, drop campaign, campaign direction, shot list, editorial concept, moodboard to campaign, brand campaign images, campaign finish, unify the series, why don't these look like one campaign. STRUCTURE skill — frame-level craft is handed off to nick-st-pierre, rory-flynn and dave-clark by design."
version: "1.0"
format: "completion-engine"
workflows: 2
---

# Fashion Coupids (Jen) — The Fashion Campaign Chain

> Creative project led by **Jen**. Domestika Teacher Plus since November 2025; eight published
> courses on AI-directed fashion design, editorials, magazine covers, creative direction and brand
> aesthetics. Instagram `@fashion.coupids`, 58K followers — *"Editorial prompt designer and creative
> direction."* Self-described AI content creator making *"realistic, luxury, and highly creative
> visual content for brands."*

## Read this before you use it

**This is a STRUCTURE extraction. Fidelity: MEDIUM on the chain, LOW on craft. Stated plainly.**

Her teaching is paywalled and, under the cost gate, **was not purchased**. What could be extracted
from the public record — full curricula for all eight courses, two complete campaign case-study
write-ups, learning outcomes, final-project specs — is the **chain**: what happens in what order and
what exists at the end of each stage. What could *not* be extracted is the craft inside each stage:
her actual prompt phrasing, her compositing hand, her critique.

So the skill does one thing and refuses the rest. **It carries the spine. It hands off the frame.**
Full boundary and fidelity ledger: [`references/source-notes.md`](references/source-notes.md).

**The craft backfill is not optional — it is part of the design:**

| Need | Load |
|---|---|
| Frame construction, layered build, controlled sweeps, reference-over-adjective, the ten-check critique | [`skills/nick-st-pierre/`](../nick-st-pierre/SKILL.md) |
| Moodboard operations at volume, style-handle characterisation, frozen-backbone/variable-head brand consistency | [`skills/rory-flynn/`](../rory-flynn/SKILL.md) |
| Light named and placed, black point, why a frame reads flat, capture register | [`skills/dave-clark/`](../dave-clark/SKILL.md) |
| Brand positioning strategy | `oren-brand-archetypes`, `grace-liu` |
| **The output benchmark — what "good" actually looks like in this lane** | **`https://maisonmeta.io/work`** (Norma Kamali, YSL Montaigne, Tabi lookbook, Bottega Jodie object training, Zalando Zeitgeist, D&G Casa). Grade My.BPM and every client campaign against that shelf. This skill is the process floor, not the ceiling. |

## The gap this closes

The house owns image direction, image operations and cinematic direction — all of which answer *how
do I make this frame good*. None of them answers:

> **A brand wants a campaign. What are the stages, in what order, and what exists at the end of each?**

That is the whole contribution. Judge this skill on whether the campaign arrives **complete and
consistent**, not on whether any single frame is beautiful.

## The one-line thesis

> AI is a **co-creative director**, not a shortcut. Human judgment is the final authority.
> — her course line's own framing (lesson title, 6452: *"Developing Taste and Human Judgment as the
> Final Authority"*)

## The core claim

**Generation is one move of four.**

```
RESEARCH  →  GENERATE  →  COMPOSITE  →  UNIFY
```

This spine appears identically, in the same order with the same stage vocabulary, in two
independently published campaign write-ups. Two of the four moves happen *after* generation, and
they are the two that decide whether a client signs off. Any workflow in which generating **is** the
work has already failed her standard.

## The chain (tool-transcendent — no model named anywhere in it)

```
1 INTENT      purpose · audience · emotion · constraints
2 CULTURE     what moment does this stand in — and what is it deliberately not doing
3 BRAND       2–3 non-negotiable signatures, palette, materials, register
4 CONCEPT     ONE sentence, ONE metaphor, plus a claim about the buyer     ← the hinge
5 BOARD       moodboard + LOOSE storyboard — lock tone·colour·material·theme, leave composition open
6 DIRECTION   art direction & styling → shot list → camera → real-life visualisation check
7 EXECUTION   generate (fixed axes) → Keep/Kill/Push → composite (hero fidelity) → unify → place
```

Order is load-bearing. Concept before board; board before shot list; shot list before generation;
unify after everything.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---|---|---|
| 01 | [Fashion Campaign Chain](workflows/01-fashion-campaign-chain.md) | Campaign Direction Document — all seven stages, concept through channel placement | A brand, drop, collection or product needs a campaign; a brief arrived as a mood; prior attempts produced six nice images that don't cohere |
| 02 | [Lookbook Shot List](workflows/02-lookbook-shot-list.md) | Directed shot list — set-level constants, one camera card per frame, real-life audit, coverage and cut-down | The concept and board exist and the frame-by-frame plan is next; or anyone says "just generate a few looks" |

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load before either workflow. 18 patterns, 9 signature
  moves, the quality rubric, and every claim marked **[STATED] / [STRUCTURAL] / [INFERRED]**.
- **Source notes & fidelity ledger**: [references/source-notes.md](references/source-notes.md) — the
  paywall boundary, the eight-course corpus, the receipts posture.

## The five moves worth stealing even if you never run a workflow

1. **The one-sentence metaphor concept.** *"A woman running through the city, a metaphor for the
   fast-paced rhythm of modern life."* A mood cannot survive being handed to four people; a sentence
   with a figure in it can. If it takes two sentences, it is two campaigns.
2. **The hero-object fidelity pass.** The model will not render your client's product correctly. Plan
   for it. Budget a compositing pass for texture, hardware and colour accuracy — and never reject a
   good generation because the clasp is wrong. That was always a post job.
3. **The series grade.** One grade, decided at set level, applied once across everything, matched to
   the **brand's** palette — not to what flatters each frame. This is the difference between a
   campaign and a folder.
4. **Fixed iteration axes.** Declare them before generating: **lighting · environment · pose ·
   styling**. Move one at a time. Change four things between attempts and you learn nothing.
5. **The real-life visualisation check.** Could a crew shoot this — location, hour, lens, a body that
   fits the space, fabric that behaves? Most of what people call "looks AI" is a physics failure, not
   an aesthetic one.

## Doctrine: tool-independence

Everything above is model-independent. Her stack as publicly taught — Midjourney, ChatGPT, Higgsfield
/ Nano Banana Pro, Replicate, Canva, Pinterest, Photoshop, Lightroom — is **quarantined in
`genius.md` Appendix A, dated 2025-11/2026-08, "verify before use."** No workflow and no execution
prompt in this skill depends on a line of it. If swapping a tool invalidates an output, the output
was wrong.

## Receipts posture (binding)

Two campaign case studies are cited throughout as **process specimens**: Versace / Greca Goddess Bag
and Onalaja / Zaza Bag. Both are **self-reported on her own Domestika project posts** and were found
**nowhere else** — no brand-side credit, no press, no agency listing. Status: **LIKELY the work
exists as shown; UNCONFIRMED that either brand commissioned it.**

Therefore: these names appear in `genius.md` and `references/source-notes.md` as evidence of *her
process*, and **never** in a prompt's Role & Activation block, never in a client-facing artifact,
never as a credential.

<!-- BEGIN:execution-prompts -->
## Execution Prompts

| Prompt | Deliverable |
|---|---|
| [`references/prompts-v2/campaign-direction-document.md`](references/prompts-v2/campaign-direction-document.md) | Campaign Direction Document — the full seven-stage chain |
| [`references/prompts-v2/lookbook-shot-list.md`](references/prompts-v2/lookbook-shot-list.md) | Directed shot list with real-life audit, coverage and cut-down |
| [`references/prompts-v2/campaign-finish-plan.md`](references/prompts-v2/campaign-finish-plan.md) | Campaign Finish Plan — selection, hero-object fidelity, retouch order, series grade, placement |
<!-- END:execution-prompts -->

## Quality gate for anything this skill produces

1. Can you say the concept in **one sentence**, with a metaphor in it?
2. Cover the captions — does the set read as **one** campaign? One light logic, one palette, one
   person, one world.
3. Is the **product accurate**? This is the line that fails brand review, and taste does not override it.
4. **Could this have been shot?** Location, hour, lens.
5. Is anything in it **specifically the brand's** — can you point at a researched signature in frame?
6. **Did you kill anything?** A set with no kills was never evaluated.
7. Is it **placed** — crop, type, format, channel?
8. Did a human make the final call, and can you say what the call was?

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **[BRAND] × [PRODUCT] — Campaign Direction** — `skills/fashion-coupids/references/prompts-v2/campaign-direction-document.md`
- **[CAMPAIGN] — Finish Plan** — `skills/fashion-coupids/references/prompts-v2/campaign-finish-plan.md`
- **Fashion Coupids — Lookbook Shot List** — `skills/fashion-coupids/references/prompts-v2/lookbook-shot-list.md`

<!-- END:execution-prompts -->
## Quality gate for anything this skill produces

1. Can you say the concept in **one sentence**, with a metaphor in it?
2. Cover the captions — does the set read as **one** campaign? One light logic, one palette, one
   person, one world.
3. Is the **product accurate**? This is the line that fails brand review, and taste does not override it.
4. **Could this have been shot?** Location, hour, lens.
5. Is anything in it **specifically the brand's** — can you point at a researched signature in frame?
6. **Did you kill anything?** A set with no kills was never evaluated.
7. Is it **placed** — crop, type, format, channel?
8. Did a human make the final call, and can you say what the call was?

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **[BRAND] × [PRODUCT] — Campaign Direction** — `skills/fashion-coupids/references/prompts-v2/campaign-direction-document.md`
- **[CAMPAIGN] — Finish Plan** — `skills/fashion-coupids/references/prompts-v2/campaign-finish-plan.md`
- **Fashion Coupids — Lookbook Shot List** — `skills/fashion-coupids/references/prompts-v2/lookbook-shot-list.md`

<!-- END:execution-prompts -->
## Quality gate for anything this skill produces

1. Can you say the concept in **one sentence**, with a metaphor in it?
2. Cover the captions — does the set read as **one** campaign? One light logic, one palette, one
   person, one world.
3. Is the **product accurate**? This is the line that fails brand review, and taste does not override it.
4. **Could this have been shot?** Location, hour, lens.
5. Is anything in it **specifically the brand's** — can you point at a researched signature in frame?
6. **Did you kill anything?** A set with no kills was never evaluated.
7. Is it **placed** — crop, type, format, channel?
8. Did a human make the final call, and can you say what the call was?

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **[BRAND] × [PRODUCT] — Campaign Direction** — `skills/fashion-coupids/references/prompts-v2/campaign-direction-document.md`
- **[CAMPAIGN] — Finish Plan** — `skills/fashion-coupids/references/prompts-v2/campaign-finish-plan.md`
- **Fashion Coupids — Lookbook Shot List** — `skills/fashion-coupids/references/prompts-v2/lookbook-shot-list.md`

<!-- END:execution-prompts -->
