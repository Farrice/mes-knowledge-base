# Source Ledger — WordsAtScale: Search Gap Method

Ground truth for this skill. No `extractions/` file exists for WordsAtScale
(confirmed via `ls extractions/ | grep -i wordsatscale` and `| grep -i "words at scale"`
— zero matches). Primary source material was recovered from
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `wc -c`)
via a per-member Python `tarfile` content scan for `wordsatscale|words at scale|words-at-scale`
(29 of 7,728 members matched). The matches are Claude.ai extraction conversations where
Fresh (the operator) pasted real YouTube transcripts of WordsAtScale (real name: Vlad,
~25K YouTube subscribers, channel catchphrase "welcome to the scale") and ran an MES 3.0
extraction. This repair read 6 of those 29 conversation files directly (raw transcript text
inside the first human turn of each); the other 23 matches were not opened for this pass and
are listed as UNCONFIRMED provenance below, not claimed as read.

## Claim-by-Claim

| Claim | Label | Source |
|---|---|---|
| Expert's real name is Vlad; channel/method is "WordsAtScale" / "Search Gap Method"; ~25,000 YouTube subscribers | VERIFIED | Transcript, "How To Rank a ZERO Domain Rating Site in 24 Hours [Secret Method Revealed]," youtube.com/watch?v=lFuDru9qv4Y — archive member `claude-export/normalized/conversations/47a03d2a-f065-49a7-ada5-f4d0fae6de57.md`, line 30 ("I have my YouTube channel which is worth the scale with 25,000 people subscribed") and 116k-commissions transcript ("My name is Vlad and if you know me, I'm an SEO and a blogger") |
| DR5 site outranking a DR76 competitor ("my VersusK website is DAO5 and I'm outranking originality which is DA of 76") | VERIFIED | Same transcript as above, line 30 |
| $95,000 + $19,000 from two affiliate programs (Pattern 9 real-world evidence) | VERIFIED | Transcript, "This Method Made Me 125K Dollars [Proof Inside]," youtube.com/watch?v=LxjOpMBn06g — archive member `466e59dc-8ef9-4266-a8bb-8aca9208d562.md`, line ~30 |
| $116,000 in commissions via an automated method | VERIFIED | Transcript, "$116K In Commisions Using This Simple Automated Method [Proof Inside]," youtube.com/watch?v=kgA6V-kWyqk — archive member `8f66b3b3-17bc-4bf8-bda9-650a25562ff7.md`, line ~30 |
| $34,000 site sale; trailing revenue ($1,500/day; 3-month avg $2,100, 6-month $1,700, 12-month $1,400); Agility Writer workflow details ("love-hate relationship with tools like neuron writer"; "I will not be choosing that although you can"; "Now I don't want this to become a single huge tutorial"; SEO score 83 vs. competitor 79) | VERIFIED | Transcript, "This Crazy AI Writing Tool Sold My Site for $34K [Proof]," youtube.com/watch?v=HaVal2rVLRY — archive member `da66bf03-28e8-48f0-b03d-d782173212cd.md`, line 30 |
| "SEO is not dead"; 99.2% of informational queries trigger AI Overviews vs. 4% of transactional queries (citing an Ahrefs analysis) | VERIFIED | Transcript, "How To Find Transactional Intent Keywords [Full Guide]," youtube.com/watch?v=vG36upd1Bfg — archive member `a7ba832f-5c80-4368-a44a-e4eb14daf68d.md`, lines 32-51 |
| Brand voice should be built from audience/consumer vocabulary, not brand vocabulary | VERIFIED | Transcript, "How to Fix Your Brand Voice Strategy (Mistakes That Kill Sales)," youtube.com/watch?v=zRQPW66Jvns — archive member `de0e7e71-f680-4246-9e7d-87c66ae6f655.md`, lines 34-45 |
| Pattern 1 (Competition Vacuum Hunting), Pattern 3 (LSI Keyword Bypass), Pattern 4 (Parallel Opportunity Processing), Pattern 6 (Index Velocity Prioritization — incl. the specific "60 seconds" figure), Pattern 7 (Rank Tracking), Pattern 8 (Top 3 Filtering), Pattern 11 (RankMath Meta), Pattern 12 (Permalink Alignment), Pattern 13 (Speed Over Polish) as originally written, and the "3-5 internal links" figure in Patterns 2 and 10 | LIKELY | Consistent with the "Search Gap Method" course structure described verbatim in the ZERO-DR transcript (searchgapmethod.com; research prompts → article prompts → product roundup prompts; "zero risk, 100% guarantee... 30 days") and with the general operating pattern across all 6 transcripts read (speed-first, proof-first, tool-agnostic). The *specific numeric thresholds* in these Success Metric lines (e.g., the exact "60 seconds," "3-5 links," "10 opportunities") were not found verbatim in the 6 transcripts read for this repair pass — they were authored by the original MES 3.0 extraction agent (see conversation `47a03d2a-f065-49a7-ada5-f4d0fae6de57.md`) and were not independently re-verified against a primary transcript here. Not contradicted by anything read; not confirmed either. |
| Pattern 5 ("<5 minutes from AI completion to published article") and Pattern 9 (affiliate flagging as a research habit) as general behaviors | LIKELY→VERIFIED (upgraded this pass) | See Real-World Evidence lines added to genius.md, sourced from the $34K-sale and $125K-method transcripts respectively |
| Pattern 14 ("timestamped proof of results") as a general behavior | VERIFIED (upgraded this pass) | See Real-World Evidence line added to genius.md, sourced from the $34K-sale transcript's exact trailing-revenue breakdown |
| "VAI AI Assistant Review," "Eco-Friendly Water Bottle Review" / "EcoFlow Water Bottle," and "Best Portable Chargers for Travel" Hall-of-Fame/Anti-Exemplar scenarios in genius.md | UNCONFIRMED | Pre-existing in genius.md before this repair pass. No VAI, EcoFlow, or portable-charger product appears in any of the 6 transcripts read. These read as illustrative/synthetic scenarios authored by the original extraction agent, not drawn from a real WordsAtScale case study. Flagged, not removed or rewritten (additive-first boundary — this repair pass did not author them and is not the right pass to adjudicate them). |
| The remaining 23 of 29 archive matches (additional WordsAtScale transcripts: iGaming $120B niche, ChatGPT/GEO ranking, NotebookLM topical maps, rank-and-rent niches, transactional-intent follow-ups, etc.) | UNCONFIRMED (unread) | Matched by filename-content scan but not opened for this repair pass; listed so a future pass does not re-run the same archive scan from zero. Titles and archive member IDs recorded in REPAIR-NOTES.md. |

## Search Discipline Record

- `ls extractions/ | grep -i wordsatscale` → no output (confirmed absent, not assumed)
- `ls extractions/ | grep -i "words at scale"` / `"words-at-scale"` → no output
- `find . -iname "*wordsatscale*"` (repo-wide, excluding this skill's own tree) → only found `agents/wordsatscale/AGENT.md` (routing metadata, no sourced content) and worktree/evolution-store mirrors of this same skill — no independent primary source
- `_archive/claude-export-2026-07-01.tar.gz` size confirmed via `wc -c` = 332,779,255 bytes (not `wc -l`, which would misreport a large binary as near-zero)
- Python `tarfile` per-member content scan (not filename-only) over all 7,728 members, case-insensitive regex `wordsatscale|words at scale|words-at-scale`, size-capped at 5MB per member to stay fast → 29 matches, all `claude-export/normalized/conversations/*.md`
