# Source Ledger — marisa-murgatroyd-course-design

Claim-by-claim source accounting for the skill. Every source actually consulted during this repair is listed, including negative results (searches that found nothing), per the "no false unrecoverable claims" rule.

## Primary skill files (internal provenance)

| Source | Consulted | Label | Notes |
|---|---|---|---|
| `skills/marisa-murgatroyd-course-design/genius.md` (pre-repair, 94 lines) | Read in full | LIKELY | 15 patterns/insights, each carrying an inline quote. Attributed in `SKILL.md` frontmatter to `source: claude.ai export 2026-07-01` — an upstream conversation export, not a primary transcript this repair can independently open. Internally consistent, so LIKELY rather than UNCONFIRMED. |
| `skills/marisa-murgatroyd-course-design/SKILL.md` (46 lines) | Read in full | LIKELY | Same provenance chain as genius.md. |
| `skills/marisa-murgatroyd-course-design/workflows/01-architect-experience-product.md` | Read in full | LIKELY | Restates genius.md patterns operationally; no new quotes beyond what's in genius.md. |
| `skills/marisa-murgatroyd-course-design/workflows/02-craft-mission-statement.md` | Read in full | LIKELY | Same. |
| `skills/marisa-murgatroyd-course-design/workflows/03-launch-mvo-from-zero.md` | Read in full | LIKELY | Same; source of the "Prescribe, don't pitch" anti-pattern anchor at line 41. |
| `skills/marisa-murgatroyd-course-design/references/prompts-v2/experience-product-architecture.md` | Read in full | LIKELY | v2 execution prompt; frontmatter dated `refactored: 2026-07-13`, `forged: born-v2` — no independent source citation of its own. |
| `skills/marisa-murgatroyd-course-design/references/prompts-v2/mission-statement.md` | Read in full | LIKELY | Same. |
| `skills/marisa-murgatroyd-course-design/references/prompts-v2/mvo-zero-audience-launch.md` | Read in full | LIKELY | Same; source of "Prescribe, don't pitch" anchor at line 54. |
| `agents/marisa-murgatroyd/AGENT.md` | Read in full | LIKELY | Derivative summary of the same skill content; no new claims. |
| `agents/marisa-murgatroyd/memory/context.md` | Read in full | N/A | Empty scaffold ("to be populated") — no claims to verify. |

## extractions/ search (ground-truth requirement per ENVELOPE.md)

- `find extractions -iname "*murgatroyd*" -o -iname "*marisa*"` — **0 results**.
- `grep -ril "murgatroyd" extractions` — **0 results**.
- Conclusion: no `extractions/` file exists for this expert. This is reported as a verified negative (commands run, zero matches), not an assumed absence — per the ENVELOPE.md rule that "no source exists" is itself a provenance claim requiring an actual search.
- Consequence: this skill's *only* ground truth is the claude.ai export already digested into the files above. No primary transcript is available inside this repo to check quotes verbatim against.

## External verification (2026-07-18, WebSearch — supplementary, not required by ENVELOPE.md but run to raise confidence where possible)

| Claim | Result | Label |
|---|---|---|
| Marisa Murgatroyd is founder of Live Your Message, creator of "The Experience Formula" | Confirmed — `liveyourmessage.com`, `liveyourmessage.com/the-experience-formula/` | VERIFIED |
| "Your mission, should you choose to accept it, is…" framing, used by Murgatroyd for her own flagship program | Confirmed verbatim in DigitalMarketer Podcast Ep. 175 summary ("Design, Launch, and Profit From a Damn Good Product with Marisa Murgatroyd") | VERIFIED |
| "59% completion vs 3-7% industry average" (used throughout genius.md/SKILL.md as her headline stat) | NOT found at 59% in public search; public sources (FindFocus, Hustle & Flowchart podcast, EIN Presswire) instead cite completion figures of 70-76% for her Experience Product Masterclass | UNCONFIRMED at the specific percentage — the general claim ("dramatically above the 3-5% industry average") is directionally consistent across sources, but 59% specifically was not corroborated externally. Downgraded from the skill's original unlabeled/implicit-VERIFIED treatment to UNCONFIRMED-at-precision in `genius.md`. |
| "59% live cohort vs 42% evergreen" completion gap | Not found in public search (searches surfaced only the 70-76% figures, no evergreen-vs-live breakdown) | UNCONFIRMED — flagged inline in genius.md anti-patterns section. |
| ~3,000 testimonials from ~7,000 students; $2,497+ price point; Experiencify LMS name | Not independently re-verified this session (out of scope for a repair-only pass; no contradicting evidence surfaced either) | LIKELY (unchanged from pre-repair status) |

## Repair scope note

This is a targeted repair of two failing heartbeat checks (anti_patterns_sourced, recognition_test) plus the batch-wide Model Calibration section — not a re-extraction. No new primary-source research beyond the two supplementary web searches above was performed; all pattern content is unchanged from the pre-repair genius.md except for the added Model Calibration section, the added Anti-Patterns section, and the two inline confidence-downgrade notes on the 59%/42% figures.
