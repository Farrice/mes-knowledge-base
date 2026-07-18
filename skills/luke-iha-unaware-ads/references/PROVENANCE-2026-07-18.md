# PROVENANCE — luke-iha-unaware-ads repair

Anchor → source file + location, for every new claim/quote added by this repair.
All located via direct `grep`/exact-string search against the live extraction files,
this session — not recalled from memory.

| Anchor (in repaired genius.md) | Source file | Locator |
|---|---|---|
| "would Iha recognize this as..." (Model Calibration recognition test) | Authored this repair; not a quote — recognition-test framing modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per envelope instruction | n/a (framing device, not a sourced claim) |
| "It doesn't read like an ad. It should read like information that's promising some sort of new insight, or it's a story, or it's a confession" | `extractions/luke-iha-hooks/transcript.txt` | grep string: `it doesn.t read like an ad` |
| "start their ad actually three to four sentences in" | `extractions/luke-iha-hooks/transcript.txt` | grep string: `most people hedge` |
| "A polite hook is a dead hook. A comfortable hook is a dead hook." | `extractions/luke-iha-hooks/transcript.txt` | grep string: `A polite hook is a dead hook` |
| "my doctor accused me of lying" | `extractions/luke-iha-hooks/transcript.txt` | grep string: `doctor accused me of lying` |
| "my husband came out as gay after 26 years of marriage and it nearly killed me" | `extractions/luke-iha-hooks/transcript.txt` | grep string: `husband came out as gay` |
| Anti-Pattern 1: opener-hedging | `extractions/luke-iha-hooks/transcript.txt`; commit date via `git log --diff-filter=A --date=short` | grep string: `most people hedge`; commit date 2026-03-20 |
| Anti-Pattern 2: polite/comfortable hooks | `extractions/luke-iha-hooks/transcript.txt` | grep string: `A polite hook is a dead hook` |
| Anti-Pattern 3: fake open loops | `extractions/luke-iha-hooks/transcript.txt` | grep string: `they think that they.re doing some sort of open loop` |
| Anti-Pattern 4: mechanism-before-relevance | `extractions/luke-iha-hooks/transcript.txt` | grep string: `a mistake that people do is they try to put that mechanism first` |
| Anti-Pattern 5: awareness-level mismatch ("99% of drop shippers...") | `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt`; commit date via `git log --diff-filter=A --date=short` | grep string: `99% of drop shippers`; commit date 2026-03-10 |
| Anti-Pattern 6: conspiracy-framing avoidance | `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` | grep string: `lean into conspiracy` |
| Genius Patterns 1-8 / Hidden Knowledge (pre-existing, unchanged) | `extractions/luke-iha/video-3-levels-of-awareness/extraction-report.md` | Sections "Genius Patterns" / "Hidden Knowledge" — synthesized from the transcript above |

## Commands run to establish anchors

```
git log --diff-filter=A --format="%ad" --date=short -- extractions/luke-iha-hooks/transcript.txt
  => 2026-03-20
git log --diff-filter=A --format="%ad" --date=short -- extractions/luke-iha/video-3-levels-of-awareness/transcript.txt
  => 2026-03-10
wc -c extractions/luke-iha-hooks/transcript.txt extractions/luke-iha/video-3-levels-of-awareness/transcript.txt
  => 25569 / 55910 bytes (both real, non-empty, not truncated)
grep -c "healthiest.*breakfast\|real reason you procrastinate" <all 8 luke-iha extraction transcripts>
  => 0 everywhere (confirms Hall of Fame Exemplar hooks are skill-authored, not verbatim — flagged UNCONFIRMED in source-ledger.md, left untouched as pre-existing content)
```
