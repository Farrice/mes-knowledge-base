# Research Integrity Audit

**Date:** 2026-06-01
**Scope:** Every research producer/consumer in the system, every workflow/skill bypassing the unified research engine, and every already-shipped output carrying grounding risk.

---

## Verdict

The system had a structural bug class, not a one-off mistake: paid-research calls could **log cost and report success for calls that returned no validated content** (false logging / false PASS), findings could be **persisted without a source URL**, and `[MODELED]` placeholder data could **slip past the gate and read as fact**. The net effect across 2026 (pre-2026-06-01) was a body of dossiers, avatars, and decision briefs that *look* researched — confident stats, verbatim "VOC," named-source attributions — but are not link-verifiable, and in several cases were produced by swarms that ran with **zero grounding queries** while logging "success." That bug class is **now FIXED**: there is a single unified research engine (`execution/research.py`) sitting on a shared trust contract (`execution/research_contract.py`), where (1) cost is logged *only* after `validate_engine_text()` returns ok, (2) a `Finding` with an empty `source_url` cannot be constructed (raises at construction), and (3) `[MODELED]` content is hard-blocked under `research_quality_gate.py --strict`. Every accelerator (Gemini, Perplexity) and the free `native_floor` now fail closed to `$0` with `cost_logged=0.0` and an honest receipt. **Residual risk** is twofold: (a) ~30 workflows/skills still bypass `research.py` (most are well-gated, but several skills market "research" with no enforced source gate at all), and (b) a backlog of already-shipped outputs from the false-PASS era are still on disk and some feed real money/positioning decisions — these need re-grounding or an explicit "AI estimate, verify before deciding" caveat before reuse.

---

## Now-Fixed (Trustworthy Going Forward)

The grounding floor is real and enforced for anything routed through the engine.

### The Unified Engine
- **`execution/research.py`** — THE engine. Thin facade dispatcher: Gemini-first → Perplexity fallback → `native_floor` (bedrock WebSearch + WebFetch + Tavily + Recall, $0, cannot break). Returns a typed `ResearchResult` with an honest Research Receipt. CLI: `run / ground / ingest / plan / gemini-start / gemini-collect`.
- **`execution/native_floor.py`** — the free floor. Every `findings.append` carries a real `source_url`; URL-less candidates are quarantined; `cost_usd` hard-set to `0.0`. Already conformant to the contract.
- **`execution/research_personas.py`** — pure plan/prompt generator (no I/O, no cost). The briefs it emits *mandate* a real `source_url` per finding, reinforcing the contract downstream.

### The 3 Trust-Fixes (the bug class, closed)
1. **No false cost logging.** In `deep_research_client.py` and `perplexity_client.py`, `validate_engine_text()` runs *before* `_log_usage`. On invalid/empty content they return `status='failed'`, `estimated_cost=0.0` ("failures never cost"), and `_log_usage` is unreachable. Cost is logged only on validated content.
2. **No unsourced findings.** `research_contract.py` defines the `Finding` type that **raises `InvalidFinding` at construction if `source_url == ''`**. `deep_research_engine.py`'s parsers quarantine URL-less claims (append to `_quarantine`, skip `findings.append`) — "never persist source_url=''".
3. **No silent `[MODELED]` passthrough.** `research_quality_gate.py` reads content first, then hard-blocks any `[MODELED]` under `--strict` (CRITICAL), plus source-count, provenance ≥80%, recency 2024+, naked-claim, and echo-chamber checks. `avatar_manifold_runner.py` tags source-less VOC `[MODELED]` and structurally fences it so the strict gate catches it; degrade writes `voc_urls=0` rather than faking findings.

### The Routing Lock
- **Mandatory routing bindings** are mirrored in `execution/routing_enforcer.py` (`avatar_manifold_coldstart`, `cold_start_converting_copy`) and re-checked post-hoc in `finalize()`.
- **Gold-standard gated path:** `/avatar-machine` → `avatar_manifold_runner.py` (Gemini Deep Research + Apify VOC + FB Ad Library + Recall) with `research_quality_gate.py validate --strict` enforcing ≥15 sources, provenance ≥80%, recency 2024+, zero `[MODELED]`. Skip only with `--no-ground` + `--voc-file`.
- **Reference engine consumers (low risk):** `deep-research.md`, `deep-research-gemini.md`, `parallel-research.md`, `research-swarm.md` are migrated to `research.py` and lead with a Research Receipt + strict gate.

---

## Consumers Still Bypassing the Engine

These run research *outside* `research.py`. Most are well-gated; the one-line fix for nearly all is the same: **route the foundation research call through `research.py` (and run output through `research_quality_gate.py`).** Sorted by risk.

| File | Path | Risk | Why it bypasses | One-line fix |
|---|---|---|---|---|
| `skills/market_intelligence/SKILL.md` | raw-tools | **HIGH** | Markets "live SERP validation / real data" for a $5K dossier, but `keyword_auditor.py` SERP is **MOCKED** and there's no enforced source gate. | Route SERP/market claims through `research.py`; remove/replace the mocked SERP and add a strict gate, or relabel output as estimates. |
| `skills/consumer-posture-research/SKILL.md` | raw-tools | **HIGH** | "Validate with real-time web search" with no tool binding, no source-count floor — behavioral predictions can be pure model priors. | Bind validation to `research.py` + enforce a source floor before claiming "research-grounded." |
| `skills/business-intelligence-audit/references/extraction-protocol.md` | raw-tools | **HIGH** | Only gate is a manual checkbox ("3 external sources checked"); confident competitor claims can ship unverified. | Replace the checkbox with `research.py` + `research_quality_gate.py` enforcement. |
| `skills/bond-halbert-copywriting/SKILL.md` | none | **HIGH** | Description sells "deep market research," but the mechanism is philosophy ("live in the market") — no web tool, no VOC pipeline. | Stop framing copy as "market-researched"; if grounding is claimed, run `/copy-engine` ground first. |
| `.agent/workflows/generate-brief.md` | direct-client | medium | Phase 3 calls `deep_research_engine.py` directly + perplexity/search_web. Mitigated by provenance tags + quality gate. | Swap direct `deep_research_engine` call for `research.py --depth deep`. |
| `.agent/workflows/research-landscape.md` | direct-client | medium | Phase 1 Demand Scan calls `deep_research_engine.py` directly. | Route Demand Scan through `research.py --depth standard`. |
| `.agent/workflows/research-topic.md` | direct-client | medium | Foundation Research uses `deep_research_client/engine` directly. | Replace with `research.py --depth deep/max`. |
| `.agent/workflows/grounding-pass.md` | direct-client | medium | `--research-first` calls `deep_research_engine.py` directly (purpose is to *add* grounding, so low misrep). | Point `--research-first` at `research.py`. |
| `.agent/workflows/parallax.md` | raw-tools | medium | Phase 2.5 ad-hoc Recall + Perplexity by claim type. Strong mitigation: mandatory halt/proceed gate for Editions 02+ (origin: Edition 02 shipped 7 fabrications). | Route STAT/TECHNICAL claims through `research.py` instead of ad-hoc Gemini. |
| `.agent/workflows/swarm.md` | raw-tools | medium | Phase 2.5 Perplexity gate ad hoc (not `research.py`). Mitigated by provenance tags + quality gate on synthesis. | Route synthesis through `research.py ingest`. |
| `.agent/workflows/research-sprint.md` | raw-tools | medium | Task-routed Perplexity/search_web/Apify, no `research.py`. | Route foundation through `research.py`. |
| `.agent/workflows/parallel-swarm.md` | raw-tools | medium | `--research/--grounded` spawns ad-hoc sub-agents; **no source gate** on pre-research, fed to personas as "real market data." | Run pre-research through `research.py`; gate before persona injection. |
| `.agent/workflows/icp-research.md` | raw-tools | medium | Apify + Perplexity, no `research.py`, no quality gate (the icp-* under-grounding failure mode). | Route through `/avatar-machine` ground or `research.py`. |
| `.agent/workflows/icp-deep-dive.md` | raw-tools | medium | Perplexity + search_web ad hoc, no source gate. | Same as above. |
| `.agent/workflows/individual-consumer-finder.md` | raw-tools | medium | Apify-first w/ Perplexity fallback; without a gate a fallback can substitute synthesized quotes. | Add quality gate; route through `research.py`/`avatar_manifold_runner`. |
| `.agent/workflows/mini-brief.md` | raw-tools | medium | Ad-hoc Perplexity + **hardcoded "GROUNDED" labels** in template (over-states grounding); no quality gate. | Make GROUNDED conditional on a real gate; route through `research.py`. |
| `.agent/workflows/grace-city-blueprint.md` | raw-tools | medium | 2 ad-hoc Perplexity deep-research queries ground the whole blueprint; no quality gate. | Route pre-flight through `research.py`. |
| `.agent/workflows/grace-media-diagnostic.md` | raw-tools | medium | Ad-hoc Perplexity feeds scored diagnostic; no source gate. | Route audience research through `research.py`. |
| `.agent/workflows/hunt-trends.md` | raw-tools | medium | Perplexity + Apify, no quality gate; trends consumed downstream as grounded zeitgeist. | Route macro-trend track through `research.py`. |
| `.agent/workflows/competitor-intel.md` | raw-tools | medium | Perplexity + WebFetch + Playwright; no formal source gate (strong browser discipline mitigates). | Add a source-count gate; route foundation through `research.py`. |
| `.agent/workflows/spy-amazon.md` | raw-tools | medium | Apify-first market research, no quality gate. | Route through `research.py` + gate. |
| `.agent/workflows/launch-monitor.md` | raw-tools | medium | Apify-first monitoring, no source gate. | Add gate on monitoring data. |
| `.agent/workflows/diandra-growth-sprint.md` | raw-tools | medium | Perplexity (budget-permitting) + **hardcoded "GROUNDED"** even when Perplexity is skipped. | Make GROUNDED conditional; route through `research.py`. |
| `.agent/workflows/diandra-content-engine.md` | raw-tools | medium | Hardcoded "Research: GROUNDED" label; leans on Recall + ad-hoc Perplexity. | Make label conditional on a real gate. |
| `.agent/workflows/authority-flywheel.md` | raw-tools | medium | search_web + Perplexity, no quality gate; positioning presented as grounded. | Route through `research.py`. |
| `.agent/workflows/council.md` | raw-tools | medium | Ad-hoc Perplexity, no quality gate — **strong mitigation:** mandatory Claims Grounding Table (GROUNDED/SUPPLEMENTED/PROJECTED). | Route Step 2.5 grounding through `research.py`. |
| `.agent/workflows/roundtable.md` | raw-tools | medium | Same as council: Claims Grounding Table present, research path raw-tool. | Same as council. |
| `.agent/workflows/teardown.md` | avatar-runner | low | Grounds via `avatar_manifold_runner.py ground --tier deep` + recon tools; ethics gate + cost gate + routing binding. Well-gated bypass by design. | None required; keep gate logged in finalize. |
| `skills/grace-andrews-media-company/SKILL.md` | direct-client | medium | Real Perplexity deep-research path, but workflow 12 offers a `search_web` fallback with **no source-count gate**. | Add a source floor to the fallback. |
| `skills/sabri-suby-ai-advertising/references/implementation.md` | direct-client | medium | Real but fully human-driven (ChatGPT DR + FB Ads Library + Reddit); no in-skill enforcement. | Add a "did you actually run the forensics?" gate or route via engine. |
| `skills/kieran-flanagan-audience-intelligence/genius.md` | none | medium | "Verified by frequency analysis" over a user-supplied corpus — rigor is operator-dependent. | Require a real corpus; flag "verified" as corpus-dependent. |
| `skills/daniel-priestley-oversubscribed/.../icp-heartfelt-alignment.md` | none | medium | Founder-supplied ICP reads as market-validated when it's reasoning-only. | Caveat as reasoning-only; route real VOC via `/avatar-machine`. |
| `skills/april-dunford-positioning/workflows/dunford-category-decision.md` | none | medium | Demands "observed customer behavior" but no tool fetches it; category claims can read as evidence-grounded. | Bind the "would my buyer Google this?" test to `research.py`. |
| `skills/diandra-escobar-linkedin-growth/SKILL.md` | raw-tools | medium | Algorithm/competitor claims have no enforced source gate. | Gate platform-mechanics claims; cite or flag. |
| `skills/tom-noske-content-creation/SKILL.md` | raw-tools | medium | Lists research as a step, binds no tool, no source floor. | Bind to `research.py`; enforce verify-or-flag. |
| `skills/jessica-jensen-platform-intelligence/SKILL.md` | raw-tools | medium | Platform-behavior claims presented as verified, no source gate. | Flag platform-mechanics as model-inferred unless cited. |
| `execution/parallel_swarm.py` | raw-tools | medium | Calls Gemini/Perplexity clients directly (cost path is safe via fixed clients) — but **swarm OUTPUT skips the `Finding`/provenance gate**, so synthesis can carry claims without a `source_url`. | Migrate synthesis through `research.py ingest` (engine `native_swarm` already exists for this). |

**Well-gated bypasses (low/none, no action needed):** `avatar-machine.md`, `copy-engine.md` (Ground-Once-Refine-Free, fails closed to $0), `skills/luke-iha-avatar-machine/SKILL.md` (gold standard), `skills/luke-iha-copy-blocks/workflows/*` (warm-cache reuse, honest degradation), `betting-edge.md` / `picks-tonight.md` (real NBA API, web is context-only), `autopilot.md` (dispatcher), `supercomputer/SKILL.md` + `brand-operating-system/SKILL.md` (inherit composed gates), `corey-mcclain-persona-engineering` (overtly "grounded fiction"), `oren-taste-development` (aesthetic, not factual), `kieran-flanagan-content-engine/workflows/03` (honest verify-or-flag), `growth-format-sprint.md`. Engine-internal infra (`research_contract.py`, `apify_client.py`, `gemini_client.py`, `deep_research_engine.py`, `research_quality_gate.py`) carries no false-log risk. Pure non-research matches (`variant-sprint.md`, `calibrate.md`, `creative-prompt.md`) excluded.

---

## Grounding-Suspect Past Work

Already-shipped outputs that carry decision weight but are not link-verifiable. **Honest framing:** most modeled data *was labeled* (`[MODELED]`, "PROJECTED", DEGRADED headers) — these are provenance gaps, not deliberate fabrication. The danger is reuse, not the existence of the file. Sorted by severity.

### HIGH — re-ground before any reuse (money / real-person / sellable / health claims)

| File | Why | Re-ground action |
|---|---|---|
| `deliverables/prediction-market-business-briefing.md` | Real-money go/no-go, ZERO URLs, hard stats as fact ("$1→$3.3M in 8mo", "7.6% of wallets profitable", "~$9.5B/mo"). | Re-run `research.py --depth deep` on each stat; attach URLs or pull the claim. |
| `deliverables/prediction-market-partner-briefing.md` | Partner-decision briefing, ZERO URLs, named trader stats as fact. | Same — re-verify every trader/volume stat with sources. |
| `deliverables/prediction-market-proposal-package.md` | Compensation/partnership ask built on the same unverified profit/market-size claims. | Re-ground the underlying claims; gate before sending. |
| `research_outputs/prediction-market-arb/00-research-dossier.md` | Capital-allocation dossier; header claims "9 searches / 4 extractions" but only 2 URLs; dense unsourced financials. | Re-run through engine; quarantine every URL-less claim. |
| `research_outputs/dj-event-matchmaking-research.md` | Andrea/Resonance go/no-go on ~35 stats, ZERO URLs ("78% dating-app fatigue", "Tinder lost 594K"). | Re-verify each market stat; supersede with a sourced brief. |
| `research_outputs/ghostwriting_niche_selection.md` | Authority Flywheel niche decision on ~23 unsourced stats (pricing bands, "~60K NSCA members"). | Re-ground pricing/sizing via `research.py`. |
| `research_outputs/ai_authority_architect_agents/` (26 dossiers + `.resolved` dupes) | VOC/pain-mining with attributed verbatim quotes, **0 URLs each (verified across all 26)**. | Re-ground via `/avatar-machine`; delete `.resolved` duplicates. |
| `research_outputs/ai_authority_architect_agents/sabri_suby.md` | Exemplar: "pain quotes" + "Forbes (April 2025)" attributions, Confidence: HIGH, ZERO URLs. | Re-ground or relabel quotes as modeled. |
| `research_outputs/ai_authority_architect_agents/final_synthesis.md` | Rolls up the 26 unsourced dossiers into "decision-ready" conclusions. | Re-synthesize only after dossiers re-grounded. |
| `deliverables/Human_Values_Collective_Delivery/.../grounding-document.md` | **Real-person** (Javier Payano) named facts as verified (award, employer, band-since-2005); claims "30+ sources," ~1 URL. Defamation/accuracy exposure. | Verify every real-person attribution against a live source before client use. |
| `deliverables/Kens_Fasting_Package/4_Market_Research/Shadow_Market_Analysis.md` | "CONFIRMED: wide-open market," ZERO URLs; drives a launch go-decision. | Re-run demand/competitor scan through engine. |
| `deliverables/Kens_Fasting_Package/4_Market_Research/Trend_Report_Fasting_2026.md` | Cites "Perplexity, Google, Reddit, IG/TikTok" but ZERO URLs; virality stats as fact. | Re-ground engagement stats or relabel as estimates. |
| `_active/kens-fasting/swarm_research/metadata.json` | Proof of false-PASS era: all 5 agents `grounding_queries: 0`, gemini-2.5-flash, 20260331. | Treat all downstream Ken outputs as ungrounded; re-run. |
| `_active/kens-fasting/swarm_research/synthesis.md` | Built on zero-grounding run; itself admits "lack of credible scientific evidence," no URLs. | Re-ground; do not ship health claims. |
| `_active/kens-fasting/04-deliverables/instagram-and-landing/landing_page_copy.md` | **Shipped sales copy**, unsourced health claims + results guarantee that its own synthesis demanded removing. **Medical-claim liability.** | Pull guarantee/"exact formula" language now; re-ground before relaunch. |
| `_archive/2026-07-28-org-sweep/unbottlenecked_blueprint/04-deliverables/06_icp_intelligence_report.md` | "5-Agent VoC Swarm," ZERO URLs, ZERO verbatims; modeled language drives $15k + $99/mo offer decisions. | Re-ground via `/avatar-machine`; re-validate offer assumptions. |
| `products/promptbase/test-outputs/03-competitive-teardown-TEST-OUTPUT.md` | **Sellable product output.** Fake provenance line ("Sourced from Reddit threads…" → links to nothing); temp:0, no web access → all numbers fabricated false precision. | Add a "these are AI estimates — verify before deciding" disclaimer to the product (see root cause below). |
| `.tmp/copy-engine/ground-status.json` | Canonical false-PASS: `rqg_strict_pass=false` while `status='PASS'` (SFV cold-start). | Re-run SFV ground; reconcile status to strict result. |
| `.tmp/copy-engine/teardown-kajabi/ground-dossier.md` | Header "rqg_strict=pass" but body DEGRADED (Gemini+Perplexity unavailable), 8 thin YouTube-title soundbites, empty Market Landscape, `[MODELED]`. | Re-run Kajabi ground when accelerators are available. |
| `_archive/2026-07-28-org-sweep/teardown-kajabi/state.yaml` | anchor-001 = "GROUND dossier (DEGRADED)"; 4 copy blocks ref a failed foundation. | Re-anchor to a re-grounded dossier before producing copy. |
| `_active/coach-cooz/_DEPRECATED/.../04_buyer_profile.md` | Invalidated "echo chamber" $10K-buyer avatar; poisoned root of the 8-file deprecated swarm. | Keep deprecated; confirm v2 fully supersedes. |
| `_active/coach-cooz/_DEPRECATED/06-manus-research/mckinsey_level_partnership_analysis.md` | Drove Warner Bros / Whole Foods / Enrichfit partnership proposals on the invalidated foundation. | Audit whether derived partnership artifacts are still in circulation; retract if so. |
| `_active/coach-cooz/_DEPRECATED/06-manus-research/Coach_Cooz_Fitness_Business_Strategy_Playbook.md` | 58KB playbook anchoring the unreachable "Apex Operator" avatar; no URLs. | Keep deprecated; ensure nothing live references it. |
| `_active/farrice-brand/icp-intelligence/deliverables/SAMPLE-REPORT-business-coach-founders.md` | **Client-facing product template**: "47 quotes… all sourced from real conversations," ZERO URLs. The unsourced-VOC pattern propagates to paid work. | Rebuild the sample via `/avatar-machine` with real source-linked VOC. |

### MEDIUM — verify before external use / decision dependency

| File | Why |
|---|---|
| `deliverables/Human_Values_Collective_Delivery/.../brand-intelligence.md` | "10+ parallel sources" header, 1 URL in-file (real org/person). |
| `deliverables/Human_Values_Collective_Delivery/.../human_values_collective_profile.md` | "Deep Research Profile," ~18 URLs, several headline claims not individually linked. |
| `deliverables/Kens_Fasting_Package/1_Product_Strategy/Swarm_Research_Summary.md` | Rolls up unsourced shadow-market + trend claims; not link-verifiable. |
| `deliverables/coach-cooz-final/source-docs/avatar_swarm_outputs/07_market_intelligence.md` | Market-sizing ("$20.1B→$37.0B, 8.2% CAGR") attributed by name only, 0 http links; drives pricing. |
| `deliverables/coach-cooz-final/source-docs/avatar_swarm_outputs/01–04_*.md` | Reddit verbatims + quantified behavior labeled GROUNDED, ZERO URLs; $10K price validated against unlinkable "Perplexity market data." |
| `deliverables/coach-cooz-final/source-docs/COMPETITIVE_INTELLIGENCE_EXECUTIVE_COACHES_2026.md` | ~5 URLs for an extensive named-competitor/pricing landscape; feeds positioning. |
| `deliverables/coach-cooz-deep-dive-march-2026.md` | "pulled last 3 campaigns data," ZERO URLs, no attached metrics. |
| `deliverables/dsc-automation-audit.md` / `dsc-recruiting-playbook.md` | 27 / 26 stat tokens, ZERO URLs. |
| `deliverables/MyBPM-SEO-AEO-Optimization.md` | 73 stat tokens (search-volume/SEO), only 6 URLs; SEO decisions on partially-sourced data. |
| `_archive/2026-07-28-org-sweep/teardown-kajabi/state.yaml` *(also HIGH above for the dossier)* | — |
| `.tmp/copy-engine/sfv-first-time-homebuyers/ground-dossier.md` | Header `rqg_strict=fail`; body asserts "grounded=True"; Gemini+Perplexity both timed out → DEGRADED; VOC bank polluted with off-topic PDFs. |
| `.tmp/copy-engine/_coldstart-sfv.log` | Documents the degraded cascade (Gemini 900s timeout, Perplexity HTTPError) — "manifold will build on [MODELED] language. Flag before shipping." |
| `_archive/2026-07-28-org-sweep/_ck2free/state.yaml` | anchor-001 = "FREE-DIRECTIVE" (un-grounded); referenced dossier **does not exist on disk** (orphaned anchor). |
| `_archive/2026-07-28-org-sweep/sfv-first-time-homebuyers/state.yaml` | DEGRADED grounding never linked back — orphaned from its (failed) provenance; empty deliverables/research dirs. |
| `_archive/2026-07-28-org-sweep/teardown-skool/state.yaml` | Initialized 2026-05-31, `anchors: []`, no Phase 0 GROUND recorded. |
| `_active/coach-cooz/02-source-docs/avatar-swarm-v2/01–04_*_v2.md` | v2 rebuilds; supersede the polluted avatar but still ZERO URLs (grounding by reference, not inline link); drive the $1,997 Ignition Offer. |
| `_active/parallax-icp-offer/icp/avatar-01/02/03 + language-map.md + pain-ladder.md` | Offer-defining avatars; provenance is Recall-card-ID-only (or none); language-map (139 quotes) says "sourced from Recall" but no card-level attribution; instructs verbatim use in sales copy. |
| `_active/farrice-brand/offers/avatar-copy-engine-offer.md` | Markets the moat as "grounded in real social listening (Gemini Deep Research)" — credibility claim only as sound as the upstream foundation (now fixed going forward). |
| `products/promptbase/03-competitive-teardown.md` | **Root cause.** Prompt directs the model to generate size estimates / unit economics / break-even from inference (temp:0, no retrieval) and never instructs it to cite or label estimates. |
| `research_outputs/2026-04-25-substack-notes-craft-perplexity.md` | False-PASS signature: "Gemini DR Max exceeded 900s," dangling async ID, promised supplement never arrived, 0 URLs. |
| `research_outputs/substack-brandjack-trends-april-2026.md` | Specific real-world claims (Anthropic "April 2," "171 emotion concepts," Amodei NYT quote) with 0 URLs; feeds Parallax angles. |
| `research_outputs/ai-brain-build-validation/red_team_validation.md` | Competitor pricing (Coachvox "$99/mo + $3,000," Personify "$399–$1,099/mo") as fact, 0 URLs. |

### LOW — flagged for completeness (demonstrative / deprecated / superseded)

`deliverables/coach-cooz-final/.../05_identity_persuasion.md`, `.../06_emotional_outcome_sales.md`, `.../08_brand_magnetism.md` (unlinked Reddit verbatim, lower decision weight); `deliverables/revenue-sprint/linkedin-content.md` (sample copy referencing "same deep research process"); `products/promptbase/test-outputs/04-brand-voice-TEST-OUTPUT.md` + `05-course-builder-TEST-OUTPUT.md` (unsourced stats / a health claim woven into sample copy a buyer may reuse verbatim); `research_outputs/human_values_collective_profile.md` (~18 URLs, partial); `_active/coach-cooz/_DEPRECATED/.../07_market_intelligence.md` (deprecated, corrected downstream); `_active/farrice-brand/content/NOTES_TRAILER_PLAYBOOK.md` + `PARALLAX_SETUP_RUNBOOK.md` (cite pre-2026-06-01 Gemini DR, possibly never-completed async); `_active/andrea-dj/research/01-market-research.md` (title-only sources, **superseded** by the rigorously verified `data-brief.md`); `_active/javier-human-values/research/grounding-document.md` (stats as fact, no URLs, internal strategy — verify before external use).

---

## Re-Ground Worklist (prioritized)

1. **Stop the bleeding on money/health/real-person/sellable HIGHs.**
   - Pull the guarantee + "exact formula" language from `Kens_Fasting_Digital_Product/landing_page_copy.md` **now** (medical-claim liability).
   - Add an "AI estimates — verify before deciding" disclaimer to `products/promptbase/03-competitive-teardown.md` (the root cause) before any further sale; it propagates to every buyer.
   - Re-verify every real-person attribution in `Human_Values_Collective_Delivery/.../grounding-document.md` against live sources before client delivery.

2. **Re-run the three prediction-market briefings + the arb dossier through `research.py --depth deep`** — attach URLs to each financial stat or pull the claim. These drive capital deployment.

3. **Re-ground the avatar/VOC backlog via `/avatar-machine` (strict gate):** the 26 `ai_authority_architect_agents/` dossiers + synthesis, `unbottlenecked_blueprint/06`, the SAMPLE-REPORT ICP template, and the coach-cooz v2 swarm. Delete the `.resolved` / `.resolved.0` duplicates first.

4. **Reconcile the false-PASS status files.** Fix `.tmp/copy-engine/ground-status.json` so `status` reflects `rqg_strict_pass`; re-run SFV, Kajabi, and Skool cold-starts when Gemini/Perplexity are available; repair the orphaned `_ck2free` anchor (missing dossier) and the unlinked `sfv-first-time-homebuyers` / `teardown-skool` anchors.

5. **Migrate the medium-risk bypassers to the engine** (one-line fix each in the table). Priority order: the **HIGH-risk skills first** (`market_intelligence` — remove the MOCKED SERP; `consumer-posture-research`, `business-intelligence-audit`, `bond-halbert-copywriting` — stop claiming "research-grounded" without a gate), then the direct-client workflows (`generate-brief`, `research-landscape`, `research-topic`, `grounding-pass`), then `parallel_swarm.py` synthesis through `research.py ingest` (`native_swarm`).

6. **Kill hardcoded "GROUNDED" labels.** In `mini-brief.md`, `diandra-growth-sprint.md`, `diandra-content-engine.md`, make the GROUNDED/Provenance label *conditional* on a real `research_quality_gate.py` pass — never a template constant.

7. **Re-verify before reuse** every MEDIUM file that feeds a live offer/positioning decision (coach-cooz market/pricing, parallax-icp-offer avatars + language-map, MyBPM SEO). Internal strategy docs can carry a "verify before external use" header instead of a full re-run.

---

## Executive Summary

1. **Was broken:** paid research could log cost + report PASS for empty calls, findings could persist with no source URL, and `[MODELED]` data read as fact — yielding confident-but-unverifiable dossiers, some from swarms that ran with zero grounding queries.
2. **Now fixed:** one unified engine (`research.py`) on a shared trust contract — cost logs only after content validates, a `Finding` can't exist without a `source_url`, and `[MODELED]` is hard-blocked under `--strict`; everything fails closed to $0 with an honest receipt.
3. **Residual risk A — bypassers:** ~30 workflows/skills still research outside the engine; most are well-gated, but four skills (`market_intelligence` with a MOCKED SERP, `consumer-posture-research`, `business-intelligence-audit`, `bond-halbert-copywriting`) claim "research-grounded" with no enforced source gate.
4. **Residual risk B — backlog:** a body of pre-2026-06-01 outputs is still on disk; most modeled data *was labeled*, so the danger is reuse — but several HIGH files drive real money/health/real-person/sellable decisions and need re-grounding or a verify-before-deciding caveat now.
5. **Next:** pull the medical guarantee + add the promptbase disclaimer today, re-run the money briefings and avatar backlog through the engine, reconcile the false-PASS status files, and migrate the HIGH-risk skills off raw-tools onto `research.py`.
