# Provenance — tom-segura-comedy-storytelling repair

All anchors below trace to `extractions/Tom Segura/transcript.txt` (single-line
file, 68,444 bytes per `wc -c`; character offsets given since the file has no
line breaks). Verified by direct substring search against the raw transcript
text — not the pre-existing `references/source-quotes.md` paraphrase, though
that file's Pattern numbering is reused for cross-reference.

| Anti-Pattern item | Anchor quote (verbatim substring found in transcript.txt) | Char offset | Pattern/Hidden ref |
|---|---|---|---|
| 1. The neutral take | "it's not funny to be like, it's fine. I don't care" | 3011 | Pattern 2 |
| 2. The flat anecdote | "you gave yourself a reason to tell the story" | 48789 | Pattern 4 |
| 3. Premature editing | "The editor can't come too earl[y]" | 10390 | Pattern 5 / Hidden 2 |
| 4. Stopping at the obvious | "too obvious isn't the joke" + "yelling at the trailer before the movie" | 36638 / 37812 | Hidden 3 |
| 5. Over-selling the absurd | "if they're not trying to be funny" | 45539 | Pattern 8 |
| 6. Rushing the beat | "the longer you hold on the real amount of time" + "25-second door hold" | 45748 / 46912 | Pattern 9 |
| 7. The derivative middle | "no one else has that story" | 34161 | Pattern 13 |
| 8. Callback as tic | "callback, callback, callback" | 61964 | Pattern 15 |
| 9. Comprehensive but dead | "there's some nuance to like what he's saying" + "you've exhausted it" | 17514 / 15187 | Hidden 9 |

Verified with:
```python
t = open("extractions/Tom Segura/transcript.txt", encoding="utf-8", errors="replace").read()
t.find("<fragment>")  # all 9 fragments confirmed present, offsets as above
```

## Model Calibration section (genius.md, new "How to Use This Skill" block)
- Quotes reused inline are the same two already-verified anchors: "the editor
  can't come too early" (offset 10390) and the "yanked"/"pulled" word-choice
  contrast, which is Pattern 11 in `references/source-quotes.md` line 67 (not
  re-verified against the raw transcript in this pass — it was already present
  and unmodified in the skill's genius.md Pattern 11 section, so it inherits
  the existing PASS status of `verbatim_exemplars`/`named_entity_floor`, not a
  new claim introduced by this repair).
- The "recognize this as" / "recognition test" language is new authorial
  framing (model-calibration instruction, not a Segura quote) — written
  against Segura's actual patterns (the antenna, the dig, the way-in) per the
  ENVELOPE instruction to model but never copy `ben-watkins-storytelling/genius.md`
  lines 7-16.

## Files NOT modified (unchanged, left untouched in `skills/`)
- SKILL.md — no failing check required a SKILL.md change.
- references/source-quotes.md, references/sample-antenna-output.md,
  references/cross-domain-patterns.md, references/prompts-v2/* — source_ledger
  and workflow_contracts already PASSED pre-repair; not touched.
