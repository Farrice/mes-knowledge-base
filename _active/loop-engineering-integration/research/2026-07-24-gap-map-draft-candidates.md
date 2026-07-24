# Gap Map — DRAFT Ranked Candidates (Canon × Loop Inventory)

**Ticket:** wayfinder 0003 · **Date:** 2026-07-24 · **Status:** DRAFT — verdicts are proposals, not decisions.
**Inputs:** [canon research](2026-07-24-canon-proven-vs-hype.md) · [loop inventory audit](2026-07-24-loop-inventory-audit.md) · [MAP constraints](../wayfinder/MAP.md)
**Binding constraints applied:** REPAIR-FIRST (audit repairs outrank new patterns) · ZERO CONTEXT COST (deterministic code/hooks/launchd only; priced exceptions) · EXTEND-NEVER-REBUILD (no host loop = exceptional justification required).
**Ranking axis:** leverage-per-risk — how many loops close, per unit of blast radius.

---

## Ranked Summary Table

| Rank | Candidate | Type | Draft verdict | Footprint |
|---|---|---|---|---|
| 1 | Sleep-proof the launchd train (RunAtLoad catch-up) | REPAIR (loops 4, 9, +3's cursor lag) | **GO** | 2 plist keys, 0 tokens |
| 2 | Calibration-closure mission card (19 seeds → load-bearing rubric) | REPAIR (loop 8) | **GO** | 1 mission card, 0 tokens (~15 min Farrice) |
| 3 | Routing-trial verdict TODAY + session-ledger report | REPAIR (loop 11) | **GO** (verdict is same-day urgent) | ~50-line py + 1 launchd section, 0 tokens |
| 4 | Phase-2 consumer on the mission-runner train | REPAIR (loop 12) | **GO** | ~20 lines in orchestrator monthly cycle, 0 tokens |
| 5 | Offer-gate routing binding | REPAIR (loop 10) | **GO** | 1 dict entry + 1 directive row, 0 tokens |
| 6 | Wargame failure-map canonical home | REPAIR (loop 7 — the DEAD one) | **GO** | ~30 lines facade + 1 workflow line, 0 tokens |
| 7 | Memory-review pull surface in /cos brief | REPAIR (loop 6) | **GO** (provisional-tier half: CONDITIONAL) | ~15 lines in cos generator, 0 tokens |
| 8 | Repair the two red verification jobs (verify-fleet 30/86, citation-integrity) | REPAIR (adjacent infra) | **GO** | py fixes, scope unknown until triaged, 0 tokens |
| 9 | Solution-injection hit-rate logging | REPAIR (loop 1, minor) | **GO** | 1 json append in router hook, 0 tokens |
| 10 | Steering-loop escalation + weekly miss-rate | REPAIR (loop 5) | **GO-LEAN** | ~10-line hook conditional + 1 metrics line, 0 tokens |
| 11 | CLAUDE.md token ratchet in monthly CORE DRIFT scan | NEW (map-not-encyclopedia) | **GO** | ~10 lines in monthly cycle, 0 tokens |
| 12 | Metric-ratchet pilot on verify-fleet pass rate | NEW (autoresearch pattern) | **CONDITIONAL GO** — only after #8, locked + capped | 1 bounded script, priced: 1 overnight session of subscription tokens |

Not padded to 15: every other canon pattern either repairs nothing (already covered) or lands in DO-NOT-DO.

---

## Per-Candidate Detail

### 1. Sleep-proof the launchd train — REPAIR · GO

**(a)** Add `RunAtLoad=true` (or a login-time catch-up invocation) to `com.antigravity.evolution-auto` and `com.antigravity.outcome-chase`. Both entry points (`evolution_orchestrator.py auto`, `outcome_chase.py generate`) are already idempotent — they self-check `not_due_yet` / 6-day dedupe, so a catch-up fire is safe.
**(b)** Repairs loop 4 (evolution daily missed 07-24), loop 9 (outcome-chase launchd log has *never been created* — the 04:00 job plausibly never fired), and clears loop 3's 3-day routing-quality cursor lag as a free side effect. Audit cross-cutting finding #3 names sleep-lossy schedules as a recurring root cause.
**(c)** Canon: Cherny's outer-loop doctrine — `/loop` is clock-driven, and its whole value is that it actually fires (Sequoia transcript, **PROVEN**). Anthropic runs the same split as `/loop` vs Routines (server-side, laptop closed) precisely because local cron loses fires.
**(d)** Footprint: one key in each of 2 plists. Zero context cost. No new files.
**(e)** Risk: near-nil. Catch-up runs write to `evolution_store/` and `.agent/` — if a harness session is mid-flight the writes are to append logs and state JSONs the orchestrator already owns; no source-tree edits, so the two-harness single-writer rule isn't implicated. Fully deterministic (no AI-memory dependence).
**(f)** Payoff: three loops go from "compounds when the machine happens to be awake" to "compounds daily." Highest closed-loops-per-line-changed in the whole brief.
**(g)** **GO** — one-key fix, three loops, no downside identified.

### 2. Calibration-closure mission card — REPAIR · GO

**(a)** Generate one mission card in `.agent/mission-queue/pending/` presenting the 19 auto-seeded eval entries as accept/reject one-liners for Farrice. 2 net approvals cross the 68 threshold; `eval_harness.py` flips `rubric_load_bearing: true` and the already-written R2 precedent-refusal path in `chain_runner.py:674` goes live with zero further code.
**(b)** Repairs loop 8 — the audit's "highest ratio of built-machinery-to-missing-closure." Extends the outcome-chase mission-card pattern proven end-to-end on 07-21 (card in `done/` with transcript).
**(c)** Canon: verification is the load-bearing primitive of the entire field (Anthropic first-party doctrine, **PROVEN**) — and the specific sub-pattern is the external-judge stop condition (`/goal`'s separate-judge design, **PROVEN** product doc): the grader must not be the producer. Farrice's blind pass IS the external judge; this card is just delivery logistics for it.
**(d)** Footprint: one generated markdown card (existing pattern), zero tokens of always-on context. ~15 min of Farrice's attention — the priced human cost, already budgeted by the audit.
**(e)** Risk: only that the card sits unread like /weekly-closeout did. Mitigation is built in: mission-runner already surfaces pending cards, and this is a one-shot, not a ritual. Deterministic throughout.
**(f)** Payoff: rubric becomes load-bearing → R2 verdict gate arms → every future finalize is checked against human-calibrated precedent instead of self-grading. This is the system's verification spine going from staged to live.
**(g)** **GO** — 15 human-minutes buys the doctrine the canon says matters most.

### 3. Routing-trial verdict + session-ledger report — REPAIR · GO (same-day component)

**(a)** Two parts. (i) TODAY: record an extend/expire verdict on `.agent/routing-enforce-trial.json` — it expires 2026-07-24 with 4 log entries and its review ritual never ran; silence = the trial lapses with no learning. (ii) Ship `execution/session_ledger_report.py` (~50 lines): bucket the 685 would-block events into multi-Stop-per-session noise vs. true never-finalized sessions, per-week trend, wired as one section of the existing health-metrics launchd job.
**(b)** Repairs loop 11 — "richest unread dataset in the system." Extends `health_metrics.py` (which currently reads only byte-size) and the existing observe-mode decision from 07-02.
**(c)** Canon: measure before you enforce — Anthropic's Stop-hook ladder is explicitly graduated (in-prompt → /goal → Stop hook → subagent, **PROVEN** doc), and the audit shows flipping `LEDGER_ENFORCE=1` today would false-positive ~10x per honest session. The report is the tuning instrument the ladder assumes. Also the field's honest-gap finding: nobody publishes loop-failure data — this repo has 817 lines of it, unread.
**(d)** Footprint: one new ~50-line py file + one call site in the health-metrics job + one JSON verdict write. Zero context cost.
**(e)** Risk: minimal — read-only analysis over an append log. The report must stay deterministic (bucketing rules in code, not model judgment) per the AI-memory-dependent-observability ban; the design already is.
**(f)** Payoff: converts 22 days of observe-mode data into an actual enforce/retire decision on finalize debt, and stops a live trial from dying by silence today.
**(g)** **GO** — part (i) is the single most time-sensitive line in this brief.

### 4. Phase-2 consumer on the mission-runner train — REPAIR · GO

**(a)** Monthly orchestrator cycle emits one mission card for the top `auto_evolve_eligible` entry in `phase2_queue.jsonl` (rows already carry that flag + `human_review_required` routing); the existing 02:30 mission-runner executes it. One card/month = 12x the current consumption rate (one cycle ever, 18 days idle, 93 July entries queued).
**(b)** Repairs loop 12 — the feedback ratchet's missing fix-arm (loop 2's audit verdict explicitly points here). Extends `evolution_orchestrator.py` monthly cycle + mission-runner; rebuilds nothing.
**(c)** Canon: this is the metric-ratchet loop — the **only PROVEN-with-independent-replication pattern in the survey** (Karpathy autoresearch → Shopify 40+ metrics; commit-on-improvement, rollback-on-regression). The repo already ran one calibrated cycle with exactly that shape: alex-suzuki KEPT 6.22→7.22, commit `dcc8f69d7`. The pattern is validated locally *and* globally; only the cadence is missing.
**(d)** Footprint: ~20 lines in the orchestrator monthly arm emitting a card from queue data. Zero context cost. Token cost of the monthly cycle itself: one skill-evolution session/month inside the subscription — priced and bounded by the single-card cap.
**(e)** Risk: mission-runner edits skill files → single-writer concern. Mitigated: runs at 02:30 (no interactive harness), and `session_lock.py` exists for long autonomous runs — the card template should take the lock. Ratchet semantics (keep only on measured score improvement) bound the damage of a bad edit; Shopify's own caveat ("throw away the hacks") is honored by the queue's `human_review_required` routing.
**(f)** Payoff: the ratchet's capture arm (99 performance records, 130-deep queue) finally drives measurable skill improvement on a schedule instead of once ever. Also arguably claims the Phase-3 unlock condition (feedback-ratchet.md:148) that is met but unclaimed.
**(g)** **GO** — the audit's clearest producer-without-consumer, fixed with the canon's best-evidenced pattern.

### 5. Offer-gate routing binding — REPAIR · GO

**(a)** One entry in `routing_enforcer.py BINDINGS` + mirror row in `directives/routing-bindings.md` (update-together rule): offer/pricing/funnel-shaped deliverables route through `/offer-redteam`, which runs `offer_gate.py`. Enforcement plumbing (UserPromptSubmit warnings) already exists.
**(b)** Repairs loop 10 — a gate with no road through it: 2 log entries ever, both from build day, nothing *can* trigger it automatically.
**(c)** Canon: adversarial-reviewer-in-separate-context (**PROVEN** pattern, Anthropic doc) applied to revenue decisions; the gate's one firing already killed the $400 audit offer and modified Signal Pilot — locally receipted. Binding it makes the anti-echo-chamber loop structural instead of remembered.
**(d)** Footprint: 1 dict entry + 1 directive table row. Zero context cost (the directive row is in an on-demand file, not CLAUDE.md).
**(e)** Risk: over-firing on offer-adjacent prompts → routing warnings are advisory with documented override flags, so worst case is a one-line nag. Honor the canon's reviewer warning (§3.8): the red-team must flag only correctness/demand gaps, not manufacture findings — that instruction lives in the existing workflow, no new prose.
**(f)** Payoff: every future offer decision passes the gate that already proved it can kill a bad offer. Cheapest insurance in the brief.
**(g)** **GO** — one dict entry to make a proven gate un-skippable.

### 6. Wargame failure-map canonical home — REPAIR (DEAD loop) · GO

**(a)** Give failure-maps a persisted, indexed home: either `docs/solutions/` cards (facade + router hook resurface these for free today) or a flat `wargames/` dir added as one more `memory_facade.py` source (~30 lines, copy `_query_solutions`). Plus one line in `/wargame-run`'s save step naming the canonical path.
**(b)** Repairs loop 7 — the audit's only DEAD loop: zero banked artifacts, zero reader code, 11 days after the OS shipped. Its entire thesis ("bank judgment as failure-maps for cheap executors") has no persistence.
**(c)** Canon: fresh-context doctrine — progress must accumulate in *files and git history*, never in the context window (Huntley, **PROVEN** for the persistence principle); and Larson's read of compound engineering: the *novel* part is plan-step retrieval of compounded artifacts (**PROVEN** framing). A wargame that isn't retrievable at plan time never happened.
**(d)** Footprint: ~30 lines in memory_facade OR zero code (reuse docs/solutions/) + 1 workflow line. Zero context cost.
**(e)** Risk: near-nil; write path is markdown files, read path is the existing facade. Prefer the docs/solutions/ route first — it's zero new code and the audit shows that resurfacing loop is the system's best-proven (31/64 facade fires).
**(f)** Payoff: revives the Wargame OS from decorative to compounding; every future wargame becomes a permanent failure-map cheap executors actually see.
**(g)** **GO** — resurrecting a DEAD loop for one workflow line + optionally 30 lines.

### 7. Memory-review pull surface — REPAIR · GO (half CONDITIONAL)

**(a)** Append "N memory rules pending review" (top rule inline) to the existing `/cos` daily brief generator (already on launchd). Optionally: auto-approve rules with judge_score ≥9.0 into a `provisional` tier that retrieval labels as such — deterministic, reversible.
**(b)** Repairs loop 6's open half: 9 distilled rules stuck `pending` since 07-19 — the highest-scored insights the system produces about itself never activate.
**(c)** Canon: self-updating-rules loop is **PLAUSIBLE with a hard ceiling** (§3.5) — it works *only* paired with review/pruning, else compound liability. The pending queue IS the pruning gate; the failure is that its input surface is invisible. Also MAP's own rule: never interview about what memory already knows — inactive rules are memory the system paid for and can't use.
**(d)** Footprint: ~15 lines in the cos generator; provisional tier ~20 more in memory_retrieve labeling. Zero context cost (brief line is in an existing generated artifact).
**(e)** Risk: pull-surface half: none. Provisional-tier half: a wrong rule auto-activates at ≥9.0 — mitigated by the explicit `provisional` label and reversibility, but this is exactly the canon's "codifying lessons that aren't true yet" failure (§ compound liability), so it stays CONDITIONAL pending Farrice's read.
**(f)** Payoff: the distill loop's output finally reaches a decision-maker daily; review latency drops from "never" to "next /cos read."
**(g)** **GO** on the brief line; **CONDITIONAL** on auto-provisional — offer both, default to the safe half.

### 8. Repair the two red verification jobs — REPAIR (adjacent) · GO

**(a)** `com.antigravity.verify-fleet` exits 1 with 52 pass / 30 fail / 4 skip of 86 contracts; `com.antigravity.citation-integrity` exits 1 with 2 missing pointers. Triage and fix to green (or explicitly retire dead contracts).
**(b)** Not one of the 12 ticket loops — audit flagged as adjacent infra — but it's the substrate: a verification fleet that's 35% red is a verifier nobody can trust, which per canon poisons every loop that relies on mechanical checks (candidates 2, 4, 12 all lean on it).
**(c)** Canon: "give the agent a check it can run" is the single most evidenced primitive in the field (Anthropic institutional doctrine, **PROVEN**); OpenAI's harness result rests on invariants "enforced mechanically via custom linters and structural tests" (**PROVEN**). Red checks are worse than no checks — they train the operator to ignore exit codes.
**(d)** Footprint: unknown until the 30 failures are bucketed (stale contracts vs real breakage) — first step is a read-only triage listing. Zero context cost.
**(e)** Risk: scope creep — 30 failures could hide real regressions requiring source edits (single-writer rule applies: do it in one harness, clean git status handoff). Cap the first pass at triage + retire-or-fix decisions per contract.
**(f)** Payoff: the verification substrate every other GO candidate stands on becomes trustworthy; exit-code green becomes meaningful again.
**(g)** **GO**, sequenced early but sized honestly: triage first, fix second.

### 9. Solution-injection hit-rate logging — REPAIR (minor) · GO

**(a)** One `json.dumps` append to `.agent/sessions/solution-injections.jsonl` in the injection branch of `skill_router_hook.py` (~line 477), so "PRIOR SOLUTION EXISTS" injections become countable.
**(b)** Minor repair to loop 1 (already COMPOUNDING) — makes the system's best loop *auditable* instead of assumed.
**(c)** Canon: the field's biggest honest gap is that nobody measures their loops (§Part 4, "no systematic public corpus of loop failures"); Shopify's ratchet works because every experiment is measured. Cheap measurement is how the next audit gets receipts instead of vibes.
**(d)** Footprint: ~3 lines in an existing hook. Zero context cost.
**(e)** Risk: none identified; append-only log, deterministic.
**(f)** Payoff: injection hit-rate becomes a real metric for the next loop audit; also the template for measuring the other hooks.
**(g)** **GO** — three lines, permanent auditability.

### 10. Steering-loop escalation — REPAIR · GO-LEAN

**(a)** Extend `steering_loop_hook.py`: when its own miss log shows ≥2 misses in the last N exchanges of a session, escalate the injected reminder from passive to imperative (~10-line conditional reading its own log). Plus one line in `health_metrics.py` computing misses/week.
**(b)** Repairs loop 5 — 54 logged misses, zero consumers.
**(c)** Canon: graduated gating (in-prompt nudge before hard Stop-hook, per Anthropic's four-strength ladder, **PROVEN** doc) — escalation-within-the-hook is the correct next rung, not enforcement.
**(d)** Footprint: ~10 lines hook + 1 line metrics. Zero context cost (the injected text already exists; only its intensity changes).
**(e)** Risk: none structural. The honest question is value: 100% of misses are `next-moves-missing`, and no evidence exists that Next-Moves blocks drive outcomes — this loop's *worth* is less proven than its plumbing.
**(f)** Payoff: modest — miss-rate trend becomes visible and the reminder self-tunes; also settles whether the steering loop deserves enforcement or retirement.
**(g)** **GO-LEAN** — do it because it's 11 lines, rank it low because the underlying loop's value is unproven.

### 11. CLAUDE.md token ratchet — NEW · GO

**(a)** Add a deterministic check to the monthly CORE DRIFT scan (already in the weekly-ritual/monthly cycle): measure CLAUDE.md token count; if it grew since last scan, emit a one-line prune prompt listing the newest additions with the canon's test ("would removing this cause mistakes?"). A ratchet on size, not content — it never edits, only flags.
**(b)** Genuinely net-new: no existing loop watches context-file growth. Justification for a NEW entry under extend-never-rebuild: it *extends* the existing monthly scan (host loop = evolution orchestrator monthly arm) and defends the MAP's own zero-context-cost constraint mechanically instead of by memory.
**(c)** Canon: map-not-encyclopedia — "the strongest signal in the entire survey" (§3.4, **PROVEN**, both frontier labs independently: OpenAI ~100-line AGENTS.md index; Anthropic "bloated CLAUDE.md files cause Claude to ignore your actual instructions"). Biggest documented failure mode in the field is compound liability — rules files that grow until the agent stops reading them (§TL;DR line 10, **PROVEN**).
**(d)** Footprint: ~10 lines in the monthly cycle + one state value. Zero context cost — ironically, it's the candidate that *protects* zero context cost.
**(e)** Risk: none — read-only measurement, human-decided pruning. Complies with the deterministic-backstop ban trivially.
**(f)** Payoff: the 50KB→26KB optimization stops silently regressing; every future loop candidate that wants CLAUDE.md prose meets a measured gate.
**(g)** **GO** — the cheapest possible enforcement of the project's own binding constraint.

### 12. Metric-ratchet pilot on verify-fleet pass rate — NEW · CONDITIONAL GO

**(a)** A bounded, Karpathy-shaped overnight run: agent may edit only failing verify-fleet contracts (or the code they check, scoped per card), metric = contracts passing, commit-on-improvement / rollback-on-regression, hard iteration ceiling, session lock held. One night, one metric, one report.
**(b)** Net-new pattern (no existing loop does timeboxed metric-ratchet experimentation). Exceptional justification: it's the canon's only independently-replicated loop, and the repo has a ready-made objective metric (candidate 8's 30 failing contracts) — the exact "mechanically checkable" precondition the canon demands.
**(c)** Canon: autoresearch → Shopify (**PROVEN** — independent replication + production generalization to 40+ metrics + first-party failure modes). Also its verbatim caveats: results "somewhat overfit," agents produce "ugly hacks... deleting files," manual review required.
**(d)** Footprint: one script (or one mission card driving existing tooling) + session lock. Context cost zero; token cost priced: one overnight session inside the subscription (Cherny-class outer loop; no paid API — cost-gate territory stays untouched).
**(e)** Risk: highest in the brief. (i) Two-harness single-writer: an overnight editing loop is exactly the pattern that assumes one writer — MUST hold `session_lock.py` and run only when no harness is active; a morning `git status` gate before any human session resumes. (ii) Reward hacking: Shopify's "deleting files" failure maps directly to an agent gaming pass-rate by gutting contracts — the ratchet must diff-review-gate contract-file deletions. (iii) Runs against an existing codebase, where Huntley disowns pure Ralph — mitigated by the narrow single-metric scope, which is autoresearch's (not Ralph's) design.
**(f)** Payoff: if it works, the repo gains a reusable overnight-ratchet primitive applicable to other deterministic metrics (health metrics, prose-classifier pass rates, hook latency) — the Shopify generalization path.
**(g)** **CONDITIONAL GO** — only after candidate 8's manual triage (so the metric is honest), with lock + iteration ceiling + morning review as non-negotiable card terms. If the conditions feel heavy, this one dies without regret; it is the brief's only speculative entry.

---

## DO-NOT-DO — canon patterns rejected for this system

1. **Install the Every compound-engineering plugin (`/ce-*`, 40+ agents).** The chain IS this system's compound loop, already calibrated to Farrice. Ry Walker: "full seven-step loop is overkill for quick fixes... parallel review agents consume significant context." Klaassen himself: not ideal on a subscription plan — "it will just use more tokens." Buying ceremony + token burn to duplicate loops 1–4, which the audit shows already compound. Violates zero-context-cost and extend-never-rebuild simultaneously.
2. **Run Ralph (fresh-context bash loop) against this repo — including the official `ralph-wiggum` plugin.** Huntley, verbatim: "There's no way in heck would I use Ralph in an existing code base" — this is a 2-year-old living tree, not greenfield. And the official plugin is **not** Huntley's Ralph: it re-feeds prompts *in the same session*, context accumulates, no re-anchoring (Giancini, PROVEN divergence) — the opposite of the pattern's point, with an unreliable `--completion-promise` string match on top. Worst of both worlds here: same-session context rot *plus* an unattended writer in a two-harness tree.
3. **Cherny-style loop sprawl ("dozens of cron loops").** The audit's core finding is that this system's failure mode is producers-without-consumers — 5 of 12 loops stall at unread logs. Adding more clock-driven producers before the consumption arms are repaired manufactures more open loops with receipts attached. Cherny's loops work because each one is narrow *and he reads the output*. Repair consumption first; new /loops only with a named consumer.
4. **Append-every-failure into CLAUDE.md ("the agent never makes the same mistake twice").** The most-circulated version of compound engineering drops the pruning half of Cherny's practice. Anthropic: "Bloated CLAUDE.md files cause Claude to ignore your actual instructions." Two frontier labs converged on ~100-line index files (PROVEN). This repo already has the correct architecture — solution cards + memory tiers + on-demand directives; failures land there, never in always-on prose. Candidate 11 is the mechanical guard.
5. **Agent-to-agent review with humans optional (OpenAI harness pattern).** PROVEN — for a 7-engineer team building a greenfield internal tool with published-throughput/unmeasured-quality. This system's deliverables are taste-bearing client and voice work where Farrice's felt verdict is the ground truth (bimodal PASS/FAIL taste signature; dissent-preserved output; blind passes). Removing the human from review would sever the only calibration source the eval set has. Adversarial *subagent* review stays (already deployed); human-optional does not.
6. **`/grep-loop`-style external critic-score tooling (Greptile et al.).** The mechanism is sound, but the vendor numbers are marketing self-reports, and the system already owns the same design property — an external numeric stop condition — via the calibrated finalize rubric + R2 precedent gate (armed by candidate 2). Adding a paid third-party scorer duplicates the gate and violates the no-new-paid-API constraint.
7. **Implement ACE (evolving-context deltas) in the harness.** PROVEN benchmark, zero published replications inside a coding-agent harness. It's the *theory* for why pruned/modular beats append-only — take the lesson (candidates 7 and 11 embody it), skip the implementation.
8. **Flip `LEDGER_ENFORCE=1` now.** The Stop-debt detector fires ~10x per honest session (685 would-blocks vs 128 real finalizes); enforcement today = constant false-positive blocks, and per canon the Stop-hook is the *strongest* rung of a graduated ladder, not the first. Candidate 3's report is the prerequisite; enforcement is a later, evidence-carrying decision.
9. **Chase the "300–700% faster" / "2–3x verification" numbers as targets.** The first is HYPE (measures LOC, unsourced to Every; "a debt accelerator"); the second is Cherny's uncorroborated self-report. Build the verification loops for their PROVEN mechanism; never cite or KPI these numbers. Compounding here gets measured the audit's way: signal captured AND later behavior demonstrably changed.

---

## Cross-cutting notes for the brief

- **Sequencing:** #3(i) is same-day (trial expires today). #1 and #8-triage unblock the most downstream value. #2 is the only candidate needing Farrice's minutes. #12 waits on #8 by design.
- **Single-writer compliance:** every GO candidate writes via launchd/mission-runner at hours no harness runs, or appends to `.agent/` logs the hooks already own. Only #12 edits source unattended — hence its lock-and-cap conditions.
- **Observability ban compliance:** every consumer added here is deterministic code reading files (report scripts, plist keys, hook conditionals) — no candidate relies on a model remembering to check something.
- **The shape of the whole brief:** 10 of 12 candidates are repairs, and the two NEW entries both *defend* existing constraints rather than add capability. That is the repair-first thesis holding up under the evidence: the system doesn't need new loops; it needs its readers wired to its writers.
