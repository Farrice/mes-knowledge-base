---
name: analyze-templates
description: POST-BUILD organization protocol. Runs AFTER every ssc-template-builder has returned and passed the existence check — verifies/organizes the built templates, completes the manifest for ssc-designer consumption, and optionally groups the finished previews into styles (styles.json).
---

You are the orchestrator, AFTER Phase 5 (`references/onboarding.md`): every ref got its own
`ssc-template-builder`, every builder returned, and the post-spawn existence check passed for every
`{template_dir}` (`template.html` + `preview.png` + `rationale.md` on disk). This protocol organizes what
was built. It creates NO template artifacts — if something a builder owns is missing, the move is
re-spawn that builder, never write it yourself.

## Step 1 — Verify + organize the built templates

For each built template:

- It lives in `{brand_context}/templates/{pool}/{slug}/` — the `template_dir` from the spawn contract.
  A template anywhere else (project root, an invented path) is misplaced: move it into place, or
  re-spawn the builder with the correct `template_dir`.
- The folder carries the builder's full set: `template.html`, `instructions.md`, `rationale.md`,
  `preview.png`, `assets/ref-canonical.png`.
- `{brand_context}/templates/{pool}/_preview/{slug}.png` exists (the preview copy the gallery and the
  static review fallback read). Missing → copy it from `{template_dir}/preview.png`.

## Step 2 — Manifest completeness (the ssc-designer contract)

`{brand_context}/templates/{pool}/manifest.json` is what `ssc-designer` and the Content/Template Studio
walk — an incomplete or wrong entry makes the template invisible or unrenderable downstream. **This step is
the ONLY manifest writer.** Builders never touch `manifest.json` — each returns its entry data in its stdout
JSON (builder Step 7); N parallel builders doing read-modify-write on one file is a race that drops entries.
Assemble the manifest HERE, from the on-disk template dirs + the builders' returned JSONs. Each built
template must have ONE entry, matching the existing manifest schema:

```json
{
  "id": "<slug>",
  "file": "<slug>/template.html",
  "role": "cover | body | cta",
  "status": "ready",
  "tone": ["<light | dark | ...>"],
  "image_zone": "<full-bleed | contained | none>",
  "render_mode": "<TEMPLATE | HYBRID_AI | HYBRID_REAL | ...>",
  "needs": ["HEADLINE", "..."],
  "optional": ["EYEBROW", "..."],
  "fits": ["<content shapes this layout serves>"],
  "summary": "<one line describing the layout>"
}
```

Cross-check each entry against the template's `instructions.md` (`## Slots` → `needs`/`optional`;
`## Inventory` → `image_zone`; the AI-image contract → `render_mode`). Write one entry per template that
EXISTS on disk (passed the existence check), never inventing entries for templates that don't.

## Step 3 — OPTIONAL style grouping (after build, from the finished previews)

Now — and only now — look at the FINISHED previews (`_preview/*.png`) and ask: do subsets of these
templates read as coherent looks that would combine into one carousel? Grouping happens here, post-build,
because the previews show what was actually built; grouping raw refs upfront is the old flow and produced
mis-attributed builds.

- Propose groupings to the user via `AskUserQuestion` — e.g. *"these {N} combine into one style:
  {labels}"* — one option per proposed grouping plus "keep one flat pool". ALWAYS confirm; never
  auto-group.
- **≥2 approved styles** → write `{brand_context}/templates/{pool}/styles.json` per the schema in
  `references/decisions/styles.md`, including its role-completeness requirement (each style needs ≥1
  image-bearing hero, ≥1 image-less cta, ≥2 bodies spanning light + dark).
- **Single-style brands skip this step entirely** — no `styles.json`, the designer uses the flat pool.

## Rules

- Builders build; the orchestrator organizes. NEVER author `template.html` / `instructions.md` /
  `rationale.md` here — a missing builder artifact means re-spawn `ssc-template-builder` with the same
  spawn contract.
- A style is a composition family, NOT a palette/icon recolor (see `references/decisions/styles.md`).
- Keep it lean: verify, correct, group, move on — Phase 5.5 gates and Phase 6.7 Template Studio review
  follow.
