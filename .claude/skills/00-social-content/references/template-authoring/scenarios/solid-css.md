# Scenario solid — flat color

> Reached from `identification-tree.md` Q1 (`bg_treatment == solid-color`, no image zone). No AI generation at
> all — the background is CSS, the text is HTML/CSS over it. This is where HTML still genuinely wins
> (quotes, single-stat statements).

## Edit mode
- **None — no AI.** Background = `background: var(--brand-*)` (the brand bg/primary). The cream/solid color
  stays CSS; it is cheaper and truer to the brand color than asking the AI for a flat fill.
- **Text:** `html-craft.md` → flow zone over the solid. Big live type, real hierarchy, breathing room.

## Generation moment
- Never. No `[ai-image-zone]` block. (Exception: a **cutout subject** over the solid — then the subject is AI
  `edit-from-ref` with a transparent background composited over the CSS color; see the cutout-on-solid
  corollary in `ai-prompt-craft.md`. That makes the slide B+A, not pure solid.)

## Build
1. Root background: `var(--brand-primary)` (or the theme bg).
2. Text: a centered flow zone (`html-craft.md` §1 + §3) — display headline, optional body/CTA, `data-slot`
   per slot, triple-brace for HTML-bearing slots, 30–50px breathing margin.

## Extra QA criterion (beyond the common gate)
- **Contrast on solid:** the text color (`text-on-light` / `text-on-dark` per the solid's luminance) holds
  WCAG AA against the solid background — measured by `measure_text_contrast.py`, not by eye.
