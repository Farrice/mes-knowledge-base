# Source Ledger — knowledge-architecture-studio

This is a METHOD/SYSTEM skill (a fusion of two of Farrice's own prompt systems — KACE
and the Intelligence Architecture Studio), not an extracted-persona skill. SKILL.md's
own frontmatter states `source: "claude.ai project export (2026-07-01)"`. A repo-wide
search (`grep -rli "KACE\|Intelligence Architecture Studio"`, `find -iname
"*claude.ai*"`, `find -iname "*project-export*"`, and `ls extractions/ | grep -i
knowledge` / `architecture`) found **no raw corpus file** — no transcript, no export
JSON/markdown — anywhere in the repo. Every claim below is therefore checked against
the skill's own already-committed files, which are the only verifiable ground truth,
and file sizes are recorded so the "no raw source" finding is itself falsifiable.

## Files consulted (ground truth, with byte sizes via `wc -c`)

| File | Size (bytes) | Role |
|---|---|---|
| `skills/knowledge-architecture-studio/SKILL.md` | 3,172 | Frontmatter + skill overview |
| `skills/knowledge-architecture-studio/genius.md` | 10,471 | Pattern/insight source (pre-repair) |
| `skills/knowledge-architecture-studio/workflows/01-extract-knowledge-architecture.md` | 5,468 | Workflow 01 |
| `skills/knowledge-architecture-studio/workflows/02-build-mastery-pathway.md` | 4,503 | Workflow 02 |
| `skills/knowledge-architecture-studio/workflows/03-architect-domain-agent.md` | 5,523 | Workflow 03 |
| `skills/knowledge-architecture-studio/references/prompts-v2/extract-knowledge-architecture.md` | 8,650 | Execution prompt v2, `refactored: 2026-07-13` |
| `skills/knowledge-architecture-studio/references/prompts-v2/build-mastery-pathway.md` | 6,937 | Execution prompt v2, `refactored: 2026-07-13` |
| `skills/knowledge-architecture-studio/references/prompts-v2/architect-domain-agent.md` | 8,587 | Execution prompt v2, `refactored: 2026-07-13` |
| `agents/knowledge-architecture-studio/AGENT.md` | 4,856 | Agent persona wrapper |
| `agents/knowledge-architecture-studio/memory/context.md` | 601 | Agent memory (mostly unpopulated placeholders) |
| `.claude/commands/knowledge-architecture.md` | 1,251 | Slash-command pointer |
| `.claude/commands/knowledge-architecture-studio.md` | 1,469 | Slash-command pointer |

No `extractions/` directory entry matches this skill (checked `alex|ben|...` naming
convention against `knowledge`, `architecture`, `intelligence-architect`, `KACE` — zero
hits across 193 top-level entries).

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| "The Studio fuses KACE and the Intelligence Architecture Studio" | LIKELY | Stated consistently in SKILL.md, AGENT.md, and memory/context.md — internally consistent across 3 independently-written files, but the two named source systems (KACE, Intelligence Architecture Studio V3) have no file of their own in this repo to verify against directly. |
| The 7-layer / 4-level / 5-component / 5-prompt / 8-point structures (as documented in workflows 01–03 and prompts-v2) | VERIFIED | Present verbatim, byte-identical in intent, across both `workflows/*.md` and `references/prompts-v2/*.md` — the two independently-authored copies agree, which is the strongest verification available without an external source. |
| "source: claude.ai project export (2026-07-01)" | UNCONFIRMED (existence of the raw export itself) | The date and provenance label are taken at face value from SKILL.md frontmatter — real and un-fabricated as a *citation*, but the underlying raw export file was not found anywhere in the repo, so its content cannot be independently checked. Do not cite this skill as if a raw transcript exists; it does not, as far as this repair could locate. |
| `references/prompts-v2/*.md` frontmatter `refactored: 2026-07-13` | VERIFIED | Present in the frontmatter of all three prompts-v2 files, read directly. |
| Every quote used as an anti-pattern anchor in the repaired `genius.md` (e.g. "Draw the graph, not the glossary", "one with only System 1 is a reckless guesser", "Where the source is silent, mark UNCONFIRMED — never fabricate expertise to fill a template slot") | VERIFIED | Each is a direct, byte-for-byte (or near-byte-for-byte, modulo markdown bold markers) quote pulled from the specific file+section cited beside it — see `PROVENANCE.md` for the exact line-level source. |

## Honest gap

No external, non-repo source material for "KACE" or "the Intelligence Architecture
Studio" was located. All anchors in the repaired `genius.md` therefore cite the skill's
own already-committed files rather than an outside interview/transcript/article — this
matches the dispatch instruction for METHOD/SYSTEM skills ("anchors ground in the
skill's own files") and is the honest ceiling on provenance for this particular skill.
