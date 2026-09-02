# Scenario A — framed image

> Reached from `identification-tree.md` Q3 (`image_zone.containment == contained-rectangle`).
> `text_placement: outside-image`. The image sits inside a contained rectangle; the text lives OUTSIDE it in a
> clean, bounded HTML zone. This is the case where HTML placing the text is SAFE — the zone is bounded, not
> guessed.

## Edit mode
- **Image:** `ai-prompt-craft.md` → **Partial — subject only** (`edit-from-ref`). The frame and composition
  are the ref; the delta is the subject inside the frame.
- **Text:** `html-craft.md` → flow zone beside/around the frame. Text is `isolable: true` by construction
  here (bounded clean zone) → HTML.

## Generation moment
- If the framed image is **fixed** (same picture every post) → generate **1× at setup**, store as a static
  asset; post-time swaps text only, zero AI.
- If the subject inside the frame **varies per post** → `edit-from-ref` every post with the validated prompt
  (`{SUBJECT}` delta). Save the validated prompt at setup (see `ai-prompt-craft.md`).

## Build
1. Image zone: `<img src="{{PHOTO_MAIN_PATH}}">` inside a contained rectangle (`object-fit:cover`,
   `border-radius` per ref). `data-slot="PHOTO_MAIN"`. **Object-isolability gate** (`identification-tree.md`
   Q3): the bounded `<img>` route is valid only when the ref's image block is flat, axis-aligned,
   non-overlapping, and free of scene treatment (rotation / perspective / cast shadow / occlusion). Rotated,
   overlapping, shadowed cards/props lying on a surface are in-scene objects → AI-placed
   (`craft/ai-prompt-craft.md` "In-scene per-post elements"), never flattened into axis-aligned `<img>` slots
   (the run-06 index-card-cover miss: ref-03's fanned, shadowed cards → 3 flat `<img>` rectangles).
2. Text zone: a bounded flow column outside the rectangle (`html-craft.md` §1) — kicker / headline / body,
   `data-slot` per slot, triple-brace for HTML-bearing slots, 30–50px breathing margin.
3. `[ai-image-zone:1]` block: `generation_route: edit-from-ref`, `ref_input: assets/ref-canonical.png`,
   `prompt_delta` = subject only (mark `# validated-at-setup` once the gate passes).

## Extra QA criterion (beyond the common gate)
- **Containment:** the image stayed inside its rectangle and did NOT invade the text zone (no bleed, no
  overlap with the headline column).
