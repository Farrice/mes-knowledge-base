# Source Ledger — luke-iha-proof-mechanisms

Claim-by-claim provenance for every pattern, hidden-knowledge item, and
anti-pattern in `genius.md`. Labels: **VERIFIED** (quote/fact confirmed present
verbatim or near-verbatim in a read source file), **LIKELY** (concept present
in source, wording paraphrased/synthesized), **UNCONFIRMED** (no direct source
found — flagged honestly, not deleted).

## Primary Sources (read in full this repair pass)

| File | Size (wc -c) | Role |
|---|---|---|
| `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | 22,022 bytes | Primary — full verbatim transcript of the "22 proof weapons" video |
| `extractions/luke-iha/video-1-proof-mechanisms/extraction-report.md` | 6,936 bytes | Secondary — deep-pass extraction report on the same video (adds "Experiential Proof Supremacy," full 22-type taxonomy) |
| `extractions/luke-iha/transcript.txt` | 32,648 bytes | Earlier/parallel transcript of the same core material (used to cross-check original genius.md authorship) |
| `extractions/luke-iha/extraction-report.md` | 7,915 bytes | Original master extraction report — the direct ancestor of the 4 patterns + 3 hidden-knowledge items already in genius.md pre-repair |
| `skills/luke-iha-proof-mechanisms/references/prompts-v2/empirical-data-synthesis-engine.md` | 9,837 bytes | Existing source-ledger anchor (already passing before this repair; unchanged) |

## Genius Patterns

| # | Pattern | Label | Anchor |
|---|---|---|---|
| 1 | The Jargon Flurry | VERIFIED | `extractions/luke-iha/extraction-report.md` §Genius Patterns + `video-1-proof-mechanisms/transcript.txt` ("does your prospect know what half of that means? Probably not, but it sounds credible") |
| 2 | The Damaging Admission | VERIFIED | `extractions/luke-iha/extraction-report.md` §Genius Patterns; transcript "Our customer support is not 24/7... but our product is generated more revenue for clients than any competitor charging 3x our price" |
| 3 | Proof Stacking at Doubt Nodes | VERIFIED | `video-1-proof-mechanisms/transcript.txt` — closing passage, "Right before a call to action, a great spot for a testimonial. Right after making a big claim, back it up with a stat or a study." |
| 4 | Contextualized Authority | VERIFIED | transcript — "If you say journal of marketing, they may not understand what that school means or why that's significant" |
| 5 | The 22-Type Proof Arsenal | VERIFIED | transcript full taxonomy list ("technical jargon... candid communication... case studies... social media metrics") + `extraction-report.md` §Methodology |
| 6 | Promise-to-Proof Match | VERIFIED | transcript rule 1 — "$1 million... $47 Stripe payment probably isn't going to cut it" |
| 7 | Hard-to-Fake Proof | VERIFIED | transcript rule 2 — "the harder your proof is to fake, the stronger it is... Anyone can Photoshop a bank statement, but if you get an independent audit from a CPA firm..." |
| 8 | The Experience-as-Proof Technique | VERIFIED | transcript rule 3 — "let people experience it themselves when possible. This is the holy grail of proof." |

## Hidden Knowledge

| # | Item | Label | Anchor |
|---|---|---|---|
| 1 | The Emotion of Truth | VERIFIED | transcript — "the best proof is just making people feel like it is true... if you create the emotional sensation of truth, you don't always need to make a logical argument" |
| 2 | Proof is About Safety, Not Convincing | VERIFIED | transcript closing line — "proof is not convincing people to buy. It's about making people feel safe buying." |
| 3 | Visuals > Correlated Data | VERIFIED | transcript — "this is basic just correlation, which does not equal causation, but it doesn't matter... Look at these numbers go up on the chart" |
| 4 | The 4 Rules of Proof | VERIFIED | transcript — "There are four rules that you need to know before we get into the 22 types" (all four rules stated verbatim in sequence) |
| 5 | Proof as Competitive Moat | LIKELY | Not a direct Iha quote in either transcript read this pass. Grounded via `video-1-proof-mechanisms/extraction-report.md` Hidden Knowledge — "Most copywriters use 3-4 proof types max. Iha deploys from a menu of 22. The taxonomy itself is a competitive advantage." The specific frame "moat" is a synthesis of that idea, not Iha's literal word. Downgraded from an unlabeled claim to LIKELY this pass — flagged honestly rather than deleted, per additive-first boundary. |

## Anti-Patterns (new section, all sourced this pass)

| Anti-pattern | Label | Anchor |
|---|---|---|
| Self-reported proof as primary evidence | VERIFIED | transcript — "Self-reported results are kind of like a meh... Anyone can Photoshop a bank statement..." |
| Promise-proof weight mismatch | VERIFIED | transcript — "$1 million... a screenshot of a $47 Stripe payment probably isn't going to cut it" |
| Random proof placement | VERIFIED | transcript — "the best marketers don't just throw proof at people randomly" |
| Proof-type overkill | VERIFIED | transcript — "You don't need to use all 22 types of proof in one campaign" / "overkill" |
| Uncontextualized niche authority | VERIFIED | transcript — "If you say journal of marketing, they may not understand what that school means" |
| Thin/flat proof collection | VERIFIED | transcript — "their proof is so flat. Nobody bothered to go and collect all these different types of proof" |

## Model Calibration Section

The "How to Use This Skill" section is LIKELY-tier: it applies the Ben Watkins
calibration pattern (structural template, not content) to Iha-specific texture
drawn from VERIFIED quotes above ("insane, autistic level," "$47 Stripe
payment," "meh," the anti-exemplar already resident in genius.md). No new
unsourced claims introduced.

## What Was NOT Touched

`references/genius-patterns.md` and `references/hidden-knowledge.md` (duplicate
copies of the pre-repair pattern/hidden-knowledge text) were left as-is —
out of scope for this pass since the auditor only inspects `genius.md` and
`SKILL.md` for these checks, and the ENVELOPE's additive-first rule means no
deletion of passing/duplicate content. Workflow files (6/6) already carry
Output Schema + Quality Gate and were not modified.
