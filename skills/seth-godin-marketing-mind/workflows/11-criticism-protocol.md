# Criticism Protocol Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Practitioner
> **Produces**: Criticism Response
> **Slash Command**: `/gmind-criticism-protocol`

---

## Purpose

Criticism gets processed as information about the critic, never as a verdict on the creator. Godin's answer to "how do you process feedback and not hide in the sand" starts with a redirection of ownership: *"When someone criticizes your product, they are not criticizing you. They're saying, 'Based on who I am and what I see, I don't want this.'"* Everything downstream — the enrollment check, the refund, the boundary against one-star reviews — is a design response to that reframe, not an emotional-resilience trick. This workflow runs the full sequence on live incoming criticism: a client complaint, a bad review, a pushback on pricing.

---

## Inputs Required

1. **The Criticism As Received** — verbatim, not smoothed over. A review, a DM, a client email, a comment.
2. **Relationship to the Critic** — client, paying customer, stranger, or chronic reviewer. The response differs.
3. **Source Filter Check** — before responding at all, does this person deeply care, do similar work, or hold an opinion the asker actually respects?

---

## Workflow

### Step 1: Diagnose — Depersonalize Before Responding

Before drafting anything, restate the criticism in the critic's terms, not the creator's wound. *"They're saying, 'Based on who I am and what I see, I don't want this.'"* This is not the same sentence as "my work is bad." If the draft response defends the work's quality, it's answering the wrong charge — the critic is describing a mismatch between who they are and what was offered, not delivering a quality verdict.

### Step 2: Never Persuade Them They're Wrong

Getting defensive costs the relationship outright: *"And if you get defensive and tell them they're wrong, you've helped no one. It doesn't matter what you want, and it doesn't matter what you like. It matters the customers you have chosen to serve."* And the mechanism for why arguing backfires specifically: *"As soon as you say you're wrong, they're not your customer anymore."* Correcting the critic doesn't win them back — it ends the relationship on the spot.

### Step 3: The Enrollment Check

Instead of arguing the point, check for continued buy-in to where the work is headed: *"I'm not going to persuade you you're wrong. I'm going to ask you if you're enrolled in the journey."* This reframes the conversation from "was this good" to "are we still going the same direction" — a question the critic can answer honestly without either party losing face.

### Step 4: The Refund-With-Trust Move

If the answer is no, release them completely and without resentment: *"if not, thank you so much for telling me your truth. Here's everything back. I don't care that you're ripping me off, because you're not ripping me off cuz you trusted me. And now I'm trusting you, and we can move on."* The refund isn't a loss to be minimized — it's the trust exchange completing itself. Holding onto the money after someone has said no costs more than the refund does.

### Step 5: "It's Not for You" as a Complete Sentence

Close the exchange without an apology tacked on: *"'It's not for you' is a totally legitimate sentence."* No hedge, no "sorry you feel that way," no attempt to soften it into agreement. State it and stop.

### Step 6: Boundary Design for Chronic Criticism

For criticism that recurs rather than arrives once — reviews, ratings, ongoing feedback streams — the fix is architectural, not attitudinal: *"if a one-star review on Google is going to ruin your whole day and push you to change a menu that's working, you need to create a boundary so you never even see a one-star review on Google cuz it's not relevant to the success of what you're trying to build. So, forgive that person and move on."* If the boundary needs staffing, staff it: *"if you need to hire a person whose only job is to send nice notes to people [who] give you one-star reviews, fine. But you don't want to hear about it."* The instruction is never "develop thicker skin" — it's remove the input.

### Step 7: The Criticism-Source Filter

Before any criticism gets weight at all, filter for who's allowed to have a vote: *"Everybody has a megaphone. Everybody can tell you what they think, but I'd really only take that criticism from somebody who deeply cares or somebody who's already doing something similar or somebody whose opinion you respect."* Three tests, any one qualifies: deep care, doing similar work, or respected judgment. Criticism that clears none of the three gets the boundary from Step 6, not a response.

---

## Output Schema

```
CRITICISM RESPONSE
====================

The Criticism (verbatim): [as received]
Relationship to Critic: [client / customer / stranger / chronic reviewer]

Source Filter:
- Deeply cares? [Y/N]
- Doing similar work? [Y/N]
- Opinion respected? [Y/N]
→ Verdict: [RESPOND / BOUNDARY — no response, forgive and move on]

If RESPOND:
Depersonalized Restatement: [the critic's mismatch, not a quality verdict]
Enrollment Check: [are they still enrolled in the journey — asked, not assumed]
If not enrolled → Refund-With-Trust: [issued, no argument, gratitude stated]
Closing Line: "It's not for you." [no apology appended]

If BOUNDARY:
What's being removed from view: [one-star reviews / recurring low-signal feedback / named channel]
Who owns the boundary: [self / hired nice-notes role]
```

---

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Depersonalized First | The critic's statement is reframed as a mismatch before any response is drafted |
| No Persuasion Attempt | The response never argues the critic into agreeing the work is good |
| Filter Applied | Source filter run before weight is given — deep care, similar work, or respected opinion, at least one |
| No Apology Tacked On | "It's not for you" stands alone; no softening clause added after it |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/godin-false-proxy-purge` | Full metrics-replacement diagnostic for the dashboard/measurement system — this workflow handles the incoming-criticism moment, that one handles what gets measured at all |
| `/gmind-two-questions` | Enrollment check is easiest to run when who's-it-for is already specific — vague positioning makes every critic look "enrolled" by default |
| `/drk-resistance` | Boundary design against chronic criticism pairs with resistance-pattern diagnosis for operators who compulsively check reviews |
| `/luke-iha-client-mastery` | Client-specific criticism (pricing pushback, scope complaints) routes through the enrollment check before any renegotiation |
