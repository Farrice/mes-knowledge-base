# Flyer Artwork — Print-True SVGs

Generated deterministically 2026-07-08 (no image-gen — this card is pure
typography + QR, and generative models garble exact text and produce fake QR
codes; these files are the actual artwork, not comps).

| File | Format | Copy | Use |
|---|---|---|---|
| `flyer-4x6-variant1.svg` | 4"×6" @300dpi + 0.125" bleed | Variant 1 (Cooz verbatim, canonical) | Hand-to-hand |
| `flyer-4x6-variant2.svg` | 4"×6" @300dpi + 0.125" bleed | Variant 2 (two-beat A/B alternate) | Hand-to-hand A/B, min 100 cards |
| `placard-8.5x11-variant3.svg` | 8.5"×11" @300dpi + 0.125" bleed | Variant 3 (unattended canonical) | Counter placard |

**QR code**: real and scannable in every file, vector modules, 4-module quiet
zone, pointing at
`coachcooz.com/stop-feeling-like-shit?utm_source=flyer&utm_medium=print&utm_campaign=war-on-fitness-industry`.
**The page does not exist yet** — do not print until the squeeze page is live
at that slug (or regenerate the QR against the final URL).

**Before print**:
1. Font: files specify Archivo Black (free, Google Fonts) with Arial Black
   fallback. Install Archivo Black, then convert text to outlines.
2. Convert RGB → CMYK per the print notes in `01-flyer/FLYER-COPY-AND-SPEC.md`.
3. Test-scan the printed proof from 3 distances (arm's length, counter, ~30").
4. Per the design spec: a little roughness is the point — if a print shop
   offers to "clean it up," decline.

Regenerate/edit: `scratchpad/gen_flyers.py` (session scratchpad) or edit the
SVGs directly — they're plain vector text.
