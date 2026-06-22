---
description: Phase 2 engine — strip raw community text to signal while keeping every word intact (verbatim, no paraphrase), source-tag every line, and enforce the Verbatim-Integrity Gate that discards any line not found in its source chunk. Outputs one running list of real, signal-rich, source-tagged sentences.
---

# /ctm-clean — Clean the Noise into Signal (Phase 2)

Raw community text is mostly noise — jokes, tangents, arguments, "thanks for sharing." This workflow strips it to signal **while keeping the original wording untouched**, tags every surviving line to its source, and runs the Verbatim-Integrity Gate so nothing paraphrased, summarized, or grammar-fixed survives into the map. Fire it after `/ctm-gather` has produced a pile of raw, unedited language and before `/ctm-map` sorts it.

The whole advantage of the method lives or dies here. The raw, ungrammatical phrasing **is** the asset — it's what you'll hand back so people feel understood. The moment AI paraphrases, you lose the exact phrasing that makes this worth doing and you're back to guessing, just with a faster guessing machine. Cleaning means removing noise, *never* polishing language.

## Pre-Flight Gate

Load [`../genius.md`](../genius.md) if it is not already hot in this conversation. Do not extract a single line before these are answered — they are the Decision Framework from `../genius.md`, narrowed to the inputs Phase 2 actually consumes.

1. **Raw text in hand?** Is there an actual pile of unedited customer language from `/ctm-gather` (typos and all), or is this still a gather problem? No raw text → go back to `/ctm-scope` → `/ctm-gather`. This workflow never invents language to clean.
2. **Sources still attached?** Every chunk must carry where it came from (URL / permalink / thread name / call date), because every extracted line will be source-tagged. If provenance was lost in gathering, recover it before cleaning — an untraceable quote can't pass the rubric.
3. **Chunked for clean extraction?** Is the pile broken into chunks of ~a few thousand words? Smaller chunks extract cleaner than dumping everything at once (`../genius.md` Hidden Knowledge). If it's one giant blob, split it first.
4. **Verbatim discipline armed?** The word-for-word rule is loaded and you are committed to re-issuing it on the first sign of drift. This is the spine of the whole phase.

## Skill Acquisition

- **Always:** [`../genius.md`](../genius.md) (the Honesty Spine, Genius Patterns 3 "keep the typos" + 4 "the verbatim rule," Signature Move 2 "the verbatim re-issue," Quality Rubric criterion 1 Verbatim Integrity).
- **The canonical method:** [`../references/customer-truth-map-guide.md`](../references/customer-truth-map-guide.md) Phase 2 — the primary truth; where this workflow diverges, the guide wins.
- **The exact prompt:** [`../references/prompt-library.md`](../references/prompt-library.md) **P3** (expert verbatim + the enhanced source-tag/drift-guard version this workflow runs).
- **Upstream input:** `/ctm-gather` (the raw pile). If gathering used NotebookLM, note that drafting/reorganizing is better in a normal chat window — move the work over once the raw text is in hand (`../genius.md` Hidden Knowledge).
- **Downstream:** hands the cleaned running list to `/ctm-map` (Phase 3 sort).

## Execution

Work one chunk at a time. Each numbered step has a move, a diagnostic, and a template marked *vary, never verbatim*. A worked thread runs through all of them — audience: **solo bookkeepers who just lost a big client** (the narrow target from the guide), source: a midnight thread in r/Bookkeeping.

### 1. Frame the chunk and run P3

**Move.** Feed AI one chunk (~a few thousand words) and run prompt **P3** from [`../references/prompt-library.md`](../references/prompt-library.md): extract only the sentences that reveal thoughts, feelings, actions, and experiences — pains, desired outcomes, emotional reactions — under the three rules below. Smaller chunks give cleaner extractions; resist the urge to dump the whole pile.

**The three rules (verbatim, from P3 / guide Phase 2):**
1. **Word-for-word.** Return the original sentences exactly. Do not paraphrase, summarize, or clean up the grammar.
2. **Drop the noise.** Cut anything that is just chitchat, jokes, or off-topic.
3. **Bracket for sense.** If a quote is gold but needs a few surrounding words to parse, add them *in brackets* — the original wording stays untouched.

**Diagnostic:** Is each returned line a real sentence from the chunk, or did AI quietly smooth it? Read three at random against the source.

**Template (vary):** the P3 prompt block, with the source identifier named at the top of the chunk so it can be tagged downstream.

### 2. Source-tag every surviving line

**Move.** Append a source tag to every extracted line so the running list is traceable: `> "quote, exactly as written" — [source, date/permalink]`. A line without a source can't be defended at the gate and is treated as suspect.

**Diagnostic:** Could a skeptic open the source and find this exact sentence? If not, it doesn't get tagged — it gets discarded (Step 3).

**Template (vary):**
> *"i lost my biggest client friday and i keep recalculating the same number hoping it changes"* — [r/Bookkeeping, 2026-03, permalink]

### 3. Run the Verbatim-Integrity Gate (the distinguishing feature)

**Move — this is what makes the cleaned list trustworthy.** Every extracted line must be a **substring of its source chunk**. Don't eyeball it — run the deterministic backstop script, which is the gate made literal:

```bash
python3 execution/ctm_verbatim_check.py --source <raw_chunk_file> --quotes <extracted_quotes_file>
```

It exits 1 and lists every non-verbatim offender (bracketed insertions like `[illustrative]` and source tags are allowed). Then act on the result:
- **No offenders (exit 0) → keep the list.** Every line is real, word-for-word, traceable.
- **Offenders listed → discard each one**, then re-issue the verbatim rule to AI before continuing:

  > *"Return these sentences word for word. Do not paraphrase. Do not fix the grammar. Do not summarize."*

Treat drift as a defect to correct, not a style choice (`../genius.md` Signature Move 2). If a single chunk produces multiple non-substring lines, re-run the whole chunk after re-issuing the rule — the model has slipped into summarizing mode and the rest of its output is suspect.

**Diagnostic (the gate, in one question):** *Is this exact line present in the source chunk?* Yes → it survives. No → it's gone, and the rule gets restated. There is no "close enough" — a tidied comma or a fixed typo is a fail, because the typo was the asset.

**What discard looks like in the thread:**
- AI returned: *"I lost my largest client on Friday and keep recalculating the figure, hoping it will change."* → **DISCARD** (grammar fixed, "biggest"→"largest," "number"→"figure"; not a substring). Re-issue the rule, re-run the chunk.
- After re-issue, AI returned: *"i lost my biggest client friday and i keep recalculating the same number hoping it changes"* → **KEEP** (exact substring; the lowercase, the missing comma, the raw cadence all preserved).

### 4. Append to the one running list, then advance the chunk

**Move.** Add the surviving, source-tagged lines to a single running list — the raw ore for the map. Then take the next chunk and return to Step 1. The output of Phase 2 is **one list**, not per-chunk fragments.

**Diagnostic:** Has the chunk stopped surprising you, or are new pains/wishes/phrasings still appearing? Keep going while it surprises; the depth-over-sweep rule from `../genius.md` Hidden Knowledge applies here too.

### Worked thread — solo bookkeeper, one chunk's running-list contribution

After P3 + source-tag + gate on a single r/Bookkeeping chunk, the running list gains (all KEEP — each verified as a substring of the chunk):
> *"i lost my biggest client friday and i keep recalculating the same number hoping it changes"* — [r/Bookkeeping, 2026-03, permalink]
> *"honestly im not even sure what id say to land another one this size"* — [r/Bookkeeping, 2026-03, permalink]
> *"i just keep a messy spreadsheet and re-check it every monday so nothing slips"* — [r/Bookkeeping, 2026-03, permalink] *(DO-category workaround — flagged for /ctm-map → /ctm-gaps)*

Discarded at the gate (not substrings — paraphrased or grammar-fixed): a smoothed version of line 1, and a summary line AI invented ("Many bookkeepers feel financial anxiety after client loss") that appears nowhere in the source. The summary is the most dangerous discard — it *sounds* true and is entirely manufactured.

> All quotes above are `[illustrative]` placeholders for format demonstration only. **A real run uses harvested verbatim quotes only** — every line a literal substring of a real source, source-tagged, gate-verified. Nothing here is invented at run time.

## Content-Type Adaptations

The verbatim rule and the gate never change. *What counts as a "chunk," what noise looks like, and how provenance is captured* shift by source type.

| Source type | How cleaning changes |
|---|---|
| **Reddit / forum threads** | Chunk by thread or by ~few-thousand-word block. Noise = memes, "this," award spam, mod notes. Keep timestamps + permalinks as the source tag; nested replies often carry the rawest emotion. |
| **Reviews (yours & rivals')** | Each review is its own micro-chunk. Star rating travels with the quote as context (a 1-star's phrasing is gold). Drop "would recommend"/"5 stars!" boilerplate; keep the specific complaint verbatim. |
| **Sales / discovery call transcripts** | Chunk by speaker turn. Keep ONLY the customer's words, never the rep's. Disfluencies ("um," "like," "i guess") are signal, not noise — they mark where the real feeling is. Source tag = call date + speaker. |
| **Support tickets / emails** | One ticket = one chunk. Strip greetings/signatures/ticket numbers; keep the problem statement exactly. Frustrated escalations are the highest-signal lines. |
| **Social comments / DMs** | Short chunks; many lines per screen. Drop emoji-only and tag-only replies; keep the offhand complaint that wasn't meant to be analyzed — that's the unprompted gold. |
| **YouTube comment sections** | Chunk by video. Heavy noise ratio; the gate matters most here. Keep the "I clicked because…" and "I still don't get…" comments verbatim. |

## Output Requirements

Return, in this order:

1. **One running list** of cleaned, signal-rich sentences — every line word-for-word from its source, every line source-tagged `> "quote" — [source, date/permalink]`.
2. **A gate log** — count of lines kept vs. discarded, and for each discard the reason (paraphrase / grammar fix / summary / not found in source) plus how many times the verbatim rule had to be re-issued. Drift that recurs is a signal the chunk size is too large or the model needs a harder constraint.
3. **DO-workaround pre-flags** — any line describing a DIY fix marked inline (it becomes a `⚠ WORKAROUND` in `/ctm-map`).
4. **One-line honesty confirmation:** that every surviving line is a verified substring of a real source and nothing was invented, smoothed, or summarized.

If no raw text was supplied, return that as the blocker and route to `/ctm-gather` rather than cleaning imagined language.

## Quality Gate

Score against the `../genius.md` Quality Rubric. This workflow **owns criterion 1 (Verbatim Integrity)** and must also clear:

- **Verbatim Integrity (rubric 1) — the veto.** Every surviving line is real, word-for-word, and a verified substring of its source; zero paraphrase, summary, or grammar fix. **Any fabricated or paraphrased line is an automatic fail, regardless of every other score.** Name the gate log as the evidence or lower the score.
- **Unprompted Sourcing (rubric 2):** the cleaned lines came from unsolicited talk (reviews/threads/DMs/own-data), not survey-shaped answers. Survey-prompted phrasing flagged.
- **Source traceability:** every line carries a tag a skeptic could open and verify. An untagged "good quote" is treated as suspect, not signal.

**Honesty Spine (non-negotiable).** The customer's words are the gold; AI sorts the gold from the pebbles — **organizing, never inventing.** Cleaning removes noise; it never improves language. A fixed typo, a smoothed sentence, or an invented summary throws away the entire advantage. Real language in, the same real language out — just with the noise gone.

**Self-check (one line):** *Could a skeptic open each source and find that exact sentence, character for character?* If yes for every line, the list ships to `/ctm-map`. If no for even one, that line is discarded and the verbatim rule is re-issued before the chunk is re-run.
