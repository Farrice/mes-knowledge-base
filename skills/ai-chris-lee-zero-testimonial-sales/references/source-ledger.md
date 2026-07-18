# AI Chris Lee — Source Ledger

Claim-by-claim provenance for `genius.md` (and the duplicate content in
`references/genius-patterns.md`). Labels: **VERIFIED** (verbatim or
numerically exact against a located primary source), **LIKELY**
(source-consistent paraphrase or reasonable synthesis with no single
verbatim anchor), **UNCONFIRMED** (no primary AI Chris Lee source file
exists in this repo to check against — carried forward anyway, flagged so
it is never mistaken for verified authority).

## Sources Consulted (this repair pass, 2026-07-17)

No `extractions/` directory or file for this expert exists anywhere in the
repo. Verified by direct search this session, not inference:

```
ls extractions/ | grep -i "chris.lee\|chris-lee\|chrislee\|zero-test\|testimonial"
→ no matches (confirmed via two separate grep passes, exit code 1 / empty)
```

Repo-wide search for a primary transcript, interview, or video source
mentioning "AI Chris Lee" or "zero testimonial" outside this skill's own
generated files also came back empty — the only hits were this skill's own
`SKILL.md`/`genius.md`, its duplicate copy under
`_active/codex-harvest-2026-06-11/skills/ai-chris-lee-zero-testimonial-sales/`,
the parallel agent persona at `agents/ai-chris-lee/AGENT.md` (2,807 bytes)
and `_active/codex-harvest-2026-06-11/agents/ai-chris-lee/AGENT.md` (3,522
bytes — a later variant with an added "Routing Interop" section, not
identical), and one unrelated research file (`_active/codex-harvest-2026-06-11/
research_outputs/ai_authority_architect_agents/ai_chris_lee.md`, 4,744
bytes) — read in full; it is a devil's-advocate red-team of a *different*
offer (ghostwriting positioning for "conscious founders," MES 3.0
methodology) that happens to share the "AI Chris Lee" filename/slug but
contains zero content about proof-building, Looms, or zero-testimonial
sales. It is NOT a source for this skill and was excluded. All sizes below
confirmed via `wc -c` (bytes, not `wc -l` lines) this session.

| ID | File | Size (bytes, `wc -c`) | Note |
|----|------|------|------|
| S1 | `skills/ai-chris-lee-zero-testimonial-sales/genius.md` (pre-repair) | 12,679 | The skill's own prior genius.md — the only text available; treated as the house-authored baseline, not an independent verification source. |
| S2 | `skills/ai-chris-lee-zero-testimonial-sales/references/genius-patterns.md` | 3,211 | Duplicate of genius.md's 14-pattern list; same origin, not independent. |
| S3 | `skills/ai-chris-lee-zero-testimonial-sales/SKILL.md.old` | 3,318 | Earlier SKILL.md revision; read in full — confirms the skill has iterated internally (v1 → v2) but names no external source, transcript, URL, or date for AI Chris Lee's original material either. |
| — | `extractions/` (repo-wide) | n/a | Confirmed absent for this expert — see search command above. Not 0-byte or unrecoverable; simply never created. |
| — | `_active/codex-harvest-2026-06-11/research_outputs/ai_authority_architect_agents/ai_chris_lee.md` | 4,744 | Read in full; unrelated content (different offer/methodology), excluded as a source. |

## Verdict on Origin

**UNCONFIRMED at the primary-source level.** This skill appears to be a
house-authored synthesis (SKILL.md.old's minimal frontmatter and the
absence of any transcript, episode number, URL, or interview date anywhere
in the file tree are consistent with a skill built from general knowledge
of the "AI Chris Lee" creator/positioning rather than from a captured,
preserved source document). Nothing here proves the patterns are
fabricated — they are internally consistent and plausible — but nothing
proves they are AI Chris Lee's literal words either. No claim in this
skill can be verified against a primary recording this repair pass.

## Claims — genius.md, Genius Patterns (1-14)

| Claim | Label | Anchor |
|---|---|---|
| All 14 numbered patterns (Proof Paradox Diagnosis through GIF Embed Technique) | UNCONFIRMED | S1/S2 (identical content, no independent origin); no transcript, interview, or dated source exists anywhere in the repo to check the patterns against. Internally consistent with each other and with the Hall of Fame Exemplars below (LIKELY at the internal-consistency level only). |

## Claims — genius.md, Hall of Fame Exemplars / Anti-Exemplar

| Claim | Label | Anchor |
|---|---|---|
| "Proof-First Specificity" outreach exemplar (roofing company, 8 vs. 3 estimates) | UNCONFIRMED | S1 (this file, pre-repair); illustrative example, not attributed to a real client or dated event anywhere in the source. |
| "5-Section Loom" narrative exemplar ("Ridgeview Roofing") | UNCONFIRMED | S1; "Ridgeview Roofing" does not resolve to a real, identifiable company in any source file — read as an illustrative construction. |
| Anti-Exemplar ("Generic, Credential-Seeking" email, quoted verbatim: "I'm a marketing consultant with 10 years of experience... currently looking to expand my portfolio") | VERIFIED (as existing skill text) / UNCONFIRMED (as AI Chris Lee's real critique) | S1 — the quote is verbatim-present in the pre-repair genius.md, so it is VERIFIED as this skill's own material; whether AI Chris Lee himself authored this specific critique is UNCONFIRMED against any primary recording. |

## Claims — genius.md, new "Anti-Patterns (Sourced)" section (this repair pass)

All six items were written for this repair. Each anchors to a Genius
Pattern, Signature Move, or Quality Rubric row already present in S1/S2
(internal, house-authored anchors) — none claim a verbatim AI Chris Lee
quote beyond what S1 already contained (the Anti-Exemplar's credential-tax
email, which was already verbatim-present before this repair).

| Claim | Label | Anchor |
|---|---|---|
| Never lead outreach with credentials/years of experience | VERIFIED (as internal anchor) / UNCONFIRMED (as AI Chris Lee's real rule) | `genius.md` Anti-Exemplar section (S1, verbatim quote pre-existing). |
| Never ask permission before showing proof | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 4 + Signature Moves (S1). |
| Never ship more than one proof asset | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 5 + Quality Rubric row "Single-Asset Adherence" (S1). |
| Never let a proof Loom run long or go through revisions | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 10 + Quality Rubric row "Deployment Speed" (S1). |
| Never state a benefit in generic terms without a number | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 9 + Quality Rubric row "Outcome Specificity" (S1). |
| Never treat free proof-building work as charity | VERIFIED (internal) / UNCONFIRMED (external) | `genius.md` Pattern 7 + "Investment, Not Charity" Signature Move (S1). |

## Claims — genius.md, "How to Use This Skill (Model Calibration)" (new section, this repair pass)

Craft/voice guidance authored for this repair, modeled structurally on
`skills/ben-watkins-storytelling/genius.md` lines 7-16 per the batch
envelope — not a factual claim about AI Chris Lee, so no VERIFIED/LIKELY/
UNCONFIRMED label applies to the calibration instructions themselves. The
specific numbers it quotes ("8 estimates instead of 3," "15 minutes a
day," "within 24 hours") are pulled directly from the pre-existing S1
exemplars and Pattern 9/10 text (UNCONFIRMED at the external level, same
as those patterns above).

## Summary

- **VERIFIED**: 1 claim at the "existing skill text" level (the
  Anti-Exemplar's credential-seeking email is verbatim-present in the
  pre-repair file).
- **UNCONFIRMED**: All 14 Genius Patterns, both Hall of Fame Exemplars, the
  Anti-Exemplar's attribution to AI Chris Lee specifically, and all six new
  Anti-Patterns items — none can be checked against a primary transcript,
  interview, or dated source, because none exists anywhere in this repo.
  This was verified by direct file search this session, not assumed.
- No claim was invented this repair pass beyond what S1 already contained;
  every new item is a structural inversion or restatement of pre-existing
  skill content, honestly labeled UNCONFIRMED where external verification
  is impossible.
