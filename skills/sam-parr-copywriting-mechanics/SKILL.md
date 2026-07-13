---
name: "Sam Parr Copywriting Mechanics"
description: "Deploy the Sam Parr Copywriting Companion OS for headline gravity, proof-first rescue, curiosity gaps, rhythm, story desire, objections, humor fit, and copywork."
version: "2.0"
format: "companion-os-skill"
workflows: 14
routing: long-tail
---

# Sam Parr Copywriting Mechanics

Use this skill when copy needs direct-response pull from the Sam Parr Copywriting Companion OS: stronger headlines, sharper curiosity gaps, proof-first ads, visual proof, better rhythm, story-led desire, objection handling, humor that fits the brand, or a copywork practice loop.

This skill's 14 workflows are self-contained in `skills/sam-parr-copywriting-mechanics/workflows/`. The companion OS (`_active/sam-parr-copywriting-os/`) was not ported to canonical — port it from the Codex fork if ad-breakdown protocols or copywork training system are needed. It does not replace `sam-parr-taste-acquisition`, `copywriting-agent`, `high-taste-writing-os`, `publishable-copy-gate`, or `proof-copy-engine`.

## Source Evidence

- Video: `https://www.youtube.com/watch?v=uf4fR3qcDkU&t=151s`
- Local source package: `extractions/video-context/uf4fR3qcDkU/`
- Transcript: `extractions/video-context/uf4fR3qcDkU/transcript.txt`
- Companion OS: `_active/sam-parr-copywriting-os/` (NOT YET PORTED — exists in Codex fork only; port separately for deep ad-breakdown protocols and copywork training system)
- Source map: `_active/sam-parr-copywriting-os/01-source-map.md` (not yet ported)
- Operating model: `_active/sam-parr-copywriting-os/02-operating-model.md` (not yet ported)
- Mechanics ledger: `_active/sam-parr-copywriting-os/03-mechanics-ledger.md` (not yet ported; mechanic routing is inlined in the Mechanic Triggers table below)
- Proof lab: `_active/sam-parr-copywriting-os/06-before-after-proof-lab.md` (not yet ported)
- Video extraction package: `extractions/video-context/uf4fR3qcDkU/` (NOT YET PORTED to canonical; exists in Codex fork — port before citing evidence limits from file)
- Evidence limit: transcript-backed spoken evidence only; visual/OCR evidence is unavailable.

## Core Method

1. Start from the desired reader action.
2. Diagnose the weak link: attention, interest, desire, proof, objection, rhythm, story, humor, or action.
3. Select one to three Sam mechanics.
4. Rewrite only the affected copy section.
5. Show the before/after behavior delta.
6. Name the proof object or proof gap.
7. Send public, client-facing, or revenue copy through `/publishable-copy-gate`.

## Canonical Workflows

| Workflow | Produces | Use When |
|---|---|---|
| [AIDA Reader-State Map](workflows/aida-reader-state-map.md) | Reader-state diagnosis and sequence repair | Copy has pieces but no movement |
| [Headline Gravity Lab](workflows/headline-gravity-lab.md) | Headline candidates, payoff line, and behavior delta | The opener is a label or weak claim |
| [Curiosity Gap Repair](workflows/curiosity-gap-repair.md) | Trustworthy open loop and payoff | Copy has information but no pull |
| [Proof Object Builder](workflows/proof-object-builder.md) | Claim map and proof-first rewrite | Claims are generic or unsupported |
| [Visual Proof Translation](workflows/visual-proof-translation.md) | Concrete comparison or visible proof line | A true fact feels abstract |
| [Rhythm And Slippery-Slope Pass](workflows/rhythm-slippery-slope-pass.md) | Line-level momentum rewrite | Copy is correct but flat |
| [Story Desire Pass](workflows/story-desire-pass.md) | Desire-building story or contrast before product | Offer appears before reader cares |
| [Objection By Detail Pass](workflows/objection-by-detail-pass.md) | Natural objection handling through detail | Reader doubt is predictable |
| [Humor Fit Check](workflows/humor-fit-check.md) | Keep, rewrite, or remove humor | Personality could help or hurt trust |
| [Copywork Rule Extraction](workflows/copywork-rule-extraction.md) | Copywork rules and applied rewrite | Writer needs better instincts |
| [Weak Ad Rescue](workflows/weak-ad-rescue.md) | Full before/after rescue with proof and behavior delta | The asset is generic, flat, unsupported, or benefit-first |

## Compatibility Workflows

These first-build workflows remain available, but the command should prefer the canonical workflows above:

| Workflow | Current Role |
|---|---|
| [Headline Proof Rewrite](workflows/headline-proof-rewrite.md) | Compatibility path for headline plus proof fixes |
| [Copywork Hour Sprint](workflows/copywork-hour-sprint.md) | Compatibility path for one-hour practice |
| [Story Desire Objection Pass](workflows/story-desire-objection-pass.md) | Compatibility path for story plus objection fixes |

## Mechanic Triggers

| Trigger | Load |
|---|---|
| Weak headline or hook | Headline gravity, curiosity gap, known phrase, new turn |
| Good point but boring | Curiosity gap, slippery slope, rhythm |
| Generic product claim | Proof-first ad, proof object builder, visual proof translation |
| Reader doubt | Objection by detail |
| Stiff or formal voice | Familiar energy, simple language |
| Product appears too early | Story-led desire, price desire sequence |
| Needs creative practice | Copywork, copy-hour, rule extraction |
| Brand can be funny | Humor fit check |

## Required Output Shape

Do not count this skill as used unless the output includes:

- original weak section,
- desired reader action,
- weak-link diagnosis,
- source mechanics used,
- evidence anchors when useful,
- proof object or proof gap,
- rewritten section,
- before/after delta,
- reader-behavior explanation,
- next gate,
- remaining risk.

## Stacking

| Stack With | How |
|---|---|
| `/copywriting-agent` | Use Sam mechanics as a direct-response scalpel inside the owner-led copy path. |
| `/high-taste-writing-os` | Use for reader pull, rhythm, and interest before composition polish. |
| `/publishable-copy-gate` | Use Sam evidence as input, then score punch, proof, voice, CTA, and anti-slop normally. |
| `/farrice-content-os` | Use in Hook Room and conversion posts when a draft lacks proof, curiosity, or rhythm. |
| `sam-parr-taste-acquisition` | Pair only when copy improvement requires broader taste acquisition or copywork training. |
| `tom-segura-comedy-storytelling` | Use before Humor Fit Check when the draft needs observational charge, a story way-in, or written-comedy timing. |

## Guardrails

- Do not claim exact visual context from the video unless a future full-frame/OCR package exists.
- Do not turn every copy task into a Sam Parr task.
- Do not overwrite the intended brand voice with Sam's style.
- Do not use humor where the brand cannot credibly carry it.
- Do not invent proof to satisfy the proof-first rule.
- Do not finish a source-to-copywriting extraction without behavior-changing proof.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

11 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Sam Parr — AIDA Reader-State Map** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/aida-reader-state-map.md`
- **Sam Parr — Copywork Rule Extraction** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/copywork-rule-extraction.md`
- **Sam Parr — Curiosity Gap Repair** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/curiosity-gap-repair.md`
- **Sam Parr — Headline Gravity Lab** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/headline-gravity-lab.md`
- **Sam Parr — Humor Fit Check** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/humor-fit-check.md`
- **Sam Parr — Objection By Detail Pass** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/objection-by-detail-pass.md`
- **Sam Parr — Proof Object Builder** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/proof-object-builder.md`
- **Sam Parr — Rhythm And Slippery-Slope Pass** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/rhythm-slippery-slope-pass.md`
- **Sam Parr — Story Desire Pass** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/story-desire-pass.md`
- **Sam Parr — Visual Proof Translation** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/visual-proof-translation.md`
- **Sam Parr — Weak Ad Rescue** — `skills/sam-parr-copywriting-mechanics/references/prompts-v2/weak-ad-rescue.md`

<!-- END:execution-prompts -->
