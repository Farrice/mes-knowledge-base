# Ad Assembly Pipeline

Drop generated clips + a VO file into `assets/`, write one JSON manifest, run one command, get a finished 9:16 ad. A different ad is a different manifest — never a code change. Your only job is taste.

## Quick start

```bash
npm install
npm run render -- --manifest manifests/jcked-hookB.json
npm run still  -- --manifest manifests/jcked-hookB.json
```

Output: `out/<adName>.mp4` and `out/<adName>-poster.png` (name comes from the manifest's `adName`).

## Folder-drop workflow

| Folder | Goes here | Naming |
|---|---|---|
| `assets/clips/` | Generated video clips | Match the shot-list `id`, e.g. `H3.mp4`, `B1.mp4` |
| `assets/audio/` | VO recording | `<adname>-vo.mp3` |
| `assets/music/` | Music bed | `<brand>-bed.mp3` |
| `assets/images/` | End-card product photo (real PDP, label exact) | `<brand>-bottle.png` |

You never edit `src/`. If a referenced file isn't there yet, render **does not fail** — a missing clip becomes a labeled slate, missing VO/music becomes silence, a missing end-card image becomes a dashed placeholder box, and the CLI prints exactly what's absent. Drop the real file in and re-render; nothing else changes.

Files the two example manifests expect:

| Manifest | Files | Kit reference |
|---|---|---|
| `jcked-hookB.json` | `clips/H3.mp4`, `B1-B4.mp4`; `audio/jcked-hookB-vo.mp3`; `music/jcked-bed.mp3`; `images/jcked-bottle.png` | JCKED kit, Hook 3 + Body 1-4 |
| `puravita-hookA.json` | `clips/H1.mp4`, `B1-B5.mp4`; `audio/puravita-hookA-vo.mp3`; `music/puravita-bed.mp3`; `images/puravita-bottle.png` | Puravita kit, Cut A |

Five placeholder clips already sit in `assets/clips/` for JCKED (solid-color stand-ins, correct duration, silent audio) — that's what `out/test-render.mp4` renders from. Overwrite them with real generations; filenames already match, no manifest edit needed.

## The two commands

```bash
npm run render -- --manifest manifests/<file>.json [--out out/<name>.mp4] [--frames 0-299]
npm run still  -- --manifest manifests/<file>.json [--out out/<name>-poster.png] [--frame 120]
```

`--frames 0-299` renders just that range — fast preview of a cut (used for the 10s proof-of-concept below). `still --frame` defaults to 15 frames into the end card; override to grab a poster anywhere. `npm run start` opens Remotion Studio.

## Manifest field reference

| Field | Notes |
|---|---|
| `adName` | Also the output filename |
| `crossfadeFrames` | `0` = hard cuts (both kits' spec, default). `>0` = crossfade of that many frames between clips — **shifts the absolute timeline**, so recompute `captions`/`vo` offsets if enabled after they're locked |
| `clips[]` | `id`, `path` (e.g. `"assets/clips/H3.mp4"`), `label` (slate text if missing), `trimInSeconds`, `trimOutSeconds` (`null` = `trimIn + targetDuration`), `targetDurationSeconds` |
| `vo[]` | `path`, `offsetSeconds` (default `0`), `volumeDb` (default `0`) — one or more VO tracks |
| `captions[]` | `text` (verbatim from the kit's on-screen-text column, ≤6 words — never the full VO line), `startSeconds`, `endSeconds` |
| `accentWords` | Words/phrases rendered in the brand accent color (captions + end card), matched case-insensitively, longest phrase first |
| `music` | `path`, `volumeDb` (default `-18`), `duckWindows[]` (`startSeconds,endSeconds,volumeDb`), `silenceWindows[]` (`startSeconds,endSeconds`, ramped over 5 frames — both kits close on silence under the final CTA) |
| `theme` | `fontFamily`, `textColor`, `accentColor`, `backgroundColor`, `brandLabel`, `captionBottomOffset` (px from bottom, default `420`, keep 350-500 to clear Meta's UI rail) |
| `endCard` | `productImage`, `offerLine`, `guaranteeLine`, `holdSeconds` (default `4`), `backgroundColor` (optional override) |

## Adjusting caption timing after listening to real VO

The one taste task the pipeline can't do for you. Shipped `startSeconds`/`endSeconds` are estimates against each kit's stated pacing — they'll drift once real VO is in.

1. Play `assets/audio/<file>-vo.mp3` (or scrub in `npm run start`) and note the real second each on-screen-text phrase is spoken.
2. Edit those two numbers in `manifests/<file>.json` — nothing else needs to change.
3. Re-render.

Check `clips[i].targetDurationSeconds` too if a beat runs long/short against real VO.

## Fonts

Captions default to `'Inter Tight','Inter',-apple-system,'Segoe UI',sans-serif` — whatever's installed. For pixel-exact Inter Tight with **zero network calls at render time**: drop an `InterTight-*.woff2` into `assets/fonts/` and set `theme.fontFilePath` to that path. Loaded locally via `@remotion/fonts`; missing file falls back to the CSS chain silently.

## Proof of concept — what's actually verified

`out/test-render.mp4` (1080x1920, 30fps, h264, ~10s) rendered from `jcked-hookB.json` with `--frames 0-299` against five ffmpeg-generated placeholder clips (solid color, correct duration, silent audio — exercises the real `<Video>` path, not just fallback). Confirmed:

- Hard cut between clips at the declared duration (H3→B1 at frame 240/8s).
- Captions burned in, safe-area offset, accent-word coloring (`4,000mg` renders amber).
- Missing VO, music, and end-card image all degrade gracefully — CLI printed what's absent, render completed anyway.
- Missing clip file (tested by removing `B2.mp4`) renders its labeled slate, no crash.
- Puravita manifest parses and renders cleanly on its own theme (no placeholder clips generated for it — same code path, out of scope this pass).

**Not tested**: a full 81-85s/112-116s end-to-end render; real Higgsfield/Veo clips; real VO driving timing; `crossfadeFrames > 0` (written, typechecked, unexercised — both shipped manifests use hard cuts).

## Troubleshooting

- **`zod: installed 3.22.3, required 4.3.6` warning** — expected. The Remotion skill pins zod at exactly `3.22.3`; render completes correctly regardless.
- **ffmpeg not found** — `brew install ffmpeg`. Only needed to generate your own test clips.
- **Codec/playback issues** — output is always H.264/MP4, 1080x1920/30fps. Re-export source clips at 24-30fps before dropping in; mixed rates can look subtly off even though Remotion still renders.
- **Font looks like generic sans** — you're on the CSS fallback chain; see Fonts above.
- **New clip doesn't show up** — check `id`/`path` matches the actual filename exactly, including case.
