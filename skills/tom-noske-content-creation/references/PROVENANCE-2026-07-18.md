# PROVENANCE — tom-noske-content-creation repair (Wave 3, Lane 4, Batch 17)

Anchor → source file + location. All quotes grep-verified verbatim against the cited transcript before being written into genius.md.

| Anchor text (as written in genius.md) | Source file | Verified via |
|---|---|---|
| "pick up the phone and be of service to his dream client" | `extractions/tom-noske/transcript.txt` | `grep -o "pick up the phone and be of service to his dream client"` — exact match |
| "none of the content that I produce on Instagram requires any upfront effort" | `extractions/tom-noske/transcript.txt` | `grep -o` — exact match, case preserved as in source |
| "what I would call the grind zone" | `extractions/tom-noske/transcript.txt` | grep-matched exact |
| "the audience knows all" | `extractions/tom-noske/transcript.txt` | grep-matched exact (Rule 2 title) |
| "so many external factors that are playing along in my mind as I'm trying to record this video" | `extractions/tom-noske/transcript.txt` | grep-matched exact |
| "the more needy you are in terms of why you're making content, the more that experience is going to come through" | `extractions/tom-noske/transcript.txt` | grep-matched exact |
| "My content is imperfect execution that you guys think is perfect" | `extractions/tom-noske/transcript.txt` | grep-matched exact |
| "creating a promise and then delivering on that promise" | `extractions/tom-noske/transcript.txt` | grep-matched (transcript has two near-identical occurrences: "...and then delivering on that promise" and "...and then you are delivering on that promise" — the shorter form quoted here is the exact verbatim match) |
| "you've refined it down by four different filters before it got to that content" | `extractions/Tom Noske/transcript.txt` | grep-matched exact |
| "the only reason a company is paying you $10,000 for a post is because they're making $100,000 off your hard-earned traffic" | `extractions/Tom Noske/transcript.txt` | grep-matched exact |
| "tell your origin story with 100% accuracy, what content would you make?" | `extractions/Tom Noske/transcript.txt` | grep-matched exact |
| "45 million views that thought it was funny, not thought you were interesting or thought you were valuable or thought you have something that you could sell them" | `extractions/Tom Noske/transcript.txt` | grep-matched exact |
| "every day is another sales pitch and eventually it just becomes white noise" | `extractions/Tom Noske/transcript.txt` | grep-matched exact |
| "There's no science. There's no math equation. I can't look at your views and go, you need to do this, this, and this" | `extractions/Tom Noske/transcript.txt` | grep-matched exact |
| Dates used in anchors: 2026-03-06 (Module A / "Five Unspoken Content Rules") | `extractions/tom-noske/extraction-report-content-creation.md`, `extractions/tom-noske/transcript.txt` | filesystem mtime of both files (`ls -la`) — used as the extraction-capture date, not a claimed video-publish date |
| Dates used in anchors: 2026-05-30 (Module B / "the two lies in the creator space") | `skills/tom-noske-content-creation/SKILL.md` line 26 ("Added 2026-05-30 from 'The two lies in the creator space.'") + `extractions/Tom Noske/transcript.txt` mtime | cross-checked against both the skill's own module note and the file's mtime |
| "Recognition test" language (Model Calibration section) | Original composition, this repair pass | Not a source quote — new craft-standard-required section; grounded in genius.md's own existing patterns (GP-6 De-Shielding, GP-1 zero-preparation) rather than invented texture |

No claim in this repair pass relies on a quote that could not be grep-matched verbatim. Where genius.md's Hall of Fame exemplars label themselves "Verbatim Reconstruction" / "Reconstructed from Source" (pre-existing content, not touched this pass), that self-labeling is preserved as-is and flagged again in `references/source-ledger.md` for transparency — these are analyst composites, not literal transcript lines.
