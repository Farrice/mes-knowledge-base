# Source Ledger — Nate Herk: AI Client Acquisition

Every claim, quote, and stat used in `genius.md` and `SKILL.md`, labeled VERIFIED / LIKELY / UNCONFIRMED. "VERIFIED" here means confirmed verbatim against the extraction source file — it does NOT independently verify Nate Herk's real-world business stats (agency revenue, market response rates) as objective fact; those remain his stated claims, labeled accordingly below.

## Sources Consulted (with file sizes, per source-search discipline)

| Source | Path | Size | Method |
|---|---|---|---|
| Primary transcript | `extractions/nate-herk/transcript.txt` | 21,987 bytes | Full read, `python3 -c` size check via `ls -la`, manual quote diff against genius.md |
| Extraction report | `extractions/nate-herk/extraction-report.md` | 6,241 bytes | Full read |
| Legacy SKILL.md | `skills/nate-herk-client-acquisition/SKILL.md.old` | — | Full read (no anti-pattern or ledger content found in it) |
| `references/genius-patterns.md`, `references/hidden-knowledge.md`, `references/implementation.md` | `skills/nate-herk-client-acquisition/references/` | — | Full read — confirmed these are mirrors of genius.md sections, not independent sources |

No other extraction directories matched `nate-herk`, `natherk`, or `herk` under `extractions/` (checked via `ls extractions/ | grep -i herk`). Only one source pair exists for this expert — there is no separate podcast/interview transcript beyond the single ~15-minute YouTube video ("How to Sign AI Workflow Clients") that `extraction-report.md` documents as the source.

## Entity Disambiguation

- **VERIFIED**: This skill (`nate-herk-client-acquisition`) is a distinct expert extraction from `nate-b-jones` (a separate skill/expert in this repo, AI orchestration/context-engineering focus). No content, quote, or pattern in this skill's files derives from Nate B. Jones material — confirmed by grep across both skill directories.

## Claim-by-Claim Ledger

| Claim / Quote | Label | Basis |
|---|---|---|
| "If you're spending weeks perfecting an automation before you've talked to a single customer, you don't have a business, you just have a hobby." | VERIFIED | Verbatim in `extractions/nate-herk/transcript.txt` |
| "Nobody really cares if you built an 18 node automation with Naden and Slack and Notion MCP. They care about the results" | VERIFIED | Verbatim in transcript.txt (note: "Naden" is the transcript's own spelling, likely a mis-transcription of "n8n" — reproduced as-is rather than silently corrected) |
| "Don't try to do outreach on all of those platforms. You're going to spread yourself too thin because they all have different methods of what works best." | VERIFIED | Verbatim in transcript.txt |
| "The first one is asking too early before you've actually proven yourself. And then the second one is not asking at all and just leaving that money on the table because you were too scared to ask." | VERIFIED | Verbatim in transcript.txt |
| "You don't need massive email infrastructure with thousands of domains. You just need a few and each domain can send about 30 messages a day" | VERIFIED | Verbatim in transcript.txt |
| "Who have you done this for?" / "you're fighting uphill the entire conversation" | VERIFIED | Verbatim in transcript.txt |
| Generic "AI Solution" Pitch anti-exemplar (full text, "Revolutionize Your Business with AI!") | VERIFIED | Present verbatim in the pre-existing genius.md — this is an extraction-authored anti-exemplar (a constructed contrast example), not a quote from Nate Herk himself. Labeled VERIFIED for "exists in the source skill file as-is, unmodified," not as a Herk quote. |
| The Trojan Horse Partnership pattern (20% rev-share, white-label positioning) | VERIFIED | Matches transcript.txt: "if any of them end up wanting to work with me, I'll give you 20% of that project revenue" and surrounding passage |
| Validation-First Outreach (100 messages/day, >5% reply rate threshold) | VERIFIED | Matches transcript.txt: "you should be sending 100 messages a day" and "If you're doing anything above 5%, you're crushing it" |
| The Golden Question / Process Constraint question ("if tomorrow you got 300 new clients...") | VERIFIED | Matches transcript.txt: "if tomorrow you've got 300 people that wanted your services, what process would break first" |
| Cold email response rate "1 to 5%... personalized emails see up to 17% higher" | LIKELY | Verbatim as stated by Nate Herk in transcript.txt; presented on-video without a cited external source, so the *statistic's real-world accuracy* is UNCONFIRMED even though the *quote* is VERIFIED against the transcript |
| LinkedIn InMail "10 to 25% response rate" | LIKELY | Same basis as above — verbatim quote, unconfirmed external stat |
| "92% of B2B buyers trust referrals from people that they know" | LIKELY | Verbatim in transcript.txt; Nate cites no source for this figure on-camera, so treat as his claim, not an independently confirmed statistic |
| "Partner source deals close 46% faster than other deal types" | LIKELY | Verbatim in transcript.txt; no source cited on-camera |
| Dale Carnegie referral stats ("only 11% of salespeople are actually asking for referrals. Yet, 91% of customers said that they'd gladly give one") | LIKELY | Verbatim in transcript.txt; attributed by Nate to "Dale Carnegie research" but no specific study/year is named in the source, so the attribution itself is UNCONFIRMED beyond "Nate cited it this way" |
| "True Verizon" — the agency Nate says he founded and exited, "scaled past 100K a month" | UNCONFIRMED | Verbatim spelling in transcript.txt, but `extractions/nate-herk/extraction-report.md` line 10 lists "Existing Overlap: Liam Ottley, True Horizon scaling" — suggesting "True Verizon" is likely a transcription artifact for "True Horizon." Not corrected in genius.md/SKILL.md to avoid inventing a fact not confirmed either way; not used as a named entity anchor in this repair for that reason. |
| Sonam podcast reference ("generate over half a million dollars in sales opportunities with cold email in six months") | UNCONFIRMED | Verbatim in transcript.txt as Nate's claim about a guest; no independent verification available in this extraction's source set; not used as an anti-pattern anchor in this repair |

## Method Note (source-search discipline)

Before labeling anything UNCONFIRMED or absent, `extractions/` was searched by name fragment (`herk`, `natherk`) and the matched directory was opened and both files read in full (not sampled) — sizes recorded above via `ls -la`. No claim in this ledger is labeled "no source exists" without that file-read step having been performed first.
