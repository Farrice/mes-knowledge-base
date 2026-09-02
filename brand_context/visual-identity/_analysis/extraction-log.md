# Extraction log — Farrice Cain visual identity

## 2026-09-02 — Mode I (Import) from declared design system

**Operator:** Claude (Fable 5.1) on Farrice's instruction ("run the visual identity thing now"). Brand name, masthead labels, fonts, and colors were NOT interviewed: every value is declared on disk in the approved Premium Minimal package, and Farrice's standing rule is never to interview about what is on disk. The one human gate kept is the Phase 4.7 identity approval.

**Sources (declared, authoritative):**
- `_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md` — intent, mood words, modes, color tokens, typography, grid and spatial law, rules and lines, standard surfaces, components, portrait policy, prohibited signals
- `_active/farrice-brand/premium-minimal/package/tokens/design-tokens.json` v0.9-review — same values, machine form
- `_active/farrice-brand/premium-minimal/package/01-BRAND-FOUNDATION.md` — brand hierarchy, audience, authority posture
- `_active/farrice-brand/premium-minimal/package/03-ASSET-STATE-LEDGER.md` — approval states, locked decisions, rejected territory
- `_active/farrice-brand/brand-direction-pilot/BRAND-DIRECTION-DECISION-BOOK.md` — Commissioned Decision Object kept as primary; portrait borrowed from Human Signal Studio; proof modules from Evidence Field Review
- `.agent/handoffs/2026-08-31-visual-workflow.md` — Performance Evidence Journal chosen as the vertical Health Performance mode inside Premium Minimal; no new palette

**Multi-brand disambiguation:** one brand detected (Farrice Cain). The Angle Map is offer mode of the same system, not a sibling. Skipped.

**Intake categories:**
- style refs: declared system used instead of raster extraction (no k-means, no OCR, no trace overlay); the package's SVG templates under `templates/static` and `templates/carousel` remain available for Phase 4.5 composition extraction later
- logo: none by design; the functional masthead label is the identity mark
- headshot: not placed; portrait policy allows only the original from the private identity add-on, which Farrice supplies
- fonts: Helvetica Neue is a macOS system font (`/System/Library/Fonts/HelveticaNeue.ttc`); no font files copied into `fonts/`, no Google Fonts URL; off-Mac renderers fall back to Helvetica/Arial

**Decisions made while mapping to the skill's schema:**
- `colors.accent` = ink on purpose. The system has no accent hue; the single bold move is the dark recommendation.
- `chrome.pagination` = null. The system uses a two-digit field index, not dots.
- `chrome.masthead.labels` = `["FARRICE CAIN", "", "CREATIVE STRATEGY FOR SUPPLEMENT + PERFORMANCE BRANDS"]` (master-brand mode); offer-mode labels stored alongside.
- Type scale sized for 1080×1350 from the contract's tracking and leading rules; absolute pixel sizes are the one set of values not declared in the contract and are therefore NOT locked.
- The approved launch banner's legacy colors (`#F3F0EA` / `#151514`) are recorded as an exception, never as tokens.

**Locked fields:** see `tokens.json → locked_fields` (brand, all fonts, all colors, masthead, pagination, tracking, grid rules).

**Next:** Phase 4.7 brand bible v1 + Farrice approval → Phase 6 regen → Phase 7 config complete. Template building (composition extraction from the package SVGs, `templates/<pool>/` with `status: ready` promotions) is the downstream pack's job and needs Farrice's promotions per the asset ledger.
