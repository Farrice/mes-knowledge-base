# RUN THIS IN FLOW — JCKED Locked Vault, end to end

Everything you need is in this one file plus the `assets/stills/` folder next to it. No other docs. Follow top to bottom. Your only jobs: paste, attach, pick the better of 2 takes, download. I do the assembly.

**Answers to your two questions first:**
- **Your 7-second narrator clip is perfect.** Clips do not need to fill the 10s max — cuts happen in edit, and a clean short clip beats a padded long one. Keep it. Drop that ChatGPT narrator image into `assets/stills/` as `NARRATOR-CHATGPT.png` — it just became our official character reference (it beat the generated sheet by proving itself).
- **10s max is fine for every clip below.** Set duration to what each card says; if Flow only offers fixed lengths, pick the nearest longer one and we trim in edit.

---

## STEP 0 — Setup (5 minutes, once)

1. Go to **labs.google/flow** → sign in → **New project**, name it `JCKED Locked Vault`.
2. Settings (gear or model picker): **Veo 3.1 Quality** (not Fast), **9:16 vertical**, highest resolution shown, **2 outputs per prompt**.
3. Find **Ingredients** (or "add reference images"). Upload these 4 files from `assets/stills/`:
   - `jcked-bottle-pdp.png` ← the real bottle. This one matters most.
   - `TEASER-H3-gate.png`
   - `B2-key-lock.png`
   - `NARRATOR-CHATGPT.png` (your ChatGPT image)
   - Skip `B4-vault-bottle.png` as an ingredient — you'll use it as a start frame only (its tiny label text is mushy; the real photo carries product identity).
4. Open the sidebar assistant and paste the block in Step 1.

---

## STEP 1 — Paste this to the Flow assistant (once per session)

```
You are assisting on a performance ad production. Standing rules for every
generation in this project — never restyle or improvise beyond them:

FORMAT: 9:16 vertical, Veo 3.1 Quality, one clip at a time from the prompts I
paste. Editorial restraint: one deliberate camera move per clip, dark navy +
steel + amber palette, quiet mechanical sound design.

VISUAL LAW: the whole ad lives on one image — a locked vault and the key that
opens it. Nothing else enters frame: no people unless the prompt names the
narrator, no hands unless named, no candy, no ribbons, no floating particles,
no reflections.

PRODUCT: the JCKED bottle must match my uploaded bottle photo exactly — white
bottle, white ribbed cap, label reading LIQUID / JCKED / L-CARNITINE 4000MG /
POWERED BY 5 PERFORMANCE BOOSTERS / SOUR GUMMY WORMS. Never redraw or
re-typeset the label. Keep the bottle at medium distance; never generate an
extreme close-up of label text.

NARRATOR (when a prompt names him): match my uploaded narrator reference image
exactly — same face, same charcoal crewneck, same kitchen. Dialogue lines are
word-for-word; do not paraphrase.

TEXT: never render on-screen text, captions, or subtitles in any clip.
AUDIO: clips marked SILENT get ambient/SFX only. Clips with quoted dialogue
keep the exact line.

I will paste one prompt per clip. Generate 2 takes each. Keep final frames
clean — my cuts happen in edit.
```

---

## STEP 2 — The clips. One card = one generation. Paste, attach, generate, pick, download.

**The 3-second check on every take (reject and rerun the losing take if any fail):**
① No text/subtitles appeared. ② Bottle label matches the photo / CPT-1 spelled right. ③ Nothing entered frame that the prompt didn't name (people, hands, candy, glare).

---

### CLIP 1 — Vault gate push · 8s · SILENT · start frame: `TEASER-H3-gate.png`
Mode: **Frames to Video** (attach the gate still as first frame). Paste:

```
[00:00-00:08] Slow controlled dolly push toward a closed steel vault gate
glowing dim amber at center frame in a dark navy cell, bare matte-steel walls
receding into shadow, the small lock plate engraved CPT-1 sharpening as the
camera nears. The air is clean and still. Cool navy ambient light, one warm
amber source behind the gate. Ambient noise: low room tone, one faint heavy
metallic tick as the mechanism engages. The corridor is empty — no people,
no hands. Matte steel free of glare, landscape free of reflections.
NO SUBTITLES. No captions. No on-screen text. 9:16.
```
Download the better take as **`H3.mp4`**

---

### CLIP 2 — Key turns by itself · 8s · SILENT · start frame: `B2-key-lock.png`
Mode: **Frames to Video**. Paste:

```
[00:00-00:04] Locked-off macro: a brass key seated in a heavy matte-steel lock
engraved CPT-1 on a dark vault door, warm amber light catching the key's teeth
against deep navy shadow. The key rotates slowly by itself, untouched, as if
unlocked from within.
[00:04-00:08] A razor-thin line of warm light spills from the door seam and
widens to a glowing slit as the door cracks open millimeters. Ambient noise:
metal-on-metal friction as the key turns, a low creak as the seam opens.
The frame stays empty of people and hands throughout. Matte steel free of
glare and reflections. NO SUBTITLES. No captions. No on-screen text. 9:16.
```
Download as **`B2.mp4`**

---

### CLIP 3 — Open vault, bottle reveal · 8-10s · SILENT · start frame: `B4-vault-bottle.png` + bottle photo as ingredient
Mode: **Frames to Video**, and ALSO attach `jcked-bottle-pdp.png` as an ingredient so the label stays true. Paste:

```
Using the provided bottle photo for the product, keep the label exactly as
shown, never restyled. [00:00-00:05] Wide composed shot: a heavy steel vault
door stands fully open onto warm amber light, the JCKED bottle centered alone
on a dark matte pedestal in the doorway, empty space around it. The camera
begins one slow hero dolly push toward the bottle. [00:05-00:10] The push
settles with the bottle at medium distance, label square to camera and
readable, the vault interior glowing warm behind it. Ambient noise: low
ambient tone, a sparse low pulse rising under the final hold, then
near-silence. No people, no candy, no floating objects, no reflections.
NO SUBTITLES. No captions. No on-screen text. 9:16.
```
Download as **`B4.mp4`**

---

### CLIP 4 (optional, the talking hook — your ChatGPT narrator) · 8s · DIALOGUE · ingredient: `NARRATOR-CHATGPT.png`
Mode: **Ingredients to Video** (text-to-video with the narrator image attached — NOT frames-to-video, which can mute speech). Paste:

```
Using the provided image for the narrator: same face, dark crewneck, neutral
kitchen, warm light on one side of his face, deep navy shadow on the other.
Phone-native handheld take at eye level, authentic micro-shake. He stands
still, hands at his sides, and says to camera, calm and level, no smile:
"You can do everything right and still carry the same fat for years. The
effort was never the problem. That fat is locked." On the last word, hard cut
to a closed amber-lit steel vault gate filling the frame. Ambient noise:
quiet kitchen room tone under his voice only, no music.
NO SUBTITLES. No captions. No on-screen text. 9:16.
```
Download as **`H1.mp4`** — if his voice sounds off across takes, tell me; we swap to the recorded-VO route.

---

### CLIP 5 (optional, second hook for the test-plan story) · 8s · DIALOGUE · ingredient: `NARRATOR-CHATGPT.png`
Same mode as Clip 4. Paste:

```
Using the provided image for the narrator: same face, dark crewneck, same
kitchen, warm light on one side of his face, a touch more contrast and pace.
Phone-native handheld take at eye level. He leans slightly forward and says
to camera with more edge, flat, no smile: "You took the right supplement at
the wrong dose. Five hundred milligrams. The research that worked went up to
four thousand." Hard cut on the last word to two brass keys side by side on
dark steel: a short stub key and a full-length key, camera pushing onto the
full-length key. Ambient noise: kitchen tone under his voice, quiet studio
tone on the key beat, no music. NO SUBTITLES. No captions. No on-screen
text. 9:16.
```
Download as **`H4.mp4`**

---

## STEP 3 — Hand back to me

Drop whatever you downloaded into:
`projects/trendscale-trial/03-video-samples/remotion-pipeline/assets/clips/`

Then tell me which clips you got. I take it from there: VO track, captions in Inter Tight with the amber accents, music bed, the silence close, and the real-photo end-card that makes the label scrub-proof. You review one finished file.

**Total Flow generations: 3 required + 2 optional = 6-10 takes. Zero Higgsfield credits.**
