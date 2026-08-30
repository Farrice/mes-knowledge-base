# Kallaway / Sandcastles Reconciliation — 2026-08-30

## Compared

- Current Kallaway enrichment: `f1370d15b`
- Parked lane: `worktree-kallaway-sandcastles-forge` at `d4b75dcf0`
- Parked implementation commit: `396d9c80b`

The two builds were complementary, not competing copies. `f1370d15b` had the stronger research-control layer: metric classes, topic-vs-format cohort rules, the 2% engagement hygiene rule, first-party maturity states, and the human substance boundary. The parked lane had the stronger delivery layer: a $0 signal producer, Growth Blueprint workflows, durable engagement state, client rendering, intake, lead magnet, packaging, and proof artifacts.

## Ownership Lock

| Layer | Owner | Preserved responsibility |
|---|---|---|
| Signal collection | `execution/outlier_radar.py` | Collect, normalize, score, enrich, and emit the versioned pack. |
| Research judgment | `kallaway-ai-content-engine` | Choose metric class, cohort eligibility, signal hygiene, data maturity, and the human creative stop. |
| Client strategy product | `growth-blueprint-os` | Produce the dossier, whitespace map, bullseye, topic scan, format playbook, blueprint, intake, and reader-pure client package. |
| Qualified authority | `micro-fame-authority-density` | Separate reach, fit, trust, and commercial action; choose the decisive positioning contrast; enforce the four-rep evidence floor. |
| End-to-end production route | `kallaway-content-operating-system` | Route accepted evidence through strategy and production components without recreating Growth Blueprint artifacts. |

The shared seam is `execution/specs/outlier-radar-pack.schema.md`, now `pack_version: 2`.

## Strongest Non-Duplicative Implementation Preserved

- Parked source corpus and extraction receipts under `extractions/kallaway*` and `extractions/growth-blueprint-os/`.
- Growth Blueprint skill, 10 workflows, command bridges, guide, and registry entries.
- Outlier Radar, enrichment, intake, lead-magnet, package-export, and client-rendering code.
- Canonical engagement state and a bounded set of final client examples in `growth-lab/`.
- A frozen offline validation set under `extractions/kallaway/validation/`.
- `f1370d15b` research controls, now carried through the signal-pack fields and Growth Blueprint topic-scan preflight.
- Main's later authority-density companion and `1ilMGCxJBQY` evidence package, preserved alongside the additive `GmIn1W9V8Rs` signal-maturity evidence rather than choosing one source lane over the other.

## Deliberately Excluded From Integration

- `.agent/outlier-radar/` database, fetched transcripts, mutable packs, and run receipts.
- Parked handoffs, session reports, health/runtime state, and organization receipts.
- `.scratch/kallaway-sandcastles-forge/` intermediates after the bounded fixtures and proof were relocated.
- Duplicate historical renders, package copies, PDFs, and ZIP exports.
- Unrelated Oren commands, other skill edits, active-campaign state, and generated global briefing-room churn.

Nothing was deleted from the parked branch. These exclusions only keep mutable history and unrelated work out of the merge.

## Contract Changes

The public-data producer now emits:

- pack: `evidence_class`, `owned_corpus_size`, `data_maturity_state`
- record: `evidence_class`, `cohort_role`, `engagement_rate`, `signal_hygiene`, `rejection_reasons`

The producer assigns `PUBLIC_PROXY` and leaves cohort role `UNCLASSIFIED`. It computes the source-backed 2% engagement rule when likes/comments are available; missing engagement stays `REVIEW`, never a silent pass. The client-strategy consumer must assign `TOPIC_COHORT`, `FORMAT_ONLY`, or `EXCLUDE` and must not convert public reach into a demand or revenue claim.

## Verification Surface

Run from repository root:

```bash
.venv/bin/python3 extractions/kallaway/validation/verify_outlier_radar.py
.venv/bin/python3 extractions/kallaway/validation/verify_lead_magnet_bakes.py
python3 execution/skill_contract_test.py skills/growth-blueprint-os
python3 execution/export_format_guard.py extractions/kallaway/RECONCILIATION-2026-08-30.md
```

The historical live receipt is preserved under `extractions/kallaway/validation/live/`; the verifier upgrades it in memory to test the v2 contract without rewriting historical evidence.

## Reconciliation Result

| Check | Result |
|---|---|
| Python syntax for retained execution and verifier files | PASS |
| Signal-pack v2 contract, maturity states, 2% hygiene, and sabotage rejection | PASS — 14/14 |
| Lead-magnet full, exclusion/backfill, degraded, and enriched fixture bakes | PASS — 43/43 |
| Growth Blueprint prompts-v2 audit | PASS — 6/6 |
| Growth Blueprint, Kallaway AI, and Kallaway Content OS heartbeat gates | PASS — 21/21 |
| Client render + reader-purity lint | PASS — 0 findings |
| Staged diff whitespace/error check | PASS |
| Repository-wide system verifier | PARTIAL — Kallaway surfaces clean; two pre-existing Jay Sun registry errors remain outside this diff |

The Jay Sun negative control is present in the pre-merge `HEAD` indexes and absent from this merge's changed-path set.

The final main reconciliation preserved both later authority-density work and the parked signal-pack v2/Growth Blueprint build. Their overlap was resolved at the Content OS routing seam: authority density owns qualified-authority judgment; signal-pack v2 owns evidence maturity and proxy hygiene; Growth Blueprint owns client strategy artifacts.
