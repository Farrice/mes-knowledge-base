# Latest Handoff

**Thread:** jen-listings  
**Full path:** .agent/handoffs/2026-08-05-jen-listings.md  
**Date:** 2026-08-05 (today)  
**Status:** ready  
**Title:** Jen Listings — 5200 Armida Package + Listing Engine v2 (/listing-package pipeline)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume jen-listings` for this one.

---

---
thread: jen-listings
status: ready
resume_hint: Fire /listing-package cold on Jen's next listing URL — first live acceptance test
unfinished: Pipeline never run end-to-end on a cold URL; 3 fact fixes pending on Jen's shipped 5200 Armida caption (main baths 4.5 not 3, ADU rental-income claim, 'zero street noise')
branch: main
pin: true
---

# Jen Listings — 5200 Armida Package + Listing Engine v2 (/listing-package pipeline)

## Purpose
- **Next session should do:** fire `/listing-package <url>` cold on Jen's next real listing as the live acceptance test — judge the finished brief, log felt verdicts to the Jen ratchet, and (once ≥5 verdicts accumulate) compile a Jen register card.
- **Not in scope:** rebuilding any part of the pipeline (it is shipped, wired, and audited); re-deriving Jen's register ladder (settled by her own verdict); re-running ground-truth seeding (5 approved samples are in).

## Load First
- `skills/jen-santulan-listing-content/workflows/listing-package.md` — the engine; phases, fetch ladder, gates, output schema
- `_active/jen-listings/CLAUDE.md` — **register ladder** (FTHB <$1.5M warm / luxury ≥$2M "Quiet Flex Elite Advisor"); Override List is binding
- `skills/jen-santulan-listing-content/references/jen-calibration-log.md` — 4 seeded felt verdicts; outranks prompt defaults
- `skills/jen-santulan-listing-content/references/prompts-v2/listing-hook-set.md` — Register-Ladder v2.1, tier slot map (FTHB-Permission mandatory <$1.5M, FORBIDDEN ≥$2M)
- `skills/jen-santulan-listing-content/references/prompts-v2/listing-send-package.md` — the forwardable-text contract
- `docs/solutions/2026-08-05-listing-package-pipeline.md` — the recipe + why each layer exists
- `_active/jen-listings/5200-armida-woodland-hills/` — worked example (shoot sheet v3 + 2 photo contact sheets)

## Current State
- **Objective:** turn a manual, three-rejection listing-content arc into a one-shot pipeline: address/URL/description in → complete brief out (strategy card + 6 hooks + scripts + cover text + caption + forwardable send text), judged after delivery.
- **What is already done:**
  - `execution/listing_intel.py` — parse/diff/ledger; MLS-vs-description contradictions as code (7/7 selftest; fixture at `execution/tests/fixtures/5200-armida.json`)
  - `execution/fair_housing_lint.py` — steering-language + schools-in-script floor, exit 2 = no ship (12/12 selftest)
  - `execution/voice_ratchet.py --client jen` — per-client felt-verdict ratchet (Farrice's default path unchanged), seeded with this session's 4 verdicts
  - Skill v3.0: new `listing-package` workflow, 2 prompts (hook-set v2.1 + send-package), tier gates added to `01-listing-content.md` and `PROMPT.md`
  - `/listing-package` minted in both harnesses; `jen_listing_package` routing binding applied (a bare Zillow/Redfin link auto-suggests it); bindings appendix regenerated
  - Ground truth: `knowledge/expert-benchmarks/jen-listing-content/` domain + **5 Farrice-approved PASS samples** (first fully-grounded vertical in the system)
  - 5200 Armida package delivered; Jen shipped her own "Quiet Flex" version — its register is now the canon for luxury
  - Two commits on `origin/main` (`885b7a8cc` + the one-shot refactor); session lock released
- **What is uncertain or stale:** the pipeline has **never run end-to-end on a cold URL** — every component is unit-tested but the full path is unproven live. Fetch-ladder rung 2 (Apify `web` actor) is untested in this workflow. `.agent/intent-memory/current.json` and `.agent/session-state.md` belong to other sessions — ignore both.
- **Latest proof/receipt:** `listing_intel.py selftest` 7/7 · `fair_housing_lint.py selftest` 12/12 · `renaissance_audit.py` 3805/3805 pass · `verify_codex_claude_parity.py` clean · `routing_enforcer.py check` exit 0 on a real Zillow-link prompt · `/listing-package` visible in the live skill menu.

## Open items on the shipped 5200 Armida copy (Jen's version — time-sensitive if it hasn't posted)
- Caption breakdown reads "Main House: 4 Beds | 3 Baths" — MLS says **4.5** main (5.5 total with ADU)
- "generate premium rental income" — ADU legal rentability unconfirmed with Marty
- "zero street noise" — unverifiable absolute; `fair_housing_lint` flags it (soften to "end of the cul-de-sac, no through-traffic")
- Encino comp in any surviving hook is Zillow-algorithmic, not a CMA

## Suggested Skills / Workflows
- `/listing-package <url>` — the front door; no flags needed, tier auto-detected
- `/voice-compile` pattern via `python3 execution/voice_ratchet.py status --client jen` — compile a Jen register card at ≥5 pending verdicts
- `python3 execution/ground_truth.py list jen-listing-content` — the 5 benchmarks new runs are scored against
- `/listing-content` — quick hooks-only pass when a full package isn't needed

## Exact Next Prompt
```text
/listing-package <Jen's next listing URL>
```
(Then judge the delivered brief and give the feedback triad — like/don't like/top changes. Verdicts get logged to the Jen ratchet automatically.)

## Acceptance Criteria
- One invocation produces the complete brief with no mid-run questions (only halt allowed: missing input, or a compliance/factual veto)
- Register matches the price tier on the **first** pass (luxury ≥$2M → authority-POV hooks, no FTHB rent math)
- Every spoken claim traces to the claims ledger as VERIFIED or ships its fallback line; the don't-say list is present
- Send text passes `fair_housing_lint` + `client_package_lint` and is forwardable to Jen without edits

## Risk Notes
- **Untested live path** — first cold run may expose fetch/parse gaps on a non-Zillow source; the ladder is designed to ask for a paste rather than fabricate, so failures should be loud, not silent.
- **Browser lock** — a sibling Claude session holding the Playwright profile forces rung 2; if both fail, the run asks for a paste (this is correct behavior, not a bug).
- **Fair housing is a real legal surface** — the lint is a floor, not a lawyer; schools stay off camera, no family/kids targeting, ever.
- **Register drift** — if Jen's taste moves again, log it to the ratchet rather than editing prompts directly; the calibration log is designed to outrank defaults.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-07-25-jen-listings.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

