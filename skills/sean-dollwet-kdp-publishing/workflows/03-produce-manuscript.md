---
name: produce-manuscript
description: Sean Dollwet's manuscript build. Runs the 5-prompt chain at full depth through a chapter-by-chapter generate→humanize loop (~1,250 words at a time, never raw paste), enforces the copyright-humanize rule and the one-day/one-week timebox, then proofreads, formats, and assigns the pen name — a publishable manuscript ready for upload.
produces: A publishable, copyright-eligible manuscript — humanized draft, proofread, formatted, pen-named
expert: Sean Dollwet
load_context: genius.md
---

# Produce Manuscript — the Publishable Draft

## Pre-Flight Gate

Run this ONLY after workflow 02 has locked the outline, spec, and irreversible title. You are turning the blueprint into copyrightable pages. The governing law: **AI drafts, human elevates** (Pattern 6). Raw AI paste is legally uncopyrightable AND degrades — "around chapter two or three it becomes extremely repetitive… surface level" because the model forgets what it wrote and hallucinates confidently. Publishing raw output joins the "AI garbage" flood.

Run this when: title + outline are signed off and you need the actual manuscript.

Do NOT: copy-paste any section as-generated, chase a masterpiece, or blow the timebox. Anti-patterns killed (genius.md): **raw AI paste**, **perfectionism** ("anything past 1 week on a first book = self-sabotage"), **padding page count with fluff**, **volume over quality** (bad reviews from AI slop suppress *every* book in the catalog — Exemplar B, the 141-book $0 pen name). Tedium is the moat (Pattern 16): the edit-improve cycle is exactly where competitors quit.

## Skill Acquisition

Load before executing:
- `genius.md` — Patterns 6 (AI drafts / human elevates / copyright unlock), 7 (value = organization + time-saved, not page count), 16 (tedium is the moat), 17 (time-or-money trade), 18 (one-day timebox / perfectionism ceiling); Hidden Knowledge 4 (pen names are standard infrastructure), 5 (catalog is the real product); Exemplar B (quality over volume); Rubric items 2, 5, 6, 8.
- `references/prompt-chain.md` — the full 5-prompt chain, especially Prompt 5 (draft → humanize loop) and the instruction seasoning.
- `references/price-sheet.md` — formatting lanes ($50–100 freelancer vs. Reedsy free), ghostwriter lane ($1–2k), word/trim/page targets.

## Execution

### Step 1 — Confirm the chain state
The manuscript is Prompt 5 of the chain, run in one continuous thread so context compounds (Prompts 1–4 already produced topic → pain points → outline → title in workflows 01–02). Tool-agnostic: any strong model works — Claude, ChatGPT, Gemini; a free model works too (slower, credit-limited). AI is the assistant, human is editor-in-chief at every step: "work with AI and go back and forth until you're happy."

### Step 2 — Run the generate→humanize loop (one subchapter at a time)
Generate exactly **one subchapter (~1,250 words) at a time**, never the whole book at once. Draft prompt with instruction seasoning: `Please write the [chapter/subchapter]` + `don't write in list style, focus on practical advice, use stories.`

Then, for EACH subchapter, run the human-elevation pass before generating the next:
1. Paste into a Google Doc.
2. **Add stories** — insert the author's real stories, examples, and own speech patterns. Every section must contain at least one story or concrete example the AI didn't produce (Rubric 5). Mark `[AUTHOR STORY]` slots where the author must supply lived material.
3. **Break the repetition.** Generic tools degrade around chapter 3–4 (the model forgets what it wrote) — so **later chapters need heavier edits** than the intro and chapter 1. Actively break repeated phrasing and surface-level filler.
4. **Cut fluff.** Delete anything that circles the topic without advancing the solution — value is per-page, not page count (Pattern 7).
5. **Fact-check every claim.** The model is confidently wrong; verify each factual assertion.
6. Generate the next subchapter.

**Never raw paste.** For simple list-books (e.g., dad jokes) plain output can be enough, but for high-content nonfiction every section is elevated. (Ghostwriter lane, Pattern 17 / price-sheet: instead of drafting, brief a $1,000–2,000 ghostwriter — accept only work you're happy with.)

### Step 3 — Enforce the copyright-humanize rule
This is the legal unlock, not a style note: "You can copyright your book if you actually humanize AI content. But if you're just copy-pasting from AI, you cannot copyright that." No section ships as-generated. The humanization pass is what makes the manuscript copyright-eligible AND lifts it out of the AI-slop flood.

### Step 4 — Hold the value-density line
Size by problem-solved, not length. Standard high-content = 30,000 words (~1,250/subchapter × 8 chapters × 3); a 10,000–15,000-word first book is legitimate. A tight 100-page book that solves the problem beats a 500-page fluff book. You don't need original insight — organize and clearly teach known information; "the value doesn't have to be new information. It can be just saving time." You become the expert as you publish.

### Step 5 — Honor the timebox
Write the first book in **one day**; a couple days is fine; **absolute max 1 week "if you're a perfectionist."** Anything longer is self-sabotage — "you're not writing a masterpiece." Ship a good-enough asset fast into a marketplace with pre-existing demand.

### Step 6 — Proofread pass
Run a final quality sweep: catch typos and grammar (Grammarly), and run a **plagiarism check** to confirm originality. This is a tedious step most skip (Pattern 16) — do it every time.

### Step 7 — Format (time-or-money lane, Pattern 17)
- **Free / DIY:** Reedsy-style free formatting tool — costs time, saves money.
- **Paid:** hire a freelancer for **$50–$100** (ebook + paperback) — costs money, saves time.
State the trade explicitly and pick by budget/speed. Format order: introduction → main chapters → conclusion.

### Step 8 — Assign the pen name
Pen names are standard infrastructure (Hidden Knowledge 4) and **sales-neutral** — they don't affect sales. Default to a **pen name per niche** so the catalog stays cleanly packaged and decoupled from personal identity (most celebrity books are ghostwritten under pen names; "J.K. Rowling" is one). This keeps the catalog sale-ready — the catalog is the real product (Hidden Knowledge 5). Don't overthink pen-name vs. real-name — pick and go (Pattern 18).

## Content Type Adaptations

| Content type | Loop depth | Timebox | Formatting |
|---|---|---|---|
| **High-content nonfiction** | Full generate→humanize per subchapter; heavier edits ch.3+ | 1 day → max 1 week | Reedsy free OR $50–100 freelancer |
| **Low-content journals** | Minimal prose; build page templates, not chapters | Fastest — often single session | DIY interior; outsource full book ~$75 (price-sheet) |
| **Medium-content coloring/activity** | Interior art, not text; per-page ~$10 if outsourced | Fast to spec | Model competitor trim; DIY or freelancer |
| **Sprint book (10–15k)** | Fewer subchapters, same humanize rule — no shortcuts | 1 day | Same lanes |
| **List-book (jokes/prompts)** | Plainer AI output acceptable; still proofread + fact-check | Same day | DIY |

## Output Requirements

Deliver a **publishable manuscript** containing:
- The full humanized draft — every subchapter showing its elevation edits (stories added, fluff cut, facts checked) with any remaining `[AUTHOR STORY]` slots flagged — OR the complete ghostwriter brief if that lane was chosen.
- Confirmation the **copyright-humanize rule** is satisfied (no raw-paste sections).
- Proofread + plagiarism-check confirmation.
- Formatting lane chosen (Reedsy free vs. $50–100 freelancer) with the time-or-money trade named.
- Pen name assigned (per-niche default) with a one-line catalog-packaging rationale.

`Execution prompt: references/prompts-v2/book-production-package.md`

## Quality Gate (pass/fail — references genius.md Rubric + anti-patterns)

- [ ] **No section ships as raw AI output** — each shows an elevation pass with ≥1 story/example the AI didn't produce; manuscript is copyright-eligible (Rubric 5, Pattern 6).
- [ ] Later chapters (3+) carry heavier edits than the intro — the ch.3 repetition was actively broken.
- [ ] Every factual claim fact-checked; plagiarism + grammar pass complete (Rubric 5, 8).
- [ ] Sized by problem-solved, not page count — no fluff padding (Rubric 2, Pattern 7).
- [ ] Time-to-ship inside the one-week ceiling; no stall in polishing (Pattern 18).
- [ ] Formatting lane is a stated time-or-money decision naming the other lane's cost (Rubric 3).
- [ ] Pen name assigned per-niche for clean catalog packaging (Hidden Knowledge 4–5).
- [ ] No volume-over-quality slop — this is one strong book, not filler that would drag the catalog's reviews down (anti-pattern; Exemplar B).
