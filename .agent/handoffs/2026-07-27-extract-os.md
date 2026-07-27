---
thread: extract-os
status: ready
resume_hint: Run /extract v3.0 on a fresh short expert video to validate auto-enrichment + derived manifest live
unfinished: P1.5 enrichment never fired live; Meg blind-pass corpus still missing; deploy Layer-5 engines on MyBPM/Jen
branch: HEAD
pin: true
---

# Extract OS — v3.0 One Spine, One Dial (adaptive forge + Meg trust layer)

## Purpose
- **Next session should do:** (1) Validate the elevated `/extract` v3.0 full-skill path end-to-end on a FRESH expert source — watch P1.5 auto-enrichment fire on a thin video, confirm the derived manifest (extraction_manifest.py) sizes honestly, and check the P8 asset-scan verdicts land in the report. (2) Deploy the new Meg Layer-5 engines on live work: `/meg-trust-email-engine` + `/meg-fan-flywheel` for MyBPM Week-1 launch, or `/meg-trust-email-engine` for Jen's FTHB list.
- **Not in scope:** rebuilding /extract-forge (stays the explicit 3-checkpoint ceremony); plugin builds (hard-gated behind operator-lift token — recommend-only).

## Load First
- `.agent/workflows/extract.md` — the v3.0 pipeline (P0-P10). NOTE: a sibling session updated P6 on 2026-07-25 — wrapper/shim minting is now owned by the Arsenal Loop (`mint_menu_wrappers.py`), do NOT hand-write wrappers.
- `execution/extraction_manifest.py` — corpus / derive / check CLI (RICH ≥8k words → 8-15 wf; MID 4-7; THIN honest + fidelity:low; --extension 2-5 wf + ≥5 prompts)
- `skills/meg-heckman-buyer-trigger-os/SKILL.md` — v1.2, 16 workflows; Layer-5 engines at Tier 2
- `/Users/farricecain/.claude/projects/-Users-farricecain-Google-Antigravity/memory/project_extract-v3-adaptive-forge.md` — the 4 locked decisions (floor fusion, auto-enrich, forge-scale extensions, asset scan)

## Current State
- **Objective:** /extract at forge parity — achieved and PoC-proven; now needs a fresh-expert validation run.
- **What is already done:** extraction_manifest.py shipped + calibrated (meg 23p→14wf vs 13 shipped; paolo 17p→10 vs 11); extract.md v3.0 rewritten; routing updated in extract-forge.md / mes-3.0-extract.md / convert-extraction.md / CLAUDE.md; Meg trust layer forge-scaled 1wf+1prompt → 4wf (/meg-micro-moments, /meg-trust-email-engine, /meg-community-voice, /meg-fan-flywheel) + 6 born-v2 prompts; all gates clear (renaissance 0-fail, skill_auditor 6/6, manifest check clear); committed 958853c29 + pushed.
- **What is uncertain or stale:** auto-enrichment (P1.5) has never fired live — source discovery via yt-dlp channel scan + WebSearch is untested; blind pass for the Meg skill still lacks a reference corpus (on-screen emails are quoted as exemplars, disqualified); citation_integrity reports 2 stale pointers (pre-existing).
- **Latest proof/receipt:** manifest check clear (17 wf / 18 prompts vs floors 4/6); finalize logged 8.33 composite with routing-override note (control-intent classifier suggested /system-audit; /go was commanded).

## Suggested Skills / Workflows
- `/extract <fresh expert video URL>` — the validation run; expect enrichment ledger + manifest table in the report
- `/meg-trust-email-engine` / `/meg-fan-flywheel` — Layer-5 deployment on MyBPM or Jen
- `/arsenal extract` — confirm the new commands surface in workflow-granularity recall

## Exact Next Prompt
```text
Run /extract on this video: <URL of a new expert, ideally a short 10-15 min single video> — validate the v3.0 pipeline end-to-end: show me the corpus verdict, the enrichment ledger (which extra sources it found and fetched), the derived manifest table BEFORE building, and the asset-scan verdicts in the final report.
```

## Acceptance Criteria
- Enrichment fires on a thin source and the ledger shows ≥2 added sources (or a clean exhaustion note)
- Manifest is presented before build; shipped counts match or exceed it; extraction_manifest.py check clear
- Report contains manifest-vs-shipped + enrichment ledger + per-workflow one-liners + asset verdicts

## Risk Notes
- 7 concurrent sessions were active at closeout — claim `session_lock.py` before any multi-file build
- Wrapper minting moved to Arsenal Loop mid-stream (2026-07-25 sibling change) — trust the P6 text on disk, not memory of this session's version
- Meg revenue figures remain UNCONFIRMED; stat citations LIKELY — labels required in any client-facing use
