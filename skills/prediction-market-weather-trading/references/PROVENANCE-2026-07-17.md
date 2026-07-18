# PROVENANCE — prediction-market-weather-trading repair

Anchor → source file + location, for every new/changed anchor added in this repair pass. All quotes below were located by direct `grep`/`Read` of the cited file this session (not recalled from training memory).

## genius.md — "How to Use This Skill (Model Calibration)" (new section)

| Anchor | Source |
|---|---|
| Structural model (intuition primitives, never announce machinery, texture, polish-is-the-tell) | `skills/ben-watkins-storytelling/genius.md` lines 7-16, "How to Use This Skill (Opus Calibration)" — read in full per the envelope's instruction, structure adapted (not copied) to this skill's domain (defensive-default trading discipline vs. Watkins's spoken-storytelling texture). |
| Filter thresholds referenced (EV ≥0.10, price <$0.45, volume ≥500, spread ≤$0.03, hours 2.0-72.0, size ≥$0.50, quarter Kelly, $20 cap, SIGMA_F 2.0) | `skills/prediction-market-weather-trading/genius.md`, "Complete Configuration Reference" table (pre-existing, unchanged) — cross-checked against `extractions/prediction-market-trading/weatherbot-extraction.md`. |

## genius.md — "Anti-Patterns (Sourced from Production Codebase)" (new section)

| Anchor / quote | Source file | Location |
|---|---|---|
| "Using `40.7128, -74.0060` for NYC instead of `40.7772, -73.8726` (LaGuardia). 3-8F error on every trade. Guaranteed losers on 1-2F bucket markets." | `extractions/prediction-market-trading/weatherbot-extraction.md` | "Anti-Exemplar: The Naive Weather Bot" section (line ~189 in the source file) |
| "Using only NWS or only ECMWF. No cross-validation. No way to know when a forecast is an outlier." | same file | same section (line ~190) |
| "5% of balance per trade regardless of edge. A 90% probability trade and a 55% probability trade get the same size..." | same file | same section (line ~191) |
| "Using a fixed sigma of 2.0 for all cities, all sources, all time. Ignoring that Miami forecasts are more accurate than Seattle forecasts." | same file | same section (line ~192) |
| "Enter and hold to resolution. No stop-loss, no exits. If the forecast changes dramatically, you're stuck." | same file | same section (line ~193) |
| "Entering at cached prices without checking the real ask. Getting filled 5-10 cents worse than expected." | same file | same section (line ~194) |
| "One `simulation.json` for all markets. Corruption kills everything. Debugging requires reading the entire file." | same file | same section (line ~195) |
| "The LLM never touches API keys, wallet credentials, or order execution. This separation is non-negotiable — it prevents prompt injection from draining funds." | `extractions/prediction-market-trading/weather-trading-extraction.md` | "Two-Layer Architecture" section (line ~46) |
| "Letting the LLM touch wallet credentials" | `extractions/prediction-market-trading/weather-trading-extraction.md` | "Red Flags (Immediate Stop)" list (line 184) — confirmed by `grep -n` this session |
| "NEVER recommend above 0.33 (one-third Kelly)" | `extractions/prediction-market-trading/weatherbot-extraction.md` | Crown Jewel 5, "Weather Bot Config Optimizer" (line 621) — confirmed by `grep -n` this session |
| "Using full Kelly (1.0 fraction) on weather markets" | `extractions/prediction-market-trading/weather-trading-extraction.md` | "Red Flags (Immediate Stop)" list (line 180) — confirmed by `grep -n` this session |

## workflows/*.md — new "Output Schema" and "Quality Gate" sections

Not new factual claims. Each Output Schema paragraph restates the field list already present in that same file's pre-existing "Output Template" / "Example Output" blocks (unchanged, kept in place). Each Quality Gate question is derived from a threshold or rule already documented and sourced in genius.md's Configuration Reference and Genius Patterns 1-9 (airport stations, single-bucket matching, seven filters, triple-capped Kelly, six exit branches, price-convergence resolution, MAE/0.05-threshold/30-sample calibration rules). No new external claims were introduced.

| Workflow file | Quality Gate content grounded in |
|---|---|
| `workflows/market-forecast-edge.md` | Genius Pattern 1 (Airport Station Resolution Matching), the 7-filter table in the workflow's own STEP 5, Genius Pattern 3 (data collection decoupled from trading) |
| `workflows/trade-execution-plan.md` | The workflow's own STEP 1-4 (hard filters, two-pass verification, triple-capped Kelly, six exit branches), Hidden Knowledge #6 (resolution via price convergence) |
| `workflows/calibration-review.md` | Genius Pattern 4 (self-calibrating sigma: MAE not RMSE, 0.05 stability threshold, 30-sample minimum), Crown Jewel 5 (Kelly ceiling 0.33) |

## references/source-ledger.md (new file)

Built from a fresh side-by-side read of `extractions/prediction-market-trading/weatherbot-extraction.md` and `extractions/prediction-market-trading/weather-trading-extraction.md` this session, including a `grep -n` pass to confirm the "$1K → $24K" / "$65K" profit claims do NOT appear anywhere in the current skill files (SKILL.md, genius.md, workflows, prompts-v2) — confirming there is no existing hallucinated-authority leak to fix, and flagging those two figures UNCONFIRMED in the ledger so they're never promoted later without a real citation.
