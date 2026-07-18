# Source Ledger — brock-johnson-shareworthy-content

Claim-by-claim provenance audit, run 2026-07-17 during the Wave 3 Lane 4
repair pass. Every file size below was confirmed with `wc -c` (bytes, not
lines) on 2026-07-17, from the repo root.

## 0. The absence check (done first, per the envelope's hard rule)

`ls extractions/ | grep -i "brock\|johnson"` → **no matches**. `extractions/`
exists as a directory (not missing) and contains files for other experts;
it simply holds nothing for Brock Johnson. This is recorded as a verified
absence, not an assumption.

`find . -iname "*brock*johnson*"` (excluding `skills/` and `.tmp/`) surfaces
only: `agents/brock-johnson/` (persona files) and evolution-store trace/variant
artifacts generated *from* this skill (not sources *for* it). No transcript,
interview file, course export, or dated primary source exists anywhere in
this repo for Brock Johnson.

## 1. Biographical / authority claims — UNCONFIRMED

| Claim | Where it appears | Label | Why |
|---|---|---|---|
| "Direct intelligence from Instagram's Head (Adam Mosseri)" | `SKILL.md` line 14 | UNCONFIRMED | No interview transcript, URL, or dated source file exists in this repo substantiating an Adam Mosseri interview. |
| "100K+ following," creator of "Build Your Tribe" | `agents/brock-johnson/AGENT.md` line 10 | UNCONFIRMED | No follower-count source, screenshot, or dated reference in-repo. |
| "18+ months of proven strategy implementation" | `agents/brock-johnson/AGENT.md` line 10 | UNCONFIRMED | No case-study, results doc, or dated log in-repo. |
| "1 share = 150-400 views (10-26x more than likes)" | `SKILL.md` line 13, echoed in `genius.md` § Metrics That Actually Matter | UNCONFIRMED as an Instagram platform statistic | No Instagram engineering source, blog post, or dated citation in-repo backs this ratio. Treated as this skill's own internal reference math (LIKELY reflects the skill author's working assumption), not independently verified. |

These claims are NOT deleted (additive-first boundary) — they're flagged
here so downstream users know the persona's authority claims are unverified
inside this repo, and would need external verification (a real Brock
Johnson interview/course transcript) before being asserted as fact in
client-facing output.

## 2. The skill's own constitutive material — VERIFIED to exist, LIKELY as methodology, UNCONFIRMED as verbatim Brock Johnson quotes

None of the files below are primary-source transcripts. They are
practitioner-style instructional prompts authored for this skill. They are
internally consistent with each other (same taxonomy, same vocabulary
across all six "Crown Jewel" prompts), which is why they're labeled LIKELY
for methodology — but no file traces back to Brock Johnson's actual words,
so nothing here is labeled VERIFIED as a quote.

| File | Bytes (wc -c) | Label |
|---|---|---|
| `references/_legacy-prompts/algorithm-transcendence-playbook.md` | 5,739 | VERIFIED (exists, populated) / LIKELY (methodology) / UNCONFIRMED (as Brock's verbatim words) |
| `references/_legacy-prompts/content-format-architect.md` | 5,147 | same |
| `references/_legacy-prompts/engagement-psychology-system.md` | 4,388 | same |
| `references/_legacy-prompts/hook-science-engineer.md` | 4,633 | same |
| `references/_legacy-prompts/shareworthy-content-generator.md` | 5,071 | same |
| `references/_legacy-prompts/viral-share-optimizer.md` | 4,535 | same |
| `references/prompts/*.md` (6 files) | identical byte-for-byte to `_legacy-prompts/` | same — verified duplicate copies |
| `references/prompts-v2/*.md` (6 files) | 5,261–6,955 each | same — restructured "structure-pure" variants (Output Contract/Skeleton/Quality Gate added), same underlying claims |
| `references/quality-rubric.md` | 83,382 | VERIFIED (exists, populated, not a stub) / LIKELY (skill's own quality calibration) / UNCONFIRMED (as verified Brock Johnson quotes) |
| `references/genius-patterns.md` | 5,013 | VERIFIED (exists) — duplicate of `genius.md`'s Unconscious Mastery Behaviors + Hidden Knowledge sections, same caveats apply |
| `agents/brock-johnson/AGENT.md` | 2,022 | VERIFIED (exists) — persona routing file, not a source |
| `agents/brock-johnson/memory/context.md` | 164 | VERIFIED (exists) — empty template, no content to source from |

## 3. What the anti-patterns and named-entity anchors in genius.md actually cite

Every "Source anchor" line added to `genius.md` in this repair points at one
of the files above and quotes it verbatim (see `PROVENANCE.md` in this
output folder for the exact file+line table). None of those anchors claim
Brock Johnson said the quoted line in an interview — they cite the skill's
own prompt files as the origin of the pattern, which is the honest
provenance available.

## Net assessment

This skill has no primary-source grounding in this repo. Its genius.md
patterns, Hall of Fame exemplars, and Signature Moves are self-consistent
synthesized content built to model a real public figure's known positioning
(Instagram growth strategist, share-based content philosophy) but are not
traceable to a transcript, course export, or interview file. Treat output
from this skill as a well-structured content framework, not as a verified
Brock Johnson quote engine, until a primary source is added to
`extractions/`.
