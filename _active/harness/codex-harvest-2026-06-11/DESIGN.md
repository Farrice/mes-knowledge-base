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

Suggested tokens (re-based 2026-08-06 on Farrice Cain Premium Minimal — canonical source: `_active/farrice-brand/premium-minimal/` incl. `REPORT-DIALECT.md`; the earlier tan/terracotta set is retired):

```css
:root {
  --ag-ink: oklch(18% 0 0);           /* #101010 ink */
  --ag-paper: oklch(96% 0.003 107);   /* #F3F3F0 canvas */
  --ag-surface: oklch(98% 0.002 107); /* #FAFAF8 paper (lifted field) */
  --ag-line: oklch(88% 0.005 107);    /* #D8D8D3 silver line */
  --ag-accent: oklch(46% 0.084 262);  /* steel blue ≈#3D5A94 */
  --ag-proof: oklch(48% 0.07 165);    /* muted proof green */
  --ag-risk: oklch(52% 0.10 25);      /* muted risk red */
  --ag-focus: oklch(46% 0.084 262);   /* links/bars — unified with accent */
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
