# Uncertainty Report - Really Real Writing

## Source Certainty
- Confirmed locally: video metadata, auto-caption file, parsed segments, clean transcript, timestamped anchors.
- Source type: public YouTube video with auto-generated captions.
- Confidence in broad mechanics: high.
- Confidence in exact wording: medium, because captions are automatic and contain overlap.

## Limits
- This package is not a complete extraction of the book `Good Writing: 36 Ways to Improve Your Sentences`.
- It is an extraction of the video conversation at `sfK6XVV0M74`.
- Some workflow names, such as `/really-real-silence` and `/really-real-oh-no`, are system adaptations of source mechanics rather than named source chapters.
- Domain adapters for social, marketing, and client work are transfer applications. They should stay faithful to the mechanics without claiming the source directly discussed every domain.

## Use Rules
- Prefer paraphrase in user-facing outputs.
- Use only brief source excerpts when evidence is needed.
- If exact quotation matters, recheck against the original video audio.
- If factual claims about the authors, book, channel, or publication context are needed in public copy, verify live before publishing.

## Completion Criteria
The package can be called complete when:
- The source folder contains metadata, ledger, mechanics, analysis, uncertainty, raw captions, and parsed transcript.
- The skill validates with `execution/validate_skill.py`.
- Public commands are discoverable in `SLASH_COMMANDS.md`.
- The behavior proof lab includes social, marketing, client, personal, and fiction/book cases.
- The package is integrated as an optional depth layer, not a universal writing default.
