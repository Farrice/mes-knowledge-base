---
date: 2026-07-24
session: loop-engineering-integration
tier: operator-guide
status: enriched
---

# Loop Engineering Integration — What We Built 2026-07-24 and How to Use It

> One session took "should we adopt loop/compound engineering?" from wayfinder map → receipt-carrying research → 12-loop evidence audit → all-12 GO → every candidate shipped and live-fire verified, then added the act-then-veto memory lane and hard-coded the Opus 5 executor registry. Decision record: `_active/harness/loop-engineering-integration/04-deliverables/LOOP-ENGINEERING-INTEGRATION-BRIEF.md` · method card: `docs/solutions/2026-07-24-loops-die-at-the-last-mile.md` · full paper trail: `_active/harness/loop-engineering-integration/wayfinder/MAP.md`.

## ⚡ If you only read 10 lines

- Your recurring cost is ONE surface now: the morning `/cos` brief — approve/reject pending rules and veto/bless ⚡ auto-activations with the prefilled commands shown there.
- Rules scored ≥9.0 auto-activate weekly as labeled PROVISIONAL (taste/voice/brand NEVER auto): veto = `python3 execution/memory_review.py veto <id>`, confirm = `... bless <id>`.
- The rubric is ARMED (`rubric_load_bearing: true`, 84/85) — every finalize now checks against your calibrated precedent.
- Fleet is green: 69 pass / 0 fail / 4 skip; finalize-debt truth: 817 events = 92 sessions (8.9x noise) — do NOT flip `LEDGER_ENFORCE` until that's deduped.
- Phase-2 queue deduped 132→20; monthly cycle emits ONE card (T1 if grounded, T2 parks for you); 21-day cadence guard.
- launchd jobs are sleep-proof (`RunAtLoad` catch-up on evolution-auto + outcome-chase — both idempotent).
- Offer/pricing work auto-routes through `/offer-redteam` (override `--no-redteam` only with a same-cycle receipt).
- Wargames bank failure-maps to `docs/solutions/` (step 8) — a wargame without a card is unfinished.
- Standing refusals (brief §refusals): no Every plugin, no Ralph, no append-to-CLAUDE.md compounding, no human-optional review, no new loops without a named consumer.
- Re-audit due **~2026-08-24**: rerun the 12-loop table; compounding = signal captured AND behavior changed, with file/log receipts.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/cos` | Morning brief incl. 🧠 Memory Review (pending + provisional lines, prefilled commands) | Daily; the one ritual left |
| `python3 execution/memory_review.py list / approve / reject / veto / bless <id>` | Rule queue actions | A /cos line surfaced a rule |
| `python3 execution/memory_review.py auto-promote` | Provisional promotions ≥9.0 (taste-guarded) | Runs Sundays via memory_weekly.sh; manual re-run is safe |
| `python3 execution/session_ledger_report.py --write` | Finalize-debt trend (dedupe + weekly table) | Before any LEDGER_ENFORCE decision |
| `python3 execution/eval_harness.py status` | Calibration state | Verifying the rubric stays armed |
| `python3 execution/verify_fleet.py run` | 73-contract health sweep | Suspected breakage; feeds the parked metric-ratchet trigger |
| `python3 execution/skill_auditor.py audit` | Tier report + CORE DRIFT + CONTEXT SIZE RATCHET | Monthly; flags CLAUDE.md growth |
| `python3 execution/verify_born_intent_drift.py --bless` | Re-baseline after deliberate skill/workflow edits | Fleet shows born-intent DRIFT on work you meant |

## The mental model

1. **Loops die at the last mile.** The audit found 4/12 compounding, 7 open, 1 dead — every failure was a working capture arm with no closing arm (unread logs, un-run rituals, sleep-lost schedules). Repair = wire a deterministic consumer; never add a producer without naming its reader.
2. **Act-then-veto beats gatekeeping for operational learnings.** High-scored system rules activate provisionally and are cheap to reverse; your taste stays the irreplaceable filter for everything voice/brand/content — a deterministic keyword guard enforces the split.
3. **Verification is the load-bearing primitive** (canon + local evidence agree). The armed rubric, green fleet, and receipts-on-both-arms metric are the spine; "2–3x" style numbers stay banned as targets.
4. **Fable conducts, Opus 5 heavies, Sonnet 5 grinds** — hard-coded in the Executor Model Registry (orchestration-doctrine.md); per-model prompting deltas in model-notes.md. Under-seating Opus 5 is now the waste.

## Capabilities shipped

### Act-then-veto memory lane
**What:** `memory_weekly.sh` runs `auto-promote` after Sunday distill; rules ≥9.0 without taste keywords promote unpinned with a `[PROVISIONAL …]` content label; /cos surfaces each with bless/veto commands. **When NOT to:** never widen the taste-guard keyword list downward; voice/brand rules stay manual forever. **Honest edge:** a wrong operational rule can act for up to a week before veto — the /cos surface is the safeguard; live-fire tested (promote→surface→veto→clean) but not yet through a real Sunday cycle.

### Phase-2 consumer + honest queue
**What:** `evolution_orchestrator.py` monthly arm emits one mission card for the highest-pressure queue skill; `queue_phase2()` dedupes 1 row/skill/7d; 21-day done-guard holds cadence. Card #1 resolved REFUSE-EVOLVE (no ground truth + stale signal) — the refuse path firing IS the loop working. **Honest edge:** existing queue rows carry stale `grounded` flags from queue time; fresh rows are correct.

### Verification spine (armed)
**What:** rubric load-bearing → R2 precedent gate live in `chain_runner.py`; finalize demands named anchors for ≥8 scores. **Worked example:** this session's own finalize was rejected once for unnamed anchors — the gate works on its author. **Honest edge:** EVAL-011 placeholder still unfilled (84/85).

### Deterministic closers (the 10 repairs)
Sleep-proof plists · trial verdict recorded (extended to 08-07) · session-ledger report in health-metrics · offer-gate binding · injection hit-rate log · wargame→solutions banking · steering escalation (≥2 misses) · context-size ratchet (baselines: CLAUDE.md 18,943B / MEMORY.md 20,111B) · /cos memory surface · fleet triage. Per-candidate detail: gap map in `_active/harness/loop-engineering-integration/research/`.

### Metric-ratchet pilot (ARMED, parked)
**What:** overnight keep-if-better/revert-if-worse run, full terms banked in `.agent/mission-queue/parked/card-metric-ratchet-pilot-ARMED.md`. **Trigger:** ≥5 genuinely failing fleet contracts, or a Farrice-named deterministic metric. **When NOT to:** while the fleet is green — ratcheting a green metric is loop-sprawl (standing refusal #3).

### Executor Model Registry (Opus 5 staple)
**What:** hard-coded seat→model table in `orchestration-doctrine.md` + per-model prompting deltas in `model-notes.md`: Opus 5 heavy executor (delete verification scaffolding, cap subagent spawns, sweep effort down), Sonnet 5 grunt (literal follower, +30% tokenizer, coverage-first review prompts). **How it stays fresh:** on any model launch, verify via the claude-api skill and update Registry + model-notes in one commit.

## Composition (options, not pipeline)

| Stack with | When it earns its cost |
|---|---|
| `/weekly-closeout` | Still the deep ritual; the repairs made its absence non-fatal, not its presence worthless |
| `/wargame-run` | Now compounds — every run banks a retrievable failure-map card |
| Aug-24 re-audit (method in `docs/solutions/2026-07-24-loops-die-at-the-last-mile.md`) | The receipts check: target ≥8/12 COMPOUNDING vs 4 at baseline |
