# Fleet Conductor Doctrine — run the repair fleets without Fable

**Written 2026-07-17 by the Fable conductor in its final access window.** This banks the
judgment that conducted Wave 3 Lanes 1–3 (46 skills to 6/6, zero fabrications surviving
to push) so an **Opus conductor runs steady-state** and Sonnet keeps executing volume —
per the Conductor Ladder (`directives/orchestration-doctrine.md`): strongest available
model conducts; when Fable is gone, that's Opus. Sonnet never conducts a fleet.

## The one-page batch lifecycle (proven at 16–17 wide)

1. **Claim + arm** — `session_lock.py claim "<mission>"`; write `.agent/fleet-active.json`
   sentinel `{"mission", "claimed": epoch, "protected": ["skills/"], "ttl_min": 150}`.
   Heartbeat the lock every merge wave. No sentinel = no dispatch, ever.
2. **Stage** — next batch from `.agent/renaissance-lane4-queue.json`; per skill run
   `skill_auditor.py check --skill <ID> > .tmp/<batch>/audit-<ID>.txt`; copy the
   hardened envelope (`.tmp/wave3-batch4/ENVELOPE.md` is canonical — sed the batch path).
   Never edit the envelope's rules; they each encode a caught failure.
3. **Dispatch** — one Sonnet worker per skill (general-purpose agent, model sonnet),
   prompt = 3 sentences pointing at envelope + audit file + exact absolute output dir.
   All workers in one message. ~8–12 min per batch wall-clock.
4. **Merge serially as workers return** — `python3 execution/fleet_merge.py .tmp/<batch> <ID>`
   (hollow-delivery guard + gate built in; exit 0 = gate-clear). Commit per skill:
   `feat(wave-3): <ID> to 6/6 — lane 4 fleet, gate-verified (<one honest caveat>)`.
   The worker's ≤120-word return is a ROUTING HINT ONLY — the gate and fleet_merge
   decide, never the summary.
5. **Opus adversarial verify, ≥1-in-5 per batch** — pick the riskiest deliveries:
   brand-new genius.md > cross-topic quote borrowing > negative-claim-heavy ledgers >
   biggest diffs. Verify prompt MUST include: (a) open cited files, byte-exact quote
   check on ≥8 anchors; (b) **spot-check UNCONFIRMED/absence claims — confirm the
   material really ISN'T there** (the #1 fabrication vector, fired twice, both caught
   only here); (c) deletion scan via git diff --stat. Verifier says CLEAN or names the
   exact violation. Fix as conductor (sentinel down or via cp), re-run the gate,
   commit the fixes in ONE `fix(wave-3): Opus adversarial verify corrections` commit.
6. **Close** — drop the sentinel, push, heartbeat, update
   `.agent/renaissance-lane4-queue.json` (remove completed batch or track a cursor),
   append `.agent/missions.jsonl`. Push rejections on this shared tree are usually the
   sibling-push race: if `git rev-list --left-right --count origin/main...main` shows
   `0 0` after fetch, the work IS on remote — verify, never force.

## The five failure shapes (full card: docs/solutions/2026-07-17-repair-fleet-poc-three-failure-shapes.md)

| # | Shape | Caught by | Countermeasure now standing |
|---|---|---|---|
| 1 | Instrument false-negative (auditor regex) | worker reading auditor source | `Output Contract` accepted; re-census after big repair waves |
| 2 | Quarantine path drift | merge from contract path only | fleet_merge copies from contract path; path claims are claims |
| 3 | False absence claim ("0 bytes", "no source exists") | Opus verify | envelope rule 2; verify prompt checks negatives; `wc -c` not `wc -l` |
| 4 | Workers running git writes | reflog forensics | envelope git-read-only rule; conductor-only commits |
| 5 | Hollow delivery (paperwork, no payload) | empty-dir check | fleet_merge exit 3 on empty; never merge a summary |

Shape 3 recurs in disguise (lazy-UNCONFIRMED: labeling something unverifiable without
searching). Zero fabrications have survived to push across 46 skills — because every
layer assumes the layer below it lies.

## Seating (Farrice's standing token-discipline ruling)

- **Conduct** (batch decisions, merge judgment, violation fixes): Fable while available,
  then **Opus**. Never Sonnet.
- **Execute** (repairs, ports, mechanical fixes): **Sonnet, always.**
- **Judge** (adversarial verify, calibration anchors): **Opus.**
- Never pin Opus (memory: opus-fallback-policy) — degrade a tier rather than stall.

## Wave 2 flip schedule (pre-built DORMANT — activation needs NO judgment)

One flip per week, each gated on the prior gate's week-1 review in `/weekly-closeout`
(read the gate's ledger, scan false positives, decide permanence):

| Due date | Gate | Activate by | Ledger to review |
|---|---|---|---|
| live now → 07-24 | routing_bindings | (live) `.agent/routing-enforce-trial.json` | `.agent/sessions/routing-enforce-log.jsonl` |
| 2026-07-24 | blind_pass | `active:true` in `.agent/enforce-trials/blind_pass.json` | `evolution_store/blind_pass_overrides.jsonl` |
| 2026-07-31 | ledger_debt | `active:true` in `.agent/enforce-trials/ledger_debt.json` | `.agent/sessions/observe-log.jsonl` |
| 2026-08-07 | steering | `active:true` in `.agent/enforce-trials/steering.json` | `.agent/sessions/steering-observe.jsonl` |

## Grading loop (R1 live advisory; R2+ needs Farrice)

`finalize --verdict SHIP|MARGINAL|FAIL --precedent EVAL-0XX` is live and advisory;
results accrue in `evolution_store/verdict_advisory.jsonl`. R2 (blocking) ships ONLY
after Farrice ratifies `_active/frontier-elevation-2026-07-17/04-deliverables/GRADING-LOOP-REDESIGN.md`
and a week of advisory data shows sane behavior. Spec + rollout table live in that doc.

## Hard rules that never bend

- **Additive only.** Never delete or rewrite passing content, workflows, or skills —
  Farrice's explicit standing instruction (2026-07-17): everything has purpose; improve,
  never remove. Cleanup candidates (e.g. `skills/_tmp_audit_diandra`) go to the removal
  ledger as PROPOSALS.
- **Files over summaries.** No wave, batch, or gate closes on anyone's summary.
- **One live writer per tree** (GOLDEN RULE) — lock before fleets; sibling races get
  verify-then-accept (docs/solutions/2026-07-15-concurrent-session-race-accept-repair-dedupe.md),
  never revert.
