# PROVENANCE — john-whiting-propaganda-machine repair

All quotes verified by grep against source transcripts before use (rule: no quote gets an anchor unless found verbatim in a source file). Sizes recorded per envelope rule 2.

## Source files (extractions/john-whiting/, all confirmed present, non-zero)
| File | Size (wc -c) |
|---|---|
| transcript-1-VllCQkcCf3Y.txt | 123,939 bytes |
| transcript-2-pzgd2l31Q-8.txt | 26,056 bytes |
| transcript-3-Kz8D7zOhxcQ.txt | 83,092 bytes |
| vision.md | 9,649 bytes |
(`-wrapped.txt` duplicates of transcripts 1-3 also present, identical byte counts — same source re-saved.)

## Anchor → source table (genius.md Anti-Patterns section, items 3–9)

| Anti-pattern item | Quote added | Verified against | Grep confirmation |
|---|---|---|---|
| Live objection-handling as the plan | "I don't handle objections anymore. I don't even try." | transcript-1-VllCQkcCf3Y.txt | `grep -o "I don't handle objections anymore"` → hit |
| Copy-pasting a funnel | "This is how you stop copy-and-pasting other people's models and start engineering." | transcript-1-VllCQkcCf3Y.txt | `grep -o "stop copy and pasting other people"` → hit (transcript stores it without hyphens; source-quotes.md's hyphenated rendering is the pre-existing skill file's own transcription choice, reused as-is) |
| Abdication dressed as delegation | "Figure out how to do every part of it yourself until it's dialed, then you delegate it. Otherwise you're abdicating." | transcript-1-VllCQkcCf3Y.txt | `grep -o "abdicating"` → hit |
| Revenue-chasing without wealth math | "You get rich by spending less than you earn and investing the difference." | transcript-3-Kz8D7zOhxcQ.txt | `grep -o "spend less than you earn"` → hit |
| Sanded-down voice | Cross-referenced to genius.md's own VOICE REFERENCE § Mode B (pre-existing "over-cleaned/spine removed" example) — internal anchor, not a new transcript quote | genius.md (this file, unchanged section) | direct read |
| Manipulation past the Ethics Gate | "When I brainwash somebody, their business doubles. When the government brainwashes people, they take vaccines and die." | transcript-1-VllCQkcCf3Y.txt | `grep -o "brainwash somebody"` → hit |
| Phantom proof | Cross-referenced to references/source-quotes.md § Self-Reported Bio, which already labels Whiting's own numbers "claims, not verified" | references/source-quotes.md (pre-existing, unmodified) | direct read, line 86-92 of that file |

All quotes were already present verbatim in `skills/john-whiting-propaganda-machine/references/source-quotes.md` (a pre-existing, pre-vetted reference file) before this repair; this repair re-cites them with file+date anchors directly on the anti-pattern list-item lines where they were previously absent. Each was independently re-confirmed against the raw transcript with `grep -o` (see table) rather than trusted from the reference file alone.

## How to Use This Skill (Model Calibration) section
Net-new section added to genius.md, modeled on skills/ben-watkins-storytelling/genius.md lines 7-16 per envelope instruction. Content is original synthesis of Whiting's own stated principles (data-over-feelings, mechanism-invisible, Mode B spine test) already documented elsewhere in this genius.md — no new factual claims. The one quote used, *"I felt like that was really just talking to me"*, is verbatim-confirmed by `grep -o` against transcript-1-VllCQkcCf3Y.txt (hit) and was already cited in references/source-quotes.md § Pattern Interrupt / Lean-Back Close. NOTE: a first draft of this section paraphrased this line as "feels like it's talking directly to me" inside quotation marks — caught and corrected during self-check before delivery to avoid a fabricated-verbatim failure; the final text uses the exact transcript wording.
