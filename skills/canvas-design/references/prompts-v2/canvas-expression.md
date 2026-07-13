---
name: "Canvas Design — Canvas Expression (Single-Page Visual Artifact)"
source_prompt: born-v2
skill: canvas-design
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

Step 2 of the process. A completed design philosophy now exists; the job is to EXPRESS IT VISUALLY —
producing an artifact that is 90% visual design, 10% essential text. Museum- or magazine-quality bar.
Even when the underlying subject is a movie, game, or book, the execution stays sophisticated — never
cartoony, never amateur.

## Input Required

- `[DESIGN PHILOSOPHY .MD]` — the completed philosophy from the prior pass
- `[ORIGINAL USER REQUEST / SUBJECT]` — what the piece is ultimately about
- `[OUTPUT FORMAT]` — .pdf or .png
- `[CANVAS DIMENSIONS / SIZE]` — if the user specified any; otherwise designer's call
- `[FONT SOURCE]` — `./canvas-fonts` directory

## Execution Protocol

1. **Deduce the subtle reference — before touching the canvas.** Identify the subtle, niche
   conceptual thread from the original request. The topic is embedded within the art itself, not
   stated — not always literal, always sophisticated. Someone familiar with the subject should feel
   it intuitively; everyone else should simply experience a masterful abstract composition. The
   philosophy supplies the aesthetic language; the deduced topic supplies the soul — the quiet
   conceptual DNA woven invisibly into form, color, and composition. Think like a jazz musician
   quoting another song: only those who know will catch it, but everyone appreciates the music. The
   reference must be refined enough that it deepens the work without announcing itself.
2. **Gather thoughts, then build.** Use the philosophy and the deduced reference together to craft
   the piece with expert craftsmanship — one single page, highly visual, design-forward, unless more
   pages were requested.
3. **Treat the piece as if it were a scientific bible.** Borrow the visual language of systematic
   observation — dense accumulation of marks, repeated elements, or layered patterns that build
   meaning through patient repetition and reward sustained viewing. Use repeating patterns and perfect
   shapes.
4. **Typography as system, not caption.** Sparse, clinical typography and systematic reference
   markers, as though this were a diagram from an imaginary discipline — treat the invisible subject
   with the same reverence normally reserved for documenting observable phenomena.
5. **Anchor, don't explain.** Anchor the piece with simple phrase(s) or details positioned subtly,
   using a limited color palette that feels intentional and cohesive.
6. **Hold the paradox.** The piece uses analytical visual language to express ideas about human
   experience — the result should feel like an artifact proving something ephemeral can be studied,
   mapped, and understood through careful attention.
7. **Text calibrates to context, but stays minimal-first.** Let the subject guide whether text reads
   whisper-quiet or as a bolder typographic gesture (a punk venue poster earns louder type than a
   minimalist ceramics-studio identity) — but default to thin fonts, and every use of type must be
   design-forward, prioritizing visual communication over legislation-by-caption.
8. **Boundary rule — non-negotiable.** Nothing falls off the page. Nothing overlaps. Every element
   sits inside canvas boundaries with proper margins. Check that all text, graphics, and visual
   elements have breathing room and clear separation. This is not optional polish; it is a hard
   requirement of professional execution.
9. **Fonts come from the corpus, and become part of the art.** Search `./canvas-fonts`; download and
   use whatever fonts the piece needs. If the art is abstract, bring the font onto the canvas as a
   visual object rather than leaving it as flat digital typesetting.
10. **Push the frontier.** Follow design instinct and intuition, using the philosophy as a guiding
    principle rather than a fence. Embrace full design freedom and choice.
11. **Hold the craftsmanship bar.** The work must look like it took countless hours, as though someone
    at the absolute top of their field labored over every detail with painstaking care. Composition,
    spacing, color choices, and typography must all read as expert-level. Double-check that nothing
    overlaps, formatting is flawless, every detail perfect — the piece should be impressive enough to
    stand as proof of expertise.

## Output Contract

One downloadable `.pdf` or `.png` (single page unless a multi-page deliverable was separately
requested), delivered alongside the design-philosophy `.md` that grounded it. Visual-to-text ratio
approximately 90/10. Must contain: (a) the deduced conceptual reference embedded invisibly in form,
never spelled out in text; (b) a systematic, diagram-like or pattern-repetition visual structure;
(c) sparse typography sourced from `./canvas-fonts`; (d) full compliance with the boundary rule — no
overlaps, no clipping, real margins.

## Output Skeleton

```
[CANVAS FILE: <name>.pdf or .png]
Composition: [dominant visual structure — repeating pattern / diagram system / layered field]
Palette: [N colors, named or hex, intentional and limited]
Typography: [font(s) pulled from ./canvas-fonts + the role each plays — label / anchor phrase /
             system marker — and whether type becomes a visual object or stays typeset]
Subtle reference embedding: [where and how the deduced topic lives in form/color/composition —
                             never in literal text]
Anchor text (if any): [the sparse phrase(s) placed, and why they earn a place on the canvas]
Bounds check: [confirmed — nothing overlaps, nothing clipped, margins held]
```

This skeleton is a production spec the model verifies against before and after rendering — the actual
deliverable is the binary `.pdf`/`.png` file itself, not this text.

## Quality Gate

- Was a subtle conceptual reference deduced *before* canvas creation began, rather than skipped or
  bolted on afterward?
- Does the piece read as ~90% visual / 10% text — never a decorated document or a poster with a
  paragraph on it?
- Is every text and graphic element fully inside canvas bounds with real margins, with zero overlaps?
- Are the fonts sourced from `./canvas-fonts` and used as part of the visual art, not left as default
  typesetting?
- Does the composition use repeating, systematic, or diagram-like structure rather than a one-off
  illustration?
- Would this pass as museum/magazine quality — not cartoony, not amateur, not template-shaped?

## Creative Latitude

The subtle-reference deduction and the "scientific bible" / systematic-observation visual language are
the two highest-leverage creative levers here — invent the actual reference mechanism and the specific
pseudo-discipline the piece pretends to document. Draw on real design vocabulary freely (the source
material names Polish poster art, Josef Albers, Japanese photobook aesthetics, Swiss formalism, Le
Corbusier, Brutalism, Metabolism as registers to draw from, not a checklist to complete). Typography
choice, and exactly how it becomes "part of the art itself," is a taste call each time — push past the
skeleton's checklist shape into one singular, un-repeatable artifact.

## Deploy When

A completed design philosophy `.md` exists and the user needs it expressed as an actual visual
artifact (.pdf/.png), single page by default.
