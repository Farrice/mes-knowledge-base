# Era-Bound Mechanics (2025-03 → 2026-07) — VERIFY BEFORE USE

> **Quarantine notice.** Everything on this page is tool-, model- and version-specific and was already
> churning *inside* the 16-month source window. Nothing in `SKILL.md`, `genius.md`, the workflows, or
> any execution prompt depends on a single line of it. If a deliverable from this skill breaks when
> the stack changes, the deliverable was wrong.
>
> Recorded 2026-08-02 from five watched sources. **Treat every name and number below as a dated
> observation, not a recommendation.** Re-verify before acting.

## Why this page exists at all

The churn is the argument. Over five sources spanning sixteen months, the *method* never changed —
dataset → captions → bake → controlled generation — while the entire model roster turned over twice:

| Date | Dataset/edit model | Character bake target | Video/control model |
|---|---|---|---|
| 2025-03-07 | — (FLUX LoRAs, SDXL + IP-Adapter alternative) | FLUX Dev | Kling (interpolation), regional hooks |
| 2025-07-17 | — | — | Wan 2.1 VACE, ATI trajectory model |
| 2025-10-07 | Qwen Image Edit | Wan 2.1 (for 2.2 compat) | Wan 2.2 |
| 2026-03-30 | Qwen Image Edit / Nano Banana | — | SkyReels V3 R2V + Wan 2.1 VACE merge, SAM 3 |
| 2026-07-17 | Flux 2 Klein | Krea 2, Ideogram 4, Wan 2.1/2.2 | Wan 2.2 |

Four of the five "current best" models named in 2025 were not the recommendation by 2026. The five
dataset rules were identical throughout.

## Platform / environment (constant across all five sources)

- **ComfyUI** — node-based local runner; every workflow ships as a drag-and-drop JSON.
  Setup ritual, unchanged in all five sources: drop JSON → Manager → *Install Missing Custom Nodes* →
  select all → install → restart → download models from the note nodes beside each loader → `R` to
  refresh → re-select in the loader.
- **Blender** — 3D layout, rigging (Rigify), camera blocking, depth/mat-ID export, greybox geometry.
- **After Effects / Nuke / Fusion** — roto, masks, tracking, final composite. He uses AE for the Roto
  Brush specifically.
- **RunPod** — rented GPU for LoRA training. Observed pricing 2026-07: RTX 5090 ≈ $1/hr; he used an
  RTX 6000 Pro. 2025-10: ~$4 total for one Wan LoRA. Affiliate link in descriptions.
- His own hardware, stated: **RTX 4090** (2025-10, 2026-03).
- **GGUF quantisation** — "grab the version that comfortably fits on your GPU's VRAM." He shot an
  entire 2025 masterclass on Q5 to demonstrate the quality floor.
- **SageAttention** — "halves your generation time without any noticeable quality loss"; he ships a
  Windows installer (2026-03).
- **Nvidia RTX Super Resolution** — 720p → 4K upscale path (2026-03).

## Models named, by source date

**2025-03-07 (Blender + ComfyUI multi-character):** FLUX Dev · FLUX 8-step LoRA · ControlNet Union
(InstantX) · Juggernaut XL + ControlNet Promax + IP-Adapter Plus (no-training path) · SAM 2 ·
Florence 2 · Hunyuan3D-2 (portable + Kijai wrapper) · Tripo AI · TRELLIS · Kling (frame-to-frame
interpolation, relevance ≈ 0.7) · ElevenLabs voice changer · MMAudio · Flux Gym · 360 HDR LoRA.

**2025-07-17 (controllable characters in footage):** Wan 2.1 VACE (chosen over the ATI trajectory
model because VACE also accepts reference images) · OpenPose ControlNet · Spline Path Control v2
(whatdreamscost) · AE and Blender trajectory export scripts he generated with Claude.

**2025-10-07 (hyperrealistic masterclass):** Qwen Image Edit (open) vs Seedream 4 / Nano Banana
(closed, "heavily censored… can get expensive") · FLUX + USO for consistency-preserving upscale ·
4x-UltraSharp · Wan 2.1 trained / Wan 2.2 used · LightX2V speed LoRAs · AI Toolkit (Ostris) ·
Flux Gym via Pinocchio.

**2026-03-30 (VFX pipeline):** model merge by **Inner Reflections** combining **SkyReels V3 R2V**
(reference-image identity, up to 4 refs) with **Wan 2.1 VACE** (inpaint/outpaint + ControlNets) —
each covers the other's stated weakness · SAM 3 (Meta) auto-masking · Qwen Image Edit (local start
frames) · Nano Banana (optional paid start frames) · Wan Lenovo realism LoRA.

**2026-07-17 (interacting characters):** **Flux 2 Klein** (dataset generation) · **Krea 2 RAW/Turbo**
(his newcomer recommendation: "light on your computer, pretty fast, good prompt adherence, good
community support") · **Ideogram 4** (open-weight, gated licence, bounding-box prompting via JSON) ·
**Wan 2.2 / 2.1** (video; trains on images only) · **Qwen3-VL** (captioning) · **SeedVR2** (2K
upscale) · AI Toolkit by **Ostris** (alternatives: Musubi Tuner for low VRAM, OneTrainer) ·
LightX2V LoRA · RES4LYF samplers.

## Numbers he stated (dated, not laws)

| Setting | Value | Source | Note |
|---|---|---|---|
| LoRA rank, one character | 16–32 | 2026-07-17 | "we could go lower… I think we could do 16" |
| LoRA rank, three characters | 64 | 2026-07-17 | scaled up for cast size |
| Training steps run | 3,000 | 2026-07-17 | deliberately overshoots to sample |
| Best checkpoint, Krea 2 | ~1,250–2,000 | 2026-07-17 | "at least in my experience" |
| Best checkpoint, Ideogram 4 | ~2,000–2,250 | 2026-07-17 | 3,000 "a little overbaked" |
| Best checkpoint, Wan | 2,500 | 2026-07-17 | tested across versions |
| Checkpoint save interval | 250–500 steps | 2025-10, 2026-07 | so there's something to sample |
| Training time | ~80–90 min | 2025-10, 2026-07 | on rented high-end GPU |
| Sample frames during video-model training | set to 1 | both | else it renders video demos and crawls |
| Video length ceiling | 81 frames (Wan 2.1) / 121 frames ≈ 5s (2026 VFX) | — | advanced workflows chunk + stitch |
| Preview-shop steps | 2 | 2025-07-17 | then finish at 8 |
| Speed-LoRA sampler split | 8 steps total, first sampler stops at 3, CFG 1 | 2025-10-07 | vs. 30 steps unaccelerated |
| Consistency-upscale start step | 18 of 20 = minimal change; 12–13 = more detail | 2025-10-07 | the identity/detail dial |
| SDXL denoise sweet spot | 0.35–0.40 | 2025-03-07 | texture-fix pass |
| Max VFX resolution | 720p | 2026-03-30 | then RTX super-res to 4K |
| Kling relevance | 0.7 | 2025-03-07 | "so it more closely follows the images" |

## Recurring era-bound gotchas

- **Quantised models double poses** in generated turnaround sheets (2025-10) — he shrugs, because the
  poses are generated individually later anyway.
- **Interpolation models add mouth movement to any face** — negative-prompt "talking, screaming"
  (2025-03).
- **Ideogram bounding-box JSON looks rotated and is correct** — LLMs will "fix" it and break it; tell
  the LLM it's correct (2026-07).
- **Ideogram 4 is a gated model** — Hugging Face account + accepted licence + read token pasted into
  the trainer (2026-07).
- **Speed LoRAs cost hand quality** — bypass the speed LoRA and raise steps when hands matter
  (2025-03).
- **Custom node packs sometimes fail to install first time** — retry, select the last version
  (2025-07).

## Ideas that are era-bound in implementation but durable in principle

Promoted to `genius.md`; listed here so nobody mistakes the mechanism for the idea.

| Era-bound mechanism | Durable principle (see genius.md) |
|---|---|
| Keyframe-interpolated ControlNet strength | Structure early, freedom late (Pattern 15) |
| 2-step preview + seed shopping | Separate take selection from quality (Pattern 16) |
| Regional LoRA hooks / SAM masks | Externalise "where" into a mask (Four Building Blocks) |
| GGUF quantisation choice | Match the model's footprint to the machine you actually have |
| Face-detailer pre-selection node | Apply a corrective only where the defect is (Pattern 6) |
| Chunk-and-stitch with per-chunk prompts | Long shots are authored in segments with scheduled intent |
