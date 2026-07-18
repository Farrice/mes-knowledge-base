# Source Ledger — steven-kotler-flow-performance

Every claim/quote used in `genius.md` and `SKILL.md`, labeled VERIFIED / LIKELY / UNCONFIRMED.
Ground truth for this repair: no `extractions/` directory matches "kotler" (checked
2026-07-18: `ls extractions/ | grep -i kotler` returns nothing). Source material was
recovered from `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed
via `wc -c`) by a per-member content scan (Python `tarfile`, 7,728 members scanned,
7 members matched "kotler" case-insensitive). Six of those members are normalized
transcripts of Kotler interviews/talks; extracted copies used for this repair live at
`.tmp/wave3-lane4-b16/scratch/kotler_sources/` (worker scratch, not part of the skill).

## Primary sources (archive members)

| Member (in `_archive/claude-export-2026-07-01.tar.gz`) | Title | Captured | Size (bytes, `wc -c`) |
|---|---|---|---|
| `claude-export/normalized/conversations/8338117f-f0a5-4760-bc80-b3b6fee81822.md` | "Fresh-Steven Kotler: The science of effortlessness: How to activate flow" | 2025-06-25 | 181,969 |
| `claude-export/normalized/conversations/7c705b11-9e4c-43a3-9ef7-2e361e6ade05.md` | "Steven Kotler: The science of effortlessness: How to activate flow" (same talk, second extraction pass) | 2025-07-09 | 89,672 |
| `claude-export/normalized/conversations/15e19af2-92d6-4954-bc5e-6bfb16ece900.md` | "Coach Fresh & (Flow State Coach) Achieve Peak Performance, Find FLOW & Do The Impossible \| Steven Kotler" | 2025-07-10 | 144,338 |
| `claude-export/normalized/conversations/b8e5e232-4cf9-432a-922c-74e40c26dcbf.md` | "Achieve Peak Creativity: Merging Flow States with AI Technology w/ Steven Kotler" | 2025-07-10 | 173,235 |
| `claude-export/normalized/conversations/d844ffc0-8133-4dee-a383-8477dc181a4e.md` | "Pt2. Achieve Peak Creativity: Merging Flow States with AI Technology w/ Steven Kotler" | 2025-07-09 | 175,248 |
| `claude-export/normalized/conversations/73de793e-4ba7-40f9-9561-19ce250bb383.md` | "Advanced code extraction protocol" — incidental single "Kotler" mention, unrelated content; NOT used as a source | 2025-10-12 | 28,688 |

Note: "Captured" is the export's `created:` timestamp for the normalized conversation
record (i.e., when the transcript was ingested into claude.ai), not necessarily the
original video's air date — labeled as such throughout to avoid overclaiming.

## Claim-by-claim

| Claim / quote (as used in genius.md or SKILL.md) | Label | Source |
|---|---|---|
| "an optimal State of Consciousness where we feel our best and we perform our best" (SKILL.md paraphrases this as "an optimized state of consciousness...") | LIKELY | `15e19af2-...md`, 8:16-8:20. SKILL.md's word "optimized" is a paraphrase of the transcript's "optimal" — close but not verbatim; flagged LIKELY rather than VERIFIED because the exact adjective differs. |
| "Psychology... they're metaphor, they're great metaphors... but there's still metaphor" | VERIFIED | `8338117f-...md`, 0:51-0:57 (identical passage also in `7c705b11-...md`). |
| "what works for me will work for you" / "what works for you probably isn't gonna work for me" | VERIFIED | `8338117f-...md`, 1:20-1:43. |
| Self-consciousness / ski body-position story ("How did I look?" → switched metric to speed → "flow became almost automatic") | VERIFIED | `8338117f-...md`, 35:48-37:04 (identical in `7c705b11-...md`). |
| "it can take 'em 15 minutes to get back into flow, if they can get back in at all" | VERIFIED | `8338117f-...md`, 33:53-33:58 (identical in `7c705b11-...md`). |
| "Type A types, they'll take on challenges that are 10%, 20%, 30% greater... simply for the thrill of it" | VERIFIED | `7c705b11-...md`, 20:23-20:51 (identical in `8338117f-...md`). |
| "you need to earn enough money to pay your bills and have a little leftover for fun. It's not a lot more, right?" | VERIFIED | `7c705b11-...md`, 23:45-23:52 (identical in `8338117f-...md`). |
| "transient hypofrontality... the temporary deactivation of the prefrontal cortex" | VERIFIED | `8338117f-...md`, 34:40-34:48 (identical in `7c705b11-...md`). |
| Motivation stack sequence (extrinsic → curiosity → passion → purpose → autonomy → mastery); "farther, faster, with a lot less fuss" | LIKELY | Consistent with `7c705b11-...md` / `8338117f-...md` motivation-stack discussion (curiosity "focus for free," passion, purpose/pro-social chemicals sections); exact phrase "farther, faster, with a lot less fuss" not independently re-verified line-by-line in this repair pass — pre-existing skill content, not re-audited word-for-word. |
| Learning +240-500%, creativity +400-700%, productivity ~+500% (McKinsey self-report) | UNCONFIRMED | Statistic block pre-dates this repair and is not among the "kotler" archive hits reviewed here. Flagged UNCONFIRMED — this repair did not locate the specific figures verbatim in the recovered transcripts (McKinsey study is mentioned in the source material's broader flow literature but the exact percentages were not independently re-traced to a transcript line in this pass). Do not present as freshly verified; treat as pre-existing skill content pending a dedicated verification pass. |
| Bannister effect (sub-four-minute mile, record fell within a month, teenagers within five years) | LIKELY | Referenced in the "science of effortlessness" transcripts (`grep -l -i bannister` hits both `7c705b11-...md` and `8338117f-...md`); the specific "within five years teenagers had done it" clause was not individually re-quoted verbatim in this pass — treat the core anecdote as sourced, the precise numeric tail as LIKELY pending closer line-check. |
| Camp Pendleton / surfing + talk therapy PTSD claim | UNCONFIRMED | `grep -l -i pendleton` confirms Pendleton is discussed in both "science of effortlessness" transcripts, but this repair pass did not extract and verify the exact surfing/PTSD claim verbatim — flagged UNCONFIRMED rather than assumed correct. |
| Agent/AGENT.md and workflow files (01-03) | N/A | Pre-existing skill scaffolding, not sourced quotes — not re-verified in this pass; unchanged by this repair. |

## Repair-pass scope note

This ledger covers the claims touched by the 2026-07-18 heartbeat repair (the new
Anti-Patterns section in `genius.md` and the recognition-test line). It does NOT
re-verify every pre-existing statistic in `SKILL.md`/`genius.md` line-by-line — those
carry LIKELY/UNCONFIRMED labels above where this pass could not independently
re-trace them to a transcript line, per the "no invented provenance" rule. A deeper
statistic-by-statistic re-verification (McKinsey figures, Bannister's exact five-year
claim, Camp Pendleton specifics) is flagged as follow-up work, not silently assumed.
