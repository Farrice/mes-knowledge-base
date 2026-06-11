# Codex Antigravity Design System

## Design Intent

Codex Antigravity should feel like a calm command center for serious creative and operating work. The design language should support scanning, comparison, routing, proof, and repeated action. It should not feel like a generic SaaS landing page, AI dashboard template, or decorative inspiration board.

## Visual Direction

- Use restrained surfaces with one or two deliberate accents rather than full-page gradients.
- Prefer structured editorial density over oversized hero composition.
- Use visual contrast to separate intent, evidence, state, and next action.
- Give creative artifacts room to breathe, but keep operational interfaces compact.
- Avoid nested cards; use bands, tables, panels, timelines, and annotated layouts when they communicate the job better.

## Color

- Base neutrals should be lightly tinted, never pure black or pure white.
- Accent colors must be tied to meaning: routing, proof, risk, creative direction, completion, or warning.
- Do not default to blue CTAs or purple-blue gradients.
- Favor palettes with useful contrast across state and hierarchy.

Suggested tokens:

```css
:root {
  --ag-ink: oklch(18% 0.012 245);
  --ag-paper: oklch(97% 0.008 92);
  --ag-surface: oklch(93% 0.012 100);
  --ag-line: oklch(76% 0.018 95);
  --ag-accent: oklch(55% 0.115 43);
  --ag-proof: oklch(49% 0.082 168);
  --ag-risk: oklch(56% 0.126 23);
  --ag-focus: oklch(50% 0.105 265);
}
```

## Typography

- Pick typefaces for the job, not because the browser default is available.
- Use a strong information hierarchy: display, section, body, caption, metadata.
- Keep body copy between 65 and 75 characters where possible.
- Use weight, spacing, and alignment to create scanning paths.
- Avoid all text sitting at the same weight or size.

## Layout

- Build around the workflow: input, route, evidence, decision, artifact, next move.
- Use stable dimensions for toolbars, boards, cards, and repeated rows.
- Vary spacing rhythm intentionally; avoid identical padding everywhere.
- Let tables and compact panels carry operational detail.
- Use cards only for repeated items, modals, or framed tools.

## Components

- Command surfaces: compact list/table layouts with command, purpose, route, and confidence.
- Quality gates: scorecards with pass/revise/rework states and specific directives.
- Creative briefs: structured sections for audience, mood, references, constraints, production notes, and anti-references.
- Artifact hubs: index-style documents that make the next action obvious.
- Review outputs: findings first, then corrections, then the smallest useful next move.

## Motion And Interaction

- Motion should clarify state, progress, or focus.
- Use quick ease-out transitions for interface feedback.
- Avoid bounce, elastic effects, or decorative fade-in on everything.
- Hover and focus states should be visible, accessible, and purposeful.

## Anti-Slop Rules

- No decorative glass cards.
- No repeated three-column card grid as the default structure.
- No split hero with text on one side and a generic illustration on the other.
- No gradient text.
- No stock-like imagery when the real product, state, or object should be visible.
- No visual decisions without a reason tied to product purpose, audience, or creative direction.
