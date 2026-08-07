# E2 — Skill Census: Vintage-Stratified Embodiment Map
*2026-07-02 · Elevation Track · deterministic classifier (`execution/skill_census.py`) · calibration 12/13 against E1 ground truth + blind Opus validation · data: `../E2-census.json`*

## Verdict

324 skills graded mechanically in seconds. E1's vintage hypothesis is confirmed at census scale: **81% of the 2026-01 bulk stratum is flagged** (hybrid/hollow/no-genius) versus ~37% of mid-period and **~6% of the 2026-07 harvest**. The factory has been *improving on its own* — the harvest-era extractions are overwhelmingly sound. The debt is concentrated, old, and now enumerated. Most consequential single finding: two of the three most-used skills in the system are flagged.

## Distribution (grade × vintage stratum)

| Stratum | n | heartbeat | solid | hybrid-flag | hollow-flag | no-genius | thin | % flagged |
|---|---|---|---|---|---|---|---|---|
| bulk-2026-01 | 97 | 2 | 16 | 37 | 17 | 24 | 1 | **81%** |
| mid-period | 157 | 4 | 95 | 43 | 10 | 5 | 0 | 37% |
| harvest-2026-07 | 70 | 3 | 63 | 1 | 3 | 0 | 0 | 6% |
| **Total** | **324** | **9** | **174** | **81** | **30** | **29** | **1** | **43%** |

Grade meanings: **heartbeat-candidate** = full taste machinery (anti-patterns + recognition/rubric + dense verbatim anchoring) · **solid** = passes entity-density (source-grounded) but machinery incomplete · **hybrid-flag** = mid entity-gaps plus template-stamp evidence (dangling §-refs / uninstantiated criteria) · **hollow-flag** = ≥45% of genius sections carry zero substantive entities (no source-ledger exemption) · **no-genius** = embodiment unmeasurable, structural gap.

## The high-stakes list (flagged × actually used)

| Usage | Skill | Grade | Stratum |
|---|---|---|---|
| 19 | luke-iha-copy-blocks (**Production Core**) | hybrid-flag | mid |
| 10 | lara-acosta-linkedin-mastery | hollow-flag | bulk-01 |
| 6 | futurepedia-prompt-engineering | hybrid-flag | bulk-01 |
| 6 | oren-operational-systems | hybrid-flag | mid |
| 4 | creative-direction | hollow-flag | mid |
| 4 | fresh-voice-system · luke-iha-vsl-leads | hybrid-flag | mid |

**The Lara microcosm**: `lara-acosta-linkedin-mastery` (bulk-01, hollow-flag, zeroent 0.467) is the most-used of the three Lara skills (10 traces) while the better-graded `content-system` (solid) and `linkedin-growth` sit at 0-1 uses. If E3 confirms the flag, the system routes daily LinkedIn work through the weakest Lara — the founding-failure fix may live in writers-room/sovereign voice rules rather than in this skill file. Retrofit-or-reroute decision rides on the bake-off.

**The 9 heartbeat-candidates** (the roster the E4 standard generalizes from): stanton, hawley, eric-roth, ward-farnsworth, lulu-cheng-meservey, oren-taste-development, bill-browder, paul-harding, susan-orlean. Note: 3 are 2026-07 harvest — the recent factory occasionally produces full heartbeat unprompted.

## Classifier provenance (trust chain)

- Implements the 7 mechanical heuristics from `../E1-factory-audit.md` plus two discovered during validation: **assembly-artifact markers** (leaked LLM meta-text like "This response will provide the requested sections…" — found verbatim at bond-halbert genius.md:205 — and self-labeled "(Reconstructed" exemplars = fabrication evidence, instant flag) and a **provenance ladder** (timestamp source-ledger fully exempts; ≥2 named-source markers downgrade hollow→review).
- **Calibration 12/13** against ground truth (7 E1 labels + 6 blind Opus verdicts) after three honest iterations: proper-noun bigrams removed (template labels like "Success Metric" masked Enfroy's hollow core), numbering stripped ("Pattern 3" is not evidence), plural-blind provenance regex fixed (missed "transcripts").
- Known limits, documented not hidden: (1) reference-genus skills (encyclopedias like creative-direction — the 1/13 miss) over-flag because embodiment metrics assume a persona; (2) fabricated-but-numeric text can evade density checks unless artifact markers catch it — **mechanical grades are screening signals for review, not verdicts; only blind-pass comparison convicts.** File count deliberately ignored (E1: anti-signal).

## Blind spot-validation (independent Opus grader, labels withheld)

| Skill | Blind verdict | Script grade | Agreement |
|---|---|---|---|
| oren-operational-systems | HYBRID | hybrid-flag | ✓ exact |
| lulu-cheng-meservey | HEARTBEAT | heartbeat-candidate | ✓ exact |
| bond-halbert-copywriting | HOLLOW (fabricated exemplars, LLM leak) | hollow-flag | ✓ exact (after artifact markers) |
| craig-clemens-copywriting | HEARTBEAT (in 5-transcript addendum) | hybrid-flag | ~ safe (review, not conviction) |
| kallaway-illusion-of-novelty | HEARTBEAT | solid | ~ safe (under-grade, conservative) |
| creative-direction | SOLID (reference encyclopedia) | hollow-flag | ✗ known genus limit |

Validator's independent structural find: Bond + Oren workflows both invoke a "genius.md § Decision Framework" that exists in neither genius.md — the E1 dangling-ref signature, confirmed blind.

## E3 bake-off sample (proposed, 5 skills)

| Slot | Skill | Why |
|---|---|---|
| Bulk expected-fail | **lara-acosta-linkedin-mastery** | hollow-flag × 10 uses × founding-failure history; settles retrofit-vs-reroute |
| Enrichment-hybrid | **luke-iha-copy-blocks** | hybrid-flag × 19 uses × Production Core — highest-stakes file in the flagged set |
| Harvest expected-pass | **alex-hormozi-business** | 2026-07 harvest, solid; huge public corpus for blind comparison |
| Heartbeat control | **andrew-stanton-audience-engineering** | the E1 natural experiment; published talks/scripts to compare |
| Top daily driver | **alex-suzuki-digital-product-revenue-os** | usage 19, solid, mid-period; validates that "solid" means ship-grade |

Each: generate 3 outputs on tasks the expert has real published work for → blind packet → Farrice rates. 15 ratings ≈ the eval-set calibration threshold (kills the 7.25 flattening) while validating the census in the same 30 minutes.

## Next (E4 preview)
Retrofit priority = flagged × usage (the table above, top-down), then the bulk-01 stratum in batches; the 29 no-genius skills need genius.md builds or archival triage. Factory patches per E1: extract-forge P7.4 blind-pass, mes-3.0-validate Check 3.5, kill hardcoded finalize scores.
