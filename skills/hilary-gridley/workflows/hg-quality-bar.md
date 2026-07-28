---
description: Articulate "what good looks like" for a role, team, or artifact class at all three altitudes (time / portfolio / artifact) — quality bar doc + accountability contract, the upstream cure for slop
---

# hg-quality-bar — What Does Good Look Like

Slop root #3 is an unarticulated bar. This workflow produces the articulation: a quality bar a team can self-grade against, plus the accountability contract that replaces AI-method policing. The clarity ritual is the product; any tools minted later (`hg-judgment-encode`) are containers for it.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md`.
- Identify the subject: a role, a team, or an artifact class. If "the whole company" → narrow to the highest-stakes role/artifact first (asymmetric-downside rule).
- This is a taste-bearing exercise — if the operator's own standards are the input, interview before writing (one question at a time); never invent their bar.

## Skill Acquisition

- `genius.md` §Core Philosophy, §Three-Layer Quality Stack, §Accountability-Not-Method
- `references/source-quotes.md` §The bar, §Accountability

## Execution

1. **Set the altitude frame.** Three layers, kept distinct: L1 how time is spent / how work happens · L2 which projects (the 10 of 100 — portfolio slop check) · L3 per-artifact quality. State which layer(s) this pass covers.
2. **Run the bar-setting ritual** (her question, verbatim): *"What is a level that, if my team is doing this on a consistent basis, I will be happy?"* Answer it per layer. For L3, name criteria per artifact class; where edit pairs exist, note them as `hg-judgment-encode` feedstock.
3. **Anchor with exemplars.** Per artifact class: 1-2 real pieces that HIT the bar (and why, in one line each) + the characteristic failure mode this team produces under pressure (its personal anti-pattern).
4. **Write the accountability contract.** Per role: what they're accountable FOR (outcomes) and what good looks like — zero statements about how or whether to use AI. Include her framing where useful: the third-party thought experiment ("you could always have contracted the work out; you're still accountable").
5. **Define the escalation ladder**: self-grade → tool feedback (if evaluators exist) → peer pass → manager judgment. Manager sits at the judgment station only.
6. **Pressure-test**: would a new hire reading only this doc know what to produce and how to self-grade? Every criterion concrete? Every layer distinct? Fix before shipping.

## Content Type Adaptations

| Subject | Emphasis |
|---|---|
| Marketing/content team | L3 per-format bars + brand voice thresholds (feeds Taste Profile Layer 3) |
| A single operator (solo) | L2 dominates — portfolio slop ("10 apps nobody uses") is the solo failure mode |
| Client engagement | Bar doc doubles as the scope/QA annex of the SOW |
| Agent harness | Bars become gate criteria; accountability contract becomes the agent brief's Output Contract |

## Output Requirements

- Deliverable: Quality Bar doc (≤2 pages — density over completeness): three-layer bars + per-artifact criteria + exemplars + anti-patterns + accountability contract + escalation ladder.
- Written in the team's language, not management-consultese.
- Execution prompt: `references/prompts-v2/quality-bar.md`

## Quality Gate

genius.md rubric: layer coverage (all named layers distinct?), pass/fail legibility, human seat clarity (manager = judgment station only?). Anti-patterns: method policing anywhere in the contract; bars stated as adjectives ("high quality," "compelling") instead of checkable criteria; conflated layers. Any present → rewrite before delivery.
