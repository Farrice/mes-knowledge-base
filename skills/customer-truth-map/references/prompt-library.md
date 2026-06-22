# Prompt Library — Customer Truth Map

Two columns of truth: the **expert's original prompts** (verbatim from the guide — use these to
replicate the method exactly) and our **enhanced / wired versions** (use these to surpass it —
tighter constraints, grounding hooks, no-fabrication gates, tool wiring). Workflows reference these
by name.

---

## P1 — Name the problems (Phase 1, Step 1)
**Expert (verbatim):**
```
I sell [your product or service] to [your specific customer].
List 15 to 20 distinct problems, frustrations, or fears this customer
is likely dealing with that relate to what I offer. Phrase each one
the way the customer might actually say it to a friend, not in
marketing language.

Then ask me which 2 or 3 of these are most worth researching deeply.
```
**Enhanced:** prepend a grounding line — *"Before listing, here is what we already know about this
customer (from prior maps / memory): [paste `memory_facade.py` + Recall results]. Build on it, don't
repeat it."* Require each item tagged `[assumed]` vs `[evidenced: source]`, so Phase 1 surfaces what
we're guessing vs. what we've already heard.

---

## P2 — Find where they talk (Phase 1, Step 2)
**Expert (verbatim):**
```
My customer is [describe them] and the problems I want to research are
[paste the 2 to 3 problems].

List the specific places online where this customer openly discusses
these problems in their own words: subreddits, forums, Facebook groups,
review sites, YouTube comment sections, and any niche communities.
For each, tell me what kind of language or content I am likely to find
there and how candid people tend to be.
```
**Enhanced:** ask for, per source: an exact URL/handle, an estimated *candor* score (1–5), whether it's
*unprompted* (review/thread) vs *prompted* (Q&A), and the recommended capture tool from
[tool-wiring.md](tool-wiring.md) (Apify reddit actor / NotebookLM / Playwright / manual). Also list our
**own-data** sources (sales calls, support, DMs, reviews) — "your past conversations are often the
single best source."

---

## P3 — Clean noise into signal (Phase 2) — **the verbatim rule lives here**
**Expert (verbatim):**
```
Below is a block of real conversation from a community where my
customers talk. Read it and extract only the sentences that reveal
their thoughts, feelings, actions, and experiences. Focus on pain
points, desired outcomes, and emotional reactions.

Rules:
- Return the original sentences word for word. Do not paraphrase,
  summarize, or clean up the grammar.
- Drop anything that is just chitchat, jokes, or off-topic.
- If a quote is gold but needs a few surrounding words to make sense,
  include them in brackets.

Conversation:
[paste your chunk here]
```
**Enhanced:** append a source tag to every extracted line — `> "quote" — [source, date/permalink]` —
so the running list is traceable. **Drift guard:** run the deterministic backstop
`python3 execution/ctm_verbatim_check.py --source <raw_chunk> --quotes <extracted>` — it exits 1 and
lists every line that is not a substring of the source chunk (bracketed insertions + source tags are
allowed). Discard each offender and re-issue: *"Return these sentences word for word. Do not
paraphrase. Do not fix the grammar. Do not summarize."* (This is the verbatim-integrity gate, checkable
in code — not a vibe.)

---

## P4 — Build the map (Phase 3)
**Expert (verbatim):**
```
Below is a list of real, unedited quotes from my customers, pulled from
where they actually talk.

Sort every quote into the categories below. Keep the original wording.
A quote can appear in more than one category if it genuinely fits.

- SAY: things they state out loud or in writing, direct quotes
- THINK: beliefs and assumptions implied but not said directly
- FEEL: emotions, frustrations, hopes, fears
- DO: actions and behaviors they describe, including workarounds and
  DIY fixes they have cobbled together
- PAINS: the specific problems, obstacles, and risks they describe
- GAINS: the outcomes, wins, and "if only" wishes they want

After sorting, write a short summary under each category naming the
2 to 3 strongest patterns you see, and flag any quote that is unusually
vivid or repeated often, since those are likely to be the most useful
in copy later.

Quotes:
[paste your cleaned quote list here]
```
**Enhanced:** add a final instruction — *"In DO, explicitly tag every described workaround/DIY fix as
`⚠ WORKAROUND` (a problem someone cared about enough to solve badly) — these feed the gap analysis."*
Keep source tags on every quote through the sort.

---

## P5 — Reframe pains into jobs (Phase 4, Step 1)
**Expert (verbatim):**
```
Below are the pain points from my Customer Truth Map.

For each one, dig past the surface complaint to the deeper progress the
customer is trying to make. Rewrite each as a job in this format:

"When [situation], I want to [motivation], so I can [desired outcome]."

Example: the pain "I keep forgetting to follow up with leads" becomes
the job "When a promising lead goes quiet, I want to stay on their radar
without feeling pushy, so I can win the work without nagging."

Then, for each job, suggest one or two angles I might not have considered
that would help the customer make that progress.

Pain points:
[paste the PAINS section of your map]
```

---

## P6 — Map the gaps (Phase 4, Step 2)
**Expert (verbatim):**
```
Using my Customer Truth Map and the jobs we just defined, build a table
with three columns:

1. Pain Point or Job: what the customer is struggling with
2. Current Fix: how they handle it today, including competitor products
   and the DIY workarounds from the map
3. The Gap: where the current fix falls short, frustrates them, or leaves
   them wanting

Focus the table on the rows where the gap is widest, because those are
the places where a better message or a better offer will land hardest.
```
**Enhanced:** add a 4th column **Gap Width (1–5)** and sort descending; the top rows are the
explicit shortlist passed to `/ctm-to-copy`, `/ctm-to-content`, `/ctm-to-offer`.

---

## P7 — For copy (Phase 5)
**Expert (verbatim):**
```
Here is my Customer Truth Map. Pull the 10 quotes that would be most
powerful to use, lightly edited, in marketing copy. For each, tell me
where it would work best: a headline, a subhead, an objection-handling
line, or a testimonial-style proof point. Keep the customer's voice.

Using the FEEL and PAINS sections of my map, write 8 headline options
for [the page or campaign you are working on]. Use the customer's own
words and emotional register wherever you can. Avoid jargon and hype.
```

---

## P8 — For content (Phase 5)
**Expert (verbatim):**
```
Based on the pains, jobs, and gaps in my Customer Truth Map, give me 15
content ideas (posts, emails, or short videos) that speak directly to
problems my customer actually raised. For each idea, include the specific
quote or pattern from the map that it is built on, so I know it is
grounded in real language and not invented.

Take the single widest-gap row from my map and turn it into an outline
for one piece of long-form content that names the problem in the
customer's words, validates the frustration with their current fix, and
points toward a better way of thinking about it.
```

---

## P9 — For positioning and offers (Phase 5)
**Expert (verbatim):**
```
Using my Customer Truth Map, draft 3 to 5 sharp positioning angles for
my [product or service]. Each angle should target a specific gap from the
map where customers are underserved. For each, write one sentence I could
say to a prospect that would make them feel understood.

Based on the jobs and gaps in my map, suggest 3 ways I could adjust or
extend my offer to close a gap customers clearly care about. For each,
note the exact pain or wish from the map it responds to, and be honest
about which ones would be simple to add versus a major undertaking.
```

---

## P10 — Triangulate (Phase 6)
**Expert (verbatim):**
```
Below are several Customer Truth Maps I built from different sources
about the same customer and problem. Produce one consolidated map.

For each category, separate:
- CONSISTENT TRUTHS: patterns and language that appear across most or
  all sources. Treat these as high-confidence.
- SOURCE-SPECIFIC: insights that show up in only one source. Treat these
  as worth noting but lower-confidence, and tell me which source each
  came from.

Maps:
[paste each map under a clear header naming its source]
```

---

## P11 — Refresh (Phase 6, "keep it fresh") — *our addition, operationalizing the habit*
```
Here is my current Customer Truth Map (dated [last refresh]) and a new
batch of recent quotes from [source(s)], all word-for-word.

1. Add the new quotes to the right categories, keeping original wording + source tags.
2. Flag NEW phrasing, NEW worries, and NEW wishes that were not in the prior map.
3. Note anything in the prior map that now seems dated or has dropped out of the language.
4. Write a dated change-log entry at the top: what was added, what shifted, what it signals
   about where this customer's world is moving.

Prior map:
[paste]
New quotes:
[paste]
```
