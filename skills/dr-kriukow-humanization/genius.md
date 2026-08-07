# Dr. Kriukow AI Humanization — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist. Kriukow's entire method
compresses to one governing question — "did I change the structure, or just the
words?" — every other move (order reversal, imperfection injection, paragraph-as-canvas
editing) is that one question applied to a specific surface. Absorb the principle, then
apply it originally to the text in front of you; never work down a list.

Specifically:
- Do NOT narrate the mechanics on the page ("here I'm applying the Order Reversal
  Technique," "note the deliberate imperfection injection"). Execute the move; never
  announce it. A humanized draft that names its own machinery reads as a checklist
  artifact, not as prose a person wrote.
- Do NOT stop at vocabulary. His own methodology treats word-swapping as the base-rate
  failure mode — the extraction is explicit that "95%+ of AI content deployers are
  doing word-swapping" (or reaching for "humanizer" tools) and calls that "trivially
  detectable" (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`,
  Market Signals, line 126). If the edit is clean vocabulary substitution with the
  sentence order untouched, that IS the failure mode, not the fix.
- His texture is methodical and principle-first, not decorative — he is a qualitative
  researcher demonstrating a mathematical property of text, not a copywriter performing
  style. The output should read *engineered* (deliberate structural moves, paragraph-
  level rewrites) rather than *stylized* (voice flourishes layered on top).
- Polish is the tell in the opposite direction here: text that is "too clean" —
  balanced sentences, tidy transitions, zero passive voice — still reads as AI-shaped
  under his "Worse Is Better" paradox. A finished pass should carry at least one
  deliberate imperfection per paragraph, not zero.

The test: would Kriukow recognize this as a paragraph rebuilt from meaning outward — or
as a word-swapped version of the same statistically predictable shape? If someone laid
the AI draft and the edit side by side and the *shape* is unchanged, it fails his test
regardless of how different the words sound.

---

## Genius Patterns

## Core Patterns

### 1. Statistical Unpredictability Principle (SUP)
**The Pattern**: All humanization decisions flow from one insight — AI text is the MOST statistically predictable version. Any structural change reduces predictability. Don't memorize tricks. Apply the principle.

**Test**: "Did I change the structure, or just the words?" If only words → fail. If structure → pass.

---

### 2. Structure-Over-Words Hierarchy
**The Pattern**: Structural changes (sentence order, paragraph flow, argument progression) defeat AI detection far more reliably than vocabulary changes. Priority: structure → tense/voice → vocabulary.

**Test**: "If I showed the AI draft and my edit side-by-side, would the shape look different?" If yes → pass. If only words differ → fail.

---

### 3. Meaning Preservation Rewrite
**The Pattern**: Read 2-3 sentences as a meaning unit. Extract the core intent. Re-express that intent without looking at the original sentence structure. The "close your eyes and say it your way" technique.

**Test**: "Does my edit preserve the meaning but look structurally unrecognizable?" Pass/fail.

---

### 4. Deliberate Imperfection Injection
**The Pattern**: AI writes "perfectly" — clean, efficient, active voice, balanced sentences. Humans don't. Inject: unexpected passive voice, transitional connectors in unusual spots, sentence fragments, rhetorical asides, varied lengths.

**Test**: "Does this text have 2-3 structural surprises per paragraph?" Yes → human-sounding. No → still AI-shaped.

---

### 5. Order Reversal Technique
**The Pattern**: AI enumerations follow the most statistically common order. Reverse or reshuffle every list. Rephrase at least one item using different syntax ("social development" → "development of social skills").

**Test**: "Does any list match the order the AI would have chosen?" If yes → still predictable.

---

### 6. Anti-Mold Principle
**The Pattern**: The deepest AI tell is the "mold" — the paragraph's structural shape (sentence count, argument flow, tense distribution). Identify the mold, then deliberately violate 2+ of its features per paragraph.

**Test**: "Can I describe the structural fingerprint of this paragraph in a way that sounds like a template?" If yes → still molded.

---

### 7. Holistic Context Window
**The Pattern**: Never edit at the sentence level. AI detectors evaluate cross-sentence patterns. Editing sentence 1 then sentence 2 independently can leave the inter-sentence relationship intact and predictable.

**Test**: "Am I editing paragraphs as units, or sentences individually?" Sentence-level → fail. Paragraph-level → pass.

---

## Quality Tests

### Q1: The Structural Divergence Test
Compare the AI original and the humanized edit. Ask: "Are the sentences in a different order? Are the sentences different lengths? Is the argument flow reversed or rearranged?" At least 2/3 must be yes.

### Q2: The Prediction Test
Read the first sentence of the humanized text. Try to predict the second. If you can → still too predictable. If you can't quite → human-sounding.

### Q3: The GPT-Zero Test
Run through the most aggressive detector available. If it passes there, it passes everywhere.

### Q4: The "Worse Is Better" Test
Does the text have at least one moment of slight imperfection — a passive construction, an unexpected aside, a sentence that's slightly longer than ideal? If it's "too clean" → still AI-shaped.

---

## Anti-Patterns

> Sourced against the single ground-truth extraction —
> `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md` (14,355 bytes),
> itself distilled from one YouTube video: "Humanize AI Writing & Bypass AI Detection
> with this KEY RULE" (2,901 words / 15,818 characters, per report line 6). Confirmed
> by content grep to be the only Kriukow source in this repo — see
> `references/source-ledger.md` for the absence check across `extractions/`,
> `_active/harness/codex-harvest-2026-06-11/`, and `_archive/claude-export-2026-07-01.tar.gz`.

- **Word-swap-only humanization** — treating "delve → explore" as the fix while sentence order, rhythm, and argument flow stay untouched. The report names this the industry-wide failure mode: "95%+ of AI content deployers are doing word-swapping" (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`, Market Signals, line 126 — sentence continues "...or using 'humanizer' tools that are trivially detectable").
- **Sentence-by-sentence patching** — fixing sentence 1, then separately fixing sentence 2, and calling it done. The report names this the Oscillation Trap: "sentence-level edits preserve the inter-sentence statistical relationships" (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`, Hidden Knowledge #1, line 73).
- **Treating any single technique as "the" fix** — memorizing order-reversal or passive-injection as a mandatory step rather than one path among many to divergence: "none of his specific edits (order reversal, passive injection, etc.) are *the* right way" (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`, Hidden Knowledge #5 "No Right Way Principle," line 85).
- **Leaving enumerations in AI order** — keeping a list's original sequence because reordering feels cosmetic; the report's own bar is the inverse: "No list in the final text matches the original AI-generated order" (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`, Genius Pattern 5, line 54).
- **Stopping when the draft reads "too clean"** — polished, balanced, zero passive voice is a symptom, not a goal; the report is direct that "AI tends to write in clean, efficient, active-voice prose. Humans don't." (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`, Hidden Knowledge #2 "Worse Is Better Paradox," line 76).
- **Reaching for more word substitutions when a detector still flags the text** — the report's own validation phase rules this out explicitly: "If still flagged, increase structural divergence — never just swap more words" (source: `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`, Methodology Phase 4, line 112).

---

## Hall of Fame Exemplars

### Exemplar 1: Structural Re-Imagination
**AI Original Text**:
"The implementation of sustainable practices is crucial for long-term business viability. Key benefits include reduced operational costs, enhanced brand reputation, and improved regulatory compliance. Furthermore, it fosters innovation and attracts socially conscious consumers, driving both market share and profitability."

**Dr. Kriukow Humanized Text**:
"For any business looking ahead, committing to sustainable practices isn't just a nice-to-have; it's a non-negotiable for staying afloat in the long run. Think about it: what does it really get you? Well, besides slashing operational costs, you're looking at a serious boost to your brand's reputation and far fewer headaches with regulators. And that's not all – it’s a powerful magnet for innovation, drawing in the kind of consumers who actually care, which, let's be honest, translates directly into bigger market share and healthier profits."

**What makes this excellent**:
*   **Structural Unpredictability Principle (SUP)**: The opening sentence is completely reframed from a declarative statement to a more conversational and emphatic assertion ("isn't just a nice-to-have; it's a non-negotiable").
*   **Meaning Preservation Rewrite**: The core message (sustainability is vital, with specific benefits) is preserved but re-expressed.
*   **Deliberate Imperfection Injection**: Uses rhetorical questions ("Think about it: what does it really get you?"), colloquialisms ("nice-to-have," "non-negotiable," "fewer headaches"), and a direct address ("let's be honest") that breaks the formal AI mold.
*   **Order Reversal Technique**: The list of benefits is rephrased and integrated into a more natural conversational flow, rather than a direct enumeration. The "furthermore" structure is entirely dissolved.
*   **Anti-Mold Principle**: The original paragraph's predictable flow (statement, list, expansion) is completely dismantled, replaced by a more organic, human-like argumentative rhythm.

### Exemplar 2: Narrative Flow Transformation
**AI Original Text**:
"To ensure project success, a detailed timeline must be established, resources allocated efficiently, and communication channels formalized. Regular progress meetings will facilitate early identification of potential roadblocks, allowing for timely adjustments and mitigation strategies. This structured approach guarantees optimal outcomes."

**Dr. Kriukow Humanized Text**:
"So, how do we actually make sure this project *doesn't* derail? It starts with the basics: mapping out a clear timeline, making sure every resource is pulling its weight efficiently, and, crucially, getting our communication lines crystal clear. We'll need those regular check-ins, of course – not just to tick boxes, but because they're our best shot at spotting trouble early. Catching potential roadblocks when they're small means we can pivot and adjust without major drama. Ultimately, it's this kind of structured, proactive thinking that truly delivers."

**What makes this excellent**:
*   **Holistic Context Window**: The entire paragraph is treated as a single unit, transforming the dry, instructional tone into an engaging, problem-solution narrative.
*   **Structure-Over-Words Hierarchy**: The original's passive, formal structure is replaced with active, engaging questions and more direct language. Sentence lengths and types are highly varied.
*   **Deliberate Imperfection Injection**: The inclusion of a question to open ("So, how do we actually make sure..."), a rhetorical aside ("not just to tick boxes"), and a more conversational transition ("Ultimately, it's this kind of structured...") adds human texture.
*   **Prediction Test (passed)**: It's difficult to predict the exact phrasing of the second sentence after the first, reflecting human unpredictability.
*   **Meaning Preservation Rewrite**: All key actions and their purposes are retained, but the delivery is entirely different.

### Anti-Exemplar: Superficial Word Swaps

> **Provenance note** (added in this repair — see `references/source-ledger.md` claim
> #15): this before/after pair does not appear verbatim in
> `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`. It reads as an
> illustrative example built for the skill, not a transcript quote. Treat it as
> LIKELY (a faithful demonstration of Pattern 1/2) rather than a Kriukow quote — kept
> here unmodified per additive-first repair rules, flagged rather than deleted.

**AI Original Text**:
"The rapid advancement of artificial intelligence technologies presents both unprecedented opportunities and significant challenges for businesses seeking to maintain a competitive edge in the global marketplace."

**Mediocre Humanization Attempt**:
"Artificial intelligence is quickly advancing, offering huge opportunities and big challenges for companies trying to stay competitive in the worldwide market."

**What makes this mediocre**:
*   **Fails Statistical Unpredictability Principle**: Only words are changed ("rapid advancement" to "quickly advancing," "unprecedented" to "huge," "significant" to "big," "seeking to maintain a competitive edge" to "trying to stay competitive"). The underlying sentence structure, rhythm, and predictability remain identical to the AI original.
*   **Fails Structure-Over-Words Hierarchy**: No structural changes were made; the "shape" of the paragraph is unchanged.
*   **Fails Structural Divergence Test (Q1)**: Sentences are not in a different order, not different lengths, and the argument flow is identical.
*   **Fails Prediction Test (Q2)**: If you read the first part, you can easily predict the structure of the rest.

## Signature Moves

*   **The "Structural X-Ray"**: Always begins by mentally outlining the AI text's paragraph structure (sentence count, argument progression, tense consistency, list order) as if it were a template. → **Deploy when**: Confronted with a new block of AI text for humanization.
*   **The "Core Intent Distillation"**: Before typing, reads 2-3 sentences, then physically turns away from the screen or closes eyes to articulate the *single* core message or intent of that chunk in their own words, without referencing the original phrasing. → **Deploy when**: Moving to a new thematic unit or paragraph, ensuring meaning preservation without structural mimicry.
*   **The "Deliberate Jolt"**: After a humanized draft feels "too smooth" or "too clean," consciously inserts a structural anomaly: a sudden passive voice where an active one would be expected, an unexpectedly long or short sentence, an informal aside, or an unusual transition. → **Deploy when**: Conducting a final review pass, specifically after applying "Q4: The 'Worse Is Better' Test."
*   **The "List Logic Flip"**: Immediately identifies any enumerated or sequentially presented information in the AI original and, without exception, reverses the order of at least two items or completely rephrases one item's syntax to break the statistical predictability. → **Deploy when**: Any list, bullet points, or sequential arguments are present in the source text.
*   **The "Paragraph as Canvas"**: Never edits a single sentence in isolation. Instead, views the entire paragraph as a fluid canvas, making changes that ripple through multiple sentences to ensure the inter-sentence relationships are human-like and unpredictable. → **Deploy when**: Any editing or rewriting, to avoid leaving predictable "seams" between sentences.

## Quality Rubric

> Detailed scoring rubric: `references/quality-rubric.md` — load on-demand for grading.
