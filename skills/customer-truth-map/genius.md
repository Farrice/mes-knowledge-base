# Customer Truth Map — Genius Context

> **Load this file before executing any workflow.** It is the IP anchor: the thesis, the
> method, the patterns, the hidden knowledge, the signature moves, the decision framework, and
> the quality rubric. The canonical source is [references/customer-truth-map-guide.md](references/customer-truth-map-guide.md)
> — where this file ever diverges from it, the guide wins.

## The One Sentence
**Stop guessing what your customer thinks; gather the exact words they already use, organize
those real words into one living map of what they say / think / feel / do and their pains /
gains, then run every piece of copy, content, positioning, and offer through that map — so your
output sounds like the reader's own head instead of yours.**

## The Honesty Spine (the one unbreakable rule)
The customer's words are the **gold**; AI is the tool that **sorts the gold from the pebbles** —
*organizing, never inventing.* The moment AI is allowed to make up a quote, paraphrase a pain,
or smooth a customer's grammar, the entire advantage is gone and you are "back to guessing, just
with a faster guessing machine." Every workflow here treats fabricated or paraphrased customer
language as an **automatic fail**. Real language in, organized language out. Nothing manufactured.

## Source & Provenance
- **Expert:** the creator behind the **Blazing Zebra** YouTube channel — a former marketing-agency
  owner who ran enterprise voice-of-customer survey programs for "some of the largest software
  companies in the world," then replaced them with this listening-first method.
- **Sources:** the 13-page guide *"The Customer Truth Map"* (verbatim-condensed in
  [references/customer-truth-map-guide.md](references/customer-truth-map-guide.md)) + the video
  *"Master TARGETED Market Research… with NotebookLM"* (`youtube.com/watch?v=GAVILEkfsvE`, full
  transcript at `extractions/customer-truth-map/transcript.txt`).
- **Lineage credited by the expert:** the **Empathy Map** (Dave Gray + XPLANE, mid-2000s,
  *Gamestorming* 2010) for the Say/Think/Feel/Do structure; **Jobs-to-be-Done** (Clayton
  Christensen, *Competing Against Luck*) for the pains→jobs reframe; **The Mom Test** (Rob
  Fitzpatrick) for the listening discipline behind it all.
- **Claims ledger:** the method itself is the expert's; the frameworks it stands on are public and
  attributed above. Any market/tool fact (e.g., "GummySearch shut down") is labeled where used and
  must be re-verified at run time — tools in this category churn.

## Core Thesis (why this beats what came before)
1. **The canyon.** The hardest problem in business is the gap between the person *selling* and the
   person who *needs it* — "almost everything we call marketing is just an attempt to throw a rope
   across that canyon."
2. **The curse of expertise.** Once you've solved a problem, you lose the ability to see it with
   fresh eyes. You've answered the same objection a hundred times, so it stops sounding like a real
   fear and starts sounding like a checkbox. The more expert you get, the further you drift from the
   beginner who is still confused — using words you stopped using years ago.
3. **The guessing tax.** Sitting down to write, you *invent* what the customer thinks, in your
   language, then answer your version of the problem. The copy is grammatical, clear, and slides
   right past the reader because it doesn't sound like anything happening in their head.
4. **Why now / why it beats surveys.** The old gold standard (expensive, slow surveys) had a flaw
   baked in: **the moment you write a survey question, you've already decided what's worth asking —
   you hand people your categories and ask them to color inside your lines. You learn what you
   thought to ask and miss everything else.** Listening to *unprompted* talk (the midnight one-star
   review, the frustrated forum thread, the offhand comment when nobody felt under a microscope)
   produces sharper results, faster, for almost nothing — because AI is now genuinely good at the
   one job that matters here: taking large, messy piles of human language and organizing them.

## The Method (six phases — each solves the mess of the one before)
| # | Phase | Solves | Workflow |
|---|---|---|---|
| 1 | **Gather** raw customer language (unedited, typos and all) from where they already talk | the guessing tax | `/ctm-scope` → `/ctm-gather` |
| 2 | **Clean** noise into signal — verbatim, word-for-word, no paraphrase | drowning in chitchat | `/ctm-clean` |
| 3 | **Build the map** — sort into Say/Think/Feel/Do + Pains/Gains, name the patterns | a flat list isn't usable | `/ctm-map` |
| 4 | **Find the deeper job + the gaps** — pains→JTBD, then the gap table | a map of talk ≠ what to do | `/ctm-jobs` → `/ctm-gaps` |
| 5 | **Put the map to work** — copy, content, positioning/offers, all map-grounded | blank-page guessing returns | `/ctm-to-copy` · `/ctm-to-content` · `/ctm-to-offer` |
| 6 | **Triangulate + keep fresh** — merge sources, refresh, change-log | a single source misleads; words go stale | `/ctm-triangulate` · `/ctm-refresh` |

The orchestrator `/customer-truth-map` runs the whole arc; `/ctm-deepen` is the enrichment layer
that takes the surface map down to identity-level resistance via the belief/posture stack.

## The Map Structure (empathy map + 2)
Six categories, each filled **only with real, sourced quotes** (a quote may sit in more than one):
- **SAY** — what they state out loud / in writing (direct quotes).
- **THINK** — beliefs and assumptions *implied* but not said directly.
- **FEEL** — emotions: frustrations, hopes, fears.
- **DO** — actions and behaviors, **including the workarounds and DIY fixes they cobbled together.**
- **PAINS** — the specific problems, obstacles, risks they describe.
- **GAINS** — the outcomes, wins, and "if only" wishes they want.

After sorting, name the **2–3 strongest patterns per category** and flag any quote that is
unusually **vivid or repeated often** — those are the copy gold.

## Genius Patterns (executable)
1. **Words-as-gold / AI-as-sorter.** Treat collection and organization as two different jobs. AI
   *only* sorts. Deploy: every gather/clean/map step. Success metric: zero invented quotes; every
   line traceable to a source.
2. **Unprompted > prompted.** Mine where people talk when they *don't* feel observed. Beats surveys
   because no category was pre-imposed. Deploy: `/ctm-scope` source selection. Metric: ≥80% of
   captured lines are unsolicited (review/thread/DM), not interview answers.
3. **Keep the typos.** The raw, ungrammatical phrasing carries the selling power — it's what you'll
   hand back so people feel understood. Cleaning grammar destroys the asset. Deploy: `/ctm-clean`.
4. **The verbatim rule.** One instruction outranks all others when extracting: *"Return these
   sentences word for word. Do not paraphrase. Do not fix the grammar. Do not summarize."* If the AI
   starts summarizing, stop it and re-issue the rule. Deploy: `/ctm-clean`, `/ctm-gather`.
5. **The Do-category goldmine.** A described workaround (the manual spreadsheet, the duct-tape
   routine) is "a problem someone cared about enough to solve badly" — a flashing sign at exactly
   where existing solutions (maybe yours) fail. Circle every one. Deploy: `/ctm-map`, `/ctm-gaps`.
6. **Pain → Job reframe.** People don't want your product; they *hire* it to make progress. Rewrite
   every pain as `"When [situation], I want to [motivation], so I can [desired outcome]."` The job
   points at the outcome, and the outcome is where the bigger ideas live (a feature solves "I keep
   forgetting"; a *positioning angle* solves "stay on their radar without feeling pushy"). Deploy:
   `/ctm-jobs`.
7. **Widest-gap-first prioritization.** Line up Pain/Job → Current Fix (competitors + DIY) → The Gap.
   The rows with the widest gaps are the shortlist: what to lead with in copy, what to build content
   around, where a new/repositioned offer meets real demand. Deploy: `/ctm-gaps`.
8. **Quote-to-slot mapping.** Real lines are pre-proven copy. Pull the 10 strongest and assign each
   a slot — headline, subhead, objection-handler, or proof point — keeping the customer's voice.
   Deploy: `/ctm-to-copy`.
9. **Grounded-idea generation.** Every content idea ships with the **specific quote or pattern it's
   built on**, so you know it's grounded in real language and not invented on "a slow Tuesday." Deploy:
   `/ctm-to-content`.
10. **Triangulation.** A map from one community misleads (each forum has its own culture, loud voices,
    blind spots). Build from several sources, then split **Consistent Truths** (across most/all
    sources → high-confidence, build core messaging here) from **Source-Specific** (one source →
    lower-confidence, hold loosely, useful for a sub-group). Deploy: `/ctm-triangulate`.
11. **Freshness as the edge.** "A map you refresh is worth ten times a map you build once and forget."
    Quarterly light pass + 1–2× yearly deep rebuild + a dated change-log. **What changes is itself the
    signal** — a read-out of where the customer's world is moving that competitors aren't tracking.
    Deploy: `/ctm-refresh`.
12. **Honest about the tools.** Don't oversell AI: most chat tools can't reliably bulk-scrape Reddit;
    NotebookLM reaches forums better *but only from sources you hand it*; manual copy-paste always
    works. State the real limit instead of pretending. Deploy: `/ctm-gather` (and our `tool-wiring`).

## Hidden Knowledge (tacit; what others miss)
- **Your own past conversations are often the single best source** — sales-call transcripts, support
  emails, DMs, reviews of your product *and competitors'* — because the person was talking directly
  about your space. Most people skip them and go straight to Reddit.
- **The narrowest target makes the strongest map.** "Small business owners" is too wide; "solo
  bookkeepers who just lost a big client" produces a useful map. Serve several? Build a separate map
  per customer — they won't blur.
- **Stop when the map stops surprising you.** Depth on 2–3 problems beats a thin sweep across many.
- **Work in chunks.** Feed a few thousand words at a time to clean; smaller chunks give cleaner
  extractions than dumping everything at once.
- **Bracket for sense, never paraphrase.** If a gold quote needs a few words of context to parse,
  add them *in brackets* — the original wording stays untouched.
- **NotebookLM is the gather tool, a chat tool is the build tool.** NotebookLM cites the exact lines
  it pulled (won't invent a quote nobody wrote) — ideal for grounded gathering; but drafting and
  reorganizing happen better in a normal chat window. Move the work over once quotes are pulled.
- **What AI genuinely does reliably** (and what to leave out): pulling/sorting/reframing real language,
  yes. Redesigning your UX from quotes alone or predicting conversion rates — no; those need real
  testing and real eyes. Don't ship the impressive-sounding moves that don't hold up.
- **The change-log becomes its own asset.** Over time, the dated record of how the language shifted is
  a competitive intelligence artifact nobody else has.

## Signature Moves (behavioral)
1. **Name the problems in their voice first.** Before hunting, have AI list 15–20 problems/fears
   "phrased the way the customer would say it to a friend, not in marketing language," then pick 2–3
   to research deeply.
2. **The verbatim re-issue.** Mid-extraction, the instant AI paraphrases, halt and re-state the
   word-for-word rule. Treat drift as a defect to correct, not a style choice.
3. **Circle the workarounds.** On every `DO` entry that describes a DIY fix, mark it — that's an
   unmet-need flag headed straight for `/ctm-gaps`.
4. **Rank by gap width.** Refuse to treat all pains equally; force the gap table and lead with the
   widest rows only.
5. **One quote per idea.** Never let a content/copy idea exist without the real line it's grounded in
   attached.
6. **Confidence-label everything cross-source.** When merging maps, every pattern is tagged
   high-confidence (consistent) or lower-confidence (source-specific) — never flattened into one
   undifferentiated list.
7. **Date the top of the map.** Every refresh writes a dated note of what was added and what shifted.

## Hall of Fame Exemplars (calibration anchors)
- **Exemplar — the follow-up reframe (JTBD done right).** Pain: *"I keep forgetting to follow up with
  leads."* Job: *"When a promising lead goes quiet, I want to stay on their radar without feeling
  pushy, so I can win the work without nagging."* Why it's gold: a reminder feature solves the pain;
  "stay on their radar without feeling pushy" is a whole positioning angle, maybe a whole offer. The
  reframe moved a feature request up to a market position.
- **Exemplar — the Do-category catch.** A customer writes: *"I just keep a messy spreadsheet and
  re-check it every Monday so nothing slips."* Surface read: minor habit. Truth-map read: a
  cared-about problem solved badly → the widest-gap candidate and the seed of both the lead content
  ("the Monday spreadsheet trap") and the offer.
- **Exemplar — quote-to-slot.** Raw line: *"honestly I'm not even sure what I'm paying for half the
  time."* → headline ("Know exactly what you're paying for") + objection-handler in the pricing
  section. The customer pre-wrote the headline; the map just found it.
- **Anti-exemplar (what NOT to do).** "Summarize the top pain points of first-time homebuyers" → a
  tidy paraphrase in *your* voice, no source lines, no vivid phrasing. It reads like marketing,
  converts like marketing, and is indistinguishable from the guessing it was meant to replace.

## Decision Framework (Pre-Flight — reused by every workflow)
Answer on paper before producing anything:
1. **One customer, one problem cluster?** Is the target narrow enough (the "solo bookkeeper who just
   lost a big client" test)? If broad, narrow it or split into separate maps.
2. **Do we already know this audience?** Front-load Recall + `memory_facade.py` before scraping — we
   may already hold real language or a prior map. Don't re-gather what we have.
3. **Real sources named?** Specific communities/threads/own-data, not "the internet." Unprompted talk
   prioritized over interview answers.
4. **Verbatim discipline armed?** The word-for-word rule is stated and will be re-issued on drift.
5. **Which output is this feeding?** Copy / content / positioning / offer — so the map is put to work,
   not admired.
6. **Fresh or stale?** Is there an existing map to refresh/compare, or is this a cold build?

## Quality Rubric (full instrument in [references/quality-rubric.md](references/quality-rubric.md))
Score 1–10; name the matching anchor for any score ≥8 (can't name it → lower it).
1. **Verbatim Integrity** — every quote is real, word-for-word, source-traceable; zero paraphrase or
   invention. *Fabrication or paraphrase = automatic fail, regardless of other scores.*
2. **Unprompted Sourcing** — language is mostly unsolicited (reviews/threads/DMs/own-data), not survey-
   shaped answers.
3. **Narrowness** — target is specific enough to produce non-blurry patterns.
4. **Map Completeness** — all six categories populated; 2–3 named patterns each; vivid/repeated quotes
   flagged.
5. **Do-Category Mining** — workarounds explicitly surfaced and circled as unmet-need signals.
6. **Job Depth** — pains reframed to outcome-level jobs that open positioning, not just features.
7. **Gap Ranking** — gap table built; widest rows identified as the shortlist with a reason.
8. **Put-to-Work Fidelity** — outputs carry the customer's voice and each is grounded in a named quote/
   pattern; nothing generic.
9. **Freshness Discipline** — dated change-log present (or scheduled); cross-source confidence labels
   applied where multiple sources exist.

## Stacking Guide (compose, don't reimplement)
This skill **owns** the language-mining → empathy-map → JTBD → gap → apply → refresh loop. It
**calls** the heavy research and feeds the production engines:

| Stack with | When | Chain |
|---|---|---|
| `/buyer-sourcer` (luke-iha-avatar-machine) | heavy, source-traced VoC mining at scale | `/ctm-gather` can delegate the mine, then `/ctm-clean` |
| `/mcraney-deep-canvass` | go from surface map to belief/resistance excavation | `/ctm-deepen` hands the map over |
| `/consumer-posture-profile` (consumer-posture-research skill) / dai-media consumer posture | add the identity / occupation / activity layer | `/ctm-deepen` enriches the map with posture |
| Verification protocol (Step 5.5) | confirm any real-world claim that rides along with the language | gate before any output that asserts facts |
| `/copy-engine`, `/ghostwrite`, `master-copywriter` | turn map → finished copy | `/ctm-to-copy` hands off |
| `/novelty-forge`, `/parallax`, `/diandra-*` | turn map → finished content | `/ctm-to-content` hands off (the map supplies the held belief + real language) |
| `/build-bos`, positioning skills | turn gaps → positioning/offer | `/ctm-to-offer` hands off |
| `/schedule` | make the quarterly refresh an actual recurring job | `/ctm-refresh` registers it |

**Common sequences:**
- `/customer-truth-map` (full arc, cold start → finished map → first outputs)
- `/ctm-scope → /ctm-gather → /ctm-clean → /ctm-map → /ctm-jobs → /ctm-gaps` (build the map)
- `/ctm-map → /ctm-deepen` (surface → identity-level depth)
- `/ctm-gaps → /ctm-to-offer` (widest gap → positioning/offer)
- `/ctm-triangulate` after running the build across 2+ communities, then `/ctm-refresh` quarterly.
