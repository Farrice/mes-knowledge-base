---
date: 2026-08-02
session: creative-generation-os
tier: operator-guide
status: enriched
---

# Creative Generation OS — What We Built 2026-08-02 and How to Use It

> One session replaced the Higgsfield subscription with an owned, pay-as-you-go creative stack: a `/generate` front door over model recipes, a Netflix-register Asset Command Center for every visual asset with full prompt provenance, a BINDING craft gate that loads a master before any prompt is written, an anime/manga direct-art-direction lane, and three freshly extracted direction masters (St. Pierre, Clark, Flynn). Companions: `skills/generate/references/craft-map.md` (the gate), `extractions/master-hunt-2026-08-02-creative-floor-dossier.md` (the queue + doctrine), `.agent/handoffs/2026-08-02-creative-generation-os.md` (the handoff).

## ⚡ If you only read 10 lines

- Browse everything: `/assets-board` — or the 🎨 Desktop icon. Netflix register: hero billboard, hover-preview cards, copy-path 📋 + copy-prompt 📝 on every asset.
- Generate anything: `/generate` — recipes in `skills/generate/models/`; `python3 execution/generate_media.py models` lists them; `quote` never spends.
- **Doctrine: NEVER freehand a generator prompt.** Load the master per `skills/generate/references/craft-map.md` first — every generation, paid or free.
- Proof on the board: two $0.65 Seedance takes of the same shot — freehand = slop, cinema-worldbuilder grammar = production-usable. One variable changed.
- Prompt-level budgets are real: `--run-id X --run-budget 3.00` on `generate_media.py run`; guard ceilings unchanged ($6/day, seedance-1080p hard-blocked forever).
- Video before Farrice sees it → `/dave-clark-flat-to-cinematic-audit` (no finding may be answerable with "switch models").
- Image exploration → `/nick-st-aesthetic-sweep` (one variable per sweep, ends in a decision); volume/brand systems → `/moodboard-sweep` (deliverable = named recipes, never images).
- Anime lane: `--style=direct` on fantastic-posters + style cards `manga-ink` / `shonen-ui-glow` / `alchemist-blaze`; character lock waits on Mickmumpitz extraction.
- Audio exists now: `generate_media.py run --model minimax-speech` ($0.10/1k chars, verified).
- Extraction doctrine: 2025–26 sources weighted; durable craft = core; tool mechanics = dated era-bound appendix only.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/assets-board` | rescan + rebuild + open the board | any "where is that asset / what made it" moment |
| `/generate` | routed, budgeted, logged generation | any image/video/audio ask |
| `python3 execution/generate_media.py quote --model <id> --prompt "…"` | cost estimate, zero spend | before any recipe call |
| `python3 execution/generate_media.py run --model <id> --prompt "…" [--project <slug>] [--run-id X --run-budget N]` | asset + sidecar + manifest + board refresh | wrapper-less recipes (recraft, minimax audio) |
| `python3 execution/generate_media.py index --file <out> --model <id> --prompt "…" [--cost N]` | provenance for wrapper outputs | after every gen.sh / video-wrapper run |
| `/dave-clark-flat-to-cinematic-audit` | shot-level flat diagnosis (8 causes) | any video that feels dead |
| `/nick-st-aesthetic-sweep` | control-prompt sweep grid ending in a decision | pinning a look instead of rerolling |
| `/moodboard-sweep` | Board Cards + Stack Matrix (named recipes) | brand/style exploration at volume |
| `python3 execution/asset_gallery.py --embed --recent 40` | Artifact-publishable highlights wall | sharing work outside the machine |
| `bash skills/fantastic-posters/gen.sh "<full direction>" --style=direct --size=WxH` | open art-direction image (no catalog template) | cinematic/billboard/anime work outside the 38 styles |

## The mental model

1. **Higgsfield was four scripts and a JSON folder.** Aggregators wrap the same models fal serves per-call. The moat was never access — it's owning your assets, prompts, and costs in one indexed place. That place is now `.agent/assets/manifest.jsonl` rendered as the board.
2. **Slop is a direction problem, not a model problem.** The A/B on the board proves it. So the system loads direction *mechanically*: craft-map → master skill → doctor pass → generate. Judgment is in the harness, not in remembering.
3. **One code path per model.** Wrapper-backed recipes refuse `run` and print the wrapper command; money-handling stays in the proven scripts; `index` carries provenance to the board.
4. **Taste compounds in owned containers**: style cards (`skills/generate/styles/`), named sweep recipes, the masters' skills. Every winner becomes retrievable and re-runnable.

## Capabilities shipped

### Asset Command Center (`/assets-board`)
**What:** `asset_index.py` sweeps all asset zones into an append-only manifest (reduce-by-path; sidecar/fal-log/higgsfield backfill; tombstones); `asset_gallery.py` renders thumbs + a self-contained file:// board — hero billboards on every view, shelf rows, hover video previews, facet dropdowns, lightbox with full prompt + copy actions; `--embed` makes an Artifact-publishable highlights cut. Palette: true black `#0a0a0a`, electric blue `#0f6fff`, white — approved register, don't drift it.
**When NOT to:** don't publish the main board as an Artifact (file:// images can't resolve) — highlights only. Don't hand-edit the manifest; fix the indexer or the engine append.
**Honest edges:** in-page refresh is only `location.reload()` — rescans need `/assets-board`; `keep`/`tags` curation fields exist in the schema but have no UI yet.

### `/generate` engine
**What:** recipe registry (12: gpt-image-2, nano-banana-2, kling-v3, seedance-480/720p, recraft-v3, minimax-speech/music verified; elevenlabs/ideogram/flux deferred stubs; seedance-1080p documented hard-block) + `generate_media.py` (quote/run/models/index; FalAdapter queue client; per-run budgets in `.agent/generate-run-state.json`; sidecar JSON per asset). Budget wiring composes with existing guards: `fal_budget_guard.py` generic mode ($1/call ceiling — bigger models must graduate to a named mode), `cost_gate.py fal-generic` row, anchored hook patterns.
**When NOT to:** people/photoreal → `higgsfield-soul` lane (BINDING); persistent characters → `/jcin-pipeline`; deferred stubs refuse until priced from fal's own pages.
**Honest edges:** elevenlabs price unverified; Higgsfield MCP spend is logged but ungated (known gap, deliberate); minimax-music untested in anger.

### Craft gate (BINDING)
**What:** `craft-map.md` — output type → master to load → doctor pass, plus the intent mirror for raw creative dumps and show-craft-with-quote for paid video. Enforced as `/generate` hard rule 0 and by memory `feedback_production-grade-floor-craft-gate`.
**Worked example:** the teaser. Freehand prompt → warped AI-slop motion. Same $0.65 through cinema-worldbuilder's M5 grammar (12° tele anchor, movement in cm and timestamps, anti-plastic block, diegetic sound bed) → production-usable push-in. Both takes are on the board as the permanent reminder.
**Honest edges:** the gate is instruction-layer, not hook-enforced; the universal "Mirror + one push-back" hook wiring is next session's first move.

### The direction layer (3 masters, 9 commands)
**What:** `skills/nick-st-pierre/` (layered construction, sweeps, style codes, reference-over-adjective, 8 anti-slop rules), `skills/dave-clark/` (8 causes of flat, look card from a 28-frame reel read, hybrid pipelines, shot-list-before-prompt), `skills/rory-flynn/` (9 Image Elements, moodboard sweeps → named recipes, style libraries, Keep/Change). All per the recency doctrine: model-independent cores, era-bound mechanics quarantined in dated appendices, receipts source-verified (Clark's unconfirmed hunt claims flagged never-to-use).
**Honest edges:** St. Pierre has no 2025–26 systematic teaching corpus — his layer is validated-against-recent, not taught-recently; his public Feb 2026 Higgsfield conflict is footnoted in the skill (using both = knowing choice). Flynn's famous 2023 cheat sheet was deliberately NOT reconstructed (unreadable + stale). Five masters remain in the dossier queue.

## Composition options (never forced)

| Stack | When it earns its cost |
|---|---|
| Clark shot list → cinema-worldbuilder prompt → seedance/kling | any video with money on it |
| St. Pierre sweep → style card → direct lane | pinning a new look you'll reuse |
| Flynn moodboard sweep → brand style library → client asset volume | client work (Angle Map deliverables, My.BPM) |
| direct lane + anime style cards → Kling animation → carousel/reel | the anime content lane |
