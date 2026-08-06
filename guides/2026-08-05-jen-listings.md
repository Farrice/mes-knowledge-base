---
date: 2026-08-05
session: jen-listings
tier: operator-guide
status: enriched
---

# Jen Listings — 5200 Armida Package + Listing Engine v2 — What We Built 2026-08-05 and How to Use It

> A live client run (5200 Armida Dr, $3.199M Woodland Hills) went through three hook generations and two taste rejections before Jen shipped her own version. That arc got codified the same day into `/listing-package`: a one-shot pipeline turning a listing URL into a complete, compliance-linted brief. Companion files: the engine at `skills/jen-santulan-listing-content/workflows/listing-package.md`, the register ladder in `_active/jen-listings/CLAUDE.md`, the recipe in `docs/solutions/2026-08-05-listing-package-pipeline.md`, the worked example in `_active/jen-listings/5200-armida-woodland-hills/`.

## ⚡ If you only read 10 lines

1. `/listing-package <zillow url | address | --paste>` — the whole engine, no flags, ever.
2. It delivers the **complete brief in one shot** (strategy card + 6 hooks + scripts + cover text + caption + forwardable send text). You judge after, not during.
3. Only two things halt a run: **no input at all**, or a **compliance/factual veto**. No mid-run taste questions — binding.
4. **Register is chosen by price before a word is written**: <$1.5M = warm FTHB voice · **≥$2M = "Quiet Flex Elite Advisor"** (authority-POV hooks, market thesis, property as evidence).
5. At ≥$2M the FTHB-Permission hook is **forbidden** — rent-vs-mortgage math is factually wrong for that buyer.
6. `python3 execution/listing_intel.py parse|diff|ledger --slug <slug>` — facts get a provenance ledger; the MLS-vs-description diff catches contradictions automatically.
7. `python3 execution/fair_housing_lint.py check --file <f> --context script|caption|package` — **exit 2 = no ship**. No safe/family/great-for-kids; schools off camera.
8. `python3 execution/voice_ratchet.py add --client jen --verdict pass|fail --line "..." --why "..."` — felt verdicts; the log **outranks prompt defaults**.
9. Fetch never fabricates: Playwright → Apify `web` actor (~$0.003) → ask for a paste.
10. Re-running the same property **resumes** from `_active/jen-listings/<slug>/listing.json` — iterations are $0.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/listing-package <url\|address\|--paste>` | Complete brief: strategy card, 6 hooks, scripts, cover text, caption, forwardable send text, pre-shoot checks | Any new listing. The default front door. |
| `/listing-content <address>` | 6 hooks only | Hook variants fast, package not needed |
| `python3 execution/listing_intel.py diff --slug <slug>` | Contradiction report (spa/basement/bath-count/price-jump/brand claims) | Verifying facts on copy someone else wrote |
| `python3 execution/fair_housing_lint.py check --file <f> --context script` | Findings table + exit 0/2 | Before any real-estate copy reaches a client. Also `rules`, `selftest`. |
| `python3 execution/voice_ratchet.py add --client jen ...` | One row in `references/jen-calibration-log.md` | Every time Farrice or Jen reacts to a line |
| `python3 execution/voice_ratchet.py status --client jen` | Counts + recompile flag at ≥5 pending | Deciding whether to compile a Jen register card |
| `python3 execution/ground_truth.py list jen-listing-content` | The 5 approved benchmark samples | Calibrating a run against what already won |

## The mental model

**1. Machines own facts; the model owns taste.** Every failure in the manual run was an ownership problem. A phantom "spa" and a phantom "finished basement" survived because facts lived in prose. Now `listing_intel.py` parses the listing into `listing.json`, diffs MLS fields against the marketing description, and emits `claims-ledger.json` where every claim carries a source (`mls_field` / `description` / `derived` / `external`) and a confidence (VERIFIED / LIKELY / UNCONFIRMED). Contradictions become don't-say items with pre-written fallback lines. Nobody has to remember to check.

**2. Register is a gate, not a vibe.** Jen has two voices and the deciding variable is price. The system picks the register from the tier *before* generation — that's what makes the next run land on the first pass instead of the third. The scraped voice profile (`references/jen-real-voice-profile.md`) describes where she's been; the calibration log describes where she's pointing. The log wins.

**3. Robustness in the sheet, simplicity in the send.** Two artifacts per listing. The shoot sheet holds research, ledger, diagnostics. The send text is one forwardable block with zero repo paths or tool names. The 5200 Armida verdict proved it: the robust sheet was better *thinking*, the forwardable text was the better *deliverable*.

## Capability 1 — `/listing-package`, the one-shot engine

**What it is.** Eight phases: intake (fetch + photo contact sheets + parse/diff/ledger) → market research with receipts → strategy/register selection → hook + script generation → package render → compliance gates → finalize → post-ship loop. Phases 3–5 run without stopping; the deliverable is complete when you first see it.

**When to reach for it.** A listing URL or address arrives and content is needed. The routing binding (`jen_listing_package` in `execution/routing_enforcer.py`) surfaces it as the `[CORE]` route on a bare Zillow/Redfin link — no command memory required.

**When NOT to.** Hooks only, with verified facts already in hand → `/listing-content` is cheaper. Non-real-estate client content → only the pattern transfers.

**How to invoke.**
```
/listing-package https://www.zillow.com/homedetails/...
/listing-package 5200 Armida Dr, Woodland Hills
/listing-package --paste
```
Tier auto-derives from list price; `--tier fthb|luxury` and `--client` exist only as overrides.

**Worked example.** 5200 Armida: 57 photos reviewed, ledger built 35 claims (31 VERIFIED / 3 LIKELY / 1 UNCONFIRMED), 2 risks + 2 confirm-items surfaced, register resolved to luxury.

**Honest edges.** **The full path has never run on a cold URL** — components are unit-tested, the end-to-end run is not. The Apify fallback rung is untested inside this workflow. Photo review depends on the in-page grid-render technique: documented, but browser-dependent.

## Capability 2 — `listing_intel.py`, facts with provenance

**What it is.** `parse` handles an HTML dump (JSON-LD + labeled-text regexes), a pre-built JSON, or `--paste` free text — unknown fields stay `null`, never guessed. `diff` is the value: spa contradiction, basement phantom-claim, bed/bath arithmetic, remodel-gap ambush (>50% price jump or ≥1.5× Zestimate gap), luxury-brand confirm items. `ledger` assigns source + confidence per claim.

**When to reach for it.** Any listing whose marketing copy you didn't write; every pipeline run.

**When NOT to.** MLS data already in hand with no marketing description to contradict — the diff has nothing to compare.

**How to invoke.**
```bash
python3 execution/listing_intel.py parse <dump> --slug <slug>
python3 execution/listing_intel.py diff --slug <slug>
python3 execution/listing_intel.py ledger --slug <slug>
python3 execution/listing_intel.py selftest     # 7/7
```

**Honest edges.** HTML parsing is tuned to Zillow's DOM; Redfin/realtor dumps parse thinner (conservative by design — a regex that might mismatch returns `null`). Derived market comparisons stay UNCONFIRMED until the research phase fills them.

## Capability 3 — `fair_housing_lint.py`, the compliance floor

**What it is.** Five hard-fail classes (familial-status steering, safety code words, protected-class targeting, exclusive+people-words, religion-landmark-tied-to-buyer) and four warns (schools in script context, persona labels leaking into caption/spoken sections, walking-distance-to-worship, unverifiable environment absolutes). Data-driven `RULES` table — adding a rule is a one-line append.

**When to reach for it.** Before *any* real-estate copy reaches a client. This is the one gate with legal weight.

**When NOT to.** Non-real-estate copy — the rules encode Fair Housing Act steering, not general tone.

**How to invoke.**
```bash
python3 execution/fair_housing_lint.py check --file <path> --context script|caption|package
python3 execution/fair_housing_lint.py check --text "..." --strict
python3 execution/fair_housing_lint.py rules
python3 execution/fair_housing_lint.py selftest   # 12/12
```

**Worked example.** Run live against the Armida shoot sheet, it flagged `"zero street noise"` as an unverifiable absolute — and correctly left `"quiet cul-de-sac"` alone.

**Honest edges.** A regex linter is a floor, not counsel. It catches known phrasings; a novel steering construction passes. Schools-in-script detection relies on a context sniff (`HOOK`/`SAY:` markers or explicit `--context script`).

## Capability 4 — the Jen calibration ratchet

**What it is.** `voice_ratchet.py` gained an optional `--client` flag. Default behavior (Farrice's Voice OS at `_active/farrice-brand/voice/calibration-log.md`) is unchanged; `--client jen` rewires log, card, and state paths to the skill's own files.

**When to reach for it.** Every felt verdict — Farrice's or Jen's, pass or fail. Today's four are seeded: two rejected hook species, two winners.

**When NOT to.** Speculation about what she might like. The ratchet records reactions to actual lines.

**How to invoke.**
```bash
python3 execution/voice_ratchet.py add --client jen --verdict pass --line "..." --why "..." --source "..."
python3 execution/voice_ratchet.py status --client jen
```

**Honest edges.** Dedupe is on exact line text, so a near-identical line logs twice. No `/voice-compile` equivalent is wired for Jen — at ≥5 pending verdicts, compiling her register card is a manual judgment pass.

## Composition (options, never pipeline steps)

| Stacks with | When it earns its cost |
|---|---|
| `skills/kallaway-hook-mastery/` | Already loaded by the generate phase. Reach for it directly when hooks underperform and you want the alignment audit. |
| Blind Bar pass (`directives/blind-bar-protocol.md`) | Wired into the gates phase by a sibling session — self-check against the golden ref, capped at one repair round, never a question to Farrice. |
| `knowledge/expert-benchmarks/jen-listing-content/` | 5 approved samples for blind comparison when a run feels off-register. |
| A second listing client | Intake/research/lint/ledger are client-agnostic. Cost is a voice pack + register file + send template — not a rebuild. |

## Known-open (carried forward)

- Pipeline unproven on a cold URL — the first live run is the acceptance test.
- Three fact fixes pending on Jen's shipped Armida caption: main-house baths read "3" (MLS: 4.5), the ADU rental-income claim needs Marty's confirmation, "zero street noise" is an unverified absolute.
- `handoff_store.py --from-temp` collided with a sibling session during this very closeout (recovered per `docs/solutions/2026-07-25-handoff-from-temp-cross-session-collision.md`); the slug-match guard is still unbuilt.
