---
date: 2026-07-13
session: joey-cinema-os
tier: operator-guide
status: enriched
---

# Joey Cinema OS — What We Built 2026-07-13 and How to Use It

> Forge extraction from Joey (Noisy Group / Control World) — the filmmaker who built a fully AI-generated K-pop group and gave the pipeline away. Shipped: three production skills installed **verbatim**, one judgment layer (`skills/joey-cinema-os/`), and 12 `/jcin-*` workflows. Blind-pass PASS (EVAL-035), heartbeat 6/6. Spine: `skills/joey-cinema-os/SKILL.md` · judgment: `skills/joey-cinema-os/genius.md` · sources archived: `extractions/joey-cinema*/`.

## ⚡ If you only read 10 lines

- The pipeline is strict: **CANON → STILLS → MOTION** (story-bible-builder → banana-pro-director → cinema-worldbuilder-pro) — layers never do each other's jobs; don't skip, don't combine.
- First thing to run on any multi-asset/multi-shot mission: `/jcin-pipeline <mission>` — asset inventory → build checkpoints → costed shot plan for approval BEFORE anything paid runs.
- Budget physics: ~117 credits per 13s 1080p Seedance gen, 200–300 per studio piece, 5–6k for a music video.
- LOCKED BLOCKS are LOCKED: never paraphrase the flat-grade close, cinema stack, Capture Realism, or FOV degree ladder; never rewrite end-position negation blocks into positive phrasing.
- Never add lighting to a flat gray reference plate — 18% gray beats white; lighting is applied exactly once, in scene plates, last.
- GPT-2 trap: Higgsfield GPT-2 = face-fidelity king; OpenAI GPT Image 2 (`gpt-image-2-director`) = layout/typography king, weak faces — never conflate.
- Higgsfield MCP is the native surface (`@tag` grammar works); Fal wrappers take no @tags (strip to prose descriptors); fal seedance-1080p is HARD-BLOCKED.
- Products: `/jcin-product-lock` (the KY method) — real documentation beats vibe prompts; gaps marked `[TBD]`, never invented; brand-neutral language even for the client's own marks.
- Seedance prompts: 280–400 words single-shot, FOV in degrees not millimeters ("47° holds, 50mm drifts"), diegetic audio only.
- Iteration physics: past ~3 failed iterations on one prompt, stop patching — Reset Ritual via `/jcin-prompt-doctor`; the honest win is 8–10 takes → 2–3.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/jcin-pipeline` | Conducted mission: bible → locks → plates → costed shot plan → shot prompts | More than one asset or shot, or unsure which layer |
| `/jcin-world-canon` | Story/world/brand bible | Multi-scene world before any scenes |
| `/jcin-character-lock` | Face lock → outfit base → 3-panel sheet | New recurring character |
| `/jcin-scene-shot` | Scene plate + matching Seedance shot prompt | One shot in a built world |
| `/jcin-product-lock` | Product identity lock (hero, turnaround, palette + avoid-row) | A product must hold identity across a set |
| `/jcin-outfit-engine` | Outfit builds and two-ref swaps | Wardrobe on a locked character |
| `/jcin-prompt-doctor` | Reset-Ritual prompt repair | A prompt is drifting or bloated |
| `/jcin-shot-plan` | Credit-costed shot plan on its own | Budgeting before generation |
| `/jcin-voice-lock` | Voice/persona payloads for prompt slots | Character voice work |
| `/jcin-story-15s` | 3-shot / 15-second micro-story | Short-form beat design |
| `/jcin-ad-world` | Branded-world ad system (locked product + avatars) | Ad set that must hold identity |
| `/jcin-studio-bridge` | fantastic-studio / creative_router wiring run | Routing studio stages through Joey's grammars |

---

## The mental model (read this once, everything else follows)

**Consistency is an asset discipline, not a model feature.** Every load-bearing decision moves OUT of the prompt and INTO locked upstream artifacts: bibles carry *who*, face locks and canonical sheets carry *what they look like*, flat reference plates carry *what rides into the frame*, block-structured prompts carry *what happens on screen*. Each generation becomes a cheap, disposable read of expensive, permanent context.

The pipeline is strict — **CANON → STILLS → MOTION** — and the layers never do each other's jobs:

```
CANON  → story-bible-builder      once per world (identity, voice, era, "never" clauses)
STILLS → banana-pro-director      per asset (face lock → outfit base → 3-panel sheet → scene plates)
MOTION → cinema-worldbuilder-pro  per shot (block-structured Seedance prompts, costed runtime)
```

Don't skip steps, don't combine them. Unbuilt character in a video ask → kick back to stills. Multi-scene world with no bible → build canon first, or proceed with the drift named out loud. Everything here is **prompt-only** ("the skill's job ends at the code block") — actual generation still fires the existing cost gates.

---

## 1. `/jcin-pipeline` — the front door and mission conductor

### What it is

The end-to-end conductor: intake via the Existence Question ("does this character/product already exist, or are we developing it?"), then bible → asset locks → scene plates → **costed shot plan** → shot prompts, checkpointed at every stage. It writes no prompts itself — it sequences the layer workflows and refuses layer-skipping.

### When to reach for it

Any mission with more than one asset or more than one shot: a branded film, a music video, an ad set, a character world, a client product library. Also when you don't know which `/jcin-*` you need — the conductor routes.

### When NOT to

Single known deliverable → go straight to the layer workflow (table below). Stylized posters or text-heavy layouts → not this lane at all (see §5).

### How to invoke

```
/jcin-pipeline 15-second MyBPM brand film — hoodie + one recurring model, Higgsfield surface
```

You'll get an asset inventory (EXISTS / NEEDS BUILD per item) to nod at, per-asset build checkpoints, then a shot-plan table (beats, mode, duration, take budget, credit estimate) **for approval before anything paid runs**. Budget physics it holds you to: ~117 credits per 13s 1080p Seedance gen, 200–300 per studio piece, 5–6k for a music video.

### The 12-workflow surface (route by task)

| You want | Command |
|---|---|
| Full mission, conducted | `/jcin-pipeline` |
| Story/world/brand bible | `/jcin-world-canon` |
| Character identity (face lock → outfit → 3-panel sheet) | `/jcin-character-lock` |
| Scene plate + matching Seedance shot prompt | `/jcin-scene-shot` |
| Product/garment/vehicle identity lock | `/jcin-product-lock` |
| Outfit builds and two-ref swaps | `/jcin-outfit-engine` |
| A prompt is drifting or bloated | `/jcin-prompt-doctor` |
| Credit-costed shot plan on its own | `/jcin-shot-plan` |
| Voice/persona payloads for prompt slots | `/jcin-voice-lock` |
| 3-shot / 15-second micro-story | `/jcin-story-15s` |
| Branded-world ad system (locked product + avatars) | `/jcin-ad-world` |
| Wire fantastic-studio / creative_router into this pipeline | `/jcin-studio-bridge` |

### Honest edges

Long missions span sessions — the conductor ends by writing a mission state note (tag names, approved refs, bible path, remaining shot rows) and pinning the session. A next session that re-asks the Existence Question on assets already locked has failed the handoff.

---

## 2. The three installed-verbatim skills — and the LOCKED-BLOCKS rule

### What they are

Installed exactly as Joey ships them ("Joey's Skill Files v3.0"), as siblings:

- **`skills/banana-pro-director/`** — stills. Six modes in strict order: Mode 0 face lock (mid-gray seamless, black camisole/tank baseline, identity only) → Mode 1 outfit base → Mode 2A 3-panel sheet (headless front, full rear, tight chest-up face lock — the default; 6-panel is legacy, explicit request only) → Mode 3 scene plates; Modes 4 (GPT-2 detail) and 5 (outfit swap) are gated utilities.
- **`skills/cinema-worldbuilder-pro/`** — Seedance video prompts. Five cinema modes (M1–M5), Frame Map / Subject Lock / Sound Bed / Capture Realism blocks, FOV anchored in **degrees not millimeters** ("47° holds, 50mm drifts"), 280–400 words per single-shot prompt, diegetic audio only.
- **`skills/story-bible-builder/`** — interview-driven canon. Output is one dense installable SKILL.md: premise, timeline, characters with voice and movement locks, era palettes, production rules, "never" clauses. Test: could a stranger write a scene in your world using only this bible and get it right?

### The rule (binding)

Their locked blocks — the flat-grade close, the cinema stack, Capture Realism, the FOV degree ladder — are **LOCKED. Never paraphrase them, never "improve" them.** Two failure modes worth naming because they look like helpfulness:

- **Never rewrite the end-position negation blocks into positive phrasing** or scatter them upward. At the end of a prompt they read as a quality filter; moved or "fixed," they read as conflicting instructions.
- **Never add lighting to a flat gray reference plate.** Baked shadows get inherited and amplified by every downstream generation; 18% gray beats white because video models amplify mistakes at high-contrast edges. A gorgeous lit hero shot is a finished deliverable, never a reference.

### How to invoke

You usually don't invoke them directly — the `/jcin-*` workflows load them by section name. Direct use works when you just want one still or one Seedance prompt: say "build a face lock with banana-pro-director" or "Seedance prompt via cinema-worldbuilder-pro."

### Honest edges

The three siblings don't yet have their own structure-pure prompts-v2 (backfill queue); the 8 v2 execution prompts live under `skills/joey-cinema-os/references/prompts-v2/` and cover the OS-level deliverables.

---

## 3. `/jcin-product-lock` — the KY method for product-grade client visuals

### What it is

Joey's character discipline transferred one-to-one to products: hero-angle lock ≈ face lock, turnaround sheet ≈ 3-panel sheet, brand canon ≈ bible. The KY method (from Joey's fashion-designer collaborator) means **real documentation beats vibe prompts**: spec sheets, Adobe technical flats, measurements, all angles, material and hardware callouts — plus a per-product **palette sheet with a colors-to-avoid row** ("matte forest green — never neon green, never teal-shifted"). This is the lane for MyBPM apparel, Jen listing hero objects, and TrendScale-class packaging.

### When to reach for it

Any product that must hold identity across a set — an apparel drop, an ad system, a listing series. The tell: you're about to generate the same product twice.

### When NOT to

One-off lifestyle image where the product never recurs. Rooms and interiors are plates, not products — Mode 3, not this.

### How to invoke

```
/jcin-product-lock MyBPM cropped hoodie — flats and measurements attached, seeds video ads
```

### Worked shape (what you'll actually get)

Documentation inventory table (gaps marked `[TBD]`, never invented — "invented canon becomes locked canon becomes prompt drift") → palette sheet with avoid-row → hero-lock prompt on the verbatim flat-grade close, with the material-true sheen exception (PVC/leather/glass/chrome keep specular; everything else matte) → turnaround (front / back / detail close-up; garments go ghost-mannequin headless) → in-context plates **last**, where lighting is applied exactly once. Take budget declared up front: 2–3 takes for a documented standard product, **up to ~50 generations for the hardest garment — budgeted knowingly, never discovered in overruns** (KY's hardest corset took ~50 with full documentation; declared, that's production; discovered, it reads as disaster).

One counterintuitive rule: **brand-neutral language even for the client's own marks.** Models don't know names; names drift regardless of who owns them. "Matte black bottle with a debossed three-letter wordmark" in the prompt; real label art composited from the cutout reference, never prompted by name.

---

## 4. The GPT-2 trap — Higgsfield GPT-2 ≠ OpenAI GPT Image 2

Joey says "GPT-2" constantly, and it is **Higgsfield GPT-2**: the face-fidelity king, credit-heavy, used for detail face shots and chest-up locks. The system's `gpt-image-2-director` is **OpenAI GPT Image 2**: layout and typography king, **weak faces**. Opposite verdicts on the same phrase — never conflate. Routing rule: faces and photoreal identity → Higgsfield lane; dense text, layouts, typographic posters → the OpenAI lane. This disambiguation is wired at every routing touchpoint; keep it that way.

Surface fork, same section because you'll hit it in the same breath: **Higgsfield MCP is the native surface** — `@tag` element grammar works, refs upload via `media_upload` / `show_reference_elements`. **Fal wrappers take no @tags** — strip every tag to its prose descriptor — and **fal seedance-1080p is HARD-BLOCKED** by the budget guard. Plan around the block, never around the guard.

---

## 5. How it composes — options, never pipeline steps

No forced wiring; these are stacks you *may* reach for:

- **Fantastic Studio (`/fantastic-studio`)** — stages 04 (model route) and 05 (prompt compile) can route photoreal-people and Seedance work through Joey's grammars; concept/divergence/critique stages stay upstream. `/jcin-studio-bridge` does the wiring run.
- **Fantastic Posters** keeps the stylized/typographic Fal lane; `gpt-image-2-director` keeps layout/text density; **Joey is the photoreal persistent-world/character/product lane.** Three lanes, no turf war.
- **Story spine** (Stanton / Ben Watkins / Hawley) sits above the visual pipeline → feed `/jcin-world-canon` premise work and `/jcin-story-15s` beat design (grab → payoff → unresolved questions; judge the 15s by how many "why?"s it leaves).
- **Ad craft** (Dara / Omar) × `/jcin-product-lock` + `/jcin-ad-world` → identity that holds across static AND video variants.
- **Voice OS**: bible voice descriptors are the character-side analog of VOICE-CARD — separate documents, never let them collide with Farrice's own voice layer.

---

## 6. Extend, never rebuild — and the honest edges

- **Extend the OS, don't re-extract.** Sources are archived (`extractions/joey-cinema*/` — 3 frame harvests, Notion doc, analysis, reference corpus). New capability = new workflow in `skills/joey-cinema-os/workflows/`, pointed at the existing locked blocks.
- **The quality bar is the Recognition Test**: would Joey hit Copy on this prompt and paste it into Higgsfield without edits? Compare against the corpus exemplars (amber-PVC-raincoat sheet, '33'-jersey character) — the usual tells are a re-described reference, a mood word, or a missing "never" clause.
- **Iteration physics**: past ~3 failed iterations on one prompt, stop patching — Reset Ritual via `/jcin-prompt-doctor` (cut it, let it breathe, re-add minimum). The honest win is 8–10 takes → 2–3, never one-shot magic.
- **Cost posture**: prompt work is never cost-gated; execution always is. When a gate denies, surface it — never retry around it.
- **Not yet proven at music-video scale in this workspace** — the extraction passed blind eval, but the first full multi-session mission here will surface rough edges; `/extract-approach` whatever we learn.

*Created 2026-07-13 (Joey Cinema OS forge session). Extend this guide as the pipeline gets its first full client mission — don't let it sediment.*
