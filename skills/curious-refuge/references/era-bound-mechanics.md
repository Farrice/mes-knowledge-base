# ERA-BOUND MECHANICS — VERIFY BEFORE USE

> **Quarantined on purpose.** Everything below is tool-, model- and price-specific detail lifted
> from four Curious Refuge videos dated **2026-03-20 to 2026-06-30**. Model versions, credit
> pricing, resolution ceilings, context windows and button paths move monthly — Ward himself says
> the 15-second reference window *"is going to be expanded very soon"* ([ANIME26] 17:00).
> **None of this is the craft.** The craft is in `SKILL.md` and `genius.md`.
>
> **Rule of use:** never copy a model name, price or setting from this file into live work without
> checking the current tool first. Read it to learn *what decision* the setting stood in for, then
> find that decision's current control surface.

Source keys: `[FILM26]` 2026-04-14 · `[CINE26]` 2026-03-20 · `[VOICE26]` 2026-06-23 ·
`[ANIME26]` 2026-06-30. Full source table: `source-notes.md`.

---

## 1. Tools named, and the role each played (as of Q2 2026)

| Tool | Role in his 2026 pipeline | Source |
|---|---|---|
| Midjourney | Style discovery and initial character look; *"not as good at following your specific direction"*, so he leaves it before storyboarding | [FILM26] 04:03–04:25 · [ANIME26] 03:44–03:56 |
| Nano Banana 2 / Nano Banana Pro (Google) | Direction-following image generation; character sheets; storyboard→plate conversion; lighting/grade transfer | [FILM26] 04:29–04:38, 11:16–12:08 · [CINE26] 10:06 |
| GPT-2 image model (OpenAI) | *"for creating character sheets, there's really no better tool"* (anime/painted style) | [ANIME26] 05:44–05:47 |
| Freepik | Aggregator he used in [FILM26]; spaces canvas; stock library; style presets. Explicit non-sponsorship | [FILM26] 04:42, 09:36–10:14, 10:45 |
| Magnific | Aggregator used in [VOICE26]/[ANIME26]; multi-model parallel generation; also cited as an image up-resser | [VOICE26] 02:10–02:39 · [ANIME26] 05:35 · [CINE26] 07:02 |
| Dreamina (CapCut/ByteDance) | Aggregator for Seedance access — *"it really feels like you're going directly to the source"* | [ANIME26] 10:03–10:19 |
| Adobe Firefly | Aggregator alternative; hosts Kling 2.5 Turbo | [FILM26] 06:11 · [CINE26] 12:04–12:15 |
| Krea | Aggregator alternative | [FILM26] 06:11 |
| OpenArt | Image → interactive 3D world; camera placement, focal length, character projection | [CINE26] 00:41–07:07 |
| Hilu (hiluai.video) | One-click relighting / light studio presets | [CINE26] 08:04–11:38 |
| SAM Audio (Meta) | Source separation — isolate a voice, keep sound effects and music bed. Free | [VOICE26] 08:51–10:02 · [ANIME26] 17:39–18:36 |
| ElevenLabs | Speech-to-speech voice replacement (`voice changer`) | [VOICE26] 07:24–08:24 |
| Topaz (Astra / Starlight Precise; Video AI / Proteus) | Video up-res, 1080p→4K | [FILM26] 16:50–17:30 · [ANIME26] 19:18–19:45 |
| Film Convert (Premiere / Resolve plugin) | Film stock emulation + halation | [ANIME26] 19:55–20:29 |
| Adobe Premiere / DaVinci Resolve | Editorial; Resolve favoured for colour, Premiere for suite integration; Resolve already has relighting | [FILM26] 16:15–16:36 · [CINE26] 11:50–11:57 |
| Runway + Nvidia | Announced real-time generative editing — *"it happens as you type"* | [CINE26] 14:35–15:08 |

**Video models he audition-tested by name:** Kling 3.0, Kling 2.6 (built-in voice clone), Kling 2.5
Turbo, Seedance 1.5 Pro, Seedance 2.0, Seedance 2.0 Omni, Google Veo 3.1 (rendered "VO 3.1" by ASR).
His per-shot verdicts are craft judgments, not standings — see `genius.md` Pattern 24.

---

## 2. Prompt strings, verbatim (as spoken, 2026)

**Character sheet — photoreal register** [FILM26] 06:15–06:26:
> *"create a four-panel layout of this character standing on a white background with one of the
> panels front-facing, one to the side, one behind, and then a close-up of his face"*

**Character sheet — stylised register, with style transfer** [ANIME26] 06:00–06:17:
> *"Create a dynamic character sheet of the man in image number two, in the same painting style as
> image number one. Show me the man from the front, back, and side, and have him in different
> expressions. Include one close-up of his face."*

**Board → plate, channel assignment** [FILM26] 11:40–11:50:
> *"Use the composition from image number one … and keep the character as at character number one."*

**Location plate in a locked style** [ANIME26] 08:04–08:12:
> *"Give me a painting of a restaurant near the beach in Positano. Use the same color grading and
> image style as the uploaded reference image, and make it 16 by 9."*

**Prompted coverage** [ANIME26] 11:14–11:38:
> *"Play out the following scene in this hotel lobby. Have the man in the character sheet sitting in
> a chair, and have multiple cuts as we see guests enjoying the hotel, but keep the same painted
> anime style represented in both of the uploaded images."* … closing line: *"he's at peace."*

**Rolling-reference continuation** [ANIME26] 15:28–15:34:
> *"Continue the scene using the uploaded reference footage, and keep the character of the woman as
> the woman and the man as the man."*

**Directed performance with a line reading** [VOICE26] 03:00–03:17:
> *"a handheld camera shot of a man with trepidation saying, 'So, I've been thinking a lot lately and
> I don't know if we should drink coffee anymore.'"* + *"he's having a serious conversation"* +
> *"the camera stays on the man"*

**Voice-conditioned generation** [VOICE26] 12:16–12:30:
> *"a handheld camera shot of the man in at image one"* … *"use the audio from at video number one"*

**CCR motion prompt** [CINE26] 13:16–13:24 — Camera, Character, Rig:
> *"A slow dolly arc shot from left to right of a woman talking with excitement, shot on a dolly
> track."*

*(The channel-assignment, coverage, continuation and CCR **structures** are durable and live in
`genius.md`. The `@image1` / `@video1` reference syntax and the specific phrasings are not.)*

---

## 3. Settings and numbers, all Q2 2026

- **Batch size:** raise generation count to the tool maximum (he uses 4), then press generate
  repeatedly — *"It will allow you to create essentially 16 images at a time."* [FILM26] 04:29–04:35
- **Resolution tiers:** character sheets 4K (reused asset) · plates feeding a video model 2K ·
  stylised 2D/anime motion 720 then up-res in post — 4K native motion *"can be like a dollar per
  second."* [FILM26] 06:35–06:42, 11:57–12:03 · [ANIME26] 11:50–12:07
- **Aspect:** 16:9 for film work throughout; 1:1 acceptable for character sheets. [FILM26] 05:21 ·
  [ANIME26] 06:24
- **Reference-clip window:** ~15 seconds, optionally chopped into 1-second context chunks; he
  expects it to grow. [ANIME26] 14:34–14:47, 17:16–17:27, 17:00
- **Voice reference:** ~15 seconds per emotional register (sad / excited / neutral).
  [VOICE26] 13:50–14:12
- **Cost arithmetic he ran on camera:** $3 per 15-second stylised generation × 7 generations = ~$21
  for one usable 15-second sequence ≈ **$80/min**; a 2-minute stylised short ≈ **$150–160**.
  [ANIME26] 14:51–15:12
- **Credit maths on a suite platform:** *"divide by two"* — 75 credits ≈ 37.5¢ — checked against the
  model's own published API price of 35¢, so *"not much of an upcharge."* [CINE26] 13:48–14:20
- **Up-res:** 1080p → 4K, "precise"/Proteus model, defaults left alone. [FILM26] 17:00–17:30 ·
  [ANIME26] 19:33–19:41
- **3D-world camera:** 85mm, 16:9, plus an auto-enhance pass to clean *"janky edges."*
  [CINE26] 03:36–03:48

---

## 4. Era-bound observations that will date fastest

- *"There's not a best AI video tool on the market"* [FILM26] 13:21 — true in Q2 2026, and the
  reason he works through aggregators. If a single model ever wins outright, the parallel bake-off
  (Pattern 24) becomes a cost, not a discipline.
- *"AI tools are so intelligent now that you can describe what you want to see"* [ANIME26] 09:48 —
  the multi-shot-coverage capability that retired the mandatory drawn storyboard arrived between
  April and June 2026. Verify a model still delivers usable coverage from a scene brief before
  relying on Pattern 17.
- One-click relight presets *"are actually prompt presets that sometimes can go awry"* [CINE26]
  11:33 — a statement about how those tools were built in early 2026, not a permanent property.
- The 3D-informed future [CINE26] 07:45 — a prediction, dated, not a receipt.
