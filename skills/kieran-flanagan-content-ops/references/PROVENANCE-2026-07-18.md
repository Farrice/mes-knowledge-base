# PROVENANCE — kieran-flanagan-content-ops repair

Anchor → source file+location. Full claim table lives in `references/source-ledger.md`;
this file lists only the new Anti-Patterns section anchors (the check the fix targets).

| Anti-Pattern item | Quote | Source file | Location |
|---|---|---|---|
| Cut-and-paste shipping | "too many people will use these cut and paste. That's not how you do that, right?" | `extractions/kieran-flanagan/transcript.txt` | Post-enricher demo segment, ~2/3 through transcript |
| Enrich-idea-not-draft | "trying to enrich just a idea is kind of hard" | `extractions/kieran-flanagan/transcript.txt` | Post-enricher demo segment |
| Ship-first-draft-hook | "obviously I would never ship this" | `extractions/kieran-flanagan/transcript.txt` | "zero employees" LinkedIn draft walkthrough |
| Vibe-marketing rejection | "I was never a big fan of the kind of vibe marketing where it was workflow tools because it's not vibing... This is not software." | `extractions/kieran-flanagan/transcript.txt` | Onboarding/audience-profile segment, referencing the "James / born marketer" prior episode |
| Stop-before-feedback-loop | "If you're a system thinker, most people stop here." | `extractions/kieran-flanagan/transcript.txt` | Immediately before the feedback-loop app description |
| Demographic-persona rejection | "Traditional personas are built from demographics and surveys — they're fiction." | `extractions/kieran-flanagan/extraction-report.md` | Hidden Knowledge, bullet 1 |
| Draft+cite-in-one-pass rejection | "Asking AI to 'write a LinkedIn post with 3 statistics and a case study' produces hallucinated data." | `extractions/kieran-flanagan/extraction-report.md` | Hidden Knowledge, bullet 3 |

Verification method: full read of `extractions/kieran-flanagan/transcript.txt` (27,523
bytes) and `extractions/kieran-flanagan/extraction-report.md` (14,945 bytes) top to
bottom — every quote above was located by direct string match, not inferred. No quote in
this skill's new Anti-Patterns section is invented; two items (Hidden Knowledge bullets)
are labeled LIKELY rather than VERIFIED because they are the extraction author's
synthesis, not Kieran's literal on-camera words — see `references/source-ledger.md` for
the full reasoning.

Files NOT used for this skill's provenance (checked and explicitly excluded, not
silently skipped): `extractions/kieran-flanagan-second-brain/*` — a separate, later
extraction whose material was routed to `simon-intellectual-library-os` and
`liam-mley-ai-brain-builder` per its own "Where it landed" section, not to content-ops.
