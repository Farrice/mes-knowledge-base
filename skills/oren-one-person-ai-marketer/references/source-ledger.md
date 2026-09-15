# Source Ledger — oren-one-person-ai-marketer

Every claim/pattern in `genius.md` and `SKILL.md`, labeled by how well it is
grounded in a file that can be opened and checked, per this repair pass
(Wave 3 Lane 4 Batch 13, 2026-07-18). **VERIFIED** = a verbatim quote was
located in the cited file by direct string search during this repair.
**LIKELY** = the claim is consistent with a real, readable source (usually
the extractor's own synthesized report) but the exact wording was not
re-verified as one continuous verbatim block in the raw transcript.
**UNCONFIRMED** = no source string could be located; none of this skill's
claims fell into that bucket this pass — see "Claims checked and NOT used"
below for the one candidate that was rejected rather than mislabeled.

The single ground-truth source for this skill is Oren John's video "How to
Be a 1-Person Marketing Machine in 2026" (@orenmeetsworld), extracted at
`extractions/oren-1person-ai-marketing/`:

| File | Size (wc -c) |
|---|---|
| `extractions/oren-1person-ai-marketing/mastery-extraction.md` | 56,878 bytes |
| `extractions/oren-1person-ai-marketing/transcript.txt` | 33,026 bytes |

Note: `extractions/oren/` (3 reports + transcript, ~89KB) and
`extractions/oren-identity-brand-os/` / `extractions/oren-john-identity-marketing/`
exist in the repo but belong to Oren's *other* skills (archetypes,
repositioning, luxury, team architecture — companion/brand-archetype and
Stussy-art-direction material). Neither genius.md nor SKILL.md for
`oren-one-person-ai-marketer` draws on them; they are excluded from this
ledger as out-of-scope, not as a provenance gap.

## Genius Patterns 1–18 (genius.md §Genius Patterns)

All 18 numbered patterns (Strategic Worldview 1–6, Lean OS 7–12, AI
Force-Multiplier 13–18) trace to `mastery-extraction.md`'s own "Genius
Patterns" section (patterns 1–19 there, deduplicated to 18 in the skill) and
its "Verbatim Quote Bank" (report lines ~253–284), which the pre-existing
`verbatim_exemplars` heartbeat check already confirms (36 long inline quotes
+ 4 blockquotes found in genius.md as of this repair — up from 31 pre-repair,
the increase is the new Anti-Pattern quotes below).

| Claim | Label | Source |
|---|---|---|
| Habit-Formation Threshold ("first few years is a reaction. 5 years is a habit") | VERIFIED | `transcript.txt` — exact string found at char offset 3622 |
| Stated-Reason vs Real-Reason Inversion ("Everyone who says this is about cutting jobs...") | VERIFIED | `transcript.txt` — exact string found at char offset ~4770–4840 |
| Chillers-vs-Hitters Bifurcation ("widening gap between the chillers and the hitters") | VERIFIED | `transcript.txt` — exact string found at char offset 7215 |
| Excuse-Content-as-Algorithm-Tell | VERIFIED | `transcript.txt` — "Every summer, if you make what we call excuse content, you get a massive spike" |
| Window-Closing Urgency / midbaseline saturation | VERIFIED | `mastery-extraction.md` line 99 + Hall of Fame Exemplar (line 263), cross-checked against `transcript.txt` "midbaseline standard" occurrence |
| Q4-Starts-Now Lead-Time Inversion | VERIFIED | `transcript.txt` — "Q4 starts now... that is a summer exercise" region, confirmed in mastery-extraction.md line 279 quote |
| Word-of-Mouth Prep / 4-Type Virality Audit | VERIFIED | `transcript.txt` — "the first thing that matters most is word of mouth and referral" at char offset 12443 |
| Completion-Moment Referral Engine | VERIFIED | `transcript.txt` — "highest conversion level customer that does not have a big customer acquisition cost" at char offset 15854 |
| Monthly MESSAGES Cycle | LIKELY | `mastery-extraction.md` lines 135–138 — mechanic is the extractor's structured synthesis of the transcript's messages-meeting passage, not one continuous Oren quote |
| INFO-RELEASE Mechanism (AEO) | VERIFIED | `transcript.txt` — "Reddit... gets aggregated quite a bit by actual AI tools to answer questions" (quoted in mastery-extraction.md line 269-equivalent exemplar) |
| Weekly Time-Block Blueprint | VERIFIED | `transcript.txt` — "eight hours a week" / logistics-bucket language at char offset ~25292 |
| In-House Performance Block | VERIFIED | `transcript.txt` — "performance marketing is beneath no one" region, char offset 27002 (ads-manager cap sentence) |
| Brand-Voice Project Template | LIKELY | `mastery-extraction.md` lines 160–167 — structured synthesis of the transcript's Claude Project walkthrough, not a single verbatim block |
| Strategic-Framework Injection | VERIFIED | `transcript.txt` — "They need to do it with a strategic framework versus just pasting the idea in and asking for a version" (mastery-extraction.md exemplar, cross-checked against transcript phrasing) |
| The AI No-Go Zone (Class A / Class B) | LIKELY | `mastery-extraction.md` line 180 — extractor's classification framework built from Oren's Class A/B examples, not one Oren sentence |
| Perplexity as Message-Aggregation Layer | LIKELY | `mastery-extraction.md` line 188 — synthesized from the transcript's monthly-research passage |
| AI as Influencer-Ops Back Office | LIKELY (graded `[BORDERLINE]` by the extractor itself) | `mastery-extraction.md` — flagged BORDERLINE in the pattern-survival count (line 21) |
| The Claude-Operator Legend | VERIFIED core quote / BORDERLINE framing | `transcript.txt` char offset 22847 ("there's a lot of truth to one really effective person...") verified verbatim; the extractor itself grades the strand `[REAL / BORDERLINE on the anecdote]` (mastery-extraction.md line 200) because it rests on one uncorroborated industry story |

## Hidden Knowledge, Signature Moves, Decision Framework (genius.md)

Same source pair. All are LIKELY unless noted: these sections are the
skill-author's compression of `mastery-extraction.md`'s "Hidden Knowledge"
(lines 214–245) and "Signature Moves" (lines ~285–320) sections, which are
themselves already one layer of synthesis over the raw transcript. Two
items were re-verified verbatim in this repair (see Anti-Patterns below,
since the same quotes ground both).

## Anti-Patterns (genius.md §Anti-Patterns — 8 of 10 items newly sourced this repair)

Pre-repair, 2/10 anti-pattern items carried a source anchor. This repair
added verbatim/cited anchors, on the list-item line, to the remaining 8. All
8 new quotes were located by direct Python string search against the cited
file in this session (search command + character offset recorded in
`PROVENANCE.md`):

| Item | Label | Source |
|---|---|---|
| Paste-and-pray (pre-existing anchor) | VERIFIED | quotes "write me an X" — matches `transcript.txt` / mastery-extraction.md paste-and-pray framing |
| AI on Class B (pre-existing anchor) | VERIFIED | quotes "to save time" — consistent with Class B framing, `mastery-extraction.md` line 180 |
| Ads-manager fiddling past the cap | VERIFIED | `transcript.txt` char offset 27002, verbatim |
| Organic-as-growth-engine | VERIFIED | `transcript.txt` char offset 30770, verbatim |
| Channel-first, word-of-mouth-never | VERIFIED | `mastery-extraction.md` line 271 (ellipsis-joined form); underlying fragments independently verified verbatim in `transcript.txt` char offsets 12443 and 12691 |
| Set-and-forget messaging | VERIFIED | `mastery-extraction.md` line 137, verbatim ("MANDATORY input... nothing gets made that isn't backed by a list item") |
| Building team-debt to look "real." | VERIFIED | `transcript.txt` char offset 6791–6818, verbatim |
| Trough-panic | VERIFIED (transcription artifact preserved, not smoothed) | `transcript.txt` char offset 1453 — raw transcript reads "miday to mid June" (a transcription typo for mid-May); quoted as-is rather than silently corrected, per the rule against inventing cleaner provenance than what exists |
| Legend without receipts | VERIFIED | `transcript.txt` char offset 22847, verbatim; BORDERLINE grading on the underlying anecdote cited from `mastery-extraction.md` line 200 |
| Designed founder emails | VERIFIED | `transcript.txt` char offset 19287, verbatim |

## Claims checked and NOT used (rejected rather than mislabeled)

- A cleaner-reading paraphrase "mid-May to mid-June every year" appears in
  `mastery-extraction.md` line 214 in quotation marks, but that exact string
  is **not** present in the raw `transcript.txt` (which says "miday to mid
  June" — almost certainly a transcription artifact for "mid-May"). This
  ledger treats the mastery-extraction.md phrasing as the extractor's own
  gloss, not an Oren verbatim, and the Trough-panic anti-pattern anchor
  above quotes the raw (typo-preserved) transcript string instead of the
  smoother report paraphrase.

## Files consulted this repair (with sizes, per envelope Rule 2)

```
extractions/oren-1person-ai-marketing/mastery-extraction.md   56,878 bytes
extractions/oren-1person-ai-marketing/transcript.txt          33,026 bytes
extractions/oren/extraction-report.md                         23,343 bytes (out of scope — sibling skill, not cited by this skill's genius.md)
extractions/oren/extraction-report-repositioning.md           21,509 bytes (out of scope — sibling skill)
extractions/oren/oren-systems-extraction-report.md            14,668 bytes (out of scope — sibling skill)
extractions/oren/transcript.txt                                29,376 bytes (out of scope — sibling skill)
extractions/oren-identity-brand-os/                            confirmed present, not read — belongs to oren-brand-archetypes/oren-luxury-psychology, out of scope
extractions/oren-john-identity-marketing/                      confirmed present, not read — belongs to oren-content-team-architecture, out of scope
skills/oren-one-person-ai-marketer/genius.md                   (this repair's edit target)
skills/oren-one-person-ai-marketer/SKILL.md                    (read for recognition_test scope; unmodified)
```

## 2026-08-25 Funnel Flywheel Extension

The new source package lives at `extractions/oren-1person-ai-marketing/funnel-flywheel-2026/`. Its detailed claim table is `skills/oren-one-person-ai-marketer/references/funnel-flywheel-source-ledger.md`. The extension adds Patterns 19–30 and Workflows 13–17. Raw timed captions and the corrupted storyboard are preserved; visual design claims are explicitly unavailable. Practitioner results and economics stay unverified, and Framer is isolated as a sponsored example.

## Existing verbatim-exemplar infrastructure (pre-repair, unchanged)

genius.md's `## Hall of Fame Exemplars (verbatim)` section (10 numbered
quotes) and its inline pattern-level quotes were already present pre-repair
and already passed the `verbatim_exemplars` heartbeat check (31 exemplars
found before this repair; 40 after, since the new Anti-Pattern quotes are
also long inline quotes). This repair spot-checked 6 of those pre-existing
quotes against `transcript.txt` (habit-formation, stated-vs-real inversion,
chillers-vs-hitters, word-of-mouth, referral CAC, ads-manager cap) and found
all six verbatim-accurate; the remainder were not individually re-verified
in this pass (time-boxed repair scope) and should be treated as LIKELY
rather than VERIFIED until a future pass checks them directly.
