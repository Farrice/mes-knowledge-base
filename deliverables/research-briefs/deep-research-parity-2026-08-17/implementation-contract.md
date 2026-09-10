# Research OS Deep-Research Parity Implementation Contract

## Decision

Build a paved companion runtime behind `/deep-research-os`, not a new research owner. Codex-native is the default. Gemini standard and native ChatGPT Deep Research are calibration challengers. The OpenAI API adapter and Gemini Max are out of scope.

## Skill System Contract

- **Function owner:** `/deep-research-os`
- **Companion components:** `execution/research.py`, `execution/research_bakeoff.py`, `execution/deep_research_client.py`, `execution/research_quality_gate.py`
- **Inputs:** frozen mission, current web evidence, claim audit, provider/import receipt
- **Outputs:** normalized mission, candidate report, claim audit, spend ledger, blind scorecard, parity verdict
- **Non-duplication boundary:** keep Free-First Research Mission as the native evidence-gathering foundation; do not create a parallel skill tree or a second hot command
- **Escalation boundary:** paid provider calls, private/authenticated access, publishing, outreach, real subagents, and global writes remain separately gated

## Goal Packet

- **Target:** deep-research runtime, provider billing assumptions, strict quality depth, import and blind-grade path
- **In scope:** local code/docs/tests and research artifacts in this isolated lane; one Gemini standard call only if the provider hard ceiling becomes machine-verifiable
- **Out of scope:** OpenAI API, Gemini Max, paid retries/fallbacks, publishing, outreach, profile changes, deployment, client-facing performance claims
- **Stop condition:** all deterministic verifiers pass; Codex-native candidate is sealed; provider eligibility produces a receipt; provisional blind scorecard and honest parity status exist
- **Turn cap:** two repair rounds after the first full verifier run
- **Evaluator:** deterministic parity verifier, Free-First verifier, Deep Research OS verifier, strict depth receipt, claim-level audit, negative controls
- **Rollback:** discard only this lane's new parity files/patch if rejected; preserve prior corrected research and all user-owned dirty files
- **Human checkpoint:** satisfied by Farrice's explicit instruction to implement this plan; the provider hard-ceiling factual gate remains non-overridable

## Agentic Engineering Packet

- **Objective:** make native research repeatable, inspectable, provider-optional, and honest about cost and parity
- **Source of truth:** approved plan, recent corrected offer authority files, Free-First contract, official provider billing documentation
- **Context plan:** freeze authority and question before external evidence; prevent historical artifact polish from changing offer eligibility
- **Review loop:** compile → cold tests → negative controls → live native research → claim audit → blind grade
- **Dependency policy:** stdlib and existing harness only; no new package or service
- **Hardening proof:** unknown billing blocks, $7.99 exposure blocks another standard reservation, duplicate interaction cannot rebill, direct/programmatic/background Gemini starts cannot bypass the mission ledger, legacy paid-provider fan-out is parked, parked Angle Map promotion fails, missing candidates remain partial

## Evolution Council Verdict

**APPROVE IN SHADOW/PAVED MODE.** The repair corrects factual and spend-control defects and adds an explicit parity surface. It must not become a claim that Codex-native equals provider Deep Research until the sealed three-way floors are met. Provider adapters stay challenger-only.

## Acceptance State

- Implementation: `PASS — BUILT AND REGRESSION TESTED`
- Codex-native candidate: `SEALED — 98/100 INTERNAL CANDIDATE SCORE`
- Codex-native evidence: `23 RESOLVED URLS / 18 DOMAINS / 21 OF 21 LOAD-BEARING CLAIMS SUPPORTED / 17 OF 17 HIGH-RISK CLAIMS SUPPORTED`
- Gemini candidate: `NOT RUN — BLOCKED BEFORE START BECAUSE A PROVIDER-SIDE HARD CEILING WAS NOT MACHINE-VERIFIABLE`
- ChatGPT candidate: `PENDING SUBSCRIPTION EXPORT`
- Provisional bakeoff: `PARTIAL — PROVIDER REFERENCES PENDING`
- Provider API spend: `$0.00 RECORDED / $0.00 PENDING`
- Exact offers: `UNTESTED / NO EVENT`
