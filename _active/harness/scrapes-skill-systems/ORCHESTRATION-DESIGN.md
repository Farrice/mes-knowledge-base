# Scrapes Skill Systems — Orchestration Design (LIVING; update in place)

*Owner: Farrice. Built 2026-09-02 in lane `worktree-scrapes-routing` from a read of every Scrapes SKILL.md, the four `ssc-*`/`l2s-*` workers, and our router, ledger, and craft-room code. Each claim is marked **VERIFIED** (read on disk, file:line) or **INFERRED** (my reading of how it will behave). Decision deltas and what would reverse each call are stated where they matter. Companion docs: `PRECEDENCE-MAP.md` (which side wins per skill), `INTEGRATION.md` (install facts), `RESUME-BRIEF.md` (state).*

## 0. The ask, in his words, and the shape of the answer

> "Take all of the Scrapes skills and integrate it fully into our system: proper routing, proper orchestration, built out so that it's compounding intelligence and smart usage of our tools and skills versus the isolatedness of them, and me having to use them as a separate pilot." — and, the same night: "nothing just auto-routes or orchestrates poorly to the wrong place, working on the wrong client and the wrong thing, pulling from the wrong context."

**The answer is a cockpit, not a rebuild.** His `00-social-content` is the engine we could not build ourselves (his 2026-09-02 verdict). We do not recreate it and we never edit it. We wrap it with four things: routing that knows it exists, a **BRAND LOCK** that decides whose context feeds it, seam hand-offs where our pens beat his defaults, and the loops that make run N+1 start where run N ended. Decision delta vs. rebuilding: zero maintenance of a parallel pipeline, full benefit of every Scrapes update, and the only cost is the wrapper drift risk in §7.

## 1. Current wiring, as it was on disk before this build (VERIFIED)

| Fact | Where |
|---|---|
| The per-prompt router scored only `skills/*/SKILL.md`; the 36 vendored skills under `.claude/skills/` were invisible to it. | `execution/find_skill.py` `build_index()` (glob `SKILLS_DIR/*/SKILL.md`), `load_or_build_index()` staleness probe |
| `routing_enforcer.BINDINGS` (41 entries) had zero Scrapes rows; `directives/routing-bindings.md` likewise. | `execution/routing_enforcer.py`, `directives/routing-bindings.md` |
| `arsenal_index.py` indexed `vendor:<name>` entries (family `scrapes-skill-systems`, `menu_status: reachable`) but nothing on the routing path reads the arsenal index. | `execution/arsenal_index.py:274-305`; `skill_router_hook.py` never imports it |
| `mint_menu_wrappers.py` cannot mint for vendor entries (`kind == "skill"`, hardcoded reachable → falls out of every class). | `execution/mint_menu_wrappers.py:185,208,218-220` |
| `ssc-designer`, `ssc-image-generator`, `ssc-template-builder` are dispatched only by `00-social-content` (Phases 0, 5.0.5–5.7, 7); `l2s-content-packager` only by `00-longform-to-shortform` Phase 8. | `.claude/skills/00-social-content/SKILL.md:94-110`, `references/pipeline-phases.md`, `references/onboarding.md:150-167` |
| `00-social-content` is a **prompt program**: Claude executes SKILL.md phase by phase; sub-agents are called via the Agent tool with a documented input contract and return a structured block. Nothing is compiled. | `SKILL.md:226-229`, `.claude/agents/ssc-designer.md:21-45,82-113`, `ssc-image-generator.md:20-45` |
| Phase 1 **hard-gates** on `brand_context/visual-identity/tokens.json` + ≥1 `status: ready` template in `brand_context/templates/<pool>/manifest.json`. No pool → "fail loudly, no legacy fallback". No pool existed for any brand. | `SKILL.md:114-152,165-177` |
| Scenario A ("finished text → images only") skips their briefing, draft, carousel-caption, and humanizer phases and keeps inference → designer → preview → images. It is a maintained entry point. | `references/inputs/input-text.md:14-37` |
| `tool-fact-checker` is not wired into `00-social-content` at all. Only `00-youtube-to-ebook` Step 4 has a fact seam. | grep across `00-social-content/` (zero hits); `00-youtube-to-ebook/SKILL.md` |
| Research cache: Phase 3 Scenario C checks `projects/str-trending-research/{date}/{slug}.md` younger than `trending_research_freshness_days` (7) before invoking `str-trending-research`. | `references/inputs/input-topic.md:12-14`; brief shape `str-trending-research/references/brief-template.md` |
| Self-improvement: every skill except `00-social-content` reads/writes `{decoupled_base}/context/learnings.md` under `## {skill}`. The file did not exist. Declared, dead. | `.claude/skills/meta-skill-creator/SKILL.md:152-161`; consumers e.g. `viz-image-gen/SKILL.md:32,319` |
| Single-brand assumption: 33 `sys-config.md` copies hold absolute paths to one `brand_context`; prose in `pipeline-phases.md:157,401` says "at project root". But the override plumbing exists: `ssc-designer` takes `brand_context_path`; `render_template.py --brand-context`; `content_studio.py --brand-context`; `ssc-image-generator` already passes `--brand-context {bc}`. | `viz-image-gen/scripts/render_template.py:2111`, `content_studio.py:4781`, `ssc-image-generator.md:406-407` |
| Publishing paths (`tool-publisher`, `tool-zernio-social`, `mkt-short-form-posting` post step, `tool-video-upload` upload) are unwired on purpose. `tool-linkedin-scraper` is dead (Apify retired). | `INTEGRATION.md` rules 3–4 |

## 2. What this build wired (VERIFIED on this lane; tests in `tests/test_scrapes_routing.py`)

1. **Router sees the skills.** `find_skill._skill_md_paths()` also globs `.claude/skills/*/SKILL.md` (symlinks skipped, `status: archived` skipped); records carry `vendor: scrapes`; the router tags them `[SCRAPES]`. 35 of 36 index (`tool-zernio-social` lacks parseable frontmatter and is DO-NOT-USE anyway).
2. **Six bindings → six front doors.** `scrapes_social_carousel → /social-carousel`, `scrapes_social_post → /social-post`, `scrapes_social_repurpose → /social-repurpose`, `scrapes_deck_build → /deck-build`, `scrapes_video_to_shorts → /video-to-shorts`, `scrapes_video_to_ebook → /video-to-ebook`. Negative signals keep `/parallax`, `/ghostwrite` (plain LinkedIn text), and the Ink + Steel Blue readouts out of the Scrapes lane. Bindings stay suggestions (Compass doctrine); the router line reads `★ /social-carousel [SCRAPES engine]`.
3. **Front doors are hand-written thin wrappers** in `.agent/workflows/` (the minter cannot own vendor skills; shape copied from `social-content-studio.md`). Each: BRAND LOCK → our seams → the Scrapes skill by name with explicit brand paths → compounding writes → a `Never` list. Slash shims + `SLASH_COMMANDS.md` rows regenerate via `generate_slash_commands.py`.
4. **BRAND LOCK** — `execution/scrapes_brand.py` (§4).
5. **`context/learnings.md` exists** at the repo root with `# General` and one `## <skill>` section per skill we route to. The declared hook is now live for the other 35 skills too.

## 3. Seam map — who owns what, pipeline by pipeline

Rule (Farrice, 2026-09-02, PRECEDENCE-MAP "Craft-room routing"): **one integrator writes, one veto reads, never six seats on one hook.** Scrapes owns machinery. Our pens own copy. Our receipts own facts. Our classifier is the gate. Our budget guard is the wallet.

### 3.1 `00-social-content` (carousel + single post) — the deep one

| Their phase | Seam | Owner after this build | Mechanism |
|---|---|---|---|
| 3 GATHER (C: topic) | research | **ours**: `execution/research.py run` (Gemini → Perplexity → free floor, receipts, budgets) | brief written to `projects/str-trending-research/<date>/<brand>--<slug>.md` in their template shape → their cache check finds it. `str-trending-research` never runs (needs XAI/Groq keys we don't hold). |
| 3 GATHER (B: YouTube, F: article, G: local file) | source | **theirs** (`tool-youtube`, `tool-web-screenshot`, `tool-transcription`) | keep; these are mechanized tools we lack. **INFERRED**: hand the `inspiration_pool` to our craft room before any draft. |
| 4 BRIEFING, 5.0 draft caption, 5.4 carousel caption | copy | **ours**: hook pen + integrator per BRAND.yaml (`pens.hook`, `pens.integrator`) | skipped in Scenario A by their own design. We deliver caption + slide script (`SLIDE n \| role \| headline ≤8w \| body ≤40w \| image concept`). Their first-slide formulas are the **shape check** on our hook, never the pen (v1 evidence: formulas alone scored 6/10). |
| 5.5 / 6 humanizer | voice | **ours**: `prose_classifier.py check` is the gate; `/tool-humanizer deep` may run first (blind bar #2) | skipped in A; we run our gate before hand-off. |
| — (absent) | facts | **ours**: `claim_audit.py check --strict` before hand-off; `tool-fact-checker` optional second pass (TEST FIRST) | the pipeline has no fact seam; we add one in front of it. |
| 5.0 inference, 5.0.5–5.7 designer | visual plan | **theirs**: `ssc-designer` with `brand_context_path` explicit | our slide script goes in as `inspiration_pool` with "headlines and bodies are FINAL"; after return we diff `slide_plan` headlines against our script; one corrective re-dispatch, else stop. **INFERRED** that the designer honors this; the v2 Jen run suggests yes, blind bar #1 confirms. |
| 7 images | render | **theirs** when a `status: ready` pool exists (`render path: scrapes-template-pool`); **ours** when it does not (`renderer_fallback`, Jen: `valley-editions/editions.py`) | `scrapes_brand.py check` decides before Phase 1 can fail. Every AI slide: craft-map master on `image_concept` (nano-banana grammar / gpt-image-2 director) → `openai_budget_guard.py check` → `ssc-image-generator`. Cost line stated before dispatch. |
| 0.7 / 7.5 studios | approval | **Farrice** | if absent, the run parks at the gate as `status: draft`. |
| 8 SAVE → publish | send | **human** | `tool-publisher` off. |

### 3.2 `mkt-content-repurposing` (via `/social-repurpose`)
Their platform mechanics; our ICP-verbatim check (the buyer's researched words appear exactly), voice check per BRAND.yaml, classifier per platform file. TEST FIRST vs `/atomize` on a Parallax edition (blind bar #3).

### 3.3 `00-slides` (via `/deck-build`) — thin
Research seam = ours (same cache trick). Outline approval is his; `claim_audit --strict` on the outline before he sees it. Renders on the brand's `tokens.json` via `viz-frontend-slides`. Readouts and research briefs never come here (Ink + Steel Blue readout OS owns them).

### 3.4 `00-longform-to-shortform` (via `/video-to-shorts`) — thin
All machinery theirs (yt-dlp, WhisperX, 5-category clip scoring, OpenCV reframe, FFmpeg caption burn — none of which edit bay has). POST phase disabled; no TTS/clone; classifier on package text; cost stated for any `viz-image-gen` illustration.

### 3.5 `00-youtube-to-ebook` (via `/video-to-ebook`) — thin
The one pipeline with a real fact seam and per-stage files (`draft-article.md` → `fact-check-report.md` → `reviewed-article.md` → `final-article.md`). Their checker runs; **ours is the veto** (`claim_audit --strict` before humanize and before PDF); classifier after their humanizer; his Step 5 review stays mandatory.

## 4. BRAND LOCK — multi-client routing that cannot guess (his 2026-09-02 requirement)

**Convention.** Every brand declares itself once: `<brand-root>/brand_context/BRAND.yaml` with `brand`, `display`, `kind: owner|client`, `aliases`, `client_root`, `brand_context`, `output_base`, `research_cache`, `template_pools`, `renderer_fallback`, `voice` (dial or canon list), `pens` (hook / integrator / veto), `research`, `never`, `notes`. Registered today: **farrice** (root `brand_context/`), **jen** (`_active/clients/jen-listings/brand_context/`), **andrea** (stub, NOT READY). Gigi's root lives on lane `worktree-gigi-engine-run`; register her when it lands. `python3 execution/scrapes_brand.py list`.

**Resolution (VERIFIED by tests).** `resolve --from-prompt "<ask>" --cwd "$PWD"`: exactly one brand's alias in the ask → lock. Zero or two+ → exit 3 AMBIGUOUS, one question ("which brand?"), stop. A client alias anywhere beats any owner default; the owner is never a fallback. `--cwd` under a `client_root` resolves that client **only when nobody is named**. The printed `BRAND LOCK:` line opens every pipeline-log and rides in every sub-agent dispatch, so a wrong brand is visible in the first line of the run, not the last slide.

**Isolation (VERIFIED by tests).** `check <brand> --pool <pool>` fails (exit 2) when `brand_context`, `voice-profile.md`, `tokens.json`, or the pool is missing (or names the renderer fallback), and runs a **cross-brand check**: every declared path must resolve under this brand's roots and under no other brand's. Jen's earlier run landed in the shared `projects/00-social-content/` tree; her BRAND.yaml now points `output_base` under her client root, and the shared research cache takes a `<brand>--` slug prefix so two brands never share a brief.

**Why manifests, not the symlink swap (decision delta).** The alternative was pointing the root `brand_context/` at the active client. Full coverage of every "project root" assumption, but it dirties a tracked directory and the merge tool would need a never-carry rule. The manifest path uses override plumbing the skills already ship. **What would reverse it:** a Scrapes script that reads `<project_root>/brand_context/` with no override and cannot be steered by `sys-config.md`. Jen's first real run is the test; if one appears, escalate to a lane-local swap plus a `worktree_lane.py` always-ours rule for `brand_context`.

**Per-client `CLAUDE.md` inheritance** stays the prose layer (identity, voice test, anti-patterns). BRAND.yaml is the machine layer the pipelines read. They point at each other; neither duplicates the other.

## 5. Compounding — how one run makes the next one better

**Before a run (every front door, Step 0):** BRAND.yaml → brand voice canon → last 3 entries under the skill's heading in `context/learnings.md` → `memory_facade.py "<brand> carousel <topic>" --top 8` (solution cards, sovereign memory, auto-memory) → the brand's `calibration-log.md` when it exists.

**After a run (Step 5):**
| Write | Loop it feeds | Existing owner |
|---|---|---|
| one `asset_index.py` manifest line per slide/clip (`src`, `model`, `prompt`=image concept, `cost_usd`, `path`) + `asset_gallery.py --quick` | Assets board; copy-path + prompt provenance (sacred) | `execution/asset_index.py` contract `:20-25` |
| one line under `## <skill>` in `context/learnings.md` | their declared self-improvement hook, now live; read at the next Step 0 | `meta-skill-creator/SKILL.md` contract |
| `chain_runner.py finalize --skill vendor:<skill> --workflow <door> --type Content\|Client Work --factual N` | `.agent/finalize-runtime.jsonl` → `evolution_orchestrator.py` (skill weights, binding review queue) → Notion performance log | `execution/chain_runner.py:2283-2350` |
| `handoff_store.py save --thread <brand>-social` | resumable threads, `/resume` | `execution/handoff_store.py` |
| `voice_ratchet.py add` on Farrice's felt verdict of a hook (owner brand only) | `calibration-log.md` → RECOMPILE nudge at 5 pending | `execution/voice_ratchet.py` |
| `research.py` receipt + the brief in their cache | next run on the topic within 7 days is free | their Phase 3 cache check |

**INFERRED, to confirm after five runs:** `evolution_orchestrator.py` will start weighting `vendor:00-social-content` finalizes like any skill, which lets the binding review queue tell us whether `/social-carousel` fires on the right prompts. What would reverse the design: finalize records with `--skill vendor:*` being dropped by a skill-existence check in `chain_runner` (check `_resolve_skill` on the first real run).

## 6. What we do NOT rebuild, and what stays off

Never rebuild: `00-social-content`, the workers, the template studio, brand_context (both), the budget guard, the precedence map, the constitution block, Jen's canvas artboards. Never edit inside `.claude/skills/*` (hash-gated; extend via `brand_context/`, `context/learnings.md`, wrappers). Stays off: every publish path (sends stay human), `tool-linkedin-scraper`, `str-trending-research` (keys), `mkt-content-analytics` (Zernio). Not installed: Agentic OS (its own project root; would collide).

Blind bars still open (Farrice taps): #1 carousel (one supplement teardown, `/social-carousel` vs the current LinkedIn path), #2 de-slop (`/tool-humanizer deep` vs hand pass, both through the classifier), #3 repurpose (`/social-repurpose` vs `/atomize` on a Parallax edition).

## 7. Risks, plainly

1. **Wrapper drift.** Our doors reference their phases by name. A Scrapes update that renames a phase or changes the designer's input contract silently changes a seam. Mitigation: the doors name phases, never copy them; after `npx @scrapes/installer` update, rerun `arsenal_index.py build --rebuild` and read `CHANGELOG.md` of `00-social-content` before the next run. **INFERRED** low frequency (their changelog shows monthly-ish).
2. **Designer rewrites our headline.** Mitigated by the post-return diff + one corrective dispatch; confirmed or refuted by blind bar #1.
3. **Template pool cost.** `ssc-template-builder` is AI-first (GPT Image). His pool: 4–6 refs × est. $0.10–0.30 = under $2, guard-checked, his approval in Template Studio. Jen's pool waits on her six inputs.
4. **Their gates encode a generic taste** (VERIFIED 2026-09-03 on his pool). `ssc-template-builder`'s Check D demands display cap-height ≥ 8.0cqw; the brand's h1 is 72px (6.67cqw). Builders inflated headlines 40–60% and pushed everything down the canvas to dodge a ring-probe false positive. Farrice's Studio read: "typography, spacing, hierarchy done poorly." Standing fix: a post-build **craft pass** in the pool (ours) back to the ref geometry, canonical re-render, decisions in `REVIEW-NOTES.md`. Second gate: `render_template.py`'s autosize requires the SINGLE-LINE width to fit, so any headline that wraps naturally shrinks toward its floor (72→37px observed). Rule: headline values carry `<br>` line breaks; written into `/social-carousel` Step 2.
5. **Brand registry sprawl.** New client → one BRAND.yaml or the lock refuses. That is the intended failure: a refusal, not a wrong brand.

## 8. Files this design owns

`execution/scrapes_brand.py` · `execution/find_skill.py` (vendor glob) · `execution/skill_router_hook.py` (tags) · `execution/routing_enforcer.py` (six bindings) · `directives/routing-bindings.md` (six rows) · `.agent/workflows/{social-carousel,social-post,social-repurpose,deck-build,video-to-shorts,video-to-ebook}.md` · `context/learnings.md` · `_active/farrice-brand/brand_context/BRAND.yaml` · `_active/clients/jen-listings/brand_context/BRAND.yaml` · `_active/clients/andrea-dj/brand_context/BRAND.yaml` · `tests/test_scrapes_routing.py`.
