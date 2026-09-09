# Onboarding — Social Content Pipeline

## What This Does

Takes whatever you have (a YouTube video, a topic, a web article, a local file, or your existing LinkedIn/YouTube feed) and produces a platform-native social post with images — drafted in your voice, humanized, and ready to publish on LinkedIn, Instagram, Twitter, Threads, and 10+ other platforms via Zernio. After the first-run setup below, every subsequent run is fully automated.

## Inputs

| Input | Required | Example | Scenario |
|-------|----------|---------|----------|
| YouTube/video URL | Either | `https://youtube.com/watch?v=abc` | B |
| Topic or idea | Either | `"why most ai agents fail in production"` | C |
| Nothing / "from my sources" | Either | (empty) | D |
| Web article URL | Either | `https://example.com/post` | F |
| Local video/audio file | Either | `/path/to/video.mp4` | G |
| Finished caption + "generate image" | Either | `"My post: ... — generate image"` | A |
| Existing post + "adapt for X" | Either | `"adapt this for instagram: ..."` | E |

## Outputs

| What | Where | Format |
|------|-------|--------|
| Final post folder | `projects/00-social-content/{YYYY-MM-DD}/{post-slug}/` | `post.yaml` + `caption.md` + `image.png` (or `slide-N.png`) + `pipeline-log.md` |
| Pipeline log | `projects/00-social-content/{YYYY-MM-DD}/{post-slug}/pipeline-log.md` | Per-run markdown with phase timing table (v2.0.0: moved out of `logs/` so multiple runs on the same date don't collide) |
| Inspiration archive | `projects/00-social-content/{YYYY-MM-DD}/logs/inspiration/` | Saved transcripts, scraped posts, screenshot extracts |
| Published post | Platform-dependent (when `/tool-publisher` is run) | Live URL or draft URL in Zernio |

## How It Works (Phases)

1. **Config** — Reads `pipeline.config.yaml` and `.claude/skills/00-social-content/skill-pack/config/sys-config.md`. Verifies brand voice exists.
2. **Detect Scenario** — Inspects the trigger and routes to one of A-G (URL, topic, file, etc.).
3. **Gather Inspiration** — Transcript (B/G), trending research (C), feed scraping (D), or screenshot extraction (F).
4. **Briefing** — One-shot question for objective, format, and platform — only what wasn't in the trigger.
5. **Content Inference** — Derives `inferred_entities` (brands/people/events/products), `inferred_palette`, and `inferred_typography` from the gathered material. For single image: drafts the caption now.
6. **Visual Planning** *(sub-agent: `ssc-designer`)* — Builds a Visual Inventory (logos/icons/photos/screenshots available BEFORE planning) and the slide plan. Runs four blocking audits: per-slide real-image check, visual floor (`ceil(2N/3)` slides must be visual), icon-anchor classification (icons ≥25% of canvas count), and white-space audit (no empty canvas). Resolves image sources for every slide.
7. **Humanizer + Preview** — For carousels: humanizes silently, drafts the caption around the slide arc, then shows the plan for confirmation. For single: humanizes inline before image generation.
8. **Generate Images** *(sub-agent: `ssc-image-generator`)* — Executes the slide_plan the designer produced. Does NOT re-decide template, source, or render mode.
9. **Save and Present** — Writes `post.yaml`, `caption.md`, image files, plus a `pipeline-log.md` timing table inside the post folder. Asks if you want to publish.

End-to-end: typically 2-5 minutes for a single post, 4-8 minutes for a carousel.

## Checkpoints

**First run only:** Interactive onboarding (this guide) walks you through brand voice, API keys, and preferences. Takes ~5 minutes. Sets `_customized: true` in `sys-config.md` so subsequent runs skip onboarding.

**Every run:** Two pause points — Phase 4 briefing (skipped if all three answers are in the trigger), and Phase 8 review before publishing. Everything else runs automatically.

**Scenario E (repurpose):** Routes to `/mkt-content-repurposing`, which has its own per-platform review.

## Setup Checklist

### Step O1 — Show what I can do

The orchestrator surfaces the 7 scenarios in a single table on first run:

```
What you give me              → What I produce
─────────────────────────────────────────────────────────────────
A YouTube/video URL           → Transcript → Post + Images       (B)
A topic or idea               → Trend research → Post + Images   (C)
Nothing / "from my sources"   → Scrape feed → Post + Images      (D)
A web article URL             → Screenshot extract → Post + Imgs (F)
A local video/audio file      → Transcribe → Post + Images       (G)
Finished caption + "image"    → Images only                      (A)
Existing post + "adapt for X" → Repurpose for platform           (E)
```

### Step O2 — Check API keys

Reads `.env` if it exists. Shows a status line for each key:

```
API Keys status:
✓/✗ GEMINI_API_KEY        — image generation (primary)
✓/✗ OPENAI_API_KEY        — image generation (alt) + Reddit research
✓/✗ APIFY_API_KEY         — Scenario D: scrape LinkedIn
✓/✗ YOUTUBE_API_KEY       — Scenario D: YouTube digest
✓/✗ XAI_API_KEY           — Scenario C: X/Twitter trending
✓/✗ SCREENSHOTONE_API_KEY — Scenario F: cloud screenshots (optional)
✓/✗ ZERNIO_API_KEY        — publishing via /tool-publisher
```

For any missing key: "You can add it to `.env` anytime. Let's continue with what you have."

### Step O3 — Brand voice setup

Open an `AskUserQuestion` popup (never plain text, never `/<skill-name>` suggestion):

```
AskUserQuestion({
  questions: [{
    question: "Shall we capture your brand voice now? This makes every post sound like you, not like AI.",
    header: "Brand voice",
    multiSelect: false,
    options: [
      { label: "Yes, set it up now",
        description: "Runs mkt-brand-voice (~5-10 min)." },
      { label: "Skip for now",
        description: "Continues without a personalized voice — you can run it later." }
    ]
  }]
})
```

If user picks "Yes" → invoke `Skill(skill: "mkt-brand-voice")` directly. After it completes, confirm: "Brand voice saved ✓"

### Step O3.5 — Visual identity setup

Open a second `AskUserQuestion` popup:

```
AskUserQuestion({
  questions: [{
    question: "And your visual identity? It defines palette, typography and brand moves — without it the pipeline infers visuals per post.",
    header: "Visual identity",
    multiSelect: false,
    options: [
      { label: "Yes, set it up now",
        description: "Runs mkt-visual-identity (~10-15 min). Carousels start using your tokens." },
      { label: "Skip for now",
        description: "Continues with per-post inference." }
    ]
  }]
})
```

If user picks "Yes" → invoke `Skill(skill: "mkt-visual-identity")` directly. After it completes, confirm: "Visual identity (brand primitives) saved ✓ — now building templates."

### Step O3.6 — Template building *(runs immediately after O3.5 when mkt-vi completes)*

`mkt-visual-identity` stops at the brand bible (tokens, moves, identity). Template-building is owned here by the `00-social-content` orchestrator. Run these phases in sequence:

**Phase 4.95 — Per-ref slug + role assignment.** *(Replaces the old family clustering — there is NO upfront clustering and NO `template-families.yaml`.)* You (the orchestrator) do a QUICK read of each file in `brand_context/visual_refs/` via the Read tool (vision) ONLY to assign each ref its per-ref metadata:

- `slug` — kebab-case, derived from the ref's **composition + role** and kept **style-neutral** (e.g. `overlay-cover`, `body-pullquote`). Do NOT bake the medium/style into the slug — a `photo-`/`cartoon-` prefix leaks the style read into the builder's `template_dir` and primes it before it reads the ref. The medium is the builder's call, never the folder name's.
- `role` — `cover` | `body` | `cta`

This is **per-ref metadata, NOT cross-ref clustering**. Do not group refs, do not pick "canonicals", do not compare refs against each other, do not write any families file. Grouping into styles happens AFTER the templates are built (Phase 5.2), from the finished previews — never from the raw refs.

**Phase 4.96 — Brand-wide AI image style extraction.** Before any builder runs, read all refs whose Phase 4.95 quick read showed an image zone and infer the brand AI image style. Write to `brand_context/visual-identity/ai-image-style.md`. Skip if no ref has an image zone. See the `ai-image-style.md` format section in `references/template-authoring/shared/template-conventions.md` for the extraction schema and prompt-template rules.

The grade you extract fixes the brand's **IDENTITY — palette / accent / grain** — these are genuinely brand-wide (plus `text_policy`, the type-routing rule). The **STYLE — medium / lighting / subject_treatment** is NOT fixed brand-wide; it is read per-template from each ref by the builder (a cartoon ref ships a cartoon, a dramatically-lit ref ships dramatic light). The grade carries only the soft `default_*` for each style field. So when you extract:

- **Extract the IDENTITY structurally.** `palette` (bg / subject / accent), `accent`, and **`grain`** (the brand's paper/surface feel — promoted to its own key) are the brand-wide floor that gives the feed unity. Also set **`text_policy`** (`html-overlay` when this brand keeps all type as HTML/overlay — the usual case; `ai-allowed` only when it genuinely bakes integrated type). These stay brand-wide.
- **`default_medium`, not `medium`.** Record the brand's MOST-COMMON medium as `default_medium` — a soft starting point, used by a template only when its ref's medium is genuinely ambiguous. It is not a law that overrides what a ref plainly shows.
- **`default_lighting` and `default_subject_treatment`, not `lighting` / `subject_treatment`.** Same posture as the medium: record the brand's most-common lighting and treatment as soft FALLBACKS. Each template's lighting + treatment are READ from its own ref by the builder; the grade's `default_*` is used only when a ref is ambiguous. Do NOT record them as brand-fixed style.
- **More than one medium across the refs → `default_medium: mixed`.** Survey the image-zone refs: if they span more than one medium (e.g. a documentary-photo cover AND a flat-cartoon explainer body — the qa-kanban case, ref-01 photo + ref-04 cartoon), set `default_medium: mixed`. Do not collapse a mixed brand onto whichever medium happens to appear first. (Lighting/treatment likewise vary per ref — the `default_*` is just the most-common, never a forced uniform.)
- **The `prompt_template` is IDENTITY-ONLY.** It must NOT prepend a single-style opener — not a medium opener ("documentary photograph of …", "Photorealistic 3D-rendered …"), not a lighting clause ("soft studio lighting"), not a treatment clause ("isolated on light grey"). The "What to NEVER include" list must NOT carry a blanket STYLE-negative ("no illustration", "no photographs", "no dramatic shadows") — that opener/negative would force every template onto one style and kill the templates whose ref legitimately differs (the run-07 cause). Keep ONLY the palette / grain identity cues (and their negatives). The style enters per-template from the ref, via the builder's `image_style`. For a brand that is genuinely uniform on a style field you MAY keep that one clause — only then is it faithful.

**Phase 5 — Per-REF template build (1 builder per ref — CLOSED spawn contract).** For EACH ref in `brand_context/visual_refs/`, spawn ONE `ssc-template-builder` agent via the `Agent` tool (`subagent_type: "ssc-template-builder"`). Prefer parallel spawning.

The spawn carries **EXACTLY** the contract below — the seven wiring fields plus the fixed boilerplate, and **nothing else**. Fill only the bracketed slots; add no prose, no `notes:`, no reading of the ref. Copy this block verbatim:

```
Build ONE ship-ready template from ONE reference image, per your full workflow (Step 0 → Step 7).
ref_path: {absolute path to THE ref image — exactly one; there is no sibling_refs}
template_dir: {brand_context}/templates/{pool}/{slug}   (absolute)
pool: {the platform pool, e.g. linkedin-carousel}
slug: {from Phase 4.95}
role: {cover | body | cta, from Phase 4.95}
brand_context: {absolute path}
brand_name: {name}

The ref image at ref_path is your ONLY source for composition, medium, element roles, text routing, logo handling and legibility — derive every one of them yourself and record them in rationale.md §2; Check A gates that read. Feed the ref as --input-image when you generate. Run Check A before generating; the automatic quality gate + Check B (treatment-contract) + Check D (display-height) + the medium conference after; the 3-try ladder on any failure. Return your single Step-7 JSON on stdout.
```

The closing paragraph is **fixed boilerplate — byte-identical on every spawn**; only the seven slots above it vary. Two ways to break this contract: a spawn **missing** any field (under-specified), or a spawn **carrying anything beyond** these fields (over-specified — see the ❌ list).

**Post-spawn existence check (NON-NEGOTIABLE).** After EACH builder returns, verify on disk that ALL THREE exist: `{template_dir}/template.html` AND `{template_dir}/preview.png` AND `{template_dir}/rationale.md`. Any missing → that build did NOT happen, no matter what the agent's return text says → the phase is NOT complete → re-spawn that builder with the exact same contract. The deliverable is files on disk, never a text reply.

**The orchestrator NEVER writes template artifacts itself, and NEVER reads the ref FOR the builder** — not `template.html`, not `instructions.md`, not `rationale.md`, not manifest entries for templates it didn't verify on disk, and not the ref's composition/medium handed down in the spawn. All five of these have been observed in real runs and each one is a hard failure, not a judgment call:

- ❌ Carrying ANY reading of the ref in the spawn — the medium ("this IS a documentary photo", "flat cartoon"), which elements are occluded, what stays HTML vs AI-baked, logo handling, the legibility method, or any "read X into rationale.md §2" instruction. The composition read is the builder's sole job, gated by Check A; handing it down is RC1 (an asserted reading passed downstream, never confronted) and it blinds your own post-build QA — you cannot independently judge a preview against a brief you authored before the build. Seen in run-07 ref-10/ref-12: the spawn dictated the medium and got good previews, but that tested the renderer, not the reader — the per-ref medium read went unproven.
- ❌ Building the refs yourself in one generic agent (or inline) instead of spawning `ssc-template-builder` per ref.
- ❌ Writing template artifacts to the project ROOT with invented slugs instead of `{brand_context}/templates/{pool}/{slug}/`.
- ❌ Spawning "builders" without the contract above (no `template_dir`), accepting prose back, and calling that a build.
- ❌ Fabricating `instructions.md` + `manifest.json` yourself and declaring "Phase 5 Complete" with ZERO deliverables on disk. If the existence check fails, the ONLY valid move is re-spawn — never write the missing files yourself.
- ❌ **Authoring a `_patches/<x>/template.html` (or any derived template/asset) during a RE-RENDER** — onboarding Phase 6.7 OR content Phase 7 / 7.5. A hand-written patched template dropped outside the pool loses its `_shared/` sibling → the brand `@font-face` sheet is never injected → silent font fallback (the run-09 break). The ONLY valid re-render is via the canonical emit (`render_template.py --emit-edit-slide` / `--tweaks`, which co-copies `_shared/`) or a re-spawn of `ssc-template-builder` / `ssc-image-generator`. There is no third option, and "I patched it by hand and it looked right" is a hard failure, not a judgment call.

**This rule is NOT scoped to onboarding Phase 5 — it holds at EVERY re-render seam** (onboarding Phase 6.7, content Phase 7 / 7.5 / 7.6). The orchestrator NEVER authors, copies, or edits a `template.html` / asset by hand outside the canonical emit, anywhere in the pipeline.

You (the orchestrator) review each returned preview **against the ref** as a subjective quality signal — your eye MAY SUGGEST that something is weak (composition, taste, white-space) and surface it to the user as a WARN, but **"verified by eye" is NEVER proof of PASS**. The proceed-gate is the objective, deterministic check (existence on disk for every ref; for a re-render, the canonical-origin guard in `render_template.py` — resolvable `_shared/` sibling, origin not under `_patches/`). By-eye SUGGESTS; the objective gate CERTIFIES. You are not the ref's reader going in; that is the builder's job, gated by Check A. Pre-reading the ref for the builder is the anti-pattern above — it also destroys your QA, because a preview can only be judged honestly against the ref by someone who did not pre-author the read. Collect all results (and pass the existence check for every ref) before Phase 5.2.

**Phase 5.2 — Post-build organization + optional style grouping.** Run the protocol in `references/template-authoring/shared/analyze-templates.md`: verify/organize each built template in its `{pool}/{slug}/` folder + `_preview/{slug}.png` copies, assemble + write `manifest.json` for `ssc-designer` consumption (Phase 5.2 is the ONLY manifest writer — builders return their entry data in their stdout JSON and never write the file; N parallel read-modify-writes on one manifest is a race), then OPTIONALLY group the finished previews into styles (confirmed with the user via `AskUserQuestion`; ≥2 approved styles → write `brand_context/templates/{pool}/styles.json` per `references/decisions/styles.md`). Single-style brands skip the grouping.

> **The post-build sequence is CONCRETE — never a freeform menu.** After the templates build, the orchestrator runs the defined chain deterministically: 5.2 organize + manifest → (styles grouping decided ONLY via the structured `AskUserQuestion` popup, or skipped for single-style) → 5.5 gates → 6 brand bible → **6.7 auto-launch the Template Studio (mandatory, non-negotiable)**. ❌ **NEVER end onboarding by asking the user to choose** — e.g. *"Want me to launch the Studio now, or group the pool into styles first?"*. The Studio launch is not optional and not an offer; styles grouping is a structured popup, not prose. The orchestrator decides and acts on the concrete next step — it does not hand the user an open question about what to do next.

**Phase 5.5 — Brand-level gates (G2 + G4).** After all templates settle:
```bash
uv run .claude/skills/mkt-visual-identity/scripts/validate_brand.py --brand-context brand_context/
```
G2: every `image_bearing:true` move must have ≥1 supporting template. G2 failure is a WARNING — popup to resolve or skip. Phase 6 proceeds regardless.

**Phase 6 — Brand bible v2 (with template gallery).** After all templates are ready (or rejected):
```bash
uv run --with playwright --with pillow python .claude/skills/mkt-visual-identity/scripts/generate_brand_bible_pdf.py
```
This v2 differs from the brand bible generated by mkt-vi (Phase 4.7) by including the template gallery (3×3 grid of `_preview/*.png`). Confirm both the PDF path and any backup in the phase summary.

**Phase 6.7 — Template Studio review *(blocking; mirrors Phase 7.5 for the POST)*.** The builder marks templates `status: ready` from its own auto quality-gate, but the USER has not yet seen them. Before the `≥1 status:ready` hard rule below acts as the proceed gate, launch the **Template Studio** so the user can walk the pool, compare each template's reference ↔ render side-by-side, edit on the canvas, and **approve**.

> **🚨 MANDATORY ACTION — LAUNCH, DO NOT ASK. 🚨** The instant template-building finishes (and `--no-preview` was NOT passed), you **MUST immediately launch the Template Studio yourself** by calling `content_studio.py {brand_context}/templates/{pool} --mode template` via `Bash` with `run_in_background: true`. This is the **ONLY allowed next action** — there is no decision to make. You **MUST NOT** end your turn with a question like *"Próximo passo natural: abrir o Template Studio… Quer que eu lance agora?"* or *"Want me to launch the Studio?"* — **asking for permission to launch instead of launching is a HARD ERROR.** The launch is automatic and is NOT subject to the user's approval; the user approves the *templates inside* the Studio, not the act of opening it. Print the URL and tell the user to review/approve; THEN block on their approval. The only thing that suppresses the launch is the `--no-preview` opt-out flag passed up front — never a chat question.

- **Skipped when:** the user passed `--no-preview` (opt-out — proceed straight to the hard rule).
- **Launch (script-only, background, auto-open) — UNCONDITIONAL:** you MUST execute this; it is not a proposal. The ONLY allowed action is calling `content_studio.py` in **template mode** on the brand pool via `Bash` with `run_in_background: true`:
  ```bash
  python .claude/skills/00-social-content/scripts/content-studio/content_studio.py {brand_context}/templates/{pool} --mode template
  ```
  The pool dir is the launch target — `content_studio.py --mode template` accepts a pool dir directly (it resolves the manifest and walks every `status: ready`/`approved` template; the "Studio operates on the brand_context pool directly" decision, 2026-06-09). It picks a **free port**, starts a stdlib `http.server`, and **auto-opens the browser** — the user runs no command. **NEVER use `Write` to author preview/editor HTML inline.** If the script can't cover a case, extend the script — never bypass it.
- **Relay + block.** Print the URL the server prints and one line: *"Template Studio just opened — for each template, compare its reference vs render (the ‹ › arrows step through the pool), edit text/layout live, read the builder's notes, and click Approve. Type 'approve' when you're done."* Then **WAIT for explicit user approval/close.** Do not run the hard rule automatically.
- **❌ Anti-pattern (HARD ERROR):** Ending onboarding with a question like *"Próximo passo natural: abrir o Template Studio… Quer que eu lance agora?"* / *"Want me to launch the Studio?"* — **the launch is automatic and not subject to the user's permission.** If you find yourself about to ask whether to open the Studio, STOP and call the `Bash` launch instead. The user's approval applies to the templates *inside* the Studio, never to the act of opening it.
- **What the Studio does.** The conference panel shows ref ↔ render per template plus the builder's **Template Card rationale** (form · per-block treatment + why · edit_mode · extraction — read from each template's `instructions.md`) as review notes/improvement suggestions next to the compare. `/approve` persists the user's tweaks (`render_template.py --tweaks`, no AI) and marks the template `approved` in the manifest.
- **Fallback (server can't start — locked-down env / no free port):** surface the manifest's per-template previews instead — point the user at `brand_context/templates/{pool}/_preview/*.png` (and per-template `preview.png`) for a static by-eye review, and have them confirm in chat. Do NOT write inline HTML; the static `preview_editor.py <template_dir>` path is the per-template editor fallback if the user wants to edit one.

After the user is done (or opted out), run the hard rule below and proceed.

**Hard rule:** after Phase 6.7, confirm `brand_context/templates/{pool}/manifest.json` has ≥1 entry with `status: "ready"`. If not, the pipeline cannot proceed to content generation — surface the gap to the user.

Confirm: "Templates ready ✓ ({N} templates built — one per ref, brand bible updated)"

### Step O4 — Set preferences

Use `AskUserQuestion` to ask **one preference at a time**. After each answer, run the conditional dependency check before moving to the next.

**Q1 — Default platform**
- options: `linkedin`, `instagram`, `twitter`, `threads`
- default: `linkedin`
- check: if `instagram`/`twitter`/`threads`, verify `ZERNIO_API_KEY` is in `.env`

**Q2 — Language**
- options: `en`, `pt-BR`, `es`, `other`
- default: `en`
- if `other`: ask which language via plain-text follow-up

**Q3 — Default format**
- options: `auto` (decide from content), `carousel`, `single`, `text`
- default: `auto`

> **No "image style" question.** Visual style (palette, typography, template family per slide) is **inferred per post** from (a) `brand_context` if it exists, and (b) the content itself (e.g., a post about a red+black+white sport team → those crest colors; a post about Claude Code → Anthropic orange + monospace headers). Asking the user "color / notebook / technical / mono?" up front confuses non-designers and locks the wrong default for half the posts they will write.

### Step O5 — Save and confirm

Write pipeline behaviour answers to `pipeline.config.yaml` and operational/path answers to `.claude/skills/00-social-content/skill-pack/config/sys-config.md`. Set `_customized: true` in `sys-config.md`. Tell the user:

> "All set! Saved:
> Platform: {platform} · Language: {language} · Format: {format}
>
> Visual style is decided per post (from your brand_context if set, or inferred from the content).
>
> Edit anytime in `.claude/skills/00-social-content/skill-pack/config/pipeline.config.yaml`
>
> Ready. Try: `/00-social-content` — give me a topic, a URL, or just say 'from my sources'."

### Conditional dependency map

| User choice | Requires | How to check | What to tell them |
|-------------|----------|--------------|-------------------|
| Platform: instagram/twitter/threads | `ZERNIO_API_KEY` | grep `.env` | zernio.com to get key → add to `.env` |
| Format: carousel/single | `GEMINI_API_KEY` or `OPENAI_API_KEY` | grep `.env` | need at least one image key |
| Source mode: "from my sources" | `APIFY_API_KEY` + `YOUTUBE_API_KEY` | grep `.env` | both keys for full Scenario D |

## Configuration Files

After first-run onboarding, your choices live in two places:

```
Pipeline config (technical — image provider, sources, publishing mode):
  .claude/skills/00-social-content/skill-pack/config/pipeline.config.yaml

Operational config (output paths, source toggles):
  .claude/skills/00-social-content/skill-pack/config/sys-config.md

Brand voice:
  brand_context/voice-profile.md
```

All three files have inline comments. Edit them anytime to change defaults for future runs.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "Voice profile missing" | Run `/mkt-brand-voice` — onboarding will resume after |
| "Both image keys missing" | Add `GEMINI_API_KEY` or `OPENAI_API_KEY` to `.env` |
| Scenario B fails (no transcript) | Pipeline auto-falls back to Scenario F (screenshot) |
| Scenario D returns nothing | Check `tool-linkedin-scraper/config/sources.md` and `tool-youtube/config/sources.md` |
| Scenario G fails (transcription) | Verify `python3` + `whisperx` available; install ffmpeg if missing |
| Images come out off-brand | Update `brand_context/assets.md` and add reference images to `brand_context/visual_refs/` (both at project root) |
| Carousel slides drift visually | Sub-agent always anchors to slide 1; if drifting, regenerate slide 1 first |
| `/tool-publisher` says "MCP not connected" | Copy `.mcp.example.json` → `.mcp.json`, set `ZERNIO_API_KEY` in `.env`, restart Claude Code |
