# AI Video Realism & Production Intelligence (2025–2026)
**For:** Trendscale creative-strategist final round — Google Flow (Veo 3.1) + Higgsfield + frontier models
**Compiled:** 2026-07-11 · WebSearch/WebFetch + internal Recall only · $0 budget
**Confidence keys:** VERIFIED = primary source (Google/OpenAI/DeepMind official) · LIKELY = single/practitioner source or reasonable inference · UNCONFIRMED = flagged gap

> **The one thing to internalize:** In mid-2026 there is no single "best" model — the pros run a **relay**, not a workhorse. Veo 3.1 for photoreal + native audio, Kling 2.6/3.0 for the talking human, GPT Image 2 / Seedream for the start frame with legible product text, then a color-grade + grain + loudness finishing pass that is what actually makes an AI ad read as "real." Amateurs pick a model. Operators pick a pipeline and hide the seams.

---

## Q1 — Veo 3.1 / Google Flow prompting structure

### RULES (copy-paste usable)
- **Order the prompt exactly:** `[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`. Veo reads structure literally, so front-load the camera. (VERIFIED)
- **Write flowing cinematic prose, not JSON** — Google's own examples are single dense paragraphs. Use structure as a *checklist you fill in prose*, not literal key-value fields. (VERIFIED for prose; JSON "measurably better" claim is UNCONFIRMED — no Google source supports it; practitioners split.)
- **Dialogue:** wrap the exact spoken line in quotes: `A woman says, "We have to leave now."` Keep it to what fits in ~8 seconds of speech. (VERIFIED)
- **SFX:** label with a colon: `SFX: thunder cracks in the distance`. (VERIFIED)
- **Ambient:** `Ambient noise: the quiet hum of a starship bridge`. (VERIFIED)
- **Negative prompts — describe the absence, never command "no":** write `a desolate landscape with no buildings or roads`, NOT `no man-made structures`. Veo handles descriptive exclusion; it fumbles imperative negation. (VERIFIED)
- **Subtitle prevention (the real problem):** Google ships **no official fix** and the burned-in-caption bug persisted for months post-launch even when users explicitly asked for none. Practitioner mitigations that reduce (not eliminate) it: (a) strip apostrophes/quotation marks from any on-camera phrase, (b) append repeated `NO SUBTITLES. No captions. No text overlay.`, (c) format as `Character says (no subtitles): welcome to our channel`. Budget a bottom-crop or inpaint pass as backstop. (LIKELY — practitioner consensus; MIT Tech Review VERIFIED the bug persists.)
- **Camera vocabulary Veo actually honors:** dolly shot, tracking shot, crane shot, aerial view, slow pan, POV shot; wide/close-up/extreme close-up/low angle/two-shot; shallow depth of field, wide-angle lens, soft focus, macro lens, deep focus. (VERIFIED)
- **Image-to-video / start frame:** generate the still (Gemini 2.5 Flash Image / "Nano Banana"), then use Flow's **"First and Last Frame"** and describe the transition in the Veo prompt. Note: in image-to-video mode Veo historically suppresses dialogue (SFX sometimes, speech rarely). (VERIFIED structure; dialogue-suppression LIKELY per Recall/Kling-comparison card.)
- **Ingredients (character + product consistency):** upload up to **3 reference images** via "Ingredients to Video"; reference them in prose: `Using the provided images for the character and the bottle, create...`. This is the native lever for holding a face/product across clips. (VERIFIED)
- **Extend beyond 8s:** use **Flow Scene Builder**, not raw text-to-video. Each hop adds ~7s up to ~20 extensions (~148s ceiling). On Veo 3.1, Extend + Frames-to-Video retain full Veo-3 quality and native audio. (LIKELY — see contradiction note below.)
- **Specs:** resolution 720p or 1080p; aspect 16:9 or 9:16; clip length 4/6/8s; all outputs carry SynthID watermark. Add/Remove-Object still runs on Veo 2 and generates no audio. (VERIFIED)

### Receipts
- Prompt formula, dialogue/SFX/ambient syntax, negative-prompt rule, camera vocab, Ingredients, specs: [Google Cloud — Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) (VERIFIED)
- Element ordering (framing→style→lighting→character→location→action→dialogue): [Google DeepMind — Veo prompt guide](https://deepmind.google/models/veo/prompt-guide/) (VERIFIED)
- Subtitle bug persistence: [MIT Technology Review, 2025-07-15](https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/) (VERIFIED); mitigation syntax: [Yapper](https://yapper.so/articles/remove-veo3-subtitles) (LIKELY)
- Scene extension mechanics: [aifreeapi extension guide](https://www.aifreeapi.com/en/posts/veo-3-extend-video-length) + [practitioner @ai.for.real.life TikTok](https://www.tiktok.com/@ai.for.real.life/video/7527744980409011511) (LIKELY)
- Ingredients (3 ref images) + first/last frame confirmed by practitioner: Recall card "Master Google VEO 3.1" ([GenHQ](https://www.youtube.com/watch?v=O8-vsMM8hSI)) (LIKELY)

---

## Q2 — UGC realism levers

### RULES
- **Add handheld micro-shake — highest-impact single trick.** Default AI camera is tripod-smooth; real phone footage wobbles. Prompt: `handheld smartphone footage, slight micro-shake, imperfect framing, subject slightly off-center`. (LIKELY)
- **Grain is the biggest "is-it-real" lever, and it is applied in post, not prompt.** AI frames have zero sensor noise; that absence is the tell. Add DaVinci/Premiere film grain at ~2–3%, or a grain overlay at 20–40% opacity. (LIKELY)
- **Override the three AI defaults explicitly:** (1) glossy even lighting → `messy natural light, one side of the face darker, hot window blowout`; (2) staged clean background → `real cluttered room, off-center plant, slight mess`; (3) retouched skin → `natural skin texture, visible pores, faint shine, no plastic skin, slightly imperfect skin`. (LIKELY)
- **Cast against the "AI-beautiful" tell:** specify age, ethnicity, non-model features, unremarkable styling. Beauty-default faces read as synthetic; ordinary faces read as UGC. (LIKELY)
- **Direct the delivery, not just the words:** `natural pauses as she speaks, occasional filler words, imperfect diction, all real motion, no robotic gestures`. (LIKELY)
- **Correct hand anatomy explicitly** in the positive prompt: `correct hand anatomy, realistic inertia, no extra fingers, no warping logos`. Hands remain the #1 artifact. (LIKELY)

### Telltale AI artifacts reviewers catch (and prompt-side mitigations)
- **Hands/fingers** (extra digits, morphing) → state hand anatomy positively; frame to keep hands out or still; regenerate.
- **Teeth** (too uniform/too many) → avoid wide open-mouth laughs; shorter dialogue.
- **Hair & fabric physics** (unnatural float) → Kling 3.0 handles hair/liquid/fabric best if the shot demands motion.
- **In-scene text/logos** (garbled) → never trust the video model to render product text; bake legible text into the **start frame** with GPT Image 2 / Seedream, then animate.
- **Lip-sync drift** → keep dialogue short; or go silent-video + external lip-sync (Q5).
- **Burned-in subtitles** → see Q1.

### Receipts
- Handheld/grain/lighting/skin levers: [MagicHour — Realistic AI Video Prompting 2026](https://magichour.ai/blog/realistic-ai-video-prompting) + [Invideo — film grain & blur for AI realism](https://invideo.io/faq/does-adding-film-grain-and-blur-to-ai-generated-video/) (LIKELY)
- JSON-style UGC casting fields + "no plastic skin" + delivery direction: [Medium/No Time — UGC ads that don't look like AI](https://medium.com/no-time/how-to-create-ugc-style-ads-with-ai-that-dont-look-like-ai-complete-workflow-e8f01344dcba) (LIKELY)

---

## Q3 — Higgsfield

### RULES
- **Keep prompts 1–3 sentences. Short beats long.** Higgsfield responds to direct commands, not descriptive paragraphs. A focused 2-sentence prompt outperforms a vague block. (LIKELY)
- **Separate image / identity / motion into distinct instructions.** The #1 failure is one block that mixes camera + character + motion → unstable framing, shifting faces, broken movement. (LIKELY)
- **For a repeatable talking human, train a Soul ID:** upload 3–5 reference photos, train ~5–10 min; that character is then available across all Higgsfield tools with a face that holds across clips. (LIKELY)
- **Product fidelity workflow:** generate the product image first; for simple motion feed one image + short prompt; for complex motion generate a **Start Frame + Final Frame** and feed both stills + a detailed prompt. (LIKELY)
- **Most photoreal talking human:** practitioner + Higgsfield's own guidance point to **Kling 3.0** (available inside Higgsfield) as the most reliable talking-head/spokesperson model with identity held across cuts. (LIKELY)

### Known break-points (partial)
- Multi-person identity consistency degrades — faces/proportions drift across frames with >1 subject. (LIKELY)
- Generation hard-fails cluster around: upstream provider error, unsupported file/oversize, IP block, NSFW false-positive, payment. (LIKELY)
- **UNCONFIRMED:** the specific claims that reflections, >2 humans, or mid-clip location changes reliably break Higgsfield — I could not verify these against a primary/authoritative Higgsfield source (the target doc 404'd). Treat as folklore until tested; recommend a quick empirical check before betting a shot on it.

### Receipts
- Prompt length + separation + Soul ID + start/final frame: [Segmind — Higgsfield prompt format guide](https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/) + [Higgsfield — beginner guide](https://higgsfield.ai/blog/how-to-make-ai-videos-beginners-guide) (LIKELY)

---

## Q4 — Character + product consistency across a multi-clip ad

### RULES (what actually works, per model)
- **Veo 3.1 (Flow):** hold consistency with **Ingredients** (same 3 reference images — narrator face + product — in every clip) AND **start-frame chaining** via Scene Builder (save last frame of clip N → Frames-to-Video seed for clip N+1). Neither is magic alone; combine them. (LIKELY/VERIFIED-feature)
- **Repeat the full description every single clip.** The model has no memory between extensions — re-state character, outfit, hair, lighting, environment, AND audio each time or you get skin-tone/wardrobe drift. This is the most-cited consistency rule across sources. (VERIFIED — practitioner consensus + Google Scene Builder behavior)
- **Higgsfield:** Soul ID is the strongest identity lock (trained model, not per-prompt reference). Best for the narrator. (LIKELY)
- **Kling 2.6/3.0:** native multi-shot storyboard mode holds subject identity across cuts with a shared audio timeline — purpose-built for exactly this. (LIKELY)
- **Seed reuse:** helps marginally within a model but does NOT survive model-switching; don't rely on it as the primary lever. (LIKELY)
- **Product text/label:** lock it in the still (GPT Image 2 / Seedream), then image-to-video — never re-generate the label inside each video clip. (LIKELY)

### Receipts
- "Repeat everything each extension / skin tone shifts otherwise": [aifreeapi](https://www.aifreeapi.com/en/posts/veo-3-extend-video-length) + practitioner TikTok above (VERIFIED behavior). Kling multi-shot storyboard: [AI Magicx April 2026 comparison](https://www.aimagicx.com/blog/veo-3-vs-kling-3-vs-sora-2-april-2026-comparison) (LIKELY).

---

## Q5 — VO + lip-sync pipeline

### RULES
- **Three viable stacks, ranked by use case:**
  1. **Veo 3.1 native dialogue** — best when the whole clip is generated in Flow and you want zero post. Cost: dialogue is a "slot machine" (sometimes no audio, sometimes tiny/robotic voice — much improved in 3.1 but still limited voice control), capped at 8s of speech, and prone to burned-in subtitles. Use for short single-line UGC beats. (VERIFIED slot-machine behavior via Recall; LIKELY on 3.1 improvement)
  2. **Silent video + ElevenLabs VO + external lip-sync** (Creatify Aurora / Higgsfield lip-sync / Kling) — best voice quality and full control; lip-sync tools extend to ~60s vs Veo's 8s. Cost: +18–60 min manual sync per clip. This is the pro choice when the voice must be consistent and directed across many clips. (VERIFIED tradeoff)
  3. **HeyGen avatar** — full pipeline (generate → dub → lip-sync → deliver) in ~2 min, 175+ languages with accurate lip-sync. Cost: the "avatar" look is more corporate-explainer than candid UGC; less cinematic. Use for talking-head/spokesperson, not gritty UGC. (VERIFIED)
- **For a narrated multi-clip ad with ONE consistent narrator voice: use ElevenLabs for the VO across all clips** (single voice = zero drift), generate video silent, lip-sync per clip. Native per-clip Veo voices will NOT match each other. (LIKELY — strong inference from consistency evidence)
- **Watch script length:** ElevenLabs voice consistency degrades past ~2 min (tonal drift, odd pauses) — split long scripts and stitch. (LIKELY)

### Receipts
- Veo "slot machine" audio / no-dialogue-in-i2v: Recall cards [Theoretically Media](https://www.youtube.com/watch?v=gWkhUd-LWTs), [Kling 2.1 vs Veo](https://www.youtube.com/watch?v=HZRUalAExhs) (VERIFIED). ElevenLabs vs HeyGen tradeoffs + 60s lip-sync via Creatify Aurora: [HeyGen comparison blog](https://www.heygen.com/blog/heygen-vs-elevenlabs-vs-rask-ai-vs-dubverse) + Recall card [JgxVyB9M62I](https://www.youtube.com/watch?v=JgxVyB9M62I) (VERIFIED/LIKELY).

---

## Q6 — Assembly / finishing that sells realism

### RULES
- **Grade every clip to one look.** Clips from different models (Veo/Kling/GPT-Image start frames) arrive with different color science — apply a unifying grade (matched white balance + LUT) in DaVinci/Premiere so the cut doesn't betray the model-switching. (LIKELY)
- **Add grain last, globally, over the whole timeline** at ~2–3% (or overlay 20–40% opacity) so mixed-source footage shares one texture — this is the single strongest post move for realism. (LIKELY)
- **Loudness:** master to **-14 LUFS with a true-peak limiter at -1 dBTP** as the safe default. IG/TikTok run hotter (~-12 to -10 LUFS), Facebook ~-13, YouTube -14. Compress VO 4:1–6:1 so it survives phone speakers; keep the music bed clearly under the VO. Always check on an actual phone speaker. (LIKELY)
- **Captions for Meta 9:16 (1080×1920):** keep all burned-in captions/CTAs inside the **center safe zone (~pixels 250–1248)**; top 14% (270px) and bottom 35% (670px) are covered by UI (profile, likes, CTA, caption). Silent-autoplay means captions are effectively mandatory. (LIKELY)
- **Upscale pass:** finish through Topaz Video (or Higgsfield/Kling native upscale to 2K/4K) before delivery — cleans compression mush and adds perceived production value. (LIKELY; Topaz specifics UNCONFIRMED from a primary source this pass.)

### Receipts
- -14 LUFS / -1 dBTP / platform variance / phone-speaker check: [Critical Listening Lab — social loudness](https://www.criticallisteninglab.com/en/learn/loudness/social-media) + [MightyVO](https://mightyvo.com/how-to-maximize-audio-for-social-media-ads/) (LIKELY). Meta safe zones 9:16: [Billo — Meta Ads Safe Zones 2026](https://billo.app/blog/meta-ads-safe-zones/) + [Lucid Media](https://www.lucidmedia.co.nz/blog/instagram-facebook-ad-safe-zones-2026/) (LIKELY).

---

## Q7 — Best-model ranking (mid-2026), by job — winners named

| Job | Winner | Runner-up | Evidence / caveat |
|---|---|---|---|
| **(a) Photoreal talking-human UGC + dialogue** | **Kling 2.6 / 3.0 Omni** | Veo 3.1 | Kling wins spokesperson "by a clear margin"; 3.0 Omni leads native audio + lip-sync in 5 languages + shared audio timeline across cuts. Veo more photoreal but weaker micro-expression/gesture timing. (LIKELY) |
| **(b) Cinematic product / mechanism b-roll** | **Veo 3.1** | Kling 3.0 / Sora 2 Pro | Veo 3.1 = best photorealism, prompt adherence, native audio, 4K in portrait+landscape. Sora 2 Pro is arguably most photoreal cinematic but **risky**: web/app shut down 2026-04-26, API only to Sept 2026 — don't build a long project on it. (LIKELY) |
| **(c) Start-frame still w/ legible in-scene text** | **GPT Image 2** | Seedream 4.5 / Ideogram v3 | GPT Image 2 measurably best on dense/small text + tops the Image Arena (largest 1st-to-2nd gap recorded). Seedream 4.5 = text + native 4K + product looks. Nano Banana Pro = cheapest true-4K. Imagen 4 Ultra = most photoreal skin but not the text king. (LIKELY) |
| **(d) Image-to-video fidelity (holds source identity)** | **Seedance v1.5 Pro / Kling 3.0** | Veo 3.1 | Seedance + Kling 3.0 lead style/identity preservation from a source still for client work; teams draft on Wan/Kling 2.5 Turbo, finish on Seedance/Kling 3.0. (LIKELY) |

**Higgsfield's place:** an aggregation layer — it hosts Kling/Soul rather than fielding a category-winning base model; its edge is Soul ID identity-lock + preset motion, not raw fidelity. (LIKELY)

### Receipts
- [Lushbinary — Sora 2 vs Veo 3.1 vs Kling comparison](https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/); [Curionic — I tested every major AI video generator 2026](https://www.curionic.net/2026/06/runway-vs-kling-vs-veo-vs-sora-ai-video-generator-comparison-2026.html); [AI Magicx April 2026](https://www.aimagicx.com/blog/veo-3-vs-kling-3-vs-sora-2-april-2026-comparison) (all LIKELY — third-party aggregators, not vendor-primary; treat rankings as directional). Image models: [Atlas Cloud](https://www.atlascloud.ai/blog/guides/best-ai-image-generation-models-2026) + [llm-stats image leaderboard](https://llm-stats.com/leaderboards/best-ai-for-image-generation) (LIKELY). I2V: [Atlas Cloud I2V guide](https://www.atlascloud.ai/blog/guides/ai-image-to-video-models-compared) (LIKELY).

---

## Q8 — Timestamp / beat-structured prompting (real syntax, not folklore)

### RULES
- **Veo 3.1 — YES, honors bracketed timestamps.** Google's official guide ships a verbatim multi-shot example using `[00:00-00:02] ... [00:02-00:04] ...` with SFX and Emotion tags per beat. This measurably improves multi-shot control in a single 8s generation. **Use timestamps in Veo templates.** (VERIFIED)
- **Sora 2 — NO parseable brackets; uses prose beats + descriptive time labels.** OpenAI's cookbook structures action "in beats or counts" (`takes four steps to the window, pauses, and pulls the curtain in the final second`) and uses labels like `0.00–2.40 — "Arrival Drift"` as **director's notes, not API syntax**. Community guides push `[0–3s] CUT 1` shot-lists and report timestamps as "the most powerful control tool," but that's practitioner practice layered on prose, not an official parser. **Strip literal brackets for Sora; keep beat-based prose.** (VERIFIED that official = prose beats; LIKELY that bracket shot-lists still help.)
- **Kling 3.0** — has a native multi-shot storyboard mode (shot list with per-shot camera/action + shared audio timeline) rather than in-prompt timecodes; sequence via the storyboard UI. (LIKELY)
- **Flow Scene Builder** — timing is handled on a **timeline of chained clips**, not timecodes inside one prompt; each ~7s hop is its own fully-described prompt. (LIKELY/VERIFIED-feature)
- **Universal rule:** describe action in *beats/counts* ("takes three steps, pauses, lifts the bottle") regardless of model — every source agrees beat-based action beats vague continuous description. (VERIFIED across Google + OpenAI)

### Receipts
- Veo timestamp syntax verbatim: [Google Cloud Veo 3.1 guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) (VERIFIED). Sora beats vs brackets: [OpenAI Cookbook — Sora 2 prompting guide](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) (VERIFIED). Community bracket shot-lists: [The AI Video Creator cheatsheet](https://www.theaivideocreator.ai/p/sora-2-prompting-cheatsheet) (LIKELY). Modular camera/action/audio/text checklist confirmed by practitioner: Recall card [rzmjA17MjTk](https://www.youtube.com/watch?v=rzmjA17MjTk) (LIKELY).

---

## (a) Canonical Veo 3.1 prompt TEMPLATES (annotated)

### Template 1 — Dialogue UGC clip (9:16, 1080p, 8s) — TIMESTAMPED (Veo honors this)
```
[00:00-00:03] Handheld selfie-style smartphone shot, a 32-year-old woman with
  natural skin texture and visible pores, no makeup gloss, holding the [PRODUCT]
  bottle slightly off-center in a cluttered sunlit kitchen. Messy natural window
  light, one side of her face brighter. She glances at the label, then to camera.
[00:03-00:08] She says, "honestly I did not think this would work." Natural pauses,
  slight micro-shake in the framing, imperfect diction, real hand movement, correct
  hand anatomy. Retain her exact face and the exact bottle from the provided images.
Ambient noise: quiet kitchen room tone, faint street sound.
Style: authentic iPhone footage, candid, not cinematic. No plastic skin.
NO SUBTITLES. No captions. No on-screen text.
```
**Field notes:** `[00:00-00:03]` = Veo-honored beat brackets · handheld/off-center/natural-light/pores = realism levers · quoted line = dialogue that fits <8s · `provided images` = Ingredients for face+product lock · `Ambient noise:` colon syntax · `NO SUBTITLES` repeated = the imperfect-but-best caption mitigation · strip the brackets ONLY if porting to Sora.

### Template 2 — Cinematic product / mechanism b-roll (16:9 or 9:16, 1080p, 8s) — TIMESTAMPED
```
[00:00-00:03] Slow dolly-in, extreme close-up of the [PRODUCT] on a wet slate
  surface, shallow depth of field, single hard key light from camera-left, cool
  rim light behind. Condensation beads catch the light.
[00:03-00:06] Macro tracking shot across the label (text pre-rendered in the start
  frame), droplet rolls down the glass. Deep, rich color, premium commercial grade.
[00:06-00:08] Crane pull-back revealing the product centered on a dark reflective
  set, subtle volumetric haze.
SFX: soft glass tap, a low cinematic swell.
Ambient noise: quiet studio room tone.
Style: high-end product commercial, shot on cinema prime lens, slightly filmic grain.
```
**Field notes:** camera terms are the exact vocab Veo honors · **label text lives in the start frame (GPT Image 2/Seedream), NOT prompted here** · `SFX:` colon syntax · no dialogue = no subtitle risk · feed via image-to-video (First/Last Frame) for label fidelity.

---

## (b) Top 10 realism levers, ranked by impact
1. **Handheld micro-shake** (prompt) — kills the tripod-smooth tell. (LIKELY)
2. **Film grain in post, over the whole timeline** — the absence of sensor noise is the #1 giveaway. (LIKELY)
3. **Legible in-scene text baked into the start frame, not the video model.** (LIKELY)
4. **Messy natural lighting** (one side darker, window blowout) vs default soft even light. (LIKELY)
5. **Non-model casting + imperfect skin** ("no plastic skin, visible pores"). (LIKELY)
6. **Consistent color grade across all clips** to hide model-switching. (LIKELY)
7. **Short dialogue + external ElevenLabs VO** for one consistent voice and clean lip-sync. (LIKELY)
8. **Explicit hand-anatomy positive prompt** + framing hands out/still. (LIKELY)
9. **Loudness master -14 LUFS / -1 dBTP**, VO above bed, phone-speaker check. (LIKELY)
10. **Cluttered imperfect environment** vs staged studio-clean background. (LIKELY)

---

## (c) Contradictions & unknowns (not smoothed over)
- **JSON vs prose for Veo:** Google's official examples are prose; no Google source claims JSON is "measurably better." Practitioner "modular/structured" advocates exist but it's checklist-in-prose, not literal JSON. **Prose is canonical; JSON is unproven.** (Google VERIFIED prose; JSON superiority UNCONFIRMED.)
- **Does Flow "Extend" use Veo 3 or Veo 2?** Older practitioner guidance: the basic Extend button ran Veo 2 Fast (no audio, lower quality) and you had to use Frames-to-Video for Veo-3 quality. Newer (Veo 3.1) sources say Extend now retains full Veo-3 quality + audio. **Likely version-drift — verify live in Flow before relying on Extend for a hero clip.** (contradiction, both LIKELY.)
- **Higgsfield break-points (reflections / >2 humans / location change):** UNCONFIRMED from an authoritative source; only general multi-person identity drift is documented. Test empirically.
- **Sora 2 availability:** web/app reportedly shut 2026-04-26, API to ~Sept 2026. If true, Sora 2 is a **short-runway** choice — do not architect the deliverable around it. Verify current status before proposing it to Trendscale. (LIKELY, single-thread — verify.)
- **Best-talking-human model:** sources split Kling (spokesperson/lip-sync) vs Veo 3.1 (photoreal) vs Sora 2 (micro-expression). Reality: **test the actual product/face on both Kling 3.0 and Veo 3.1 and pick per-shot** — the ranking is close enough that your specific footage decides it.
- **Platform LUFS:** -14 is the safe master, but IG/TikTok normalize hotter; there is no single official Meta LUFS spec published — treat -14/-1dBTP as a floor and trust the phone-speaker check.
- **Model landscape is weeks-fresh:** Kling 3.0, Seedream 4.5, GPT Image 2, Nano Banana Pro all shifted through 2026. Re-verify the winner table before a final pitch — rankings here are directional (aggregators, not vendor benchmarks).

---
*Primary sources (VERIFIED tier): Google Cloud Veo 3.1 guide, Google DeepMind Veo prompt guide, OpenAI Sora 2 cookbook, MIT Technology Review. Practitioner/aggregator (LIKELY tier): Higgsfield/Segmind, MagicHour, Invideo, HeyGen, Atlas Cloud, AI Magicx, Curionic, Critical Listening Lab, Billo. Internal: 20 Recall cards on Veo/Kling/Higgsfield/UGC prompting.*
