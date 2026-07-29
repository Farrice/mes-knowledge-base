# MOVE PLAN — Global Organization Sweep

**Generated** 2026-07-28 · **Status**: awaiting Farrice's approval · **Nothing has moved.**

Built from `project_filer.py plan` across all 70 projects (read-only, no `--out`) plus
`artifact_router.py classify` for the loose files outside any project. Zero scan errors.

## What this is

| Tier | Count | Meaning | Your job |
|---|---|---|---|
| **CLEAR** | 67 files / 25 projects | Router is certain (confidence ≥ 0.8), no control-plane referrer | Skim the table, veto anything that looks wrong |
| **JUDGMENT** | 3 filer items + 6 structural decisions | No correct default exists | **Decide these** |
| **LEAVE** | 73 files | Pinned — referenced from control-plane files, never moves by rule | Nothing |

94 inbound references get rewritten automatically as part of the CLEAR moves, so no link breaks.
Full per-file detail is in the scan JSON; this doc is the decision surface.

---

## CLEAR — 67 files, auto-fileable

Each row is one project's loose root files going into their canonical subfolders.
Reference rewrites are automatic; a `verify` pass must show 0 broken links after each.

| Project | Files | → Subfolder(s) | What they are | Inbound refs |
|---|---|---|---|---|
| `_active/_ledgers` | 20 | 02-research | autopilot run ledgers | 0 |
| `projects/prediction_market_arb` | 7 | 02-research | research | 3 |
| `_active/prompt-renaissance` | 6 | 01-source | source | 0 |
| `_active/platform-bakeoff` | 3 | 04-deliverables | deliverable | 16 |
| `_active/positioning-cowork-2026-07-25` | 3 | 04-deliverables | deliverable | 5 |
| `_active/chris-restaurants` | 2 | 04-deliverables + 90-exports | deliverable, export | 0 |
| `_active/dwa-threads-engine-2026-07-05` | 2 | 04-deliverables | deliverable | 6 |
| `_active/elevation-track` | 2 | 04-deliverables | deliverable | 8 |
| `_active/harness-apex-2026-07-07` | 2 | 04-deliverables | deliverable | 1 |
| `_active/notion-intellectual-library` | 2 | 04-deliverables + 90-exports | deliverable, export | 4 |
| `_active/parallax-icp-offer` | 2 | 06-system + 04-deliverables | system, deliverable | 1 |
| `projects/Ken's Fasting Digital Product` | 2 | 04-deliverables | deliverable | 6 |
| `projects/Kens_Fasting_Digital_Product` | 2 | 04-deliverables | deliverable | 8 |
| `_active/alignment-architect-2026-07-07` | 1 | 04-deliverables | deliverable | 9 |
| `_active/coach-cooz` | 1 | 04-deliverables | deliverable | 7 |
| `_active/codex-repeatability` | 1 | 04-deliverables | deliverable | 1 |
| `_active/disney-crowd-app` | 1 | 90-exports | export | 1 |
| `_active/farrice-final-10` | 1 | 04-deliverables | deliverable | 7 |
| `_active/jen-listings` | 1 | 04-deliverables | deliverable | 2 |
| `_active/josh-dancewear-brand` | 1 | 04-deliverables | deliverable | 1 |
| `_active/memory-bakeoff` | 1 | 04-deliverables | deliverable | 4 |
| `_active/operator-core-backport` | 1 | 04-deliverables | deliverable | 0 |
| `_active/pmf-brief-2026-07-07` | 1 | 04-deliverables | deliverable | 0 |
| `projects/andrea-dj` | 1 | 04-deliverables | deliverable | 0 |
| `projects/farrice-website` | 1 | 03-working-drafts | draft | 4 |

---

## LEAVE — 73 files pinned

Referenced from a control-plane file (`CLAUDE.md`, `.agent/workflows/`, `directives/`,
`execution/`, `skills/`). Pin rule: these never move and their referrers are never
rewritten, because a control-plane file often hardcodes the path.

Top pin sources: `.agent/workflows/merch-os.md` (9), `avatar-machine.md` (8),
`cooz-flywheel-v5.md` (3), `4c-architect.md` (2), `create-skill.md` (2),
`missions.md` (2), `CLAUDE.md` (2).

**One thing worth knowing**: 2 files are pinned by `execution/archive/google_operator_*`
— an *archived* script. That's a stale pin holding real files in place. Not urgent,
but it means the pin set is slightly wider than it needs to be.

---

# JUDGMENT — decisions only you can make

## J1. Three low-confidence moves (filer says 0.5)

| File | Proposed | My read |
|---|---|---|
| `projects/farrice-website/styles.css` | `01-source/styles.css` | **Don't move.** This is a live website file. `styles.css` next to `index.html` is how the site loads; filing it into `01-source/` breaks it. Website source is code, not an artifact. |
| `_active/prompt-wiring-os-2026-07-13/forge-wave.js` | `01-source/forge-wave.js` | Same class — an executable script, not a document. Safe to move only if nothing shells out to it by path. |
| `_active/codex-repeatability/v4-high-taste-output-os.metadata.json` | `01-source/…` | A `.metadata.json` sidecar. It must live *beside* the file it describes, or the pairing breaks. Move only with its partner, or leave. |

**Recommendation: leave all three.** They're the 3 of 143 the router itself flagged as uncertain, and in each case the uncertainty is real.

## J2. Duplicate clusters — which copy is canonical?

These are not true duplicates. They're **one project split across trees by naming drift**, with non-overlapping contents.

**Ken's Fasting — 3 dirs, 23 files, no overlap**
- `projects/Ken's Fasting Digital Product` (9) — strategy, sprint plan, swarm research
- `projects/Kens_Fasting_Digital_Product` (2) — instagram strategy, landing page copy
- `deliverables/kens-fasting-package` (12) — the assembled client package (`START_HERE` + 6 numbered folders)

→ **Proposed**: consolidate into one `projects/kens-fasting/`, with the assembled package as `04-deliverables/`. Kills the apostrophe name in the same move.

**Jen Santulan — 3 dirs, but 3 different things**
- `_active/jen-listings` (21) — the **live** per-address listing engine, has its own `CLAUDE.md`, touched 07-25
- `projects/jen-santulan` (29) — the foundation/repositioning/messaging BOS work, cold since 05-31
- `deliverables/jen-santulan` (2) — one listing's content (21212 Ingomar Ct)

→ **Proposed**: `deliverables/jen-santulan/*` → `_active/jen-listings/` (it's a listing). `projects/jen-santulan/` → `_active/jen-listings/00-foundation/`, since memory and `CLAUDE.md` inheritance both point at `jen-listings` as the live home. **Your call** — if the BOS work is a separate engagement, it stays separate.

**PMF — 4 dirs, 3 of them holding a single file**
- `pmf-offer-package-2026-07-05` (8+ files, properly foldered) ← the substantial one
- `pmf-brief-2026-07-07` (1), `pmf-offer-map-2026-07-07` (1), `pmf-ofm-options-2026-07-07` (1)

→ **Proposed**: consolidate all four into `_active/pmf-offer-shelf/`. **Caveat**: memory (`project_pmf-offer-shelf-2026-07-07`) points at `pmf-offer-map-2026-07-07`. The filer rewrites memory-dir referrers automatically, so the pointer follows — but you should know the anchor moves.

**Coach Cooz / Trendscale** — `deliverables/coach-cooz-final` (32, content from 03-19) and `projects/trendscale-trial` (11,637) + `_active/trendscale-brief-revision` (87). Both are working-dir + snapshot pairs. → **Proposed**: leave for now, lower value than the three above.

## J3. `projects/` vs `_active/` — one tree or two?

19 dirs in `projects/`, **16 with no entry file**, 6 of them single-file stubs all dated 2026-05-31 (one abandoned batch: `_ck2free`, `course-graveyard-coach`, `invisible-expert`, `sfv-first-time-homebuyers`, `teardown-kajabi`, `teardown-skool`).

Nothing in the system distinguishes the two trees — `artifact_router` scores `_active/<x>` at 0.98 and `projects/<x>` at 0.78, but that's the only difference. Jen Santulan currently lives in **both plus `deliverables/`**.

→ **Options**: (a) merge `projects/` into `_active/` and have one tree; (b) keep two and define the split explicitly (e.g. `_active/` = current work, `projects/` = client engagements); (c) leave as-is and just add entry points. **Recommend (a) or (b) — (c) preserves the ambiguity that caused this.**

## J4. Archive candidates — cold, and nothing references them

Zero memory/knowledge/directives/CAMPAIGN references, no activity in 90+ days:

| Project | Last touched | Files |
|---|---|---|
| `projects/remotion-studio` | 2026-03-15 | 14,680 |
| `projects/farrice-website` | 2026-03-27 | 3 |
| `_active/strategic-clarity` | 2026-03-31 | 11 |
| `projects/unbottlenecked_blueprint` | 2026-04-03 | 6 |
| `_active/chris-restaurants` | 2026-04-09 | 54 |
| `projects/Claude Code Harness Analysis` | 2026-04-02 | 2,108 |
| the 6 single-file stubs (05-31) | 2026-05-31 | 1 each |

→ **Proposed**: `_archive/` with a one-line stub pointer left behind so a grep still finds them.
**Not proposed for archive** despite being cold: `javier-human-values`, `parallax-icp-offer`, `content-system-audit`, `andrea-dj` — all referenced from memory, so JUDGMENT per the brief's never-archive-by-inference rule.

## J5. `deliverables/` — 22 loose files, no correct default

The router returns **ambiguous for all 22** (no project alias matches). `deliverables/` is
also outside `_sweep_project_roots()`, so nothing has ever swept it. Grouped by my read:

| Files | Proposed home | Confidence |
|---|---|---|
| 5× `prediction-market-*`, `polymarket-kalshi-arbitrage-feasibility.md`, `trading-dashboard-demo.html` | `projects/prediction_market_arb/` | high — name match |
| `design-brief-linkedin-carousel-*` (2), `linkedin-ghostwriting-outreach-playbook.md` | `_active/linkedin-launch/` | high |
| `momentous-reputation-analysis-2026-07-25.md` | `_active/linkedin-launch/01-research/` | high — Momentous is a supplement brand, your Proof-to-Market ICP |
| 3× `phase2-karpathy-audit-*`, `playwright-retrofit-audit-2026-05-14.md`, `design-md-health-2026-05-11.md` | `_active/system-audit/` | medium |
| `MyBPM-SEO-AEO-Optimization.md`, `mybpm-event-planning-analysis.md` | MyBPM — but the only MyBPM dir is `_active/mybpm-merch-os-run-1`, which is merch-specific | **needs you** |
| `suzuki-general-use-demo-pack.md`, `prompt-course-consumer-posture.md`, `IN-BETWEENER_pitch_deck.html` | unclear | **needs you** |
| `coachella-weekend-2-family-plan.md` | personal, not a project | `_archive/`? |

## J6. Root strays — 5 files

All unpinned, all classified ambiguous.

| File | Evidence | Proposed |
|---|---|---|
| `bakemargin-desktop.png`, `bakemargin-mobile.png` | 1.2 MB + 894 KB, 07-20. Referenced only from `extractions/ray-amjad-agentic-ladder/blind-pass-*` — byproducts of an eval run | `_archive/` or `extractions/ray-amjad-agentic-ladder/05-assets/` |
| `page-farrice-profile-full.yml` | 68 KB Playwright accessibility snapshot of your LinkedIn profile page | `_active/linkedin-launch/01-research/` |
| `fleet-status.md` | Generated by `/system-audit`, **zero references**, 4.5 months stale, regenerable | `_archive/` |
| `SLASH_COMMANDS.pdf` | 87 KB from 2026-03-05 vs the live `.md` at 200 KB / today. Wildly out of sync, regenerable | `_archive/` or delete |

---

## Execution contract if you approve

Per project, one at a time, `linkedin-launch` first and alone (it needs the J-decisions on its
`03-*`/`04-*` taxonomy collision applied by hand *through* the filer):

```bash
python3 execution/project_filer.py plan  --project "<abs dir>" --out /tmp/p.json
python3 execution/project_filer.py apply --plan /tmp/p.json --dry-run   # read it
python3 execution/project_filer.py apply --plan /tmp/p.json
python3 execution/project_filer.py verify --project "<abs dir>"          # MUST PASS
```

Never hand-author plan JSON (the filer now refuses plans without its provenance stamp).
Never `apply` across more than one project. A verify FAIL stops the run. Commit per project.
Every apply writes a receipt and flushes an inverse `mv` to `.agent/organization/REVERT-<date>.sh`
**per move**, so a mid-run crash is always recoverable.
