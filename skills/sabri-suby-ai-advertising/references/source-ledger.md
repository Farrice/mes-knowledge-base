# Source Ledger — sabri-suby-ai-advertising

Every claim in this skill (SKILL.md, genius.md, references/) traced to its origin, labeled VERIFIED / LIKELY / UNCONFIRMED per `directives/verification-agent-protocol.md`. This ledger was built during the Wave 3 Lane 4 heartbeat repair (2026-07-18); it did not exist before.

## Source-search performed (2026-07-18)

- `ls extractions/ | grep -i sabri` and `grep -i suby` — **zero hits**. No `extractions/sabri-suby*` or `extractions/*suby*` directory exists (only an unrelated `extractions/sabrina-ramonov`, a different expert — flagged in `MEMORY.md` as a recurring name-collision risk).
- `find extractions -iname "*suby*" -o -iname "*sabri*"` — zero hits.
- Python `tarfile` scan of every `.tar.gz`/`.tar` archive in the repo (including `_archive/claude-export-2026-07-01.tar.gz`) for member names containing "suby" or "sabri" — zero hits.
- Repo-wide grep for "sabri suby", "kingkong", "sell like crazy" across `.md`/`.txt`/`.json` (excluding this skill and worktree mirrors) — no primary transcript, interview, or book excerpt found. Hits were limited to other skills/agents/commands that *reference* this skill by name, not source material.
- `research_outputs/ai_authority_architect_agents/sabri_suby.md` (2,590 bytes) exists but is **misfiled** — its content is a ghostwriter-fatigue market-pain dossier (unrelated topic), not Sabri Suby's own teaching; its own "Grounding Verification" addendum (2026-06-02) already flags its original quotes as `[MODELED]`/unsourced. Not used as a source here.
- `agents/sabri-suby/AGENT.md` (79 lines) — restates the same unattributed claims as SKILL.md (King Kong, $7.8B+ revenue). No independent provenance; itself downstream of this skill.
- `skills/sabri-suby-ai-advertising/SKILL.md.old` (109 lines) — legacy version, same unattributed pattern content, no citations.
- `skills/sabri-suby-ai-advertising/LICENSE.txt` — MIT license boilerplate, no content provenance.

**Conclusion**: no primary source file (transcript, interview, podcast, book excerpt) for Sabri Suby exists anywhere in this repository. All pattern/insight/quote content in `genius.md` and `references/genius-patterns.md` + `references/hidden-knowledge.md` pre-dates this repair with unknown original derivation. Per the Wave 3 hard rule ("a claim that sources are ABSENT is itself a provenance claim"), this conclusion is recorded here as the result of the search above, not asserted without it.

## Claim-by-claim labels

| Claim | Location | Label | Note |
|---|---|---|---|
| Sabri Suby is founder of King Kong; "$7.8B+ in client revenue" | SKILL.md L12, `agents/sabri-suby/AGENT.md` L10 | UNCONFIRMED | Publicly-associated facts (King Kong agency, author of *Sell Like Crazy*) are widely known in marketing-industry general knowledge, but no source file in this repo cites a URL, date, or document establishing the specific "$7.8B+" figure — treat as UNCONFIRMED until a dated source is attached. |
| "We don't write ads, we assemble ads" | `references/hidden-knowledge.md` §6 | UNCONFIRMED | No locatable primary-source file. Quote pre-dates this repair. |
| 15 Genius Patterns (Inverse Competition, Raging River, Bleeding Neck, Forum Foraging, Revenue Indicator Stack, Shop The Competition, Weak Copy Detection, Side-by-Side Test, Consumption Precedes Conversion, Doesn't Look Like An Ad, News/Gossip/Intrigue, Three-Element Formula, Identity Trigger, Objection Anticipation, Small Batch Testing) | `genius.md`, `references/genius-patterns.md` | UNCONFIRMED | Methodology framework of unknown original derivation; internally consistent with direct-response marketing practice generally, but not traceable to a specific Suby transcript/interview/book page in this repo. |
| 7 Hidden Knowledge insights | `genius.md`, `references/hidden-knowledge.md` | UNCONFIRMED | Same gap as above. |
| Hall of Fame Exemplars ("Local Hero" ad, "Bleeding Neck" landing page, Anti-Exemplar) | `genius.md` | UNCONFIRMED (labeled as illustrative) | These are constructed teaching examples, not claimed as verbatim Suby output — no change needed to their framing, only to explicit labeling here. |
| Evolved Pattern "Defensive Permeability Calibration," added 2026-04-09, Evolution Cycle 1, KEPT | `genius.md` Evolution Log | VERIFIED (as an artifact of this file) / UNCONFIRMED (as a Suby attribution) | The dated evolution-log row is a real, present artifact of this skill's own evolution history — that much is VERIFIED by direct inspection. Whether the underlying persuasion-intensity insight is actually Suby's is UNCONFIRMED for the same reason as everything above. |
| 4 workflow files (Output Schema + Quality Gate) | `workflows/*.md` | LIKELY | Structurally sound, house-style-consistent with other passing skills; not itself a factual claim requiring source verification. |

## What would upgrade these to VERIFIED

A primary source file — full or partial transcript of a Sabri Suby interview/podcast/course, a King Kong blog post with URL and access date, or an excerpt from *Sell Like Crazy* with page reference — placed under `extractions/sabri-suby/` and cited by file + location in a future pass. None was available during this repair; per the Wave 3 hard rules, no anchor was fabricated in its absence.
