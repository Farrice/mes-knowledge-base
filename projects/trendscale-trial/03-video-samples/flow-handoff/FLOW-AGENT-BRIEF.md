# Google Flow Studio — Creative Assistant Handoff (JCKED Locked Vault)

Paste the block below into Flow's sidebar assistant at the start of the session. Upload the assets it names (from `assets/` next to this file) before generating. Per-clip prompts live in `../jcked/JCKED-PROMPT-PACK.md` (Veo 3.1 timestamped blocks — paste them exactly as written; they already carry the subtitle guard and negatives).

---

## PASTE BLOCK — session brief for the Flow assistant

```
You are assisting on a performance ad production. Follow these standing rules for
every generation in this project; do not restyle or improvise beyond them.

PROJECT: JCKED "The Locked Vault" — 9:16 vertical ad, Veo 3.1 Quality, 1080p,
8s clips, generated scene by scene and assembled in edit. Editorial restraint:
one deliberate camera move per clip, dark navy + steel + amber palette, quiet
mechanical sound design, no music unless the prompt says so.

VISUAL LAW: the whole ad lives on one image — a locked vault and the key that
opens it. The lock is an enzyme called CPT-1, the key is the nutrient. Nothing
else enters frame: no people unless the prompt names the narrator, no candy,
no ribbons, no floating particles around the product, no reflections.

PRODUCT FIDELITY (non-negotiable): the JCKED bottle must match the uploaded
reference photo exactly — white bottle, white ribbed cap, label reading LIQUID /
JCKED / L-CARNITINE 4000MG / POWERED BY 5 PERFORMANCE BOOSTERS / SOUR GUMMY
WORMS. Never redraw, restyle, or re-typeset the label. Keep label shots at
medium distance; extreme close-ups of label text are handled in edit with real
photography.

TEXT: never render on-screen text, captions, or subtitles in any clip.
Captions are burned in later in edit.

WORKFLOW PER CLIP: I will paste a timestamped prompt and attach a start frame
(Frames to Video) plus the bottle photo as an ingredient when the product
appears. Generate 2 takes per clip. Keep the final frame of each take clean —
hard cuts happen in edit.

AUDIO: clips marked "generate silent" get ambient/SFX only — the narrator
voiceover is recorded separately and laid in post. Clips with quoted dialogue
keep the line word-for-word.
```

---

## Clip order (Teaser first, then full Variant B)

| # | Clip | Start frame asset | Bottle ref | Prompt source |
|---|---|---|---|---|
| 1 | Teaser beat 1 — vault gate push (4s) | `assets/stills/TEASER-H3-gate.png` | no | Pack → Teaser 3, [00:00-00:04] beat |
| 2 | Teaser beat 2 — key turns in CPT-1 lock (6s) | `assets/stills/B2-key-lock.png` | no | Pack → Teaser 3, [00:04-00:07] beat |
| 3 | Teaser beat 3 — open vault, bottle hero (8s) | `assets/stills/B4-vault-bottle.png` | YES | Pack → Teaser 3, [00:07-00:14] beat |
| 4–8 | Full cut: H3 + B1→B4 | per pack cards | B3/B4 yes | Pack → clip cards H3, B1-B4 |

## Accept/reject gate (run on every take before downloading)

1. Label legible and identical to the photo at its largest on-screen size; CPT-1 engraving crisp and correctly spelled.
2. Zero burned-in text or subtitles.
3. No people, hands, candy, or orbiting objects (unless the clip's prompt names the narrator).
4. Palette holds navy + amber; no daylight or teal drift between clips.
5. One steady camera move; no end-of-clip freeze, shimmer, or morph.
6. Clean final frame (cuts happen in edit).

## After generation

Download best takes to `remotion-pipeline/assets/clips/` named per `../jcked/clips.json` (H3.mp4, B1.mp4...). VO via ElevenLabs per the pack's narrator card. Assemble: `npm run render -- --manifest manifests/jcked-hookB.json`. Final label close-up comes from the real photo via the end-card — never from a generated frame.

## Known Flow cautions (from research, verify live)

- "Extend" may drop to older-model quality — prefer fresh Frames-to-Video per clip over chaining Extend (⚠F3).
- Image-to-video sometimes suppresses spoken dialogue — narrator clips that must speak on camera: try text-to-video with the character ingredient instead (⚠F2).
- Subtitle bug has no official fix — the prompts' NO SUBTITLES guard is best-effort; reject takes with text (⚠F1).
