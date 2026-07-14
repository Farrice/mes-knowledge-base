---
description: "/jcin-ad-world — branded-world ad system: build the brand's world ONCE (bible + product locks + avatar locks + scene-plate library), then feed BOTH static ad production (Dara Denney formats) and video ad production (worldbuilder grammar) — campaign-scale identity that holds across every variant, with the fake-BTS world-texture move for believability"
---

# The Branded Ad World (Joey Cinema OS)

Dara Denney's discipline says format × messaging are independent test axes — you rotate them constantly. Joey's discipline supplies the third axis those rotations assume and almost nobody locks: **identity**. The bottle, the founder-avatar's face, the garment's construction, the world's light — held constant across twenty variants, so the test measures the format and the message instead of the render lottery. His Control world is the proof: locked characters and locked plates producing music videos, backstage content, domestic slice-of-life, and red-carpet paparazzi shots that all read as the same world. This workflow builds that asset base ONCE for a brand — bible, product locks, avatar locks, scene-plate library — then feeds it into both ad vessels: static (Dara's 7 archetypes) and video (worldbuilder grammar). Expensive permanent context upstream; every ad variant becomes a cheap read of it.

## Pre-Flight

Read before executing:
1. `skills/joey-cinema-os/genius.md` (patterns 5, 6, 16, 24; § System Fit — the product transfer: face lock ≈ hero-angle lock, 3-panel sheet ≈ turnaround, bible ≈ brand canon)
2. `skills/joey-cinema-os/SKILL.md` (§ The Pipeline — strict CANON → STILLS → MOTION order; § Stacking Guide)
3. `skills/dara-denney-meta-ads/SKILL.md` (§ The 3-Layer Static System, § The 7 Format Archetypes, § Stacking Pattern: Video ↔ Static)
4. `extractions/joey-cinema-os/extraction-report.md` (§ Applied Intelligence — branded-world ad systems; § Hidden Knowledge — fake-BTS worldbuilding)

> 🔒 **Pre-Flight Gate** — answer before any asset builds:
> 1. **The Existence Question, brand edition.** Does this brand already have locked world assets (bible, product locks, avatar sheets, plates)? Inventory first — the whole workflow is a build-ONCE discipline, and rebuilding an existing lock is the anti-pattern it exists to kill. Existing world → skip to Step 4.
> 2. **Real product documentation in hand?** The KY rule: real documentation beats vibe prompts. For garments/products, collect spec sheets, technical flats, measurements, all angles, and a colors-to-avoid palette BEFORE locking. Missing docs → name the gap and budget accordingly (~50 generations for the hardest garment, knowingly), or mark the lock `[TBD]` — invented canon becomes locked canon becomes prompt drift.
> 3. **Chain order holds.** No bible → no locks. Unlocked product/avatar → no ads. Kick back to the right layer instead of improvising identity inside an ad prompt.

## Input Required

- The brand: what it sells, who fronts it (founder? avatars? nobody?), and the owning project folder for the world assets
- Existing asset inventory — bible, locks, sheets, plates already on disk (paths), or an honest "nothing yet"
- Real product documentation available: spec sheets, technical flats, measurements, photography from all angles, brand palette WITH colors-to-avoid — or the list of what's missing
- The campaign's first job: which ad vessel ships first (static, video, both), which persona/awareness level it targets
- Budget posture: credits available and how many takes the hardest asset is allowed (~50 gens for a hard garment is the honest planning number)

## Skill Acquisition

The build phase runs this skill's own Tier 1/2 workflows in pipeline order — they are the stages here, not options: `/jcin-world-canon` → `/jcin-product-lock` / `/jcin-character-lock` → `/jcin-scene-shot` (plates). The FEED phase (Step 4 onward) offers cross-hub partners: Dara workflows for static, worldbuilder grammar for video. Per the no-forced-wiring rule those handoffs are options a campaign composes — never mandatory pipeline steps. Skim `skills/dara-denney-meta-ads/SKILL.md § Render Wiring` for the cost-gated production surfaces before promising renders.

## Execution

### Step 1: Brand bible — `/jcin-world-canon` (once)
Build the brand's world bible via story-bible-builder: what the world IS (era, palette hexes, light quality, production rules), who lives in it (avatar roster), the voice, and the **"never" clauses** — locks exclude as much as they include ("warm terracotta and cream — never neon, never gradient-purple"). For a brand, the bible is the brand canon: positioning language stays out; what a camera can see goes in. Every `[unknown]` stays `[TBD]`. Gate: the stranger test — could someone who's never heard of this brand shoot a scene in its world using only the bible, and get it right?

### Step 2: Identity locks — `/jcin-product-lock` + `/jcin-character-lock` (per asset)
- **Products** (`/jcin-product-lock`): hero lock → turnaround sheet → in-context plates, the KY technical-flats method — construction documentation in, colors-to-avoid palette attached, one product per reference, as large as the format allows.
- **Avatars/characters** (`/jcin-character-lock`): strict Mode 0 → 1 → 2A order — face lock → outfit base → 3-panel sheet. One face per identity reference. Founder-as-avatar for founder ads gets the same treatment as a Control member.
- All reference plates flat: 18% gray, zero baked lighting — these assets seed video, and baked shadows get inherited and amplified downstream.
- One variable per shot when building the series; identity stays locked while pose/framing/expression rotates.

### Step 3: Scene-plate library — `/jcin-scene-shot` (per location)
Build the brand's recurring locations as environment plates (worldbuilder Mode 3 cinema-prose): the shop counter, the gym floor, the kitchen, the delivery van. Plates carry world; canonical refs carry identity — **canonical-over-plate**: every named subject keeps its own reference even when visible in a plate. A library of 4–8 plates covers most campaigns. Register the library in the owning project folder with tag names locked (`@shop_plate`, `@founder_ref`, `@bottle_ref`) — tags persist across the whole campaign, not per session.

### Step 4: Feed STATIC ad production (Dara stack — optional offer)
Hand the locked world to Dara's static engine; her layers do strategy/format/copy, this world supplies every pixel of identity:
- **`/dara-static-engine`** (`skills/dara-denney-meta-ads/workflows/08-static-engine.md`) — the 3-layer build (Strategy → Design → Copy); the key visual slots are filled from product locks + plates instead of generated cold.
- **`/dara-transformation-static`** (`workflows/13-transformation-static.md`) — before/after with a locked avatar: same face both frames, which is exactly what unlocked generation can't do.
- **`/dara-static-production`** (`workflows/15-static-production.md`) — the renderer; its brand-brain step ingests the bible + colors-to-avoid sheet as the constraint doc; 3-variation batches rotate copy/format while references hold identity.
- **`/dara-format-swap`** (`workflows/16-format-swap.md`) — winner in one vessel → paired spec in the other on the same research; the locked world is what makes the swap visually seamless.

### Step 5: Feed VIDEO ad production (worldbuilder grammar — optional offer)
Video variants compile through `skills/cinema-worldbuilder-pro/SKILL.md`: `/jcin-shot-plan` costs the campaign's shots BEFORE generation (beats, durations, per-shot mode, take budget), then per-shot prompts consume `@tags` from the Step 2–3 library. A 15s hero cut routes through `/jcin-story-15s`; founder/UGC-register video ads borrow Dara's format archetypes for the beat structure while the worldbuilder carries the camera. Mode discipline: one cinema mode dominant per shot; the cut between modes is the punch.

### Step 6: The fake-BTS / world-texture layer (the believability move)
A synthetic brand world reads real through mundane *context*, not just render fidelity. Salt the campaign with behind-the-scenes-that-never-happened: the product on a cluttered kitchen counter at 7am, the avatar in the makeup chair, the blue-screen shoot with film crew visible, camcorder-era grade, the delivery box half-opened on a doormat. Domestic and workaday registers — shot inside the same locks and plates — are what make the polished hero assets believable by contrast. Budget 2–3 texture assets per campaign flight; they're also the cheapest organic-style content the world produces.

### Step 7: Campaign card
Close by writing the world's state down: assets built (with file paths + tag names), assets still `[TBD]`, per-asset take costs observed, and which ad vessels are currently fed. Next campaign starts at Step 4, not Step 1 — that's the compounding.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| **DTC product brand (MyBPM-shape)** | Product locks lead; KY technical flats mandatory for apparel; statics lean grid/headliner/comparison (Dara archetypes 2/4/6); fake-BTS = studio-shoot texture + packed-orders domesticity. |
| **Personal/founder brand** | Founder avatar lock (with consent, from real photos) ≈ face lock; founder-ad plays (`/dara-founder-ad` beat structure) shot inside the world; texture layer = desk, car, gym — the mundane registers that make an AI-assisted feed read lived-in. |
| **Local service (Jen-listings-shape)** | Plates dominate: the neighborhoods, the staged rooms; product lock ≈ the listing's hero angles; statics = educational-infographic + transformation (archetypes 1/5); world texture = open-house prep BTS. |
| **Client campaign sprint** | Compose with `/dara-static-ad-sprint` (`workflows/17-static-ad-sprint.md`): the sprint sells 5–10 concepts, this world is the reusable asset base under all of them — price the world build once, amortize across flights. |

## Output Requirements

1. **World inventory** — what exists / what was built this run / what stays `[TBD]`, each with file path and locked tag name.
2. **The three lock artifacts** (or pointers to them): bible, product/avatar reference sheets, plate library — flat-graded, never-clause-carrying, colors-to-avoid attached.
3. **Feed manifests, offered not imposed** — for static: which Dara workflow(s) + which locked assets fill their visual slots; for video: the costed `/jcin-shot-plan` + per-shot prompt list.
4. **Texture-layer plan** — 2–3 fake-BTS/domestic asset concepts inside the same locks.
5. **Campaign card** (Step 7) saved with the owning project — the next flight's starting state.
6. Every generation-touching step carries its guard pre-flight (`higgsfield_budget_guard.py` / `fal_budget_guard.py` / `creative_router.py` cost line) — surfaced, never bypassed.

Execution prompt: references/prompts-v2/shot-plan.md — honor its Output Contract.

```
BRAND WORLD — [brand] · [owning project path]

INVENTORY:
  Bible:        [path / built this run / TBD]      "never" clauses: [count]
  Product locks:[@tag → path, per product]         colors-to-avoid: [attached?]
  Avatar locks: [@tag → path, per avatar]          one face per ref: [confirmed]
  Plate library:[@tag → path, per location]        flat-graded 18% gray: [confirmed]

STATIC FEED (offered):
  /dara-static-engine → [which locked assets fill Layer-2 visual slots]
  /dara-transformation-static → [avatar @tag held across before/after]
  /dara-static-production → [bible + colors-to-avoid = the brand-brain doc]

VIDEO FEED (offered):
  /jcin-shot-plan → [beats, durations, per-shot mode, take budget, total credits]
  per-shot prompts → [which @tags each consumes]

TEXTURE LAYER (2–3 fake-BTS/domestic concepts, same locks):
  1. __________   2. __________   3. __________

CAMPAIGN CARD: built [list] · TBD [list] · observed cost/take [n] · vessels fed [static/video]
NEXT FLIGHT STARTS AT: Step 4 (the world persists; only ads get made)
```

## Quality Gate

> 🛡️ Anchor against `genius.md § Quality Rubric` — the load-bearing rows here are **Identity persistence** (10 = holds across a full campaign incl. wardrobe/action/era) and **World believability** (10 = fake-BTS/mundane texture reads documentary-real).

- **Built once, read many.** No identity decision lives inside an ad prompt — if a variant needed the product re-described, the lock failed; fix the lock, not the prompt.
- **Pipeline order held** — bible before locks, locks before plates, plates before ads; any skip was named out loud with drift accepted knowingly.
- **Locks carry "never" clauses and colors-to-avoid** — a lock that only says what IS won't hold over hundreds of renders.
- **No invented canon** — every bible field is sourced or `[TBD]`; a designer/owner recognizes their own product's construction in the output (the KY success metric).
- **Cross-hub handoffs presented as options** — Dara and worldbuilder feeds offered with a reason, never wired as mandatory stages (no-forced-wiring is binding).
- **Identity is the held axis** — the ad test plan varies format × messaging while references stay fixed; if a test cell varies identity AND message, the readout is noise.
- **Texture layer exists** — at least the plan for it; a world with only hero shots reads like a catalog, not a world.

## Common Pitfalls

- **Rebuilding a lock because a variant "looks off."** The failure is almost always in the ad prompt re-describing what the reference carries (double-weighting identity) — cut the re-description before touching the lock. If the lock itself drifted, repair it via `/jcin-prompt-doctor`, don't fork it.
- **White seamless plates for video-bound assets.** White reads clean to human eyes and breaks edges downstream — video models amplify mistakes at high-contrast edges. 18% gray, zero lighting information, always, when the asset seeds motion.
- **Vibe-prompting a real product.** "Sleek black bottle with gold accents" produces a plausible bottle that isn't yours. The KY rule is documentary: construction docs in, all angles in, colors-to-avoid attached — the success metric is the owner recognizing their own product's construction.
- **Treating the Dara handoff as a stage.** The static feed is an offer with a reason; a brand might ship video-only for a quarter. Forced wiring turns a compounding asset base into a bureaucratic pipeline (binding: hubs compose freely).
- **Skipping the texture layer as "extra."** The mundane registers are what make hero polish believable — Joey's Control world reads real because of the makeup chairs and blue screens, not despite them. Two texture assets per flight is the floor, and they're the cheapest content the world makes.
- **Building the whole world before the first ad ships.** Build the bible + the locks the FIRST campaign needs, ship, then extend. A complete world with zero ads is stock on a shelf, not a campaign.
