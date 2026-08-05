---
thread: hilary-gridley-forge
status: ready
resume_hint: Fire /hg-verdict-to-evaluator on LinkedIn posts — mint the first evaluator from Farrice's own verdict history
unfinished: Farrice-judged blind pass for A-tier promotion; Taste Profile offer unvalidated (no prospect send, price anchor is Farrice's call)
branch: main
pin: true
---

# Hilary Gridley Extraction — Anti-Slop Judgment Encoding OS (13 workflows + Taste Profile)

## Purpose
- **Next session should do:** Fire `/hg-verdict-to-evaluator` on LinkedIn posts — mine Farrice's own verdict/voice-ratchet logs into the first minted evaluator, proving the crown-jewel pipeline against real harness data. Then (separately) a Farrice-judged blind pass to promote `hilary-gridley` from B-tier-clear to A-tier.
- **Not in scope:** Rebuilding or re-extracting the skill (complete, committed, menu-parity verified). Launching the Taste Profile offer publicly — `/offer-redteam` must run first and send-before-build binds.

## Load First
- `skills/hilary-gridley/SKILL.md` + `genius.md` — the 13-workflow manifest and the 14 genius patterns; genius.md loads before any workflow
- `skills/hilary-gridley/workflows/hg-verdict-to-evaluator.md` — the exact next action's workflow (harness bridge: verdict logs → evaluator)
- `skills/hilary-gridley/references/prompts-v2/judgment-encode.md` — the Output Contract that workflow honors
- `skills/hilary-gridley/references/taste-profile-spec.md` — canonical three-layer spec for the moat asset (the productized-offer payload)
- `extractions/hilary-gridley/extraction.md` + `visual-context.md` — full MES 3.0 extraction and the verbatim slide capture
- `docs/solutions/2026-07-28-front-door-masks-first-workflow-from-minter.md` — the minter bug this session found; read before the next forge

## Current State
- **Objective:** Harvest the anti-slop masterclass (Hilary Gridley, Marketing Against the Grain) into a deployable skill and build the Taste Profile concept into a real asset + productized offer.
- **What is already done:**
  - `skills/hilary-gridley/` — 13 workflows in 3 tiers + Taste Profile cluster; `genius.md` (14 patterns, recognition test, source-anchored anti-patterns); 4 references incl. `taste-profile-spec.md`, `loop-frameworks.md` (Bodnar/Flanagan material kept attributed, never blended), `source-quotes.md`
  - 10 born-v2 execution prompts, `renaissance_audit.py` 0-fail, library built, pointers wired
  - `agents/hilary-gridley/AGENT.md`; all 13 `/hg-*` commands menu-reachable; front door `/hilary-gridley`
  - Visual layer: `/watch` focused passes captured the two-panel teaching slide verbatim (time badges ~half a day → ~15 min, "flagged this three days ago… You already knew," named 90-day data window, unrequested second-order insight)
  - Expert name corrected **Gidley → Gridley** against her own Substack byline (auto-captions garbled it); all paths/files renamed before the error calcified
  - Verification: `skill_auditor.py check` 7/7 PASS · blind pass **model-judged PASS** (EVAL-057) vs 2 verbatim published pieces in `extractions/hilary-gridley/reference-corpus/`
  - Finalized (`--type Extraction`, anchors named), `forge_gate.py record` done, committed to main
- **What is uncertain or stale:**
  - A-tier promotion requires a **Farrice-judged** side-by-side (embodiment-standard); current verdict is model-judged only
  - Taste Profile offer is a shelf asset, unvalidated — no prospect send yet; price anchor deliberately left as Farrice's call
  - "Inside the Box / David Epstein" citation from the host is flagged UNCONFIRMED in `loop-frameworks.md` — use the principle, never the attribution
- **Latest proof/receipt:** `evolution_store/ground_truth/eval_set_v1.jsonl` EVAL-057 · `extractions/hilary-gridley/blind-pass-log.md` · `extractions/hilary-gridley/blind-pass-sample.md` (the judged Tier-1 output)

## Suggested Skills / Workflows
- `/hg-verdict-to-evaluator` — the exact next action; mines this harness's own Column A/B data
- `/hg-taste-profile` — build Farrice/Parallax's own profile (Layers 1-2 largely exist on disk; the run is mostly Layer 3 + canonization)
- `/hg-taste-profile-offer` then `/offer-redteam` — package and stress-test before any send
- `/hg-slop-diagnostic` — the free-teardown lead magnet shape for prospects

## Exact Next Prompt
```text
/hg-verdict-to-evaluator LinkedIn posts

Mine my accumulated felt verdicts, voice-ratchet history, and taste-calibration
logs for LinkedIn posts specifically. Follow the workflow: assemble real Column
A/B pairs (rejected-vs-accepted, corrected-vs-original, draft-vs-published),
grade provenance honestly, then run the encoding pipeline. Dedupe mined criteria
against the ban-bank, VOICE-CARD, and reader-contract dials — cite canon rather
than restating it. Lead the report with the "new since last codification"
patterns; those are the payload. Ship the evaluator harness-native (nudges,
never blocks) and set the re-mine cadence.
```

## Acceptance Criteria
- A structured Column A/B corpus exists for LinkedIn posts with an honest provenance grade
- The pattern report separates already-canonical rules from genuinely new patterns, and the new ones lead
- A native evaluator ships and is menu-reachable, nudging rather than blocking (Compass Doctrine)
- Re-mine cadence stated in the evaluator header

## Risk Notes
- **Provenance over volume**: if fewer than 5 clean pairs survive filtering, the workflow's honest output is a collection brief — do not pad with invented pairs (the anti-pattern this whole skill exists to kill)
- **Canon collision**: restating ban-bank/VOICE-CARD rules as "discoveries" is the fail mode; cite one source of truth
- **Minter bug (recurring)**: after any new skill forge, verify `ls .agent/workflows/<prefix>-*.md | wc -l` equals the workflow count — the front door masks the first workflow and the minter reports clean anyway
- **Concurrent-session rule**: forge-class multi-file work claims `session_lock.py` first (this session did; released at close)

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
