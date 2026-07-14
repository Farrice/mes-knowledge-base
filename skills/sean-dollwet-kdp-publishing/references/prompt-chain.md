# The Production Prompt Chain — Verbatim

Source: "Try This Digital Product Strategy for 30 days" (youtube.com/watch?v=vhuo0A7Oy74, 25:14), a live screen-recorded build, plus the outline-from-competitors method from the "COMPLETE Amazon KDP Tutorial" (youtube.com/watch?v=qn6VasGSexI). Dollwet ran it in Claude (Opus 4.7, Pro plan ~$20/mo) in one continuous thread titled "Profitable book topics to write." **Tool-agnostic: any strong model works — Claude, ChatGPT, Gemini.** A free model works too (slower, credit-limited). AI is the assistant; the human is editor-in-chief at every step.

> "AI is just an assistant. It's not a replacement. So you want to work with AI and go back and forth until you're happy."

---

## Prompt 1 — Topic brainstorm

```
Give me 50 profitable book topics I can write about.
```
(Tutorial variant: "Give me 50 profitable book topics I can write about for my Amazon KDP business.")

**What came back:** intermittent fasting for women over 40, air fryer, sourdough baking, anxiety workbook, ADHD productivity, Mediterranean diet meal prep, self-discipline, stoicism, decluttering for overwhelmed adults… and "how to stop overthinking," which he picked.

**Human-judgment step → validate on Amazon, not in the model.** Take the candidate to Amazon, set category to Books, and confirm **3+ competitors below 80,000 BSR** in the **Paperback** format (DS Amazon Quick View shows BSR + ASIN inline). Live examples he confirmed: BSR 189, 312, #1,013 — "way below 80,000… selling extremely well." No cluster of sub-80k books = kill the topic, pick another candidate. Also narrow to one problem, one audience before proceeding (e.g., not "weight loss" but "intermittent fasting for women over 50").

---

## Prompt 2 — Pain points

```
Let's go with the topic of how to stop overthinking. Please list out the biggest
pain points of this target audience.
```

**What came back (verbatim on screen):** "Lying awake at night replaying conversations… / Mentally rehearsing worst-case scenarios that almost never happen / Reading way too much into texts, emails, and tone of voice / Feeling exhausted before the day even starts / Making simple decisions feel impossible / Drafting and redrafting a message ten times before sending / Constantly second-guessing decisions they already made / Feeling stuck in 'analysis paralysis' / Beating themselves up over small mistakes for days / … Physical symptoms like tight chest, headaches, jaw clenching / Procrastinating because the thinking feels safer than doing / Ruminating on past failures, embarrassments, or regrets."

**Human-judgment step → select the pain points to solve.** You choose which subset the book will actually address; this becomes the spine of the outline and the source of subtitle benefits. Don't let the model pick for you.

---

## Prompt 3 — Outline

```
Here are pain points that I think we should focus on solving. Based on this,
please create a detailed book outline for this book.
```

**What came back:** a full title + structure — Introduction: "The Exhausting Loop You Can't Seem to Escape" (opening hook / what overthinking actually is / the hidden cost / why "just stop thinking about it" has never worked); Part One — Ch.1 "Why Your Brain Won't Shut Off," Ch.2 "The Six Faces of Overthinking," Ch.3 "When Thinking Feels Safer Than Doing," Ch.4 "Stop Second-Guessing Every Decision You Make."

**Stronger method — outline FROM competitors (from the tutorial).** The market has already A/B-tested chapter structures for you. Before or instead of a blank-slate outline:
1. **TOC stalking:** open the top competitors' "Read sample," scroll to their table of contents, copy the standout chapters into your outline, skip the fluff. Combine the best chapters from multiple bestsellers.
2. **Review mining:** read positive and negative reviews for repeated patterns — what buyers loved, and "I wish the author covered this." Build your book to *do the liked things and fix the complaints*.
3. **The paste-reviews hack:** highlight the entire competitor review block → paste into the model → `summarize what people liked and what people didn't like` → feed that summary into the outline. Compresses hours of reading into seconds.

> "Learning from the best-selling competitors, taking the best parts of their book and put it into ours… people are saying 'I wish the author covered this'… you make sure that your book covers that exact thing."

---

## Prompt 4 — Titles

```
Give me 10 title ideas for this book. Give me versions of titles that are clear,
but also catchy.
```

**What came back + his verbatim taste verdicts (the taste-test rubric in action):**

| Title | Verdict | Why |
|---|---|---|
| Unstuck | ❌ reject | "Catchy, but you have no idea what your book is about" — the anti-example |
| Quiet the Noise | ➖ ding | Too vague |
| The 2:00 a.m. Mind | ➖ ding | Too catchy |
| Out of Your Head | okay | Passable |
| Stop Overthinking Everything | ✅ | Catchier than plain, still clear |
| The Overthinker's Escape Plan | ✅ | Clear + catchy |
| The End of Overthinking | ✅ | Clear + catchy |
| Stop Living in Your Head | ✅ | Clear + catchy |

**The rule:** reject anything you can't decode from the title alone; ding anything *too* catchy at the expense of clarity; **clarity breaks ties.** Then add a benefit-stacked subtitle (the keyword-plus-flair formula: main keyword + spice, e.g. "10-Minute Decluttering Cheat Sheet").

**Chosen:** "Stop Overthinking Everything: A Practical Guide to Quieting Your Mind and Trusting Yourself Again."

> "It's catchy, but you have no idea what your book is about, and that is a huge mistake people make when it comes to creating book titles."

---

## Prompt 5 — Draft (the generate → humanize loop)

```
Let's go with this. Please write the introduction chapter.
```

**What came back (verbatim):** "It's 2:14 a.m. You've been lying in bed for hours. Your body's heavy, your eyes burn from being open too long, and yet your mind is sprinting…" → "Your Brain Is Doing Its Job a Little Too Well — Your brain has one main job: keep you alive. Not happy. Not peaceful. Not even particularly content. Alive."

**Human-judgment step → humanize every chapter (the copyright unlock).** Generate ONE chapter → paste into a Google Doc → edit: add personal stories, insert your own speech patterns, break the repetition that starts around chapter 3–4 (the model forgets what it wrote), cut fluff, **fact-check every claim** (the model is confidently wrong). Then generate the next. Repeat to **10,000–15,000 words** for a first book. Raw paste is legally uncopyrightable and degrades — humanizing fixes both.

> "You can copyright your book if you actually humanize AI content. But if you're just copy-pasting from AI, you cannot copyright that."

Instruction seasoning for the draft prompt: "don't write in list style, focus on practical advice, use stories."

---

## Prompt 6 — Cover (two prompts, realistic → text-based)

Covers go through an image model (ChatGPT/GPT-Image or Gemini — "Claude is not the best with images"; free ChatGPT ≈ 3 image generations).

**6a — realistic first pass:**
```
Please create a book cover for the book titled [Stop Overthinking Everything:
A Practical Guide to Quieting Your Mind and Trusting Yourself Again].
```
→ a realistic meditation-by-a-lake cover.

**6b — re-prompt to text-forward (the on-trend style):**
```
make it a text based cover, make the text the main focus, images or vectors
surround it just as a complimentary element.
```
→ a typographic cover (stacked "STOP / OVERTHINKING / EVERYTHING" + botanical vectors).

**Human-judgment step → pick by current trend.** In self-help, text-forward covers currently convert better; realistic-image covers are "old-school." Choose the text-based version.

> "These text-based covers are doing really well nowadays. So these realistic images type book cover designs is kind of old-school."

---

## The chain as a pipeline

50 topics → **validate on Amazon (3+ sub-80k)** → narrow to one problem/one audience → pain points → **you select** → outline (blank-slate OR competitor-TOC + review-mining) → 10 clear-but-catchy titles → **taste-test (clarity breaks ties)** → chapter-by-chapter generate + **humanize** → two-style cover → pick text-based. Each prompt consumes the prior output so context compounds; the human is the gate between every step.
