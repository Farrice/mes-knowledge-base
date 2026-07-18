# Source Ledger — writing-depth-layer

Claim-by-claim provenance for every anchor added or relied on during the Wave 3 Lane 4 Batch 18 heartbeat repair (2026-07-17). `writing-depth-layer` is a system/craft composition skill — it owns no craft of its own, so "ground truth" here is (a) the actual extraction transcript behind its one directly-quoted source (Lamott + Allen), (b) this repo's own dated finalize/session records, and (c) the skill's own reference files and the 13 owner-skill paths it routes to. Every quote below was located with a direct file read/grep before being cited; none is asserted from memory.

## Claims from genius.md — VERIFIED

| # | Claim / quote used as anchor | Source (file + location) | Status |
|---|---|---|---|
| 1 | "writer is actually more interested in the sentence than the content" | `extractions/anne-lamott-neal-allen-really-real/source.clean.txt`, timestamp `[00:02:46.080]` (line 56) | VERIFIED — read directly, exact match |
| 2 | "Literary showing-off is contrasted with story and care." | `extractions/anne-lamott-neal-allen-really-real/evidence-ledger.md`, row `00:30:54-00:31:25` | VERIFIED — read directly, exact match |
| 3 | "Clarity is a courtesy. Compression can be care, not coldness." | `extractions/anne-lamott-neal-allen-really-real/evidence-ledger.md`, row `00:24:06-00:26:13` | VERIFIED — read directly, exact match |
| 4 | "The goal is not dumping emotion." (mechanic #2, "Realness Is Not Rawness") | `extractions/anne-lamott-neal-allen-really-real/mechanics.md`, section 2 | VERIFIED — read directly, exact match |
| 5 | "A sentence is alive when it earns the next sentence." | `extractions/anne-lamott-neal-allen-really-real/evidence-ledger.md` row `00:02:07-00:03:27` / `mechanics.md` section 1 | VERIFIED — read directly, exact match |
| 6 | "'Comprehensive' output = system failure regardless of score." | `CLAUDE.md`, line 50 (Chain preamble) | VERIFIED — read directly, exact match |
| 7 | Writing Depth Layer finalize entry, 2026-06-14 02:19, composite:7.25, status "Needs Improvement" | `knowledge/log.md`, line 188 | VERIFIED — read directly, exact match |
| 8 | Lamott-Allen technical sentence-craft expansion described as a "36 rules module" / "36-rules module" | `knowledge/log.md`, lines 186 and 188 (2026-06-14 02:12 / 02:19 entries) | VERIFIED — read directly, exact match |
| 9 | "Diagnose before treating. Never refine on a misdiagnosed draft. A wrong weakest-link call sends the wrong owner." | `skills/writing-depth-layer/references/depth-deficit-taxonomy.md`, line 246 | VERIFIED — read directly, exact match |
| 10 | 13 owner-skill paths cited in the Routing Map (§4) exist on disk with a `genius.md` (Hawley, Roth, Connelly, Cole, Lamott-Allen, Lamott-craft, Fareed, Sutherland, Lara Acosta, Diandra Escobar, Kallaway, Pressfield, ghostwriting-voice-engine) | `skills/<each-path>/genius.md` — spot-checked with `ls`/`test -f` this session | VERIFIED — all 13 confirmed present |
| 11 | 12 workflow files in `skills/writing-depth-layer/workflows/` each carry an Output Schema/Contract + Quality Gate section | `skills/writing-depth-layer/workflows/*.md` | VERIFIED — pre-existing PASS confirmed by `skill_auditor.py` heartbeat (`workflow_contracts` check), unchanged by this repair |

## Pre-existing claim flagged for honesty (not fabricated by this repair, but not exact either) — LIKELY

| # | Claim | What was checked | Status |
|---|---|---|---|
| 12 | SKILL.md line 31 / genius.md §1 quote the source (Lamott + Allen) as saying a real writer **"cares more about the sentence than the content."** | The actual transcript line is: *"writer is actually more interested in the sentence than the content"* (`extractions/anne-lamott-neal-allen-really-real/source.clean.txt`, `[00:02:46.080]`) — close paraphrase, not a verbatim match ("cares more about" vs. "is actually more interested in") | LIKELY — the underlying claim (a real writer prioritizes sentence over content) is real and sourced; the exact wording in quotation marks is a paraphrase, not a verbatim transcript quote. Pre-existing content, out of this repair's scope to rewrite (additive-first boundary) — flagged here so it is never mistaken for a checked verbatim anchor. The verbatim alternative (claim #1 above) is what this repair's new anchors cite. |

## Claims scoped out of this repair — UNCONFIRMED

| # | Claim | Status |
|---|---|---|
| 13 | Any specific reader-outcome or performance number for a `/deepen`-treated draft (e.g., engagement lift, completion rate) | UNCONFIRMED — no such claim appears in genius.md/SKILL.md; noted here only to confirm none was invented during this repair. If a future pass adds a performance claim, it must carry its own anchor. |
| 14 | Whether the 12 `/depth-*` workflows have been run end-to-end against a real draft outside the 2026-06-14 finalize note (which scored the initial build "Needs Improvement," not "Keep") | UNCONFIRMED — knowledge/log.md shows the skill's only finalize record scored 7.25/"Needs Improvement"; no later "Keep"-status finalize for this skill was found in `knowledge/log.md` during this repair's search window. Surfaced, not resolved — a future finalize pass should re-score. |

## Search discipline followed

Per the batch envelope: searched local repo first (`git log --follow`, `knowledge/log.md`, `.agent/performance-log.jsonl`, `extractions/` filtered for `lamott`/`allen`) before concluding any absence. Local sources were sufficient — no claim in this repair required scanning `_archive/claude-export-2026-07-01.tar.gz`, so it was not opened. `writing-depth-layer` has no dedicated `extractions/` folder of its own (it is a composition layer, not a named-expert extraction); its one direct-quote source is the `anne-lamott-neal-allen-really-real` extraction it composes, used above.
