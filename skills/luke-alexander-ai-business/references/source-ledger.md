# Source Ledger — luke-alexander-ai-business

Repair pass: Wave 3 Lane 4 Batch 9 (2026-07-18). Ground truth located and read in full:
`extractions/` has no `luke-alexander*` file (checked: `ls extractions/ | grep -i alexander` = 0 hits).
The skill's actual source is the claude.ai account export archive
(`_archive/claude-export-2026-07-01.tar.gz`, 332MB, present on disk, opened via Python
`tarfile` per-member scan — no name-fragment match on "alexander"/"kendo" in tar member
*names*, so the census index was used instead). `_active/harness/claude-export/harvest/census-full.json`
lists a `"Luke Alexander"` expert entry with 5 conversation IDs (`count: 5, max_richness: 9`).
All 5 were located inside the tar under `claude-export/normalized/conversations/<id>.md` and
extracted for direct read (sizes recorded below — these are YouTube-transcript-in-chat
conversations: the human pastes a timestamped transcript of a Luke Alexander video, then asks
Claude to extract prompts/patterns from it. The timestamped lines are Luke's own spoken words,
not the requesting user's).

## Sources Consulted (with recorded sizes — tarfile per-member scan)

| Conversation ID | Title | Created | Size (bytes) | Contains |
|---|---|---|---|---|
| `46535df5-a7ae-477e-8da7-ccfd6f5078ee` | "Luke Alexander: The Blueprint To Making $1,000,000 With AI This Year" | 2025-09-03 | 58,351 | Full video transcript (timestamps 0:00–~22:00+), bio, stack layers, agency-model rejection, $83,333/mo math |
| `58b43e7b-ee4e-435c-a698-10b0c0fa8f72` | "Luke Alexander: This is how to make $173,228/month selling AI offers" | 2025-09-03 | 37,262 | Full video transcript, 4x rule, commodity/buzzword rejection, information-asymmetry quote, Ferrari analogy |
| `0d1f2783-ca66-45ea-9b84-8e81a7338cc2` | "[V1.CONTEXT PROFILE ARCHITECTURE]... Its Boring.. But It Will 100x Your AI Output" | 2025-10-09 | 33,769 | Full video transcript, water-bottle memory analogy, 90%/99% context claims, "boring fundamentals" quotes |
| `172a1060-4607-41b7-a653-a31bb5456e13` | "[V.2 Context Profile Engine]... This prompting secret makes AI perform 1000x better pt.2" | 2025-10-07 | 31,174 | Continuation transcript + Claude-generated prompt artifacts (not verbatim Luke) |
| `e34babf7-7d82-47d7-866e-99bd830bfeb2` | "[Fresh's INPUT]-Luke Alexander: How To Make $50k/month With AI Operating In 2026 pt.2" | 2025-12-03 | 30,211 | Continuation transcript + Claude-generated prompt artifacts (not verbatim Luke) |

No 0-byte or unrecoverable files among these five — every size above is a real, non-empty
`.md` read in full via Python `tarfile.extractfile()`. AppleDouble shadow copies
(`._<id>.md`, 163 bytes each, macOS metadata artifacts, not content) exist alongside each
real file in the tar and were excluded by filename check.

## Claims — VERIFIED / LIKELY / UNCONFIRMED

### Bio (SKILL.md intro, genius.md, AGENT.md)
- "trained ~5,000 sales reps, generated close to $10M personally online" — **VERIFIED**. Verbatim: *"my name is Luke Alexander. I have trained like 5,000 sales reps, made close to $10 million personally online"* (`46535df5…`, timestamp 0:37–0:42).
- "now builds Kendo AI, an enterprise AI sales-training startup" — **VERIFIED**. Verbatim: *"now I'm building an AI startup... called Kendo AI. And it is extremely insane, technical, highl[y], enterprise-grade, basically AI, sales, training, management, ramp up... Kind of like Gong, but AI"* (`46535df5…`, 0:44–0:58).
- "(Closer Cartel, IPO/growth-partner offers)" — **VERIFIED**. Both named directly as Luke's own info products/companies: *"every VSSL that you've ever seen from me from closer cartel, IPO..."* (`58b43e7b…`, 6:36–6:38); *"in my own info product in closer cartel. I wrote our VSSLs. I wrote our webinars. I wrote our funnels."* (`46535df5…`, 19:42–19:47).

### Pattern: Service Layer Arbitrage
- "you're probably a decade late" (LLM layer) — **VERIFIED**, `46535df5…` 2:24–2:30, exact match.
- Three-layer stack (LLMs → software → services) — **VERIFIED**, same passage, 2:07–2:44.

### Pattern: Problem-First Battle Selection
- "You're only selling things based on problems you solve." — **LIKELY**. Close paraphrase of Luke's problem-selection framing across `46535df5…` 4:39–5:21; not located as one contiguous verbatim sentence in the five sources — could be a compressed synthesis from the original extraction pass. Treat as paraphrase, not direct quote.
- "guys are literally buying cars and posting them online and making a million dollars" — **VERIFIED with correction**. Actual verbatim (`46535df5…`, 5:00–5:04): *"guys are literally just buying cars and posting them online and making a million dollars and not being good at anything."* The pre-repair genius.md dropped "just" and truncated the clause; corrected to the fuller verbatim line in this repair pass.

### Pattern: Upside Economics
- "$83,333/month = $1M/year" math and "old agency model from like 2018" rejection — **VERIFIED**, `46535df5…` 10:56–11:15, exact match on the 2018/retainer line.
- "$25K setup fee... $300-400K over 4 months, $200K in a single week, $4.5M collected" — **VERIFIED**. Verbatim: *"we ended up making about 300k or 400k from this client in the span of like 4 months... I sold... a $25,000 setup fee"* (`46535df5…`, 11:41–11:52) and *"our team was paid $200,000 in a single week of work... we did $4.5 million collected"* (`46535df5…`, 6:23–6:31).

### Pattern: Conversion Lever Math
- Show rate/close rate/booking-rate lever example (30%→50%, 20%→40%, 3%→5%) and "We fixed show rate. We fixed close rate. No new traffic." — **LIKELY**. The multiplication-chain framing and lever concept are directly attested in the sources (e.g., `58b43e7b…` 11:48–12:02 ROI-based selling; conversion-lever language recurs across all five transcripts), but this exact worked numeric example was not found as one verbatim block in the five located conversations — plausibly drawn from a portion of one of the longer transcripts not re-verified line-by-line in this pass, or a compressed synthesis from the original 2026-07-01 extraction. Flagged for a follow-up read if this pattern is used in a client-facing deliverable.

### Pattern: Sell the Outcome, Bury the Engine
- Buzzword-slop quote — **VERIFIED**, `58b43e7b…` 10:07–10:16, exact match.
- Ferrari/engine analogy — **VERIFIED**, `58b43e7b…` 10:42–11:04, exact match (transcript is auto-generated lowercase; capitalization normalized in genius.md, wording otherwise verbatim).

### Pattern: Information Asymmetry Is the Margin
- "If they knew what you know, they wouldn't pay you..." — **VERIFIED**, `58b43e7b…` 12:59–13:07, exact match.

### Pattern: Strengths-to-Offer Mapping
- Four-question inventory and four-question offer definition — **LIKELY**. Consistent with Luke's teaching style and terminology found across the sources but not isolated as one verbatim block in this pass; treat as a faithful synthesis pending a full re-read of `172a1060…`/`e34babf7…` (which are largely Claude-generated prompt artifacts layered on the transcripts, not pure Luke transcript).

### Pattern: The 4x Retention Rule
- "getting at least a 4x" / "our 4x rule. That's a good ROI." — **VERIFIED**, `58b43e7b…` 17:05–18:11, exact match.

### Pattern: Context Profile System
- "90% of people fail" (context-window mismanagement) — **VERIFIED**, `0d1f2783…` 8:01, exact match.
- "99% of the time it's about the quality of your context rather than the quantity" — **VERIFIED with correction**. Actual verbatim (`0d1f2783…`, 8:55–9:02): *"99% of the time it's more about the quality of your context rather than the quantity of your context."* Corrected to include "more" in this repair pass; substance unchanged.
- Five-layer context profile (identity/role, project DNA, working files, immediate context, output specs) — **VERIFIED**, `0d1f2783…` 8:39–8:47, exact match.
- "Do the JSON thing" / JSON formatting — **VERIFIED**, `0d1f2783…` 10:55, near-exact ("Structure it. Do the JSON thing.").

### Pattern: Context Handoff Protocol
- Water-bottle memory analogy — **VERIFIED**, `0d1f2783…` 3:01–3:18, exact match.

### Insight: The Boring Layer
- "most viewed videos are the least important... the least viewed" — **VERIFIED**, `0d1f2783…` 0:28–0:33, exact match.
- "Closer Cartel did a lot of money... because we paid attention to these little things" — **VERIFIED**, `0d1f2783…` 12:09–12:18, exact match (used to correct the pre-repair version, which had genericized this to "even in info").

### Insight: Info Product Owners Are Whales
- Same buying-cars quote as above — **VERIFIED with correction** (see Problem-First Battle Selection entry).

### Insight: Staffing Is the One Human Bottleneck
- "Finding closers has to be done manual" — **UNCONFIRMED in this repair pass**. Not located verbatim in the five sources read here; the pre-repair genius.md attributed this exact phrase to Luke. Replaced in this repair with a verified adjacent quote: *"I know where to source sales reps"* / *"we're churning a lot of sales reps"* (`58b43e7b…`, 9:16–11:25), which supports the same underlying claim (staffing is manual/hard) without asserting an unverified verbatim line.

### Insight: The Ladder Has Three Rungs
- Freelancer/operator/SaaS ladder — **LIKELY**. The three-tier concept is consistent with the stack framing in `46535df5…` (2:07–2:44) but the specific "three rungs" framing as a standalone teaching moment was not isolated verbatim in this pass.
- "burnt down my businesses" (SaaS cost) — **VERIFIED**, `46535df5…` 1:01–1:03, exact match ("I stopped making money. I've literally... burnt down my businesses" — order in transcript is reversed from a natural reading; both clauses present and verbatim).

### Insight: The Service Business Is the R&D Lab
- Closer Cartel/IPO hand-written VSLs → Kendo productization — **VERIFIED**, `46535df5…` 19:42–19:47 (see Bio section) plus Kendo bio quote.

## Not Re-Verified in This Pass (out of scope, unmodified files)
- `workflows/*.md` and `references/prompts-v2/*.md` — passed `workflow_contracts` at audit time; not touched by this repair; claims inside them trace to the same 2026-07-01 harvest but were not individually re-checked against the five source transcripts in this pass.
