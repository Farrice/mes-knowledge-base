---
description: Cold-start → converting-copy orchestrator. Grounds a market ONCE (real research, cost-previewed), caches it, then assembles + verifies world-class copy. Every later iteration/refinement reuses the cache for $0. "Ground Once, Refine Free."
tier: system
---

# /copy-engine — Cold-Start → Converting Copy (Ground Once, Refine Free)

The end-to-end copywriting orchestrator. From a cold prompt ("write converting copy for product X / market Y / objective Z") it: grounds the market in **real research + social listening** (once, cost-previewed), caches the intelligence, then drives the full Luke Iha copy stack to a verified, converting deliverable. **Every subsequent iteration, refinement, or writers-room pass reuses the cache at $0** — research fires only on a cold market or an explicit `--refresh`.

> **The core invariant (deterministic, not a prompt rule):** all market grounding routes through `execution/avatar_manifold_runner.py ground`, whose reuse gate returns `$0` for a fresh market and only cold-starts (paid) on a cache miss. WARM-reuse is a *code property* — Claude cannot accidentally re-spend. (Satisfies `feedback_ai-memory-dependent-observability.md`.)

## Usage
```
/copy-engine write a converting VSL lead for <product> / market: <market> / objective: <goal> [--asset vsl|ad|email|landing|headline] [--refresh] [--tier free|lean|deep]
```
- **No flags = smart default:** auto-detects COLD vs WARM. You almost never pass a flag.
- `--refresh` — the one flag you'll reach for: re-ground a market you know has moved (paid, cost-previewed).
- `--tier` — `deep` (default, Gemini+VOC ~$0.61) / `lean` (Apify VOC ~$0.11) / `free` ($0, model-side live tools). If you decline the cold-start cost gate, it auto-falls to `free` and BANNERS it.

## The cost model (what you're approving)
| When | Cost |
|---|---|
| **Cold-start a new market (one-time)** | ~$0.50–$2.50 (often **$0** under Google AI Ultra). `estimate` prints it before firing. |
| **Every iteration / refinement / writers-room pass** | **$0.00** (cache reuse) |
| **`--free` or declined gate** | **$0.00** (Recall + WebFetch + free Reddit/HN + Playwright; Standard-tier, `[MODELED]`-tagged) |

---

## PHASE 0 — INTENT (Gate G0)
Parse: **product · market · objective · asset type · awareness guess · proof assets on hand.** Slugify the market to a canonical `<slug>` (lowercase → kebab-case → ≤60 chars; reuse an existing slug if the market is already cached — run `ls .tmp/copy-engine/` and match before minting a new one, to avoid double-grounding).

**Gate G0 — Halt question:** "Confirm: product=X · market=Y · objective=Z · asset=A · awareness≈L. Do you have proof assets (testimonials, stats, before/afters)?" PROCEED requires all five named + a yes/no on proof. *(This cheap gate prevents grounding the wrong market.)*

## PHASE 1 — GROUND (the only paid phase; reuse makes it $0 on iterations)
Route through the chokepoint. It REUSES a fresh dossier at $0 and only cold-starts (paid) on a miss:
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --product "<product>" --tier <tier> 2>&1 | tail -6
```
- **WARM** (`♻️` in output) → skip all research, go straight to Phase 2 ($0).
- **COLD** → the runner prints the cost estimate first. If `--dry-run`/decline → re-run `--tier free` ($0, model fills VOC via free live tools). On approval, it fires Gemini Deep Research + free Reddit/HN + Apify VOC, writes `.tmp/copy-engine/<slug>/ground-dossier.md`.
- **STALE** (`⏳`) → reuses anyway ($0) with a nudge; pass `--refresh` only if the market truly moved.
- Recall grounding (free) also fires model-side: `mcp__recall__search` (2-query focused) for expert/voice cards.

**Gate G2 — Grounding sufficiency.** PROCEED requires: dossier exists AND (`voc_source_urls ≥ 15` OR you accept `[MODELED]` explicitly). If thin and budget allows, `--refresh --tier deep`; else proceed with `[MODELED]` flags propagated. *(Prevents world-class-sounding copy on a fabricated market — the Parallax-02 failure mode for sales copy.)*

## PHASE 2 — STRATEGY + WARM_CORE (interpretation; $0)
Read the dossier and the manifold (run `/avatar-manifold` if a full manifold is wanted; the dossier alone suffices for most assets). Then **write `warm_core`** — the structured intelligence block every refinement workflow consumes — to `.tmp/copy-engine/<slug>/warm-core.json`:
```json
{
  "slug": "<slug>",
  "grounded_at": "<from ground-status.json ts>",
  "tier": "deep|lean|free",
  "dominant_emotion": "...",
  "core_wound": "...",
  "pain_to_promise_gap": "<the gap curiosity must bridge>",
  "market_beliefs": {
    "external_problem": "what the market thinks the problem is",
    "internal_problem": "the real problem / your reframe (UMP)",
    "external_solution": "what the market thinks the fixes are",
    "internal_solution": "your unique mechanism (UMS)"
  },
  "top_voc_soundbites": ["verbatim…", "verbatim…"]
}
```
`market_beliefs` maps **1:1** onto the Curiosity Quadrant's 4 cells; `core_wound`/`dominant_emotion` feed CRAVES + pain-chain. This block is the wiring that lets every later pass be pure craft on real intel. Then:
- `/copy-equation` at offer level → name the single limiting block.
- `/little-big-idea` → the through-line. Awareness level from the dossier → Schwartz ladder.

**Persuasion-mechanics pre-flight** (2 questions, wired 2026-06-09 per the Sean Macintyre deployment audit — answer from the dossier, deploy only on YES):
1. *Is this audience armored?* (burned by gurus, high skepticism, "seen it all" — check VOC soundbites for cynicism markers) → YES: run `skills/sean-macintyre-persuasion-philosophy/` armor-diagnose BEFORE block sourcing; its output feeds the curiosity + proof blocks.
2. *Is the mechanism borrowed or inherited rather than proven?* (UMS lifted from a competitor/template) → YES: run Sean's mechanism-test on the UMS before promising it.

## PHASE 3 — BLOCK SOURCING (parallel sub-agents; $0 — reads warm_core)
Source the 6 blocks. All read `warm-core.json` + the dossier (no new research). Dispatch the **PROOF** block as a sub-agent with research tools (it's the one factual surface) — it emits the claim ledger:
- pain → `/pain-chain` (calibrated by Pain Matrix dim) · promise → `/promise-engineering` (identity ceiling) · curiosity → `/curiosity-engine` (Quadrant from `market_beliefs`) · **proof → verify each candidate stat live**, emit `.tmp/copy-engine/<slug>/proof-claims.md` (claim | source | VERIFIED|LIKELY|UNCONFIRMED) · constraints/conditions → `/constraint-dissolution` + `/conditions-stack`.

## PHASE 4 — ASSEMBLE ($0)
`/copy-from-scratch` with belief-state sequencing + proof-braid → `.tmp/copy-engine/<slug>/draft.md`. No visible block labels. Carries the claim ledger forward.

## PHASE 5 — VERIFY (Gate G5 — the load-bearing gate)
**High-stakes detection:** if the market is a **regulated / harm-bearing domain** — real-estate, mortgage/lending, financial/investing, insurance, medical/health, legal, tax, supplements — add `--high-stakes`. In that mode every $/program/rate/eligibility claim must be **primary-source VERIFIED** (an official `.gov`/program page in the ledger), not merely labeled. LIKELY/UNCONFIRMED is rejected. This is non-optional for regulated markets — a wrong DPA amount or eligibility claim is real harm, not a quality nit.
```bash
// turbo
HS=""   # set HS="--high-stakes" for real-estate / financial / medical / legal / insurance / tax markets
python3 execution/verify_proof_ledger.py --draft .tmp/copy-engine/<slug>/draft.md --ledger .tmp/copy-engine/<slug>/proof-claims.md $HS || echo "LEDGER GATE FAIL — verify/label/cut claims before delivery"
python3 execution/prose_classifier.py check .tmp/copy-engine/<slug>/draft.md || true
```
**Important — "VERIFIED to the dossier" ≠ true.** The Gemini grounding can misattribute amounts or miss a cap. For high-stakes claims, the proof sub-agent must cross-check each $/program/eligibility claim against the **primary source** (the official program page), and label the ledger row `VERIFIED via <authority/URL>`. Claims that can't be primary-verified must be cut or explicitly caveated ("as of <date>, verify current"). Any residual high-stakes flags become an **Agent Verify-At-Send checklist** handed to the client (the licensed professional confirms before publishing).

**Gate G5 — PROCEED requires:** `verify_proof_ledger` exits 0 (standard: every claim present + labeled; high-stakes: every claim primary-source VERIFIED) AND no `UNCONFIRMED` claim presented as fact. On FAIL → re-verify to primary source, label, caveat, or cut. *Do not deliver on a FAIL.* (The freshness-tax hook is the harness-level backstop if this is skipped.)

## PHASE 6 — POLISH ($0)
`/craves-polish` on key lines (mechanism name → Specific/Visual) + velocity compression.

**Stanton clamp-audit (engagement pass) — `/stanton-clamp-audit`:** walk the assembled copy beat by beat (section by section, claim by claim) and mark every place a cold reader's attention would drop — proof that's explained instead of shown, a predictable next benefit, a static feature list. Re-clamp each: open a curiosity debt before each new section, withhold the mechanism one beat longer, give every feature a change. On a sales page a dropped beach ball is an exit; this is the line between copy that's read and copy that's skimmed. Surgical — restore forward pull at named points, never rewrite a verified block.

**Optional Really Real depth layer:** If the user asks for copy with emotional truth, heart, resonance, reader trust, less generic language, or a more human feel, load `skills/lamott-allen-really-real-writing/` after proof is sound. Use it to remove fake empathy, bound inflated promises, name the buyer's real pressure in plain words, and keep conversion intact. Skip this for speed-only copy or when the copy already needs pure structural repair.

**Optional Ward rhetorical-device pass:** When a hook, CTA, or headline must land harder — flat, forgettable, not quotable — run `/ward-rhetorical-engine` (or `/ward-saxon-punch`) on that single line. Apply one classical device (Saxon-punch, chiasmus, antithesis, cadence) to the line carrying the argument so it lingers. Surgical, line-level only; never restructure verified blocks for sound.

**Optional Mitch Albom restraint pass:** When the copy leans on emotion (grief, loss, transformation, story-driven testimonials) and reads as trying too hard to move the reader — stacked adjectives, telling them how to feel — run `/albom-restraint-pass` to strip the reached-for feeling and re-earn it by what's withheld ("sentiment without sentimentality"), so the emotional beat cuts instead of strains. For a story-first asset that needs its one human truth named first, `/albom-theme-first-engine`. Emotional craft only — never override verified proof or invent feeling claims the intel can't back. Skip for pure transactional copy.

**Optional Michael Connelly telling-detail vividness pass:** When the copy reads as an abstract benefit list ("save time, reduce stress, scale faster") and you need the reader to *infer* the benefit from one concrete particular (trusted more than being told), run `/connelly-copy-detail` (or `/telling-detail-engine` on a specific line) to replace the abstraction with the single true detail that implies the feature set — with a per-detail honesty-spine confirmation that every detail is real/substantiated. Pairs with `/momentum-audit` when the draft has "good places to stop." Detail-selection only; never manufacture a claim the verified proof can't back.

**Optional Ocean Vuong perceptual defamiliarization pass:** When a hook, lead, or key image reads as platform-sameness — the line any AI would write — run an Ocean Vuong estrangement pass (Species Test) to defamiliarize the image so it demands a re-read. Perceptual freshness only; never override clarity-to-action or verified proof. Skip for pure transactional copy.

**Optional Paul Harding sensory-perception pass:** When the copy describes the product/outcome as an abstract benefit or feature list and never makes the reader FEEL it — no texture, no luminous concrete experience — run `/harding-perceptual-copy` (or `/harding-two-things` / `/harding-precision-wonder` on a specific block) to give the reader the real, precise product detail AND the felt experience of it, letting them infer the benefit by recognition. Sensory maximalism distinct from Connelly's one-detail economy and Vuong's estrangement: render the seeing so it lands as recognized truth. The honesty spine is load-bearing — every rendered particular must be true; never manufacture a sensation the verified proof can't back. Perception/sentence-surface only; never override clarity-to-action or verified proof. Skip for pure transactional copy.

**Optional Bill Browder high-stakes grip pass:** When the copy carries dry/complex domain material (finance, lending, compliance, legal, technical specs) that must grip, OR the stakes land flat / the threat is asserted not felt, OR there's a real adversary (a system, a status quo, a named villain) — run `/browder-next-sentence-test` to flag every comfortable stopping point and re-engineer the pull, `/browder-stakes-architecture` to build the caring before the fall and escalate real jeopardy, and `/browder-villain-evidence` to render the adversary through receipts so the accusation survives a lawyer. Grip + jeopardy + evidenced-villain only; the honesty spine is load-bearing — never manufacture a stake or a claim the verified proof can't back. Skip for low-stakes transactional copy with no real adversary.

**Optional Susan Orlean telling-subject + pull-the-punch pass:** When the copy must make an *overlooked or low-demand* subject feel worth caring about (a niche product, an unglamorous service, an origin/brand story the reader doesn't think they need) — run `/orlean-telling-subject` to frame the small specific (the door) that secretly carries the large theme (the house), `/orlean-wait-what-lead` to open on one true, picture-able detail that overcomes "I don't need to read this," and `/orlean-pull-the-punch` to cut overwritten "look-at-me" prose down to plain confident lines that actually land. Subject-framing + seductive-lead + restraint only; the honesty spine is load-bearing — the wait-what detail must be real, never manufacture significance the proof can't back. Skip for high-demand transactional copy where the reader already wants the thing.

**Optional Lulu conviction + authenticity pass:** When the copy must *install a belief* rather than just inform — a manifesto body, a contrarian thesis, a founder-voice landing page — run `/lulu-conviction-copy` to sequence belief installation (recognition hook → crack → new framework → identity bridge → evidence cascade), then `/lulu-authenticity-engineering` to strip corporate signals and keep the emotional "wrongness" AI would sand off. The one nerve: it has to be real or it dies on contact — never manufacture authenticity over claims the verified proof can't back. Skip for straightforward transactional copy where the proof already carries the sale.

## PHASE 7 — FINALIZE (+ optional creative)
```bash
// turbo
python3 execution/chain_runner.py finalize "<asset> for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow copy-engine \
  --type Content --intent N --expert-score N --adversarial N \
  --factual <score-from-ledger> --sub-agents <n> \
  --notes "Factual Grounding: <score> | Verification: PASS | Grounding: <tier>, voc_urls=K | Cache: WARM|COLD"
```
**The orchestrator must grep finalize output for `QUALITY GATE BLOCKED` and NOT deliver on a match** (finalize exits 0 even when it blocks). Derive `--factual` from the ledger (all VERIFIED → ≥8; UNCONFIRMED-as-fact → <6).
Optional ad creative (gated): `python3 execution/creative_router.py route --request "..."` → `python3 execution/fal_budget_guard.py check` → `/fantastic-posters`.

---
## Iteration contract (why this is "Refine Free")
Re-running `/copy-engine` on the SAME market, or running ANY standalone refinement (`/craves-polish`, `/curiosity-engine`, `/writers-room`, `/copy-block-audit`, `/pain-chain`), hits **WARM** at Phase 1 → **$0**, and reads `warm-core.json` for the market psychology. Research fires once per market; craft is infinite and free. Cost reappears only for a genuinely NEW factual claim (one `perplexity_ask` ~$0.02) or an explicit `--refresh`.

## Graceful degradation (never fabricate to fill a gap)
Every external call chains `Gemini → Perplexity → free/recall → [MODELED]`. Budget-exhaustion DEGRADES to $0 (the runner fails closed, never escalates pools). A degraded ground proceeds with `[MODELED]` flags propagated to G5 — the system labels uncertainty, it never invents.

## Quality Gate
3 halt gates only (G0 intent · G2 grounding · G5 verification) — do not add more (rubber-stamp anti-pattern). Blocks invisible in customer copy. Promise at identity edge. Claim never bigger than proof. Mechanism name passes the portability test. Clarity is King.
