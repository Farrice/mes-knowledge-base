# Canva-native editions — the repeatable recipe (2026-09-02)

The template stays a template. Every edition is a copy of it, filled through the Canva connector. Nothing is moved; only text, photos, and colors change. First run: Jen · The Valley · Tarzana Edition 01 (design `DAHUEKxS7Ig`, copied from Local Gem `DAHUD1-FGgs`).

## The loop (one edition, ~10 tool calls, $0)
1. `copy-design` the template → new design id. The original is never edited.
2. `upload-asset-from-url` for each photo. Only public HTTPS URLs work (her Facebook photo URLs do; local files do not). Returns an `asset_id` per photo.
3. `read-design` with `open_transaction: true`, all pages → every element's `locator_id`, plus the `transaction_id`.
4. `edit-design` per page (one call per page): `replace_text` on masthead / headline / body / pill · `format_text` color `#F7F5F2` on headlines · `update_fill` with the page locator to swap the background photo, or with an inset shape's locator to swap a rounded photo · `delete_element` for accents we don't want · `add_text` + `format_text` for a line the template lacks.
5. Check each returned thumbnail. Then `edit-design` with `finalize: "commit"`.
6. `get-export-formats` → `export-design` png → `fetch_export.py` to bring the pages down.

## What the API cannot do (do it in Canva, one click each)
- Recolor the decorative badge / arrow / stripe rects (`recolor_element` refuses `rect-element`). We delete the arrows; the smiley stays yellow until recolored in the editor.
- Change the pill's stroke color (`update_stroke_properties` errors on this shape).
- Remove the headline's gradient text effect. `format_text` sets the color to cream in the document, but the template's effect still renders the ivory-to-yellow gradient. Editor: select headline → Effects → none, or keep it.
- Change typeface (`fontRef` is read-only). Added text lands in Canva's default font; match it in the editor if it matters.

## Slots per page (Local Gem)
| page | archetype | slots |
|---|---|---|
| 1 | cover | masthead, headline (italic first line), subline, pill, background photo, badge |
| 2–4 | spot | masthead, headline, pill, body, background photo, two rounded inset photos |
| 5 | close | masthead, headline, pill, (added) close line, smiley |

## Edition 01 content map
| page | copy | photo | truth |
|---|---|---|---|
| 1 | $869K in Tarzana · three homes, one price, the 7am line at Laidrey on Ventura… buying or selling | her listing exterior | comp VERIFIED (FACTS.md); photo is her listing, not the comp |
| 2 | Laidrey Coffee on Ventura · 18600 Ventura Blvd, doors at 7am | template stock cafe (placeholder) | Laidrey address + hours VERIFIED (Yelp/laidrey.com); needs her own photo of the spot |
| 3 | Three Buildings. One Lot. · new construction in Tarzana, listed by me… DM for a private showing | her kitchen bg, living + pool insets | photos LIKELY 5421 Bothwell; price and address left off until she confirms |
| 4 | What $869K Buys Here · 3 bed, 1.5 bath, 1,136 sq ft on a 7,296 sq ft lot… not mine | template stock patio (placeholder) | comp VERIFIED; insets deleted rather than mislead; needs a street/exterior photo |
| 5 | Send Me the Street. · her verbatim close | template stock cafe (placeholder) | hers |
