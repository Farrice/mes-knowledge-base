---
name: book-blueprint
description: Sean Dollwet's full pre-production package. Stalks competitor TOCs, mines reviews for loves/complaints, builds the pain-point inventory and detailed outline, locks the spec, engineers the irreversible title, and sets cover direction — everything decided BEFORE a manuscript word is drafted.
produces: Pre-production package — pain-point inventory, competitor-informed outline, spec, engineered title+subtitle, cover direction
expert: Sean Dollwet
load_context: genius.md
---

# Book Blueprint — the Pre-Production Package

## Pre-Flight Gate

Run this ONLY after a topic has cleared workflow 01's BSR gate (3+ competitor books <80,000 BSR, paperback). You are converting a validated topic into a build spec. The title decided here is **irreversible post-publish** (Hidden Knowledge 1): Amazon doesn't allow title changes, and fixing one means unpublish/republish, which typically destroys accumulated reviews. So title work is done to full standard here, before anything ships.

Run this when: a topic is GO and you need the outline, title, spec, and cover brief locked before drafting.

Do NOT: invent a brand-new concept (Pattern 3 — model proven topics, differentiate at the margin), skip the subtitle (it's free selling space), or write an artsy title. Anti-patterns killed (genius.md): **artsy/curiosity/clever titles**, **writing without an outline** ("turning on the camera with no script and just yapping"), **padding page count with fluff**.

## Skill Acquisition

Load before executing:
- `genius.md` — Patterns 3 (one-problem-one-audience), 4 (keyword+flair titling), 5 (title taste-test), 7 (value = organization, not page count), 12 (review-moat door-close, for cover/title/content beats); Hidden Knowledge 1 (title irreversible), 3 (doubled price = conveyed value), 8 (Coco Wyo coloring benchmark); Exemplars A, C (Stop Overthinking anatomy), E; Rubric items 4, 9, 10.
- `references/prompt-chain.md` — Prompts 2 (pain points), 3 (outline, incl. TOC-stalking + review-mining), 4 (titles with the verbatim taste verdicts), 6 (cover, realistic → text-based).
- `references/price-sheet.md` — book spec targets (30k / 5x8–6x9 / 150–200pp; first book 10–15k; model-the-trim + offer-slightly-more).

## Execution

### Step 1 — Stalk competitor TOCs (the market already A/B-tested the structure)
Open the top page-one competitors' "Read sample" / Look Inside, scroll to each table of contents, and copy the standout chapters into a working outline; skip the fluff. Combine the best chapters from multiple bestsellers. This is modeling proven structure, not ripping off (genius.md anti-pattern: ripping off vs. modeling — extract and recombine working elements, never clone).

### Step 2 — Mine the reviews (cover the loves, fix the complaints)
Read positive AND negative reviews for repeated patterns. The paste-hack: highlight the entire competitor review block → paste into the model → `summarize what people liked and what people didn't like` → feed that summary into the outline. Buyers literally tell you the gaps — "I wish the author covered this" — so your book *does* the liked things and *fixes* the complaints. "Taking the best parts of their book and put it into ours."

### Step 3 — Build the pain-point inventory
Run Prompt 2 verbatim: `Let's go with the topic of [X]. Please list out the biggest pain points of this target audience.` (Source return for "stop overthinking": "Lying awake at night replaying conversations… mentally rehearsing worst-case scenarios… analysis paralysis… tight chest, headaches, jaw clenching…") **You** select which subset the book solves — don't let the model pick. This inventory becomes the spine of the outline AND the source of subtitle benefits.

### Step 4 — Construct the detailed outline
Run Prompt 3: `Here are pain points that I think we should focus on solving. Based on this, please create a detailed book outline for this book.` Merge the model's blank-slate structure with the competitor-TOC chapters from Step 1 and the complaint-fixes from Step 2. Enforce **one problem, one audience** (Pattern 3): the outline names one method for one narrow audience, not "everything for everyone." Every chapter must advance the promised transformation from pain-points to subtitle-benefits — cut anything that circles the topic without advancing the solution. Value comes from organizing and clearly teaching known information (Pattern 7) — you don't need original insight; "people just want reminders."

### Step 5 — Lock the spec
Decide word count, trim, and page count against `references/price-sheet.md`:
- **Standard high-content:** 30,000 words · 5x8–6x9 trim · ~150–200 pages. Math: 30,000 ÷ 8 chapters = ~3,750/chapter ÷ 3 = ~1,250 words per subchapter.
- **Sprint / first book:** 10,000–15,000 words is a legitimate first book.
- **Low/medium content:** model competitors' trim + page count (e.g., coloring 8.5x8.5, ~80pp), then **offer slightly more** (40 pages → 45). Size by problem-solved, never page count — "highest value per page."

### Step 6 — Engineer the title (the irreversible decision)
Run Prompt 4 verbatim: `Give me 10 title ideas for this book. Give me versions of titles that are clear, but also catchy.` Then:
- **Main title** = the exact primary search phrase + optional flair ("decluttering" → "10-Minute Decluttering Cheat Sheet"). Amazon is a search engine — if the buyer's typed phrase isn't in your title, you don't surface.
- **Subtitle** = a stack of **3–4 concrete benefits** drawn from the pain-point inventory, with numbers and power words, plus secondary searchable keywords, long over short. Never skip it — it's free selling space. Canonical skeleton (Exemplar C): "Stop Overthinking: 23 Techniques to Relieve Stress, Stop Negative Spirals, Declutter Your Mind, and Focus on the Present."
- **Taste-test rubric (Pattern 5), clarity breaks ties.** Reject anything you can't decode from the title alone; ding anything *too* catchy. Cite the verbatim rejections from `references/prompt-chain.md`: **"Unstuck" ❌** ("catchy, but you have no idea what your book is about" — the anti-example); **"Quiet the Noise" ➖** (too vague); **"The 2:00 a.m. Mind" ➖** (too catchy); passes: "Stop Overthinking Everything," "The Overthinker's Escape Plan," "The End of Overthinking." Between two clear titles pick the catchier; between clear and catchy, clarity wins. Chosen exemplar: "Stop Overthinking Everything: A Practical Guide to Quieting Your Mind and Trusting Yourself Again."
- Confirm the target keyword appears **verbatim** and get explicit sign-off — the title is irreversible after publish.

### Step 7 — Set cover direction
Model the page-one *winners* (Pattern 12 — beat incumbents on the buyer's decision path: cover → title → Look Inside). For self-help, **text-forward covers convert better** now; realistic-image covers are "old-school" (Prompt 6b). Requirements: title text BIG and readable at thumbnail size, strong color contrast, imagery that matches topic/genre. For coloring, model the Coco Wyo kawaii "Bold-Easy" language (Hidden Knowledge 8). Never clone a competitor's cover — stand out. If pricing above category norm, the cover must *visibly* convey the extra value (Hidden Knowledge 3), or it won't sell.

## Content Type Adaptations

| Content type | Outline source | Spec | Title/cover flex |
|---|---|---|---|
| **High-content nonfiction** | TOC-stalk + review-mine + pain-points | 30k words / 5x8–6x9 / 150–200pp (sprint: 10–15k) | Text-forward self-help cover; benefit-stacked subtitle from pain inventory |
| **Low-content journals** | Model competitor interior structure | Model trim + offer slightly more | Keyword title still mandatory; design/trend carries the cover |
| **Medium-content coloring/activity** | Model page-one winners' page mix | Model trim (~8.5x8.5, ~80pp) + offer slightly more | Coco Wyo "Bold-Easy" language; big readable title, high contrast |
| **Sprint book** | Tighter outline, fewer chapters | 10–15k words | Same title standard — no shortcuts on the irreversible decision |

## Output Requirements

Deliver a **book-production package** containing:
- **Pain-point inventory** with the selected subset marked.
- **Competitor-informed outline:** chapters + subchapters, per-section word targets, the transformation arc named, and which chapters answer which review complaints.
- **Locked spec:** word count / trim / page count with the rationale.
- **Title package:** chosen main title + benefit-stacked subtitle with pain-point mapping and verbatim-keyword confirmation, plus 4 runner-ups and the taste-test verdicts; a note that sign-off is required because the title is irreversible.
- **Cover direction sheet:** modeled winners, text-vs-realistic call, the readability/contrast rules, and DIY-vs-outsource cost from the price sheet.

`Execution prompt: references/prompts-v2/book-production-package.md`

## Quality Gate (pass/fail — references genius.md Rubric + anti-patterns)

- [ ] Outline built FROM competitor TOCs + review-mining, not blank-slate invention; every chapter advances the transformation, no fluff padding (Rubric 7 order, anti-pattern: writing without an outline).
- [ ] Book names ONE problem for ONE audience (Rubric 10).
- [ ] Main title leads with the **verbatim searched keyword** and passes the taste-test — decode-in-one-read, clarity breaks ties; zero artsy/curiosity titles (Rubric 4).
- [ ] Subtitle stacks **3–4 concrete benefits** traceable to the pain inventory; subtitle is never skipped.
- [ ] Spec matches the price sheet (30k/5x8–6x9/150–200pp OR 10–15k sprint OR model-trim+slightly-more); sized by problem-solved not page count.
- [ ] Cover direction beats incumbents on cover/title/content (Pattern 12), text-forward for self-help, readable at thumbnail, never a clone.
- [ ] Title irreversibility acknowledged and sign-off captured before proceeding to draft.
