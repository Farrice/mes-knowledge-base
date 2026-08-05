---
name: "Benoit Vatere — Full-Funnel Media Systems"
description: "Liquid Death's Chief Media Officer: media buying and measurement as an engineered system — spend maps by funnel stage, incrementality triage (ROAS×new-to-brand, geo holdouts), home-run-only testing with day-4 kills, channel selection by controllable levers, one-job-per-creative mapping, the Golden Core CAC-inversion diagnostic, retail media for CPG. Use for media audits, 'why did Meta stop working', channel planning, test discipline, and CPG/DTC measurement. Do NOT use for ad creative production (dara-denney-meta-ads), ad psychology (sarah-levinger), or brand/creative strategy (oren-*)."
version: "1.0"
format: "completion-engine"
workflows: 10
sources: "Marketing Against the Grain — 'The #1 Marketing Lesson From Building a $1B+ Brand' (2026, 34min, watched w/ frames). Single-source skill: fidelity flags honored."
---

# Benoit Vatere — Full-Funnel Media Systems

**Invocation**: `/deploy-skill benoit-vatere`
**Domain**: Media Buying Systems • Incrementality & Measurement • Channel Selection • Funnel-Stage Creative Mapping • CPG Retail Media

The media-systems architect seat. Everyone talks Liquid Death's creative; Benoit built the distribution machine underneath — "a full-funnel media system with creative equations that fuel it." Fills the roster gap between creative-side paid experts (Dara, Omar, Alex Copper, Sarah Levinger) and operator attribution (Vince): the buying, measurement, and testing doctrine itself.

**Core Philosophy**:
- Signals over perfection — "I don't need perfect, I need signals"; decision latency in days
- Platform ROAS is contaminated; incrementality (NTB, holdouts) is the truth layer
- Channels are lever sets, not audiences — no controllable lever, no dollar
- One job per creative unit; the funnel never collapsed
- Chase CAC:LTV from day one and you fail — the Golden Core is finite
- Let go of control where you scale; keep control of how you buy

## Available Workflows

### Tier 1 — Foundation
| # | Workflow | Produces | Use When |
|---|----------|----------|----------|
| 1 | [Spend Map](workflows/spend-map.md) | Every dollar tagged by funnel stage + imbalance read + ONE rebalance move | First touch on any account; client audits; quarterly reviews |
| 2 | [Incrementality Triage](workflows/incrementality-triage.md) | ROAS×NTB quadrant, fake-winner flags, geo holdout design, iROAS ladder | Budget allocation; any channel that "prints"; no test infra yet |
| 3 | [Channel Lever Audit](workflows/channel-lever-audit.md) | Channel × job × lever matrix with ADMIT/REFUSE verdicts | Channel planning; media sales pitches; "should we be on X?" |
| 4 | [Funnel Creative Map](workflows/funnel-creative-map.md) | One-job brief headers + buyer-state message ladder | Creative planning; two-job ads in the account; retargeting design |

### Tier 2 — Practitioner
| # | Workflow | Produces | Use When |
|---|----------|----------|----------|
| 5 | [Golden Core Diagnostic](workflows/golden-core-diagnostic.md) | CAC-inversion diagnosis + up-funnel shift memo | "Meta stopped working"; rising CAC; early-stage budget design; investor pressure |
| 6 | [Home-Run Test Charter](workflows/home-run-test-charter.md) | ≥20%-effect test roadmap with pre-written day-4 kills | Test planning; a bloated always-inconclusive test queue |
| 7 | [PDP Chain Audit](workflows/pdp-chain-audit.md) | CTR→CPM→CPC→PDP-view decomposition + weakest-lever fix | Mid-funnel efficiency; good-CTR-bad-results campaigns |
| 8 | [Retail Media Plan](workflows/retail-media-plan.md) | Retail-media allocation move + D2C-obsession corrective (CPG; fidelity: low) | CPG brands; D2C-heavy spend; TikTok Shop questions |

### Tier 3 — Stacking
| # | Workflow | Produces | Use When |
|---|----------|----------|----------|
| 9 | [BV × Dara Stage Briefs](workflows/bv-x-dara-stage-briefs.md) | Per-stage creative briefs: Benoit headers, Dara bodies, dissent ledger | Creative production against the system map |
| 10 | [BV × Vince Measurement Stack](workflows/bv-x-vince-measurement-stack.md) | Three-layer measurement stack (platform/blended/incrementality) for DTC+retail | Measurement architecture; attribution disputes |

## Stacking Guide
| Pair with | For |
|---|---|
| `dara-denney-meta-ads` | Creative production inside the stage/job system (workflow 9) |
| `vince-nijhof-dtc-operator-system` | Blended attribution × incrementality (workflow 10) |
| `sarah-levinger-ad-psychology` | Psychological angle work inside RE-ANGLE/WIN-BACK briefs |
| `luke-iha-*` / `omar-eddaoudi-*` | Hook/copy depth on consideration units |
| `kallaway` / `oren-*` | Organic virality as the awareness layer (Liquid Death's own early play) |
| Proof-to-Market offer | Spend Map + Golden Core + Retail Media = the CPG audit vocabulary for supplement/performance buyers |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Receipts**: [references/source-quotes.md](references/source-quotes.md) — timestamped verbatims
- **Era-bound claims**: [references/era-bound-2026.md](references/era-bound-2026.md) — verify before citing platform mechanics as current
- **Full dossier**: `extractions/benoit-vatere/extraction-report.md`
- **Name note**: captions garble him as "Benwa/Benwis" — Benoit Vatere (VERIFIED)

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

8 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Channel Lever Matrix — [Brand], [date]** — `skills/benoit-vatere/references/prompts-v2/channel-lever-matrix.md`
- **Creative Map + Message Ladder — [Brand], [date]** — `skills/benoit-vatere/references/prompts-v2/creative-message-ladder.md`
- **Golden Core Diagnostic — [Brand], [date]** — `skills/benoit-vatere/references/prompts-v2/golden-core-memo.md`
- **Test Charter Pack — [Brand], [date]** — `skills/benoit-vatere/references/prompts-v2/home-run-test-charter.md`
- **Incrementality Triage — [Brand], [date]** — `skills/benoit-vatere/references/prompts-v2/incrementality-triage.md`
- **PDP Chain Audit — [Brand], [window]** — `skills/benoit-vatere/references/prompts-v2/pdp-chain-audit.md`
- **Retail Media Move — [Brand], [date]** — `skills/benoit-vatere/references/prompts-v2/retail-media-move.md`
- **Spend Map — [Brand], [window]** — `skills/benoit-vatere/references/prompts-v2/spend-map-audit.md`

<!-- END:execution-prompts -->
