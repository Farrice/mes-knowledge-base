# Jen Social Design Library

Five independent, reference-derived social design systems for Jen Santulan. Each keeps the visual grammar of one supplied carousel pack while using one restrained Jen layer for identity, voice, accessibility, sourcing, and real-estate safety.

Status: **production-capable design foundation; proof copy only; not approved for publishing**.

## What this solves

You can hand Codex a content source, a desired outcome, approved imagery, and optionally a system name. Codex can then:

1. choose the best of the five systems;
2. turn the source into one swipe argument with one idea per slide;
3. create a structured content packet;
4. render 1080×1350 PNGs in the selected visual grammar;
5. run fit, contrast, image-rights, source, fair-housing, and human-review checks.

The current Valley Native navy/cream system remains intact. These are five additional editorial modes, not a replacement or rebrand.

## The five systems

| System | Best job | Emotional result | Avoid |
|---|---|---|---|
| **After Hours Guide** | Curated local guides, premium neighborhood atmosphere, restaurants, listing mood | Cultured, cinematic, in-the-know | Dense buyer math or alerts |
| **Sunlit Local Notes** | Local gems, weekend routines, community discoveries, saveable lists | Friendly, curious, lightly handmade | Luxury or formal explainers |
| **Quiet Home Editorial** | Jen POV, reflective home stories, permissioned client moments | Intimate, mature, trustworthy | Listicles or data-heavy posts |
| **Valley Moments** | Day-in-the-life, commute, routine, short narrative lessons | Contemporary, energetic, emotionally observant | Formal listing proof |
| **Hidden Address Journal** | Listing/neighborhood pairings, hidden-value stories, premium local editions | Vintage, discerning, collected | Casual updates or dense education |

The complete extraction and decision logic is in [REFERENCE-HARVEST.md](REFERENCE-HARVEST.md). Each system's blind-designer-ready specification lives in [systems/](systems/).

## What to hand Codex

Use plain language. This is enough:

```text
Create a 5-slide Jen carousel from this content: [paste source or point to file]
Audience: [who it is for]
Job: [teach / local affinity / listing proof / personal trust / conversation]
System: [choose for me or name one]
Approved photos: [paths or attach them]
Sources and dates: [for any factual claim]
The one thing Jen genuinely believes: [her natural point of view]
```

If the system is not named, route by content job—not by which palette seems attractive.

## Creation contract

1. **Lock the source.** Separate verified facts, Jen's lived point of view, and proof-only placeholder copy.
2. **Choose the engine.** Use the router in `systems.json`; do not blend visual grammars inside one carousel.
3. **Write the swipe.** Cover promise → retention bridge → one idea per slide → human close. Copy comes before design.
4. **Build the packet.** Validate against `input.schema.json`.
5. **Render.** `python3 render.py --input <packet.json> [--style <system-id>]`.
6. **Inspect at phone size and full resolution.** Check wrapping, contrast, focal-point collisions, copy density, image crop, and slide-to-slide rhythm.
7. **Human gate.** Jen approves voice; the relevant source owner approves volatile facts; no automatic publishing.

## Files

- `systems.json` — machine-readable tokens, routing, and constraints.
- `input.schema.json` — reusable content-packet contract.
- `render.py` — five-style PNG renderer.
- `examples/proof-content.json` — one proof carousel per system.
- `proofs/` — 15 rendered transfer-test slides plus one contact sheet.
- `references/` — five contact sheets representing all 27 supplied reference slides.
- `REFERENCE-HARVEST.md` — why the references work and what was extracted.
- `SHARED-JEN-LAYER.md` — the fixed Jen behavior across all five systems.
- `systems/*.md` — the human design manual for each independent system.

## Proof state

- **VERIFIED:** all 27 supplied slides were inventoried and visually represented in the saved reference sheets.
- **VERIFIED:** palettes were sampled from the supplied pixels; roles were assigned by observed usage.
- **LIKELY:** the recommended font families are functional analogues. Raster packs do not expose their original font files.
- **VERIFIED:** the proof renderer used the written tokens and Jen/Valley imagery rather than the original reference slides.
- **PASS FOR DIRECTION REVIEW:** all five engines produced recognizable three-slide transfer tests.
- **UNTESTED:** Jen's taste verdict, a full 5–7-slide production carousel, Canva editability, and live audience response.

## Do not flatten the library

The shared Jen layer may govern identity, voice, sourcing, and safety. It must not force every system into navy/steel, make every slide use the same masthead, or merge the five type/composition grammars. Consistency comes from repeated internal rules, not visual sameness.
