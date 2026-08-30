# First Home Valley — imagery bank

Real photographs only. No generated images, no illustrations, no CGI renders.

## Licence position

Everything in `shortlist/` and `prepared/` is **CC0 or Public Domain Mark**. That means
commercial use is cleared and **no attribution is required** — nothing here puts a credit
obligation on Jen's feed. Full source records are in `provenance.jsonl`: one row per file
with the Openverse id, the originating provider, the landing page, the licence, and the
query that found it.

Sourced via the Openverse API, which needs no key. Providers that actually delivered:
**rawpixel**, **StockSnap**, **Wikimedia Commons**.

## What the pool gave, honestly

| | |
|---|---|
| Fetched | 93 candidates across two passes |
| Survived the eye | 22 (~24%) |
| Cut on sight | posed smiling-stock families, CGI renders, wrong-geography houses (Pacific Northwest, Europe), wrong-city street maps, one flatly unusable flatlay |

The pool's strength is **place** — California streets, palms, golden hour, archival
suburbia. Its weakness is **people**: every human frame on offer is either posed
commercial stock, an engraving, or a disembodied pair of hands. That gap is real and
is called out in the open-items list below.

## Assignments

**The rule, set by the design pass:** STRUCTURE slides stay white, STORY slides carry
photography. The three photo-free slides are the three densest layouts — that is the
deck's breathing rhythm, not a gap.

| Artboard | Image | Treatment | Why this one |
|---|---|---|---|
| A1 · Hook | `palm-tree-sunset-city-02` | bleed | The basin at golden hour, palms, skyline. Establishes place in one frame. |
| A2 · Old Map | `valley-street-01` | duotone | Archival palm-lined street. The 1981 beat wants an archival photograph, not a modern one. |
| A3 · 29→40 | *(none)* | — | Comparison slide. Stays white. |
| A4 · 21% | `apartment-building-dusk-03` | duotone | Curved balconies — architectural, abstract, doesn't compete with the stat. |
| A5 · Three Questions | *(none)* | — | Densest slide on the deck; a photo would bury it. |
| A6 · CTA | `valley-street-00` | bleed | Apartment block at dusk with palms. Closes where the buyer actually lives. |
| R1 | `apartment-building-dusk-01` | bleed | Looking out a window at the apartments you rent. Exactly the reel's premise. |
| R2 | `apartment-building-dusk-02` | bleed | Renting, at dusk — the literal subject of the line. |
| R3 | `california-bungalow-00` | bleed | The entry home. Replaced a better photograph (see below). |
| R4 | `suburban-neighborhood-aerial-02` | bleed | The market itself, from above. |
| R5 | `house-key-lock-00` | bleed | Keys in the lock — the "last week I handed her keys" payoff. |
| M1 · Magnet | *(none)* | — | Card layout with its own numbered list and CTA. Stays white. |

## Design pass — what the first cut got wrong

Three slides shipped broken in pass one and are fixed:

1. **A6's call to action was invisible.** A6's v1 frame was already dark, so its inline
   colours were authored for a dark ground. The light→dark remap fired on it anyway and
   turned a white button's navy label white — "DM me MATH" disappeared into its own
   button. Fix: `ALREADY_DARK = {"A4", "A6"}` is skipped by the remap.
2. **Band treatments sat on live type.** Every v1 layout pins content to both edges with
   `justify-content:space-between`, so an edge band has no empty edge to occupy. A3's
   source line and page number were buried under the band; M1's headline was swallowed.
   Fix: band treatments removed entirely; those slides stay white.
3. **A global `scale(1.10)` cropped every image.** It was added once to hide a scan
   border on A2 and silently took 10% off all the others — that is what reduced R2 and
   R4 to a wrist on empty grey. Fix: scale and `object-position` are per slide now; only
   A2 carries a scale.

R2 and R4 also got new photographs; the close-crop hand shots never survived a 4:5 frame.

### One deliberate downgrade

`front-door-house-00` — a yellow stucco wall, a red arched door, a painted house number —
is the strongest single photograph in the bank. It is not in the deck. It reads
Mediterranean, and its yellow/red fights the navy palette hard enough that the slide stopped
looking like Jen's brand. `california-bungalow-00` is the weaker photo and the right one.
It stays in `shortlist/` if that call ever gets reversed.

## Held in reserve

`palm-tree-sunset-city-00` (B&W palms), `palm-tree-sunset-city-01` (Valley haze),
`balcony-plants-apartment-02`, `los-angeles-street-01`, `apartment-building-dusk-02`,
`suburban-neighborhood-aerial-02`, `table-math-01` (archival desk, another 1981 option),
`front-door-house-02` (archival porch), `sunlight-through-window-floor-00`,
`contract-signing-pen-01`, `front-door-house-00`.

## Open items

1. **No usable photograph of a person.** Reels 1–5 currently carry place and objects.
   Fixing it needs a library the CC0 pool doesn't have — a free Pexels or Unsplash API key
   (two-minute signup, both free, both commercial-cleared) would open it. That key is
   yours to create; the fetcher already has the free-first path wired at
   `execution/broll_source.py`.
2. **Jen's own photography beats all of this.** Four real reel stills already sit in
   `_active/clients/jen-team-pilot/landing/img/`, but at 360×640 they are too small for a
   1080×1350 artboard. Originals would replace half this bank.

## Rebuilding

```bash
python3 fetch_bank.py pull      # role-based first pass
python3 sweep.py                # wide second pass
python3 contact_sheet.py        # look at them before trusting a filename
python3 make_shortlist.py       # copy the keepers
python3 prepare.py              # downscale to artboard-ready
```
