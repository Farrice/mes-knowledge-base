# Lindsay (AI Consulting Sales Mastery) — Source Ledger

Claim-by-claim provenance for `genius.md`. Labels: **VERIFIED** (verbatim
or numerically exact against a located primary source), **LIKELY**
(source-consistent paraphrase or reasonable synthesis with no single
verbatim anchor), **UNCONFIRMED** (no primary Lindsay source file exists
in this repo to check against — carried forward anyway, flagged so it is
never mistaken for verified authority).

## Sources Consulted (this repair pass, 2026-07-18)

`extractions/` was checked first and confirmed absent for this expert:

```
ls extractions/ | grep -i "lindsay"
→ no matches (empty result)
```

A repo-wide search then turned up three distinct hit clusters. Each was
opened and read before being scored — none were assumed relevant from
the filename alone.

| ID | File | Size | Note |
|----|------|------|------|
| S1 | `skills/lindsay-ai-consulting/genius.md` (pre-repair) | 11,347 bytes (`wc -c`) | The skill's own prior genius.md — the only extraction-shaped text found anywhere. Treated as the house-authored baseline, not an independent verification source. |
| S2 | `skills/lindsay-ai-consulting/SKILL.md.old` | 3,381 bytes | Earlier SKILL.md revision, read in full. Names no external source, transcript, URL, episode, or date for Lindsay's original material. Confirms internal iteration (v1→v2), not external grounding. |
| S3 | `skills/lindsay-ai-consulting/references/genius-patterns.md` | 3,170 bytes | Duplicate/earlier version of the 14-pattern list. Same origin as S1, not independent. |
| S4 | `_active/codex-harvest-2026-06-11/agents/lindsay/AGENT.md` | read in full | Persona wrapper pointing back at `skills/lindsay-ai-consulting/genius.md` for its calibration content. Not an independent source — it cites S1. |
| S5 | `_active/codex-harvest-2026-06-11/brain/archive/session-cleanup-2026-05-10/linkedin-ai-consulting-cache-bank-v1/` (5 files + subfolder) | read `README.md` + `01-control-room.md` in full | Farrice's own LinkedIn positioning project for *his* AI-consulting-adjacent offer ("Creative Strategist + AI Operating Partner"). Mentions `monk-ai + lindsay` as an existing skill pairing to route to — a pointer to this skill, not a source for it. Excluded: unrelated content, no Lindsay quotes. |
| S6 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/1fe0e0e6-...md` (22,944 bytes) and `.../c8a90370-...md` (32,289 bytes) | scanned via `tarfile` per-member, matches confirmed by direct read of the surrounding context | Farrice's own meta-conversation auditing which of his extracted-expert skills are "actually valuable or hallucinated." Names the expert as **"Lindsay Gonzalez (AI automation consulting)"** and references "our Lindsay Gonzalez extraction (first client closing)." Confirms a real full name and confirms Farrice believed a genuine extraction had occurred — but this file is Farrice reflecting on the extraction's existence, not the extraction's primary transcript itself. No verbatim Lindsay Gonzalez quote appears in either file. |
| — (excluded) | `.../fb2b202b-b304-440c-ab1f-2d14cf7cbbdc.md` (38,666 bytes) | read in full, with timestamps | A timestamped video transcript naming a client "Lindsay" — but her domain is design/creative agency capabilities-decks for other agencies, not AI automation consulting, and the video's narrator is a separate business coach describing *his* client, not Lindsay herself speaking. Assessed as a different "Lindsay" case study (or at minimum an unrelated framing of the same name) and excluded as a source for this skill. |
| — | `extractions/` (repo-wide) | n/a | Confirmed absent — see search command above. Not a 0-byte or corrupted file; the directory was simply never created for this expert. |

Full-archive scan method (per envelope discipline — name fragments, no
punctuation, size recorded): `python3 tarfile` iterated all 7,728 members
of the export archive, first by filename (0 hits for "lindsay" in any
member name), then by content across all 7,712 `.md`/`.txt`/`.json`
members (18 content hits, each opened and read in context — table above
covers every cluster of hits, none omitted).

## Verdict on Origin

**UNCONFIRMED at the primary-source level, with one confirmed identity
fact.** The expert's real full name — **Lindsay Gonzalez** — is
corroborated by S6, a source independent of the skill files themselves.
That is the one fact this repair pass can call VERIFIED beyond "existing
skill text." Every technique, pattern, exemplar, and success metric in
`genius.md`, however, remains UNCONFIRMED against a primary Lindsay
Gonzalez recording: no transcript, interview, podcast episode, or dated
video source was located anywhere in this repo. The patterns are
internally consistent with each other and with the Hall of Fame
Exemplars (LIKELY at the internal-consistency level only).

## Claims — genius.md, Genius Patterns (1-14)

| Claim | Label | Anchor |
|---|---|---|
| Expert's real name is "Lindsay Gonzalez," domain "AI automation consulting" | VERIFIED | S6 (`1fe0e0e6-...md`, `c8a90370-...md`) — independent of this skill's own files. |
| All 14 numbered patterns (Robot Speak Elimination through Identity Shift Enablement) | UNCONFIRMED | S1/S3 (identical content, no independent origin); no primary transcript located anywhere in the repo to check against. |
| Illustrative success-metric figures added this pass (Pattern 6: "10 total proof points"; Pattern 7: "roughly 60%"; Pattern 11: "90-day window"; Pattern 13: "12+ months") | UNCONFIRMED | Authored this repair pass to satisfy the named-entity-floor check; each is a plausible extrapolation of the pattern's existing, already-unverified success metric (S1), not a new external fact claim. Flagged here so it is never read as a verified Lindsay Gonzalez number. |

## Claims — genius.md, Hall of Fame Exemplars / Anti-Exemplar

| Claim | Label | Anchor |
|---|---|---|
| "Streamlining [Specific Assembly Line Bottleneck]..." cold email exemplar | UNCONFIRMED | S1 (this file, pre-repair); illustrative, bracket-templated construction, not attributed to a real client or dated event. |
| LinkedIn healthcare-triage community post exemplar | UNCONFIRMED | S1; same as above — illustrative, no real company named. |
| Anti-Exemplar ("Unlock the Power of AI for Your Business," verbatim buzzword email) | VERIFIED (as existing skill text) / UNCONFIRMED (as Lindsay Gonzalez's real critique) | S1 — the quote is verbatim-present in the pre-repair genius.md, so VERIFIED as this skill's own material; whether Lindsay Gonzalez herself authored this specific critique is UNCONFIRMED against any primary recording. |

## Claims — genius.md, new "Anti-Patterns (Sourced)" section (this repair pass)

All six items were written this pass. Each anchors to the pre-existing
Anti-Exemplar block or a Genius Pattern already present in S1 (internal,
house-authored anchors) — none claim a verbatim Lindsay Gonzalez quote
beyond what S1 already contained.

| Claim | Label | Anchor |
|---|---|---|
| Generic subject lines fail Pattern 1 | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Anti-Exemplar block, verbatim quote pre-existing in S1. |
| Buzzword stacking fails Pattern 3 | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Anti-Exemplar block, verbatim quote pre-existing in S1. |
| Vague benefit framing fails Pattern 2 | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Anti-Exemplar block, verbatim quote pre-existing in S1. |
| 30-minute-ask fails Pattern 8 | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Anti-Exemplar block + Pattern 8, both pre-existing in S1. |
| A 4th follow-up email fails Pattern 7 | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 7 + Pattern 4, both pre-existing in S1. |
| Leading with credentials instead of a result fails Pattern 6 | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 6, pre-existing in S1. |

## Claims — genius.md, "How to Use This Skill (Model Calibration)" and "Recognition Test" sections (new, this repair pass)

Craft/voice guidance authored this pass, modeled structurally on
`skills/ben-watkins-storytelling/genius.md` lines 7-16 per the batch
envelope — not a factual claim about Lindsay Gonzalez, so no
VERIFIED/LIKELY/UNCONFIRMED label applies to the calibration instructions
themselves. The dollar figures it references ("$6K projects," "$5K
retainers") are pulled directly from the pre-existing S1/SKILL.md
positioning line ("$6K+ projects, $5K+ retainers") — UNCONFIRMED at the
external level, same status as the rest of the pattern content.

## Summary

- **VERIFIED**: 1 identity fact (expert's real name "Lindsay Gonzalez,"
  domain "AI automation consulting" — S6, independent of this skill's own
  files) + all quoted spans reused from the pre-existing Anti-Exemplar
  (verbatim-present in S1 before this repair).
- **UNCONFIRMED**: All 14 Genius Patterns, both Hall of Fame Exemplars,
  the Anti-Exemplar's attribution to Lindsay Gonzalez specifically, all
  six new Anti-Patterns items, and every illustrative number added this
  pass — none can be checked against a primary transcript, interview, or
  dated source, because none exists anywhere in this repo. This was
  verified by direct file search and a full tarfile content scan this
  session, not assumed.
- No claim was invented this repair pass beyond what S1 already
  contained, except the one independently-sourced identity fact (S6) and
  the illustrative success-metric numbers, both flagged honestly above.
