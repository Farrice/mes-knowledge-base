# Source Ledger — deya-business-systems

## Sources Consulted

1. **Primary — 4 claude.ai export conversations**, recovered from `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes on disk; `tar -tzf` confirms 3,864 members). Filename search for "deya" against the tarball's file listing returns **zero** hits — conversations are stored by UUID, not by subject — so a naive `ls`/`tar -tzf` grep would wrongly conclude the source is absent. Content-level search (`tar -xzOf ... | grep -a -i "deya"`, then a full extraction of `claude-export/normalized/conversations/` — 272MB, 3,850 files) surfaced 18 conversation files that mention Deya. Four were read in full or near-full and anchor every claim below:
   - `d81c6e71-fc59-45d2-a618-45a889a71e89.md` — "💎 🧑🏽‍💻 12-14-15 Deya \| the 1-page business plan that made me $200K+ in 2024" — **77,564 bytes** — captured 2025-12-05T19:25 — contains the full YouTube transcript (source video credited in-file to `watch?v=ekpA_Ya1DCg`, via Merlin AI transcript tool). This is the primary source for the entire skill; the SKILL.md line `source: claude.ai export 2026-07-01` refers to this archive.
   - `fba00784-27ed-400b-9798-5914495cbac4.md` — "💎💎💰 Deya \| Businesses I Would Start in 2026 (If I Had to Start Over)" — **50,384 bytes** — captured 2025-12-20T15:31
   - `1037ef70-d002-45e7-a8bf-627970244fdc.md` — "💎🧑🏽‍💻💡 12-9-25 Deya: Best & Worst Online Businesses to Start in 2026" — **79,108 bytes** — captured 2025-12-05T17:45
   - `a819015f-b9dd-4ecb-a218-731847ee4b86.md` — "💎🧑🏽‍💻 12-9-25 Deya: how to start a $100K online business in 2026" — **68,202 bytes** — captured 2025-12-05T18:42
   - The remaining 14 Deya-tagged files are follow-on "crown jewel prompt" derivative conversations (Farrice building AI prompts on top of the extraction) — checked for additional verbatim Deya quotes, none found beyond what's captured below; their content is meta-commentary about prompt engineering, not new source material.
2. **`extractions/`** — checked (`ls extractions/ | grep -i deya`): zero results. No dedicated Deya extraction file exists in this directory.
3. **`_active/codex-harvest-2026-06-11/extractions/`** — checked (`find ... -iname "*deya*"`): zero results. One unrelated hit for the literal string "deya" inside `research_outputs/.../gemini.json`, which is an AI-plugin-market research file, not Deya content.
4. **`agents/deya/AGENT.md`**, **`agents/deya/memory/context.md`** — existing repo files, cross-referenced for consistency; the memory file is an unpopulated stub ("To be populated") and contributes no source content.

## Claim-by-Claim Ledger

| # | Claim | Label | Anchor |
|---|---|---|---|
| 1 | "built two six-figure businesses and helped clients scale to seven figures" | VERIFIED | d81c6e71: "I've started two six figure businesses of my own and helped clients scale to seven figures and I have never once written a 50-page business plan" |
| 2 | "$200K+" in 2024 (personal income) | VERIFIED (self-reported claim) | d81c6e71 conversation title: "the 1-page business plan that made me $200K+ in 2024" — this verifies Deya made the claim; it is not independently audited income data |
| 3 | "founder of DBM Bootcamp" | UNCONFIRMED | Not found verbatim in any of the 4 read conversations; zero matches for "Bootcamp" across all 18 Deya-tagged files. Likely carried over from the original extraction's bio research (visible only in an artifact block the export doesn't render), but not verifiable against readable source text |
| 4 | "~200k YouTube" subscriber count | VERIFIED (self-reported) | CORRECTED 2026-07-17 by Opus adversarial verify: Deya's own first-person statement exists — fba00784 ("getting the channel to maybe 200k… we might be at 200k" + persona header "YouTuber (~200K subscribers)") and 1037ef70 ("Built 200K+ YouTube channel"). Original pass falsely reasoned no Deya-specific statement existed (only the Emma Chamberlain mention in a819015f was checked). Self-reported, not independently audited |
| 5 | Named Person Anchor — "Esther" (service), past self (matcha), herself (book-club) | VERIFIED | d81c6e71 verbatim, see `source-excerpts.md` §1 |
| 6 | Problem Severity Scale — pen-cap / 2 a.m. anchors | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §2 |
| 7 | Dual-Gate Validation (worth paying × can afford) | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §3 |
| 8 | Founder Passion Floor 6-7/10 | VERIFIED | d81c6e71 verbatim: "I think it's important that you care at least a six or seven out of a scale of 10" |
| 9 | Remarkable Offer Brainstorm — Hormozi + Seth Godin Purple Cow attribution | LIKELY / VERIFIED (split) | d81c6e71 verbatim says "I love this question from **Alex Heros**" — near-certainly an auto-transcription artifact for "Alex Hormozi" (no entrepreneur named "Alex Heros" fits context); label the Hormozi half LIKELY. The Seth Godin/Purple Cow half is VERIFIED verbatim in the same passage: "go check out anything Seth Goden has written about product remarkable product Purple Cow" |
| 10 | Beta Price Ladder ($5→$10→$15; freelance +10-20%/client) | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §4 |
| 11 | Customer Voice quotes ("reading all these business books...", "drowning in the work...") | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §5 |
| 12 | Simplified Sales Funnel + TikTok "Business Book Club" series | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §6 |
| 13 | Product Suite Emergence — matcha-machine analogy | VERIFIED | d81c6e71 verbatim: "the pods could be one thing but the next product in the product Suite could be like an espresso machine but for matcha a matcha machine" |
| 14 | Specificity Stacking — Maya video-editor example | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §7 |
| 15 | "$100K math: $100 product needs 1,000 buyers/year" | LIKELY | Not located as a direct Deya quote in the 4 read files. It is arithmetically consistent with her stated framing (specificity over reach) but not confirmed as her own spoken words — treat as a reasonable inference layered onto her pattern, not a verbatim claim |
| 16 | "Boom, Validated" personal-spend heuristic | VERIFIED | fba00784 / 1037ef70 verbatim (recurring 5x across both files): "I have paid money for three of them. So boom, validated." — `source-excerpts.md` §8 |
| 17 | Cold-to-Committed via Community Love — Digital Nomad Girls / Jenny | VERIFIED | fba00784 / 1037ef70 / a819015f verbatim: "I found this community I really loved called Digital Nomad Girls. And I essentially pitched the founder..." — `source-excerpts.md` §9 |
| 18 | Rename the Discovery Call | VERIFIED | d81c6e71 verbatim, `source-excerpts.md` §10 |
| 19 | Content Precedes Product (Book Club series preceded the database product) | VERIFIED | d81c6e71 verbatim: "I actually did this before I made the product and that can happen as well when you're already creating content that you're passionate about product ideas will emerge out of that content" |
| 20 | New Anti-Patterns section (6 items: 50-page plan, demographics, build-before-validate, vague problem, saturated-market/generic-offer, funnel-bro complexity) | VERIFIED | All 6 quoted verbatim from d81c6e71 — see SKILL.md anchors and `source-excerpts.md` §§1, 11-14 |

## Note on Archive Access (for future workers on this skill)

Extraction command that worked: `tar -xzf _archive/claude-export-2026-07-01.tar.gz -C <scratch-dir> claude-export/normalized/conversations` (~272MB decompressed, 3,850 files). `tar -tzf` (filename listing) alone will NOT surface Deya content — the archive stores conversations by UUID, not by subject line, so filename grep returns nothing and would produce a false "no source exists" conclusion if trusted alone. Content-level search (`tar -xzOf <archive> | grep -a -i "<term>"`, or a full extraction + `grep -rli`) is required. Recorded here so this false-absence trap doesn't recur.
