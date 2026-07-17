# Split-the-Word Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Foundation
> **Produces**: Category Verdict
> **Slash Command**: `/gmind-split-the-word`

---

## Purpose

Fuzzy words carry hidden weight. "I'm an entrepreneur," "I'm being authentic," "this is my business" — each of these does silent work in a decision, and none of them means one thing. Godin's move: find the load-bearing noun, cleave it into two crisp categories, give a one-line test that assigns the asker to a pole, then advise — differently — per pole. *"It's when you're confused that the stress kicks in."* The deliverable resolves category confusion because that's where the stress lives, not because the advice itself changed.

---

## Inputs Required

1. **The Self-Description** — the word doing unexamined work ("I'm an entrepreneur," "this is a business," "I need to be authentic," "that was a good decision").
2. **The Context** — what's being decided or diagnosed using this word.

---

## Workflow

### Step 1: Diagnose — Find the Load-Bearing Fuzzy Noun

Scan the input for the word carrying more than one meaning at once. Confusion, not lack of effort, is usually the actual source of stress: *"It's when you're confused that the stress kicks in."* If the asker can't self-classify in one sentence, the word hasn't been split yet.

### Step 2: Define the Two Poles

State both poles plainly, with a proper noun or scene anchoring each side where possible. Don't soften either pole into a spectrum — Godin's splits are binary, not gradient.

### Step 3: Give the One-Line Assignment Test

State the test as a single sentence the asker can apply to themselves right now, no worksheet required.

### Step 4: Deliver Pole-Specific Advice

The advice differs by pole — never give the same guidance to both sides of the split. Freelancers get "get better clients," entrepreneurs get "build the asset that runs without you." Confusing the two poles ("hire yourself out more" advice given to someone trying to build an institution) is the exact failure Godin diagnoses in the freelancer trap: *"every time times get tough, they hire the best available cheapest person. You know who that is? Themselves. Cuz they work for free."*

---

## Canonical Splits (Reference Table)

| Split | Verbatim Test | Pole-Specific Advice |
|---|---|---|
| **Entrepreneur / Freelancer** | *"An entrepreneur makes money when they're asleep. If you are doing the work, you're probably a freelancer."* | Freelancer: guard your time like gold, get better clients not more clients — *"You can't have more clients, cuz you're a freelancer. But you can have better clients. Better clients challenge you more, pay you more, talk about you more."* Entrepreneur: build the asset that doesn't need you in the room — *"I managed to make it so that there were a whole parts of the operation that I didn't touch. That's how I grew up as an entrepreneur."* |
| **Brand / Logo** | *"If they came out with a line of hotels, we all know what it would be like. Hyatt doesn't have a brand. There's just a logo. If they came out with a line of sneakers, we have no clue what it would be like."* | Full treatment lives in `/godin-brand-promise` (seth-godin-brand skill) — cross-reference rather than duplicate. |
| **Hobby / Business** | *"As soon as you turn it into a business, it's not yours anymore. It's the customers... Everyone always picks their best option."* | Hobby: don't monetize what's giving you joy on your terms — *"Don't let a business ruin your hobby."* Business: serve the customer's ledger, never sell on friendship — *"if that's how you're getting listings, you're not being of service."* |
| **Decision / Outcome** | *"Would a good decision-maker choose what I chose? If the answer is yes, then you made a good decision."* | Decision quality: judge on information-at-the-time only. Outcome: irrelevant to the verdict — *"If you buy a lottery ticket and win the lottery, you made a bad decision."* Anti-paralysis unlock: *"I don't have to guarantee the outcome."* |
| **Problem / Situation** (Part 2) | *"Problems have solutions. Situations do not."* Engineer's calibration: *"You can't rewrite the laws of physics. You can't be in two cities at the same time."* | Situation: acceptance is the only move — off the hook. Problem: on the hook — *"I might not like the solution... Still a solution. We just don't want to do it."* The salary case: 15 uncomfortable minutes a year IS the solution. *"The easy ones are already gone."* |
| **But / And** (Part 2) | *"I'm on vacation but it's raining"* = ruined; *"I'm on vacation and it's raining"* = *"now what am I going to do with that?"* | But-sentences: the excuse lives in the but-clause — rewrite with "and," then classify what remains as problem or situation. And-sentences: both things stay true, no one becomes the excuse — *"they don't become the excuse. They just become one of the problems or the facts of what you're dealing with."* |
| **Quality: spec / luxury / zero-defect** (Part 2) | *"Quality means three different things"* — the Camry meets spec; the Rolls is luxury mislabeled quality; zero-defect is *"the kind we use as an excuse to be a perfectionist."* | Meets-spec: ship the minute spec is met — full treatment in `/gmind-ship-check`. Luxury: a positioning choice, not a virtue. Zero-defect: *"The point of perfectionism is not to make it better. It's to keep you from shipping it."* |

---

## Output Schema

```
CATEGORY VERDICT
==================

The Fuzzy Word: [word doing hidden work]

Pole A: [name] — [one-line definition]
Pole B: [name] — [one-line definition]

Assignment Test: [one sentence, self-applicable]

Verdict: [which pole the asker lands on, and why — cite the test result]

Pole-Specific Advice:
[the guidance for THIS pole only — not generic advice that ignores the split]
```

---

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Binary, Not Gradient | Two poles stated, no third "it's a spectrum" hedge |
| Self-Applicable Test | The assignment test is one sentence the asker can run without a worksheet |
| Pole-Specific Advice | Advice differs materially by pole — same advice for both poles fails this gate |
| Confusion Named as Stress Source | Output states plainly that category confusion, not effort, is producing the stress |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/godin-brand-promise` | Brand/logo split hands off directly into the Nike/Hyatt diagnostic |
| `/gmind-hire-yourself-audit` | Entrepreneur/freelancer split feeds directly into task-tagging for burnout diagnosis |
| `/gmind-quit-or-dip` | Decision/outcome split is the precondition for a clean quit-or-persist call |
| `/nate-b-jones-intent-engineering` | Category confusion diagnosis pairs with intent clarification work |
