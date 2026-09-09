---
description: Turn a review, ranking, award, or closing into content people who aren't hiring today will still see and remember — hook-line posts, green-screen news, breaking-news frames, and closing-day capture
---

# /alyssa-stalker-authority-as-story — Never a Screenshot

A screenshot review is "swipe, it's irrelevant to me" to anyone not hiring right now [31:28–31:31]. Instead: "take one line out of the review, find the hook line, make that the hook of a post, and then break down the story of the transaction and why they said that about you" [30:52–31:04]. Awards get green-screened as news with "what I did differently" [29:19–29:29]. Testimonials get filmed "when you're handing them the keys" [32:49–32:52]. Authority is the smallest slice of the mix, about monthly, and it "hits them in their head" even when nobody shares it [28:04–28:34].

## Pre-Flight Gate

Load `genius.md` Patterns 11, 12 and anti-patterns 1, 4, 8. Required: the actual review text, ranking, award, or a closing date plus the transaction story. Never invent a review or a client quote. If only a star rating exists, this workflow produces a capture plan, not a post.

## Skill Acquisition

- `genius.md` — Patterns 11, 12
- For Jen: `_active/clients/jen-listings/CLAUDE.md` anti-patterns ("As a top 1% agent" is banned; humility is on-brand) — authority for Jen is the client's story, never her rank
- `luke-iha` proof ladder if the review needs to become a proof object in a sales asset

## Diagnose Before Treat

Classify the input: **review** (words exist), **ranking/award** (a third party said it), **result** (10% over ask, keys handed), or **upcoming closing** (nothing captured yet). Each has a different first move: hook-line, green-screen, story carousel, capture plan.

## Execution

### A. Review → hook-line post [30:52–31:04]
1. Pull the one line a stranger would stop on. Quote it exactly.
2. Make it slide 1 or the spoken hook.
3. Tell the transaction story in 3–4 beats: the client's situation, the moment it got hard, what you did, why they said that line.
4. Frame it so the *next* client sees themselves: "framing this specific client scenario as something relatable to the next person that you want to help" [28:47–28:54].

### B. Ranking / award → green-screen news [29:12–29:51]
1. Green-screen the article or build a news-style card (not an AI graphic).
2. Script: "You want to know how I got on this list? Well, let me tell you" → three things you did differently → what it means for the person watching.
3. Alternative frame: "breaking news" about yourself, Tatiana Londono style — "you won't believe what this client said about her agent," swipe to the review [32:11–32:32].

### C. Result → story carousel
1. Slide 1: the result as the client felt it, not the number alone.
2. Middle: the two or three decisions that produced it.
3. Payoff: "that's the kind of [buyer/seller] I love working with."

### D. Upcoming closing → capture plan [32:38–33:17]
1. Ask at the emotional peak: keys in hand, 10% over ask, closing day.
2. "Hey, really quick, I want to do a quick video" — pull the phone.
3. Question list (5–6): what were you most nervous about; what surprised you; what would you tell a friend in your shoes; what did I do that you didn't expect.
4. Comedic variant: ask one question, cut the answer to a different question (Katie Day / Tom Ferry room) [33:20–34:02] — only if the agent is "funny and fun and playful" [33:49–33:52].
5. Clip later; one message per clip.

### E. Cadence + expectation
- Slot it about monthly [28:04–28:06].
- Pre-declare: fewer likes than local content; the job is memory [27:04–27:10], [28:27–28:34].

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| Carousel | A or C |
| Reel | B (green-screen) or D (clipped testimonial) |
| Story | One hook line + "here's the story" link to the post |
| Single image | The hook line over a real photo from the closing |
| Create-mode text post | The hook line alone, credited to "a client last week" |

## Output Schema

```markdown
# AUTHORITY STORY PACK — [agent] — [input type]

## Input
- Type: review / ranking / result / upcoming closing
- Verbatim: "…" (or "none captured yet")

## A. Hook-line post (if review)
- Hook line: "…"
- Story beats: 1… 2… 3… 4…
- Next-client frame: …

## B. Green-screen / breaking-news script (if ranking)
- Card text:
- Script (≤30 s):
- "What I did differently" ×3:

## C. Story carousel (if result)
| Slide | Text |

## D. Capture plan (if upcoming)
- Moment:
- Ask line:
- Questions ×6:
- Comedic variant: [yes/no + why]

## Cadence + expectation
Slot: [date] · Expected: fewer likes; memory, not engagement

## Handoff → 07-content-mix-planner / posting queue
- Output produced: Authority Story Pack
- Next input: the post + its authority slot
- Validation: no screenshot, no "look at me," client story present [yes/no]
- Open risk: [client consent to use words/video]
```

Execution prompt: `references/prompts-v2/authority-story-pack.md` — honor its Output Contract.

## Quality Gate

- Is the client's actual language quoted, never paraphrased into a claim?
- Does the next client see themselves in the story?
- Is there zero screenshot-of-review and zero "as a top X agent"?
- Is the cadence about monthly and the like-count expectation pre-declared?
- Does the capture plan hit the emotional peak, not weeks later?
- Consent: does the agent have the client's OK to use the words or footage?
