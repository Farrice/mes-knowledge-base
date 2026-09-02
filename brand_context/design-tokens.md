# Design Tokens — pointer

*Populated 2026-09-02. The living design system is `_active/farrice-brand/parallax-design-system/DESIGN.md` (plus `PARALLAX_BRAND_BOOK.html`, `photography-direction.md`, `voice-and-tone.md`). Readout and brief deliverables use the separate "Ink + Steel Blue" premium-minimal dialect in `_active/farrice-brand/premium-minimal/REPORT-DIALECT.md`. Do not fork tokens here; update DESIGN.md.*

## Parallax (personal brand, newsletter, social)
Japanese minimalism meets hip-hop typography. Muji meets Madlib. Take the most familiar premium format and change exactly 3%. The 3% is the offset: one letter in violet. Quiet defiance, never aggressive.

| Token | Value |
|---|---|
| ink (primary, surface) | #1C1C1E |
| violet (accent) | #7B61FF |
| warm-white (on-surface, on-accent) | #F5F0EB |
| display / headline | Space Grotesk 700 |
| body | Source Serif 4 400, 17–20px, line-height 1.6 |
| labels, captions, buttons | JetBrains Mono, letter-spacing 0.05–0.12em |

## Visual identity for the Scrapes pipeline
`00-social-content` reads `brand_context/visual-identity/tokens.json` and approved templates, produced by `/mkt-visual-identity`. That run has approval gates and is Farrice's to drive. Feed it `parallax-design-system/DESIGN.md` and `PARALLAX_BRAND_BOOK.html` as the reference material. Until it runs, the pipeline falls back to inferred palette; do not let it default to the Anthropic-terracotta look.

## Hard rules
- Real brand logos on any slide that names a tool or company; never a generic icon.
- No orange anywhere in Jen Santulan client work (separate brand; OFF mode).
