# Regression Investigation — 2026-07-06

**Trigger**: `.agent/evolution-paused.json` gates Phase-3 cross-pollination on investigating the 6 REGRESSION entries in `evolution_store/regression_audits/audit_20260706_081423.json` (the cascade audit, `cascade_audits/audit_20260706_081438.json`, is clean/unrelated — 0 downstream regressions, `flag: false`).

## The 6 flagged entries
3 in `content` domain (LinkedIn post, Twitter thread, TikTok hook — all scored 6.45, deltas -0.55 to -1.05) and 3 in `research` domain (consumer persona, niche mapping, competitive analysis — all scored 6.33, deltas -0.67 to -1.17).

## Root cause

`execution/regression_suite.py` is **non-executing by design** — it never runs the golden-set task through a skill. `current_score` is a 30-day rolling average of `Quality Score` pulled from the Notion Performance Log, filtered by `skill_benchmark.detect_domain()`, a naive substring match over skill *names* (`DOMAIN_KEYWORDS['content'] = ['content','viral','tiktok',...]`, `['research'] = ['research','consumer','validation','behavioral','persona']`).

Queried the live Performance Log directly (last 30 days, same filter the audit uses):
- **content bucket, n=18**: 16 of 18 entries are `jen-santulan-listing-content` (real-estate listing copy, misclassified purely because "content" is a substring of the skill's name) scored 6.17, plus 2 `content-os-exemplars` entries at 7.25. Zero LinkedIn/Twitter/TikTok generalist skill ever ran in this window.
- **research bucket, n=2**: both entries are `source-command-deep-research` (a research *tool*, not a persona/market-intel skill), scored 6.08 and 5.67.

Re-ran `regression_suite.py audit --domain content` and `--domain research` live: reproduced 6.45 / 6.33 exactly — the numbers are real, but they measure the wrong thing.

`git log --follow` on the dominating skill: `skills/jen-santulan-listing-content` last touched 2026-05-22 (hookify activation) — **no content change** between then and the 07-02 finalize runs that produced the 6.17 scores. `source-command-deep-research` isn't a versioned skill in `skills/` at all.

Second, compounding factor: `evolution_store/ground_truth/rubric_v1.md` was created 2026-04-24 and calibrated 2026-04-25 (`051d4b6a`) and 2026-05-23 (`807ea9d7`, deliberately lowering `_EARNED_8_CAP` 7.5→7.25 "to break MARGINAL plateau"). The golden-set baseline audit (`audit_20260420_150223.json`) ran 2026-04-20 — **before the rubric existed** — scoring 8.2–8.75 across every domain. All 7 domains in today's audit cluster near 7.23–7.61 except content/research, matching the 2026-07-02 system-audit finding that composite scores flatten at 7.25 post-calibration. The golden-set `expected_min` thresholds (7.0–7.5) were never re-baselined against the calibrated rubric.

## Classification

| Domain (3 entries each) | Verdict | Evidence |
|---|---|---|
| content — LinkedIn/Twitter/TikTok tasks | MEASUREMENT_DRIFT | Proxy dominated by 1 misclassified real-estate skill (16/18 samples); no generalist content skill ran in-window; golden tasks never executed |
| research — persona/niche/competitor tasks | MEASUREMENT_DRIFT | Proxy = 2 samples from a misclassified research *tool*, not a persona/market-intel skill; golden tasks never executed |
| (all 6, secondary factor) | BASELINE_INFLATED | expected_min thresholds authored 2026-04-20, pre-dating rubric_v1 (04-24) and the 05-23 EARNED_8_CAP tightening; every other domain fell ~1.0-1.5 pts too, just short of the 0.5 REGRESSION cutoff |
| Any of the 6 | SKILL_DEGRADED | None found — the dominating skills' files are unchanged since well before the scoring window |

6/6 classify as MEASUREMENT_DRIFT (with BASELINE_INFLATED as compounding cause) — 0 SKILL_DEGRADED, 0 INCONCLUSIVE.

## Recommendation

**Lift the regression gate.** No skill content degraded. The audit's proxy methodology is broken on two independent axes (domain-misclassification by name substring, and pre-calibration thresholds) — it cannot currently distinguish real regression from measurement noise for content/research. Repair needed before this gate is trustworthy again: (1) fix `DOMAIN_KEYWORDS` collision (`content`/`research` substrings hitting unrelated skill names) or switch to skill-tag-based classification, (2) re-baseline `expected_min/target` against a fresh audit run under the calibrated rubric, (3) ideally make the suite execute the golden tasks rather than proxy from unrelated Performance Log rows.

Findings file: `evolution_store/regression_audits/investigation_2026-07-06.md`
