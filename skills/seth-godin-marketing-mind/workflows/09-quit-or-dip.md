# Quit-or-Dip Memo

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Practitioner
> **Produces**: Quit-or-Dip Memo
> **Slash Command**: `/gmind-quit-or-dip`

---

## Purpose

Quit decisions get made on shame or sunk cost, almost never on evidence. Godin's method separates the hard part into two structurally different shapes — a dip that ends, or a slope that doesn't — checks whether anyone has ever survived this specific dip, zeroes out the sunk cost as a gift already spent, and judges the decision on information-at-the-time rather than outcome. The result is a verdict, not a feeling.

---

## Inputs Required

1. **The Thing in Question** — The business, project, role, or commitment being evaluated.
2. **What's Been Invested** — Time, money, reputation, relationships already spent.
3. **The Current Hard Part** — What specifically is difficult right now.
4. **Evidence of Others** — Anyone the operator knows of who has been through this exact hard part before.

---

## Workflow

### Step 1: Classify the Hard Part — Dip or Slope

Run the discriminator before anything else. *"What we want to figure out, is there a dip? The hard part before it gets easier. This is what happens at the gym in February. Most people quit the gym in February because that's when it gets hard. If you get through that dip, it's pretty clear that by June, you've got six-pack abs."* Against the slope: *"then there are other things we sign up for where either no one's ever gotten through this dip or there is no dip. It's just a slope. So, you can't smoke your way through emphysema. It's just going to keep getting worse and worse and worse and worse and worse."* Name which shape the Current Hard Part is — a temporary wall with an end, or a decline with no bottom.

### Step 2: Run the Survivor Evidence Test

Test the dip classification against real evidence, not hope. *"There are some real estate brokers who make a fine living and aren't hustling their out of their minds. But, none of those people have been real estate brokers for 1 year. They made it through the hard part."* Ask: who, specifically, has come before the operator through this exact dip? If the Evidence of Others input is empty or vague, treat the dip claim as unproven — a hoped-for dip with zero survivors behaves like a slope until proven otherwise.

### Step 3: Zero Out Sunk Costs as a Gift

Reframe What's Been Invested using the accounting move, not the guilt move. *"My blood, my sweat, my tears, my time, my money, they're all gone. They're gone no matter what. So, tomorrow, do I want to accept what that bought as a gift from my former self? Or, do I want to say, 'No, thank you. I'm going to go build a new thing that's going to resonate with the people who need it.'"* Godin's closing evidence on the psychology of the reframe: *"if you talk to people who made that smart decision of walking away from sunk costs, almost all of them will tell you they're glad they did."* State plainly what the sunk cost bought (skills, relationships, market knowledge, a clarified no) as something already received — never as a debt still owed.

### Step 4: Run the Good-Decision-Maker Test

Separate the decision from its outcome using the live demonstration, not the lecture. *"Would a good decision-maker choose what I chose? If the answer is yes, then you made a good decision."* Anchor it against the anti-case: *"If you buy a lottery ticket and win the lottery, you made a bad decision. Buying a lottery ticket is always a bad idea. But, then you got lucky."* And the inverse absolution: *"if you make a good decision and it turns out badly, not your fault. You just didn't get lucky this time."* Score the original decision to enter or persist on information-at-the-time only — never on how it's currently turning out.

### Step 5: Run the Future-Self Check

Close the evaluation on identity, not urgency. *"You want to become the person your future self will thank you for. You want to make decisions that the Melanie in eight years is going to say, 'Wow, I'm glad I did that.'"* Ask which choice — persist or quit — the operator's future self is more likely to thank them for, using the evidence gathered in Steps 1-4, not present-moment pressure.

### Step 6: Deliver the Verdict

Land on one of three calls, with the tutu normalization available to strip shame from any quit verdict: *"You don't wear a tutu to work anymore, even though you took ballet lessons when you were six... we all quit stuff as we grow up."*

- **PERSIST** — Dip confirmed, survivors exist, good-decision-maker test passes on continuing.
- **QUIT** — Slope confirmed, or a claimed dip with zero survivor evidence.
- **REDESIGN** — Dip is real but the current approach isn't the one survivors used; change the method, not the commitment.

---

## Output Schema

```
QUIT-OR-DIP MEMO
==================

The Thing: [name it]
Hard Part Classification: [DIP / SLOPE] — reasoning

SURVIVOR EVIDENCE:
[named survivors, or "none found — treat as unproven dip"]

SUNK COST REFRAME:
What it bought (received as a gift): [skills / relationships / knowledge / clarity]

GOOD-DECISION-MAKER TEST:
Would a good decision-maker choose what was chosen? [Yes/No] — based on information at the time

FUTURE-SELF CHECK:
[which path the future self thanks them for, and why]

VERDICT: [PERSIST / QUIT / REDESIGN]
[one sentence, no shame language, no "but I've already put in"]
```

---

Execution prompt: `references/prompts-v2/quit-or-dip-memo.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Dip vs. slope classified | Named explicitly with reasoning, not assumed |
| Survivor evidence checked | Real named survivors, or the dip claim is marked unproven |
| Sunk cost zeroed | Framed as a gift already received, never as debt still owed |
| Decision judged on information | No outcome-language ("it's going well/badly") drives the verdict |
| Verdict is one of three | PERSIST / QUIT / REDESIGN — never a hedge |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/ash-learning-scorecard` | Track the evidence quality feeding the decision-vs-outcome test over time |
| `/constraint-audit` | Confirm the hard part is the real bottleneck before classifying it dip or slope |
| `/daisy-chain` | Check the quit-or-persist call against the other life domains it will pull on |
| `/dan-martell-business-scaling` | Forward-only asset-building plan once the verdict lands PERSIST or REDESIGN |
