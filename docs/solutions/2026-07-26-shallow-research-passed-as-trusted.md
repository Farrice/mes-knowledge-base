---
name: shallow-research-passed-as-trusted
problem_signature: "Ad-hoc Workflow research swarms run single-pass on search snippets with self-verified evidence and no depth floor binds them, so reconnaissance ships as decision-grade insight through finalize"
domain: system
tags: [research, depth-gate, governance, swarm, quality-gate, verification]
date: 2026-07-26
status: active
session: "ledger-caa55f1e-d179-4eea-9b5d-af76c6e46aae.json"
---

## Problem


A 12-agent, 1.5M-token offer-rederivation swarm (2026-07-25) produced strategy recommendations Farrice was about to bet his runway on. He caught it as shallow from the outputs alone. It had passed finalize at composite 8.33 with Factual Grounding 9.

Measured after the fact, the failure was NOT breadth: that run pulled 87 distinct sources across 79 domains. The failure was that **zero of those URLs survived into the decision artifact** (`RESULTS.md` scores 0 sources / 0 domains against the gate), the evidence was snippet-depth rather than page-depth, it ran a single pass, and every VERIFIED label was self-assigned by the agent that found the claim.

## Root Cause

Five stacked failures, any one of which would have been survivable alone:

1. **Brief guards pointed the wrong way.** The swarm brief pre-committed against overrun ("one sitting," "no token burn") and never against shallowness — no fetch mandate, no round minimum, no source floor.
2. **The adversarial phase attacked conclusions and trusted evidence.** Path-killers stress-tested the three offers; nobody attacked the six sweeps beneath them.
3. **Ad-hoc Workflow research answered to no gate.** `research-protocol.md` demanded 15 sources for deep and `research_quality_gate.py` existed, but both bound only the `research.py` path. Workflow swarms bypassed every deterministic floor.
4. **Finalize measured URL-having, not coverage.** No dimension existed for sources-per-question, full-page reads, or rounds run, so a reconnaissance sweep laundered into "trusted insight."
5. **The engine itself was structurally shallow.** `tavily_extract()` (full-page reads) sat as dead code with ZERO callers; claims were 400-char snippets or page titles; verification capped at top 6-8 claims; standard depth got zero gap-fill rounds; depth config had drifted across 3+ files (code deep=6 sources vs the protocol's 15); Playwright appeared in no research workflow, so JS-rendered primary sources were structurally unreachable.

## Approach That Worked

1. **Build one depth contract** — `execution/research_depth.py`: sources/domains/agents/gap-rounds/verify/extracts per tier. Deleted the three drifted local copies; `native_floor.py`, `research_personas.py`, `swarm_conductor.py` now import from it, and `directives/research-protocol.md` defers to it.
2. **Wire the dead code into the engine** — `tavily_extract` called inside `run_floor` on top URLs round-robined across domains; extracted pages upgrade their finding's claim from snippet to page content; snippet-only sources count HALF toward the source floor.
3. **Make failure loud** — `research.py` at deep/max: DEGRADED becomes exit 2 + `acceptable:false` + a RECON-GRADE banner naming the unmet floor. No more quiet passes.
4. **Scale verification with claims and make it independent** — both workflow JS engines now verify ALL load-bearing claims (cap 20), refuters are agents that did NOT find the claim, REFUTED claims are dropped rather than labeled.
5. **Restore the rounds** — gap-fill at standard=1, deep=2, max=3 (standard previously got zero, so "standard" research was single-pass by design).
6. **Add the Playwright primary-source lane** — declared `primary_sources` plus `PRIMARY-SOURCE-BLOCKED:` pickup from sweep agents, so JS-rendered and login-gated pages get read instead of silently dropped.
7. **Make the floor bind the ARTIFACT, not the pipeline** — `research_quality_gate.py --depth <tier> --receipt` validates any research file from any origin and emits a receipt JSON.
8. **Wire the receipt into finalize** — `chain_runner.py finalize --depth-receipt`; a Research-type finalize without a PASSING receipt caps Factual Grounding at 6. Ungated research ships with a `⚠️ RECON-GRADE — not decision-grade` banner.

## Dead Ends

- **Trusting the written standard.** `research-protocol.md` already said deep = 15 sources and had said so for months. Documentation never stopped a single shallow run; only the exit code did.
- **Assuming the fix was "more sources."** Measurement disproved it — round 1 had 87 sources and still failed. Chasing source count would have fixed nothing.
- **Rebuilding `deep_research_engine.py`'s title-as-claim path.** Explicitly left alone as legacy; the fix routes around it rather than expanding scope.
- **Un-archiving the `.claude/agents/deep-research.md` (deleted — archived agent, no longer on disk) agent** (it had Playwright but no fan-out). Rejected: violates the no-named-subagents binding. The Playwright capability was rebuilt inside the workflow instead.

## Verification

- Fixtures: 5 sources @ deep → DEGRADED · 5 snippet-only @ standard → 2.5 effective sources, DEGRADED · 16 full-page @ deep → REAL · `research.py ingest --depth deep` on thin findings → exit 2 · `--depth quick` regression clean (52 sources, REAL, exit 0).
- **The incident artifact fails the new gate**: `research_quality_gate.py validate RESULTS.md --depth deep` → exit 1, "DEPTH CONTRACT UNMET for deep: 0 sources / 0 domains (contract: 15 sources / 6 domains)."
- **Proof run on the fixed stack**: 296 distinct sources / 155 domains vs 87/79 (~25 vs ~14.5 per question), with gap-fill wave executed and the Playwright lane returning live Meta Ad Library data (13 brands with 15+ active ads, exact counts) that the old stack structurally could not reach.
- **The gate is not rubber-stamping**: the new findings PASS the depth contract and still FAIL overall on 42% provenance attribution.

## Weaker-Model Trap

A cheaper executor will read "make research deeper" and add more search queries or more agents. That is the trap this card exists to prevent: **breadth was never the deficiency.** The four things that must survive any re-implementation are (a) full pages, not snippets, with snippets weighted half; (b) at least one gap-fill round, because single-pass research is reconnaissance; (c) verification by an agent that did not find the claim, since finder-labeled VERIFIED is a self-report; and (d) the floor binding the artifact rather than the pipeline, because a gate with a bypass is a suggestion. A second trap: the executor may "fix" a failing gate by lowering the floor in `research_depth.py`. The floors mirror `directives/research-protocol.md` — moving them down silently re-creates the exact drift (code deep=6 vs protocol 15) that caused the incident.

## Re-solve guard

Before "fixing" shallow research again: (1) `python3 execution/research_depth.py --json` — the contract exists, extend it rather than forking new floors; (2) any research artifact gets `research_quality_gate.py validate <file> --depth <tier> --receipt` and finalize gets `--depth-receipt` — if a run bypassed this, the bug is the bypass, not the floors; (3) rerun the fixture battery in Verification above after touching `native_floor.py` or either workflow JS engine.

## Pointers

- `execution/research_depth.py` · `execution/native_floor.py` · `execution/research.py` · `execution/research_quality_gate.py` · `execution/chain_runner.py` (Step 2.4)
- `.agent/workflows/swarm-research.workflow.js` · `.agent/workflows/deep-research-swarm.workflow.js` · `.agent/workflows/swarm.md` § DEPTH CONTRACT
- `directives/research-protocol.md` (now defers to the contract)
- Incident artifact: `_active/offer-strategy/offer-rederivation-2026-07-25/04-deliverables/RESULTS.md` (RECON-GRADE banner + FAIL receipt) · proof: `DEPTH-FIX-PROOF.md` (same folder) · corpus: `.tmp/research/offer-validation-deep/`
- Plan + five-failure autopsy: `~/.claude/plans/and-if-you-re-able-valiant-zebra.md`
