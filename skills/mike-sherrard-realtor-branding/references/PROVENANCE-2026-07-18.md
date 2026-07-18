# PROVENANCE — mike-sherrard-realtor-branding repair pass (Wave 3 Lane 4 Batch 11)

## Source discovery (per SOURCE-SEARCH DISCIPLINE)

1. `ls extractions/ | grep -i sherrard` → no hits. No dedicated `extractions/mike-sherrard/` directory exists.
2. Name-fragment search without punctuation across the repo (`grep -rli "sherrard"`) surfaced
   `_active/claude-export/index.json`, `.../triage/triage-index.json`, `.../triage/heuristic-scores.json`,
   `.../harvest/census-full.json`, `.../harvest/gap3-input.json`, `.../harvest/census-input.json`.
3. `gap3-input.json` names the skill directly: `{"mode": "lane", "skill": "mike-sherrard-realtor-branding",
   "agent": "mike-sherrard", "mds": [".tmp/claude-export/normalized/conversations/327fae11-....md",
   ".tmp/claude-export/normalized/conversations/1804507d-....md"], "total": 2}` — exactly two source
   conversations, no more, no fewer.
4. Those `.tmp/` paths no longer exist on disk (normalized-conversation cache was cleaned up), so the two
   conversation IDs were located inside `_archive/claude-export-2026-07-01.tar.gz` via a
   `python3 tarfile` **per-member** scan (`tarfile.open(..., 'r:gz'); for m in t: ...`) matching on the
   raw conversation-ID substring — never a filename guess.
5. Both members found and extracted; **sizes recorded via `wc -c` after extraction, matching the
   `TarInfo.size` reported by the tarfile scan exactly** — 32,129 bytes and 42,523 bytes. Neither is
   0-byte or truncated. Both were opened and read in full this session before any claim was labeled.

## Anchor table

| Anchor ID | Repair-pass filename | Original tar member | Bytes | Title | Captured |
|---|---|---|---|---|---|
| S1 | `90pct-zero-leads.md` | `claude-export/normalized/conversations/1804507d-a25e-415b-916b-1b04822b03cd.md` | 32,129 | "Mike Sherrard: Why 90% of Realtors Get ZERO Leads From Social Media (How to Fix it FAST)" | 2025-06-20 |
| S2 | `hormozi-25k-branding.md` | `claude-export/normalized/conversations/327fae11-77f5-4cae-9a5a-6f10a08639e5.md` | 42,523 | "10-29-25 Mike Sherrard: REVEALING Alex Hormozi's $25,000 Personal Branding Strategy for Real Estate Agents" | 2025-10-29 |

Both are the raw Merlin-AI YouTube transcript plus the human's `/extract-deep` prompt turns and the
assistant's own meta-commentary about the extraction it was building. The actual MES-framework artifacts
the assistant claims to have created were **not captured** in the export (every artifact turn is the
stub "Viewing artifacts created via the Analysis Tool web feature preview isn't yet supported on
mobile"). This means the transcripts themselves — not a lost intermediate report — are the ground truth
for everything in `skills/mike-sherrard-realtor-branding/genius.md` and `SKILL.md`.

## Anchor → claim mapping

Full claim-by-claim table with per-pattern timestamps lives in
`references/source-ledger.md` in this output directory. Every new Anti-Pattern bullet added this
pass carries its own timestamp + filename + capture-date anchor inline on the same list-item line
(required by the batch envelope so the deterministic auditor's `_HB_SOURCE_ATTR_RE` regex — which only
scans the single list-item line, not surrounding prose — finds the anchor).

## What was NOT changed

- `SKILL.md` — already passing (`verbatim_exemplars`, `named_entity_floor`, `workflow_contracts` all
  PASS in the original audit); no edits needed or made.
- All three workflow files under `workflows/` — already passing `workflow_contracts`; untouched.
- All three files under `references/prompts-v2/` — untouched.
- The existing 10 Genius Patterns and 5 Hidden Knowledge entries in `genius.md` — preserved verbatim,
  not rewritten; only two new sections were inserted (Model Calibration, Anti-Patterns Sourced).
