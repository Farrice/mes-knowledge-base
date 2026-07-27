---
date: 2026-07-27
session: extract-os
tier: operator-guide
status: enriched
---

# Extract OS — v3.0 One Spine, One Dial — What We Built 2026-07-27 and How to Use It

> This session elevated `/extract` to forge parity: output size is now DERIVED by `execution/extraction_manifest.py` instead of asserted, thin sources auto-enrich from the same expert before anyone settles for a small build, extensions forge-scale by rule, and every run closes with an asset scan. Proof: the Meg Heckman trust layer was forge-scaled same-session from 1 workflow + 1 prompt to 4 workflows + 6 prompts (skill v1.2, 16 workflows, all gates clear). Companions: `.agent/workflows/extract.md` (the v3.0 pipeline), memory card `project_extract-v3-adaptive-forge.md` (the four locked decisions).

## ⚡ If you only read 10 lines

- `/extract <anything>` now ships forge shape by default — ≥7 prompts + 3-tier workflows when the corpus earns it. No more 1-workflow surprises.
- Sizing is deterministic: `python3 execution/extraction_manifest.py corpus|derive|check`. RICH ≥8,000 words → 8-15 workflows forced-Deep; MID 5-8k → 4-7; THIN → honest count + `fidelity: low`, never padded.
- Thin source? The pipeline auto-enriches: ≤4 more sources from the SAME expert (yt-dlp/WebSearch, free only), then re-measures. Short video ≠ small output.
- Existing expert? Extension Mode forge-scales the new layer: 2-5 workflows + ≥5 prompts INTO the existing skill (`--extension`). "Extend don't rebuild" = where assets live, never how few.
- Every run ends with asset verdicts: orchestrator (BUILD at ≥8 wf) / agent (always) / plugin (RECOMMEND-only, hard-gated) / council seat.
- `/extract-forge` is unchanged: the explicit 3-checkpoint full-ceremony session when Farrice wants per-phase control.
- Report contract: manifest-vs-shipped table + enrichment ledger + per-workflow one-liners — "what did it actually do" is never a mystery again.
- New Meg Layer-5 engines, all fireable: `/meg-micro-moments` (audit) · `/meg-trust-email-engine` (3 trust emails) · `/meg-community-voice` (reply OS) · `/meg-fan-flywheel` (UGC + rhythm).
- Doctrine line: when two pipelines share quality gates, the gap is whoever decides output size — that decision is now a derived number.
- First thing to run next: `/extract` on a fresh short expert video to watch enrichment + manifest fire live (never tested end-to-end).

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/extract <source>` | Forge-shape skill: manifest-derived workflows/prompts, references, agent, asset scan | Any expert source, any length — the default harvest path |
| `python3 execution/extraction_manifest.py corpus --dir extractions/<slug>` | Word count + RICH/MID/THIN verdict | Before/after enrichment; deciding if more sources are needed |
| `... derive --patterns N --deliverables N --corpus-words N [--extension] --out <json>` | The build manifest (tiers, prompt floor, orchestrator flag) | After MES extraction, before building anything |
| `... check --skill skills/<dir> --manifest <json>` | Shipped-vs-floor audit (observe-mode; `--enforce` to fail) | Verification step of every extraction |
| `/extract-forge <source>` | Same shape via full ceremony: Vision doc + 3 checkpoints | You want to steer each phase of a critical-domain extraction |
| `/meg-trust-email-engine` | Welcome + customer-life + co-creation emails, sendable | Any brand whose welcome automation is an invoice |
| `/meg-community-voice` | Voice card + 100% comment-backlog replies + daily system | Ads running with unanswered comments |
| `/meg-fan-flywheel` | "Spotted" features + build rule + never-skip-a-week rhythm | Real customers, no UGC motion or broken drop cadence |
| `/meg-micro-moments` | 7-moment trust audit + install order, routes to the engines | Zero-audience launch or flat engagement diagnosis |

## The mental model

1. **One spine, one dial.** `/extract` and `/extract-forge` share every quality gate and build standard; they differ only in ceremony. The forge is the max setting of the same machine, not a different machine — so elevating extract meant moving one decision (output size) from judgment to a derived number, not cloning forge prose.
2. **Floors are earned, not asserted.** The corpus is measured (words, post-enrichment), yields are counted (patterns, deliverables), and the manifest falls out deterministically. A thin source that resists enrichment ships small HONESTLY (`fidelity: low`) — the floor rises with evidence, never with hope.
3. **The enrichment inversion.** Old routing: short source → use the small pipeline. New routing: short source → go get more of the same expert first. The 15-minute video is a starting point for harvesting, not a ceiling on output.
4. **Trust the report, not the run.** Every extraction ends with manifest-vs-shipped + enrichment ledger + asset verdicts — the operator audits scale decisions after the fact without re-opening the session.

## Capability: derived manifests (`extraction_manifest.py`)

**What it is**: a Layer-3 CLI that measures corpus mass, converts extraction yields into workflow/prompt floors (calibrated: meg 23 patterns → 14 vs 13 shipped; paolo 17 → 10 vs 11 shipped; extension 7 → 4+6), and audits shipped skills against their manifest.
**When to reach for it**: every extraction (wired into extract.md P1.5/P4/P9); also standalone when converting old extractions (`convert-extraction.md` now points here).
**When NOT to**: don't run `check --enforce` against pre-v3 skills — the 369 existing skills were sized under old rules; observe-mode only.
**Honest edges**: sizing formula is calibrated on 2 skills + 1 extension; expect a coefficient tweak after 3-5 fresh runs. `corpus` counts only `transcript*/source*/corpus/*` file patterns — oddly-named source files are invisible to it.

## Capability: auto-enrichment (extract.md P1.5)

**What it is**: below RICH, the pipeline discovers ≤4 more same-expert sources (yt-dlp channel scan, WebSearch), dedups against `extractions/<slug>/`, fetches transcripts, re-measures, and logs an enrichment ledger. Two unquoted sources get set aside as blind-pass reference corpus — pre-solving the corpus gate that blocked Meg's blind pass twice.
**When NOT to**: explicit "light extract" skips it; never use budget-gated APIs for discovery (cost gate).
**Honest edges**: **never fired live** — source discovery (channel scan quality, dedup precision) is the least-proven part of v3.0. The first validation run should watch it closely.

## Capability: forge-scale extensions (Extension Mode)

**What it is**: existing-expert overlap now derives its own manifest (`--extension`: 2-5 workflows, ≥5 prompts for a 5+-pattern layer) and integrates with tier placement + version bump + provenance append. The 2026-07-21 Meg run (1 workflow for a 7-pattern layer) is the named anti-pattern.
**Worked example**: this session's PoC — trust layer → `/meg-trust-email-engine` + `/meg-community-voice` + `/meg-fan-flywheel` + upgraded `/meg-micro-moments`, 6 prompts (`micro-moments-install`, `trust-welcome-email`, `customer-life-email`, `cocreation-ask-email`, `brand-voice-replies`, `spotted-feature-pack`), SKILL.md v1.2.
**Honest edges**: Meg blind pass still lacks a reference corpus (her emails aren't publicly archived; on-screen ones are quoted as exemplars, disqualified) — Layer 5 ships B-tier-honest until real SHC emails are collected, e.g. by subscribing to the list.

## Composition (options, not pipeline steps)

| Stack | When it earns its cost |
|---|---|
| `/extract` → `/merch-os`-style orchestrator | Asset scan flags BUILD at ≥8 workflows — mint the Tier-0 front door |
| `/extract` → `/arsenal` | Confirm new commands surface in workflow-granularity recall before ending the session |
| Layer-5 engines → MyBPM Week-1 / Jen FTHB | The live deployment surface for the new Meg workflows |
| `/extract-forge` | Critical-domain expert where Farrice wants checkpoint control |

## Honest edges (session-level)

- P6 wrapper minting changed mid-stream: a sibling session (2026-07-25 Arsenal Loop) now owns shim minting via `mint_menu_wrappers.py` — trust the current extract.md on disk, not this session's original hand-minting text.
- Finalize logged a routing-override note (control-intent classifier wanted `/system-audit`; `/go` was commanded — intentional, on record).
- 2 pre-existing citation-integrity warnings remain (`python3 execution/citation_integrity.py`) — unrelated to this build but unresolved.
