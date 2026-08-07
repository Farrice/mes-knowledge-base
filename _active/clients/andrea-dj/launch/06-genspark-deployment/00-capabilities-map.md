# 00 — Genspark Capabilities Map + Routing Matrix

*Verified Genspark.ai catalog and prompt-routing logic as of 2026-05-28. Re-verify quarterly — the model landscape changes monthly.*

---

## TL;DR

Genspark is the **multi-model orchestration layer** for Resonance asset production. Pro plan ($249.99/mo or $199.99 annual) = 125,000 credits + 1 TB storage + all models. Video burns 100-2,000 credits/gen — translating to roughly 60-250 video generations/month before the wall.

**The routing decision is the entire game.** Don't ask Super Agent generic questions for Resonance — specify the model.

---

## Section 1 — Verified Model Catalog

### Image Generation (FREE on Pro through Dec 2026)

| Model | Best For | Status |
|---|---|---|
| **Nano Banana Pro** (Gemini 2.5 Flash Image / Pro tier) | **Default workhorse for Resonance brand stills** — versatility, character consistency across calls | ✓ VERIFIED |
| **GPT Image 1.5 / 2** | Text-in-image (posters, lyric overlays, IG carousel slides with copy) | ✓ VERIFIED |
| **Flux 2 Pro** | Photoreal stills — humans, fabric, skin detail | ✓ VERIFIED |
| **Recraft V3** | Vector, brand illustration, logo-friendly | ✓ VERIFIED |
| **Ideogram V3** | Strong on faces + text rendering | ✓ VERIFIED |
| Seedream v4.5 / v5 Lite | Listed in 2026 reviews | LIKELY |
| Qwen Image 2 | Listed in 2026 reviews | LIKELY |
| Higgsfield Soul 2.0 | **NOT in Genspark** — use direct Higgsfield MCP for soul-tier photoreal people (per visual-tool-routing rule) | NOT IN GENSPARK |
| MidJourney 6/7 | Historically requires own subscription | NOT IN GENSPARK |
| Stable Diffusion 3.5 | Not surfaced in 2026 catalog reviews | NOT CONFIRMED |

### Video Generation (CREDIT-METERED)

| Model | Native Audio | Img-to-Vid | Aspect | Cost / 8s clip | Best For |
|---|---|---|---|---|---|
| **Veo 3.1 Quality** (Google) | ✓ Best in class (48kHz dialogue + SFX) | ✓ | 16:9 / 9:16 / 1:1, 4K | $6.00 (w/ audio) | **Hero clips, landing page, Substack embed** |
| **Veo 3.1 Fast** | ✓ | ✓ | Same as Quality | $0.15–0.40 / video | Drafts, cost calibration |
| **Kling 2.1 Master** (Kuaishou) | ✗ (V3 partial) | ✓ | 16:9 / 9:16 / 1:1, 1080p 30fps | ~$1.40 | **Close-up face stability** (Reel B-roll, intimate convos) |
| **Runway Gen-4.5** | Limited | ✓ | 16:9 / 9:16 / 1:1, 720p/1080p | $1-3 | **Story sequence character consistency (95%+)** |
| **Seedance 2.0 Pro** (ByteDance) | ✓ Joint audio+video | ✓ | 7 ratios incl. 21:9, up to 2K, max 15s | ~$1.20 | **IG Reel hero with audio** (Veo's cheaper cousin) |
| **Hailuo 02** (MiniMax) | ✗ | ✓ | 9:16 / 16:9, 768p Standard | $0.36 | Smooth ambient B-roll, cheapest |
| **PixVerse V6** | ✗ | ✓ | All ratios | $0.72 | Fastest cheap drafts |
| **VIDU Q3** | Limited | ✓ | Standard ratios | varies | Lower priority |
| **Wan V2.7** | Limited | ✓ | Standard ratios | varies | Open-weight family |
| ~~Sora 2 Pro~~ | ✓ | ✓ | All | **DEAD** | **DO NOT USE** — app ended Apr 2026, API ends Sept 24, 2026 |

### Other Tools

| Tool | When To Use |
|---|---|
| **Super Agent** | Multi-step missions (research + slide + write + call in one prompt). When you don't know which model wins. |
| **AI Slides** | Resonance pitch decks, sponsor decks, press one-sheeter. Auto-pulls citations. |
| **AI Sheets** | Research tables (e.g., "top 20 Chicago lifestyle press contacts with email + beat + recent stories"). Live research analyst. |
| **AI Pods** | Long-form audio (Resonance founder podcast). Not launch-critical now. |
| **Sparkpages** | Hand Andrea a structured research result with citations + follow-ups. |
| **Call For Me** | Super Agent makes real phone calls — book venue, request quotes. Verified live. |

---

## Section 2 — Routing Matrix (Resonance-specific)

For every Resonance asset class, the verified-best model:

| Asset | Model | Reason |
|---|---|---|
| **Brand still — every IG post, carousel slide, landing page image** | Nano Banana Pro | Locked = visual continuity. Free on Pro. |
| **Brand still with TEXT overlay** (e.g., "Saturday July 18" cards) | GPT Image 2 | Text rendering wins. Free on Pro. |
| **Photoreal interior scene WITHOUT recognizable specific people** | Flux 2 Pro | Fabric + light fidelity. Free on Pro. |
| **Photoreal people in scene — recognition moments** | Higgsfield Soul 2.0 (direct, NOT Genspark) | Per visual-tool-routing.md — Soul wins on photoreal people |
| **Landing page hero video (5-8s, ambient loop, native audio)** | Veo 3.1 Quality | Best native daytime + ambient audio |
| **IG Reel hero (10s, vertical, on-beat)** | Seedance 2.0 Pro | Joint audio-video, cheaper than Veo |
| **IG Reel B-roll close-up (faces hold frame >3s)** | Kling 2.1 Master | Face stability beats Veo on close-ups |
| **Substack embed (single hero clip with audio)** | Veo 3.1 Quality | Substack autoplays muted but Veo audio = no separate sync later |
| **Story sequence (3-5 clips, same character)** | Runway Gen-4.5 | Only model purpose-built for character consistency |
| **Dance-energy clip (hands almost touching, recognition turning to movement)** | Kling V3 | Built for multi-shot motion choreography |
| **Cheap draft / mood test** | Veo 3.1 Fast or PixVerse V6 | Test prompt structure before spending |
| **Research + Note draft + ICP teardown** | Super Agent + Mixture of Agents | Multi-model reflection on copy |
| **Press list / venue quote table** | AI Sheets | Live research analyst |
| **Sponsor deck / pitch deck** | AI Slides | Auto-citations |

---

## Section 3 — Super Agent vs Direct Model Calls

### Use Super Agent when:
- Task is multi-step / multi-tool (research → slide → image → write)
- You don't know which model wins
- Cost preview matters less than coverage

### Override and call directly when:
- You know the winning model (Veo 3.1 for hero, Nano Banana Pro for brand stills)
- You need consistency across runs (same model = same look)
- You're conserving credits

### Magic phrases (proven to improve Super Agent output)

| Phrase | What It Does |
|---|---|
| `"Use Mixture of Agents and reflect across GPT, Claude, Gemini before finalizing"` | Triggers reflection pass — "keeps the strongest parts." Use for high-stakes copy. |
| `"Always use a reference image"` | Reference images make video results "10x better" (Lindy/multiple reviewer consensus) |
| `"Act as a creative director. Brief me on 3 different routes before generating."` | Forces multi-option thinking before burning credits |

### Example Super Agent prompt for Resonance

```
Act as a creative director for a curated daytime sober dance party in Chicago called Resonance. 

Brand: pre-noon natural light, two-person recognition moments, no nightclub tropes, no neon, no UV.

Use Mixture of Agents to draft 3 hero-shot concepts. For each, name which Genspark model you'd use and why (Flux 2 Pro vs Nano Banana Pro vs Ideogram V3). 

Do NOT generate yet — return the brief first.
```

---

## Section 4 — The 9 Universal Prompt Rules

Apply to every Genspark video call. Distilled from Google Veo, Kling, Runway, Seedance prompting guides + reviewer comparisons.

1. **Reference images on every video call.** Non-negotiable. The hero still IS the keyframe; the prompt is the motion direction.

2. **Top-down prompt structure**: aspect ratio + duration → 2-4 clip shot list → per-clip (shot size + lens + camera move + subject action + lighting + motion + audio) → negative prompts at the end.

3. **Name the light source physically**, not the brightness adjective. *"Window-left, overcast Chicago morning"* beats *"soft cinematic lighting."* Stabilizes shadows.

4. **One verb per beat.** *"She turns toward the door, recognizes him, half-laugh."* Three concrete actions. Not *"they vibe."*

5. **Lock identity tokens across clips.** Same lens (e.g., 35mm), same palette, same wardrobe descriptor on every shot. For I2V, the source image IS the identity lock.

6. **Audio direction is part of the prompt** for Veo 3.1 / Seedance 2.0. *"Ambient: low room tone, distant Chicago L train, no music."* If you don't direct audio, the model invents it.

7. **Negative prompts at the end** suppress slop. Resonance default tail:
   > `no nightclub, no neon, no UV blacklight, no laser, no strobe, no crowd, no champagne pop, no slow-mo confetti, no golden hour, no fisheye, no shaky cam, no AI-blur on hands.`

8. **Image-to-video (I2V) and text-to-video (T2V) are different prompt styles.** Don't mix. For I2V, describe motion + camera move only — the source image carries scene/identity. For T2V, describe everything.

9. **Iterate on 2-3 models per beat, not 2-3 prompts on one model.** Generate the same shot in Veo + Kling + Seedance; pick winner. Credit-cheaper in aggregate than 5 misses on one model.

---

## Section 5 — Anti-Patterns (Banned for Resonance)

### Banned descriptors (signal "AI nightclub slop")
- "Golden hour," "magic hour," "sun-kissed" — predictable orange grade
- "Stadium lighting," "concert lights," "laser show," "strobe," "UV blacklight," "neon glow"
- "Crowd blur," "shaky cam," "live-TV color grading" — viral-trend tells
- "Energetic vibe," "everyone dancing," "high-energy crowd" — produces yoga-class-disconnect look (per `feedback_visual-tool-routing.md`)
- "Cinematic" alone — meaningless. Specify lens + light source + grade instead

### Standard negative-prompt tail for every Resonance video
```
no nightclub, no neon, no UV blacklight, no laser, no strobe, no crowd, no champagne pop, no slow-mo confetti, no golden hour, no fisheye, no shaky cam, no AI-blur on hands, no club lighting, no EDM stage, no festival.
```

### Where Super Agent gets it wrong
- **Defaults to flashiest model** (e.g., picks Sora 2 for video when you want Veo). **Veto by naming the model.**
- **Auto-adds "cinematic, professional, high-quality"** invisibly to prompts. Pre-empt with your own style spec.
- **Rotates models between calls** — breaks visual continuity. **Lock to one model per series.**

---

## Section 6 — Credit Budget Discipline

### Pro tier monthly: 125,000 credits

### Per-asset rough cost (in credits)
| Asset class | Model | Credits | Notes |
|---|---|---|---|
| Image (Nano Banana, GPT Image, Flux) | Various | FREE on Pro through Dec 2026 | Generate liberally |
| Veo 3.1 Quality 8s w/ audio | Veo | ~1,500-2,000 | Save for hero pieces |
| Veo 3.1 Fast clip | Veo | ~50-150 | Drafts only |
| Kling 2.1 Master 8s | Kling | ~300-500 | Reel B-roll workhorse |
| Runway Gen-4.5 8s | Runway | ~300-500 | Story sequences |
| Seedance 2.0 Pro 8s | Seedance | ~250-400 | IG Reel hero |
| Hailuo 02 8s | Hailuo | ~80-150 | Cheap ambient |
| PixVerse V6 5s | PixVerse | ~150 | Fastest drafts |

### Resonance launch wave total estimate
- 4 hero pieces × Veo 3.1 Quality (~8,000 credits)
- 12 Reel B-roll × Kling 2.1 Master (~6,000 credits)
- 6 IG Reel hero × Seedance 2.0 (~2,400 credits)
- 6 cheap drafts × Veo Fast (~600 credits)
- ~~Image generation FREE on Pro~~

**Total launch wave: ~17,000 credits = 13.6% of monthly Pro budget**. Comfortable margin for iteration.

---

## Section 7 — When to Re-Verify

This catalog snapshots May 2026. Re-verify quarterly:

- **Sora 2 API dies September 24, 2026.** Remove all references.
- **Veo 3.5+ likely Q3 2026.** Update if Quality/Fast tiers change.
- **Kling V4 likely Q4 2026.** Watch for face-stability improvements.
- **Higgsfield Soul integration into Genspark** — currently UNCONFIRMED. If it lands, route photoreal-people prompts inside Genspark instead of via direct Higgsfield MCP.
- **Pricing**: Genspark publishes no official per-model cost matrix. Credit-per-clip ranges are reviewer-consensus, not official. Budget conservatively.

**Re-run the research swarm**: `/autopilot research Genspark Q3 2026 model catalog changes`. Updates this file.

---

## Section 8 — Resonance Spike Test (run before locking the stack)

Before committing the routing matrix to production, run a **spike test**:

1. Pick ONE Variant B hero shot (after Andrea picks variant) — e.g., `variant-b-hero-shots-v3/B1-v1-3ef7ce7c.png`
2. Generate the SAME 6-second I2V prompt across **Veo 3.1 Quality, Kling 2.1 Master, Runway Gen-4.5**, all with same reference image
3. Score each on:
   - Source-image fidelity (does it preserve the shot?)
   - Daytime light register (does it stay daylight, not drift to golden hour?)
   - Face stability (no morph at end of clip?)
   - End-of-clip cleanness (no AI loop feel?)
   - Brand register match against 12 Non-Negotiables
4. Pick the winner. Lock it. Update this file with the spike results.

**Budget**: ~$15 total. **Time**: ~30 min including review.

If Veo 3.1 wins the spike — confirmed primary. If Kling wins on this specific brief — pivot the matrix.

---

*Next: `01-image-to-video-prompts.md` for exact I2V prompts using these models on Resonance's v3 hero shots.*
