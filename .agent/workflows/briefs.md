---
description: Research-brief library — the Briefing Room index, brief rendering, playbook/asset/visual section kinds, agent context packs (Farrice Cain Premium Minimal report dialect); briefs also live on the Asset Command Center's 📋 shelf
---

# /briefs — Research-Brief Library (the Briefing Room)

The storage system: every brief lives at `deliverables/research-briefs/<slug>/` as a self-contained `<slug>-brief.html` plus `<slug>-brief.json` (provenance — the JSON is what gets re-rendered after edits), `<slug>-brief.md` (agent-paste mirror), and `<slug>-context.json` (**agent context pack** — every file path + source URL the brief references, with roles; feed it to any agent for instant grounding). The Asset Command Center (`/assets-board`) indexes the same directory as the **📋 Research Briefs** shelf.

## Open the Briefing Room (default front door)

// turbo
```bash
python3 execution/brief_library.py --open   # regenerates deliverables/research-briefs/index.html, newest first
```

Each card carries quick-copy buttons: **`path`** (absolute `.md` path — for Codex / Claude Code / anything with file access) and **`copy brief`** (the ENTIRE brief inline, context pack included — paste into any chat LLM with no filesystem). `md` / `ctx` open the mirror and the context pack.

## Open a single brief (or the board)

```bash
open deliverables/research-briefs/<slug>/<slug>-brief.html   # one brief
python3 execution/asset_index.py && python3 execution/asset_gallery.py && open .agent/assets/assets-board.html   # board view
```

## Produce a NEW brief

1. Do the research (Chain applies — route/load/ground as usual; scraping via `apify_client.py` or Monid per `directives/monid-usage-policy.md`).
2. Write the brief as structured JSON per the schema in `execution/render_brief.py`'s docstring. Core grammar: trust header (window/lens/sources/compiled), evidence rows each carrying `source_url` + `confidence` (VERIFIED/LIKELY/UNCONFIRMED — never render an unverified claim without its chip), ranked `decision` section, `deploy` copy-paste blocks, `caveats` reliability ranking, source `ledger`. Enrichment kinds (2026-08-06, all additive): `playbook` (numbered plays: command + touched paths + receipt), `assets` (linked-asset cards w/ copy-path), `timeline`, `flow`, `stats`, `matrix` (visual-learner aids, inline CSS/SVG only), `related` (swing links to briefs / `docs/solutions/` cards / missions). The context pack is generated automatically from everything the sections reference (+ optional top-level `context` extras).
3. Render + index:

```bash
python3 execution/render_brief.py <path/to/brief.json> --open
python3 execution/brief_library.py
python3 execution/asset_index.py && python3 execution/asset_gallery.py
```

Design system: **Farrice Cain Premium Minimal, report dialect** — tokens live in `templates/research-brief/template.html` `:root` ONLY (never inline in briefs); canonical brand source `_active/farrice-brand/premium-minimal/` incl. `REPORT-DIALECT.md` (why the italic-serif accent word + steel blue are sanctioned on report surfaces). Reference anatomy: `extractions/eddy-ballesteros/reference-corpus/brief-anatomy.md`. Living format reference (every section kind, once): `deliverables/research-briefs/design-system-showcase/`.

## Mission reports (brief-format build reports)

Mission/`/go` close-outs and night-shift builds SHOULD ship as briefs (exemplar: `deliverables/research-briefs/night-shift-2026-08-06/`): chip `<CONTEXT> · BUILD REPORT`, `summary` verdict → `decision` (what got built, ranked) → `evidence` (claims vs receipts) → `playbook`/`deploy` (how to run what shipped) → `caveats` → ledger. Render + `brief_library.py` refresh lands it in the Briefing Room automatically.

## Share-safe export (BINDING rule: internal briefs never go out)

Internal briefs carry absolute paths, run costs, candid strategy, and the agent context pack. **Never send one to a client or prospect.** The only client-visible form is the share variant:

```bash
python3 execution/render_brief.py <slug>/<slug>-brief.json --share   # → <slug>-brief-share.html
```

`--share` strips: context pack, all `file://` ledger links, run-cost/stack line, playbook `touches` paths, asset path rows/thumbs, file-path swing links, and the page quick-copy buttons. External URLs and all content sections stay. Rendered on demand only — not part of the default output set. **Limit:** `--share` strips the mechanical internals; costs or paths written into authored prose (deks, evidence text, ledger `used_for`) are the author's to redact — skim the share variant before sending.

## Re-render after editing a brief's JSON (or after any token change)

```bash
python3 execution/render_brief.py deliverables/research-briefs/<slug>/<slug>-brief.json
# token change? re-render the whole library:
for j in deliverables/research-briefs/*/*-brief.json; do python3 execution/render_brief.py "$j"; done && python3 execution/brief_library.py
```
