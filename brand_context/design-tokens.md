# Design Tokens — Farrice Cain Premium Minimal (+ Performance Evidence Journal mode)

*Rebuilt 2026-09-02. The Parallax design system is archived and no longer a source. Living sources: `_active/farrice-brand/premium-minimal/package/` (02-DESIGN-CONTRACT.md, tokens/design-tokens.json v0.9-review, approved visual parent "P2-01 Premium Minimal V1"), `_active/farrice-brand/brand-direction-pilot/BRAND-DIRECTION-DECISION-BOOK.md` (Commissioned Decision Object kept as primary), and the 2026-08-31 visual-workflow verdict (`.agent/handoffs/2026-08-31-visual-workflow.md`). Do not fork tokens here; update the package.*

## Design intent
A commissioned decision object translated into a personal brand: quiet, exact, contemporary, decisive. Expensive because the thinking has been edited, not because the surface is decorated. Three mood words: **Restrained. Contemporary. Decisive.** A choice that serves none of them gets removed.

## Color (canonical)
| Token | Value | Use |
|---|---|---|
| canvas | #F3F3F0 | default background |
| paper | #FAFAF8 | lifted field, alternate page |
| ink | #101010 | primary text, the one dark recommendation |
| graphite | #555553 | secondary text |
| line | #D8D8D3 | rules, quiet structure |
| stone | #8C8C82 | large indices, nonessential labels only |
| white | #FFFFFF | dark-page text only |

Approved-banner exception: the launch banner keeps its legacy #F3F0EA / #151514 exactly. Those are not system tokens.

## Typography
Helvetica Neue only (fallback Helvetica, Arial, sans-serif). Weights 400 / 500 / 700. Display: sentence case, tracking -0.025em, close optical leading. Functional labels: uppercase, +0.16em tracking, bold. Prohibited: serif, italic, outline, decorative quotation marks, faux small caps, luxury tracking.

## Two modes, one system
- **Master-brand mode:** masthead `FARRICE CAIN`, descriptor `CREATIVE STRATEGY FOR SUPPLEMENT + PERFORMANCE BRANDS`. Content: point of view, lived observation, teardown, framework. Offer only in a restrained footer or final frame.
- **Offer mode:** masthead `THE ANGLE MAP`, author `FARRICE CAIN`. Three campaign arguments and one recommendation. Route grammar only when the content genuinely compares choices.

## Performance Evidence Journal (vertical Health Performance mode, verdict 2026-08-31)
Not a parallel brand system. A mode inside Premium Minimal for health and performance marketers who buy edited judgment and inspectable proof. Borrowed grammar: scientific blueprint structure (Alpine Bio reference), a bounded ledger grid (Operate reference), mono evidence labels (Integrated Biosciences reference). Preserve the canvas, Helvetica Neue, open space, proof boundaries, and the single dark recommendation. **Add no new palette.** Rejected directions: Peak State Cinema (dark full-bleed motion photography) and Private Performance House (linen, brushed metal, amber) both require a rebrand and risk category sameness.

## Photography
Original, unaltered Farrice portraits only (natural black wardrobe, warm real environments, direct unforced eye contact). Cropping allowed, nothing else. No synthetic portraits, beauty edits, creator-lifestyle props, stock supplement imagery, faux-lab imagery.

## Proof surfaces
Evidence crops, source labels, proof-status chips (VERIFIED / LIKELY / UNCONFIRMED), annotated margin notes live one click deeper, in Featured content and proof artifacts. The top-of-profile scan leads with the decision, never the documentation.

## Feeding the Scrapes pipeline
`00-social-content` reads `brand_context/visual-identity/tokens.json` and approved templates, produced by `/mkt-visual-identity`. That run has approval gates and is Farrice's to drive. Reference material for it: `premium-minimal/package/tokens/design-tokens.json`, `02-DESIGN-CONTRACT.md`, and the approved carousel and static templates under `premium-minimal/package/templates/`. Until it runs, the pipeline infers a palette; never let it default to the Anthropic-terracotta look.

## Hard rules
- Real brand logos on any slide that names a tool or company.
- Client brands are OFF mode: Jen Santulan work uses her palette, no orange, never this system.
