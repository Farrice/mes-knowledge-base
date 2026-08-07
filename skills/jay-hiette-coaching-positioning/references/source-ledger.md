# Jay Hiette Coaching Positioning — Source Ledger

Ground truth for `jay-hiette-coaching-positioning` is two claude.ai extraction conversations, each built from a full verbatim YouTube transcript (via Merlin AI transcription) pasted as a human message. `agents/jay-hiette/memory/context.md` already names both videos; this repair located, extracted, and re-read the raw transcripts to verify every quote used in `genius.md`.

## Primary Source Corpus

| Source | Claimed capture date | Where found | Size | Label |
|---|---|---|---|---|
| `_archive/claude-export-2026-07-01.tar.gz` (full claude.ai export archive) | Archive created 2026-07-01 | Repo root `_archive/` | 332,779,255 bytes (confirmed `ls -la`, 2026-07-17) | VERIFIED to exist |
| Conversation `8e18a4b6-fae7-4f41-9fe5-133a1613b3a1.md` — "Jay Hiette \| Exactly How I Built a $200k Per Year (Profit) Consulting Business \| Online Coaching Mastery" (YouTube transcript via Merlin AI, `youtube.com/watch?v=_dmWrCvEuTQ`) | Pasted into claude.ai 2026-02-04T05:49:07Z | `claude-export/normalized/conversations/8e18a4b6-...md` inside the tarball; also indexed in `_active/claude-export/index.json` | 57,097 chars (per index.json `char_count`); extracted copy = 58,164 bytes (`wc -c`, matches within markdown-frontmatter overhead) | VERIFIED — extracted and read in full this repair (2026-07-17) |
| Conversation `a54b5e3f-2b1a-4dca-87fd-272df45486a6.md` — "Jay Hiette \| Why Identity-Led Content Is Taking Over \| Identity-Led Content Mastery" (YouTube transcript via Merlin AI, `youtube.com/watch?v=ENNzeF8K6fk`) | Pasted into claude.ai 2026-02-22T11:53:26Z | Same tarball path pattern; indexed in `_active/claude-export/index.json` | 52,750 chars (index.json); extracted copy = 53,884 bytes | VERIFIED — extracted and read in full this repair (2026-07-17) |

Both conversations follow the same shape: a single long human turn pastes the raw Merlin AI transcript verbatim (one unbroken paragraph, ~3,500 and ~2,800 words respectively), followed by assistant turns running an MES 3.0 extraction protocol that produced the skill's original `genius.md` patterns. The transcript text itself — not the assistant's extraction commentary — is the primary source for every direct quote in this repair.

## Claim-by-Claim (anti-patterns and quotes added in this repair)

| Claim / quote | In-repo anchor | Label |
|---|---|---|
| "most gurus on the internet will tell you the complete opposite. They'll tell you to post more organic content or you're not trying hard enough or you're not good enough at what you do, which is complete BS" | `8e18a4b6-...md`, human turn 2026-02-04T05:49:07Z (single-paragraph transcript block) | VERIFIED — verbatim, confirmed by direct re-read of the extracted conversation file |
| "he had 800,000 followers and he just wasn't converting clients... Yip... had a few hundred followers and was able to make €8,000 in a few weeks" | Same source | VERIFIED — verbatim |
| "When you call out a problem, gaining body fat, lack of leads, people just scroll because they don't even know if they own that problem yet... Instead, describe the moment that they can't ignore. Every time you walk in the kitchen, you overeat" | Same source | VERIFIED — verbatim |
| "we're not running ads directly to a book call, etc. We're just simply getting people to follow you" | Same source | VERIFIED — verbatim |
| "the key thing you want to focus on is getting clear with the foundations and the message before you integrate the ads, the scaling, and all of the other steps" | Same source | VERIFIED — verbatim |
| "You copy others to try to fit in. And when you finish this video, you will learn exactly how to stand out" | `a54b5e3f-...md`, human turn 2026-02-22T11:53:26Z | VERIFIED — verbatim |
| Pre-existing genius.md quotes (optometrist/books analogy, "every time you walk in the kitchen, you overeat," IEL example "War Within Method," Yip/€8,000, Daniel $2-3K→$23K, Matus 290→23,000, "why it's important to fail in public") | `8e18a4b6-...md` and `a54b5e3f-...md`, both files | VERIFIED — all cross-checked against the raw transcript text during this repair; every one traces to the pasted transcript, none invented |
| "Anti-Nurture" Hidden Knowledge insight — "forcing them through a 90-day nurture sequence is negligence, not nurturing" | `genius.md` Hidden Knowledge section (pre-existing, not modified this repair) | UNCONFIRMED as a Jay verbatim line — the two-lane monetization structure (direct conversation vs. nano-offer ascension) IS verbatim in the transcript, but the "90-day negligence" framing is the original extraction's interpretive gloss, not a quote. Left in place (out of scope, additive-first boundary); flagged here for visibility rather than silently treated as sourced fact. |

## Absence Check (verified, not assumed)

- `ls extractions/ | grep -i hiette` → no output (run 2026-07-17). No file under `extractions/` matches this expert — confirmed by direct listing, not inferred.
- `grep -ril "hiette" _active/harness/codex-harvest-2026-06-11` → no output (run 2026-07-17) — codex-harvest does not contain Jay Hiette material.
- `grep -ril "hiette" _active/claude-export` → hits only in index/triage/census JSON metadata files (titles, routing pointers), not raw conversation content — those files were checked and confirmed to be indexes, not sources.
- `tar tzf _archive/claude-export-2026-07-01.tar.gz | grep -i hiette` → no filename hits (conversation files are named by UUID, not by title), so the two source conversations were located via `_active/claude-export/index.json` (which maps UUID → title) rather than by filename search, then extracted by exact path with `tar xzf ... -O <path>` and confirmed present by `wc -c` (58,164 and 53,884 bytes — non-empty, real content, not a 0-byte or truncated pull).

## Notes on This Repair

- Only the three failing heartbeat checks were addressed: `anti_patterns_sourced` (6 sourced anti-pattern bullets added to `genius.md`), `recognition_test` (Model Calibration section added to `genius.md`), `source_ledger` (this file).
- `verbatim_exemplars`, `named_entity_floor`, and `workflow_contracts` were already passing and were not touched.
- SKILL.md, the three workflow files, and the three `references/prompts-v2/*.md` files are unmodified — not included in this output directory (flat layout, changed files only).
