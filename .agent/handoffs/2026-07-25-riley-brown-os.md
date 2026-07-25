---
thread: riley-brown-os
status: ready
resume_hint: Farrice blind pass + paste Typefully/Cal.com keys + IG live-test
unfinished: A-tier judgment; 2 scheduler keys; IG/TikTok paths untested
branch: main
pin: true
---

# Riley Brown OS — Watch + Forge + $0 Capability Layer (scrape-creator, ad-spy, Social Intelligence DB)

## Purpose
- **Next session should do:** (1) run Farrice's blind pass on the riley-brown skill to promote it to A-tier; (2) add `TYPEFULLY_API_KEY` + `CALCOM_API_KEY` to root `.env` (free tiers) and live-verify `/post-scheduler` + `/scheduling-links`; (3) live-test the Instagram/TikTok paths in `execution/social_intel.py` (only YouTube is proven).
- **Not in scope:** re-extracting Riley (forge complete, composite 8.33), rebuilding any capability workflow (all shipped + committed in `21a0e3e17`), new tool purchases (standing $0 decision).

## Load First
- `skills/riley-brown-marketing-automation/SKILL.md` — the skill front door (12 workflows, stacking guide)
- `extractions/riley-brown-marketing-automation/blind-pass-log.md` + `.tmp/blind-pass-riley/` — EVAL-055 generated pieces for the Farrice pass (references: `extractions/riley-brown-marketing-automation/reference-corpus/`)
- `.agent/workflows/scrape-creator.md`, `.agent/workflows/ad-spy.md` — the two proven pipelines
- `directives/notion-databases.md` — Social Intelligence DB schema (`NOTION_DB_SOCIAL_INTEL` in .env)
- `docs/solutions/2026-07-24-replicate-creator-tool-stack-at-zero-cost.md` — the banked replication rule

## Current State
- **Objective:** Riley Brown's 9-workflow agentic marketing stack extracted (forge) and replicated at $0 on owned infra.
- **What is already done:** `/riley-brown` front door registered; 16-pattern genius.md; 9 born-v2 prompts (renaissance 0-fail); AGENT.md; blind pass EVAL-055 PASS (model-judged); skill_auditor 6/6; Social Intelligence Notion DB created (integration-owned, `3a749875-a897-8104-a867-fc9aeb53f52c`); `/scrape-creator` PoC (2 real pages, $0.01); `/ad-spy` PoC (5 real AG1 ads, 176-day winners, $0); `/creative-from-winners`, `/brand-asset-scrape`, `/inbox-drafts` shipped; git divergence merged; all pushed (`21a0e3e17`).
- **What is uncertain or stale:** IG/TikTok scrape+normalize written but never live-run; scheduler shells inert without keys; A-tier pending Farrice judgment; Knowledge Vault has 2 duplicate "Riley Brown" pages from the earlier Codex session (surface to Farrice before deleting).
- **Latest proof/receipt:** finalize composite 8.33 logged to Notion + Performance Log; Apify wallet $2.93/$29.

## Suggested Skills / Workflows
- `/riley-brown` — expert front door (persona + arsenal)
- `/scrape-creator <handle> --platform instagram --limit 3` — the IG live-test in one command
- `/ad-spy <brand>` — sprint-offer competitor intel
- `/resume riley-brown-os` — this thread

## Exact Next Prompt
```text
Resume riley-brown-os. Three tasks: (1) show me the blind-pass pieces side by side with the real Riley transcripts, unlabeled, for my A-tier judgment; (2) I'm pasting TYPEFULLY_API_KEY and CALCOM_API_KEY — wire them into .env and live-verify /post-scheduler and /scheduling-links end to end; (3) live-test /scrape-creator on an Instagram creator with --limit 3 and show me the Notion pages.
```

## Acceptance Criteria
- Farrice records PASS/FAIL on the blind pass (updates EVAL-055 lineage; A-tier or named gap)
- Both scheduler workflows produce a real verified artifact (Typefully draft URL, live Cal.com link)
- IG path writes ≥1 correct Notion page or the failure is documented in the workflow's cost/limits notes

## Risk Notes
- Never commit `.env`; keys arrive via Farrice only.
- Apify spend on IG/TikTok tests: keep `--limit ≤3`, per-run ceiling $0.25 stands.
- Meta Ad Library requires real-browser Playwright (raw HTTP 403s) — don't "optimize" to requests.
- One stale session-lock entry may linger (release was classifier-blocked); it expires via heartbeat TTL — claim fresh, don't fight it.
