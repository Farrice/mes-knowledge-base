# Ground-Truth Calibration — Review Protocol (Farrice)

**Created**: 2026-07-17 (Frontier Elevation Program, Wave 1 seeder)
**Goal**: Turn calibration from an *authoring* job into a *review* job. Everything below is pre-scored against `rubric_v1.md` anchors. Your job is to **agree or adjust**, not to write from scratch.

**Inputs**:
- `seed_candidates_2026-07-17.jsonl` — 30 pre-scored candidates (this file's subject).
- `eval_set_v1.jsonl` — the live calibration set (44 entries; **do not bulk-edit**).
- `rubric_v1.md` — the anchors every score cites.

---

## READ THIS FIRST — the load-bearing math changed (the rubric text is stale)

`rubric_v1.md` still says the rubric arms "once at least 15 of the 30 eval tasks have human-validated scores." **That number is obsolete.** The gate moved to a proportional rule on 2026-05-03 (`execution/eval_harness.py::calibration_status`):

> **load-bearing = `human_calibrated ≥ max(10, floor(0.8 × total_entries))`**

Current status (run `python3 -c "import sys;sys.path.insert(0,'execution');from eval_harness import calibration_status as s;print(s())"`):

| metric | value |
|---|---|
| total_entries | 44 |
| human_calibrated (`calibrated_by_human:true`) | 27 |
| **load_bearing_threshold** | **35** |
| rubric_load_bearing | **false** |
| pending review (already in eval_set) | 17 |

**Consequence you must know**: because the threshold is 80% of *total*, **appending an un-calibrated row RAISES the bar.** Promoting a fresh seed adds +1 to both numerator and denominator, so it only nets +0.2 toward the gap. **Ratifying an entry already in the set** (numerator +1, denominator unchanged) nets a full +1.0. This changes the fastest path — see below.

---

## FASTEST PATH TO ARM THE JUDGE (do this first, ~15 min)

You are **8 calibrations short** (35 − 27). The 17 pending entries already in `eval_set_v1.jsonl` are `EVAL-011` (a skipped placeholder) and `EVAL-029`–`EVAL-044` — **your own model/self-judged blind-pass records** (Jenny Hoyos, Oren, Priestley, Godin, Joey Cinema, etc.). They need only your *felt* AGREE.

1. Open `eval_set_v1.jsonl`, find each entry with `"calibrated_by_human": false`.
2. For each: if you agree with the recorded blind-pass verdict, flip `"calibrated_by_human": false` → `true` and add `"human_calibration_notes": "<your one-line felt verdict>"`. If you disagree, adjust the scores/verdict first, then flip.
3. **Ratify any 8 of the 17** → 27+8 = 35 ≥ 35 → **rubric is load-bearing.** Ratify all 17 → 44/44, and it stays armed permanently (see promotion note).

Re-run the status command after; `rubric_load_bearing` should read `true`.

> The 30 seed candidates below are **not** the fastest arm-the-judge lever — they are how you make the calibrated set *deep and honest*: they add the mid-band, the inflation-corrections, and the non-Content types (Research / System / Analysis / Client Work) the current set is missing. Do the ratify pass first; then work the seed batches to raise calibration *quality*.

---

## THE THREE REVIEW BATCHES (~20 min each)

`seed_candidates_2026-07-17.jsonl` is split into `batch: 1|2|3`, **10 entries each, deliberately mixed** across the weak / mid / strong spectrum and across task types — so each sitting calibrates the full range of your taste, not one band.

Every candidate carries:
- `proposed_scores` — my 1-10 on intent / expert / adversarial / factual + composite.
- `anchor_names` — the **named rubric anchor** each score matches (rubric discipline: an 8+ must name its anchor).
- `expected_verdict` — PASS / MARGINAL / FAIL under the bimodal filter.
- `rationale` — one line on why.

Batch spread (honest, non-inflated):

| batch | FAIL | MARGINAL | PASS | types |
|---|---|---|---|---|
| 1 | 3 | 3 | 4 | Research, Extraction, Content, System |
| 2 | 3 | 4 | 3 | Content, Extraction, System, Strategy, Client Work |
| 3 | 5 | 1 | 4 | Content, Research, System, Analysis, Strategy |

**Per entry, do ONE of:**
- **AGREE** — scores land right. (No edit needed to the seed file; you'll promote it — see next section.)
- **ADJUST** — edit `proposed_scores` and `anchor_names` **in place** in `seed_candidates_2026-07-17.jsonl`, then promote. Follow your calibration signature: bimodal, narrow marginal band, −1/dim on real failures, when in doubt fail harder.

**What to watch for (these are the calibration-bearing cases):**
- `SEED-011`, `SEED-012` — the **inflation archetypes**: the trace self-scored **9.67 / 9.33** (10/10 on two dims). I dropped them ~2.3 pts to 7.3 MARGINAL because the blind-pass was *model*-judged, A-tier still pending your felt verdict. **If you'd ship them as A-tier, adjust up; if the drop is right, agree.** This single call is what teaches the judge to stop inflating.
- `SEED-001`–`SEED-010` — real prose-gate FAILs pulled from `content-finish-log.jsonl`. Banned-move density → Expert/Adversarial Anchor 3 (per EVAL-009 precedent). Confirm slop deserves the same FAIL as expert-not-embodied.
- `SEED-021`, `SEED-022`, `SEED-025` — genuine PASS work with hard evidence (prose gate CLEAN, verified git receipts, cross-harness runtime verification). These are the "8 is earned, anchor named" exemplars.

---

## HOW TO PROMOTE AN AGREED ENTRY INTO `eval_set_v1.jsonl`

Promotion strips the seed-only fields, sets `calibrated_by_human: true`, and appends the row to the live set. **Promote one entry at a time as you agree** — never bulk-append the whole seed file (un-calibrated rows raise the threshold).

**Exact one-liner** (replace `SEED-011` with the id you're promoting; add your felt note):

```bash
cd "/Users/farricecain/Google Antigravity" && ID=SEED-011 NOTE="agree — model over-rated; 7.3 marginal is right" python3 - <<'PY'
import json, os
ID, NOTE = os.environ["ID"], os.environ["NOTE"]
seeds = {json.loads(l)["id"]: json.loads(l) for l in open("evolution_store/ground_truth/seed_candidates_2026-07-17.jsonl")}
s = seeds[ID]
row = {
    "id": s["id"], "source": s["source"], "task_type": s["task_type"], "domain": s["domain"],
    "user_request": s["user_request"], "produced_by": s["produced_by"],
    "expected_intent_alignment": s["proposed_scores"]["intent_alignment"],
    "expected_expert_standard": s["proposed_scores"]["expert_standard"],
    "expected_adversarial_resilience": s["proposed_scores"]["adversarial_resilience"],
    "expected_factual_grounding": s["proposed_scores"]["factual_grounding"],
    "expected_composite": s["proposed_scores"]["composite"],
    "expected_verdict": s["expected_verdict"],
    "rubric_anchors_matched": s["anchor_names"],
    "lessons": s["rationale"],
    "calibrated_by_human": True,               # <-- the promotion act (YOUR act, never the seeder's)
    "human_calibration_notes": NOTE,
}
with open("evolution_store/ground_truth/eval_set_v1.jsonl", "a") as f:
    f.write(json.dumps(row, ensure_ascii=False) + "\n")
print("promoted", ID, "->", row["expected_verdict"], row["expected_composite"])
PY
```

If you **adjusted** first, edit the seed row in place before running the one-liner — it reads the (edited) `proposed_scores`.

After a promotion pass, re-check:

```bash
cd "/Users/farricecain/Google Antigravity" && python3 -c "import sys;sys.path.insert(0,'execution');from eval_harness import calibration_status as s;import json;print(json.dumps(s(),indent=1))"
```

`rubric_load_bearing: true` means the calibrated judge is armed — finalize scores are now checked against *your* anchored ground truth, not the model's self-report.

---

## GUARDRAILS

- **Only you promote.** The seeder marked every candidate `human_calibrated: false` and touched nothing in `eval_set_v1.jsonl`. Setting `calibrated_by_human: true` is exclusively your act.
- **One at a time.** Promote as you agree; don't bulk-append the seed file (proportional threshold penalises un-calibrated bulk rows).
- **Keep the spread honest.** If your promotions end up 90% PASS, the inflation is back. The seed set is intentionally ~⅓ FAIL / ¼ MARGINAL / ⅓ PASS — real work looks like that.
- **The rubric text lags the code.** When in doubt about the threshold, trust `eval_harness.calibration_status()`, not the "15" in `rubric_v1.md` (worth a one-line fix to that file when you next touch it).
