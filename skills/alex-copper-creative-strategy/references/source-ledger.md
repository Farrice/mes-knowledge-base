# Source Ledger — alex-copper-creative-strategy

Every source consulted for the Wave 3 Lane 4 repair pass, labeled VERIFIED / LIKELY / UNCONFIRMED per claim.

At the time of the 2026-07-17 repair, **no `extractions/` coverage existed for Alex Cooper under either spelling.** That historical check was verified via direct commands:
- `ls extractions/ | grep -iE 'cooper|copper'` → 0 results (193 total entries in `extractions/`)
- `find . -iname "*cooper*"` (repo-wide, excluding this skill's own directory) → 0 results
- `find extractions -iname "*adcrate*" -o -iname "*ad-crate*" -o -iname "*ad_crate*"` → 0 results

Run 2026-07-17. Ground truth for that repair was therefore the skill's own existing files, each opened and read in full, with byte counts recorded via `wc -c`.

## 2026-08-01 Primary-Source Addition

A primary YouTube source package now exists at `extractions/alex-copper-static-ads/`. Its clean transcript contains 5,427 words, and its evidence package includes native captions, metadata, five contact sheets, and 18 selected frames. The skill-level timestamp and claim ledger is `references/static-ads-2026-source-ledger.md`.

This source upgrades Written-on-the-World Telegraphing from secondhand support to SOURCE-VERIFIED method evidence and adds Workflow 07 mechanics: acquisition null context, selling-locus choice, static eye path, customer-language provenance, and white-space-to-test isolation. Alex's performance, volume, spend, and vendor claims remain SELF-REPORTED unless independently verified.

## Files consulted (all internal to this skill)

| File | Size (bytes, `wc -c`) | Status |
|---|---|---|
| `genius.md` | 29,306 | VERIFIED — read in full |
| `SKILL.md` | 6,797 | VERIFIED — read in full |
| `SKILL.md.old` | 11,299 | VERIFIED — read in full; no anti-pattern content found there |
| `references/hidden-knowledge.md` | 2,461 | VERIFIED — read in full |
| `references/genius-patterns.md` | 4,650 | VERIFIED — read in full |
| `references/implementation.md` | 2,300 | VERIFIED — read in full |
| `references/agent_system_prompt.md` | 3,988 | VERIFIED — read in full |
| `references/_legacy-prompts/ai-visual-generation-protocol.md` | 17,194 | VERIFIED — read in full (Common Pitfalls, lines 263-284) |
| `workflows/02-performance-creative-production.md` | — | VERIFIED — grepped, line 48 read in context |
| `workflows/01,03,04,05,06-*.md` | — | VERIFIED — already pass `workflow_contracts`; not modified |

## Claim-by-claim (new Anti-Patterns section + Model Calibration section)

1. **"the algorithm isn't broken, your creative sucks"** — VERIFIED as verbatim text in `references/agent_system_prompt.md` line 12. LIKELY (not VERIFIED) as an actual spoken Cooper line — no primary transcript exists in this repo to cross-check; the line lives inside a persona-voice document authored for this skill, not a cited quote bank.
2. **"meta ads is a creative game, not a media buying game"** — VERIFIED as verbatim text in `references/agent_system_prompt.md` line 9. LIKELY as an actual Cooper utterance, same caveat as #1.
3. **"Become an absolute hoarder of top performing ads."** — VERIFIED as verbatim text in `genius.md` line 202, inside the section explicitly dated and sourced to "Farrice's claude.ai extraction sessions on Alex Cooper's DC Diaries appearance ('Reinventing Creative Strategy with AI') plus the Crown Jewel follow-up chats" (`genius.md` line 169). LIKELY as a verbatim Cooper quote — this is a secondhand extraction note, not a primary transcript file, so it cannot be independently re-verified inside this repo.
4. **"The only people making good ads with AI are people who make good ads without AI"** — same provenance as #3 (`genius.md` line 240). LIKELY.
5. **"I don't think creative shops as they currently work will be around in 2-3 years."** — same provenance as #3 (`genius.md` line 245). LIKELY.
6. **"Problem: Full AI ads lack trust. Solution: AI for hooks only, humans for testimony."** — VERIFIED as verbatim text in `references/_legacy-prompts/ai-visual-generation-protocol.md`, Pitfall 3. UNCONFIRMED as Cooper's literal words — this section reads as synthesized operator guidance, not a quoted transcript excerpt; no attribution language ties it to a spoken Cooper line.
7. **"Problem: AI attempting photorealism often hits uncanny valley. Solution: Lean into stylized/surreal"** — same file, Pitfall 1. UNCONFIRMED as literal Cooper words, same reasoning as #6.
8. **The "Feature-First, Who Cares?" Anti-Exemplar** (`genius.md`, Hall of Fame Exemplars section) — VERIFIED as pre-existing skill content (not new invention by this repair pass). UNCONFIRMED as describing a real Cooper-critiqued ad — written as an illustrative composite, not a cited real campaign.
9. **Workflow 02's inline anti-pattern line** ("Do NOT use collision as a gimmick...") — VERIFIED as existing workflow text, `workflows/02-performance-creative-production.md` line 48. This is house-authored guidance for the skill, not a Cooper quote — labeled VERIFIED as a skill-authored constraint, explicitly not attributed to Cooper.

## What this means for downstream use

Every first-person "Cooper says" line in this skill (`genius.md` §16-27, Hidden Knowledge items 8-13) is a **LIKELY**-grade secondhand paraphrase from Farrice's own extraction sessions on the DC Diaries appearance — no primary transcript for that session exists anywhere in this repo (`extractions/` or otherwise). Treat those attributions as LIKELY, not VERIFIED, until a transcript file is added under `extractions/`. Content authored for the skill itself (personas, pitfalls lists, workflow guardrails) is VERIFIED as existing skill material but UNCONFIRMED as literal Cooper quotation where no attribution language says otherwise.
