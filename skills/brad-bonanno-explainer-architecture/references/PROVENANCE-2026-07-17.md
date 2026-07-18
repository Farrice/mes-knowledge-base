# PROVENANCE — brad-bonanno-explainer-architecture repair

Every anchor added to `genius.md` this repair, with exact source file + location. All quotes below were checked verbatim against the source file during this repair (not reconstructed from memory).

| Anchor added in genius.md | Source file + location | Verbatim? |
|---|---|---|
| "How to Use This Skill" — *"And I can literally hear the keyboards clattering right now, Brad, this is going to torture your token budget. This actually surprised me, so let's do the math."* (t=05:01) | `extractions/brad-bonanno/extraction-report.md`, Pattern 5, "Verbal evidence (transcript t=05:01)" | Verbatim — exact quote already present in source file |
| "How to Use This Skill" — *"Sam is still introducing what he's going to talk about today and Claude has already ingested the entire thing."* | `extractions/brad-bonanno/extraction-report.md`, Exemplar A | Verbatim |
| "How to Use This Skill" — Brad's on-camera texture description ("confident-but-friendly explainer, mid-30s, soft-lit gray-wall vlog setup, animated hand gestures, leans-into-camera energy") | `extractions/brad-bonanno/extraction-report.md`, Source Identity section (opening paragraph) | Verbatim (lightly re-punctuated to fit prose, no words changed) |
| Anti-Patterns item 1 — *"Rotating examples to 'show breadth' — amateur creative cowardice disguised as helpfulness."* | `extractions/brad-bonanno/extraction-report.md` does not carry this exact sentence; it is the pre-existing `genius.md` line 47 ("Anti-pattern" callout under Pattern 2), which itself paraphrases extraction-report.md Pattern 2 + Signature Move SM2 ("Resist the urge to 'show breadth' — that's amateur creative cowardice disguised as helpfulness") | Verbatim against `genius.md`'s own pre-existing SM2 text |
| Anti-Patterns item 2 — *"A 10-minute screen-recording of someone walking through a UI. High effort, low retention, low branding leverage, and the viewer remembers nothing because every frame looks the same."* | `extractions/brad-bonanno/extraction-report.md`, Pattern 1, "Anti-exemplar" line | Verbatim |
| Anti-Patterns item 3 — *"Saying 'it's cheap' without any visual anchor. Or worse — flashing a number on screen for 0.8 seconds in a non-branded format. The viewer doesn't internalize transient visuals."* | `extractions/brad-bonanno/extraction-report.md`, Pattern 4, "Anti-exemplar" line | Verbatim |
| Anti-Patterns item 4 — *"If Brad had recorded the same script as a podcast (audio-only) or as a Loom screen-recording with no PIP, the video would have 30-50% lower retention."* | `extractions/brad-bonanno/extraction-report.md`, Hall of Fame "Anti-Exemplar" section | Verbatim |
| Anti-Patterns item 5 — creators who "make their face huge during demos... signals 'watch me,' which competes with the demo content" | `extractions/brad-bonanno/extraction-report.md`, HK2 | Verbatim (quoted fragments) |
| Anti-Patterns item 5 — frame references 11, 23, 60, 78 for consistent bottom-left PIP | `extractions/brad-bonanno/extraction-report.md`, HK2 ("frame 60, frame 78") + Exemplar A (frames 11, 23) | Verbatim frame numbers, combined from two source paragraphs |
| Anti-Patterns item 6 — *"Indie creators who hand-wave on cost ('it's pretty cheap') signal lack of confidence in their own measurements."* | `extractions/brad-bonanno/extraction-report.md`, HK3 | Verbatim |
| HK6 grounding quote — *"bald, black quarter-zip, raised hand mid-gesture, mouth open in pattern-interrupt energy"* | `extractions/brad-bonanno/extraction-report.md`, HK6 (describing Frame 1) | Verbatim |
| SM3 grounding — "frames 60 and 78... 'clean rounded card'" | `extractions/brad-bonanno/extraction-report.md`, HK2 | Verbatim phrase "clean rounded card"; frame numbers verbatim |
| SM5 grounding quote — *"the setup takes care of the rest"* (t=02:38) | `extractions/brad-bonanno/extraction-report.md`, Pattern 7, "Verbal evidence (t=02:38)" | Verbatim |
| Quality Rubric intro — "(35 points total; pass threshold 25/35)" | `extractions/brad-bonanno/extraction-report.md`, Quality Rubric closing line ("Pass threshold: 25/35 (avg 3.6 across 7 criteria)") + genius.md's own pre-existing rubric (7 criteria × 5 = 35, arithmetic, not a new claim) | Verbatim pass-threshold figure; the "35 total" is arithmetic on the pre-existing 7-criteria/1-5-scale structure, not a new sourced fact |
| Pause Test criterion grounding — "no dead pause point across the source video's 80 sampled frames" | `extractions/brad-bonanno/extraction-report.md`, HK4 ("There is no DEAD pause point in this video") + extraction header ("80 frames") | Verbatim claim + verbatim frame count |
| Single-Source criterion grounding — "frames 11, 14, and 23" | `extractions/brad-bonanno/extraction-report.md`, Pattern 2 "Visual evidence" ("Frames 11, 14, 23 all show the same YouTube video") | Verbatim |
| Pre-empted Objections criterion grounding — *"Brad, this is going to torture your token budget"* (t=05:01), frame 49 | `extractions/brad-bonanno/extraction-report.md`, Pattern 5 | Verbatim |
| Trust-Anchor criterion grounding — "frames 44, 49, and 60... $0.70/$0.82/$0.95/$1.62" | `extractions/brad-bonanno/extraction-report.md`, Pattern 4 "Visual evidence" | Verbatim |
| Recognition-test sentence ("would Brad Bonanno recognize this as someone architecting...") | Authored this repair pass — not a source quote. Modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per ENVELOPE.md instruction, content is specific to Brad's own patterns (Pause Test, modality mix) as documented above | N/A — original craft language, not attributed to Brad as a quote |
| Source Ledger claim table | Compiled this repair from direct reads of `extraction-report.md` + `ls`/`find`/`wc -c` on `extractions/brad-bonanno/` | See `references/source-ledger.md` |

## File-size verification (run this repair, raw output)

```
extractions/brad-bonanno/extraction-report.md   — 24368 bytes
extractions/brad-bonanno/visual-context.md      — 32493 bytes
extractions/brad-bonanno/download/video.en.vtt      — 96742 bytes
extractions/brad-bonanno/download/video.en-orig.vtt — 96742 bytes
extractions/brad-bonanno/download/video.mp4     — 16499020 bytes
extractions/brad-bonanno/frames/                — 80 .jpg files, 4094-24852 bytes each
extractions/brad-bonanno/transcript.txt         — DOES NOT EXIST (confirmed via ls; genius.md's
                                                    pre-existing Source Material line is a broken
                                                    pointer, out of this repair's scope)
```

No claim of "source absent" was made anywhere in this repair without the corresponding file read above.
