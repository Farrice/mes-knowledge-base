---
name: "Cody Schneider — Signal-Based Marketing Systems"
description: "Cody Schneider (founder, Graphed — deploys marketing agents for fast-growing companies): engagement as hand-raise, the 10-20 creator aperture that covers ~80% of a niche, cheapest-first waterfall enrichment, four-lane domain separation, and 'an agent is code with a thinking loop and a live data stream.' Use for designing signal-based targeting systems, reading engager pulls into qualified hand-raises and content angles, enrichment cascade design, outbound infrastructure blueprints, organic content engines built on real source material, 90-day winner remix rotations, and agent-vs-automation build verdicts. Do NOT use for writing the outreach copy itself (luke-iha / copy-engine), LinkedIn post authorship (lara-acosta / ghostwrite), automation plumbing you already have (nick-saraev, /arsenal), offer economics (alex-hormozi), or anything that sends — this skill is listening-and-design only in house."
version: "1.0"
format: "completion-engine"
workflows: 11
routing: core
sources: "Greg Isenberg, 'These AI Marketing Agents Get You Customers' (44:00, 2026-08-05) — transcript + 100 frames, watched at the demo timestamps, extracted 2026-08-06"
---

# Cody Schneider — Signal-Based Marketing Systems

**Invocation**: `/deploy-skill cody-schneider-signal-outbound` · Front door: `/signal-system-blueprint`
**Domain**: Intent Signal • Audience Sourcing Math • Enrichment Cascade Logic • Deliverability Architecture • Organic Content Loops • Agent-vs-Automation Judgment
---
The targeting epistemology the bench was missing: *how you know who to talk to before you write a word*. Every other outbound and content expert starts downstream of a list — Cody treats the list as the creative act. Founder of Graphed, screen-shares his own terminal, gives the entire stack away for free: *"There's no gatekeeping here. I despise people that do this. Don't buy a course."*

**Core Philosophy**:
- Engagement is a hand-raise — a dated, checkable declaration that beats every firmographic
- Monitor 10–20 outliers, get ~80% of the industry; aperture inflation pays to re-find the same people
- Judgment goes exactly one place: before the expensive step. Everything else is code
- *"You should not be paying Anthropic to do an API call — you should be paying them to make the software that does it"*
- Never ask an LLM to have the idea; extract it from real human conversation
- Winners repeat on a 90-day clock. Novelty is a cost paid during prospecting, then amortized

## Available Workflows

### Tier 1 — Signal Doctrine
| # | Workflow | Produces | Use When |
|---|----------|----------|----------|
| 1 | [Signal System Blueprint](workflows/signal-system-blueprint.md) | End-to-end loop design with the judgment step located + per-run cost | **Front door** — cold-starting or rebuilding a targeting system |
| 2 | [Creator Aperture](workflows/creator-aperture.md) | 10–20 account listening roster + kill list + creators file for `signal_scout.py` | Starting any signal system; quarterly re-audit; pulls returning noise |
| 3 | [Engager Signal Audit](workflows/engager-signal-audit.md) | Qualified hand-raise ledger + honest volume + human decision queue | Weekly, after a pull; QA-reading a client's automated roster |
| 4 | [Resonance to Angle](workflows/resonance-to-angle.md) | Angle brief with ICP verbatim block and evidence trail per angle | Before a content sprint; offer copy from real buyer language |

### Tier 2 — System Design
| # | Workflow | Produces | Use When |
|---|----------|----------|----------|
| 5 | [Waterfall Enrichment Design](workflows/waterfall-design.md) | Cascade ordered by cost-per-marginal-hit + hit-rate ladder + stop rule | Client enrichment stacks; a list costs too much for its yield |
| 6 | [Outbound Infra Blueprint](workflows/outbound-infra-blueprint.md) | Four-lane domain design, capacity math, tripwires, failure runbook | Client outbound builds; deliverability collapse; before anyone sends from a company domain |
| 7 | [Reply Handling Playbook](workflows/reply-playbook.md) | Goal-prompt, routing table, objection library, 6-month re-touch — **draft-only** | Replies arriving; designing a conversation layer with human review |
| 8 | [Organic Engine](workflows/organic-engine.md) | Source-material engine spec + first batch of real insight cards | Team/personal content engine; content is generic and the input is the suspect |
| 9 | [90-Day Winner Remix](workflows/winner-remix-90.md) | Winners corpus with mechanisms + dated rotation calendar | Quarterly planning; an account with history that restarts from scratch |

### Tier 3 — Meta / Cross-Domain
| # | Workflow | Produces | Use When |
|---|----------|----------|----------|
| 10 | [Agent or Automation](workflows/agent-or-automation.md) | Build verdict — script/automation/agent/reject + inference cost crossover | **Before building anything agentic**, here or for a client |
| 11 | [Marketing-as-Code Audit](workflows/marketing-as-code-audit.md) | Classified activity audit + build queue ranked by hours-returned | A function feels busy but not productive; scoping a retainer |

## House Constraint (binding)
**Listening only in-house.** Farrice sends nothing automatically (decision 2026-08-06) — reputation and distribution stay human. The listening half is implemented as `execution/signal_scout.py` (creators file → engager roster + resonance report, Apify-budget-guarded, never contacts anyone). Workflows 6 and 7 are client-facing design artifacts here, never auto-fired.

## Stacking Guide
| Pair with | For |
|---|---|
| `lara-acosta` / `/ghostwrite` | Resonance verbatims → hooks and posts. This skill supplies the *what*; she supplies the shape |
| `kallaway` | Why a winner won — mechanism clustering with a psychology lens, so the remix is principled not statistical |
| `nicolas-cole` | 90-day remix pass through his proven-format library |
| `nick-saraev` | He builds the automation; workflow 10 decides which steps deserve inference at all |
| `alex-hormozi` | The ICP gate scored on money-model math, not title matching |
| `writers-room` | Trapped-context mining as the Layer 0 source material that engine has been missing |
| `daniel-priestley` | Earned-media arithmetic as the argument for the oversubscribed motion |
| `/arsenal` | Mandatory before any build recommendation — ~40 systems exist; extend, never rebuild |
| `/copy-engine` / `luke-iha` | The message itself, once this skill has decided who and why-now |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Full dossier**: `extractions/cody-schneider-signal-outbound/extraction-report.md` (18 patterns, 10 hidden-knowledge items, 5 exemplars, 8 signature moves, 8-criterion rubric)
- **Era-bound stack** (dated 2026-08, verify before use): [references/era-bound-2026-08-stack.md](references/era-bound-2026-08-stack.md) — every vendor, actor, and price. Workflow bodies name roles only.
- **Blind pass**: `extractions/cody-schneider-signal-outbound/blind-pass-log.md`
- **Execution prompts**: `references/prompts-v2/` (11 structure-pure v2 prompts, one per workflow)

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

11 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **[PROPOSED_SYSTEM] — Build Verdict** — `skills/cody-schneider-signal-outbound/references/prompts-v2/agent-or-automation-verdict.md`
- **[BUYER] — Listening Aperture** — `skills/cody-schneider-signal-outbound/references/prompts-v2/creator-aperture.md`
- **Engager Signal Audit — [DATE]** — `skills/cody-schneider-signal-outbound/references/prompts-v2/engager-signal-audit.md`
- **[FUNCTION] — Marketing-as-Code Audit** — `skills/cody-schneider-signal-outbound/references/prompts-v2/marketing-as-code-audit.md`
- **[ORG] — Organic Engine Spec** — `skills/cody-schneider-signal-outbound/references/prompts-v2/organic-engine-spec.md`
- **[BUSINESS] — Outbound Infrastructure Blueprint** — `skills/cody-schneider-signal-outbound/references/prompts-v2/outbound-infra-blueprint.md`
- **[OFFER] — Reply Handling Playbook (Draft-Only)** — `skills/cody-schneider-signal-outbound/references/prompts-v2/reply-handling-playbook.md`
- **[NICHE] — Angle Brief ([DATE])** — `skills/cody-schneider-signal-outbound/references/prompts-v2/resonance-angle-brief.md`
- **[BUSINESS] — Signal System Blueprint** — `skills/cody-schneider-signal-outbound/references/prompts-v2/signal-system-blueprint.md`
- **[SEGMENT] — Enrichment Cascade Design** — `skills/cody-schneider-signal-outbound/references/prompts-v2/waterfall-cascade-design.md`
- **[ACCOUNT] — 90-Day Remix Rotation** — `skills/cody-schneider-signal-outbound/references/prompts-v2/winner-remix-calendar.md`

<!-- END:execution-prompts -->
