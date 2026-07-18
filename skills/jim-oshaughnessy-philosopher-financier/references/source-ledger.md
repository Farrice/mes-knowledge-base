# Source Ledger — jim-oshaughnessy-philosopher-financier

Repair pass: 2026-07-18, Wave 3 Lane 4 Batch 7. Every source consulted during
this repair, plus a claim-by-claim status for every non-trivial assertion in
`genius.md`. Labels: **VERIFIED** (primary source in-repo, quote/fact
confirmed against it) / **LIKELY** (well-established public record or
strong indirect evidence, not confirmed against an in-repo primary source) /
**UNCONFIRMED** (no source located anywhere searched).

## Sources checked (with sizes, per the audit protocol)

| Source | Method | Result |
|---|---|---|
| `extractions/` (repo root) | `ls extractions/ \| grep -i oshaughnessy` and `grep -i osh` | 0 hits — only unrelated names (Josh Sanders, Joshua Smith) |
| `_active/codex-harvest-2026-06-11/` | `grep -rli oshaughnessy` | Hits are downstream copies of this repo's own agent/skill files (`agents/jim-oshaughnessy/AGENT.md`, index files), not a primary transcript — these are the same synthetic content already in `skills/jim-oshaughnessy-philosopher-financier/`, not an independent source |
| `research_outputs/ai_authority_architect_agents/jim_oshaughnessy.md` | Read in full (10,052 bytes) | AI-generated "Blue Ocean" LinkedIn-ghostwriting market-strategy memo written in his analytical style for a third party (Farrice's business), **not** a transcript or interview with O'Shaughnessy. Zero verbatim quotes from him. Not usable as a source. |
| `_archive/claude-export-2026-07-01.tar.gz` | `wc -c` (332,779,255 bytes) then full-content grep (`tar -xzOf ... \| grep -a -i oshaughnessy`, not filename-only) over the full extracted stream | **0 matches**, confirmed with a clean grep exit code (no error, no output) after a complete read of the archive |
| `agents/jim-oshaughnessy/AGENT.md` + `memory/context.md` | Read in full | Agent persona/config file referencing the skill; `memory/context.md` is an empty template ("(None yet)"). No source material. |
| `skills/jim-oshaughnessy-philosopher-financier/genius.md` (pre-repair) | Read in full | The existing "Hidden Knowledge" and "Genius Patterns" content itself, with zero inline citations to any source file |

**Conclusion**: no primary-source transcript, interview, podcast episode, or
book excerpt for Jim O'Shaughnessy exists anywhere in this repo. This
independently reconfirms the earlier finding by the nba-betting-edge repair
worker on an adjacent skill. Every pattern in this skill is analyst-inferred
synthesis from his public persona, not extraction from a primary source.

## Claim-by-claim status

| Claim | Status | Note |
|---|---|---|
| Author of "What Works on Wall Street" | LIKELY | Well-established public record (widely known investing book); not verified against an in-repo primary source |
| Founder of O'Shaughnessy Asset Management (OSAM) | LIKELY | Well-established public record; not verified against an in-repo primary source |
| Host/co-host of "Infinite Loops" podcast | LIKELY | Well-established public record; not verified against an in-repo primary source |
| Pattern 1 (Arbitrage of Human Nature) | LIKELY-plausible | Consistent with the well-known thesis of "What Works on Wall Street" (systematic factor investing exploiting behavioral bias); exact phrasing UNCONFIRMED |
| Pattern 2 (Encyclopedia Protocol) | UNCONFIRMED | No source anchor |
| Pattern 3 (Pre-Fall/Post-Fall Assessment) | UNCONFIRMED | No source anchor |
| Pattern 4 (Book as Career Catalyst) | LIKELY-plausible | Consistent with his public career arc (book preceded firm); exact framing UNCONFIRMED |
| Pattern 5 (Practitioners Over Academics) | UNCONFIRMED | No source anchor, though thematically consistent with rules-based investing |
| Pattern 6 (Feedback Obsession) | LIKELY-plausible | Quant investing inherently produces dated performance feedback; exact framing UNCONFIRMED |
| Pattern 7 (Many Paths to Heaven) | UNCONFIRMED | No source anchor |
| Pattern 8 (Reread Protocol) | UNCONFIRMED | No source anchor |
| Pattern 9 (Four Horsemen Defense) | UNCONFIRMED | No source anchor for this as his named framework |
| Pattern 10 (Authenticity Over Polish) | UNCONFIRMED | No source anchor |
| Pattern 11 (Consensus Reality Check) | UNCONFIRMED | No source anchor |
| Pattern 12 (Synthesis Engine) | UNCONFIRMED | No source anchor |
| Pattern 13 (Saturated Intuition Recognition) | UNCONFIRMED | No source anchor |
| Pattern 14 (Rebel Integration) | UNCONFIRMED | No source anchor |
| Pattern 15 (Four Acts Architecture) | LIKELY-plausible | Consistent with his public career arc (analyst → author → OSAM founder → 2021-era majority-stake transition → podcast host); the "four acts" framing itself is analyst-applied |
| Pattern 16 (Money as Information System) | UNCONFIRMED | No source anchor |
| Pattern 17 (Mind-Body Reintegration) | UNCONFIRMED | No source anchor — lowest-confidence pattern in the file |
| "The Barron's Gambit" (hidden knowledge) | UNCONFIRMED | No source anchor |
| "The $200 Check Imagination Trigger" | UNCONFIRMED | No source anchor; the specificity of the anecdote (a "strange letter," a "30-year novel project") reads as invented narrative detail |
| "The Marduk Power Play Pattern" | UNCONFIRMED | No source anchor; the "Marduk" label does not resolve to any known O'Shaughnessy reference |
| "The 45% Genetic Investment Behavior" | UNCONFIRMED | No cited study; do not present as a research finding |
| "The Death/Rebirth Universal Pattern" | UNCONFIRMED as O'Shaughnessy-specific | Generic Campbellian/mythological trope with no anchor tying it to him personally |
| "The Gestabo Pass Principle" | UNCONFIRMED | Highest-risk entry — the term itself does not resolve to a recognizable proper noun or known reference; flag for removal or replacement on next real-source pass |
| Hall of Fame Example 1 (What Works on Wall Street framework narrative) | Mixed | Book title + factor content LIKELY (public record); the "arbitrage of human nature" narrative framing in quotes is UNCONFIRMED as verbatim O'Shaughnessy language — it is analyst paraphrase |
| Hall of Fame Example 2 (OSAM strategic transition narrative) | Mixed | Firm name LIKELY (public record); the internal-motivation narrative ("focus on legacy and transmission... rather than merely maximizing a personal payout") is UNCONFIRMED analyst inference |
| Evolution Log entry (2026-04-09) | VERIFIED | Present verbatim in the pre-repair `genius.md`; internal system record, not a claim about O'Shaughnessy |

## What this means for downstream use

Any deliverable produced with this skill that states a specific fact,
statistic, or quote "as O'Shaughnessy" should carry a hedge or drop the claim
unless it maps to a LIKELY-or-better row above. The UNCONFIRMED entries can
still season tone/voice work as clearly-flagged speculative texture, per
`directives/verification-agent-protocol.md` — they cannot anchor a factual
claim in client-facing or published work.
