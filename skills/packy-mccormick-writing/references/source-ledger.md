# Source Ledger — packy-mccormick-writing

> Claim-by-claim audit for `genius.md` (repaired 2026-07-17/18, Wave 3 Lane 4 Batch 13).
> Every source below was opened and read directly (not assumed). Sizes recorded via `wc -c` / Python `tarfile` member `.size`.

## Source-Search Discipline (name-fragment method)

Ran per envelope instructions before writing any claim:

1. `ls extractions/ | grep -i packy` and `grep -i mccormick` — **zero hits**. No `extractions/packy-mccormick*` directory exists in this repo.
2. `find . -iname "*packy*"` / `*not-boring*` / `*notboring*` (excluding `skills/` and `.tmp/`) — found `agents/packy-mccormick/AGENT.md` + `memory/context.md` (persona files, not raw source) and `.claude/commands/packy-mccormick*.md` (routing pointers only).
3. SKILL.md frontmatter says `source: claude.ai export 2026-07-01`, pointing at `_archive/claude-export-2026-07-01.tar.gz`. Ran a **Python `tarfile` per-member scan** (`tarfile.open(...).getmembers()`, 7,728 total members) filtering names for `packy`/`mccormick`/`not-boring`/`notboring` — **zero name hits** (the archive stores conversations by UUID, not by title).
4. Cross-checked `_active/claude-export/index.json` (a 1,988,307-byte harvest index with per-conversation titles) for the string "packy"/"mccormick" — **2 hits**: two archived Claude conversations both titled a variant of *"Packy McCormick: A Tactical Masterclass in Online Writing"* (the David Perell "How I Write" interview transcript, pasted into Claude for analysis), with `md_path` pointers into the (now-purged, `.tmp/`-only) normalized-conversation cache.
5. The `md_path` files no longer exist on disk (`.tmp/` is gitignored and this harvest is from 2026-07-01), but their exact UUIDs (`98be524c-d84e-44aa-b1a9-85c81629088c`, `5335f577-bd49-4833-92f3-a6a09ee6c8b0`) were used as the second `tarfile` name-filter pass against `_archive/claude-export-2026-07-01.tar.gz` — **4 members matched** (2 real files + 2 macOS AppleDouble `._*` sidecar files), confirming the raw conversation markdown IS present inside the archive under `claude-export/normalized/conversations/<uuid>.md`.
6. Extracted both members with `tarfile.extractfile()` and read them in full.

This is the only ground-truth source recoverable for this skill. No "sources are absent" claim is made without the above direct-read chain — sizes recorded below, not asserted.

## Sources Consulted

| # | File | Size (bytes) | Status | Notes |
|---|------|---------------|--------|-------|
| 1 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/98be524c-d84e-44aa-b1a9-85c81629088c.md` | 116,734 (tar member `.size`, confirmed on extraction) | VERIFIED | David Perell "How I Write" interview transcript with Packy McCormick, conversation created 2025-05-05T05:35:28Z per `_active/claude-export/index.json`. Read in full via Python `tarfile.extractfile()`. |
| 2 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/5335f577-bd49-4833-92f3-a6a09ee6c8b0.md` | 121,187 (tar member `.size`, confirmed on extraction) | VERIFIED | Second archived capture of the same interview, conversation created 2025-10-16T19:01:55Z per index.json. Contains the fullest inline timecodes (used for all Anti-Patterns anchors below). Read in full via Python `tarfile.extractfile()`. |
| 3 | `_active/claude-export/index.json` | 1,988,307 | VERIFIED | Harvest index; queried programmatically (recursive string walk) for "packy"/"mccormick" to locate source #1 and #2's conversation IDs, titles, and creation dates. |
| 4 | `skills/packy-mccormick-writing/genius.md` (pre-repair) | 14,781 | VERIFIED | Existing compiled genius file — all 9 Genius Patterns and 5 Hidden Knowledge quotes cross-checked against sources #1/#2 and confirmed verbatim (see spot-checks below). Preserved unchanged; only additive sections appended. |
| 5 | `skills/packy-mccormick-writing/SKILL.md` | 4,159 | VERIFIED | Read for consistency; not modified (recognition-test and anti-pattern gaps were both fixable inside genius.md per envelope instructions). |
| 6 | `agents/packy-mccormick/AGENT.md` + `memory/context.md` | 5,129 + 460 | VERIFIED | Persona/routing file; read for corroboration of pattern names, not cited as an independent primary source. |
| 7 | `extractions/` (repo-wide) | n/a | UNCONFIRMED-absent, verified by direct listing | No `extractions/packy*` or `extractions/*mccormick*` or `extractions/*not-boring*` directory exists. Confirmed via `ls extractions/` (193 entries) + targeted `find`/`grep -rli` — zero matches. This is a verified absence, not an assumed one. |

## Verbatim Spot-Checks (pre-existing genius.md quotes vs. source #2)

Confirms the quotes already inside genius.md (which drove the passing `verbatim_exemplars` check) are genuinely sourced, not fabricated:

| Pre-existing genius.md quote | Found in source #2 at | Match |
|---|---|---|
| "It's like doing a maze — I go all the way back to the beginning and try again." | line 522, timestamp 21:27 | VERIFIED verbatim |
| "I'm not trying to make a statue, I just need marble." | line 757-759, timestamp ~37:xx | VERIFIED verbatim |
| "pretty bad editors" (ChatGPT/Claude) | lines 938-941, timestamp 40:41 | VERIFIED (genius.md paraphrases "ChatGPT and Anthropic and Claude are both pretty bad editors in different ways") |
| "is this idea dumb?" / caricature drift | lines 375-431, timestamps 15:01-17:23 | VERIFIED — spoken by Packy himself (confirmed the surrounding turn is his, not interviewer David Perell's, by reading the full exchange before attributing) |

## Claim-by-Claim Labels (new content added this repair)

| Claim / bullet | Label | Anchor |
|---|---|---|
| Model Calibration: "would Packy McCormick recognize this as..." test | N/A (framing device, not a factual claim) | Original phrasing, modeled on `skills/ben-watkins-storytelling/genius.md` structure per envelope instruction — not a quote |
| Model Calibration: "cost physics" name-check reference | VERIFIED | source #2, lines 408-429, timestamps 16:23-17:23 |
| Anti-Pattern: maze-restart quote (21:27) | VERIFIED | source #2, line 522 |
| Anti-Pattern: "pretty bad editors" (40:41) | VERIFIED | source #2, lines 940-941 |
| Anti-Pattern: qualifier-stuffing warning (41:50-42:06) | VERIFIED | source #2, lines 963-970 |
| Anti-Pattern: beta content quote (5:37-5:54) | VERIFIED | source #2, lines 160-166 |
| Anti-Pattern: "is this idea dumb?" (17:19-17:26) | VERIFIED | source #2, lines 429-431 |
| Anti-Pattern: "cost physics" attribution | VERIFIED | source #2, lines 408-429 |
| Anti-Pattern: spaced-repetition abandonment (77:34-77:40) | VERIFIED | source #2, lines 1741-1746 |
| Anti-Pattern: "good or is this company bad" (48:18-48:23) | VERIFIED | source #2, lines 1109-1116 |
| Anti-Pattern: 20-to-1 sponsorship selection ratio | VERIFIED | source #2, lines 1109-1111 ("there's 20 companies that want me to write one of those for every one that I do") |
| Anti-Pattern: paywall quote (45:12-45:16) | VERIFIED | source #2, lines 1037-1040 |
| Anti-Pattern: hyperbole/hooky quote (5:20-5:26) | VERIFIED | source #2, lines 5-8 of source #2 (opening section) |
| Conversation dates 2025-05-05 / 2025-10-16 | VERIFIED | `_active/claude-export/index.json`, `conversations[762]` and `conversations[2359]` `created` fields |

## Method

Name-fragment search only (`grep -i packy`, `grep -i mccormick`, `grep -i not-boring`), no punctuation assumptions. Both archived transcript files were opened with a Python script using `tarfile.extractfile()` and read in full via the Read tool before any quote was cited. No file or directory was declared absent without a direct listing/scan confirming it (extractions/ absence confirmed by `ls` + `grep -rli`; archive presence confirmed by two independent `tarfile` member scans — first by expert-name fragment, second by exact conversation UUID once the UUID was recovered from `index.json`). Every quote used in the new Anti-Patterns section and Model Calibration section was matched against the raw transcript text by line number before being written into genius.md.
