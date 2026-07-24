# Loop Inventory Audit — 2026-07-24

Evidence-based audit of every feedback/compounding loop wired into the repo. Method per loop: input signal → where learning lands → evidence it changed later behavior → verdict → repair. All timestamps checked live on 2026-07-24 ~15:00 local. Evidence = file mtimes, log tails, `launchctl list`, git log, tracker JSONs. No system files modified.

**Verdict key**: COMPOUNDING = signal captured AND demonstrably changes later behavior. OPEN = machinery exists and captures signal, but the closing half (consumption/decision/behavior change) doesn't fire. DEAD = no signal captured or no artifact exists.

## Verdict Table

| # | Loop | Verdict | One-line evidence |
|---|------|---------|-------------------|
| 1 | Solution recorder | **COMPOUNDING** | 51 cards, newest 2026-07-24; router hook injects "PRIOR SOLUTION EXISTS" (skill_router_hook.py:477); solutions hits in 31/64 memory-facade fires incl. today |
| 2 | Feedback ratchet | **COMPOUNDING** | performance-log.jsonl 99 records + 29 inbox, entries every day 07-15→07-24; scores feed phase2_queue (93 entries queued in July) |
| 3 | Learning router | **COMPOUNDING** | skill-weights.json non-uniform (0.5–1.67), rewritten 07-23 by daily orchestrator; find_skill.rank() applies weights at routing time |
| 4 | evolution_orchestrator auto | **COMPOUNDING** (one missed day) | orchestrator_state: daily 07-23, weekly 07-17, monthly 07-10 all ran; skill_audit regenerating (07-24 10:59); today's 07:00 daily missed |
| 5 | Steering loop | **OPEN** | 54 misses (`next-moves-missing`) logged 07-08→07-23; zero consumers of the miss log beyond byte-size in health_metrics.py |
| 6 | Memory pipeline | **COMPOUNDING to distill / OPEN at review** | harvest ran 07-24 (+8 → 5447/5447 embedded, 100%); distill-weekly proposing rules; 9 flagged rules stuck `pending` in memory_review.py, oldest 07-19 |
| 7 | Wargame failure-maps | **DEAD** (as a compounding loop) | Zero wargame-run artifacts exist anywhere on disk; no execution-layer code reads failure-maps (grep empty) |
| 8 | Calibration / ground truth | **OPEN** | 66/68 human-calibrated (2 short of load-bearing); 19 auto-seeded pending Farrice review since 07-17; verdict_advisory: 2 of last 3 SHIPs missing precedent |
| 9 | Revenue tracker outer loop | **OPEN** | 177 deliverables logged, only 4 have revenue ($4,400); pipeline drained 101→16 on 07-21 but /weekly-closeout has 0 finalize records ever; outcome-chase launchd log never created |
| 10 | offer_gate / offer-redteam | **OPEN** | offer-gate-log.jsonl: exactly 2 entries, both 2026-07-21T14:08 (build day), both FLAG; never fired since — no trigger wires it to new offer work |
| 11 | Session ledger (observe mode) | **OPEN** | 685 would_block events since 06-14 (347 entries in last 7 days); no analyzer/reviewer; LEDGER_ENFORCE never flipped; routing-enforce trial expires TODAY with 4 log entries and its review ritual never ran |
| 12 | Skill-evolution Phase 2 | **OPEN** | Queue producer runs daily (130 queued, 93 in July); consumer ran ONCE — commit dcc8f69d7 2026-07-06 (alex-suzuki 6.22→7.22); 18 days idle since |

Adjacent infra findings (not on the ticket list): `com.antigravity.citation-integrity` last exit 1 (2 missing pointers); `com.antigravity.verify-fleet` last exit 1 — fleet at 52 pass / 30 fail / 4 skip of 86.

---

## Per-Loop Detail

### 1. Solution recorder — COMPOUNDING
- **(a) Input**: cracked problems → `/extract-approach` → `docs/solutions/*.md` cards.
- **(b) Lands**: 51 cards (2026-07-07 → 2026-07-24), `docs/solutions/index.md` maintained.
- **(c) Evidence of closure**: three independent resurfacing paths, all live: (1) `execution/skill_router_hook.py:477` injects `PRIOR SOLUTION EXISTS (from docs/solutions/ — read before re-solving)` per prompt, degradation-guarded (line 444); (2) `execution/memory_facade.py` has `solutions` as a first-class source (line 78, `_query_solutions` line 377) — `.agent/memory-facade-fires.jsonl` shows solutions results in 31 of 64 fires, including today's fire (solutions: 3); (3) cards are being created same-session as work (2026-07-24 Riley Brown card appears inside the same day's observe-log produced_paths). Citation-integrity job even treats a card (2026-07-13-divergent-branch-work-silently-lost) as canon in its error text — cards are load-bearing.
- **(d) Verdict**: COMPOUNDING.
- **(e) Repair (minor)**: router hook doesn't log *when* it injects a solution, so injection hit-rate is unmeasurable. One `json.dumps` append to `.agent/sessions/solution-injections.jsonl` in the injection branch of `skill_router_hook.py` makes this loop auditable. Zero context cost.

### 2. Feedback ratchet — COMPOUNDING
- **(a) Input**: chain_runner finalize / `log_performance.py` scores per deliverable.
- **(b) Lands**: `.agent/performance-log.jsonl` (99 records; +inbox 29, skipped 1). Days 07-15→07-24 all present (peak 30 on 07-19).
- **(c) Evidence of closure**: (1) scores mechanically feed `evolution_store/queue/phase2_queue.jsonl` (regression rule "2 scores <7.0 in 7d" — 93 entries queued in July, so the detector runs); (2) ratchet already changed system shape historically — E4/E5 sweep de-templated 45 hardcoded score blocks (documented in feedback-ratchet.md); (3) anchor discipline enforced in code (`taste_signature.py` Rule 2, 7.25 cap; `verdict_advisory.jsonl` records SHIP-without-precedent misses); (4) sub-agent truth measured (`sub_agent_misses.jsonl` updated 07-21).
- **(d) Verdict**: COMPOUNDING on the capture/detect side. Its downstream *fix* arm is Loop 12, which is open — see there.
- **(e) Repair**: none needed here; the weak link is the Phase-2 consumer (Loop 12).

### 3. Learning router — COMPOUNDING
- **(a) Input**: per-trace routing quality (cursor `.agent/routing-quality-cursor.json`, last_trace 20260721_203120) + finalize scores.
- **(b) Lands**: `.agent/skill-weights.json` (mtime 07-23, written by `evolution_orchestrator.py` daily cycle), `.agent/routing-intelligence.json` (582KB, mtime today 14:56 — written per-prompt by the hook).
- **(c) Evidence of closure**: weights are genuinely learned, not defaults — spread 0.5 (brand-operating-system) to 1.67 (april-dunford-positioning) — and are read back at decision time: `find_skill.py` applies them in `rank()` (confirmed via grep; skill_router_hook.py:28 documents the wire). So yesterday's outcomes literally reorder tomorrow's `[CORE]` surfacing.
- **(d) Verdict**: COMPOUNDING.
- **(e) Repair (minor)**: quality cursor lags 3 days behind traces (last consumed trace 07-21 vs v2_traces active 07-24 11:36) — only because the daily cycle missed 07-24 (see Loop 4). Fixing Loop 4's catch-up fixes this.

### 4. evolution_orchestrator.py auto — COMPOUNDING, one scheduling gap
- **(a) Input**: performance log, traces, skill audits.
- **(b) Lands**: `evolution_store/` (skill_audit_* regenerated 07-24 10:59; queue files 07-23 07:00), `.agent/skill-weights.json`, `orchestrator_state.json`.
- **(c) Evidence of closure**: `orchestrator_state.json` = daily 2026-07-23T07:00:03, weekly 07-17, monthly 07-10 — the launchd train (`com.antigravity.evolution-auto`, last exit 0) has been running its cycles. Pause state clean (`evolution-paused.json`: paused=false since 05-04).
- **(d) Verdict**: COMPOUNDING for its deterministic arms (weights, audits, queue population). **Gap**: today is 07-24 15:00 and last_daily is 07-23 — the 07:00 run was missed (log tail shows only a status dump with `days_remaining: 0.0`, i.e. due-but-not-run). StartCalendarInterval fires are lost when the machine sleeps through the minute.
- **(e) Repair**: add `RunAtLoad=true` (or a `StartInterval` fallback / `launchd` `WakeRequestsSleep` alternative: a login-time catch-up invocation of `evolution_orchestrator.py auto`, which is already idempotent — it self-checks `not_due_yet`). One plist key, zero context cost.

### 5. Steering loop — OPEN
- **(a) Input**: `steering_loop_hook.py` injects the Next-Moves requirement per exchange (state file `.agent/steering-loop-state.json` updated today 15:04 — hook is alive) and logs misses.
- **(b) Lands**: `.agent/sessions/steering-observe.jsonl` — 54 events, 100% `next-moves-missing`, spanning 07-08 → 07-23.
- **(c) Evidence of closure**: none. Grep shows the only readers of steering-observe.jsonl are the hook itself and `health_metrics.py`, which tracks *file size and age only*. No digest, no per-model miss-rate, no escalation, no decision record on whether to enforce. The observe log is write-only.
- **(d) Verdict**: OPEN — observation without a consumer.
- **(e) Repair**: extend the existing hook (no new prose): when the last N exchanges of a session contain ≥2 logged misses, have `steering_loop_hook.py` escalate its injected reminder from passive to imperative (it already injects text per exchange — this is a 10-line conditional reading its own log). Plus one line in `health_metrics.py` computing miss-count-per-week so the weekly board shows the trend instead of bytes.

### 6. Memory pipeline — COMPOUNDING through distill; OPEN at the human review gate
- **(a) Input**: episodic plugin captures (L1) → launchd `harvest-memory-daily` (daily 14:40 UTC per log) → embed → `distill-weekly`.
- **(b) Lands**: `.memory/sovereign.db` (86MB, mtime today 11:36); flagged rules into `memory_review.py` queue.
- **(c) Evidence of closure**: harvest log is a clean daily heartbeat — `[2026-07-24T14:40:04] embedded +8 → 5447/5447 (100.0%) · distill: ok`, unbroken 07-17→07-24. Distill-weekly ran and *judged* (sample rule scored 9.5/10, flagged fr_96b46c6f). mirror-nightly + memory-backup exit 0; backups dir current (07-24 03:00). Facade fires return sovereign/episodic hits (64 logged fires, latest today). The mechanical loop closes.
- **(d) Verdict**: pipeline COMPOUNDING; the *learning* half is OPEN — 9 distilled rules sit `pending` in `memory_review.py list` (oldest 07-19, one added every day since). The highest-scored insights the system produces about itself are never approved, so they never activate.
- **(e) Repair**: the review backlog needs a pull surface, not more machinery: append a "N memory rules pending review" line (with the top rule inline) to the existing `/cos` daily brief generator — it already runs on launchd. Optionally auto-approve rules with judge_score ≥9.0 into a `provisional` tier that retrieval labels as such; deterministic, reversible.

### 7. Wargame OS failure-maps — DEAD as a loop
- **(a) Input**: `/wargame-run` banks frontier judgment (Moves/Expect/Fail/Trigger) "in the mission's wargames/ folder" per workflow.
- **(b) Lands**: nowhere findable. `find . -iname "*wargame*"` outside skills/workflows/extractions returns only `guides/2026-07-13-wargame-os.md`. Zero banked wargame-run artifacts exist on disk 11 days after the OS shipped.
- **(c) Evidence of re-read**: none possible — nothing banked, and grep for `failure_map`/`failure-map` across `execution/*.py` returns nothing; no facade source, no router injection, no ledger.
- **(d) Verdict**: DEAD. The skill exists and may have been used in-session, but banked judgment ("bank judgment as failure-maps for cheap executors" — the OS's entire thesis) has no persistence or resurfacing mechanism.
- **(e) Repair (minimal, zero context cost)**: give failure-maps a canonical home the existing machinery already indexes: `docs/solutions/` cards (the facade + router hook resurface these for free) or a flat `wargames/` dir added as one more source block in `memory_facade.py` (~30 lines, copy `_query_solutions`). Then one line in `/wargame-run`'s save step pointing at the canonical dir. Without a canonical persisted path, every wargame is a one-shot.

### 8. Calibration + ground-truth rubric — OPEN (2 reviews from closing)
- **(a) Input**: finalize verdicts + human blind-pass reviews → `evolution_store/ground_truth/eval_set_v1.jsonl` (auto-appending — mtime today 11:30).
- **(b) Lands**: eval set (85 entries), `rubric_v1.md`, `blind_pass_overrides.jsonl` (active — mtime 07-24 09:54).
- **(c) Evidence of closure**: partial. `eval_harness.py status`: 66 human-calibrated of 68 needed → `rubric_load_bearing: false`, `calibration_complete: false`. 19 auto-seeded entries pending review since seed_candidates_2026-07-17.jsonl. `verdict_advisory.jsonl` (the R1 advisory for the R2 precedent gate): 2 of the last 3 SHIP verdicts logged `MISSING_PRECEDENT — R2 will refuse this`. The blind-pass hard gate in chain_runner (line 674) is dormant until `.agent/enforce-trials/blind_pass.json` activates. Everything is staged; the trigger is a human review that hasn't happened. Calibration drift check (`eval_harness.py calibrate --days 7`) is wired only into /weekly-closeout — which has never left a finalize record (see Loop 9), so no evidence it has ever run on schedule.
- **(d) Verdict**: OPEN — highest ratio of built-machinery-to-missing-closure in the system; the missing piece is ~15 min of Farrice reviewing 19 seeds (2 net reviews reach load-bearing).
- **(e) Repair**: don't build — *deliver the review*. Generate a single mission card (`.agent/mission-queue/pending/`, the outcome-chase pattern already proven 07-21) that presents the 19 auto-seeded entries as accept/reject one-liners. When 68 is crossed, `eval_harness` flips load-bearing and the already-written R2 refusal path in chain_runner goes live with zero further work.

### 9. Revenue tracker outer loop — OPEN (recently improved)
- **(a) Input**: finalize auto-registers deliverables → `.agent/revenue-outcomes.json` (177 outcomes, mtime today 11:36).
- **(b) Lands**: same file + `revenue_tracker.py pipeline/report`.
- **(c) Evidence of closure**: mixed. Good: pipeline is down to **16** awaiting outcome (ticket expected ~101 — a real drain happened; `card-outcome-chase-2026-07-21.md` sits in `.agent/mission-queue/done/` with transcript, so the outcome-chase → mission-runner train fired end-to-end at least once). Bad: only **4 of 177** deliverables have revenue attached ($4,400 total) — outcome data essentially never comes back; `/weekly-closeout` (the designed drain ritual) has **zero** entries in performance-log.jsonl, ever; and `com.antigravity.outcome-chase` launchd job's log file (`.agent/cos/outcome-chase.log`) does not exist — the daily 04:00 job has plausibly never fired via launchd (script created 07-21; 04:00 = machine asleep), meaning the 07-21 chase was manual.
- **(d) Verdict**: OPEN — the inner registration loop compounds; the outer outcome loop closes only when manually pushed.
- **(e) Repair**: same fix as Loop 4 — sleep-proof the launchd schedule (`RunAtLoad` catch-up on `outcome_chase.py generate`; it's already idempotent with a 6-day dedupe). That makes the chase card self-generating weekly; mission-runner already executes it.

### 10. offer_gate.py / offer-redteam — OPEN
- **(a) Input**: offer definitions checked for demand receipts / units sold.
- **(b) Lands**: `.agent/offer-gate-log.jsonl`.
- **(c) Evidence of closure**: the two logged runs (both 2026-07-21T14:08:10, both FLAG) did real work — they're the red-team that killed the $400 audit and modified Signal Pilot (memory: "offer_gate.py + /offer-redteam = the anti-echo-chamber loop"). But both entries share one timestamp = a single build-day invocation. Nothing has triggered it in the 3 days since, and nothing *can* trigger it automatically — no routing binding, no hook, no finalize integration references it.
- **(d) Verdict**: OPEN — a gate with no road through it.
- **(e) Repair**: add one binding to `routing_enforcer.py BINDINGS` (+ mirror row in `directives/routing-bindings.md`, per CLAUDE.md's update-together rule): offer/pricing/funnel-shaped deliverables route through `/offer-redteam`, which runs `offer_gate.py`. The enforcement plumbing (UserPromptSubmit warnings) already exists; this is one dict entry.

### 11. Session ledger — OPEN
- **(a) Input**: PostToolUse/Stop events → finalize-debt detection.
- **(b) Lands**: `.agent/sessions/observe-log.jsonl` — 817 lines: 685 `would_block`, 52 autopins, 54 auto-closeouts, since 2026-06-14.
- **(c) Evidence of closure**: the *capture* is superb (would_block entries carry debts, produced_paths, measured subagent_spawns). The *closure* is absent: observe mode has run for 22 days (Farrice decision 07-02) with 347 entries in just the last 7 days; no analyzer summarizes would-block causes; `health_metrics.py` reads only byte-size; LEDGER_ENFORCE has never been trialed. Compare: 685 would-blocks vs 128 finalize records — finalizes happen, but the Stop-time debt pattern (skill loaded → produce → no finalize *yet at that Stop*) fires ~10x per honest session, meaning flipping enforce today would block constantly on false positives. That's a tuning signal nobody is reading. Related: the routing-bindings enforce trial (`.agent/routing-enforce-trial.json`) **expires today** with 4 log entries (2 of them fixtures) and its designated review ritual (/weekly-closeout) has never run — the trial will silently lapse with no verdict.
- **(d) Verdict**: OPEN — richest unread dataset in the system.
- **(e) Repair**: a ~50-line `execution/session_ledger_report.py` (would-block causes bucketed: multi-Stop-per-session noise vs true never-finalized sessions; per-week trend) wired as one section of the existing health-metrics launchd job. Its output is the evidence needed to either fix the Stop-debounce and flip `LEDGER_ENFORCE=1`, or consciously retire enforcement. Also: record a verdict on the routing trial today (extend or expire is fine — silence is not).

### 12. Skill-evolution / autoresearch Phase 2 — OPEN
- **(a) Input**: performance regressions → `evolution_store/queue/phase2_queue.jsonl` + `skill_evolution_candidates.json` (both refreshed daily by the orchestrator, mtime 07-23 07:00).
- **(b) Lands**: queue of 130 entries (1 May, 36 June, 93 July — producer accelerating).
- **(c) Evidence of closure**: exactly one calibrated-era consumption: commit `dcc8f69d7` 2026-07-06 "first calibrated-era Phase 2 cycle — alex-suzuki KEPT 6.22→7.22" — proof the loop *can* close and produce a measured skill improvement. Nothing since: 18 days, 93 new queue entries, zero cycles. Phase 3 remains PAUSED pending "eval set ≥15 human-calibrated + one Phase 2 cycle on a calibrated candidate" (feedback-ratchet.md:148) — the first condition is met (66), the second happened once, so the unlock is arguably satisfied but unclaimed.
- **(d) Verdict**: OPEN — daily producer, near-never consumer. This is the ratchet's missing fix-arm.
- **(e) Repair**: put consumption on the same train as production: monthly orchestrator cycle emits a mission card for the single top `auto_evolve_eligible` queue candidate (the queue rows already carry that flag and `human_review_required` routing), executed by the existing 02:30 mission-runner. One card a month = 12x current consumption rate, human-gated where the queue says so, zero new prose.

---

## Cross-cutting observations

1. **The pattern is consistent: capture compounds, consumption doesn't.** Loops 1–4 close because a deterministic job both writes AND reads (weights → rank(); cards → injection). Loops 5, 8, 9, 11, 12 all stall at the identical joint: a log/queue accumulates and the designated reader is either a human ritual that never runs (/weekly-closeout: 0 finalize records ever) or nothing at all.
2. **/weekly-closeout is the single point of failure for four loops** (revenue drain, calibration drift check, evolution queue decision, routing-trial review). Its own directive says the staleness hook should prompt it — evidence says that prompt either doesn't fire or doesn't convert. Every repair above routes around it via launchd/mission-cards rather than through it.
3. **Sleep-lossy launchd schedules** are a second recurring cause (evolution-auto missed 07-24; outcome-chase log never created). `RunAtLoad`/catch-up on the idempotent entry points fixes three loops at once.
4. **Two red launchd jobs** need attention independent of this audit: citation-integrity (exit 1, 2 missing pointers) and verify-fleet (exit 1, 30/86 contracts failing).
