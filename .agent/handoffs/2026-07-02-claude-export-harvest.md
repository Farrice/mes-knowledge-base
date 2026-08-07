---
thread: claude-export-harvest
status: ready
resume_hint: Battle-test: run a real client program through /strength-conditioning + a real offer through /coaching-business; felt verdict decides
unfinished: Battle-test both conductors; review 3 pending memory rules; optional: deep veins (Priestley 84 convs) + 4 noted-skill polish
branch: main
pin: true
---

# Handoff — claude.ai Export Harvest: COMPLETE → Battle-Test Phase

**Date:** 2026-07-02 · **Thread:** claude-export-harvest · **Status:** build DONE, battle-test NOT started

## Next session's focus (per Farrice)

**Battle-test the harvested expert system with real work — felt verdict decides:**
1. Run a **real client program** through `/strength-conditioning` (conductor routes Galpin/Israetel/Teo/Aragon)
2. Run a **real offer** through `/coaching-business` (conductor routes Welch/Hiette/Novotny/Elkaim + Kotler/Eyal/Manson)
3. Weekly memory review: `python3 execution/memory_review.py list` → 3 pending rules (2 new @8.5 from the export distill, 1 old from May)

Per Farrice's standing rule: **gates measure floor, not ceiling — his felt verdict on real output is the true test.** If a lane feels flat, do a surgical `/extract-amplify` pass; never rebuild (see multi-engine-rebuild 3/10 lesson).

## What this session completed (all committed, all verified)

The **entire claude.ai account export** (3,711 conversations, 142 Projects, 1.37GB) was imported, deduplicated, deployed, and verified:

- **Import pipeline** (reusable): `execution/claude_export_{parser,ingest,triage,consolidate,state}.py` · runbook `docs/claude-export-import.md` · operator guide `docs/OPERATING-THE-HARVEST.md`
- **Memory:** 3,624 conversations in sovereign.db (workspace=claude-export), **100% embedded** (paid-tier Gemini key from the "Gemini Antigravity" project, swapped into .env), built-in-memory profile pinned, launchd `com.antigravity.harvest-memory-daily` installed (daily no-op backstop)
- **~65 new skills** across 5 waves (systems IP: `/extract-mastery` MES 3.0, `/knowledge-architecture`, `/context-profile` · fitness S&C package · 28 expert lanes · Gap 1 coaching-business vertical · Gap 3 one-off lanes) + **34 skill enrichments** (Gap 2: 251 patterns + 43 workflows into Nate B. Jones ×7 skills, Dan Koe, Saraev, Wiebe, Lara, Priestley, Godin, Fladlien 27→30wf, Kallaway, Cole, Iha, Alex Cooper name-fix, etc.)
- **Routing wired:** DOMAIN_REGISTRY Domain 16 (Fitness) + 6 swim-lane adds · PRODUCTION_CORE 24/45 (+strength-conditioning-os, +extract-mastery) · 165 invocation cards · all 65 slash shims verified present
- **Verification (evidence-based):** 743 structural checks · adversarial content review 59 SOLID / 5 usable-with-notes / 0 hollow · data-completeness audit vs DB counts · no-forced-wiring greps clean
- **Commits:** `338bea73` (harvest), `fd562ea7` (routing+guide), `4df661ed` (memory automation), `f02f1aec` (three-gap expansion), `31a3268a` (Elkaim fix)

## Key context for the next agent

- **New standing rule (memory: `no-forced-wiring-hubs-compose-freely`):** hubs are independent peers; cross-hub handoffs are OPTIONS, never pipeline steps; no expert-stuffing.
- **Known caveats (verification notes):** `steven-young-consciousness` (epistemic framing), `sarah-levinger`/`tess-barclay` (leaner attribution), `jiang-xueqin` ("Three Locks" possibly reconstructed), `daniel-thrasher` (name collides with YouTube musician — content verified as ClickBank manager). Prune if unused; all runnable.
- **Deep veins deliberately unmined:** Priestley 84 more convs, Godin 68, Fladlien 68, Kallaway 39 — census has every ID: `_active/harness/claude-export/harvest/census-full.json`.
- **Raw export backup:** the zips in `~/Downloads/` are irreplaceable (single-use URLs). `.tmp/claude-export/` + `_active/harness/claude-export/` are git-ignored (private).
- **Pre-existing staged renames** in `_active/linkedin-launch/` (252 files) were NOT ours and remain staged-uncommitted — someone should commit or unstage deliberately.

## Suggested skills for next session

- `/strength-conditioning` — the S&C conductor (battle-test #1)
- `/coaching-business` — the coaching-business conductor (battle-test #2)
- `/extract-amplify` — surgical enrichment if a lane feels flat (never rebuild)
- `/resume` — thread triage if picking up elsewhere
- `prose_classifier.py check` — before any client-facing deliverable ships
