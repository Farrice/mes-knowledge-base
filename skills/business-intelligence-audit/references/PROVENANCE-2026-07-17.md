# Provenance — business-intelligence-audit repair

## Absence verification (Rule 2 — no invented "no source" claims)

```
$ ls extractions/ | wc -l
193
$ ls extractions/ | grep -iE "business.intel|mckinsey|minto|consult|7s|mece"
(no output — exit 1)
```

Confirmed by direct read of the 193-entry `extractions/` directory listing: no person/expert extraction backs this skill. This is expected — `business-intelligence-audit` is a METHOD skill (McKinsey/MECE/Pyramid-Principle consulting methodology), not an extraction from a named expert's transcript/interview/podcast, per the task brief.

## Anchor → source table (Anti-Patterns section, genius.md)

| Anchor text (genius.md) | Source file | Line | Verified by |
|---|---|---|---|
| "Your marketing strategy lacks clear differentiation..." | `genius.md` (pre-repair) | 191 | `sed -n '188,193p' skills/business-intelligence-audit/genius.md` |
| "Recommendations bucketed only by time horizon (0-7 days, 30 days, 90 days) without funding dependencies..." | `workflows/executive-growth-roadmap.md` | 77 | `sed -n '75,78p' skills/business-intelligence-audit/workflows/executive-growth-roadmap.md` |
| "Never invent a concrete number to illustrate the fix..." | `references/prompts-v2/04-messaging-audit.md` | 50 | `sed -n '48,52p' skills/business-intelligence-audit/references/prompts-v2/04-messaging-audit.md` |
| "No two bullets in the same section restate the same fact (MECE check)" | `references/prompts-v2/01-business-scan.md` | 102 | `sed -n '100,103p' skills/business-intelligence-audit/references/prompts-v2/01-business-scan.md` |
| "What NOT To Do: at least 3 items to stop, avoid, or not invest in, each with a reason" | `references/prompts-v2/09-recommendation-engine.md` | 51 | `sed -n '48,52p' skills/business-intelligence-audit/references/prompts-v2/09-recommendation-engine.md` |
| "name a real, specific implication (not a generic \"improve marketing\")" | `references/prompts-v2/02-competitive-intelligence.md` | 107 | `sed -n '105,108p' skills/business-intelligence-audit/references/prompts-v2/02-competitive-intelligence.md` |

## External verification (Pattern-level provenance notes added to genius.md)

Run via WebSearch, 2026-07-17:
- 7-Step Problem Solving, MECE, Issue Trees, Hypothesis-Driven Approach: confirmed real, documented McKinsey/BCG/Bain methodology (Slideworks, Wasil Zafar, myconsultingoffer.org, caseinterview.com, hackingthecaseinterview.com).
- McKinsey 7S Framework: confirmed real, Waterman/Peters, 1980s (StrategyU).
- Pyramid Principle / "So What" test: confirmed real, Barbara Minto (myconsultingoffer.org, strategypunk.com, Goodreads).
- "Four Horsemen Audit" (Fear/Greed/Hope/Ignorance): searched explicitly for McKinsey attribution — none found. McKinsey's actual published bias frameworks (groupthink, loss aversion, confirmation bias, anchoring) are different. The fear/greed/hope/ignorance phrasing traces instead to investment-psychology commentary (Globe and Mail/O'Shaughnessy, Fibtimer). Corrected in genius.md Pattern 7 with an honest provenance note rather than leaving the implied-McKinsey framing uncorrected.
- "Pre-Fall / Post-Fall Assessment": searched for an external maturity-model match — none found under this name. Labeled UNCONFIRMED / treated as this skill's own synthesis.

No quote in this repair was written without being read verbatim from its cited file first. No claim of "no source" was made without an actual `ls`/`grep` read and a recorded count.
