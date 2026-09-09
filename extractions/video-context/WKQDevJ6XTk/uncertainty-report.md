# Uncertainty Report

## Verified in this package

- The video identity, title, channel, duration, publication date, chapters, and public availability come from YouTube metadata acquired on 2026-08-28.
- The spoken source is preserved as English auto-captions in `transcript.vtt`, a 9,738-word cleaned reading transcript, and timestamped caption segments.

## Evidence limits

- Full media download failed at YouTube's PO-token layer. No frame or OCR evidence is available, so this package must not support claims about demonstrations, on-screen text, editing, body language, or visual teaching mechanics.
- Auto-captions can mis-transcribe names, punctuation, and speaker turns. Treat exact wording as transcript evidence, not an independently authenticated quotation.
- The opening claim about book sales and Amazon review counts is host-stated and time-sensitive; it is not independently verified here.
- Statements about Matt Haig's process, career, and preferences are interview testimony. Label them `SELF-REPORTED` when the distinction matters.
- The plain transcript returned by `youtube-transcript-api` is the clean reading surface. The timestamped VTT and ledger preserve source location but contain rolling-caption overlap; use them to locate evidence, not for word-count claims.

## Permitted conclusion

The source is sufficient for a transcript-grounded extraction of Matt Haig's writing, editing, reader-accessibility, emotional-storytelling, and taste-protection mechanics. It is insufficient for a visual-production extraction or independent proof that the mechanics caused commercial outcomes.
