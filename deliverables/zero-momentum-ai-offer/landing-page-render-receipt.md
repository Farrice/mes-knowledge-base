# Landing Page Render Receipt

Run August 19, 2026 against the isolated Pulse preview at `127.0.0.1:8771`.

## Visual authority

- Canon: `_active/farrice-brand/parallax-design-system/DESIGN.md`.
- Identity: canonical Parallax wordmark and favicon assets; no reconstructed mark.
- Palette: Ink `#1C1C1E`, Violet `#7B61FF`, Warm White `#F5F0EB`; retired steel, green, beige-alert, and red status colors removed.
- Type: Space Grotesk for display, Source Serif 4 for reading, JetBrains Mono for labels and operational data.
- Geometry: flat surfaces, sharp corners, one 2px CTA radius, no gradients, shadows, glows, pills, bento cards, or floating price card.
- Page concept: one editorial proof ledger with a deliberate dark-to-light human-hold reveal.

## Spacing and composition

- Desktop field: 12-column asymmetric hero with the headline on eight columns and the pilot ledger in the right margin.
- Section rhythm: 64–128px tokenized spacing, with true release zones before the proof state, human-hold reveal, acceptance terms, and final CTA.
- Reading lanes stay near 60–65 characters; operational density is concentrated in the workflow and test-bench sections.
- The three pain points are editorial rows rather than cards; the five workflow stages are one connected spine.
- Mobile uses 24px page gutters, a 12px controlled headline offset, a vertical workflow rule, and full-width CTAs.

## Browser inspection

| Viewport | Result |
|---|---|
| 1280 × 800 | PASS — full-page screenshot inspected; three-beat rhythm and right-margin pilot ledger hold |
| 768 × 1024 | PASS — single-column hero and vertical workflow spine; scope remains two-column |
| 375 × 812 | PASS — no horizontal overflow; reading order, release zones, and scope collapse hold |

- Document width equals scroll width at 375, 768, and 1280px.
- Both CTA targets are at least 48px high at every tested breakpoint.
- Both wordmark assets loaded at their 1344px natural width.
- One H1, one main landmark, no duplicate IDs.
- Fresh browser tab: zero console errors and zero warnings.
- Visible-copy extraction: prose classifier `CLEAN`, AI score `0/10`, 685 words, zero detected signals. (The raw HTML wrapper is not treated as prose because repeated tags create false structural matches.)

## Visual evidence

- `screenshots/after-desktop-1280.png`
- `screenshots/after-tablet-768.png`
- `screenshots/after-mobile-375.png`
- `screenshots/before-desktop.png`

This is a local render receipt. It is not a public deployment, booking integration, payment event, or conversion test.
