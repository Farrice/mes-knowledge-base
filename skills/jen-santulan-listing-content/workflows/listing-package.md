---
description: URL/address/description in → sendable listing package out. Fetch + photos → market research with receipts → register-aware hooks + scripts → ONE taste checkpoint → caption + forwardable send text, compliance-gated. "Research Once, One Checkpoint, Sendable Out."
---

# /listing-package — Listing URL → Sendable Package (One Checkpoint)

The end-to-end listing content engine, codified from the 5200 Armida arc (2026-08-05: three hook generations, two taste rejections, a claims ledger that caught a phantom spa, a phantom basement, and a wrong bath count — this workflow makes all of those mechanical). Client: Jen (default); core is portable — a second client is a voice-pack + register-file drop-in.

> **The core invariants (deterministic, not prompt rules):** facts route through `execution/listing_intel.py` (parse → diff → ledger — contradictions are code-detected, not vibes); compliance routes through `execution/fair_housing_lint.py` (exit 2 = no ship); the send text routes through `execution/client_package_lint.py`. The model does strategy, hooks, scripts, and taste — the machines do facts, diffs, and floors.

## Usage

```
/listing-package <zillow/redfin/realtor url>
/listing-package <street address>
/listing-package --paste            (then paste any listing description)
```
- **No flags needed, ever.** Input type auto-detected: URL → fetch · address-shaped → search-then-fetch · anything else → treated as pasted description. Tier auto-derived from list price. `--tier fthb|luxury` and `--client` exist only as overrides.
- Re-running on the same property RESUMES: existing `_active/jen-listings/<slug>/listing.json` → skip fetch/research, regenerate downstream only (WARM pattern).

## The cost model
| When | Cost |
|---|---|
| Fetch via Playwright (primary) | $0 |
| Fetch fallback — Apify `web` actor (only if browser blocked/captcha'd) | ~$0.003 |
| Neighborhood amenities via Apify `maps` (optional, luxury tier) | ~$0.007 |
| Market research (`research.py --depth standard`, Gemini-first) | usually $0 |
| Everything else (strategy, hooks, scripts, caption, package) | $0 |

---

## PHASE 0 — INTENT (Gate G0)

Detect input type. Mint slug `<number>-<street>-<city>` (check `ls _active/jen-listings/` first — existing dir = RESUME, never duplicate). Guess tier from any visible price.

**Gate G0 — halt only if:** no URL, no address, no description — ask for one of the three. Otherwise proceed silently. *(Cheap gate; prevents researching the wrong property.)*

## PHASE 1 — INTAKE ($0 → $0.003)

Fetch ladder — **never fabricate a fact a rung couldn't reach:**
1. **Playwright** (listing page): navigate → `browser_evaluate` to pull JSON-LD + full facts text + photo IDs → save dump to `_active/jen-listings/<slug>/page-dump.json`. If "Browser is already in use" (sibling session lock) → rung 2, and note it.
2. **Apify `web` actor** (`rag-web-browser`): `python3 execution/apify_client.py` web fetch of the URL (~$0.003; on `budget_exhausted` → rung 3).
3. **Ask for a paste.** One request to Farrice; `--paste` mode parses it. NEVER proceed on invented facts.

Photos: render the photo-ID grid in-page (numbered contact-sheet technique — 4-across grid, screenshot, repeat), save `photo-contact-sheet-*.jpeg` to the slug dir, and READ them — visual claims in scripts must trace to a photo or be marked walkthrough-confirm.

Then:
```bash
// turbo
python3 execution/listing_intel.py parse _active/jen-listings/<slug>/page-dump.json --slug <slug>
python3 execution/listing_intel.py diff --slug <slug>
python3 execution/listing_intel.py ledger --slug <slug>
```
The diff output (contradictions: description-vs-MLS-fields, bed/bath arithmetic, price-jump/Zestimate-gap ambush, brand claims) feeds the don't-say list automatically.

## PHASE 2 — MARKET (usually $0)

Real tools, receipts on everything — **never answer market questions from training memory:**
```bash
// turbo
python3 execution/research.py "housing market <zip>: median sale and list price, price per sqft, days on market, YoY trend, <month year>" --depth standard --json
```
Plus, per tier: FTHB → comparable rents (rent-vs-mortgage math inputs); luxury → comparable actives in prestige-adjacent cities (label algorithmic comp sets as UNCONFIRMED-pending-CMA with a fallback line). School ratings + distances (caption data only). Optional luxury amenities: `maps` actor. Merge external findings into the ledger (`source: external`, confidence from the receipt).

**Honesty anchors computed here, before any writing:** $/sqft vs zip median (ABOVE median = the what-you-get frame is the only honest frame; no "deal"/"smart money" claims) · price-history jump % · Zestimate gap (both = open-house Q&A prep, never content).

## PHASE 3 — STRATEGY ($0, internal — no stop)

Tier → **register** per `_active/jen-listings/CLAUDE.md` Override List ladder. Buyer map (3-5 named buyers, life-logistics framing, fair-housing-safe). Magic trifecta (pattern interrupt · the real pitch · bonus proof). **What-NOT-to-claim block** from the diff + honesty anchors. Ten lines, carried into the checkpoint header.

## PHASE 4 — GENERATE ($0)

Load: `skills/kallaway-hook-mastery/SKILL.md` + this skill's `PROMPT.md` + `references/jen-real-voice-profile.md` + **`references/jen-calibration-log.md`** (felt verdicts outrank defaults). Execute `references/prompts-v2/listing-hook-set.md` (register-ladder v2.1) with listing.json + ledger as fact source: 6 hooks per the tier slot map (spoken ≤12 words · on-screen text · visual · lock-in · scene-built bodies), cover-text→photo pairs.

## GATE G1 — FARRICE TASTE CHECKPOINT (the one pause)

Present: the 10-line strategy card + all 6 hooks + full scripts. This is where his judgment operates — iterate HERE. Rules: feedback-turn protocol (restate verdicts → ONE take by ONE pen); **spiral brake: 2 rejected takes on one artifact = stop producing variants, go back to the inputs**; log felt verdicts to the Jen ratchet (`python3 execution/voice_ratchet.py add --client jen ...`). **Caption and send text do NOT render before his verdict.**

## PHASE 5 — PACKAGE ($0)

On approval: execute `references/prompts-v2/listing-send-package.md` → the forwardable text (numbers block → options w/ one top pick → cover pairs → register-matched caption → filming notes → don't-say list). Write the repo substrate: `_active/jen-listings/<slug>/<slug>-SHOOT-SHEET.md` (strategy, full research, ledger pointers, diagnostics) + `SEND-TO-JEN-text.md` + `.metadata.json` sidecar.

## PHASE 6 — GATES (Gate G2 — the veto; do not deliver on FAIL)

```bash
// turbo
python3 execution/fair_housing_lint.py check --file _active/jen-listings/<slug>/SEND-TO-JEN-text.md --context package
python3 execution/client_package_lint.py _active/jen-listings/<slug>/SEND-TO-JEN-text.md
python3 execution/prose_classifier.py check _active/jen-listings/<slug>/SEND-TO-JEN-text.md || true
```
- fair_housing_lint exit 2 → fix and re-run; this is a hard floor, not a suggestion.
- prose_classifier: judge findings against the register (production-sheet structure flags are expected; em-dashes/slop vocab in SPOKEN lines are real and get fixed).
- **Claims coverage:** every $/rate/eligibility/spec claim in spoken text exists in the ledger as VERIFIED, or its fallback line is used instead (**high-stakes rule — real estate is a regulated domain; primary-source only for program/rate claims**).

## PHASE 7 — FINALIZE

```bash
// turbo
python3 execution/chain_runner.py finalize "<slug> listing package — hooks+scripts+caption+send text" \
  --expert "Jen Santulan" --skill jen-santulan-listing-content --workflow listing-package \
  --type "Client Work" --intent N --expert-score N --adversarial N \
  --factual <from-ledger: all VERIFIED → ≥8> --sub-agents <n> \
  --content-file _active/jen-listings/<slug>/SEND-TO-JEN-text.md \
  --notes "Register: <tier> | Ledger: <n> claims, <n> contradictions surfaced | Fetch: <rung> | Factual Grounding: N | Verification: PASS"
```
**Grep the output for `QUALITY GATE BLOCKED` and do NOT deliver on a match** (finalize exits 0 even when it blocks).

## PHASE 8 — LOOP (next session, when the reel is live)

Which option she filmed + 48h numbers + any felt verdicts → `voice_ratchet.py add --client jen`; strong performers → ground-truth candidates (`knowledge/expert-benchmarks/jen-listing-content/`). This loop is what makes run N+1 land the register on the first pass.

---

## Graceful degradation (never fabricate to fill a gap)
Fetch: Playwright → Apify web → ask-for-paste. Research: Gemini → Perplexity → free floor, findings labeled by the receipt. Photos unavailable → visual directions marked "confirm on walkthrough," never invented. A claim that can't be verified ships as its fallback line or not at all.

## Output Schema
| Artifact | Path | Valid when |
|---|---|---|
| Listing facts | `_active/jen-listings/<slug>/listing.json` | parses; nulls where unknown; never-invented values |
| Claims ledger | `<slug>/claims-ledger.json` | every spoken claim traceable; contradictions carry fallback lines |
| Diff report | `<slug>/claims-diff.json` | contradiction/risk/confirm items present when the data disagrees |
| Photo sheets | `<slug>/photo-contact-sheet-*.jpeg` | numbered grid, reviewed |
| Shoot sheet (substrate) | `<slug>/<slug>-SHOOT-SHEET.md` | strategy + hooks + diagnostics + pre-shoot checks |
| **Send text (the deliverable)** | `<slug>/SEND-TO-JEN-text.md` | passes both lints; one top pick; forwardable as-is |

## Quality Gate
- [ ] G0/G1/G2 are the ONLY halt gates — do not add more (rubber-stamp anti-pattern)
- [ ] Register selected from tier BEFORE generation; slot rule honored (FTHB-Permission mandatory <$1.5M, forbidden ≥$2M)
- [ ] Ledger built by `listing_intel.py`, not by hand; every contradiction in the don't-say list with a fallback
- [ ] Market claims carry receipts; $/sqft-vs-median honesty anchor computed before writing
- [ ] G1 happened: Farrice saw hooks + scripts before caption/package rendered
- [ ] Both lints clean on the send text; finalize ran with `--content-file`; no `QUALITY GATE BLOCKED`

**Auto-fail (run is incomplete, not merely short):** a fact stated on no rung of the fetch/research ladder · FTHB-Permission hook in a luxury set · send text containing a repo path or tool name · don't-say list absent · caption rendered before the G1 verdict.
