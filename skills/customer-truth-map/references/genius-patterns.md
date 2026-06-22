---
description: The 12 genius patterns of the Customer Truth Map, expanded into atomic, copy-paste-ready entries — each with what it is, the executable move, the workflow to deploy it in, and a measurable success signal. Same names/numbers as genius.md.
---

# Genius Patterns — Executable (the 12)

These are the 12 patterns from [`../genius.md`](../genius.md) (§ "Genius Patterns"), expanded so an
agent can lift any one and run it. **Same names, same numbers, no contradictions** — genius.md owns
the *why*; this file owns the *do it now*. The honesty spine sits above all twelve: real language in,
organized language out, **never** invented (Pattern 1 is its enforcement).

> Format per entry — **What it is** · **Executable move** (copy-paste-ready) · **Deploy when**
> (which `/ctm-*` workflow) · **Success metric** (the measurable signal it worked).

---

### 1. Words-as-gold / AI-as-sorter
- **What it is:** Collection and organization are two different jobs; AI does *only* the second.
- **Executable move:** Before any extraction, declare the contract out loud: "Your job is to sort and
  organize the real sentences I give you. You do not write, invent, paraphrase, or improve any
  customer language." Re-assert it whenever output drifts toward composition.
- **Deploy when:** every gather / clean / map step (`/ctm-gather`, `/ctm-clean`, `/ctm-map`).
- **Success metric:** zero invented quotes; **every line traceable to a named source.**

### 2. Unprompted > prompted
- **What it is:** Talk captured when people *don't* feel observed beats survey answers — no category
  was pre-imposed on them.
- **Executable move:** In source selection, rank sources by how unsolicited they are: one-star
  reviews written at midnight, frustrated forum threads, offhand DMs > interview transcripts >
  surveys. Pick from the top of that ladder first.
- **Deploy when:** `/ctm-scope` (source selection).
- **Success metric:** **≥80% of captured lines are unsolicited** (review / thread / DM / own-data),
  not interview or survey answers.

### 3. Keep the typos
- **What it is:** The raw, ungrammatical phrasing carries the selling power; cleaning grammar
  destroys the asset you hand back so people feel understood.
- **Executable move:** Preserve sentences exactly — spelling, slang, run-ons, ALL CAPS, emoji.
  Reject any "tidied" version. If readability is needed, see Hidden Knowledge "bracket for sense."
- **Deploy when:** `/ctm-clean`.
- **Success metric:** captured lines are byte-for-byte the originals; no silent grammar fixes.

### 4. The verbatim rule
- **What it is:** One instruction outranks all others while extracting.
- **Executable move:** Issue verbatim: *"Return these sentences word for word. Do not paraphrase. Do
  not fix the grammar. Do not summarize."* The instant the AI summarizes, **stop it and re-issue the
  rule** (the move is Signature Move 2, "the verbatim re-issue").
- **Deploy when:** `/ctm-clean`, `/ctm-gather`.
- **Success metric:** spot-check 5 random extracted lines against source — 5/5 match exactly.

### 5. The Do-category goldmine
- **What it is:** A described workaround (the manual spreadsheet, the duct-tape routine) is "a problem
  someone cared about enough to solve badly" — a flashing sign at exactly where existing solutions
  (maybe yours) fail.
- **Executable move:** Scan every `DO` entry for a DIY fix or workaround and **circle it** with a
  visible marker; route each circled item to the gap table.
- **Deploy when:** `/ctm-map`, then `/ctm-gaps`.
- **Success metric:** every workaround in the map is flagged and carried into `/ctm-gaps`; none lost.

### 6. Pain → Job reframe
- **What it is:** People don't want your product; they *hire* it to make progress. The job points at
  the outcome, where the bigger ideas (positioning, offers) live.
- **Executable move:** Rewrite each pain into the JTBD template:
  `"When [situation], I want to [motivation], so I can [desired outcome]."` Then ask of the outcome:
  does this open a *positioning angle*, not just a feature?
- **Deploy when:** `/ctm-jobs`.
- **Success metric:** each top pain has a job statement whose outcome clause names a market position,
  not a feature spec.

### 7. Widest-gap-first prioritization
- **What it is:** Not all pains are equal; the widest gaps are the shortlist for what to lead with.
- **Executable move:** Build the table — `Pain/Job → Current Fix (competitors + DIY) → The Gap` —
  score gap width, sort descending, and **act only on the top rows.**
- **Deploy when:** `/ctm-gaps`.
- **Success metric:** a ranked gap table exists; the shortlist is the widest rows *with a stated
  reason*, not a flat list of every pain.

### 8. Quote-to-slot mapping
- **What it is:** Real lines are pre-proven copy ("the words are already proven because a real person
  already said them").
- **Executable move:** Pull the 10 strongest quotes and assign each a single slot — headline,
  subhead, objection-handler, or proof point — keeping the customer's exact register.
- **Deploy when:** `/ctm-to-copy`.
- **Success metric:** 10 quotes → 10 slot assignments; every slotted line is a real, sourced quote.

### 9. Grounded-idea generation
- **What it is:** Every content idea ships with the specific quote or pattern it's built on, so it's
  grounded in real language, not invented on "a slow Tuesday."
- **Executable move:** For each idea, attach the source line in brackets: `[grounded in: "<quote>"]`.
  Reject any idea that can't name its quote/pattern.
- **Deploy when:** `/ctm-to-content`.
- **Success metric:** 100% of generated ideas carry a named source quote/pattern; zero ungrounded.

### 10. Triangulation
- **What it is:** A map from one community misleads (each forum has its own culture, loud voices,
  blind spots). Build from several, then separate by confidence.
- **Executable move:** Merge maps and split every pattern into **Consistent Truths** (across most/all
  sources → high-confidence, build core messaging here) vs **Source-Specific** (one source →
  lower-confidence, hold loosely, useful for a sub-group). Label each.
- **Deploy when:** `/ctm-triangulate`.
- **Success metric:** every merged pattern carries a confidence label; nothing flattened into one
  undifferentiated list.

### 11. Freshness as the edge
- **What it is:** "A map you refresh is worth ten times a map you build once and forget." What changes
  is itself the signal — a read-out of where the customer's world is moving.
- **Executable move:** Schedule a quarterly light pass + 1–2× yearly deep rebuild, and keep a **dated
  change-log** of what was added and what shifted. Register the cadence via `/schedule`.
- **Deploy when:** `/ctm-refresh`.
- **Success metric:** a dated change-log exists (or is scheduled); each refresh records adds/shifts.

### 12. Honest about the tools
- **What it is:** Don't oversell AI — state the real limit instead of pretending capability it lacks.
- **Executable move:** Match tool to job and name the constraint: most chat tools can't reliably
  bulk-scrape Reddit; NotebookLM reaches forums better *but only from sources you hand it*; manual
  copy-paste always works. Pick the working path; say which one and why.
- **Deploy when:** `/ctm-gather` (and the `tool-wiring.md` reference).
- **Success metric:** the gather log names the tool used, its known limit, and the fallback taken when
  the primary path failed.

---

**Self-check:** Could an agent open any single entry above and run it end-to-end in a vertical it has
never touched — without inventing a quote to fill a slot? If not, the entry is under-specified.
Cross-reference [`genius-patterns`] ↔ [`hidden-knowledge.md`] (the tacit layer) ↔
[`quality-rubric.md`] (the scored layer): patterns 1, 4 enforce rubric criterion #1 (the veto).
