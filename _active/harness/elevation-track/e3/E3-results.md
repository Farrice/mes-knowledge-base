# E3 Results — The Blind Bake-Off Reveal
*2026-07-02 · Farrice's 15 blind ratings vs sealed key · scored data: `E3-scored-results.json` · eval entries EVAL-014→028*

## Headline

**The arbitrage claim survives its first contact with ground truth.** Farrice identified the real expert in only **5 of 15 comparisons (33% — below coin-flip)** and preferred the skill-generated piece **8-6-1 over the real expert's published work**. Four of five skills blind-pass. The only voice that beat the machine, all three times, was Andrew Stanton's.

## Per-skill verdicts

| Skill | Census grade | Detected | Preference (gen/real/tie) | **Blind-pass** |
|---|---|---|---|---|
| lara-acosta-linkedin-mastery | hollow-flag | 2/3 | 2/1/0 | **PASS** — fooled once, generated preferred twice |
| luke-iha-copy-blocks | hybrid-flag | 0/3 | 2/1/0 | **PASS** — called real Luke "disjointed," generated "feels more like Luke" |
| alex-hormozi-business | solid | 0/3 | 2/0/1 | **PASS** — called the real "10 Truths" post "too polished and try hard" |
| andrew-stanton-audience-engineering | heartbeat-candidate | 3/3 | 1/2/0 | **FAIL** — spotted the real voice every time |
| alex-suzuki-digital-product-revenue-os | solid | 0/3 | 1/2/0 | PASS (marginal) — indistinguishable, but real preferred 2/3 |

## What the results actually mean

**1. Luke is the crown-jewel proof of arbitrage.** He is obscure enough that model training data can't be doing the work — yet a hybrid-flagged skill file produced copy Farrice both couldn't distinguish AND preferred, while judging real Luke "disjointed." The block-grammar workflows carry genuine replication power. For lesser-known experts, the skills themselves are the asset.

**2. Census flags measure the file, not the output.** The hollow-flagged Lara passed; the heartbeat control failed detection. This confirms E1/E2's own caution — mechanical grades are maintainability/screening signals; only blind-pass convicts. Reframe: E2 flags = *retrofit priority for durability and model-independence*, not output-quality verdicts. (Caveat: for famous voices like Lara/Hormozi, training-data bleed inflates pass rates — the model partly knows their styles. Luke controls for this; Stanton cuts the other way.)

**3. The Stanton FAIL carries the E4 gold.** Farrice's notes on every correct detection say the same thing: the real pieces were "conversational, human, more rhythm"; the generated were "teed-up, polished, overexplaining, try-hard." He even misjudged real Hormozi as AI *because it was too polished*. **Polish is the tell.** The E4 standard must encode anti-overpolish: preserve spoken texture, roughness, and rhythm variance; kill the instinct to tidy. (Methodology note: Stanton's real pieces were spoken TED transcript vs everyone else's written artifacts — modality mismatch made his real voice easier to spot and more charming; the finding directs, not convicts.)

**4. The "7.25 flattening" was a misdiagnosis — the guardrail is correct and stays.** Traced to `taste_signature.py` Rule 2 (8-must-be-earned): any dim ≥8 without a named rubric anchor caps at 7.25, below the 7.5 PASS floor — Farrice's own bimodal discipline, working as designed. The eval set was already 12/13 human-calibrated and load-bearing (the E2-era claim of "0 calibrated" was wrong). The real bug is upstream: extraction workflows hardcode `--intent 8 --expert-score 8` with no anchors (E1 finding, stands), and finalizes routinely skip anchor-naming. **E4 fix: anchor-named scores derived from evidence, never templated scores. Do NOT remove the guardrail.**

## Decisions settled

- **lara-acosta-linkedin-mastery**: NO reroute needed — output passes. Census hollow-flag reclassified as *maintainability debt* (file has zero verbatim voice anchors; works today largely via model competence + framework). Light retrofit when touched: add voice anchors + source-ledger.
- **luke-iha-copy-blocks**: KEEP as Production Core with confidence. Cheap fix only: repair dangling genius.md §-references.
- **alex-suzuki**: passes blind, but Farrice preferred the real 2/3 and flagged the generated voice as "more polite, not wider appeal" — retrofit target: raise the voice's edge. (Separate standing concern: persona is an alias with unverifiable claims; compliance gate stays.)
- **stanton**: the skill is NOT broken (deepest file in the system; generated still preferred once) — the gap is voice *texture*, the E4 anti-polish rule's first test case.
- **Eval set**: 28 entries, 27 human-calibrated (threshold 22) — blind-pass entries EVAL-014→028 now in `eval_set_v1.jsonl`.

## E4 mandate (from evidence, ready to execute)
1. Blind-pass eval step into `extract-forge.md` P7.4 + `mes-3.0-validate.md` Check 3.5 (per E1).
2. Kill hardcoded finalize scores in `extract.md:100-106` / extract-forge equivalents → scores must be anchor-named.
3. **New: anti-overpolish rule** in the embodiment standard — encode "polish is the tell": preserve conversational texture, rhythm variance, imperfection; ban teed-up openers and overexplanation. Source: Farrice's blind notes, 5/5 consistent.
4. Embodiment checklist (E1) into the forge gate; census (`skill_census.py`) re-run after each harvest wave.
