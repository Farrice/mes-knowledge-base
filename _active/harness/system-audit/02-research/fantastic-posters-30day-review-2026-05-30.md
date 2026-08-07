# Fantastic Posters 30-Day Usage Review
**Period:** 2026-04-30 (install) → 2026-05-30 | **Generated:** 2026-05-30

---

## 1. Executive Summary

28 calls / $2.008 spent across 3 active days (Apr 30 – May 2); silent for the 28 days since. Poster ($1.672, 83%) vastly outweighs video ($0.336 Kling, 17%); Seedance, edit, and rembg have zero calls. jen-listings and deliverables use cases are fully orphaned; parallax has a single exploratory call. Recommended action: **tighten** — lower the daily block and per-call ceilings to match actual usage patterns, surface kling more prominently in the mybpm workflow, and flag seedance for archival if still unused in the next 30-day cycle.

---

## 2. Spend Breakdown

| Use Case | Poster | Edit | Kling | Seedance | Total | Status |
|---|---|---|---|---|---|---|
| mybpm | $0.011 | $0 | $0.336 | $0 | **$0.347** | Active (video bridge tested) |
| parallax | $0.011 | $0 | $0 | $0 | **$0.011** | Underused (1 call, install day) |
| jen-listings | $0 | $0 | $0 | $0 | **$0.000** | ORPHANED |
| deliverables | $0 | $0 | $0 | $0 | **$0.000** | ORPHANED |
| uncategorized¹ | $1.650 | $0 | $0 | $0 | **$1.650** | Test/dev batch |
| **TOTAL** | **$1.672** | **$0** | **$0.336** | **$0** | **$2.008** | |

> ¹ 25 poster calls with empty `brief` fields logged 2026-05-01 and 2026-05-02 — consistent with a development/style-exploration batch session. No named use case associations possible.

---

## 3. Per-Mode Analysis

**poster** (27 calls, $1.672, 83.3% of total spend): The only mode seeing meaningful use. All 28 days of activity was concentrated in the first 3 days post-install. Largest single call cost $0.17 (high quality), representing 17% of the $1.00 per-call ceiling — ceiling is substantially over-provisioned relative to actual call costs. Peak daily poster spend was $0.99 on 2026-05-01, representing just 16.5% of the $6.00 daily cap. 5 of 27 calls were high-quality ($0.17 each); 20 were medium ($0.04); 2 were low ($0.011). Only 2 of 27 calls had named briefs (mybpm + parallax); the remaining 25 are an unlabeled batch, strongly suggesting a systematic testing or style-exploration session rather than production use.

**kling** (1 call, $0.336, 16.7% of total spend): A single smoke test on install day (2026-04-30, 21:07 UTC): "animate vaporwave-synth poster" at 3s duration / audio off. Cost $0.336, which is 16.8% of the $2.00 per-call ceiling. The smoke test confirms the Kling pipeline works. No production Kling calls have been made since. The video-bridge pattern (poster → Kling animation) is validated but dormant.

**edit, rembg** (0 calls each): No image-to-image edits or background removals logged in 30 days. Edit mode was not needed in any logged session; rembg's chained transparency pipeline has never been exercised.

**seedance-480p, seedance-720p** (0 calls each): The Seedance 2.0 video extension has zero usage in 30 days. No brief ever referenced animate, trailer, or reveal via Seedance. The wrapper (`execution/fal_video_seedance.py`) is installed but untriggered.

**seedance-1080p**: Hard-blocked, as expected. No log entries or error patterns referencing this mode.

---

## 4. Limit Calibration Recommendations

### Poster modes (poster, edit)
- **Largest poster call**: $0.17 = **17% of $1.00 ceiling** — far below the 90% raise threshold. No raise warranted.
- **Peak daily poster spend**: $0.99 = **16.5% of $6.00 daily cap** — well below 50%.  
  Recommendation: lower `per_call_block_usd_by_mode.poster` from $1.00 → **$0.25**. This provides clear headroom above the actual maximum ($0.17 for a single high-quality image) while blocking runaway `--n=10 --quality=high` mistakes more tightly ($1.70 → blocked at $0.25 before the first call).  
  Apply same tightening to `edit` ($1.00 → **$0.25**) for consistency; edit mode is unused but benefits from a tighter ceiling as a safeguard.

### Video modes (kling, seedance-*)
- **Kling**: 1 call at $0.336, ceiling $2.00 = 16.8% utilization. Not ≥ 90%. No ceiling change needed.
- **Seedance**: 0 calls across all variants. Neither the "0 kling + 5+ seedance" nor the "0 seedance + 5+ kling" rule triggers (kling=1). Ceilings unchanged, but the zero-use pattern warrants a 30-day re-evaluation flag (see Section 7).

### Global caps
- **Per-day block**: Peak was $0.99 ≤ 50% of $6.00 cap. Apply rule: new cap = peak × 1.5 = **$1.50**. Lower `per_day_warn_usd` from $3.00 → **$0.75** proportionally.
- **Per-cycle block**: At $2.008 spent vs $15.00 ceiling (13.4% utilization), the cycle cap is appropriate headroom and should be left as-is.
- **No 1080p attempts** in 30 days. No action needed.
- **No consecutive failure halts** — `consecutive_failures` was 0 at review time. No config issue to investigate.

---

## 5. Use Case Status

| Use Case | Calls | Spend | Status | Recommendation |
|---|---|---|---|---|
| mybpm | 3 (2P+1K) | $0.347 | **Active** | Add kling video step to mybpm workflow; the smoke test proves the pipeline — it just needs a prod trigger |
| parallax | 1 | $0.011 | **Underused** | 1 exploratory call on install day. No newsletter covers since. Add a poster step to `/parallax` workflow (Phase 2 → cover gen) |
| jen-listings | 0 | $0.000 | **ORPHANED** | (a) If Jen is an active client: wire `--batch` call into listing workflow. (b) If Jen is inactive/prospective: demote to "dormant" in use-case table |
| deliverables | 0 | $0.000 | **ORPHANED** | The `strategy brief / deliverable covers` use case was never triggered. (a) Add cover-gen step to deliverables output workflow, or (b) demote — covers may be lower-priority than initially assumed |

---

## 6. Style Usage (Poster Mode)

Only 2 of the 38 registered styles appear in the log. The remaining 25 calls used blank style fields, consistent with a testing batch (likely iterating quality tiers, not styles).

| Style | Calls | Context |
|---|---|---|
| `vaporwave-synth` | 1 | mybpm install-day test |
| `editorial-fashion` | 1 | parallax install-day test |
| *(empty/unlabeled)* | 25 | Dev/test batch — quality tier iteration |
| *(all other styles)* | 0 | Unused |

**Signal**: 36 of 38 styles have never been exercised in production. Style exploration has not moved beyond the initial test pair.

---

## 7. Video Usage Status

| Metric | Value |
|---|---|
| Kling calls | 1 (smoke test, 2026-04-30) |
| Seedance calls | 0 (all variants) |
| Audio mode | `off` (only call) |
| Bridge pattern used | Yes — poster → Kling (1 instance) |
| Days since last video call | 28 |

**Assessment**: The video extension is functional (smoke test succeeded, download failure was a local path issue not a generation failure per the log note) but has not been used in production. Kling has a single validated proof-of-concept. Seedance has zero calls and no identified use case in 30 days.

**Recommendation**: Keep Kling alive and surface the `poster → kling animate` bridge more explicitly in the mybpm workflow. Flag Seedance for archival if still at 0 calls at the 60-day review (2026-06-30). Do NOT archive Kling — the smoke test establishes a viable bridge that just needs integration.

---

## 8. Recommended Action

**`tighten`**

Reasoning: The install was active for exactly 3 days (primarily a test batch), then silent for 28 days. Current limits are calibrated for $6/day active use that hasn't materialized. Tightening the daily block to $1.50 and per-call poster ceiling to $0.25 matches actual usage patterns while preserving full video capacity for the one use case (kling/mybpm) that has been validated.

Secondary action: **`integrate-video-harder`** for kling specifically — the bridge works, it's just not wired into any production flow.

---

## 9. Anomalies

**None significant.**

- 0 failures, 0 halts, 0 rate-limit triggers across 28 calls
- 0 `seedance-1080p` attempts (hard block is working)
- The 2026-04-30 Kling call shows `output_path: "(download failed locally; Fal generation succeeded — see fix in fal_video_kling.py download_video)"` — the video was generated and billed correctly; the local download path had a bug. This is a one-time resolved issue per the note, not a recurring concern.
- 25 of 27 poster calls have empty `brief` fields — this is a data quality gap, not a spend anomaly. All calls succeeded. The missing briefs make it impossible to retroactively assign these to a use case.

---

## Appendix: Raw Totals

```
lifetime_calls:              28
lifetime_spent_usd:          $2.008
current_cycle_spent_usd:     $2.008
wallet_balance_estimate:     $17.99
consecutive_failures:        0
halt_reason:                 null

Mode breakdown (lifetime):
  poster:       $1.6720  (27 calls)
  edit:         $0.0000  (0 calls)
  rembg:        $0.0000  (0 calls)
  kling:        $0.3360  (1 call)
  seedance:     $0.0000  (0 calls)

Active days (of 30):         3
Last active:                 2026-05-02
Days silent:                 28
```

*Full report path: `_active/harness/system-audit/02-research/fantastic-posters-30day-review-2026-05-30.md`*
