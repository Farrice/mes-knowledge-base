# Source Ledger — shan-hanif-audience-monetization

Every claim added or referenced in this repair pass (`genius.md`'s new "How
to Use This Skill," "Anti-Patterns," and entity-floor fix lines) is traced
here and labeled VERIFIED / LIKELY / UNCONFIRMED. Primary source is a single
YouTube video transcript (`extractions/shan-hanif/transcript.txt`, **23,496
bytes**, confirmed via `wc -c` 2026-07-18). Secondary sources are the
extraction report (`extractions/shan-hanif/extraction-report.md`, **7,608
bytes**) and the validation report (`extractions/shan-hanif/validation-report.md`,
**1,535 bytes**). All three files were opened and read in full for this
repair — no "absent source" claim is made anywhere in this skill.

No enrichment/Perplexity research layer exists for this extraction —
extraction-report.md states its source as "YouTube Video Transcript (~10
mins)" only, single-source.

## VERIFIED (verbatim in `extractions/shan-hanif/transcript.txt`, confirmed by direct text search)

| Claim / Quote | Location in transcript.txt |
|---|---|
| "I've grown my LinkedIn page to 45,000 followers and generated an additional $484,000 for my agency this year." | opening lines |
| "in 2025 alone, I sold basically $484,000" / "the agency did $25 million in revenue" in 2025 | first third, business-context passage |
| "if you don't post content, you're not an expert. It's all in your head. Nobody cares. You're a ghost" | mid-transcript, positioning-rationale passage |
| "the very first thing they're going to do is Google you, find your LinkedIn, look at you" | same passage, immediately after the "ghost" line |
| "What you don't want to do is create like a swipe file. One of the worst things you can do is here's 20 prompts, here's 20 this, here's 20 pages. No insight." | lead-magnet section |
| "not stories about your journey and what you felt and like oh my mom didn't believe in me" | storytelling-content rules passage |
| "If you're celebrating eight clients, nobody wants to work with you because you are a tiny terrible agency" | same storytelling-content rules passage |
| "talk about your own launches, whatever you have without naming the clients and being lame" | educational-content passage |
| "If there was a tactical post on raising prices for clients, that is not awareness cuz it's too tactical" | awareness-content definition passage |
| Four content types: "Awareness content, educational content, storytelling content, and conversion content." | content-strategy section |
| "I actually did a 7-day lead magnet run on our socials" / sends "two emails per day" on the backend | lead-magnet-sprint passage |
| "Hijack other people's work to showcase your skill. Reverse engineer other people's businesses funnels launches." | educational-content passage |
| "I call it hot outreach. It's a madeup thing because that makes it sticky." | educational-content passage, own-framework example |
| "$97, get my retention playbook" as a tripwire example | lead-magnet examples passage |

## LIKELY (faithful synthesis of transcript content, not a single verbatim sentence)

| Claim | Basis |
|---|---|
| "Does this make me look like the best in the world?" filter (genius.md Pattern 2) | Compresses the transcript's storytelling-rules passage ("stories you need to tell," "I want to work with the guy that's a winner") into a single framing question — an accurate synthesis, not a literal quoted sentence from the source. |
| "$10M Equity Split" Hall of Fame exemplar (genius.md) | Built from the real "I give equity to my best team members early" line in the transcript; the specific "$10M ARR" post text is extraction-report illustration, not a verified real Shan Hanif post. Treat as an illustrative composite, not a reported fact about Genflow's cap table. |
| "Whoop Funnel Breakdown" Hall of Fame exemplar (genius.md) | Built from the transcript's real instruction to reverse-engineer "Gym Shark, Whoop" emails/funnels; the specific 600-word post text is an extraction-report-authored illustration, not a real published Shan Hanif post. |
| Genflow's "$100 million in revenue since we began" | Reported in the transcript as Shan's own site-copy claim ("jungflow.com... we've actually done $100 million in revenue since we began") — this is a claim ABOUT Genflow's marketing copy, not independently verified against Genflow's audited financials. |
| extraction-report.md's "Existing Overlap" ties to Justin Welsh, Daniel Priestley, Tyler Denk | Editorial framing added by the extraction pipeline, not sourced to the transcript itself. |

## UNCONFIRMED

| Claim | Why unconfirmed |
|---|---|
| Exact video title, publish date, or YouTube URL | Not present in transcript.txt or extraction-report.md — the extraction captured spoken content only, no video metadata was retained. Cite "2025" only because Shan says "in 2025 alone" about his own revenue inside the transcript, not because any file records an upload date. |
| "Gemflow" vs "Genflow" spelling | The transcript's ASR output alternates between "Gemflow" and "Genflow" in different passages (likely a transcription artifact around a similar-sounding brand name). genius.md and SKILL.md standardize on "Genflow"; both spellings are present verbatim in the raw transcript. |
| Any prior claim that source material for this skill is "unrecoverable" or the extraction folder is empty | FALSE — verified directly this pass: `extractions/shan-hanif/transcript.txt` = 23,496 bytes, `extraction-report.md` = 7,608 bytes, `validation-report.md` = 1,535 bytes (via `wc -c`, never `wc -l`). All three exist, are non-empty, and were read in full. |
