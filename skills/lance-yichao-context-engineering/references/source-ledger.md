# Source Ledger — lance-yichao-context-engineering

Repair pass, Wave 3 Lane 4 Batch 9. Ground-truth search performed this
session (name fragments, no punctuation): `yichao`, `lance`, `manus`,
`peak` — across `extractions/` (directory listing, zero matches),
`_archive/claude-export-2026-07-01.tar.gz` (Python `tarfile`, per-member
name scan, 7,728 members total, zero matches), and a repo-wide grep for
`Peak Ji`, `Yichao Ji`, `context rot`, `Lance Martin` outside this skill's
own files. **No raw interview transcript or primary extraction source for
either expert exists anywhere in this repo.** This is recorded honestly,
not assumed — see file sizes below for what was actually opened and read.

## Files consulted (size recorded, per envelope instruction)

| File | Size | Role |
|---|---|---|
| `_active/harness/swarm-apex-2026-07-07/research/manus.md` | 38 lines / 5,141 bytes | **Primary internal source used for repair.** A 2026-07-07 Sonnet deep-research brief on Manus's actual architecture, carrying its own claim-by-claim VERIFIED/LIKELY/UNCONFIRMED labels. Cites two external primaries directly: `manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus` and a LangChain webinar featuring Yichao "Peak" Ji (`youtube.com/watch?v=6_BcCthVvb8`). Read in full this session. |
| `skills/lance-yichao-context-engineering/references/genius-patterns.md` | 103 lines / 6,725 bytes | Pre-existing skill content (23 patterns). Not independently re-verified against a primary transcript this session — treated as LIKELY (consistent with widely-known public writing from both experts, per general model knowledge) except where corroborated below. |
| `skills/lance-yichao-context-engineering/references/hidden-knowledge.md` | 22 lines / 2,102 bytes | Pre-existing skill content (7 tacit-knowledge items). Same LIKELY treatment; Tacit Knowledge 7's "one-third of actions" figure specifically flagged UNCONFIRMED (see genius.md). |
| `skills/lance-yichao-context-engineering/SKILL.md.old` | 85 lines / 4,047 bytes | Pre-existing skill scaffold (v1.0.0). Internal artifact, not an external source. |
| `agents/lance-yichao/AGENT.md` | 39 lines / 1,954 bytes | Pre-existing agent persona file. Internal artifact, not an external source. |
| `extractions/` (directory) | 0 matching files | Confirmed empty for this expert — `ls extractions/ | grep -i yichao` and `| grep -i lance` both return nothing. |
| `_archive/claude-export-2026-07-01.tar.gz` | 7,728 members scanned | Python `tarfile.open().getmembers()`, filtered on name fragments `yichao`/`lance`/`manus`/`peak` (case-insensitive, no punctuation). Zero matches on any expert-specific source file. |

## Claim-by-claim labels

- **[VERIFIED]** — KV-cache hit-rate economics ($0.30/MTok cached vs $3 uncached, ~100:1 input:output ratio), append-only/byte-identical prompt-prefix discipline, deliberate retention of failed actions/stack traces, no dynamic tool removal (logit-masking instead), the Peak Ji "we do not divide by role" quote, Wide Research fan-out (100+ sub-agents, `submit result` schema-constrained decoding, Pro-tier $199/mo), GAIA-benchmark-vs-user-preference mismatch, credit-burn figures (400 credits / 4 Google Maps lookups, ~1,000 credits before first output). All traced to `_active/harness/swarm-apex-2026-07-07/research/manus.md`, itself citing manus.im primary + the LangChain webinar.
- **[LIKELY]** — The "128K-200K" pre-rot threshold language, the reversibility principle quote ("Almost every action in Manus is reversible..."), the persistent `todo.md`-as-special-event recitation mechanic. Corroborated in shape by the research brief but not opened against a raw primary transcript this session.
- **[UNCONFIRMED]** — The "one-third of agent actions were just updating the todo list" figure (Tacit Knowledge 7). Could not be re-located in any file in this repo this session. Left in place per the additive-first/no-deletion boundary, flagged inline in genius.md rather than presented as verified.
- **Everything else in `genius-patterns.md` / `hidden-knowledge.md`** not listed above (schema field names, three-layer action space, atomic-function philosophy, guardrail layering, collective feedback mining, line-based format preference, evaluation triad structure, memory-confirmation UX) is pre-existing skill content, internally consistent with the VERIFIED material above but not independently re-sourced against a primary transcript this session — treated as LIKELY / expert-consistent operationalization, not re-labeled VERIFIED.

## What this repair did NOT do

Did not fabricate a transcript, did not invent a date/quote/URL for any
claim, and did not relabel a pre-existing unsourced claim as VERIFIED
without a matching primary anchor. Where no anchor could be found, the
claim is marked UNCONFIRMED and left in place rather than silently
deleted or silently upgraded.
