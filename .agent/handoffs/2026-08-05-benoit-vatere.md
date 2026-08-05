---
thread: benoit-vatere
status: ready
resume_hint: /extract Extension Mode on benoit-vatere from the 2 corpus transcripts already on disk (~18k words)
unfinished: Corpus enrichment to close tool-name-density gap; Golden Core teardown as LinkedIn lead magnet; A-tier side-by-side still open
branch: main
pin: true
---

# Benoit Vatere Forge — Full-Funnel Media Systems Extraction (Liquid Death)

## Purpose
- **Next session should do:** Enrich the shipped `benoit-vatere` skill with the two corpus transcripts already on disk (~18k words) via `/extract` Extension Mode to close the one named embodiment gap (tool-name density), then draft the Golden Core teardown as a LinkedIn cash-launch lead magnet.
- **Not in scope:** Rebuilding the skill (it shipped and passed all gates), re-watching the source video, re-running the blind pass (PASS recorded as EVAL-059), any new expert extraction.

## Load First
- `skills/benoit-vatere/genius.md` — 12 patterns, signature moves, quality rubric, recognition test. Load before any Benoit work.
- `skills/benoit-vatere/SKILL.md` — 10 workflows in 3 tiers + 8 wired born-v2 prompts + stacking guide.
- `extractions/benoit-vatere/reference-corpus/` — **the enrichment fuel**: `2025-05-entertain-or-die-keynote.md` (5.6k words, solo keynote + audience Q&A) and `2026-shoptalk-cpg-guys-episode.md` (12.5k words). Both verbatim captions with provenance headers, already fetched.
- `extractions/benoit-vatere/extraction-report.md` — full MES 3.0 dossier (12 patterns, 8 hidden-knowledge items, 3 exemplars + anti-exemplar, 8-criterion rubric).
- `extractions/benoit-vatere/blind-pass-sample.md` — the two generated samples judged against unseen work; the "what gave it away" section names exactly what enrichment must fix.
- `skills/benoit-vatere/references/era-bound-2026.md` — platform mechanics quarantined from durable doctrine; re-verify before any external citation.

## Current State
- **Objective:** Ship a forge-grade extraction of Benoit Vatere (Chief Media & Digital Commerce Officer, Liquid Death) covering media buying, measurement, and incrementality — the roster's missing media-systems seat.
- **What is already done:**
  - Watched the 34-min Marketing Against the Grain interview (`9zBThLCpPh4`) — full captions + 100 scene-aware frames.
  - Identity VERIFIED (The Org / LinkedIn / Groceryshop 2025); ex-founder Mammoth Media + VTAGZ (CPG attribution SaaS), ex-CEO PlayHaven. Captions garble him as "Benwa/Benwis".
  - Built `skills/benoit-vatere/`: genius.md (12 patterns), SKILL.md, 10 workflows (4 foundation / 4 practitioner / 2 stacking), source-quotes.md (timestamped receipts), era-bound-2026.md.
  - Forged 8 born-v2 execution prompts — `renaissance_audit.py` 0 fail, `prompt_library.py build` + `wire_prompt_pointers.py --write` done, pointers live in SKILL.md.
  - Registered: `agents/benoit-vatere/AGENT.md`, 9 minted wrappers + front door `/benoit-vatere`, registries synced, menu parity clean.
  - Gates: `skill_auditor.py check` **7/7 PASS**; blind pass **PASS (EVAL-059)** judged against 2 unseen verbatim pieces; `chain_runner.py finalize` logged; `forge_gate.py record` stamped.
  - Committed + pushed to main: `dec2f5654` (forge), `c40754e9b` (Farrice felt verdict: **like**, no changes requested).
- **What is uncertain or stale:**
  - Skill is **B+ tier**, not A — A-tier needs a Farrice-judged side-by-side, still open.
  - The named residual gap: real Benoit name-drops infrastructure mid-answer (AMC, Stackline, Walmart Connect, Amazon DSP, BigQuery/Looker, Circana, LiveRamp, Trade Desk) far denser than a transcript-only base supports. The corpus transcripts contain all of these — that is the enrichment target.
  - `retail-media-plan` workflow carries `fidelity: low` by design (source gives doctrine, not tactics).
  - `.agent/session-state.md` was overwritten by a concurrent Kallaway-forge session — do not read it as this thread's state.
- **Latest proof/receipt:** `extractions/benoit-vatere/blind-pass-log.md` (EVAL-059 PASS + Farrice "like" line); `evolution_store/ground_truth/eval_set_v1.jsonl`.

## Suggested Skills / Workflows
- `/extract` (Extension Mode) — forge-scales a new layer into an existing skill; the correct route for corpus enrichment (never re-forge).
- `/benoit-vatere` — expert front door: loads AGENT.md persona + full arsenal.
- `/golden-core-diagnostic` — the teardown workflow that becomes the lead magnet.
- `/ghostwrite` or `/parallax` — for turning the teardown into Farrice-voice distribution (load `_active/farrice-brand/voice/VOICE-CARD.md` + dial first).
- `/arsenal <task>` before building anything new.

## Exact Next Prompt
```text
/extract Extension Mode on benoit-vatere — enrich the existing skill from the two
transcripts already at extractions/benoit-vatere/reference-corpus/ (Entertain-or-Die
keynote 2025-05 + CPG Guys Shoptalk 2026, ~18k words combined). Target the named
blind-pass gap: infrastructure/tool-name density (AMC, Stackline, Walmart Connect,
Amazon DSP, BigQuery+Looker, Circana, LiveRamp, Trade Desk) and his mid-answer
micro-stories. New material to fold in that the interview did NOT contain: the
path-to-purchase model, exposed-audience-as-first-party-data distribution, retailer
branded-search incrementality, glance views on/offline, the total-ROAS-with-the-CFO
move (never open channel-level), and light-buyers-over-loyalists creative doctrine.
Extend genius.md + add workflows only where a genuinely new deliverable exists; do
not rebuild what shipped. Then re-run skill_auditor.py check and record a fresh
blind-pass line.
```

## Acceptance Criteria
- `skills/benoit-vatere/genius.md` carries the new patterns (path to purchase, exposed audience, branded-search incrementality, glance views, CFO total-ROAS frame, light buyers) with corpus citations — no invented material.
- Tool/infrastructure names appear where the doctrine actually calls for them, sourced to the corpus, not asserted from memory.
- `python3 execution/skill_auditor.py check --skill benoit-vatere` still returns 7/7.
- `renaissance_audit.py` stays 0 fail if any prompt changes; `wire_prompt_pointers.py --write` re-run if prompts were added.
- A new `blind-pass-log.md` line records the post-enrichment verdict.
- Work committed to main (all-work-on-main is binding).

## Risk Notes
- **Concurrent sessions:** a sibling session shipped a Kallaway hook-mastery forge against this same tree during this session and overwrote `.agent/session-state.md`. Before starting, confirm no other tool is live on this directory (`session_lock.py`); if files change unexpectedly, apply `docs/solutions/2026-07-15-concurrent-session-race-accept-repair-dedupe.md` (accept → repair → dedupe, never revert).
- **Era-bound drift:** platform mechanics in the corpus (Meta frequency behavior, ASC/Advantage+ automation, TikTok Shop state, retail media network capabilities) are 2025–2026 snapshots. Anything cited externally must be re-verified; keep them in `references/era-bound-2026.md`, never in genius.md as durable truth.
- **Fidelity:** the corpus is spoken conference material with caption artifacts (names garbled, "rorowass" = ROAS, "Rondell" = likely a retail media network). Quote carefully; do not clean his imperfect English into essay prose — polish is the tell.
- **No re-forge:** re-running `/extract-forge` would duplicate the skill. Extension Mode only.
- **Open outer-loop debt (unrelated but live):** 31 revenue-tracker outcome check-ins due; 10 open missions; `/weekly-closeout` overdue.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-08-04-benoit-vatere.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
