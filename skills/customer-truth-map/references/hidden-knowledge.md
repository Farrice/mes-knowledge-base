---
description: The 8 tacit insights of the Customer Truth Map — the things practitioners learn the hard way that aren't in the obvious method. Each expanded as the insight → why others miss it → how to deploy it. Same 8 as genius.md.
---

# Hidden Knowledge — Tacit Insights (the 8)

These are the eight tacit items from [`../genius.md`](../genius.md) (§ "Hidden Knowledge"), expanded.
They are what separates a usable map from an impressive-looking one — the moves an expert makes
without thinking that a first-timer skips. **Same 8, same order, no contradictions** with genius.md.

> Format per entry — **The tacit insight** · **Why others miss it** · **How to deploy it.**

---

### 1. Your own past conversations are often the single best source
- **The insight:** Sales-call transcripts, support emails, DMs, and reviews of your product *and your
  competitors'* are the customer talking directly about your exact space — richer than any cold forum.
- **Why others miss it:** It feels like "research" should mean going *outside*, so people jump
  straight to Reddit and skip the gold already sitting in their own inbox and CRM.
- **How to deploy it:** In `/ctm-scope`, list own-data sources *first* (and front-load Recall +
  `memory_facade.py` — we may already hold prior language). Ingest those before scraping anything new.

### 2. The narrowest target makes the strongest map
- **The insight:** "Small business owners" is too wide to produce signal; "solo bookkeepers who just
  lost a big client" produces a useful, non-blurry map. Serving several? Build a *separate* map per
  customer — they won't blur together.
- **Why others miss it:** A wider target *feels* like a bigger market and bigger upside, so people
  resist narrowing — and get patterns so generic they're indistinguishable from guessing.
- **How to deploy it:** Apply the "solo bookkeeper who just lost a big client" test in the Pre-Flight
  Decision Framework. If the target is broad, narrow it or split into multiple maps before gathering.

### 3. Stop when the map stops surprising you
- **The insight:** Depth on 2–3 problems beats a thin sweep across many. Diminishing returns arrive
  when new sources stop producing new patterns.
- **Why others miss it:** Completionism — the urge to "cover everything" feels rigorous, so people
  keep gathering long after the signal has saturated and dilute the strong findings.
- **How to deploy it:** During `/ctm-gather` / `/ctm-map`, watch for the surprise rate dropping. When
  the last batch added no new pattern, stop the sweep and go deep on the 2–3 strongest.

### 4. Work in chunks
- **The insight:** Feeding a few thousand words at a time yields cleaner extractions than dumping
  everything at once.
- **Why others miss it:** Bigger context windows tempt people to paste the whole pile, assuming "more
  context = better" — but large dumps push the model toward summarizing instead of quoting.
- **How to deploy it:** In `/ctm-clean`, batch the raw corpus into a few-thousand-word chunks and run
  the verbatim extraction per chunk; concatenate the verbatim outputs afterward.

### 5. Bracket for sense, never paraphrase
- **The insight:** If a gold quote needs a few words to parse, add them *in brackets* — the original
  wording stays untouched, so the line is still genuinely the customer's.
- **Why others miss it:** When a quote is confusing, the reflex is to rewrite it for clarity — which
  silently converts the customer's words into yours and breaks the honesty spine.
- **How to deploy it:** In `/ctm-clean`/`/ctm-to-copy`, supply context only inside `[brackets]`:
  e.g., *"and then it [the dashboard] just froze on me again."* Original untouched, sense restored.

### 6. NotebookLM is the gather tool, a chat tool is the build tool
- **The insight:** NotebookLM cites the exact lines it pulled (it won't invent a quote nobody wrote),
  which makes it ideal for grounded *gathering*; but drafting and reorganizing happen better in a
  normal chat window. Move the work over once the quotes are pulled.
- **Why others miss it:** People pick one tool and try to do everything in it, then either fight
  NotebookLM's drafting limits or lose citation-grounding when they gather in a plain chat.
- **How to deploy it:** Per `tool-wiring.md`: pull and cite in NotebookLM (`/ctm-gather`), then carry
  the verbatim quotes into a chat window for sorting, mapping, and drafting (`/ctm-map` onward).

### 7. What AI genuinely does reliably (and what to leave out)
- **The insight:** Pulling, sorting, and reframing real language — yes. Redesigning your UX from
  quotes alone or predicting conversion rates — no; those need real testing and real eyes.
- **Why others miss it:** The impressive-sounding moves (predict my conversion!, redesign my product!)
  are the ones people most want to demo — and the ones that don't hold up, eroding trust in the whole
  method.
- **How to deploy it:** Keep the method inside AI's reliable lane (organize real language); route
  anything requiring prediction or design judgment to real testing. State the limit out loud
  (Pattern 12). Don't ship the moves that don't hold.

### 8. The change-log becomes its own asset
- **The insight:** Over time, the dated record of how the language shifted is a competitive-
  intelligence artifact nobody else has — a read-out of where the customer's world is moving.
- **Why others miss it:** People treat the change-log as version-control housekeeping, not as the
  product, so they overwrite the old map instead of dating and keeping the deltas.
- **How to deploy it:** In `/ctm-refresh`, never overwrite — append a dated entry of what was added and
  what shifted. Periodically read the log *as analysis*: the shifts are the insight competitors aren't
  tracking.

---

**Cross-reference:** these eight sit *under* the 12 patterns in [`genius-patterns.md`] — #1–#2 inform
`/ctm-scope`, #3–#5 inform the gather/clean discipline (Patterns 3, 4), #6–#7 inform the
honest-tooling stance (Pattern 12), #8 informs freshness (Pattern 11). The veto in
[`quality-rubric.md`] (#1, Verbatim Integrity) is what #4 and #5 exist to protect.
