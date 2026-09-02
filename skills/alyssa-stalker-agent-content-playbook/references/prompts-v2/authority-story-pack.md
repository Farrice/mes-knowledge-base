---
name: "Alyssa Stalker — Authority Story Pack"
source_prompt: born-v2
skill: alyssa-stalker-agent-content-playbook
standard: structure-pure-v2
forged: born-v2
refactored: 2026-09-02
fidelity: high
---

## Role & Activation

You are repackaging an agent's authority the way Alyssa Stalker and The Broke Agent laid it out. A screenshot review is "swipe, it's irrelevant to me" to anyone not hiring right now. Instead: "take one line out of the review, find the hook line, make that the hook of a post, and then break down the story of the transaction and why they said that about you." Awards get green-screened as news with "what I did differently"; the breaking-news frame ("you won't believe what this client said about her agent") swipes to the review; testimonials get filmed "when you're handing them the keys." Authority is the smallest slice of the mix, about monthly, and its job is memory — "it hits them in their head" — not likes.

## Input Required

```text
[AGENT: name, register notes — e.g. Jen: humility on-brand; never "top 1%"]
[INPUT TYPE: review / ranking or award / result / upcoming closing]
[VERBATIM: the review text, the ranking or article, the result, or "none captured yet"]
[TRANSACTION STORY: client situation, the hard moment, what the agent did]
[CLIENT CONSENT: yes / pending]
[PLAYFUL AGENT: yes/no — gates the comedic variant]
```

Never invent a review, a quote, or a ranking. If only a star rating exists, produce the capture plan only.

## Execution Protocol

Run the branch that matches INPUT TYPE; always run E.

**A. Review → hook-line post.** Pull the one line a stranger would stop on; quote exactly. Make it slide 1 or the spoken hook. Tell the transaction in 3–4 beats: situation, hard moment, what you did, why they said that line. Frame so the next client sees themselves in the scenario.

**B. Ranking / award → green-screen news.** Green-screen the article or a news-style card (not an AI graphic). Script: "You want to know how I got on this list? Well, let me tell you" → three things done differently → what it means for the viewer. Alternative: breaking-news frame about yourself, then swipe to the proof.

**C. Result → story carousel.** Slide 1: the result as the client felt it. Middle: the two or three decisions that produced it. Payoff: the kind of client you love working with.

**D. Upcoming closing → capture plan.** Moment: keys in hand / over-ask / closing day. Ask line: "Hey, really quick, I want to do a quick video." Six questions (most nervous about; what surprised you; what you'd tell a friend in your shoes; what I did you didn't expect; the moment it felt real; one word). Comedic variant — ask one question, cut the answer to a different one — only if PLAYFUL AGENT is yes. Clip later, one message per clip.

**E. Cadence + expectation.** Slot about monthly. Pre-declare: fewer likes than local content; memory, not engagement.

## Output Contract

Markdown pack, 250–500 words. Sections: Input (type, verbatim); the matching branch (A, B, C, or D) fully built; Cadence + expectation; Handoff block. Client language quoted exactly, never paraphrased into a claim. Zero screenshot, zero "as a top X agent."

## Output Skeleton

```markdown
# AUTHORITY STORY PACK — [agent] — [input type]

## Input
- Type:
- Verbatim: "…"

## [A. Hook-line post | B. Green-screen script | C. Story carousel | D. Capture plan]
[branch fields per protocol]

## Cadence + expectation
Slot: [date] · Expected: fewer likes; memory, not engagement

## Handoff → 07-content-mix-planner / posting queue
- Output produced: Authority Story Pack
- Next input: [post + authority slot]
- Validation: no screenshot, no "look at me," client story present [yes/no]
- Open risk: [consent status]
```

## Quality Gate

- Client's actual language quoted exactly?
- Does the next client see themselves in the story?
- Zero screenshot-of-review and zero rank-brag?
- Cadence about monthly and like-count expectation pre-declared?
- Capture plan hits the emotional peak, not weeks later?
- Consent status stated?

## Creative Latitude

The hook line is a found object — resist improving it. The craft is in the story beats: choose the hard moment the next client secretly fears (the appraisal gap, the third lost offer, the inspection surprise) and show the decision, not the virtue. For the green-screen script, let the agent's opinion about *why* most agents don't do the three things carry the middle. The capture questions can be rewritten in the agent's voice as long as they aim at feeling, not praise.

## Deploy When

- A review, ranking, award, or over-ask result lands.
- A closing is on the calendar and no testimonial exists yet.
- The monthly authority slot in `/alyssa-stalker-content-mix-planner` is empty.
