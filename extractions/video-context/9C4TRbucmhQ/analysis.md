# Source-to-Skill Analysis — RoboNuggets `/generate` (Higgsfield Replacement)

**Source:** "This 1 Claude Skill fully replaces your Higgsfield Subscription" — Jay E / RoboNuggets, https://www.youtube.com/watch?v=9C4TRbucmhQ (15:41, watched 2026-08-02: full captions transcript + 14 targeted frames).

## Extracted method (what Jay built)

1. **Four-step flow** (flow diagram @12:37): Route Model → Prep References → Generate Media → Log + Gallery.
2. **Routing rules** (tooltip @12:44): per-media-type defaults (Nano Banana 2 Lite images, Kling 3.0 video), named-model override, provider order cheapest-first (Kie.ai → fal.ai → WaveSpeed), per-model recipe files in `models/`, **paid video always cost-quotes and waits for an explicit go**.
3. **Prompt-level controls** (@1:10): per-run budget ceilings ("total budget 3USD, don't exceed"), multi-model comparison batches, hard content rules, cheapest-provider instruction.
4. **Output discipline** (@1:45): named variants table (name/model/ratio/concept); generated paths feed follow-up work in-session (image → Kling animation → website build, @2:30).
5. **Local gallery** (@13:33–14:17): masonry "Generations" console (~1,600 items), filters/search/sort/pagination, Models + Styles dropdowns; Styles panel = click-to-copy style cards with reference thumbs. Build spec (@15:19): one self-contained HTML file, no server, click-tile-copies-path.
6. **Ownership argument**: Higgsfield = subscription wrapper over the same models; pay-as-you-go aggregators + local storage = you own every asset and prompt, no deletion window, no training-rights ambiguity.

## How it landed in this system (extend, never rebuild)

| Source element | Our implementation |
|---|---|
| `/generate` skill + models/ recipes | `skills/generate/SKILL.md` + `skills/generate/models/*.json` + `execution/generate_media.py` (quote/run/models/index) |
| Cheapest-first provider chain (Kie→fal→WaveSpeed) | **fal-only by Farrice's decision** (already wired, budgeted); provider-pluggable `PROVIDERS` dispatch for later |
| Paid-video quote-then-go | Already house law (`fal_budget_guard.py`, `quote_required` recipes) — kept, surfaced in SKILL hard rules |
| Prompt budget ("$3 total") | `--run-id/--run-budget` + `.agent/generate-run-state.json` |
| Log every prompt beside asset | Sidecar JSON per asset + `.agent/assets/manifest.jsonl` (append-only, reduce-by-path) |
| Generations gallery + Styles panel | `execution/asset_index.py` + `execution/asset_gallery.py` → `/assets-board` (indexes ALL asset zones, not just generations — Farrice's scope call) + `skills/generate/styles/<slug>/` registry |
| Model routing defaults | Deferred to existing BINDING lanes first (`creative_router.py`: people→Soul, style→fantastic-posters), then recipe defaults |

## Skill System Contract

| Field | Value |
|---|---|
| Source evidence | This package: `video-context-ledger.md` (timestamped), `uncertainty-report.md`, 5 evidence frames |
| Objective | In-house pay-as-you-go creative generation + visual asset command center; no Higgsfield subscription dependency |
| Components | `/generate` (skill+workflow+3 born-v2 prompts) · `generate_media.py` · model recipes · styles registry · `asset_index.py` · `asset_gallery.py` · `/assets-board` · `fal_budget_guard.py generic` mode · `cost_gate.py fal-generic` row · anchored `cost_gate_hook.py` patterns · creative_router audio lanes |
| Step order | assets-board first light → engine + budget wiring → registration/forge gate → hook anchoring (own commit) → cold-start proof |
| Handoffs | wrapper output → `generate_media.py index` → manifest → board; engine run → manifest+sidecar → board auto-refresh |
| Human checkpoint | Farrice ack on commit `fix(cost-gate-hook)` (money-gate trigger surface); paid-video go remains per-call |
| Validation | `asset_index.py --verify` · idempotent sweep · `renaissance_audit.py` 0 fail · `cost_gate_hook.py --self-test` · quote/run/refusal tests (all green 2026-08-02) |
| Behavior-changing proof | Cold-start run: real campaign assets (teardown carousel, 08-04) generated quote-first under a $3 prompt budget, landing on the board with provenance |
| Result surface | `/assets-board` (visual), variants tables in-conversation, `/generate` cheat table |
| Context policy | SKILL.md hot via skill listing; recipes/styles/prompts on-demand; this package cold |
| Reuse hook | New model = one recipe file; new provider = one adapter + Farrice cost decision; gallery pattern reusable for any future visual index |
