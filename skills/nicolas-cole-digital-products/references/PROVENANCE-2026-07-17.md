# PROVENANCE — nicolas-cole-digital-products repair

Anchor → source file + location. All quotes verified with `grep -F` against
the cited file (exact-substring match, including transcription stutters
preserved verbatim where quoted). Full claim-by-claim table for every
pre-existing pattern is in `references/source-ledger.md`; this file covers
only the NEW text added by this repair (genius.md "How to Use This Skill"
rewrite, entity-floor fixes, and the new Anti-Patterns section).

Source files:
- **DP** = `extractions/nicolas-cole-digital-products/transcript.txt` (39,852 chars, single continuous line, no timestamps) + `extractions/nicolas-cole-digital-products/extraction-report.md`
- **GEN** = `extractions/nicolas-cole/transcript.txt` (18,152 chars, single continuous line, no timestamps) — separate Cole session on offer stacking

| Anchor (as it appears in genius.md) | Source | Verified |
|---|---|---|
| "I'm going to be blunt on purpose" | DP | grep -F match |
| "it's so unbelievably simple that it's complicated" | DP | grep -F match |
| "30 full-time team members" | DP | grep -F match |
| "22-23 cohorts tested" (paraphrase, not quoted) | DP | "22 23 cohorts" present; genius.md text left unquoted per fix |
| "$400,000 a year" | DP | grep -F match |
| Pattern 5 — "Creating the low ticket digital product is really the forcing function for you to crystallize all of your thinking... Once that thing is created, you can double monetize it by going and now I'm going to create the opportunity to teach it live" | DP | grep -F match, both fragments |
| HK #5 — "and we also give you AI prompts and we also give you these templates" | DP | grep -F match |
| HK #5 — "you can absolutely use that um as just like a standalone product" | DP | grep -F match |
| HK #6 — "when you just give more for the sake of more, it actually has the inverse effect" | GEN | grep -F match |
| HK #6 — "my health and wellness cheat sheet... my coffee picks for the year... my favorite dog training routines" | GEN | grep -F match |
| HK #6 — "Does Does that make the offer more compelling? No, not at all" | GEN | grep -F match (transcript stutter "Does Does" preserved) |
| HK #8 — "aim for somewhere like three to seven questions... You don't need to answer a 100 questions. You don't need a 100 assets" | GEN | grep -F match |
| HK #8 — Gary Halbert / "slippery slope" | GEN | "one of my favorite sales copywriters ever is uh Gary Halbert... he used to call it the slippery slope" — grep -F match |
| Anti-Pattern 1 (jump to recurring) | DP | grep -F match |
| Anti-Pattern 2 (price at bottom of range) | DP | grep -F match |
| Anti-Pattern 3 (price point mismatched to vehicle) | DP | grep -F match, two fragments |
| Anti-Pattern 4 (jump to community) | DP | grep -F match, two fragments |
| Anti-Pattern 5 (word/video count fixation) | DP | grep -F match (transcript stutter "number of of videos" preserved, quote truncated before the stutter to stay clean) |
| Anti-Pattern 6 (incongruent bonus padding) | GEN | grep -F match, three fragments |
| Anti-Pattern 7 (interchangeable vehicle terms) | DP | grep -F match, two fragments |

## Flagged as UNCONFIRMED (not given a false anchor)

- **Pattern 9 — Buyer Broadcast Architecture** (Artifact Design / Vocabulary
  Injection / Visible Transformation Marker): searched DP, GEN,
  `nicolas-cole-ghostwriting-v1/transcript.txt`,
  `nicolas-cole-ghostwriting-v2/transcript.txt`, and
  `nicolas-cole-client-acquisition/extraction-report.md` for "broadcast,"
  "screenshot," "vocabulary," "artifact" — zero matches in all five files.
  Left in place (additive-first boundary; not a failing check on its own)
  but labeled UNCONFIRMED in `references/source-ledger.md` rather than
  silently anchored. Signature Move 6 ("Broadcast Audit") and one Quality
  Rubric row inherit the same UNCONFIRMED status since they restate this
  pattern.
- **Pattern 10 — the specific "2x+" / "$1,200+" unbundling figures**: the
  unbundling mechanic itself is VERIFIED (GEN — "$350 and you're getting
  four products"), but no "2x" multiplier or "$1,200" figure appears
  anywhere in either transcript. Labeled LIKELY (concept confirmed, number
  is an illustrative elaboration) rather than VERIFIED.
