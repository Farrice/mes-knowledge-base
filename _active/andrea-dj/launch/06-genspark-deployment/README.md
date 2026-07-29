# Genspark Deployment Pack — Resonance Launch

*Production-ready prompts for turning Resonance hero assets into multi-format launch content via Genspark.ai. Routes the right model to the right surface, every time. Research-grounded (3-agent swarm, 25+ verified sources, 2026-05-28).*

---

## What This Folder Is

Six deliverables that take you from "I have hero stills" to "I have a full launch wave deployed." Open in order:

| File | Purpose | Use When |
|---|---|---|
| **`00-capabilities-map.md`** | Verified Genspark model catalog + routing matrix | Before any generation — confirm you're picking the right model |
| **`01-image-to-video-prompts.md`** | Image-to-video prompts for hero loop / Reel / Story sequence | You have a hero still and need a video clip |
| **`02-social-media-prompt-pack.md`** | IG carousel slide gen + Reel scripts + Story sequences | Daily/weekly social content cadence |
| **`03-announcement-content-pack.md`** | Phase 2 event announcement multi-asset deployment | Once venue + JR/anchor DJ lock |
| **`04-waitlist-landing-pack.md`** | Waitlist post + landing page hero video + email confirmation | Phase 1 ship-this-week + landing page deployment |
| **`05-model-overrides.md`** | When to override Super Agent's auto-routing (anti-patterns) | When Genspark routes wrong; copy-paste override prompts |

---

## The Load-Bearing Claim

**Genspark is a multi-model orchestration layer, not a single tool.** The routing decision IS the game. For Resonance's anti-club daytime register, the right stack is:

| Surface | Model | Why |
|---|---|---|
| **Brand stills** (every IG post, carousel slide, landing page image) | **Nano Banana Pro** | Locked to one model = visual continuity across the launch |
| **Landing page hero video** (5-8s ambient loop, native audio) | **Veo 3.1 Quality** | Native daytime + ambient audio in one MP4 |
| **IG Reel hero video** (10s, vertical, slightly more motion) | **Seedance 2.0** | Joint audio-video; cheaper than Veo, same register |
| **IG Reel B-roll** (close-up faces, mid-conversation, 6-10s) | **Kling 2.1 Master** | Face stability beats Veo at close range |
| **Story sequence** (3-5 clips, same characters across) | **Runway Gen-4.5** | 95%+ character consistency from single reference |
| **Substack post embed** (one hero clip with audio) | **Veo 3.1 Quality** | Native ambient room tone in same MP4 |
| **Research / messaging drafts** (founder voice, ICP teardown, Note variants) | **Super Agent + Mixture of Agents** | Multi-model reflection on copy |
| **Quick drafts / cost calibration** | **Veo 3.1 Fast** or **PixVerse V6** | Test prompt structure before spending Quality credits |

**Never use Sora 2 for anything load-bearing past July 2026** — the app ended April 26, 2026; API dies September 24, 2026. ([OpenAI Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)) Build no prompting muscle there.

---

## Deployment Sequence (this week → July)

### This week (Thu 5/28 → Fri 5/29)

1. **Read `00-capabilities-map.md`** — confirm Genspark Pro tier, model access, credit budget
2. **Read `04-waitlist-landing-pack.md`** — generate the landing page hero video (Veo 3.1 Quality, ~$6-7.50)
3. **Read `02-social-media-prompt-pack.md`** — generate Phase 1 Wed 6/3 carousel slides (Nano Banana Pro, ~$0 on Pro tier through Dec 2026)

### Next week (Mon 6/1 → Sun 6/7)

4. **Generate Phase 1 supporting B-roll** via `01-image-to-video-prompts.md` (Kling + Seedance, ~$10-15 total)
5. **Stage Phase 2 announcement assets** per `03-announcement-content-pack.md` — ready to fire on venue + JR lock
6. **Run Substack Note hero illustrations** via Nano Banana Pro (free tier through Dec 2026)

### Phase 2 fire-day (venue + JR confirmed)

7. **Generate Day 0 announcement Reel** via `03-announcement-content-pack.md` (Seedance 2.0, ~$1.50)
8. **Generate Reel 4 (22s on-camera + B-roll)** — use existing v3 hero still as keyframe (Kling 2.1 Master, ~$1.75)

### Phase 3 ramp (T-14 to T-0)

9. **Generate T-14 set preview Reel** (Veo 3.1 Fast for stack of vinyl + needle drop, ~$0.40)
10. **Generate T-7 "room is ready" Reel** (Veo 3.1 Quality for landing-page-style ambient, ~$6-7.50)

**Total estimated launch wave cost**: ~$50-75 across all video generations + free image generation on Pro tier. Sub-1% of one quarter's Resonance revenue projection.

---

## Inputs You Already Have

These v3 assets feed every prompt below as **reference images / keyframes**:

- `_active/andrea-dj/launch/03-visual-variants/variant-a-hero-shots-v3/` — 8 Editorial Broadsheet shots
- `_active/andrea-dj/launch/03-visual-variants/variant-b-hero-shots-v3/` — 7 Latin-American Modernism shots
- `_active/andrea-dj/launch/03-visual-variants/variant-c-hero-shots-v3/` — 8 Restrained Marble + Sage shots

**Critical rule**: Once Andrea picks the winning variant (per `05-andrea-decisions.md`), ALL Genspark prompts below should reference shots from that variant only. Don't mix-and-match registers across the launch.

---

## What's NOT in This Folder (by design)

- **Generic Genspark tutorials** — this is Resonance-specific; consult Genspark's docs for tool basics
- **Hand-written copy for posts** — that lives in `01-announcement-package/README.md` (Phase 1/2/3 calendar) and gets paired with these visual prompts
- **Landing page HTML** — that's `launch/waitlist-landing-page.html` (already built, deployed); this folder generates ASSETS that drop INTO it
- **Image-only prompts that don't lead to video** — covered in `03-visual-variants/prompt-set-for-manual-deployment.md` (the v3 prompts already ran)
- **Sora 2 prompts** — model is sunset, intentionally excluded

---

## Source Inventory (research grounding)

**Genspark capabilities**:
- [Lindy: I tested Genspark AI's 2026 features](https://www.lindy.ai/blog/genspark-ai-features)
- [Scribe: Genspark Claw Features Explained (14+ models)](https://scribehow.com/page/Genspark_Claw_Features_Explained_14_AI_Models_Phone_Calls_and_Cloud_Computer__-4x1S7XeQbuDGYhW05lGkA)
- [Floatboat: Genspark Pricing](https://floatboat.ai/blog/genspark-ai-pricing)
- [OpenAI Genspark case study](https://openai.com/index/genspark/) (ARR + tool-orchestration verified)

**Image-to-video models**:
- [Curious Refuge — Veo 3.1 Review](https://curiousrefuge.com/blog/veo-31-quality-ai-video-generator-review)
- [Google Cloud Veo 3.1 Prompting Guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- [GeeLark — Kling 2.1 Master Prompt Guide](https://www.geelark.com/blog/kling-2-1-master-prompt-guide/)
- [Runway Gen-4 Research Page](https://runwayml.com/research/introducing-runway-gen-4)
- [Atlas Cloud — Seedance vs Kling vs Sora vs Veo](https://www.atlascloud.ai/blog/guides/seedance-vs-kling-vs-sora-vs-veo)
- [Pollo AI — Veo 3.1 Hands-On](https://pollo.ai/hub/veo-3-1-review)
- [OpenAI Sora Discontinuation Notice](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)

**Visual culture references**:
- [Daylight DJ sessions ("Solarcade")](https://medium.com/counterarts/the-rise-of-daylight-dj-sessions-gatherings-b66b2381e7aa)
- [Cercle Odyssey](https://www.designboom.com/design/inside-cercle-odyssey-paris-nomadic-concert-immersive-sound-vision-04-06-2025/) (Neels Castillon cinematographer)
- [Axios — Coffee rave 478% YoY growth](https://www.axios.com/2025/10/02/coffee-raves-daybreaker-soft-clubbing)

**Competitive landing pages** (steal patterns from):
- [CAVA Circle — two-noun headline](https://www.cavacircle.com/)
- [Thursday — cadence-as-identity](https://www.getthursday.com/)
- [Daybreaker — founding myth + whitespace](https://www.daybreaker.com/)

---

## Versioning

- **v1.0 (2026-05-28)**: Initial deployment pack from /autopilot research swarm. Source: 3 parallel research agents + synthesis pass.
- Future: re-research quarterly. Model landscape changes monthly. Sora-style sunsets will continue.
