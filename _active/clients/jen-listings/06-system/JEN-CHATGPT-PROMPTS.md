# Jen's ChatGPT extraction pack (living; update in place)

Purpose (Farrice, 2026-09-02): "extract her live voice and voice profile from their conversations and sessions, and her memory and history... the quickest route to getting her content to sound like her." Not interviews. Every prompt reads what her account already holds and returns it in a fixed shape, so six outputs drop into this system without translation.

How to run: Farrice, in her ChatGPT with her login, once. Before prompt 1, check Settings → Personalization: **Memory on** and **Reference chat history on** (LIKELY the current setting names; if the second toggle is absent, the prompts still read saved memory, and "NOT IN HISTORY" answers will be more common). Start a fresh chat per prompt. Paste each output into `06-system/jen-chatgpt-outputs/<file>` using the filename at the bottom of each prompt. Nothing here is shown to Jen as a system; she reads the merged profile once and says "that's me" or "not me."

Every prompt carries the same preamble so the outputs stay uniform:

```
Use only what you already know about me: your saved memory of me and our past conversations. Do not invent, do not generalize from "typical realtors," do not use anything from the web. Quote me exactly where you can and put quotes in quotation marks. Mark every line either HERS (my exact words or a near-verbatim paraphrase) or INFERRED (your read of me). If you don't have something, write NOT IN HISTORY instead of guessing. Answer in plain markdown with exactly the headings I give you, no intro, no closing.
```

---

## Prompt 0 · what do you actually hold on me

```
[preamble]

List what you remember about me and what our past conversations cover, in these headings:

## Saved memories about me
(one line each, verbatim as stored if you can)

## Topics we've talked about
(one line per topic, with roughly when and how often)

## What I've asked you to write for me
(captions, posts, emails, scripts, bios: one line each, with the date if you have it)

## What I've told you I dislike or won't do
(one line each)

## Gaps
(what you'd need to know about me that isn't in your memory)
```
Save as: `00-inventory.md`

---

## Prompt 1 · my voice, from how I actually write and talk to you

```
[preamble]

Build a profile of how I write and talk, from my own messages to you and the things I've asked you to write and then corrected. Use these headings:

## Register
(2–4 lines: energy, warmth, formality, how I open, how I land a thought. Quote three of my messages that show it.)

## Sentence habits
(length, punctuation I lean on, lowercase or not, ellipses, exclamation points, emoji I actually use and where, how I sign off)

## Words and phrases I use often
(a list, each with one quoted example from me)

## Words and phrases I never use, or corrected you on
(a list; include what I replaced them with, if I did)

## How I explain real estate to someone who doesn't know it
(quote two or three examples where I explained a term or a step in my own words)

## The difference between how I talk about work and how I talk about my life
(2–4 lines with a quote for each)

## Ten lines that are most "me"
(numbered, quoted exactly, with what they were about)
```
Save as: `01-voice.md`

---

## Prompt 2 · my line bank

```
[preamble]

Pull every reusable line of mine you can find in memory and our history: things I've said to you about clients, buying, selling, money, stress, and my job. Quote exactly. Group them under these headings, at most twelve per heading, oldest date you have next to each:

## Openers (how I start a thought or a post)
## Reassurances (what I say when someone is scared or stuck)
## Closes and sign-offs
## Humor and sass
## How I describe what I do
## How I describe my clients and who I want to work with
## Lender and money words I use naturally (rates, buydowns, credit, down payment)
## Lines you wrote for me that I kept without changing
## Lines you wrote for me that I changed, and what I changed them to
```
Save as: `02-line-bank.md`

---

## Prompt 3 · the people I help, in my words

```
[preamble]

From what I've told you about my clients, my past deals, and who I'm trying to reach, build this:

## Who I say I help
(quote me; note where I've been specific about age, stage, budget, neighborhoods, buying vs selling)

## Where they are in life when they find me
(HERS quotes first, then INFERRED)

## What they're afraid of
(quote the fears I've named or described; one per line)

## The questions they ask me most
(quote as many real questions as you have, in their words or mine)

## What they get wrong before we talk
(quote my corrections or explanations)

## Neighborhoods, price ranges, and property types I talk about most
(a list with counts if you can)

## The client stories I've told you
(one paragraph each: what happened, what I did, what I said about it; quote my own line from the story)
```
Save as: `03-people.md`

---

## Prompt 4 · my stories and my life, the parts I've shared

```
[preamble]

List the stories and personal details I've shared with you that are not about a specific client: my family, my background, how I got into real estate, festivals and music, food, travel, what I'm proud of, what I'm tired of. Use these headings:

## Stories I've told you
(one paragraph each, with the line I used, quoted; mark HERS/INFERRED per paragraph)

## Things I've said I love
## Things I've said I'm over or won't do
## How I talk about my husband, my kid, and my team, in my words
## Anything I've asked you to keep private or leave out of posts
```
Save as: `04-stories.md`

---

## Prompt 5 · taste, cringe, and the rules I've given you

```
[preamble]

Everything I've ever told you about how my content should look, sound, or feel, and everything I've rejected. Headings:

## Rules I've given you for my posts, captions, or bio
(quote each)

## Things I've called cringe, cheesy, salesy, fake, or "not me"
(quote each, with what it was)

## Visual taste I've mentioned (colors, fonts, photo style, what I like on other agents' pages)
## Formats I've said I like or won't do (talking to camera, carousels, stories, reels)
## Posts or drafts I told you I loved, and why
## The words I use when I like something vs when I don't
```
Save as: `05-taste-and-rules.md`

---

## Prompt 6 · the facts I repeat (so we never invent them)

```
[preamble]

List the factual things I state as my own knowledge, so nobody has to guess them: neighborhoods and streets I name, price bands, programs, lender terms and how I define them, my brokerage and team, my listings, my markets. Headings:

## My markets and neighborhoods (with anything I've said about each)
## Price ranges I talk about
## Programs, loan types, and lender terms I've explained, in my definition
## My team, brokerage, and role, as I've described them
## Listings and deals I've mentioned (address or description, date if you have it, what I said)
## Facts you are not sure I stated (INFERRED only)
```
Save as: `06-facts-hers.md`

---

## After the six outputs land

One merge pass, by us, no ask on Jen:

1. New section in `jen-real-voice-profile.md`: "From her ChatGPT (date)". Additive. The voice memo lines and the July scrape stay above it and win on conflict.
2. HERS quotes only go into the voice bank and the line bank. INFERRED lines are notes, never copy.
3. Every "NOT IN HISTORY" becomes one calibration-log row, so the gap is named, not filled.
4. Prompt 6 facts get a HERS label in `FACTS.md` and still get re-checked before a post.
5. She reads the merged profile once: "that's me" or "not me," line by line if she wants. That is the only ask.

Uniformity rule: if a seventh prompt is ever added, it carries the same preamble, fixed headings, HERS/INFERRED marks, and a filename. No free-form prompts.
