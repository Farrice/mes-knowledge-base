# Source Ledger — mitch-albom-writing-mastery

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 11). This ledger records every
source consulted for this skill and labels every non-trivial claim
VERIFIED / LIKELY / UNCONFIRMED per `directives/verification-agent-protocol.md`.
"Verified" here means: the exact quote was located by direct string search
in the cited file (offsets recorded); paraphrase/derived claims are LIKELY;
anything I could not locate a source for is UNCONFIRMED, never silently
dropped or invented.

## Sources Consulted (with sizes — `wc -c`)

| File | Size (bytes) | Role |
|---|---|---|
| `extractions/mitch-albom/transcript.txt` | 92,280 | PRIMARY. Full transcript of the *How I Write* interview with David Perell (2026). Single-line text (no internal newlines) — verified by direct substring search, offsets given below are character positions. |
| `skills/mitch-albom-writing-mastery/references/genius-patterns.md` | 4,578 | Earlier-generation pattern skeleton (Patterns 1–18, no embedded quotes). Pre-dates the quote-enriched genius.md. Read in full. |
| `skills/mitch-albom-writing-mastery/references/hidden-knowledge.md` | 3,231 | Earlier-generation hidden-knowledge skeleton. Read in full. |
| `skills/mitch-albom-writing-mastery/references/implementation.md` | 2,630 | Implementation notes. Read in full. |
| `skills/mitch-albom-writing-mastery/references/use-cases.md` | 12,200 | Use-case catalog. Read in full. |
| `skills/mitch-albom-writing-mastery/references/cross-domain-patterns.md` | 15,990 | Cross-domain deployment notes. Read in full. |
| `skills/mitch-albom-writing-mastery/SKILL.md.old` | 3,783 | Prior SKILL.md version, superseded. Read for continuity check only. |

`ls extractions/ | grep -i albom` returns exactly one directory
(`extractions/mitch-albom/`) containing exactly one file
(`transcript.txt`, 92,280 bytes — not 0-byte, not unrecoverable). This is
the only primary source for this expert; no other Albom source material
exists in the repo as of this pass.

## Claim-by-Claim Labels

### Biographical facts (SKILL.md / genius.md header)
- "He's written 14 books... sold more than 40 million copies... writing for more than 45 years" — **VERIFIED**. Verbatim in transcript.txt, offset ~0–420 (interview cold open).
- "*Tuesdays with Morrie*... at one point was the bestselling memoir of all time" — **VERIFIED**. Verbatim in transcript.txt cold open.
- "*The Five People You Meet in Heaven*" — **VERIFIED**. Named directly in transcript.txt cold open.

### Anti-Patterns (AN-1 through AN-7, genius.md)
- AN-1 quote "a cheap attempt to try to write flowery phrases about death" — **VERIFIED**, transcript.txt offset ~15,744.
- AN-2 quote "I don't start with characters. I don't start with plots. I start with a theme" — **VERIFIED**, transcript.txt offset ~8,187.
- AN-3 quote "the minute they let go of that cord, they're never getting back" — **VERIFIED**, transcript.txt offset ~1,697.
- AN-4 quote "those long pages with all the details... I don't ever like to read" + "the Tom Clancy... this is how a submarine works kind of" — **VERIFIED**, transcript.txt offset ~6,183–6,234 (contiguous passage, mother's compliment).
- AN-5 quotes "opens up your ability to look at things in a... marveling way" and "when you marvel at something, you use a different language" — **VERIFIED**, transcript.txt offset ~69,222. Note: the two clauses appear split across an interviewer/Albom exchange in the raw transcript; genius.md's earlier draft ("you use a different language when you marvel") over-smoothed this into a single sentence — corrected in this pass to keep the two clauses separately quoted and accurate to the transcript.
- AN-6 quote "98% writing for readers" and the doo-wop detail — **VERIFIED**, transcript.txt offset ~40,950 and ~40,950–41,300 respectively. Transcript spelling is "doo-op" (likely an auto-transcription artifact for "doo-wop"); this pass now quotes the transcript's actual spelling ("50s doo-op rock and roll") rather than the previously silently corrected "doo-wop."
- AN-7 quote "I wouldn't change any of it, but... the reader feels overwhelmed by all these terrible acts" (Albom's editor, re: *The Little Liar*) — **VERIFIED**, transcript.txt offset ~52,984–53,700. This anchor was previously missing (AN-7 had no quote); added in this pass.

### Named-entity enrichment added this pass (Patterns 7, 8, 9, 10, 11, 13, 18; Hidden Knowledge 1, 3, 5, 8, 10; Signature Moves)
- "holding a child's attention... you see it on their eyes like when they're starting to fade" + "I operate an orphanage" + "three-year-old now" — **VERIFIED**, transcript.txt offset ~5,255–5,716.
- "your first paragraph and your last paragraph tend to work together" + "I like to know the endings of my books before I start them" — **VERIFIED**, transcript.txt offset ~2,059–2,090.
- "when you write, you rock back and forth, but sometimes you stop" / "it's not working when I stop" — **VERIFIED**, transcript.txt offset ~60,032–60,205.
- "I had the image of a color wheel" / "I've been on blue for a long time" — **VERIFIED**, transcript.txt offset ~57,829.
- "force yourself to stop in the middle of a sentence that you really want to finish" — **VERIFIED**, transcript.txt offset ~28,618.
- "I just email myself and I tag the... subject line, book idea" + "a whole bag of just little pieces of yellow paper" — **VERIFIED**, transcript.txt offset ~43,700–44,228.
- "this is the first one that I've really written which is about loss of love" / "loss of life is a pain that you carry with you... but you're in two different worlds" — **VERIFIED**, transcript.txt offset ~90,025.
- "the person that you yearn for and miss" — **VERIFIED**, transcript.txt offset ~91,641 (adjacent passage, same exchange).
- "I read them to her towards the end of the writing... before I turn it in" + "can't see her face" — **VERIFIED**, transcript.txt offset ~84,851–85,075.

### Cross-Domain Applications table (genius.md)
- All row content — **LIKELY**. These are the extraction team's synthesized transfers of Albom's verified patterns into marketing/copy/ghostwriting/founder-story/content-series domains. Albom never discusses LinkedIn, brand marketing, or copywriting in the source transcript — this table is a legitimate cross-domain application (labeled as such in the skill's own framing) but is not itself a verbatim claim about Albom.

### Hall of Fame Exemplars (genius.md)
- Exemplar 1 ("The Last Class") and Exemplar 2 ("The Five People's Purpose") — **UNCONFIRMED as verbatim book text**. Both are explicitly labeled "(Reconstructed from ...)" in the skill itself — they are illustrative paraphrase/pastiche written to demonstrate the patterns, not actual excerpts from *Tuesdays with Morrie* or *The Five People You Meet in Heaven*. Confirmed by direct comparison: the real opening of *Tuesdays with Morrie* does not match this text. This label was already implicit in the "Reconstructed" framing; this pass makes it explicit here so it is never mistaken for a verified book quote.
- Anti-Exemplar ("Generic Cityscape Opening") — **N/A / not a factual claim**. Deliberately fabricated negative example for illustration; carries no provenance claim about Albom.

### Signature Moves (genius.md)
- "The Peripheral Scan," "The Child's Ear Test," "The Unifying Cord Check" — **LIKELY**. Synthesized/named abstractions built from already-VERIFIED patterns (Gravedigger Technique, Three-Year-Old Attention Test, Tether Principle) rather than direct Albom quotes; the naming is the extraction team's, the underlying behavior is sourced.
- "The Mid-Sentence Anchor" — **VERIFIED** as of this pass (quote added; see Pattern 13 anchor above).

### Decision Framework (genius.md)
- Items 1–3 (theme, cord, ending) carry direct verified quotes already present before this pass ("I start with a theme... not the other way around"; "I like to know the endings of my books before I start them"). — **VERIFIED**.
- Items 4–8 (reader-vs-prose, restraint, gravedigger, 98%-for-reader, flow/breathe) — **LIKELY**, synthesized from multiple verified patterns elsewhere in the file rather than restated as fresh quotes here; no new unverifiable claims introduced.

## What Remains UNCONFIRMED (honest gap, not silently dropped)
- No second independent source exists for this expert (no book excerpts, no second interview, no written craft essay) — everything traces to the single 92,280-byte transcript. Any claim about Albom's process not traceable to that transcript (e.g., specifics of his journalism career at the Detroit Free Press beyond what's stated in the transcript, or claims about *The Little Liar*'s full plot) should be treated as UNCONFIRMED and not asserted as fact in downstream output.
- The two Hall of Fame Exemplars are UNCONFIRMED as verbatim book text (see above) — downstream workflows should not present them as direct quotes from the published books.
