# frbpm — Farrice Anime Avatar CANON (locked 2026-08-03)

The character is **Farrice Cain, stylized** — modern shonen cel register ("twilight" design-round winner, his pick). Trigger word / dataset spine: **`frbpm`** (made-up, non-colliding; echoes the My.BPM music thread). Public display name: **FRESH** (Farrice's real-life nickname, given 2026-08-04). In prompts and captions the trigger stays `frbpm`; in titles, dialogue, and content he is Fresh.

Method: `skills/mickmumpitz/workflows/01-character-lock-dataset.md`. The dataset IS the character; the model is disposable.

## Identity map (one line, for any captioner or prompt)
frbpm is the Black man with warm brown skin, a short tapered natural fade, a thin mustache with soul-patch goatee, high cheekbones and a strong jaw, wearing matte-black over-ear headphones with a thin cyan accent ring around his neck.

## Consistency budget (the decision everything else executes)

| LOCKED — never changes, never captioned | VARIABLE — varied AND captioned in every image | FREE |
|---|---|---|
| Face geometry (cheekbones, jaw, eyes) · warm brown skin · tapered fade · thin mustache + soul-patch goatee · **signature: matte-black over-ear headphones w/ thin cyan ring** · modern shonen cel render style | Expression · pose/action · setting/environment · lighting · headphones position (around neck ↔ on ears — captioned when on ears) | Background incidental detail |
| **Wardrobe v1 (locked this version):** black bomber over white tee, black slim pants, clean white low-top sneakers | | |

Wardrobe note: locked in v1 (silence welds it to the trigger). To add outfits later: generate a wardrobe-variant sub-set, caption the outfits explicitly, THEN treat wardrobe as VARIABLE. Never mix half-captioned wardrobe.

## Canonical references
- **Style/identity anchor:** `dataset/I1.png` (identity close-up) + the design-round winner (board: `avatar-design-round` / twilight)
- **Real-photo ground truth** (identity source, not style): wedding photo `~/Downloads/05_Media_Files/174433_…273A0932.jpg` + Secta `EcoS5Baf` / `t6zBuqFN` (staged copies used at build time)
- Full manifest: `dataset/` — T1–T5 turnaround · I1 identity · E1–E6 expressions · B1 body · R1–R3 range · S1–S3 wide-scale · L1–L3 lighting · H1–H4 headphone anchors (each `.png` + reverse-prompt caption `.txt`)

## Usage recipe (until a bake rung exists — reference-chaining)
```bash
bash skills/fantastic-posters/gen.sh "<full art direction: 'The character frbpm: the exact man in the reference images — [identity map line]. Modern shonen cel style. [scene/pose/expression/lighting].' NO text." \
  --style=direct --quality=medium --size=WxH \
  --refs="_active/farrice-brand/05-assets/anime-avatar/dataset/I1.png,_active/farrice-brand/05-assets/anime-avatar/dataset/<closest-pose-or-angle>.png"
```
- Pick the 2–3 dataset refs CLOSEST to the target shot (angle + framing beat style words).
- Register swaps (manga-ink strips, etc.): keep the identity map + refs, change only the render-style clause — identity survives, register changes.
- Drift repair: snip the drifted detail from a dataset image, add it as an extra ref (the Mickmumpitz move — better picture, not better adjective). Diagnostic: `skills/mickmumpitz/references/prompts-v2/consistency-drift-diagnostic.md`.

## Known repair list (v1)
- T3 (left profile): sneaker colorway drifted black/white before shoes joined LOCKED — re-roll when convenient ($0.04).
- No real-photo profile reference exists on disk — profile views are style-authored; if Farrice exports true profile photos from Photos.app, re-anchor T3/T4.

## Bake-readiness
This dataset + captions is LoRA/finetune-ready (per-image caption files, trigger word, locked/variable discipline). If a fal training recipe is added later, bake per `skills/mickmumpitz/` Step 6 (sample the curve, several checkpoints, prune first) — no dataset rework needed.

## Acceptance test v1 (2026-08-03) — FOLDER HOLDS
12/12 fresh prompts rendered via the usage recipe (board: 🎭 frbpm-acceptance). Honest-folder findings, failures as objects: (1) A4 podcast — cyan ring reads on only one earcup under warm light (detail suppression; snip-and-refeed H1 if it matters); (2) A6 crouch — finger anatomy simplified in the shoelace grip (small-hand rendering; harmless at social scale); (3) A12 extreme close-up — forehead creasing heavier than canon register (realism drift at extreme crop; add "smooth cel skin" clause on extreme close-ups). Identity, wardrobe, sneakers, silhouette, and the manga-ink register swap (A7) all held. Both required transfers proven: true profile with no profile photo (A10), register swap with identity intact (A7).
