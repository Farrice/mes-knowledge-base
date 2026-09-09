# Landing Page Ground-Up Rebuild Receipt

Run August 19, 2026 against the isolated Pulse preview at `127.0.0.1:8771`.

## Verdict

The prior 7,600px editorial proof-ledger treatment is retained only as a failed baseline. The current page was rebuilt from the visitor job: identify the leak, inspect the working behavior, understand the five-day build, evaluate proof and terms, and request a review.

This receipt establishes local render and interaction quality. It does not establish Farrice's felt approval, public deployment, conversion performance, or collected-payment proof.

## Preservation and rejection

- **Preserved:** offer facts, $1,500 price, $750 start, five-business-day delivery, human approval, proof-state disclosure, test evidence, Parallax wordmark, type roles, and core palette.
- **Rejected:** the proof-ledger concept, poster-scale typography, 128px release zones, decorative offsets, repeated status ornament, and full-page editorial pacing.
- **New page job:** one functional B2B service website with a sticky header, visible price and CTA, interactive proof case, explicit scope, native FAQ, and honest unconnected booking state.

## Website design system

- Page-scoped source: `WEBSITE-DESIGN.md`; the canonical Parallax system remains unchanged.
- Ink `#1C1C1E`, Violet `#7B61FF`, Warm White `#F5F0EB`.
- Same-hue accessibility variants: `#6D50F3` on Warm White and `#8F79FF` on Ink. Canonical Violet remains the non-text signal.
- Helvetica Neue and system sans-serif fallbacks for both display and reading copy; platform monospace for operational metadata.
- 1,184px maximum grid; 80px desktop, 68px tablet, and 56px mobile section rhythm.
- Flat surfaces, nearly square controls, no gradients, shadows, glows, pills, glass, or bento wall.

## Browser inspection

| Viewport | H1 | Section rhythm | Document height | Overflow | Result |
|---|---:|---:|---:|---:|---|
| 1280 × 800 | 67.2px | 80px | 5,210px | 0px | PASS |
| 768 × 1024 | 48px | 68px | 6,344px | 0px | PASS |
| 375 × 812 | 43.875px | 56px | 8,813px | 0px | PASS |

- Sticky header: 77px desktop/tablet and 67px mobile.
- Header CTA: 44px minimum height at all three breakpoints.
- One H1; no duplicate IDs; no broken internal anchors; no unnamed links or buttons.
- English document language, descriptive title, and header, nav, main, and footer landmarks present.
- Fresh browser tab: zero console errors and zero warnings.
- Primary text contrast: Ink on Warm White is 15.03:1.
- Accessible Violet variants: 4.53:1 on Warm White and 5.14:1 on Ink.
- `WEBSITE-DESIGN.md` front matter parsed successfully with all required local schema groups. The optional official `@google/design.md` lint could not complete because its `npx` call timed out after 60 seconds; this is recorded as a tooling limitation, not a false PASS.

## Interaction inspection

- The interactive example completed five visible workflow stages.
- Final state: `Ready for your approval`.
- Final result: `The proposal is ready for your approval. Nothing has been sent.`
- FAQ disclosure opened correctly.
- The local-only CTA revealed the missing booking destination and moved focus to that status message.
- Reduced-motion CSS preserves functionality without smooth scrolling or control transitions.

## Visual evidence

Current Helvetica-style, simplified-copy renders:

- `screenshots/simplified-copy-desktop.png`
- `screenshots/simplified-copy-tablet.png`
- `screenshots/simplified-copy-mobile.png`

Previous ground-up renders retained for comparison:

- `screenshots/rebuild-final-desktop.png`
- `screenshots/rebuild-final-tablet.png`
- `screenshots/rebuild-final-mobile.png`

Failed and iterative evidence remains available for regression comparison:

- `screenshots/after-desktop-1280.png` — rejected baseline.
- `screenshots/rebuild-iter1-desktop.png` — first ground-up composition.
- `screenshots/rebuild-iter2-first-viewport.png` — anchor-alignment correction.

## Boundary

No page, booking link, payment destination, profile, post, or outreach message was deployed or sent. The exact offer remains unvalidated until a client pays the first $750 deposit.
