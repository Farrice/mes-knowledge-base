---
description: Turn a book into top-of-funnel for a DIFFERENT product — the shoulder-topic book that uses your real offer as its worked example, plus the book-as-webinar-close bonus
tier: 3
stacks_with: /sean-dollwet-kdp-publishing, /nicolas-cole-nonfiction-value-architecture, /sv-webinar-script
---

# /sv-book-funnel-bridge — The Book That Sells the Other Thing

Produces the **book-to-offer bridge**: the shoulder-topic thesis, the worked-example placement strategy, the attribution tracking, and the webinar-close bonus play.

Sam's book teaches **marketing** — how to build an email list, build a first funnel, build a flywheel. Her business sells **legal templates**. Everyone told her it wouldn't work: *"everyone disagreed with me at the time because my book is about marketing and online business, not legal stuff, and everyone said that's not going to drive anything to your business."*

It became a measurable acquisition path: *"I actually discovered Sam through the book, then joined her newsletter, and then bought the Ultimate Bundle."*

## Pre-Flight Gate

Load `genius.md`. The structural question:

> **What is the shoulder topic — the problem adjacent to your product that your buyer never stops having?**

Sam's product solves a problem people *exit*: *"If I went and got a filling at the dentist, I don't need to get his newsletter about what a filling is. I've done it already. It's over."* So she writes about the problem they never finish: getting customers.

If your product's problem is ongoing and never exits, the shoulder play is less necessary — write about the core problem and say so.

**Cannibalization check**: Nathan raises it directly — authors whose book closely mirrors their course *"often talk about cannibalizing sales."* Sam's answer is that hers are *"extremely different."* If the book substantially teaches the course, this play does not apply.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md`
3. `skills/sam-vander-wielen/references/cross-domain-patterns.md`
4. The book (existing or planned) + the product it should feed

## Execution

### Step 1 — Name the shoulder topic

Write: *"My product solves [PROBLEM THEY EXIT]. My buyer never stops having [ADJACENT PROBLEM]. The book is about [ADJACENT PROBLEM]."*

Test it against the exit logic. If the reader would still want this content two years after buying your product, it's a real shoulder topic.

### Step 2 — Place the product as the worked example

**This is the mechanic that makes the book a funnel rather than a brand asset.** Sam: *"I very strategically used my product, the Ultimate Bundle, in the book as the example — obviously — of what I built."*

The reader picks it up to learn the shoulder topic and *incidentally becomes fluent in your product.* Map the placements:
- Where the product appears as the case study
- Where its numbers illustrate the shoulder lesson
- Where the reader is shown the product's mechanics without being sold

Rule: the product is **evidence for the book's argument**, never an ad inside it.

### Step 3 — Build the path

Book → newsletter → offer. The book's CTA points at the **newsletter**, not the checkout. Sam's observed path has three steps, and the middle one does the conversion work over months.

### Step 4 — Instrument attribution

Sam runs a post-purchase survey asking where they heard of her **and** *"what are all the places that you consumed content from me before you decided to purchase"* — newsletter, how long on it, roughly how many issues read, podcast, roughly how many episodes.

Build the equivalent. Without it the book's contribution is invisible and you'll conclude it didn't work.

### Step 5 — The webinar-close bonus play

The book becomes the bonus that answers the gap the webinar teaching opens. Sam holds up the physical copy at the close (full script in `/sv-webinar-script`, Beat 5):

> *"Today I've taught you all the legal steps. But even if you do that — how are you getting customers? How are you building an email list? It's all right here. And I'm going to send it to you for free if you purchase right now."*

The shoulder topic **is** the gap. That's why the book works as the bonus: it's the same structural relationship, deployed at the close.

Result: *"the most on-webinar signups ever"* — 128 in five or six minutes.

### Step 6 — Consider the missing upsell

Sam names this as a mistake: the book's content could have been an email-marketing course sold as an upsell. *"I could easily crank out an email marketing course of some sort… people ask me for it all the time."* If the shoulder topic has real demand, plan the paid version.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **No book yet** | Same architecture applies to a long-form free resource, a signature talk, or a podcast season. The book is a format, not a requirement |
| **Book closely mirrors the course** | Play does not apply — cannibalization is real. Differentiate the book first |
| **Product problem never exits** | Shoulder play optional; write about the core problem |
| **Physical bonus infeasible** | Digital copy at close, physical shipped to buyers over a price threshold |
| **B2B** | Shoulder topic is usually the buyer's *career* problem, not the company's |

## Output Schema

```
BOOK FUNNEL BRIDGE — [Book] → [Product]

## Shoulder Topic
Product solves (exits): [ ]
Buyer never stops having: [ ]
Book is about: [ ]
Exit test: PASS/FAIL
Cannibalization check: PASS/FAIL + reasoning

## Worked-Example Placements
| Chapter/section | How the product appears | Evidence or ad? |

## The Path
Book CTA → [destination] → [nurture] → offer
Expected lag: [ ]

## Attribution Instrument
Post-purchase survey questions:
1. Where did you first hear of me?
2. All places you consumed content before purchasing?
3. Newsletter: how long / roughly how many issues?
4. Podcast: roughly how many episodes?

## Webinar Close Bonus
The gap the teaching opens: [ ]
How the book answers it: [ ]
Close script pointer: /sv-webinar-script Beat 5
Physical or digital: [ ]

## Upsell Option
Is there paid demand for the shoulder topic? [ ]
```

## Quality Gate

Reject and rebuild if:
- The book substantially teaches the paid product (cannibalization)
- The product appears as an advertisement inside the book rather than as evidence
- The book's CTA points at the checkout instead of the nurture asset
- No attribution instrument exists — the book's contribution will be invisible
- The shoulder topic fails the exit test (the reader wouldn't want it two years post-purchase)
- The close bonus doesn't answer the gap the teaching actually opened

**Execution prompt**: `references/prompts-v2/book-funnel-bridge.md`
