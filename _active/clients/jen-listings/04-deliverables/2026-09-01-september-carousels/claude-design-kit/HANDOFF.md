# Valley Native in Claude Design — the handoff

This kit is everything Claude Design needs to explore Jen's system: the spec, the rules, the final copy, the cleared photos, and the finished slides as references. Read this page, then use `PROMPTS.md`.

## What's already inside Claude Design

A design-system project named **Jen Santulan · Valley Native** was synced from this repo. It holds the component cards (masthead and stamp, the four Valley buildings, the map glyphs, the print, bars and panels), the 21 finished slides as templates, the ten presentation boards, the photo bank, DESIGN.md and the rulebook. When Claude Design asks which design system to use, pick that one. Everything it generates then starts on-system.

## The five-minute setup (once)

1. Go to claude.ai/design and sign in with the same account that runs Claude Code.
2. Open the project **Jen Santulan · Valley Native**. If you don't see it, it's in the projects list; the type is "design system."
3. Start a new design in that project. When it asks for context, attach from this kit: `DESIGN.md`, `RULEBOOK.md`, `COPY-DECK.md`, and the `photos` folder (or the specific photos you want used).
4. Paste one prompt from `PROMPTS.md`. Each prompt asks for genuinely different directions, not shades of one idea, and names the axis it explores so you can judge fast.
5. Pick a direction. Ask for the full seven slides in it. Export PNG or PDF from the design.

Steps 2 and 3 describe the product as it works today; if a button is named differently, the idea is the same: a project with a design system attached, a new design inside it, context files attached, a prompt pasted.

## The rules that don't move (so exploration stays on-brand)

- Navy, steel blue, soft blue, cream. Nothing warm. No orange, ever.
- Figtree + Playfair Display italic + Overpass. Three families.
- Real photos only, from `photos/`, treated as prints with a border and caption. Jen's three are placeholders from her grid until she sends originals.
- The stamp under the masthead on every slide, same spot. The zip rotates.
- Copy is final in `COPY-DECK.md`. Design explores; it does not rewrite. Every last slide ends on her close: "i'm here for you... i do this to protect you and your best interest."
- Fair housing: never "safe," "family," "great schools," "quiet neighborhood," or who a place is for.

## What "variations" should mean

Explore one axis at a time, three to four candidates per axis, each clearly different:

1. **Cover composition.** Print upper-right with headline bottom-left (current) · headline top with the print bleeding off the bottom edge · full-width print with a cream band · no photo, ghost map only, headline huge.
2. **Photo treatment.** Print with border (current) · print with a torn top edge drawn in navy line · duotone navy on cream · photo inside a drawn building outline.
3. **Rhythm.** Two navy slides at 4 and 7 (current) · navy at 1 and 7 · alternating · cream throughout with one navy close.
4. **Type scale.** Current (headline 70, accent 94) · louder (headline 96, one word per line) · quieter, more body · the numeral slides at 240px.
5. **The stamp.** Roundel + text (current) · text only, no mark · a larger stamp on the cover only · the stamp as a vertical spine down the left edge.

Judge each candidate with the same three questions: does it still read as Jen at thumbnail size, does the copy still land, would it survive a screenshot with no other slides around it.

## Bringing a direction back into the pipeline

When you like something, export its PNGs or PDF and send them to me with one line on what changed ("cover: headline top, print bleeds bottom"). I update the generator so every future set inherits it, re-render all 21 slides, and re-sync the design-system project. The system stays one system.

## What's in this folder

- `DESIGN.md` — the spec, machine-readable tokens plus the rationale
- `RULEBOOK.md` — the seven rules, in plain words
- `COPY-DECK.md` — final copy for the three carousels and the ten presentation boards
- `PROMPTS.md` — five prompts to paste, one per exploration axis, plus a "new set" prompt
- `photos/` — the cleared photo bank with provenance
- `reference/carousels/` — the 21 finished slides as PNG; `reference/presentation/` — the ten boards; `reference/*.pdf` — vector PDFs of each set
- `source/` — the generators, so any direction you pick can be encoded and repeated
