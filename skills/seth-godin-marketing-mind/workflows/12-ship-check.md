# Ship Check Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Practitioner
> **Produces**: Ship Verdict
> **Slash Command**: `/gmind-ship-check`

---

## Purpose

Perfectionism gets treated as a moral failure, not a personality trait — withholding something that would help someone is the thing that needs defending, not the shipping of it. Asked how to spot perfectionism in a restaurant owner, an artist, a copywriter, or a baker who's never sent the flyer, Godin skips the diagnosis of why they're stuck and goes straight to the stakes: *"Who's it for and what's it for? If what you're offering is going to make someone's life better how dare you hold it back?"* This workflow runs that flip on any unshipped thing, then sorts it into a verdict — ship now, ship to a few, or fix a named spec gap.

---

## Inputs Required

1. **The Unshipped Thing** — what's being withheld, specifically. Not "my business" — the actual asset: the flyer, the offer, the draft, the menu, the launch.
2. **Who's Being Held Back From It** — the person or few people this would help, named if possible, not "the market."
3. **The Stated Reason for Holding It** — "not ready," "not perfect," "needs one more pass." Get the exact excuse before treating it.

---

## Workflow

### Step 1: Diagnose — What's Being Withheld, and From Whom

Before applying pressure, name the two things precisely: what isn't shipping, and who doesn't have it because of that. The restaurant owner, the artist, the copywriter, and the baker in Godin's own list all share one shape — *"you're constantly tweaking the menu and you have to get it just right or you're an artist who has all this unfinished stuff or you're a writer and you know, you're working on marketing copy but you can't quite... or you're baker and you're fussing over the flyer you've just never sent out."* If the diagnosis stops at "perfectionism," it hasn't located the actual withheld thing yet.

### Step 2: The Moral Flip

State the reframe as delivered — pressure, not comfort: *"If what you're offering is going to make someone's life better how dare you hold it back? How dare you take this thing that isn't perfect but is meeting spec, that is good enough. How dare you hold it back and let that person flounder?"* This isn't permission to ship sloppy work. It's a refusal to accept "not perfect yet" as a reason to withhold something that already clears the bar of helping someone.

### Step 3: The Meeting-Spec Test

Spec isn't a vague standard — it's the answer to who's-it-for and what's-it-for, already defined. If those two questions have specific answers (cross-reference `/gmind-two-questions`), spec is knowable, and the test is binary: does this thing do the job it was built to do for the person it was built for? *"How dare you take this thing that isn't perfect but is meeting spec, that is good enough."* Meeting spec and being perfect are different bars — only the first one is required to ship.

### Step 4: Risk Calibration

Size the actual downside of shipping something that turns out not to work: *"If it doesn't work, a few people discovered it didn't work. You're not doing surgery, it's okay. Go make it better. If it does work, go do the new thing."* Most withheld work is being protected from a risk that doesn't match its actual stakes — a flyer, a draft, a menu item is reversible. Naming the real (usually small) cost of a miss is often what unsticks the ship decision on its own.

### Step 5: The Misdirected-Effort Check

Sometimes the polishing isn't fear — it's effort aimed at the wrong lever entirely. His case: *"if you're busy tweaking the menu and tweaking the menu and it's teenagers eating pizza in the suburbs, why? You didn't do anything to help their problem. You should be spending all your time installing a new kind of jukebox, spend all your time organizing community bus trips, doing something that will actually help the people you're here to help."* Before ruling this a shipping problem, check whether the effort is even pointed at what the audience needs — a perfect menu doesn't fix a jukebox problem.

### Step 6: The Verdict

Sort the unshipped thing into one of three outcomes:

- **SHIP NOW** — meets spec, risk is small and reversible, effort is correctly aimed. No more passes.
- **SHIP TO FEW** — not ready for everyone, ready for a handful: *"Instead you can show up and we're not talking about for the world, for a few people and say here I made this and watch what happens."*
- **GENUINE SPEC GAP** — the thing doesn't yet do the job it was built to do for who it was built for. Name the specific gap. Fix only that, then re-run Step 3.

---

## Output Schema

```
SHIP VERDICT
=============

The Unshipped Thing: [specific asset]
Who's Being Held Back From It: [named person or few people]
Stated Reason for Holding: [the excuse, verbatim]

Spec Check:
- Who's it for: [ ]
- What's it for: [ ]
- Meets spec? [Y/N]

Risk If It Doesn't Work: [named, sized — reversible or not]
Misdirected-Effort Check: [is the polishing aimed at what the audience actually needs, or somewhere else]

VERDICT: [SHIP NOW / SHIP TO FEW / GENUINE SPEC GAP]
If GENUINE SPEC GAP → The specific gap: [name only this — nothing else gets touched]
```

---

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Withheld Thing Named | The audit targets a specific asset, not a general feeling of not-readiness |
| Spec Before Ship | Meeting-spec test run against named who's-it-for/what's-it-for answers, not a vibe check |
| Risk Sized Honestly | The downside of a miss is stated concretely — never left as unspecified dread |
| One Gap, Not a List | GENUINE SPEC GAP verdicts name exactly one fix, not a rewritten to-do list |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/gmind-two-questions` | Spec is only knowable once who's-it-for/what's-it-for are specific — run that first if spec is undefined |
| `/gmind-fear-isolate` | If the withholding traces to fear of a transaction rather than genuine spec gaps, hand off to the fear-experiment workflow |
| `/ship-it` | Ship Check produces the verdict; ship-it handles the mechanics of the actual release |
| `/drk-resistance` | Chronic ship-avoidance across multiple assets is a resistance pattern, not a series of unrelated spec gaps |
