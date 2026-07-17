# Premise Audit Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Foundation
> **Produces**: Premise Audit Report
> **Slash Command**: `/gmind-premise-audit`

---

## Purpose

Most questions arrive broken. Someone asks "how do I show up more consistently" and the question itself is the problem — it assumes reach-marketing works, that hustle is the missing ingredient, that outcomes prove decisions, or that the founder has to be the face of the thing. Godin never treats a broken question as answerable. He names the trap, answers a different question first — the one the asker will actually need — then returns to the original, now trivial or dissolved. This workflow runs that sequence on any live brief, question, or plan.

---

## Inputs Required

1. **The Question or Brief** — verbatim, as asked. Don't paraphrase it smoother before running the audit; the trap often lives in the exact wording.
2. **Who's Asking** — freelancer, founder, employee, client — context for what "six months from now" looks like for them.
3. **What They Think They Need** — the tactical ask on the surface.

---

## Workflow

### Step 1: Diagnose Before Treat — Scan for the Embedded Assumption

Read the question for which of the four trap families is doing invisible work:

- **Reach-marketing trap** — the question assumes "getting the word out" is the job. *"Marketing is not about getting the word out. Marketing is not showing up in social media or in other places, becoming familiar, and then people just give up and buy from you. That's not how it works."*
- **Hustle trap** — the question assumes more effort, more hours, more clients is the fix. *"There's a dead zone in between there... that zone of eight people or 18 people or 30 people where you're doing all the jobs, you're not getting paid enough, you're too busy to do anything, and you're stressed out of your mind."*
- **Outcome-judgment trap** — the question judges a choice by how it turned out. *"Did it turn out well?" "Yeah." "That's what everybody says. They're completely unrelated."*
- **Founder-centrality trap** — the question assumes the person has to be the face, the maker, the one answering every review. *"I am authentically me, please punch me in the face... it should be about the customer."*
- **Waiting-for-permission trap** (Part 2) — the question assumes someone else authorizes the start: a publisher, a platform, a boss, an audience threshold, "feeling ready." *"No one's forcing you to not wait. You're choosing to wait. What a safe, lovely place to hang out... Congratulations. You've built a perfect place to hide."* Route rich cases to `/gmind-pick-yourself`.

Do not proceed until one trap family is named. If none fits cleanly, say so — a forced trap is worse than no trap.

### Step 2: Name the Trap in One Line

State it flat, before any content, the way he does it to a friendly host on air: *"What a trap, Mel. What a trap."* No cushioning, no "great question, but." The naming is the first move, not a preamble to the real answer.

### Step 3: Find the Six-Months-From-Now Question

Ask what this person will be blocked by once the asked question is solved. Granola-Saturday isn't really about Saturday: *"Business is almost never about what you make right now... The number of times you're going to be in the kitchen inventing a new kind of granola is close to zero. So, we should take a really deep breath before we even get there and say, how do you want to spend your day?"* The question behind the question is usually about logistics, capacity, or identity — not the craft itself.

### Step 4: Answer Upstream With the Explicit Detour

Flag the redirect out loud, get consent, then answer the deeper question first: *"So, I want to answer a different question and then we're going to come back to."* Deliver the upstream answer with a concrete enumeration, not a vague gesture — his version names the actual disciplines: *"These are issues of logistics and marketing and packaging and customer service and finance and supply chain and management of people."*

### Step 5: Return to the Asked Question — Now Trivial or Reframed

Come back to the original ask. Either it answers itself now, or it needs one line to close. If the trap was reach-marketing, the return line is a mechanism swap, not a tactic: *"You tell a story. This story creates tension... but then what you want is for people to relieve the tension by buying from you."* Don't re-litigate the trap here — it's already named. Just close the loop.

---

## Output Schema

```
PREMISE AUDIT REPORT
=====================

Question As Asked: [verbatim]

Trap Family: [Reach-Marketing / Hustle / Outcome-Judgment / Founder-Centrality]
Trap Named: [one line, no cushioning]

The Six-Months-From-Now Question: [what they'll actually be blocked by]

Upstream Answer:
[the detour — answered explicitly, with named disciplines/mechanisms, not vague gestures]

Return to the Asked Question:
[now trivial, or reframed in one line]
```

---

Execution prompt: `references/prompts-v2/premise-audit-report.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Trap Named First | The trap is stated before any content — not buried after advice |
| Upstream Specificity | The detour answer names concrete mechanisms (logistics, tension, capacity) — not "focus on the fundamentals" |
| Case Carried | At least one named micro-case or verbatim anchor from the source per audit |
| No Re-Litigation | The return-to-question step closes in one line — doesn't repeat Step 2 |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/april-dunford` | Premise audit clears the ground before positioning work starts |
| `/icp-build` | Trap detection catches "everyone" ICPs before they're formalized |
| `/gmind-two-questions` | Natural sequel once the premise is cleared — run who's-it-for/what's-it-for next |
| `/kallaway-content-psychology` | Reach-marketing trap detection pairs with attention-psychology diagnosis |
