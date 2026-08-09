---
name: "Target Universe and High-DMI Market"
produces: "Enumerable target-universe specification with observable indicators, disqualification logic, and demonstrability verdict"
expert: "Jordan Crawford — Evidence-First GTM Intelligence"
load_context: "genius.md"
tier: 2
---

# Target Universe and High-DMI Market

## Pre-Flight Gate

Require a `QUALIFIED` or explicitly `PROVISIONAL` PQS and its Research Receipt. Read `references/research-tool-contract.md`. Do not purchase data or scrape restricted sources. This workflow specifies a universe; it does not send to it.

## Skill Acquisition

Load patterns 6, 7, 8, 12, and 14. High DMI here means the problem leaves demonstrable public or permissioned traces and the relevant universe can be known well enough to disqualify explicitly.

## Input Required

- PQS and evidence strength
- Known-good and bad-fit examples
- Geography, channel, and legal/privacy bounds
- Available public or permissioned data sources
- Competition/message saturation observations

## Execution

1. Translate each qualification rule into one or more observable indicators.
2. Record source, freshness, false-positive risk, and missingness for every indicator.
3. Partition private context from public queries, then enumerate plausible candidates broadly from lawful/approved sources. Record tool status and failed searches.
4. Disqualify candidates in order: no problem evidence, wrong company state, wrong person/access, stale/ambiguous evidence.
5. Estimate universe size as `KNOWN`, `RANGE`, or `UNKNOWN`; never invent precision.
6. Assess demonstrability, universe knowability, and message competition separately.
7. Return `HIGH-DMI`, `MIXED-DMI`, or `LOW-DMI` plus the market-narrowing move.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Small finite B2B | Candidate-level evidence table |
| Large B2B | Sample known-good/bad cases before scaling enumeration |
| Local market | Geography and observable local events dominate |
| Privacy-sensitive | Use aggregate/permissioned indicators; prohibit personal enrichment |

## Output Requirements

Indicator map, source map, candidate/disqualification schema, universe estimate with confidence, DMI scorecard, Research Receipt, exceptions, and one narrowing or research move. Use `references/prompts-v2/target-universe-high-dmi.md`.

## Quality Gate

- Every inclusion criterion has an observable signal or `UNKNOWN`.
- Universe construction and model judgment are separable.
- Candidate count is not called TAM or demand.
- Privacy and source restrictions are explicit.
- Public traces do not promote a provisional PQS to qualified.
- Failed/blocked retrieval is `NO RESEARCH EVENT`.
- Output contains zero outreach execution.
