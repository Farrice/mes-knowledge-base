---
thread: insight-brief
status: active
resume_hint: Verify 05:30 listening runs landed since 08-01 (listening-run.log), then week-2 POV batch from the vault
unfinished: Run verification + 3 diverged-branch recovery + mission #6 POV batch + DM-send status log
branch: main
pin: true
---

# Angle Map Listening Engine — v4.1 Content Factory Build (fusion + vault + two-ring dossier)

## Purpose
- **Next session should do:** (1) Verify the 05:30 local listening runs have landed daily briefs + COS exec cuts since 08-01 (`_active/health-performance-ip-library/06-system/listening-run.log`, `daily/`) and mark published vault assets POSTED in `_active/farrice-brand/content/vault/INDEX.md`. (2) Recover the three diverged branches main lacks: `codex/end-session-control-plane` (+30 files/2333 lines — live Codex thread, coordinate before merging), `codex/global-adaptive-judgment-floor` (its verifier `execution/verify_global_adaptive_judgment_floor.py` sits untracked in the tree), `origin/claude/youtube-notion-integration-analysis-ubiusy` (`execution/social_to_notion.py`, 681 lines, never landed). (3) Campaign mission #6: week-2 POV post batch — draw from the stocked vault (3 READY assets) + `2026-08-04-week-2-pov-batch.md`. (4) Log DM-send status vs the 07-31 commitment (5 one-gap DMs; the 14-day clock starts at first five logged sends).
- **Not in scope:** rebuilding any part of the engine (v4.1 is the standard); touching the paused cloud routine (trig_01LPK9dSCmABXfq1g3pRWGsq, re-enable only at claude.ai/code/routines); editing canon bodies of docs 03/07/08 (engine feeds deltas; curation is explicit).

## Load First
- `_active/health-performance-ip-library/AUTOMATION_PROMPT.md` — v4.1 engine spec (Angle Map center, Daily Core, rotating deep-focus calendar, story bench, factory + vault contracts)
- `_active/health-performance-ip-library/daily/2026-07-31-angle-map-listening-brief.md` — the standard-setting inaugural brief (verdict: good; §12 = factory re-run shape)
- `_active/linkedin-launch/04-deliverables/context-os/08-TWO-RING-RESONANCE-DOSSIER.md` — two-ring ICP/audience identity build (extends 07; ring definitions for all content tagging)
- `_active/farrice-brand/content/vault/INDEX.md` — vault state (3 READY: drawer post, proof-decay essay, drawer video script)
- `_active/linkedin-launch/CAMPAIGN.md` — campaign queue (mission #6 next)

## Current State
- **Objective:** one $750 Angle Map sold within 14 selling days of first five logged sends; the engine exists to power content → inbound → cash.
- **What is already done:** v4.0 fusion (geo-brief + insight-brief → one engine, Angle Map canon center) · v4.1 Content Factory (story bench: Kallaway/Cole/Lara/Hoyos+Puri; rotating finished-format calendar; four-tag assets; two-ring dial) · content vault scaffolded + 3 READY assets · promises-not-kept ledger live · living-doc delta anchors in 03/07 · COS 🎧 section wired (cos_prep.py) · launchd 05:30 job loaded (`com.antigravity.angle-map-listening`) · cloud routine paused after final harvest · Apify pipe proven ($0.005 smoke + 4 live scrapes) · 08 dossier canonical · inaugural brief Drive-exported · cloud W31 brief/synthesis recovered as `-cloud-run` variants (2026-08-04).
- **What is uncertain or stale:** whether the 05:30 runs actually fired 08-01→08-04 (unverified — check the log first); DM-send status vs 07-31 commitment (board callback pending since 08-01); founder-side language in dossier 08 is composite until 3 qualified DMs (update trigger set); the "who sent you this?" DM-intake line adoption.
- **Latest proof/receipt:** commits `4952ab8a6` (v4 build) · `9765e5d5f` (inaugural run) · `f1c7e0843` (v4.1 standard) · `08fa61c75` (dossier); mission `angle-map-listening-engine` closed done, verdict good, in `.agent/missions.jsonl`.

## Suggested Skills / Workflows
- `/resume insight-brief` — reopens this thread with the pinned handoff
- `/content-queue` — idea-selection layer over the vault (composes freely, never forced)
- `/cos` — daily sitting; board callback checks the DM sends; weekly is 2d overdue
- `/voice-compile` — 14 felt verdicts pending; run before the next pen session (week-2 POV batch is a pen session)

## Exact Next Prompt
```text
Resume the insight-brief thread. First verify the Angle Map Listening Engine's scheduled runs: read _active/health-performance-ip-library/06-system/listening-run.log and list which daily briefs landed since 2026-08-01; fix silently-failed runs before anything else. Then run /voice-compile, then draft campaign mission #6 (week-2 POV batch, 3 posts) pulling hooks and tags from _active/farrice-brand/content/vault/ and the 08-TWO-RING-RESONANCE-DOSSIER ring definitions. Before drafting, ask Farrice for DM-send status against the 07-31 five-send commitment and log it.
```

## Acceptance Criteria
- listening-run.log inspected; every missed day since 08-01 explained or repaired; tomorrow's run verified live
- vault INDEX reflects true asset states (READY/POSTED)
- three diverged branches either merged (with sibling-session coordination) or explicitly parked with reasons
- week-2 POV batch drafted at voice-card standard, ring/pillar tagged, filed to vault
- DM-send status logged (revenue_tracker or pipeline.md), board callback answerable

## Risk Notes
- One tool per tree: `codex/*` branches belong to live Codex threads — never merge while a sibling session is mid-write; coordinate or park.
- The launchd job runs headless with acceptEdits; if the Mac slept through 05:30 the run fires on wake — a missing brief is diagnosable from the log, never assume the engine is broken.
- Apify/Perplexity standing approval (2026-07-31) is budget-bounded: $29/mo + $30/mo; trackers `.agent/apify-usage.json`, `.agent/perplexity-usage.json`.
- Dossier 08's founder verbatim is composite and labeled — never quote it as a real customer voice in public copy.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-07-31-insight-brief.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
