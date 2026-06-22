---
description: Phase 3 engine — sort the cleaned, source-tagged list into SAY / THINK / FEEL / DO + PAINS / GAINS (a quote may sit in several), keep original wording, name 2–3 strongest patterns per category, flag vivid/repeated quotes as copy gold, and tag every DO-category workaround ⚠ WORKAROUND. Outputs the saved Customer Truth Map.
---

# /ctm-map — Build the Customer Truth Map (Phase 3)

This is the heart of the system: take the cleaned, source-tagged running list from `/ctm-clean` and sort every quote into the six categories — **Say / Think / Feel / Do** plus **Pains / Gains** — keeping the original wording, then name the strongest patterns and circle the gold. A flat list of quotes isn't usable; an organized map is. Fire this after `/ctm-clean`, before `/ctm-jobs` reframes the pains.

The structure is the **Empathy Map** (Dave Gray + XPLANE, mid-2000s, popularized in *Gamestorming*) with one twist: keep the categories, fill them **only with real, sourced quotes**, and add an explicit Pains/Gains split so the opportunity is visible. The AI is not inventing anything here — it's reorganizing your customer's real words into a shape you can act on.

## Pre-Flight Gate

Load [`../genius.md`](../genius.md) if it is not already hot in this conversation. Do not sort a single quote before these are answered — they are the Decision Framework from `../genius.md`, narrowed to what Phase 3 consumes.

1. **Cleaned list in hand?** Is there a gate-passed, source-tagged running list from `/ctm-clean`, or is this still raw text? Raw text → run `/ctm-clean` first. This workflow sorts existing real quotes; it never extracts or invents new ones.
2. **One customer, one problem cluster?** Is the target narrow enough (the "solo bookkeeper who just lost a big client" test)? A blurry target produces blurry patterns. If the list mixes two audiences, split into two maps.
3. **Source tags intact?** Every quote must still carry its `— [source, date/permalink]` tag through the sort, so the map stays traceable end to end.
4. **Verbatim discipline still armed?** Sorting must never become an excuse to tidy a quote so it "reads better" in its category. Wording stays exactly as cleaned.

## Skill Acquisition

- **Always:** [`../genius.md`](../genius.md) (the Map Structure, Genius Pattern 5 "the Do-category goldmine," Signature Move 3 "circle the workarounds," Quality Rubric criteria 4 Map Completeness + 5 Do-Category Mining).
- **The canonical method:** [`../references/customer-truth-map-guide.md`](../references/customer-truth-map-guide.md) Phase 3 — the primary truth; where this workflow diverges, the guide wins.
- **The exact prompt:** [`../references/prompt-library.md`](../references/prompt-library.md) **P4** (expert verbatim + the enhanced version that adds the `⚠ WORKAROUND` tag and keeps source tags through the sort).
- **Upstream input:** `/ctm-clean` (the gate-passed running list).
- **Downstream:** the saved map feeds `/ctm-jobs` (pains → JTBD), `/ctm-gaps` (DO-workarounds → gap table), and the whole Phase-5 apply layer (`/ctm-to-copy`, `/ctm-to-content`, `/ctm-to-offer`).

## Execution

Each numbered step has a move, a diagnostic, and a template marked *vary, never verbatim*. A worked thread runs through all of them — audience: **solo bookkeepers who just lost a big client.**

### 1. Sort every quote into the six categories (run P4)

**Move.** Feed the cleaned list to AI and run prompt **P4** from [`../references/prompt-library.md`](../references/prompt-library.md). Sort every quote, keeping the original wording. **A quote may appear in more than one category** if it genuinely fits — a single line can be both a FEEL and a PAIN.

- **SAY** — stated out loud / in writing (direct quotes).
- **THINK** — beliefs/assumptions *implied* but not said directly.
- **FEEL** — emotions: frustrations, hopes, fears.
- **DO** — actions and behaviors, **including the workarounds and DIY fixes they cobbled together.**
- **PAINS** — specific problems, obstacles, risks.
- **GAINS** — outcomes, wins, "if only" wishes.

**Diagnostic:** Did any category come back empty, or did every quote land in exactly one box? Empty categories usually mean the gather was too narrow; one-box-each usually means AI under-sorted (most real lines are dual-coded).

**Template (vary):** the P4 prompt block, with the cleaned list pasted in and source tags preserved on every line.

### 2. Keep wording + source tags through the sort

**Move.** Verify the sorted quotes are still verbatim and still tagged. Sorting is a *move*, not an *edit* — a line that got tidied to "fit" its category is a verbatim-integrity failure and goes back to its exact form.

**Diagnostic:** Spot-check three sorted quotes against the cleaned list. Same characters? Same tag? If not, restore.

### 3. Name the 2–3 strongest patterns per category

**Move.** Under each category, write a short summary naming the **2–3 strongest patterns** you see — the recurring shape of how this customer talks in that dimension. Patterns are observations *about* the quotes, drawn only from quotes that are present; they never introduce a claim no quote supports.

**Diagnostic:** Can you point at the specific quotes each named pattern rests on? If a pattern has no quotes under it, it's a guess — cut it.

**Template (vary):** *"FEEL — strongest patterns: (1) shame framed as professional inadequacy ('not even sure what id say'); (2) the fear is exposure, not income…"* — each clause traceable to listed quotes.

### 4. Flag the copy gold (vivid / repeated)

**Move.** Mark any quote that is unusually **vivid** or **repeated often** across sources — these are the most useful in copy later (`../genius.md` Map Structure). A vivid line is a pre-written headline; a repeated line is a confirmed pattern.

**Diagnostic:** If you had to write one headline tomorrow, which three listed quotes would you reach for? Flag those at minimum.

**Template (vary):** `★ COPY GOLD` inline on the flagged line, with a one-word reason (vivid / repeated-3×).

### 5. Tag every DO-category workaround ⚠ WORKAROUND (the signature move)

**Move — this is what turns a map into an opportunity finder.** Walk the DO category. Every described workaround, DIY fix, manual checklist, or duct-tape routine gets tagged `⚠ WORKAROUND`. A workaround is **"a problem someone cared about enough to solve badly"** — a flashing sign at exactly where existing solutions (maybe yours) fail. Each one is an unmet-need flag headed straight for `/ctm-gaps`.

**Diagnostic:** For each DO entry, ask: *did the customer build or maintain something to cope with this?* Yes → `⚠ WORKAROUND`. A described habit that solves a real problem badly is the highest-value line on the map.

**Template (vary):**
> *"i just keep a messy spreadsheet and re-check it every monday so nothing slips"* — [r/Bookkeeping, 2026-03] `⚠ WORKAROUND` `★ COPY GOLD`

### 6. Save the map as the living document

**Move.** Write the result to a single plain-text/markdown file (e.g., `customer-truth-map.md`) — the document you keep open and reuse. Date the top (every refresh writes a dated note, `../genius.md` Signature Move 7). This file is what every downstream workflow reads.

**Diagnostic:** Is the file self-contained — could `/ctm-gaps` run from it alone, with all six categories, named patterns, copy-gold flags, and `⚠ WORKAROUND` tags present?

### Worked thread — solo bookkeeper, an excerpt of the saved map

```
CUSTOMER TRUTH MAP — solo bookkeepers who just lost a big client   [built 2026-03]

PAINS
- "i lost my biggest client friday and i keep recalculating the same number hoping it changes"  — [r/Bookkeeping, 2026-03]  ★ COPY GOLD (vivid)
- "honestly im not even sure what id say to land another one this size"  — [r/Bookkeeping, 2026-03]
  Patterns: (1) revenue-cliff panic; (2) a pipeline that was never built because one client masked it.

FEEL
- "i keep recalculating the same number hoping it changes"  — [r/Bookkeeping, 2026-03]
  Patterns: (1) shame read as professional inadequacy; (2) fear of exposure over fear of income loss.

DO
- "i just keep a messy spreadsheet and re-check it every monday so nothing slips"  — [r/Bookkeeping, 2026-03]  ⚠ WORKAROUND  ★ COPY GOLD
  Patterns: (1) manual, anxiety-driven tracking; (2) follow-up handled by memory + dread, not system.

GAINS
- "if i just had two more clients this size id stop checking my bank app at 2am"  — [r/Bookkeeping, 2026-03]
  Patterns: (1) the wanted outcome is calm, not just revenue.
```

> Every quote above is `[illustrative]` — placeholders for format only. **A real run sorts harvested verbatim quotes only**, each a gate-passed substring of a real source, source-tagged, never invented or smoothed during the sort.

## Content-Type Adaptations

The six categories are universal; *which categories run hottest and what the patterns reveal* shifts by where the language came from.

| Source mix | How the map changes |
|---|---|
| **Reddit / forum-heavy** | THINK and FEEL run rich (people theorize and vent openly); DO workarounds are abundant and explicit. Watch for loud-voice skew — one prolific poster can fake a "pattern." |
| **Review-heavy (yours + rivals')** | PAINS and GAINS dominate; competitor reviews especially expose `⚠ WORKAROUND` behavior ("I had to keep my own spreadsheet alongside their app"). DO is where the gap analysis gold concentrates. |
| **Sales / discovery calls** | SAY and PAINS are dense; FEEL surfaces in hesitations. Calls are the single best source (the person spoke directly about your space, `../genius.md` Hidden Knowledge) — weight their patterns higher. |
| **Support tickets / emails** | PAINS and DO dominate (every ticket is a problem + an attempted fix). Heavy `⚠ WORKAROUND` yield. GAINS are thin here — supplement from another source. |
| **Social comments / DMs** | SAY and FEEL run hot; offhand, unprompted lines make the best COPY GOLD. PAINS often implied (THINK) rather than stated. |
| **Mixed / triangulated** | Run the sort per source first, keep source tags, then note which patterns appear across sources vs. in one only — this pre-stages `/ctm-triangulate` (Consistent Truths vs Source-Specific). |

## Output Requirements

Return, in this order:

1. **The saved Customer Truth Map document** — dated at top; all six categories (SAY / THINK / FEEL / DO / PAINS / GAINS) populated only with real, source-tagged, verbatim quotes; a quote allowed in multiple categories where it genuinely fits.
2. **2–3 named patterns per category** — each traceable to the specific listed quotes it rests on.
3. **`★ COPY GOLD` flags** on vivid/repeated quotes, with a one-word reason.
4. **`⚠ WORKAROUND` tags** on every DO-category DIY fix — the explicit unmet-need flags handed to `/ctm-gaps`.
5. **One-line honesty confirmation:** that every quote in the map is a real, source-tagged, verbatim line and that sorting introduced no new or smoothed language.

If the cleaned list was missing or untagged, return that as the blocker and route to `/ctm-clean` rather than sorting imagined or untraceable quotes.

## Quality Gate

Score against the `../genius.md` Quality Rubric. This workflow **owns criteria 4 (Map Completeness) and 5 (Do-Category Mining)** and must also clear:

- **Map Completeness (rubric 4):** all six categories populated; 2–3 named patterns each; vivid/repeated quotes flagged. An empty category or an unflagged map caps the score.
- **Do-Category Mining (rubric 5):** every workaround surfaced and tagged `⚠ WORKAROUND` as an unmet-need signal. A DO category with DIY fixes left un-circled is a miss — those are the gap-analysis seeds.
- **Verbatim Integrity (rubric 1) — the veto.** Every sorted quote is still real, word-for-word, and source-tagged; the sort smoothed nothing. **Any quote tidied, paraphrased, or invented during sorting is an automatic fail, regardless of every other score.**

**Honesty Spine (non-negotiable).** The customer's words are the gold; AI sorts the gold from the pebbles — **organizing, never inventing.** Sorting reorganizes real language into a usable shape; it never adds a quote, smooths a quote, or asserts a pattern no quote supports. A map of invented or tidied lines reads like marketing and converts like marketing — indistinguishable from the guessing it was built to replace.

**Self-check (one line):** *Is every line in this map a real, source-tagged quote, every named pattern backed by listed quotes, and every DO-workaround circled?* If yes, the map is saved and shipped to `/ctm-jobs`. If no, the failing category goes back to the sort before anything downstream runs.
