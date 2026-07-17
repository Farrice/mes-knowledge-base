# Fear Isolation & Experiment Design

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Practitioner
> **Produces**: Fear Experiment
> **Slash Command**: `/gmind-fear-isolate`

---

## Purpose

A stalled launch or avoided outreach is never a motivation problem — it's an unnamed fear wearing a task's clothes. Godin's method never coaches the feeling. It strips the task down to the smallest possible interaction, isolates the exact variable that's scary, and designs a runnable experiment that transacts with the fear directly instead of around it. Then it fixes the opening question, because most fear lives in the first "no" a prospect is allowed to say.

---

## Inputs Required

1. **Stalled Task** — What hasn't shipped, what outreach isn't happening, what's been "almost ready" too long.
2. **Substitute Activity** — What's the person doing instead that feels like progress but isn't the scary thing.
3. **The Ask** — The actual first move required: an email, a DM, a pitch, a cold call, a launch post.
4. **Current Opener** — The literal first sentence or question the prospect hears.

---

## Workflow

### Step 1: Diagnose the Substitute

Find what's stalled and name the comfortable activity standing in for it. Godin's counterfeit-work detector: *"'Oh, I know, I'll just post a whole bunch of pictures on Instagram instead.' That's not something you're afraid of, so you're going to do it, and it's not going to work."* Ask the operator: what have you been doing this week that looks like the work but was never the scary part? Write that activity down next to the task it's replacing. If nothing's been avoided, this workflow doesn't apply — go run `/gmind-ship-check` instead.

### Step 2: Strip to the Smallest Triggering Interaction

Reduce the stalled task to the smallest unit that still produces the fear. Use the bus-station logic directly: *"here's an exercise that you should actually try in real life. Go to the bus station and bring with you a $10 bill. And walk up to somebody and say, 'Will you give me a five for this $10 bill?'"* The exercise works because it isolates one variable — a stranger might say no to an obviously good deal — from everything else (product quality, market fit, timing) that usually gets blamed instead. Do the same reduction on the operator's task: cut it down until only the single scary interaction remains.

### Step 3: Name the Actual Fear Variable

State the fear in one sentence, stripped of task language. Godin's own diagnosis of the bus-station exercise: *"you're selling something that's obviously worth more than you're selling it for. It turns out that feeling is why you're afraid. You're afraid of having a transaction with somebody who might say no."* Most stalled launches trace to this same variable — not "the product isn't ready," but the transaction itself. Write the fear as: "I am afraid of [specific interaction] because [someone] might say no." No hedging language, no reframing into "readiness" or "quality" — the fear stays named as a transaction, not a task.

### Step 4: Design the Runnable Experiment

Build a version of the isolated interaction that can run this week, using the same shape as the bus-station test: cheap, fast, real stranger, real possible no. It doesn't need to be the full launch — it needs to trigger the exact fear from Step 3 and produce a result within days. Specify: who gets asked, what exactly is said, and how the no gets counted (not avoided, not explained away — counted as data). The point isn't to eliminate the fear before running it. The point is to run it while afraid.

### Step 5: Redesign the Opening Question

Audit the Current Opener for whether it can be answered with a flat no. Godin's Girl Scout case: *"I've trained thousands of Girl Scouts how to sell Girl Scout cookies... these 9-year-olds would yell, 'Want to buy some Girl Scout cookies?' And everyone's going to the supermarket, so they just would walk right by."* His redesign replaced the ask with a question everyone already has an answer to: *"What's your favorite kind of Girl Scout cookie?' It turns out everyone has an answer to that question... Their sales went through the roof cuz they got over the hard part of the interaction."* Rewrite the operator's opener the same way — find a question that invites an answer instead of a verdict, so engagement happens before commitment is requested.

### Step 6: Set the Fear Posture

Close with the standing instruction, not a promise of relief: *"We should name the fear. We cannot make it go away, but we can dance with it. Well, guess what? Transacting with strangers is going to trigger fear. It's the shadow, it's the same thing, two sides of the same coin. Do not deny it, do not pretend it's going to go away, it's real."* The experiment doesn't cure the fear — it runs alongside it. Flag any plan that depends on the fear disappearing first as a substitute activity in disguise.

---

## Output Schema

```
FEAR EXPERIMENT
================

Stalled Task: [what hasn't shipped]
Substitute Activity: [the comfortable stand-in, named]

FEAR VARIABLE:
[one sentence — the transaction, not the task]

THE EXPERIMENT (runs this week):
- Who: [specific person/stranger]
- What's said: [exact ask]
- How the no gets counted: [not avoided — logged]

OPENER REDESIGN:
- Old opener (answerable with no): [current line]
- New opener (everyone has an answer): [redesigned line]

FEAR POSTURE:
Named, not dissolved. The experiment runs while afraid, not after the fear clears.
```

---

Execution prompt: `references/prompts-v2/fear-experiment.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Substitute named | The comfortable stand-in activity is called out by name, not glossed over |
| Fear variable isolated | Fear is written as a transaction sentence, not a task-readiness excuse |
| Experiment runnable | Runs this week, cheap, produces a real possible no |
| Opener redesigned | New opener cannot be answered with a flat no |
| No comfort loop shipped | The plan doesn't quietly require the fear to disappear first |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/drk-resistance` | Diagnose whether the block is samskara-driven or ego-driven before designing the experiment |
| `/pmj-opener` | Low-resistance opener engineering to carry the Girl Scout redesign further |
| `/ash-offer-test` | Mafia-offer and commitment-ladder testing as a second runnable-experiment discipline |
| `/hughes-empathy-ladder` | Generate specific fear hypotheses on the prospect's side, not just the operator's |
