# Report Dialect — Premium Minimal on internal report surfaces

**Decided by Farrice, 2026-08-06** (Readout OS mission). Applies to internal HTML report surfaces (research briefs, mission reports, the Briefing Room) rendered by `execution/render_brief.py` + `templates/research-brief/template.html`. The brand law in `package/02-DESIGN-CONTRACT.md` governs all outward-facing assets (LinkedIn, banners, client work) unchanged.

## The two sanctioned exceptions

1. **Italic-serif accent word stays.** The signature move of the brief format — ONE word per display/section heading wrapped `*like this*` renders in Source Serif 4 italic — is retained on report surfaces, recolored to the steel accent. Rationale: it is the recognition anchor of the format Farrice rated close-to-perfect; brand law's serif/italic prohibition remains in force everywhere outward.
2. **Functional hues added.** The approved system is hueless (canvas/ink/silver). Reports carry meaning-bearing color the master palette doesn't define:
   - **Steel blue** (`--ag-accent` / `--ag-focus`, oklch(46% 0.083 262) ≈ `#3D5A94`) — accent word, links, data bars, CTA. One blue, kept quiet ("Ink + Steel Blue" direction; the rejected Midnight Editorial navy/gold is NOT this and stays dead).
   - **Muted proof green / risk red** — VERIFIED/LIKELY/UNCONFIRMED confidence chips only. Never decorative.

## Canonical values

Neutrals come verbatim from `package/tokens/design-tokens.json` (`canvas #F3F3F0 · paper #FAFAF8 · ink #101010 · graphite #555553 · line #D8D8D3 · stone #8C8C82`). The report template maps them onto its existing `--ag-*` token names — see `templates/research-brief/template.html` `:root`, which is the implementation of record for report surfaces.

Everything else — grid restraint, one dark interruption per sequence, no gradients/shadows/badges, anti-slop rules — follows the master system.
