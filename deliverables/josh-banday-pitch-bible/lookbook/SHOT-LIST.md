# Lookbook Shot List — Josh Banday half-hour pitch (working title In-Betweener)

Living doc. Frames generated from this list, never improvised at the prompt bar (Dave Clark w03: script → outline → shot list → prompts).

## The idea in one sentence
A recurring guest actor who cannot say no keeps hitting other people's marks on a studio lot while secretly writing his own show.

## Genre container
Single-camera workplace comedy, photographed like a prestige half-hour (Atlanta / Hacks register). The container forgives: empty frames, practical-lit interiors, a lot that looks lived in rather than glamorous.

## Look card (mechanism, not mood)
1. **Light** — one motivated practical per frame, always visible or just out of frame: a stage tungsten unit, a video-village monitor, a pop-up-tent skylight, sodium parking lamps, office fluorescents. Key comes from one side; the other side falls off.
2. **Contrast and black point** — true black exists in every frame (deck floor is #070707). Everything not touched by the practical sits two stops under. Highlights roll off, never clip.
3. **Palette** — near-black neutral base with one accent family: warm amber-gold (deck gold #C9A96E). A single desaturated cream on paper, coffee cups, tape. No second warm, no orange, no teal.
4. **Atmosphere** — hazer smoke in stage light beams; dust in daylight shafts; marine-layer haze at night in the lot. Air density between planes in every frame.
5. **Capture register** — 35mm color negative, fine grain across the frame, vintage 2x anamorphic character (oval bokeh, soft edges, horizontal streak on practicals only), eye-level, static or near-static.

## Physics budget
Spent on the hero frame only (a single stage light in an otherwise dark stage). Every other frame is a shot a real crew could take on a real lot at a real hour.

## Aspect
All frames 16:9. Location cards crop to 3:2 in the deck; the hero runs full-bleed.

## Shots (camera reports)

| # | Slot in deck | Size / position | Light source | Subject action | Notes |
|---|---|---|---|---|---|
| 01 | Hero key art | Wide, eye level, centered, static | One tungsten stage unit from high camera-left, hazer on | An X of gaffer tape on the stage floor under the light; the *Roommates* living-room set out of focus far behind | The show's thesis: standing on a mark that isn't yours. Physics-budget frame. |
| 02 | Stage 7 — The Performance | Medium-wide from behind video village, slightly low | Set lighting spill plus two glowing monitors | Sitcom living-room set lit for a take; director's chair and two crew silhouettes in the near foreground, backs to camera | No faces. Coverage pair with 01. |
| 03 | Craft Services — The Bargaining Floor | Medium, eye level, three-quarter | Morning sun through a white pop-up tent | Folding table: coffee urns, bagel trays, a crumpled call sheet; two crew figures out of focus behind the table mid-conversation | The transaction floor. Cream accent lives here. |
| 04 | Trailer Village — The Hierarchy | Wide, low, down the row | Late sun from camera-right, long shadows | A row of large gleaming star trailers descending in size to a small dented shared trailer at the far end with a paper sign taped to its door | Size equals worth, in one frame. |
| 05 | The Writers' Room — The Holy of Holies | Medium, eye level, from the hallway | Warm interior light through a door window into a dim corridor | Closed door with a frosted window; through it, index cards pinned on a wall and a whiteboard; the hallway floor catches the spill | The room he isn't in. |
| 06 | The Parking Lot — The Truth | Wide, eye level, static | Sodium lamps overhead, one car's interior dome light | Studio parking structure at night, marine-layer haze; one parked car with its interior light on, driver-side window fogged | Where real conversations happen. |
| 07 | Production Offices — The Machine | Medium-wide through a glass wall | Fluorescent ceiling panels, one desk lamp | A bullpen of desks stacked with call sheets and binders; a conference room behind glass with blinds half-closed; whiteboard schedule grid | Decisions made without him. |

## Cadence (for the scroll, not a cut)
Hero holds full-bleed; six location cards read as a grid. Two-frame coverage on the stage (01 + 02) so the lot reads as one place.

## Generation and selection protocol
- Model: nano-banana-2 via `execution/generate_image.py`, `--aspect 16:9 --resolution 1K`.
- Prompts in `frames/prompts.py`; five-paragraph scene-plate prose (banana-pro-director Mode 3B, pure environment, cinema stack folded into the closing paragraph).
- Rule of Five relaxed to two takes per frame; pick, never composite, at this budget.
- Reject any frame with legible text, a readable face, a second warm, or a lifted grey black point.
- Frames land in `frames/`, converted to JPEG (q85, 1600 px) before embedding.

## Receipts
- Cost gate: gemini-image approved 2026-09-12 (quota lane, ~$0.006 per frame).
- Frame files: see `frames/manifest.json` once generated.
