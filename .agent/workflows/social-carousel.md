---
description: "/social-carousel — Any brand's carousel: BRAND LOCK → research with receipts → OUR pens write caption + slide script → claim audit + classifier → Scrapes 00-social-content Scenario A (designer, template pool, images, studios). Cost stated before any AI slide. Never posts."
---
<!-- front door for the vendored Scrapes Skill Systems (2026-09-02). Machinery = .claude/skills/00-social-content (never edited); seams = ours. Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md -->

# /social-carousel — carousel for a named brand, our copy, their machinery

State the scale in one line before starting: one carousel, N slides (3–7), one caption, one brand.

## Step 0 — BRAND LOCK (never guess)
1. `python3 execution/scrapes_brand.py resolve --from-prompt "<the ask>" --cwd "$PWD"`.
   - exit 3 (ambiguous or nobody named) → ask ONE question: "Which brand: farrice, jen, andrea?" Stop until answered.
   - exit 0 → copy the printed `BRAND LOCK:` line verbatim; it opens the pipeline-log and every dispatch.
2. `python3 execution/scrapes_brand.py check <brand> --pool <platform>-carousel` (default `linkedin-carousel`; Jen defaults to `instagram-carousel`).
   - `render path: scrapes-template-pool` → their designer + image generator will render.
   - `render path: brand-renderer` → visuals go through the brand's own renderer (BRAND.yaml `renderer_fallback`); Scrapes stops after the slide plan.
   - `blocked` → stop and say what is missing (tokens.json, voice-profile.md, or a template pool). Do not improvise a pool.
3. Load, in this order: BRAND.yaml → the brand's voice canon (`voice.canon` or VOICE-CARD §7 dial for Farrice) → the last 3 entries under `## 00-social-content` in `context/learnings.md` → `python3 execution/memory_facade.py "<brand> carousel <topic>" --top 8`.

## Step 1 — RESEARCH with receipts (ours, into their cache)
1. `python3 execution/research.py run "<topic> <audience>" --depth standard` (quick when the topic is evergreen). Read the receipt; label every fact VERIFIED / LIKELY / UNCONFIRMED.
2. Write the brief in the Scrapes shape (`.claude/skills/str-trending-research/references/brief-template.md`) to `projects/str-trending-research/<YYYY-MM-DD>/<brand>--<slug>.md`. The brand prefix is mandatory: two brands never share a brief.
3. For a client, add a claims ledger to the brief: every number, street, product, or date with its source line.

## Step 2 — CRAFT ROOM (one integrator writes, one veto)
1. Hook pen per BRAND.yaml `pens.hook`: client → `.agent/workflows/alyssa-stalker-hook-reframe.md` (Topic + Who + Lens placement) then `/vicious-hook` (Luke Iha: consequence first, open loop, Germanic words, stakes). Farrice → VOICE-CARD dial + `/vicious-hook`. The Scrapes first-slide formulas (`.claude/skills/00-social-content/references/carousel-first-slide-copywriting.md`) are the SHAPE CHECK on the final hook, never the pen.
2. Integrator per `pens.integrator` writes ONE take: the caption (narrative → facts → door → attribution for Jen; VOICE-CARD register for Farrice) and a slide script — for each slide `SLIDE n | role | headline (≤8 words) | body (≤40 words) | image concept`. Cover hook = the chosen hook, verbatim. **Headlines carry their line breaks as `<br>`** (one thought per line, as the brand's frames do): the Scrapes renderer's autosize shrinks any headline that must wrap on its own, so a broken headline keeps the brand's 72px while an unbroken one collapses to 37px (evidenced 2026-09-03).
   Slot ergonomics for the editorial pool (evidenced 2026-09-03, blind bar 01): SOURCE_LABEL / EVIDENCE_LABEL ≤ ~50 chars (uppercase letterspaced, one line or they clip); VERDICT_WORD and the band HEADLINE are one line; FOOTER_TOPIC on the close is the short CTA word; portrait photo slots (two-photo, photo-right) take portrait crops, band and evidence slots take wide crops.
3. Veto seat per `pens.veto`: the brand-as-itself read. One pass. Two rejected takes → stop and go back to the input (spiral brake), never a third variant.
4. Machine floor, all must pass before hand-off:
   - `python3 execution/claim_audit.py check <caption+script file> --strict` (tags present, UNCONFIRMED density ≤30%). Fails → fix facts or cut the claim.
   - Optional: `/tool-humanizer deep` against the brand's voice-profile.md FIRST (blind bar #2 pending), then always `python3 execution/prose_classifier.py check <file>` — FLAGGED never ships.
   - Jen only: `python3 execution/jen_stamp_lint.py <file>` and the fair-housing lint from `/listing-package`.

## Step 3 — COST LINE (before anything paid)
State: templates $0 · AI slides = (count of FULL_AI/HYBRID_AI slides in the plan) × est. $0.04–0.19 (GPT Image, quality-dependent) or $0 on the Gemini path · running month from `python3 execution/openai_budget_guard.py status`. If any AI slide is planned, run `python3 execution/openai_budget_guard.py check --n=<count> --quality=<q>` — DENIED means no AI slides this run (template-only degrade), never a retry.

## Step 4 — SCRAPES MACHINERY (Scenario A, brand paths explicit)
Invoke the `00-social-content` skill with the finished caption + slide script and the words "finished text, just the images" (Scenario A). Pass and repeat in every dispatch:
- `brand_context_path` = BRAND.yaml `brand_context` (absolute), `template_pool` = the resolved pool dir, `output_base` = BRAND.yaml `output_base`, `brand_name` = display name.
- `ssc-designer` gets our slide script as `inspiration_pool` with the instruction: headlines and bodies are FINAL — plan visuals around them, do not rewrite them. After it returns, diff its `slide_plan` headlines against our script; any rewrite → re-dispatch once with the correction, else stop and report.
- Every `render_template.py` / `content_studio.py` call carries `--brand-context <brand_context>`. Run the renderer as `uv run --quiet --with playwright python …/render_template.py` and pass `--data` as a JSON FILE path (`slide-NN.data.json`), never inline: inline JSON longer than a filename crashes the renderer (Errno 63, evidenced 2026-09-03).
- For each FULL_AI / HYBRID_AI slide, run the `image_concept` through the craft-map master before `ssc-image-generator` (`skills/generate/references/craft-map.md`: nano-banana grammar or `gpt-image-2` director). Freehand prompts never fire.
- `render path: brand-renderer` → stop after the slide plan; render with the brand's renderer (Jen: `python3 _active/clients/jen-listings/06-system/valley-editions/editions.py` per its README) into `output_base/<date>/<slug>/`.
- Template Studio and Content Studio are Farrice's approvals. If he is not present, leave the run at the studio gate with `status: draft` and say so.

## Step 5 — COMPOUND (the run feeds the loops)
1. `python3 execution/asset_index.py` contract: one manifest line per slide PNG (`src=scrapes/ssc-image-generator|brand-renderer`, `model`, `prompt`=image_concept, `cost_usd`, `path`), then `python3 execution/asset_gallery.py --quick`.
2. Append one line under `## 00-social-content` in `context/learnings.md` (what to keep, what to change, verdict pending).
3. `python3 execution/chain_runner.py finalize "<brand> carousel: <slug>" --skill vendor:00-social-content --workflow social-carousel --type <Content|Client Work> --intent N --expert-score N --adversarial N --factual N --notes "BRAND LOCK: <brand> | cost: $X | render: <path> | Verification: PASS"`.
4. `python3 execution/handoff_store.py save --thread <brand>-social --status <shipped|draft> --hint "<slug>: what needs his tap"`.
5. When Farrice gives a felt verdict on the hook: `python3 execution/voice_ratchet.py add --verdict pass|fail --line "<hook>" --why "<his words>"` (Farrice's brand only; client verdicts go to the client's calibration notes).

## Never
Edit inside `.claude/skills/*`. Post or schedule (sends stay human; `tool-publisher` stays off). Run a client's copy through Farrice's voice card. Let the Scrapes draft phase write a client's words. Start without the BRAND LOCK line.
