---
thread: kallaway-growth-blueprint
status: ready
resume_hint: Google Form (15 min) + Stripe link (10 min) turn the intake funnel + campaign Day-1 live; then first DMs carry a landing face
unfinished: His 3 deploy tasks + optional re-look at the 2 rebuilt interactives
branch: worktree-kallaway-sandcastles-forge
pin: true
---

# Extraction: Kallaway Growth System → Growth Blueprint OS - Built, Judged 5/7, Shipped

**Thread:** kallaway-growth-blueprint · **Status:** ready · **Date:** 2026-08-28
**Lane:** `.claude/worktrees/kallaway-sandcastles-forge` (auto-merges to main at session close — all paths below are repo-relative and valid post-merge)

## What this session did (two days, complete)
Extracted Kallaway's "0→100K with Claude" system (his 6 free skill files verbatim + both videos + Sandcastles MCP docs), ran his skills as a verbatim baseline on frozen inputs, built the surpass system (**Growth Blueprint OS**: $0 YouTube outlier engine, 9 workflows, client-grade render pipeline, lead magnet, intake funnel, enrichment function), had it judged by Farrice side-by-side — **5/7 OURS CLEARLY WINS** (EVAL-064) — rebuilt the 2 losers to his notes, and shipped the 31-file client package. Two full quality resets happened mid-mission (reader-purity rule; production-grade register reset) — both are now permanent contracts in the skill.

## Next session focus (in order)
1. **Farrice's Google Form** (15 min, phone-doable): create from `growth-lab/intake/google-form-kit.md` → paste form_url/prefill_entry/sheet_id into `growth-lab/intake/faces-config.json` → re-bake: `.venv/bin/python3 execution/build_intake_faces.py` (post-merge: python3 from repo root). Full detail: `growth-lab/intake/operator/FARRICE-WHEN-BACK.md`.
2. **Stripe link** (10 min — same link unblocks the LinkedIn campaign Day-1 gate AND the intake `payment_url`; see `_active/linkedin/05-lead-gen/2026-08-07-PAYMENT-SETUP-ACTION.md`).
3. **Optional re-look**: the two rebuilt interactives — `growth-lab/farrice-parallax/exports/positioning-wheel.html` + `bullseye-321-mix.html` (every clickable now ends insight+action+positioning; 42 clickables verified).
4. **First campaign DMs** can carry a landing face link (`growth-lab/intake/faces/face-*.html`) once the form is wired.
5. Optional: arm daily radar refresh — staged UNARMED at `.scratch/kallaway-sandcastles-forge/outlier-radar-refresh.UNARMED.md` (needs Farrice's explicit yes).

## Core Paths
- `growth-lab/DEPLOY-CARD.md`
- `growth-lab/LEVERAGE-MAP.md`
- `skills/growth-blueprint-os/SKILL.md`
- `skills/growth-blueprint-os/genius.md`
- `growth-lab/farrice-parallax/growth-blueprint.md`
- `growth-lab/intake/operator/FARRICE-WHEN-BACK.md`
- `extractions/kallaway/E2E-REPORT-2026-08-27.md`
- `_active/linkedin/CAMPAIGN.md`

(Why each: deploy card = commands · leverage map = money uses · SKILL/genius = contracts incl. the BINDING Register Contract + Q10 insight floor + reader-purity · flagship blueprint = his live 90-day plan · when-back = his 3 tasks · E2E report = verification receipts · campaign = funnel wiring, log 2026-08-28. Wave 2 spec when needed: `extractions/kallaway-growth-system/extraction-report.md` §6.6-6.7.)

## Do NOT Rebuild
Everything in `growth-lab/`, `skills/growth-blueprint-os/`, `execution/{outlier_radar,pack_enrich,intake_bridge,build_lead_magnet,build_intake_faces,export_growth_package}.py`, `templates/{lead-magnet,intake,research-brief}/`. Wave 2 (his 4 undistributed production-loop skills) is PARKED with the only public spec banked — extend Wave 1, never rebuild it.

## Standing decisions (do not relitigate)
NO Sandcastles subscription (their data can't see his buyer's platforms; trial parked "later if ever") · NO Adobe Acrobat Studio (PDF Spaces failed as lead magnet — no capture/white-label; verdict on disk) · Ahrefs API unfunded ("Insufficient plan" on all endpoints) · Apify retired · TikTok/IG = owned-metrics-first (decision card: `growth-lab/DECISION-CARD-tiktok-ig-data.md`) · enrichment manual-fire only · client artifacts carry ZERO operator language (binding memory rule).

## Suggested skills (next agent)
- Skill tool → `growth-blueprint` (front door; loads SKILL.md + genius.md) for any strategy/artifact run
- `/gb-orchestrate` to route mid-engagement; `/gb-intake` when the first form submission lands
- `update-config` only if the radar launchd job gets armed
