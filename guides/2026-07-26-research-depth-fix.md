---
date: 2026-07-26
session: research-depth-fix
tier: operator-guide
status: enriched
---

# Research Depth Fix: What We Built 2026-07-26 and How to Use It

> Shallow research can no longer ship as trusted insight. A single depth contract (`execution/research_depth.py`) now governs every research floor in the system; full-page reads replaced snippets; verification scaled to all load-bearing claims by agents that didn't find them; and a depth gate binds the ARTIFACT rather than the pipeline, so ad-hoc Workflow swarms can't bypass it. Companion files: the autopsy sits at `docs/solutions/2026-07-26-shallow-research-passed-as-trusted.md`, the measured proof is `_active/offer-strategy/offer-rederivation-2026-07-25/04-deliverables/DEPTH-FIX-PROOF.md`, and the paste-ready external prompt is `DEEP-RESEARCH-PROMPT.md` in that same folder.

## ⚡ If you only read 10 lines

1. `python3 execution/research_depth.py --json` gives the one table every research floor now reads. Deep = 15 sources / 6 domains / 2 gap rounds / verify-all.
2. `python3 execution/research_quality_gate.py validate <file> --depth deep --receipt` gates ANY research artifact, from any origin, and emits a receipt.
3. `python3 execution/chain_runner.py finalize ... --type Research --depth-receipt <path>`. No passing receipt means Factual Grounding is capped at 6, automatically.
4. Snippets now count **half** toward the source floor. Full pages count whole.
5. At depth `deep`/`max`, DEGRADED is a hard fail: exit 2, `acceptable:false`, RECON-GRADE banner.
6. Verification is independent by construction: the agent that found a claim never verifies it. Finder-labeled VERIFIED = UNCONFIRMED.
7. Gap-fill rounds: standard=1, deep=2, max=3. Standard used to get zero, which made "standard research" single-pass by design.
8. JS-rendered / login-gated primary sources route to the Playwright lane instead of being dropped silently.
9. Any research shipped without a passing gate wears the RECON-GRADE banner. Shallow work may exist; unlabeled shallow work may not.
10. Every research-shaped swarm brief must carry the four guards in `.agent/workflows/swarm.md § DEPTH CONTRACT`.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/research_depth.py --json` | the full depth contract; `--depth deep` for one tier | before writing any research brief, or when you're tempted to invent a floor |
| `python3 execution/research.py "<q>" --depth deep` | unified research + honest receipt; exit 2 if under-floor | any real research question |
| `python3 execution/research_quality_gate.py validate <file> --depth <tier> --receipt` | quality report + `<file>.depth-receipt.json` | before trusting ANY research artifact, including one a swarm just wrote |
| `python3 execution/chain_runner.py finalize ... --depth-receipt <path>` | finalize with the depth cap lifted | finalizing a Research-type deliverable |
| `Workflow` with `deep-research-swarm.workflow.js` + `primary_sources: [...]` | multi-wave swarm with the Playwright lane armed | research where key sources sit behind JS or logins |

## The mental model

**Three ideas make the rest obvious.**

**Breadth was never the deficiency.** The incident run pulled 87 sources across 79 domains, which is respectable. It still produced untrustworthy work, because the evidence was snippet-deep, single-pass, self-verified, and, worst of all, **zero of those 87 URLs survived into the decision document.** Research quality is not how much you gathered; it's how much of it reached the person deciding.

**A standard that binds one pipeline is a standard with a bypass.** `research-protocol.md` had demanded 15 sources for deep for months. It bound `research.py` only, so every ad-hoc Workflow swarm walked past it. Floors must attach to artifacts, not to the code path that happened to have the gate.

**Gates must measure what the failure fakes.** Finalize scored Factual Grounding on URL presence, so shallow work laundered itself through URLs and scored a 9. The new gate measures sources-per-question, full-page reads, and whether verification actually ran, which are the things a shallow run cannot counterfeit.

## Capability 1: the depth contract

**What it is.** `execution/research_depth.py` holds one table: sources, domains, agents, fan-out, gap rounds, verification policy, and full-page extracts per tier. `native_floor.py`, `research_personas.py`, and `swarm_conductor.py` import from it; `directives/research-protocol.md` now defers to it in writing. Before this, those numbers lived in three files that had drifted: code said deep=6 sources while the protocol said 15.

**When to reach for it.** Any time you're about to write a number into a research brief. Read the contract instead of asserting a floor.

**When NOT to.** Don't edit the floors to make a failing run pass. That's the exact drift that caused the incident, and the Weaker-Model Trap section of the Solution Card calls it out by name.

**How to invoke.** `python3 execution/research_depth.py --json` (full table) or `--depth deep` (one tier).

**Honest edges.** `deep_research_engine.py` still carries a legacy title-as-claim path that was deliberately left alone, sitting outside the contract's reach.

## Capability 2: full-page reads and the half-weight rule

**What it is.** `tavily_extract()` had existed for months with **zero callers**, meaning the system knew full-page reads mattered and routed around the knowledge. It's now wired into `run_floor`: top URLs are round-robined across domains, extracted, and each extracted page upgrades its finding's claim from a 400-char snippet to real page content. Snippet-only sources count **half** toward the source floor.

**When to reach for it.** Automatic on any `research.py` run at standard or above.

**When NOT to.** `--depth quick` skips extraction by design (extracts=0); use it for single-claim sanity checks, not decisions.

**Worked example.** Fixture: 5 snippet-only sources at standard depth resolve to 2.5 effective sources and return DEGRADED. 16 full-page sources at deep return REAL.

**Honest edges.** Extraction caps at 20 URLs per call (tvly's ceiling) and fails soft: a dead `tvly` binary degrades to snippets rather than erroring, so watch the receipt's full-page extract count.

## Capability 3: loud failure

**What it is.** At `deep`/`max`, a DEGRADED result now exits 2, carries `acceptable:false` in JSON, appends the unmet floors to warnings, and prints a RECON-GRADE line. It used to return quietly and get consumed downstream as if it had passed.

**When to reach for it.** Automatic. Check exit codes when scripting around `research.py`.

**Worked example.** `research.py ingest --findings thin.jsonl --depth deep` → exit 2.

**Honest edges.** `quick` and `standard` still return 0 on DEGRADED, deliberately, since those tiers are explicitly not decision-grade.

## Capability 4: independent verification at scale

**What it is.** Both workflow engines now verify every load-bearing claim (runaway cap 20) instead of the old top-6/top-8. Refuters are prompted to REFUTE, default downward on silence, and REFUTED claims are **dropped** rather than labeled. Gap-fill rounds restored: standard=1, deep=2, max=3.

**When to reach for it.** Any research swarm. The rule worth memorizing: **a claim labeled VERIFIED by the agent that found it counts as UNCONFIRMED.**

**When NOT to.** At `quick` depth verification stays capped at 4, since that tier is for sanity checks where a full verify round costs more than it returns.

**Honest edges.** The cap-20 runaway stop means a run generating 40+ load-bearing claims leaves some unverified, and the synthesis must say so.

## Capability 5: the Playwright primary-source lane

**What it is.** `deep-research-swarm.workflow.js` accepts a `primary_sources` array and also harvests `PRIMARY-SOURCE-BLOCKED:` URLs that sweep agents report when WebFetch returns a JS shell. Up to 3 browser agents read those pages under `directives/browser-automation-safety.md` (read-only: no logins, no forms, no purchases).

**When to reach for it.** When the evidence that would settle the question lives behind JavaScript: ad libraries, live pricing pages, dashboards.

**When NOT to.** Static pages. WebFetch is faster and cheaper, and this lane is for what WebFetch structurally cannot reach.

**Worked example (live, this session).** The lane read the public Meta Ad Library and returned 13 supplement brands with 15+ simultaneously active US ads inside ten minutes (Omni Creatine ~750, Legion ~330, Crave Creatine ~290 with ads running continuously since July 2025) plus verbatim confirmation that CREVARI's $1,000 Creative Autopsy is still live with its exact terms. None of that was reachable before.

**Honest edges.** The browser is shared, and a concurrent session driving it showed up in this run's notes. Verify `location.href` before trusting an extraction.

## Capability 6: the depth gate (the governance piece)

**What it is.** `research_quality_gate.py` gained `--depth <tier>` (floors from the contract, applied to any artifact regardless of origin) and `--receipt` (writes `<file>.depth-receipt.json`). `chain_runner.py finalize` gained `--depth-receipt`: a `--type Research` finalize without a **passing** receipt caps Factual Grounding at 6 and stamps the reason into notes.

**When to reach for it.** Before treating any research output as decision-grade, especially output from an ad-hoc Workflow swarm, which previously answered to nothing.

**Worked example.** The incident artifact, gated: exit 1, *"DEPTH CONTRACT UNMET for deep: 0 sources / 0 domains (contract: 15 sources / 6 domains)."* The document that scored 8.33 at finalize now fails at the door.

**Honest edges.** The gate is strict on provenance. This session's own new findings PASS the depth contract and still FAIL overall at 42% claim attribution. Correct behavior on working-notes files, but don't read a FAIL as "worthless"; read the specific issues.

## Composition (options, never wiring)

| Stacks with | What it buys | When it earns the cost |
|---|---|---|
| `/wargame-run` | fights the route on paper before research spends tokens | multi-day missions where a wrong premise is expensive |
| `/swarm` (`swarm.md § DEPTH CONTRACT`) | the four guards land in the brief automatically | any research-shaped swarm brief |
| `/extract-approach` | banks the crack so nobody re-solves it | after any non-trivial fix; this session's card is the template |
| Gemini Deep Research (`research.py gemini-start`) | a second retrieval stack, $0 on Ultra quota | deep/max runs where blind-spot diversity matters |

## Where things stand

The 234 KB corpus at `.tmp/research/offer-validation-deep/` (296 sources, 155 domains) is honestly labeled **RECON-GRADE**, because the verify phase never ran once the proof run was stopped. Promoting it is a bounded run: verify plus synthesize on what already exists, gate the report, finalize with the receipt.
