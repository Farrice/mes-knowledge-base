# Source Ledger — andy-lo-premium-websites

Claim-by-claim provenance for the skill's expert-attribution claims. Ground
truth for this skill is a single secondary extraction; no primary transcript
sits in this repo, so verbatim quotes are checked against
`extractions/andy-lo/extraction-report.md` (the only source file that exists
for this expert — confirmed by `ls extractions/ | grep -i andy` and a direct
read; file size 19,714 bytes, `wc -c`). Original YouTube video source was
NOT independently re-fetched by this repair pass — everything traces to the
extraction report, one hop from the primary source.

## Primary Source

| Source | Size (wc -c) | Status |
|---|---|---|
| `extractions/andy-lo/extraction-report.md` | 19,714 bytes | VERIFIED present, read in full |
| Underlying YouTube videos (3, 6,375 words per extraction-report.md header) | n/a | LIKELY — the extraction claims 3 videos/6,375 words; this repair pass did not re-fetch the raw videos to independently confirm word count or that all 3 videos exist as described |

## Claim-by-Claim (12 Genius Patterns + 8 Hidden Knowledge)

All 12 Genius Patterns and 8 Hidden Knowledge items in `genius.md` are
**VERIFIED** as faithful (near-verbatim) condensations of
`extractions/andy-lo/extraction-report.md` §Genius Patterns (lines 22-94) and
§Hidden Knowledge (lines 96-120) respectively — line-by-line diff confirms no
pattern/insight was added that isn't in the source.

New anchors added to `genius.md` in this repair pass (verbatim substrings
confirmed present in the source via `grep -n` before use):

| Anchor added to genius.md | Verified in extraction-report.md at | Status |
|---|---|---|
| `"first frame"` / `"last frame"` (Pattern 2) | line 31 | VERIFIED verbatim |
| `"Frames to Video"` (Pattern 3) | line 139 | VERIFIED verbatim |
| `"$5K-$15K per site"` (Patterns 5, 11; Hidden Knowledge 5) | line 185 | VERIFIED verbatim |
| `11 sequential steps` / Level 3 Option B step count (Patterns 6, 10) | lines 159-171 (steps 1-11 counted directly) | VERIFIED by direct count |
| `"just drag and drop"` (Pattern 7) | line 114 | VERIFIED verbatim |
| `"24-Hour Quickstart"` (Pattern 9) | line 209 | VERIFIED verbatim (section heading) |
| `"$20K"` (Pattern 12) | line 197 | VERIFIED verbatim |
| `6,375-word, 3-video` (Hidden Knowledge 1) | line 6 | VERIFIED verbatim |
| `"nice to have"` (Hidden Knowledge 7) | line 117 | VERIFIED verbatim — this quote existed in the source but had been dropped from genius.md's condensed paraphrase; restored here |
| `"connect to content generation agents for CMS publishing"` (Hidden Knowledge 8) | line 224 | VERIFIED verbatim |
| Anti-Patterns section, all 6 items | Genius Patterns 2/3/4/7/11 + Hidden Knowledge #2 (see per-item citations in genius.md) | VERIFIED — each is a direct logical inversion of a documented pattern, not an invented Andy Lo quote; framed in genius.md as skill-authored guidance, not attributed to Andy's own words |

## Flagged Gap — Hall of Fame Exemplars (NOT touched, honesty flag only)

`genius.md` § "Hall of Fame Exemplars" contains three illustrative
case studies — "Aura Smart Lamp," "Apex Adventures," and the anti-exemplar
"Generic AI Build Co." — that do **NOT** appear anywhere in
`extractions/andy-lo/extraction-report.md`. Git blame traces them to the
2026-03-20 "Savant-level genius.md enrichment — 148 skills upgraded" commit,
not the original extraction.

**Label: UNCONFIRMED / illustrative composites.** These are not real Andy Lo
client projects — they read as synthesized examples built to demonstrate the
patterns, not sourced case studies. Per the envelope's boundary rule
("never delete or rewrite passing content" — this section is part of what
makes `verbatim_exemplars` pass), this repair pass did not remove or rewrite
them. Flagging honestly here instead: if this skill is ever presented as
containing real Andy Lo case studies, that would be a false claim. As
illustrative teaching exemplars, they are fine; as "things Andy Lo built,"
they are not verified and should not be cited that way.

## Flagged Gap — Signature Moves / Quality Rubric (NOT touched)

Both sections are **LIKELY** — they are reasonable editorial synthesis of
the 12 Genius Patterns / 8 Hidden Knowledge items (same 2026-03-20 enrichment
pass), consistent with the source material's content, but they are
paraphrase/synthesis rather than material found verbatim in
`extractions/andy-lo/extraction-report.md`. No specific claim in either
section contradicts the source; neither should be read as an Andy Lo quote.

## Recognition-Test / Model-Calibration Section

The new `## How to Use This Skill (Model Calibration)` section in
`genius.md` is **VERIFIED** as grounded: every named artifact it references
("$5K-$15K per site," "Prompt Document as Build Blueprint," the Nano
Banana → Flow tool sequence) is drawn from the same extraction report cited
throughout this ledger. The calibration guidance itself (the "polish is the
tell" framing, the invisible-machinery instruction) is this repair worker's
synthesis of the extraction's Executive Summary framing
("architects a multi-tool pipeline where each tool operates in its zone of
excellence," line 18) — labeled **LIKELY** as an interpretive extension, not
a direct Andy Lo quote.
