---
name: "Canvas Design — Design Philosophy Creation"
source_prompt: born-v2
skill: canvas-design
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

Step 1 of a two-step visual-art process. The job here is not to design a layout or a template — it is
to write a **manifesto for an art movement**: a VISUAL PHILOSOPHY that a later expression pass will
interpret through form, space, color, composition, images, graphics, shapes, and patterns, with text
used only as a minimal visual accent. Whatever the user asked for is a foundation for this philosophy,
not a constraint on it — creative freedom stays wide open at this stage.

## Input Required

- `[USER REQUEST / SUBJECT]` — the raw ask (poster, art piece, brand mark, other static visual)
- `[ANY EXPLICIT CONSTRAINTS]` — format (.pdf/.png), size, page count, if the user specified any
- `[SUBTLE REFERENCE OR TOPIC]` — optional; the conceptual thread the piece should carry (may be
  deduced later, in the expression pass, rather than supplied here)

## Execution Protocol

1. **Treat the request as foundation, not cage.** Take the subtle input/instructions into account,
   but do not let them constrain the philosophy's creative freedom.
2. **Name the movement** in 1-2 words. Calibrate against the register of: "Brutalist Joy" /
   "Chromatic Silence" / "Metabolist Dreams" — invent a genuinely new name and movement, do not reuse
   these.
3. **Write the philosophy as 4-6 substantial paragraphs**, concise but complete, articulating how the
   movement manifests through all of:
   - Space and form
   - Color and material
   - Scale and rhythm
   - Composition and balance
   - Visual hierarchy
4. **Avoid redundancy.** Each design aspect (color theory, spatial relationships, typographic
   principles, etc.) gets mentioned once unless a later paragraph is adding genuinely new depth to it.
5. **Emphasize craftsmanship repeatedly.** The philosophy must stress, more than once, that the final
   work should read as though it took countless hours, was labored over with care, and comes from
   someone at the absolute top of their field. Use framings like "meticulously crafted," "the product
   of deep expertise," "painstaking attention," "master-level execution" — this repetition is
   essential, not padding to trim.
6. **Leave creative space.** Be specific about the aesthetic direction, but concise enough that the
   next pass (canvas expression) has real room to make interpretive choices at an extremely high
   level of craftsmanship.
7. **Keep the philosophy generic relative to the literal subject.** State the aesthetic language so it
   could, in principle, be reused elsewhere — the philosophy is the worldview; the actual subject
   enters later, in the expression pass, as a subtle embedded reference, not as text in this document.
8. **Calibrate tone and structure** against the shape of: Concrete Poetry (monumental form + bold
   geometry, sculptural typography), Chromatic Language (color as the primary information system),
   Analog Meditation (texture and breathing room, whispered typography), Organic Systems (natural
   clustering, modular growth), Geometric Silence (grid precision, dramatic negative space) — study
   their *shape* (name → one-line philosophy → visual-expression paragraph), not their content.

## Output Contract

A single standalone `.md` file containing exactly:
1. The movement name (1-2 words), as a heading.
2. 4-6 paragraphs covering space/form, color/material, scale/rhythm, composition/balance, and visual
   hierarchy — each addressed once, no repeated ground.
3. Explicit, repeated craftsmanship-emphasis language woven through (not confined to one sentence).
4. No literal restatement of the user's subject — the document reads as reusable aesthetic language.

## Output Skeleton

```
# [MOVEMENT NAME — 1-2 words]

[Paragraph 1 — the philosophy's core statement + how it manifests in space and form]

[Paragraph 2 — color and material language]

[Paragraph 3 — scale and rhythm]

[Paragraph 4 — composition, balance, and visual hierarchy]

[Paragraph 5 (and 6 if needed) — deepen without repeating prior ground; reinforce the
craftsmanship framing at least once more]
```

## Quality Gate

- Does the philosophy name a movement in 1-2 words?
- Is it 4-6 full paragraphs (not a bullet list, not a single paragraph)?
- Does craftsmanship-emphasis language appear more than once across the document?
- Does each of the five design dimensions (space/form, color/material, scale/rhythm,
  composition/balance, visual hierarchy) appear once, without redundant restatement?
- Is the document free of the user's literal subject, reading as generic/reusable aesthetic language?
- Is "text as minimal visual accent, not explanation" established as a governing principle somewhere
  in the document?

## Creative Latitude

The five worked examples in the source material are calibration for *shape*, never a menu to pick
from — invent an actual new movement and name. Draw freely on any design-historical or art-historical
vocabulary that serves the piece (the source material itself reaches for Polish poster art, Josef
Albers, Japanese photobook aesthetics, Swiss formalism, Le Corbusier, Brutalism — as illustrations of
register, not a checklist to cycle through). The poetic quality of the philosophy's language is itself
part of the craft being demonstrated — write it as well as the art it will produce, not as a spec
document wearing poetic vocabulary.

## Deploy When

The user requests a poster, art piece, design object, or "something visual," and no design philosophy
yet exists for this piece. Always runs before canvas expression — the philosophy is the input the
expression pass depends on.
