# Workflow: Lead-Form Builder

**Produces**: a complete lead-form spec — offer selection (Special Offer / Product for Prospects / Promotion) + full page copy in the four-part anatomy (Hook → Value Prop → Credibility → CTA) — ready to build in ScoreApp or any form tool.

## Load Context

1. Read `../genius.md` (mandatory) — especially pattern 8 and Hidden Knowledge 3.
2. Read the SLL System Map's offer shelf. If empty, run the offer-shelf step of workflow 01 first.

## Steps

1. **Pick the offer type** for this quarter:
   - **Special Offer** — discount / limited-time / launch campaign.
   - **Product for Prospects** — the easy first step: intro workshop, online assessment/scorecard, waitlist, discussion group. (Default choice for cold audiences — lowest commitment hand-raise.)
   - **Promotion** — time-boxed, MUST have an end date.
2. **Write the page in the drawn anatomy** (two layers — the offer is not the page):
   - **Hook** — explains what's going on, immediately.
   - **Value Prop restated** — "if I do this, I will get this," in one breath.
   - **Credibility** — testimonials, qualifications, or linked research. Real only; claims quarantine.
   - **CTA** — one action: fill in the form to get started.
3. **Confirm the hand-raise framing**: the form captures a SIGNAL of intent ("signal that they want to do business with you"), so ask only what the sales process needs — friction beyond that loses the raise.
4. **Wire the LAPS handoff**: who contacts a fill, within what SLA, toward appointment → presentation → sale.
5. Tool note: ScoreApp is Priestley's tool (assessments/scorecards native). Spec is tool-agnostic — build wherever the business already operates.

Output step — Execution prompt: `references/prompts-v2/sll-lead-form-spec.md` — honor its Output Contract.

## Output Schema

```
# Lead Form — [Business] — Q[x]
Offer type: [Special Offer | P4P | Promotion (end date)]
Offer: [one sentence]
## Page Copy   (HOOK · VALUE PROP · CREDIBILITY · CTA — full copy, in order)
## Form Fields (minimum viable signal)
## LAPS Handoff (owner · SLA · next step script pointer)
```

## Example Output (abridged, S&C coach)

> **Offer type**: P4P — "Executive Strength Score" (5-min assessment)
> **HOOK**: "Find out in 5 minutes why your training stopped working after 35 — and the 3 numbers that predict whether it'll work again."
> **VALUE PROP**: Take the assessment → get your Strength Score + a personal 3-move priority plan for a 45-minute-a-week rebuild.
> **CREDIBILITY**: "Down 14kg, deadlifting 2× bodyweight at 44 — while running a 40-person team." — [client name]. Coach: CSCS, 11 years coaching working professionals.
> **CTA**: "Get your Strength Score →" (name, email, one question: 'biggest obstacle right now?')
> **LAPS**: fills → Farrice, same-day email, offer of 15-min score-review call.

**What makes this excellent**: the hook names the reader's situation and promises a specific, fast diagnostic; the value prop is one if-then breath; credibility is a checkable client result plus real credentials (no fabricated counts); the form asks exactly 3 things — the obstacle question feeds the sales call. The offer is an easy first step, not a disguised sales call.

## Quality Gate

- [ ] Offer is one of the three types; promotions carry an end date
- [ ] All four anatomy parts present, in order, no padding between them
- [ ] Credibility items are real and checkable (Factual Grounding veto applies)
- [ ] Form asks minimum viable signal (≤4 fields unless sales process demands more)
- [ ] LAPS handoff named with SLA
