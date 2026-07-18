# Source Ledger — manus-ai-consulting

Every claim added or already present in `SKILL.md` / `genius.md`, labeled by
how well it is grounded in a file that can be opened and checked. VERIFIED =
a verbatim quote was located, by direct read, in the cited file during this
repair (2026-07-18). LIKELY = consistent with a real source but not
re-verified verbatim by this worker. UNCONFIRMED = no source file located;
treat as house-authored/illustrative until a primary transcript surfaces.

No `extractions/` directory exists for "manus" (checked: `ls extractions/ |
grep -i manus` → no hits). Ground truth for this repair is the
swarm-apex-2026-07-07 research brief, per the envelope's pointer.

## Anti-Patterns (new `## Anti-Patterns` section, genius.md)

| # | Claim | Label | Source | Notes |
|---|---|---|---|---|
| 1 | Peak Ji quote: "we do not divide by role... very cautious about adding more sub agents because communication is very hard" | VERIFIED | `_active/swarm-apex-2026-07-07/research/manus.md`, line 9 | Quote located verbatim in the local brief file by direct read. The brief itself tags this VERIFIED against a LangChain webinar + Recall card; this worker did not independently re-fetch the YouTube source, so the "VERIFIED" label here is inherited from the brief's own primary-source tag, not re-confirmed against the video by this pass. |
| 2 | KV-cache hit rate = "the single most important metric"; $0.30/MTok cached vs $3 uncached | VERIFIED | `manus.md`, lines 13-14 | Quote located verbatim. Brief tags this VERIFIED against manus.im/blog (primary). Not independently re-fetched by this worker. |
| 3 | "Failed actions and stack traces deliberately left in context... implicitly updates the model's internal beliefs" | VERIFIED | `manus.md`, line 17 | Quote located verbatim. Same manus.im/blog primary source, not independently re-fetched. |
| 4 | `todo.md` recitation as attention hack, "avoiding lost-in-the-middle goal drift across ~50 tool calls" | VERIFIED | `manus.md`, line 15 | Quote located verbatim. Same manus.im/blog primary source, not independently re-fetched. |
| 5 | Opaque credit burn: "400 credits on 4 Google Maps lookups, 1000 credits before first output, no real-time spend alerts, billing on failed runs" | VERIFIED (brief's tag) — secondary-sourced | `manus.md`, line 28 | Quote located verbatim. Brief itself sources this to review roundups (lindy.ai, allaboutai.com, metaflow.life) — secondary, not primary — while still tagging it VERIFIED at the brief level (consistent reviews). Flagged here as secondary-sourced so the distinction isn't lost downstream. |

`_active/swarm-apex-2026-07-07/research/manus.md` — confirmed non-empty,
`wc -c` = 5,141 bytes (checked this repair pass; rules out a false
"unrecoverable/0-byte" claim).

## How to Use This Skill / recognition-test line (genius.md, new section)

| Claim | Label | Source |
|---|---|---|
| "Peak Ji ... chief scientist" title, LangChain webinar attribution | LIKELY | `manus.md` header + "Agent Loop Mechanics" § attributes this to a Recall card + LangChain webinar (`youtube.com/watch?v=6_BcCthVvb8`). Title/attribution not independently re-verified against the video by this worker — inherited from the brief. |
| "three agents total... general executor, planner, knowledge-management module" | VERIFIED | `manus.md`, line 9, same Peak Ji quote as Anti-Pattern #1 |

## Pre-existing genius.md content (not modified, not newly sourced this pass)

| Claim | Label | Notes |
|---|---|---|
| Self-Executing Deliverable Architecture (Maintenance Manual Layer, Decision Fork Map, Implementation Verification Protocol) | UNCONFIRMED | No source file found anywhere in the repo (`find . -iname "*manus*"` and `extractions/` search both came up empty for a primary transcript). Reads as house-authored methodology, not a Manus.ai quote. Left as-is (additive-first boundary) but not counted toward `anti_patterns_sourced`. |
| Hall of Fame Exemplars 1 & 2 (retail inventory, healthcare governance) + Anti-Exemplar (generic AI strategy doc) | UNCONFIRMED | Same — no locatable source. Illustrative/synthetic content, not attributed to a real Manus.ai deliverable or client engagement. Left as-is; not used as anti-pattern anchors in this repair since they carry no verifiable source. |
| Signature Moves (4 items) | UNCONFIRMED | Same — no locatable source. |
| Expert-Specific Quality Rubric | UNCONFIRMED | Same — house-authored rubric, not a Manus.ai artifact. |
| SKILL.md "$300,000 McKinsey-level insights" / "$300K insights at 1/100th the cost" framing | UNCONFIRMED | No pricing/benchmark source found. Marketing framing inherited from the skill's original authoring pass (note: current `SKILL.md` line 13 is a truncated sentence — "**Core Principle**: AI doesn't replace consultants—it enables $" — a pre-existing defect, not introduced by this repair; out of scope for the 3 assigned failing checks, flagged here for a future pass). |

## Files consulted this repair (with sizes)

```
_active/swarm-apex-2026-07-07/research/manus.md    5,141 bytes
skills/manus-ai-consulting/SKILL.md                 (read, not modified this pass)
skills/manus-ai-consulting/SKILL.md.old             (read for diff context, not modified)
skills/manus-ai-consulting/genius.md                (read; modified copy in this output dir)
skills/manus-ai-consulting/workflows/*.md           (4 files, read — all already carry Output Contract + Quality Gate, no change needed)
skills/ben-watkins-storytelling/genius.md            lines 1-20 read as house-style model for the Model Calibration section
skills/luke-iha-creative-strategy/references/source-ledger.md   read as format model for this ledger
```

`extractions/` directory: `ls extractions/ | grep -i manus` → no results.
No expert-specific transcript exists for Manus.ai in this repo; the
swarm-apex research brief is the only primary-sourced ground truth
available, per the envelope's explicit pointer.
