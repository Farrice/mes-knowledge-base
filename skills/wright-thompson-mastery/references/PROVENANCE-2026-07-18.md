# PROVENANCE — wright-thompson-mastery repair (Wave 3 Lane 4 Batch 18)

Anchor → source file + location. All char offsets are `str.find()` positions in the
single-line file `extractions/wright-thompson/transcript.txt` (62,511 bytes, 0 newlines
— confirmed with `wc -c`, per ENVELOPE's warning that `wc -l` misreads single-line files
as empty).

| Anchor in genius.md | Source file | Location | Verified verbatim? |
|---|---|---|---|
| "I don't think I'm ever gonna say that explicitly..." | `extractions/wright-thompson/transcript.txt` | char 46834–46951 | Yes |
| Joe Montana "struggle with what to do when time was diminishing..." | `extractions/wright-thompson/transcript.txt` | char 47071–47189 | Yes |
| "I don't think I ever said that" | `extractions/wright-thompson/transcript.txt` | char 47198–47230 | Yes |
| "I can write around a hole in my knowledge, it's just bad" | `extractions/wright-thompson/transcript.txt` | char 40943–41056 | Yes |
| "Jay Love used to always warn me about like repetition of effect" | `extractions/wright-thompson/transcript.txt` | char 50559–50622 | Yes |
| "keep going back and back and back and back and back and back" | `extractions/wright-thompson/transcript.txt` | char 50653–50775 | Yes |
| "you can't depressurize the cabin" | `extractions/wright-thompson/transcript.txt` | char 28491–28523 | Yes |
| "break the spell by jumping ahead in time" | `extractions/wright-thompson/transcript.txt` | char 28673–28722 | Yes |
| "push a ball downhill and then clear out all the obstacles so it rolls" | `extractions/wright-thompson/transcript.txt` | char 28778–28847 | Yes |
| "not being so hamfisted with posing the question literally in the piece" | `extractions/wright-thompson/transcript.txt` | char 46236–46364 | Yes |
| "in most braintorming sessions the goal for the individuals... is to look good not to make the thing good" | `extractions/wright-thompson/transcript.txt` | char 52521–52651 | Yes (transcript's own spelling "braintorming" preserved as a noted transcription artifact) |
| "the accidental thing done in a sense of collaborative fun and joy..." | `extractions/wright-thompson/transcript.txt` | char 53604–53718 | Yes |

## Method

For each quote used as an anti-pattern anchor: `python3 -c "text.find(quote)"` against
the raw transcript, confirming an exact substring match (not a paraphrase). All 12
lookups above returned a positive index — zero UNCONFIRMED quotes in this repair.

## What was NOT re-verified this pass

`genius.md` sections outside Anti-Patterns (Core Philosophy, Voice DNA, Signature Moves
1-6, Decision Framework, Quality Rubric, Cross-Domain Application) and
`references/cross-domain-patterns.md` were written by the original extraction pass and
were already passing `verbatim_exemplars` and `named_entity_floor` — out of scope for
this repair (ENVELOPE: fix only the failing checks, preserve what passes). A spot-check
of 4 of the 12 cross-domain-patterns.md quotes (Patterns 1, 3, 9, 11) confirmed present
in transcript.txt during this pass: Pattern 1 ("I always want to know what the ending
is..." char 21614) and Pattern 9 (thesis quote, char 46834) matched by exact substring;
Pattern 3 ("purple"/"under-reported," char 40625) and Pattern 11 ("280,000 words... cut
173,000... ran at 107," char 31212) matched in substance but the raw transcript renders
them with transcription artifacts — "under reportported" (garbled) for "under-reported,"
and "It was 280,000 words and it ran at 107" (transcript repeats "280,000" rather than
stating a final word count) versus the skill's smoothed "The first draft was 280,000
words and I cut 173,000. It ran at 107" — a light, non-fabricating cleanup of a
transcription glitch, not an invented number. The remaining 8 patterns were not
individually re-checked this pass.
