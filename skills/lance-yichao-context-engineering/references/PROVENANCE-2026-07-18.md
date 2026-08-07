# PROVENANCE — lance-yichao-context-engineering repair

Anchor → source file + location. All anchors below point to files actually
opened and read this session; sizes recorded in `references/source-ledger.md`.

| Anchor text (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "we do not divide by role... communication is very hard" (Peak Ji quote) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 9 |
| "$0.30/MTok vs $3 uncached — 10x gap drives every decision" / ~100:1 ratio | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 13 |
| "strictly append-only context with deterministic JSON serialization" | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 14 |
| Failed actions/stack traces left in context deliberately | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 17 |
| Tools not dynamically removed; logit-masking instead | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 17 |
| Wide Research: 100+ sub-agents, `submit result` schema-constrained decoding, Pro-tier $199/mo | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 24 |
| GAIA benchmark vs. user-preference mismatch | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 27 (roundup) / general LIKELY framing in brief |
| Credit burn: 400 credits / 4 Google Maps lookups, ~1,000 credits before first output | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 28 |
| `todo.md` as persistent, re-appended "special event" | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | line 10 |
| "Almost every action in Manus is reversible if you can offload it to the file system or external state." | `skills/lance-yichao-context-engineering/references/genius-patterns.md` (Pattern 4, pre-existing) | corroborated in shape by `_active/harness/swarm-apex-2026-07-07/research/manus.md` line 16 |
| "128K to 200K" pre-rot threshold | `skills/lance-yichao-context-engineering/references/genius-patterns.md` (Pattern 2) / `hidden-knowledge.md` (Tacit 1), pre-existing | not independently re-verified against a primary transcript this session; LIKELY |
| "one-third of agent actions were just updating the todo list" | none found | searched `_active/harness/swarm-apex-2026-07-07/research/manus.md`, repo-wide grep for "one-third", `extractions/`, claude-export tarball — no match. UNCONFIRMED, left in place, flagged inline. |
| No `extractions/` source dir for this expert | `extractions/` directory listing | `ls extractions/ \| grep -i yichao` and `\| grep -i lance` — empty |
| No expert source in claude-export archive | `_archive/claude-export-2026-07-01.tar.gz` | Python `tarfile.getmembers()`, 7,728 members, name-fragment scan (yichao/lance/manus/peak) — zero matches |

## Illustrative (non-provenance) additions

A small number of implementation-guidance sentences were added to thin
pattern sections (Patterns 6, 15, 21) that are explicitly framed as
operationalization/illustration — e.g. "a 90-day-mature deployment" for
Pattern 21's guardrail decay. These are NOT attributed to Lance Martin or
Yichao Ji as quotes or verified facts; they carry no VERIFIED/LIKELY label
because they aren't claims about the experts at all, just worked examples
of how to apply the pattern. Flagged here for the adversarial verifier so
they aren't mistaken for provenance claims.
