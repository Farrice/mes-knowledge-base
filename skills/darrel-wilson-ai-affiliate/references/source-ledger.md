# Source Ledger — darrel-wilson-ai-affiliate

Claim-by-claim verification for the factual assertions in `SKILL.md` and `genius.md`.
Labels: **VERIFIED** (verbatim or numerically exact match found in a primary source) /
**LIKELY** (concept/number confirmed, but a supporting detail is paraphrased beyond what
the source states, or the wording was lightly recontextualized) / **UNCONFIRMED** (no
matching text found in any source file read for this repair).

## Sources Read For This Repair (with sizes — none assumed empty or absent)

| File | Size | Result |
|---|---|---|
| `extractions/darrel-wilson-affiliate-marketing/extraction-report.md` | 14,540 bytes | Read in full — the MES extraction this skill was built from. |
| `extractions/darrel-wilson-affiliate-marketing/transcript.txt` | 21,929 bytes | Read in full — primary source, "affiliate marketing 2026" tutorial video. |
| `extractions/darrel-wilson-ai-money/transcript.txt` | 14,562 bytes | Read in full — second primary source, "5 ways to make money with AI" video (this is the direct source for the AI-utility-site, lead-scraper, and AI-website-sales patterns; it has no matching extraction-report.md of its own). |
| `_active/harness/codex-harvest-2026-06-11/extractions/` | — | Checked per envelope instruction: `ls extractions/ \| grep -i wilson` returns nothing under this path; no Darrel Wilson material exists in the Codex harvest import. |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 bytes | Checked per envelope instruction: `tar -tzf ... \| grep -i darrel` returns zero matching entries. No additional Darrel Wilson source material exists in the Claude export archive. |

No `agents/darrel-wilson/AGENT.md` file was located during this repair (SKILL.md's Quick
Reference cites one) — flagged here as an open gap, not fabricated as present.

## Claim Ledger

| # | Claim (as stated in genius.md / SKILL.md) | Label | Source anchor | Note |
|---|---|---|---|---|
| 1 | "$50-60K/month in commissions," "over $500K from single affiliate programs" | VERIFIED | affiliate-marketing/transcript.txt | "I average about $50 to $60,000 a month in commissions... here's an affiliate program where I've literally earned about half a million dollars." |
| 2 | "10-year affiliate marketing veteran" | VERIFIED | affiliate-marketing/transcript.txt | "I've been doing affiliate marketing for like the last 10 years already." |
| 3 | Operating Philosophy quote: "People like to buy, but they just hate being sold to, right?" | VERIFIED | affiliate-marketing/transcript.txt | Exact match. |
| 4 | Elegant Themes tutorial example: 282,000 views, ~3 years old, still earning | VERIFIED | affiliate-marketing/transcript.txt | "it has about 282,000 views, and this was about 3 years ago." |
| 5 | Pattern 1 (Utility-First): currency tool example, "$1,000 to Thailand" → "about 31,000 Thai bots" | VERIFIED (content) / note on transcription artifact | ai-money/transcript.txt | Exact quote; "bots" is almost certainly a mis-transcription of "baht" (the Thai currency) — flagged `[sic]` in genius.md rather than silently corrected. |
| 6 | Pattern 2 (Indirect Promotion): "Omnisend email review" vs. "3 emails we send that make us $500/day" | VERIFIED | affiliate-marketing/transcript.txt | "would you want to watch a video on Omnisend email review or three emails we send that make us $500 a day?" |
| 7 | Pattern 2: NordVPN mention in Google Flow video, "a few hundred in the first month" | VERIFIED | affiliate-marketing/transcript.txt | "I actually recommend NordVPN... I made a few hundred in the first month, and I wasn't even trying to sell them." |
| 8 | Pattern 3 (Required Tool Funnel): hosting tutorials require purchase to follow along | VERIFIED (concept) | affiliate-marketing/transcript.txt | "in order to actually follow this tutorial, they have to click on that link, and they have to purchase Divvy." Photoshop example in genius.md is an extractor-generalized illustration of the same mechanic, not a Wilson quote — label that specific sentence LIKELY. |
| 9 | Pattern 4 (AI Lead Scraper): RFP examples — "€30,000, which is about 35,000K"; Central Coast Community Energy RFP, "December 18th, 2025," deadline "the 21st of next year" | VERIFIED | ai-money/transcript.txt | All three figures/dates are exact matches, including the transcript's own garbled "35,000K" conversion (quoted verbatim, not corrected). |
| 10 | Pattern 4: n8n cron trigger "every 2 hours" | VERIFIED | ai-money/transcript.txt | "every 2 hours we're fetching stuff throughout the internet." |
| 11 | Pattern 5 ("Finished Product" Close): "$200," Hostinger Horizons/Lovable/Bolt | VERIFIED | ai-money/transcript.txt | "It'll only cost you $200"; tools named directly: "lovable or hosting or horizons." |
| 12 | Pattern 6 (Recurring Revenue): "$200 upfront... monthly subscription" | VERIFIED (concept) | ai-money/transcript.txt | "you're putting them on a monthly subscription, so that way you can get recurring revenue." Specific figure "$97/month" and the "five clients = $485/month" math in genius.md are extractor-modeled numbers, not stated by Wilson — label LIKELY. |
| 13 | Pattern 7 (Parasite SEO): Medium/LinkedIn domain authority, "Blogify Review" ranking example | VERIFIED (concept) / LIKELY (DA figures) | affiliate-marketing/transcript.txt | "platforms like LinkedIn and Medium have huge domain authority... I'll type in Blogify Review and the very first result is actually a Medium article." Specific DA scores (Medium 95, LinkedIn 98, Reddit 97 used across workflows) are not stated in the transcript — these are plausible external SEO-tool figures the extraction added; label LIKELY, not attributed to Wilson. |
| 14 | Pattern 8 (Link Automation): "all you got to do is give them one affiliate link. The AI will actually place the affiliate link on all the buttons" | VERIFIED | ai-money/transcript.txt | Exact quote (corrected from an earlier paraphrase during this repair). |
| 15 | Pattern 8: "coin signal" AI crypto-analysis site, Coinbase/Binance affiliate links | VERIFIED | ai-money/transcript.txt | "so here's my website coin signal... The whole point of this is to make affiliate commissions from Coinbase and also Binance." |
| 16 | Hidden Knowledge #1 (Anti-Freemium Filter) | VERIFIED | affiliate-marketing/transcript.txt | "Any company offering a free and pro version, I typically try to avoid it... I have terrible results with free models." |
| 17 | Hidden Knowledge #2 (Marketplace Protection): Impact, Awin, PartnerStack | VERIFIED | affiliate-marketing/transcript.txt | "impact.com... awind.com. This was previously known as share a sale... partner stack." |
| 18 | Hidden Knowledge #3 (Long-Form Conversion): "5%" vs "2%" conversion, "$8,000" per 350K views | VERIFIED | affiliate-marketing/transcript.txt | "Long-form content has the best conversion rates in the industry at about 5%"; short-form "around 2%"; "for every 350,000 views on YouTube, I make about $8,000." |
| 19 | Hidden Knowledge #4 (Social Fatigue): 15,000 Facebook members, "no one buys," Pinterest "one conversion a month" | VERIFIED | affiliate-marketing/transcript.txt | Matches closely; transcript has a garbled connector ("No one buys. my Pinterest.") which genius.md's Anti-Patterns #6 quotes across with an ellipsis — flagged here as a known transcription artifact, not an editing error introduced by this repair. |
| 20 | Hidden Knowledge #5 (Workflow-as-Product): menu-scraping workflow sold for "$5,000" | VERIFIED | ai-money/transcript.txt | "I'm personally working with someone right now that sold an AI workflow for about $5,000... it scrapes menu items from restaurants." |
| 21 | Hidden Knowledge #6 ("Ugly Website" Prospecting): Google Maps, Fitactory Nashville example | VERIFIED | ai-money/transcript.txt | "we found this one website fitactory Nashville... I would essentially take their logo... shoot them an email." |
| 22 | File-converter micro-app: "$400 bucks a month" | VERIFIED | ai-money/transcript.txt | "The site has made about 400 bucks a month in revenue." |
| 23 | Niche Analysis Framework commission figures (Sephora 5%, Vitamin World 8%, Under Armour 10%, Amazon 1-25%, NordVPN 40%/30%, Elegant Themes 50%, Shopify $150, Coinbase 50%, web hosting up to 300%) | VERIFIED | affiliate-marketing/transcript.txt | All individual figures matched verbatim in the commission-structure section of the transcript. |
| 24 | Anti-Pattern #1-#7 (see genius.md § Anti-Patterns) | VERIFIED | both transcript.txt files | Each carries its own verbatim quote and source file in-line; see genius.md for the full text. |
| 25 | "Agent: `agents/darrel-wilson/AGENT.md`" (SKILL.md Quick Reference) | **UNCONFIRMED** | — | No such file was found on disk during this repair. Not corrected in SKILL.md (out of scope for this batch — SKILL.md was not a failing-check target), but flagged here so a future pass doesn't treat the pointer as confirmed. |
| 26 | Workflow tables, Quality Rubric, Signature Moves, Output Schema field lists (workflows) | N/A — not a provenance claim | — | Original skill-authoring synthesis and structural scaffolding, not factual assertions about Wilson. No VERIFIED/LIKELY/UNCONFIRMED label applies. |

## Zero-Byte / Absence Claims (per envelope Rule 2)

No claim of source absence is made without a file read or listing check first:
- `extractions/` for "wilson"/"darrel" surfaced exactly the two directories used above — confirmed via `ls extractions/ | grep -i darrel`, not assumed.
- `_active/harness/codex-harvest-2026-06-11/extractions/` — checked via `ls | grep -i darrel`, zero results, confirmed empty of Wilson material (directory itself exists and is non-empty for other experts).
- `_archive/claude-export-2026-07-01.tar.gz` — 332MB archive, listed via `tar -tzf` and grepped for "darrel", zero matching entries. Full extraction was not performed (not warranted given zero listing hits and archive size), but this is a listing-based negative, not an unread assumption.
