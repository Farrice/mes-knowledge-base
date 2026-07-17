# Frontier Elevation Blueprint — Antigravity OS v-Next

## Context

Farrice invoked `/go` with a vision-level mission: take everything built in this workspace
(900+ skills, 222 expert front doors, the Chain, the memory stack, deterministic hooks,
orchestration doctrine) and elevate it to **truly frontier / world-class** at knowledge and
creative work — AND make it **portable and owned**: deployable on Claude Code, Codex,
Antigravity, or any future model/platform, with the option to productize it as IP or
install client-specific versions built from this base.

### Mission Card (from /go Stage 0)

```
MISSION CARD
Intent: Design the frontier-elevation + ownership architecture for the Antigravity OS
Serves: revenue-scale-20-30k (platform leverage) + revenue-5k-incumbency (as lens, not brake) ⚑ Farrice ruled: build IS the priority
Felt standard (VERBATIM, updated at approval): "a real shot at being a one-person army…
  who could get like a billion dollars in revenue at some point, or have the skills and
  capabilities to achieve some extraordinary and remarkable things. I want to aim for the
  stars! I don't want us to aim for something low, generic, or AI slop. That's what I've
  been building this to be against." Plus: "I feel that's my fault and being the
  bottleneck" — the blueprint engineers the bottleneck out of the system, never the
  operator out of the judgment seat.
Pattern: wayfinder (decisions before deliverables) → then fleet per approved wave
Loads: /system-audit ownership (control-plane), orchestration-doctrine, portability OS
Gates: plan-mode approval (this doc), then per-wave T2 gates
Tier: T3 — waiting for Farrice's nod on this plan
Cost: $0 (design phase)
```

### Farrice's locked answers (2026-07-17)

1. **Sequencing**: The build IS the priority. Revenue-first filter applies as a *lens*
   (prefer pieces that also compound the sprint) but never as a brake.
2. **Frontier means all four**: output-quality ceiling, leverage/throughput, compounding
   intelligence, AFK autonomy.
3. **Ownership**: model-agnostic kernel + productize-ready (sellable IP / client-installed
   versions derived from this base).
4. **Felt gaps**: all four (quality still needs him, power sits unused, doesn't run without
   him, not yet translating to income).
5. **Mid-turn addition**: elevation must cover the asset base itself — core skills,
   workflows, agents, experts — not only harness plumbing.
6. **Model seating (Farrice, mid-turn)**: Fable does all high-level orchestration;
   Opus and Sonnet execute. Matches Conductor Ladder doctrine — bake this seating into
   every wave's execution plan.

## Evidence base

### Agent A findings — portability layer (LANDED 2026-07-17)

- `execution/platform_compiler.py` v1: drift-detect only (SHA baseline over 6 constitution
  files), lint invariants, observe-only in evolution daily. **v2 aspiration in its own
  docstring: generate siblings from canon + overlays.**
- Shared constitution spine nearly empty: `directives/constitution-core/` = 3 blocks
  (~6 lines). ~95% of CLAUDE.md/GEMINI.md/AGENTS.md/constitution.md is forked prose.
- Codex parity: `.codex/hooks.json` hook mirror PROVEN live (cost gate, ledger, router);
  `codex_dynamic_workflow.py` plans/receipts fleets but **never spawns real subagents**.
- Harness-locked value ≈15-20%: physical hooks (.claude/settings.json, 16 hooks) +
  real parallel subagent fan-out + native Skill auto-load. Everything else (337 execution
  scripts, 384 skills, 1,705 workflows, memory, Chain) is plain files/Python — portable.
- 5 gaps to "deploy anywhere with ownership": (1) empty shared spine / hand-sync,
  (2) enforcement parity only Claude+Codex (Gemini/IDE = prose), (3) no off-Claude
  parallelism, (4) unretired forks (~/.codex/skills broken ports, Codex Antigravity clone),
  (5) Antigravity IDE unverified, Gemini CLI dead, MCP auth non-transferable.
- Existing roadmaps: CODEX-PARITY runbook, platform-bakeoff capability-matrix + PROTOCOL,
  compiler v2 note, OPERATING-CODEX-AND-CLAUDE.md.

### Agent B findings — audit-backed weakness map (LANDED 2026-07-17)

**Through-line: the scaffolding keeps outpacing the truth-loops that keep it honest.**

Top weaknesses (receipts in `_active/system-audit/`, `evolution_store/`, `.agent/sessions/`, `docs/solutions/`):
1. Quality loop uncalibrated: `evolution_store/ground_truth/eval_set_v1.jsonl` = 44 entries,
   ZERO human_calibrated (needs ≥15 to become load-bearing). April's #1 fix, still open.
   94-99% of finalizes score 8+ (implausible) with no calibrated judge.
2. Skill-tier collapse: `skill_audit_2026-07-16.md` — 367 skills, A=4 (was 56 in April),
   324/367 fail ≥2 heartbeat checks. Growth turned dilutive. Gate is punitive, nothing repairs.
3. Blind-pass latch rubber-stamped: `blind_pass_overrides.jsonl` — `--skip-blind-pass` fired
   on essentially every recent extraction.
4. Enforcement in permanent shadow mode: every observe-log entry `would_block:true,
   enforce:false`; learning-debt streak-3 unresolved. Compass-not-cage became no-cage.
5. Steering Next-Moves ~100% missed per `steering-observe.jsonl`.
6. Top recurring failure cluster: concurrency/merge silent data loss (6+ solution cards
   Jul 11–16) — direct blocker for Swarm Apex.
7. Routing hijacks recur post-Wave-1 (control-router-hijacks-deliverable-missions 7-13).
8. Evolution loop logs but doesn't learn: quality→routing weight loop never wired
   (Apex PLAN.md:55); deep-research swarm verifier never fires.

**Unshipped plans already written**: Harness Apex `_active/harness-apex-2026-07-07/PLAN.md`
Waves 3 (Structured Mission Contracts), 4 (Model Portability), 5 (Universal Maker /make)
all QUEUED. Swarm Apex `_active/swarm-apex-2026-07-07/PLAN.md` 4 build sessions unshipped.
COS v3 Phase 6 unverified. Elevation Track E5 harvest roadmap open.

**Confirmed STRONG — never rebuild**: Knowledge Compiler, tiered context loading +
Recall Tier-1.5, factual-grounding veto, jw-engine worker envelope (propagate it),
BM25 find_skill router + routing_enforcer BINDINGS (surgical patches only),
budget-gated APIs.

### Farrice's second-round answers (2026-07-17)

7. **Enforcement**: graduated flip — gates go live one at a time, 1-week trial each,
   documented override always available (compass-not-cage preserved).
8. **Skill triage**: REPAIR EVERYTHING (all 324 failing skills). No archiving. Sequenced
   core → revenue-serving → active-project → long-tail via renaissance_queue.
9. **AFK**: T1 + drafts. Two added requirements (verbatim intent): outputs stored in
   Google Drive / Google Docs so everything is findable from his phone, not only local;
   and "proper orchestration of the models baked in so we're not running up my usage and
   burning through tokens haphazardly."

---

### Scope ruling (Farrice, at approval — WIDENED)

This is NOT a knowledge/creative-work OS. It is an **operator OS for the whole life**:
work, personal, client-facing, goals, task objectives, hobbies, interests. The one-person-
army standard governs every wave. Concretely:
- The goal spine already carries non-business goals (father-presence, health-rebuild,
  bowling-first-place) — every wave's machinery (missions, AFK runs, COS receipts, /make)
  must serve ALL goals in `.agent/cos/goals.json`, not just revenue threads.
- **Extraction engine generalizes to ANY discipline** (emphasized lever): the same MES
  blind-pass rigor that extracts marketing minds must extract any world-class capability
  Farrice wants — a bowling coach, a sleep scientist, a negotiator, a CFO, a chef.
  Wave 6's craft-extraction variant is the vehicle; Wave 3's repair standard is the floor.
- The modality registry (Wave 6) is open-domain by contract: any deliverable, any craft,
  any life domain routes through one door to expert + toolchain + verifier.
- Anti-slop is the founding identity of the system ("that's what I've been building this
  to be against") — the calibrated judge (Wave 1) and prose/blind-pass gates are what
  make "aim for the stars" enforceable rather than aspirational.

# THE PROGRAM — 8 waves, Fable conducts, Opus judges, Sonnet executes

**Ordering thesis (Opus architect, confirmed):** fix the tree, then the judge, then the
gates, then unleash fleets. A repair-fleet against an uncalibrated judge would manufacture
324 plausible-looking passes — the exact disease that collapsed A-tier 56→4. Concurrency
firewall precedes everything because fleets on a shared tree silently lose work today.

**Token discipline (global, per Farrice):** Fable appears only as conductor (compile,
route, merge, verify-sample). Opus only for judgment-grade work (schema design, verify
sampling, calibration anchors). Sonnet for ALL volume execution (skill repairs, ports,
fixture runs). Overnight fleets are Sonnet-heavy by construction. Every wave's kickoff
names its seating before spawning.

## Wave 0 — Concurrency Firewall (1 session)
No fleet runs until concurrent writes are impossible-by-default.
- Make `execution/session_lock.py claim` mandatory in `/go` / `/extract-forge` / swarm
  kickoffs (SessionStart hook in `.claude/settings.json`; mirror in `.codex/hooks.json`).
- Codify merge SOP from the two 2026-07-15 solution cards into
  `directives/merge-discipline.md` (Accept→Repair→Dedupe→Fidelity-check).
- Fleet rule: workers write only to `.tmp/<session>/`; conductor merges serially through
  deterministic gates.
- **Accept:** second lock-claim on same tree exits 1 (fixture); 3-worker fan-out produces
  zero cross-writes to canonical paths.

## Wave 1 — Ground Truth & Calibrated Judge (2 sessions, Farrice-gated)
The judge must tell good from bad before any gate means anything.
- **CORRECTED 2026-07-17 (seeder finding):** gate field is `calibrated_by_human`; 27/44
  already true; live threshold = `max(10, 80% of total)` = 35. Fastest path: RATIFY 8 of
  the 17 pending in-set entries (EVAL-029–044) — appending un-calibrated rows RAISES the
  bar, ratifying nets +1.0 each. 30 pre-scored seeds SHIPPED
  (`evolution_store/ground_truth/seed_candidates_2026-07-17.jsonl` + `REVIEW-PROTOCOL.md`,
  honest spread 11 FAIL / 8 MARGINAL / 11 PASS) for coverage depth after arming.
  Farrice's job is REVIEW, not authoring — three ~20-min batches.
- Once ≥15: turn `chain_runner.py finalize` score-inflation guardrail from advisory to
  blocking; nightly calibration-drift check in `evolution_orchestrator.py`.
- **Accept:** human_calibrated ≥15; re-scored last 50 finalizes show <60% at 8+; judge
  agrees with Farrice ≥80% on 5-entry held-out set.

## Wave 2 — Enforcement Live + Blind-Pass Integrity (2 sessions)
Graduated flip out of shadow mode, per Farrice's call.
- Flip order (1-week trial each, revert flag documented): (1) routing BINDINGS,
  (2) blind-pass latch, (3) finalize/ledger debt, (4) steering loop. Every gate keeps a
  logged override — compass, not cage.
- Blind-pass unfakeable: requires provenance-verified reference corpus; skips land in a
  visible ledger surfaced in the COS morning receipt.
- Wire quality→routing weights (Apex W1.3, never wired): composite <7 weights the route
  down in routing learning. Consult BINDINGS upstream of fuzzy ranking.
- **Accept:** 20-query misroute regression passes; a known-thin extraction FAILS finalize
  without override; enforcement ledger shows real blocks.

## Wave 3 — Asset Renaissance: repair ALL 324 skills (6-10 sessions, mostly AFK-able)
Farrice override: repair everything, no archiving. Sequenced, not triaged:
- **Lane order:** PRODUCTION_CORE (~25) → revenue-serving cluster (claim-safe/
  health-performance content skills feeding the Aug-12 sprint) → active-project skills →
  long tail, drained via `renaissance_queue.py`.
- **Repair fleet pattern:** Opus conductor scouts + batches; one Sonnet executor per skill
  under the jw-engine worker envelope, writing to `.tmp/<session>/`; task = restore the
  6 heartbeat items (source-ledger, ≥5 sourced anti-patterns, ≥3 verbatim exemplars,
  recognition test, named-entity floor, Output Schema + Quality Gate).
- **File-not-summary gate:** `renaissance_audit.py` + `skill_auditor.py` run on the actual
  file; worker summaries never trusted. Opus verifies 1-in-5 against the Wave-1 judge;
  blind-pass on every regenerated exemplar.
- **Apex Wave 4 folds in here:** every repaired genius.md gains the mandatory
  model-calibration block (ben-watkins exemplar) — ships per-repair, not as separate pass.
- **Long-tail lanes run as overnight T1 fleet work (Wave 7 synergy) — Sonnet-only.**
- **Accept:** core + revenue skills 6/6 heartbeat + calibration block; A-tier recovers on
  the CALIBRATED judge; zero repaired skills fail re-audit; queue drains to empty.

## Wave 4 — Structured Mission Contracts + Fleet Plumbing (3-4 sessions)
Apex Wave 3 + Swarm Apex, shipped.
- `directives/worker-envelope-standard.md` (propagate jw-engine envelope) + per-stage
  advisory `model_tier` (judgment→highest, execution→inherit, mechanical→cheapest — this
  is Farrice's token-discipline requirement made deterministic).
- JSON schemas between JCC/supercomputer/swarm stages; validator hard-fails and
  re-dispatches on missing/contradictory outputs (deliverable-paths-not-self-report).
- Pilot `strike` as native Workflow script head-to-head vs prose-JCC; migrate on evidence.
- **Accept:** validator rejects a deliberately-broken payload; pilot beats prose path on
  completeness + fabrication count.

## Wave 5 — Kernel/Distro Split + platform_compiler v2 (3 sessions) — OWNERSHIP
- **Three layers:** (a) portable KERNEL — Chain, memory stack, knowledge_compiler,
  execution spine, and a platform-neutral hook CONTRACT (grow `directives/constitution-core/`
  from 3 blocks to the real shared spine, compiled to `.claude/settings.json` /
  `.codex/hooks.json` / future adapters); (b) PERSONAL layer — voice, clients, goals,
  taste ledgers → `personal/`; (c) CLIENT overlay template + installer story
  (`distro/client-overlay-template/`) — kernel + overlay composes into a client-specific
  build. This is the productize-as-IP foundation.
- **platform_compiler v2:** promote from drift-detect to generate-siblings-from-canon.
  Block schema: shared-invariant blocks + platform-adapter blocks + overlay blocks.
  Keep ALL v1 rails (canaries, REF_PATTERN checks, constraints-last) as pre-write gates.
  Pilot on AGENTS.md (the proven-live sibling) before Gemini/IDE; keep hand-authored
  fallback until 3 clean regenerations.
- **Accept:** v2-regenerated AGENTS.md passes v1 check+lint; forked prose share drops
  materially from ~95%; scratch client overlay produces a valid build.

## Wave 6 — Universal Maker, Any Domain (2-3 sessions)
Apex Wave 5, widened per the scope ruling: `directives/modality-registry.md` (modality →
toolchain + expert + verifier) covering business AND life domains; thin `/make` front door
through the Chain; and `craft-extraction` MES variant that extracts ANY world-class
capability — "world-class financial model," "McKinsey-grade slide," but equally "PhD-grade
bowling coaching plan," "elite sleep protocol," "top-1% negotiation prep" — same
blind-pass discipline regardless of domain.
- **Accept:** `/make` on 3 modalities (at least one non-business/personal-domain) routes
  to the right verifier and passes it; one craft-extraction artifact survives side-by-side
  blind-pass vs a real apex artifact.

## Wave 7 — AFK Autonomy + Drive Sync (2 sessions)
- launchd mission-runner (mirror `com.antigravity.evolution-auto` pattern) executes queued
  `/go` Mission Cards overnight: **T1 auto + content as DRAFTS only** — nothing publishes,
  sends, or spends. T2/T3 park for morning approval. `session_lock` held for the run.
- **Google Drive/Docs sync (Farrice requirement):** overnight drafts + morning receipts
  push to a structured Drive folder via the existing `gws` CLI (OAuth already wired;
  7-day-expiry fix documented; claude.ai Drive MCP `create_file` as fallback) — everything
  phone-retrievable, never local-only.
- Morning COS receipt: outcomes, deliverable paths (local + Drive links), token cost,
  blind-pass-skip count, parked T2/T3 decisions.
- **Accept:** seeded overnight T1 mission completes under lock, touches nothing above T1,
  drafts appear in Drive, morning receipt carries real paths + cost.

## Sequencing & effort
Waves 0→1→2 strictly ordered (~5 sessions, 1-2 weeks incl. Farrice's 3×20-min calibration).
Wave 3 starts after 2 and runs long (its long tail becomes Wave 7's overnight workload).
Waves 4-5 parallel-safe after 2. Wave 6 after 4. Wave 7 core can ship early (after 0)
for T1-only work, full drafts-mode after 2. Total ≈ 20-24 working sessions.
Revenue lens honored: Wave 3 lane 2 (sprint-serving skills) lands inside the sprint window.

## Riskiest assumptions & de-risks
1. Farrice completes calibration → auto-seed so it's review-not-author, 3×20-min batches.
2. Repair fleet re-inflates the gate → deterministic audit is sole merge arbiter, Opus
   1-in-5 verify vs calibrated judge, blind-pass on regenerated exemplars.
3. compiler v2 breaks derived constitutions → v1 rails as pre-write gates, AGENTS.md-only
   pilot, hand-authored fallback until 3 clean regenerations.

## Never rebuilt (audit-confirmed strong)
knowledge_compiler.py · tiered context loading + Recall Tier-1.5 · factual-grounding veto ·
jw-engine worker envelope (propagated, not replaced) · BM25 find_skill + routing_enforcer
BINDINGS (surgical patches only) · budget-gated APIs · launchd/evolution infra.

## Verification (program-level)
- Each wave has deterministic acceptance criteria above; no wave closes on a summary —
  fixtures and audits run on real files.
- After Waves 1-2: `python3 execution/chain_runner.py` finalize distribution re-checked
  (inflation broken); observe-log shows real blocks.
- After Wave 3 lane 1: `python3 execution/renaissance_audit.py` 0-fail on PRODUCTION_CORE.
- After Wave 5: `python3 execution/platform_compiler.py check && lint` green on generated
  siblings; scratch client-overlay build boots on Codex (the proven second harness).
- After Wave 7: one real overnight run reviewed in the morning COS brief with Drive links.
- Mission logged both ends in `.agent/missions.jsonl` per /go Stage 2.5.
