# PROVENANCE — claim-safe-health-marketing repair

Anchor → source file+location table. All facts used to source anti-patterns and
enrich zero-entity sections are pulled from material **already present and cited
inside this skill's own files** — no new external research was conducted, and no
new claims were introduced. This is a regulatory-knowledge skill; ground truth is
the skill's existing genius.md Sources block + `references/source-ledger.md`, not
a person-voice `extractions/` folder (confirmed none exists: `ls extractions/ |
grep -i claim-safe` and broader regulatory-term greps returned zero hits).

| Anchor added | Location added | Traces to (file + location) |
|---|---|---|
| "$650K refund order, Rejuvica/Sobrenix, Nov 2024" | genius.md: How to Use This Skill; Underlying Belief; GP-08; Anti-Pattern... wait see note below | genius.md original line 17 (Sources block: "FTC enforcement actions: Rejuvica/Sobrenix (Nov 2024, $650K refund, alcohol-craving claims)..."); corroborated `references/source-ledger.md` row 8 |
| "FTC Health Products Compliance Guidance (Dec 2022, updated 2023)" | genius.md: Underlying Belief; Anti-Pattern #6 | genius.md original line 11 (Sources block); `references/source-ledger.md` row 1 |
| "FTC's 1983 Deception Policy Statement" | genius.md: GP-03; Concrete-Metaphor Library | `references/source-ledger.md` row 6 ("FTC, 'Net impression' doctrine (1983 Deception Policy Statement...)") |
| "NAD's 2025 Reus Research and Ingenuity BrainPack decisions (BBB National Programs)" | genius.md: Anti-Pattern #3 | genius.md original line 16 (Sources block) and line 68 (GP-02 body, "BrainPack, Reus Research, Olly cases"); `references/source-ledger.md` row 7 |
| "Pearson v. Shalala, 164 F.3d 650, 1999" | genius.md: Concrete-Metaphor Library | genius.md original line 15 (Sources block) and GP-04 heading; `references/source-ledger.md` row 4 |
| "16 CFR Part 255" | genius.md: Word-Swap Bank | genius.md original line 14 (Sources block) and GP-05 heading |
| "Dougherty's category-specific high-risk term list" | genius.md: Word-Swap Bank | `references/red-flag-word-bank.md` line 40 heading ("Category-Specific High-Risk Terms (Dougherty's 'especially sensitive' list)") — read directly, quote is verbatim from that file |
| "`references/platform-rules.md` — Meta Personal Attributes policy" | genius.md: Anti-Pattern #5 | `references/platform-rules.md` line 11 (Meta section, "Personal Attributes policy") — read directly, verbatim mechanic |
| "`references/platform-rules.md` — Amazon scanner does not parse sentence-level meaning" | genius.md: Anti-Pattern #7; Concrete-Metaphor Library | `references/platform-rules.md` line 30 (Amazon section) — near-verbatim phrase already used in that file |

## Correction to anchor-count note above
The $650K/Rejuvica anchor appears in three places (How to Use This Skill,
Underlying Belief, GP-08) — each instance traces to the same single source
(genius.md original Sources line 17 / source-ledger.md row 8), reused because it
is the one concrete enforcement dollar-figure already verified in this skill's
own source material. Reuse of one verified fact across sections is intentional
(minimal-touch, no new unverified facts introduced) — not double-counted as
independent sourcing.

## UNCONFIRMED / not touched
No new UNCONFIRMED items were introduced. The skill's existing UNCONFIRMED flag
(genius.md original line 22 — Ballard/Dougherty self-reported track records) was
left untouched; it was already correctly labeled and did not need repair.

## Files reviewed but not modified (already passing)
- `references/source-ledger.md` — already lists every source VERIFIED/LIKELY,
  claim-by-claim; source_ledger check was not in the failing list. Copied
  unmodified into this output dir for layout completeness.
- `SKILL.md` — already contains recognition-test language (Quick Reference
  section: "Recognition test: would a supplement regulatory attorney AND a
  direct-response copywriter both sign off..."); recognition_test check was not
  failing. Not copied to output (unchanged).
- `references/platform-rules.md`, `references/red-flag-word-bank.md`,
  `workflows/*.md` — read for grounding but not modified; workflow_contracts
  check was not in the failing list for this skill.
