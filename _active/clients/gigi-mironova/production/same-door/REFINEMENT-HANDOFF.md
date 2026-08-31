# Same Door — refinement handoff

> **SUPERSEDED BY V4 / THE CALM CLOSER.** The Playfair/italic and soft-navy notes below
> document the prior pass only. Current authority: `CHARACTER-SYSTEM.md`, `tokens.py`,
> and `png/22-character-the-calm-closer.png`.

Everything needed to refine and enrich the kit by hand, in one place.

## The two live surfaces

| Surface | URL | Use it for |
|---|---|---|
| **Design canvas** (editable) | <https://claude.ai/code/artifact/1785940e-b1f7-49e5-a897-56dac8eab4e1> | Click any element, restyle in the properties panel, retype text inline, drag, export PNG/PDF. **Save** publishes for everyone. |
| **Kit page** (delivery to Gigi) | <https://claude.ai/code/artifact/595f01a0-e79c-47ee-9148-19442b475c14> | The finished package she receives — carousel, scripts, captions, stories, covers, don't-say list. |

Canvas notes: each artboard is independent (Main = slide 1). The photos ride as named
files — swap one by replacing the file of the same name and re-saving. PNG export is
per-artboard from the toolbar.

## Working files (regenerate anything)

`_active/clients/gigi-mironova/production/same-door/`

- `tokens.py` — the design system: every color, both photo treatments, type rules
- `build.py` — all 11 boards + every line of slide copy · `python3 build.py`
- `render.py` / `review_sheet.py` — PNGs + the contact sheet · run after any build
- `share_page.py` — the kit page: scripts, captions, bio, don't-say · `python3 share_page.py`
- `gen_covers.py` — the nine highlight covers → `covers/`
- `canvas-assets/` — the 8 canvas images (downsampled) · full-res in
  `../american-transaction/imagery/prepared/` with provenance
- Re-seed the canvas after editing boards: the seed command is in this session's
  history; artboards are the `.dc.html` files + `canvas.json`

## The design system (for any tool)

- **Type**: Figtree 400–800 throughout, with Manrope for Russian. No script or italic
  accent face; emphasis is a bold sans highlight.
- **Palette**: ink `#173A54` · band `#244C68` · muted `#566E7E` · mist `#DCE8EE` ·
  clay `#BD765E` · paper `#F7F3EC` · bone `#ECE7DE`
- **Grammar**: 1080×1350; 64/72px padding; ruled header + footer; ghost Playfair numeral
  760px bled off the right; photos are `bleed` (color, scrim) or `duo` (navy duotone);
  white slides are the densest; framing per-slide inline, never global

## Prompt for Claude Design / any refinement session

> Refine these artboards without changing the system: Figtree structural type with a
> readable bold highlight, soft HouseSellers navy (ink #173A54, deep #244C68,
> clay #BD765E), 1080×1350 with a ruled header/footer and an oversized ghost
> numeral bleeding off the right edge. Photography stays real (no generated images),
> treated as navy duotone or scrimmed color bleed. Every number is verified and must not
> change without a fresh source: $2,500 rent, $319,999 list, $620.31 listed dues,
> $2,658/mo estimate at 6.66%,
> $224 month-one principal, $393,000 building average, 82 days, $1,034,250 SFV median.
> Keep "estimate, not a quote" wherever $2,658 appears. Keep all fair-housing language
> exactly: no neighborhood demographics; verify dues against association documents.
> Russian text is a native-speaker draft; do not rewrite it. Voice: calm, precise, no
> exclamation marks, lowercase headline register.

## Copy pass provenance (2026-08-31)

Rewrite ran through three loaded experts: Luke Iha insight vectors (missing-variable on
the dues; hidden-condition on rent-vs-payment; authority reversal for the close), Georgi
nested curiosity loops (C1→C2→C3→C5), Cole sentence craft (terminal words, compression).
Georgi's harder clickbait footers were rejected for her verified register — calm,
no-nonsense — which wins every tie. Facts and compliance rails untouched.
