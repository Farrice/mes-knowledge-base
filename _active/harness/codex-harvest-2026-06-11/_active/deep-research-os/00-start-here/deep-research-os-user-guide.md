# Deep Research OS User Guide

## What It Is

Deep Research OS is your research command package for work where weak evidence
would produce weak decisions. It blends deep research, wide decomposition,
social listening, first-principles analysis, systems thinking, ICP deep
canvassing, and anti-hallucination verification.

Use it when you need more than a summary. Use it when the work has money,
positioning, client trust, market timing, or public claims attached.

## Best Entry Points

| Use | Command |
|---|---|
| Full trace plus research route | `/virtuoso --mode research [objective]` |
| Direct research command | `/deep-research-os [objective]` |
| Market/category work | `/deep-research-os --market [market]` |
| Buyer psychology | `/deep-research-os --icp [buyer/problem]` |
| Voice-of-customer mining | `/deep-research-os --social-listening [market/community]` |
| Product or offer validation | `/deep-research-os --pmf [product/offer]` |
| Many items at once | `/deep-research-os --wide [list/category]` |
| Draft verification | `/deep-research-os --claim-audit [draft or claims]` |

## High-Leverage Use Cases

| Use case | What you get |
|---|---|
| Offer-market fit diagnosis | Evidence-backed verdict on who buys, why, what they compare, and what promise lands. |
| ICP deep canvass | Identity-level buyer map with resistance, language, objections, and bridge messaging. |
| Social listening pack | Real public language from reviews, forums, threads, and comments with source links. |
| Competitive intelligence | Competitor positioning, pricing, proof, content moats, gaps, and wedge opportunities. |
| Trend radar | Current signals, decaying trends, emerging language, and category movement. |
| Claim audit | Verified, triangulated, directional, inferred, unverified, and contradicted claims. |
| Wide research table | Consistent analysis across many companies, products, creators, offers, or markets. |
| Client strategy memo | A polished, source-backed memo that can feed consulting, positioning, content, or sales assets. |

## How To Prompt It

Use this shape:

```text
/virtuoso --mode research
Objective: [decision this research needs to support]
Context: [what I already know]
Audience: [who the output is for]
Source preferences: [public web, local files, user-provided docs, specific sites]
Deliverable: [brief, market map, ICP, social listening pack, claim audit, table]
Risk if wrong: [what bad decision we are trying to prevent]
Deadline/depth: [quick, standard, deep, max, wide]
```

Fast version:

```text
/deep-research-os --market I need to know whether AI skill/plugin packages are a real buyer demand, who buys them, what they pay for, what is slop, and what wedge we can own.
```

## What The Trace Means

- `Support stack considered` means those routes were evaluated.
- `Support stack executed` means the workflow or script actually ran.
- `Worker packets prepared` means the system has a delegation plan.
- `Real subagents spawned: false` means no actual Codex subagents were launched.
- `Paid/API boundary` means provider-heavy research needs approval first.
- `Evidence ledger` is the source truth, not decoration.

## Quality Bar

A good Deep Research OS result must include:

- A research plan.
- A source ledger.
- Claim labels.
- Contradictions and gaps.
- Social listening sources when buyer language matters.
- Systems and first-principles analysis for strategy work.
- Clear recommendations with confidence and risk.
- A next data pull instead of pretending the map is complete.

## Best Next Prompt

```text
/virtuoso --mode research --delegate
Objective: Build a buyer-backed market intelligence brief for [market/offer].
Deliverable: Market map, ICP deep canvass, social listening ledger, competitor wedge, and offer-market fit verdict.
Source preferences: Public web and local workspace only unless I approve paid/API tools.
Risk if wrong: I do not want to build or sell something the market does not want.
```
