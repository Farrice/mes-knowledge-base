# PROVENANCE — authority-hacker-ai-social-media repair

Anchor → source file + location. Full claim-level detail lives in `references/source-ledger.md`; this is the compact index of every new anchor added in this repair.

| Anchor (in repaired genius.md) | Source file | Location |
|---|---|---|
| "they auto reply on threads, complete useless stuff as well" | extractions/ai-social-media-panel/transcript.txt | single-block transcript, ~char offset 2650 (auto-reply/Operation Kill the Bots passage) |
| "It's like this is an automated reply. It just repeats what I said in the post and say, 'Oh my god, this is great.'" | extractions/ai-social-media-panel/transcript.txt | same passage, immediately following the above |
| "this is this fantasy of like, oh, if I get rich" / "literally has no value" | extractions/ai-social-media-panel/transcript.txt | same passage |
| "restricted in the API... start like 50k a month" | extractions/ai-social-media-panel/transcript.txt | "Operation Kill the Bots" API-restriction passage |
| "I almost have it introduce clunky language sometimes" / "you don't want to sound like AI" | extractions/ai-social-media-panel/transcript.txt | Imperfection Engineering passage (near "clunky language" keyword) |
| "there was no value added wasn't that good" | extractions/ai-social-media-panel/transcript.txt | weekly-audit / underperforming-post passage (near "emoji" keyword) |
| "AI chatbots give better answers than any social media post could..." | extractions/ai-social-media-panel/extraction-report.md | Hidden Knowledge #1, "Information Is Dead on Social Media" |
| "Authority Hacker generated hundreds of thousands of leads per month and found no correlation between traffic and revenue." | extractions/ai-social-media-panel/extraction-report.md | Hidden Knowledge #2, "Traffic ≠ Money" |
| "When Claude Code (or any LLM) writes multiple posts in one conversation thread, they converge in tone, structure, and length." | extractions/ai-social-media-panel/extraction-report.md | Hidden Knowledge #5, "The Sub-Agent Variety Trick" |
| "If you publish low-quality AI posts that get low engagement, your next high-quality post gets suppressed..." | extractions/ai-social-media-panel/extraction-report.md | Hidden Knowledge #4, "Platform Algorithm Memory" |
| "122K views, 6K saves" | extractions/ai-social-media-panel/extraction-report.md | Executive Summary bullet, "What Makes Them Different" |
| "$0.17/image" | extractions/ai-social-media-panel/extraction-report.md | Genius Pattern 10 body + Hidden Knowledge #6 ("The $2.50 Ad Agency") |
| "would Gael Breton recognize this as his own" | new (repair worker's calibration language) | genius.md § How to Use This Skill (Model Calibration) — modeled on skills/ben-watkins-storytelling/genius.md lines 7-16, written fresh for this expert's texture, not copied |

## Absence verification (per envelope Rule 2)

Before writing any "no source exists" claim, real file reads + sizes were recorded:
- `extractions/ai-social-media-panel/transcript.txt` — 68,471 bytes (`wc -c`), confirmed non-empty, confirmed readable, full text scanned for anti-pattern candidates.
- `extractions/ai-social-media-panel/extraction-report.md` — 19,597 bytes (`wc -c`), confirmed non-empty, read in full.
- No `extractions/` folder matches `authority|hacker|breton|webster` by name (checked via `ls extractions/ | grep -i` against those four terms, 193 total extraction folders scanned) — the source material for this expert lives under the topical folder `ai-social-media-panel`, not a surname folder. This is a naming-convention fact, not a missing-source claim.
