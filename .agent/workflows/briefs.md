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

## What ships as a brief (Visual Delivery Doctrine — Farrice-ratified 2026-08-06, both harnesses)

**Reusable deliverables default to visual briefs.** The line: outputs meant to be REUSED ship as briefs; quick answers, corrections, and conversation stay conversation. This is the default offer, never a cage. **Markdown stays first-class** (Farrice, 2026-08-06): standalone md deliverables remain fully legitimate — the doctrine adds a visual layer, it never demotes md. Every brief already ships its md mirror; any markdown, brief-born or standalone, has a paved road to the Drive content vault (below). Lineage: the Nate B Jones work-primitive rule ("a document is complete only when an agent can use it to decide, act, check, and know when not to act" — `skills/semantic-document-library-os/`); the brief's `.md` mirror + context pack ARE the agent half of that contract, the HTML is the human half. Grounding: before this doctrine, 96% of all deliverables shipped as markdown (338 md vs 13 html, audit 2026-08-06).

Family recipes (chip · category · default priority · section spine):

| Family | Chip pattern | category / pri | Section spine |
|---|---|---|---|
| Research | `RESEARCH BRIEF · <lens>` | `research` / P2 | summary → evidence (chips+sources) → bars/stats → decision → deploy → caveats → ledger |
| ICP / avatar profile | `ICP PROFILE · <name>` | `icp` / P1 | summary (identity-level) → stats → matrix (resistance map) → evidence (VERBATIM buyer language — never elevated) → decision (how to write to them) → deploy → caveats. Exemplar: `deliverables/research-briefs/icp-invisible-expert/` |
| Extraction dossier | `EXTRACTION · <expert>` | `extraction` / P2 | summary → evidence (genius patterns w/ timestamps) → playbook (signature workflows) → related (skill dir) → caveats (era-bound appendix flagged) → ledger (source video) |
| Client deliverable | `<CLIENT> · <asset>` | `client: <name>` / P1 | per production-sheet verdict; `--share` render is the ONLY outward form |
| Build receipt | `<CONTEXT> · BUILD REPORT` | `build report` / P2 | summary verdict → decision (what shipped, ranked) → evidence (claims vs receipts) → playbook/deploy → caveats. Exemplar: night-shift-2026-08-06; /go close-outs offer this per go.md Stage 3 |
| Mission brief | `MISSION · <arena>` | `mission` / P1 | summary (facts + 1-line resume) → stats (session count/deliverables/assets/days) → spark (momentum) → progress (lifecycle stage) → decision (blockers & forks) → assets → playbook → timeline → related → caveats. Compiled nightly by `/sweep` from session records (performance-log, handoffs, missions, artifacts, commits); LIVING (updated in place, sessions append to timeline). Synthesized slots (lede/next_move/why/caveats/operator_read) allow-listed — LLM can only write meaning, never mutate figures. Example: `mission-proof-to-market`. |

Semantic-document activation map (how the 13-section semantic schema lands in brief kinds): Decision Rules→`decision` · Quality Tests/Failure Modes→`caveats`+`evidence` chips · Execution Protocol→`playbook`/`deploy` · Inputs/Outputs/Authority→`stats`/`matrix`/`assets` · Maintenance→`ledger`+`timeline`.

**Portable backstop → the Drive content vault** (Farrice has 30TB — leverage it): `--gdoc` uploads any brief as a native Google Doc on request (graceful on OAuth expiry). Any standalone markdown ports the same way: `python3 execution/md_to_gdoc.py <file.md> [--folder-id …|--create-folder …|--mirror-folders]` (styled tables, pageless-friendly). Offer the Drive port whenever a deliverable is worth keeping outside the repo — content vaults and asset libraries live there.

## The librarian (housekeeping — deterministic, runs on every regen)

`brief_library.py` keeps the shelves: `archive <slug>` / `unarchive <slug>` (also live buttons on room cards when served) · `audit` (counts + stale + broken context-pack paths; same line renders in the room header). **Auto-currency**: periodical categories (`zeitgeist`, `angles`) auto-archive after **30 days** (constants at top of `brief_library.py` — tune freely, never a cage). **Archived is never gone**: files, md mirrors, and context packs stay exactly where they are — still openable, citable in `related` sections, and agent-feedable; the shelf filter changes presentation only, and `unarchive` is always one action away. Supersession: set `"superseded_by": "<slug>"` in the old brief's JSON; the room chips it with a link to the successor.

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
