# Source Ledger — sarah-levinger-ad-psychology

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 15). Ground truth = `_archive/claude-export-2026-07-01.tar.gz` (332MB, UUID-named members), located via per-member content scan (`python3 tarfile` scan for `levinger`, case-insensitive, over all 7,728 members — not a filename grep, which would have missed these UUID-named files). No `extractions/` file exists for this expert (`ls extractions/ | grep -i levinger` returns nothing) — the tarball conversations are the only ground truth.

## Primary Source — VERIFIED

**File**: `_archive/claude-export-2026-07-01.tar.gz` → member `claude-export/normalized/conversations/f7154662-7772-4b23-a2bd-997afcfd91ab.md`
**Size**: 59,950 bytes (`wc -c`, confirmed against tarfile member.size)
**Conversation title**: "💎💎💰 Sarah Levinger | Micro-Movie Content | How To Script Micro Movie Ads That Scale in 2026 (Step-by-Step)"
**Created**: 2025-12-30T02:33:17Z
**Content**: Contains the full verbatim YouTube transcript (Merlin AI auto-transcription) of Sarah Levinger's video "How To Script Micro Movie Ads That Scale in 2026 (Step-by-Step)" — https://www.youtube.com/watch?v=8WRS3-y4K98 — pasted as a human-message attachment, followed by a Claude extraction pass (MES 3.0 protocol) that produced 9 artifacts. The artifact bodies themselves are NOT captured in the export (rendered as "Viewing artifacts created via the Analysis Tool web feature preview isn't yet supported on mobile" placeholders) — only the raw transcript and the assistant's planning/summary text are readable.
**Status**: VERIFIED — read in full. Every quote in genius.md's "Verbatim Exemplars" and "Anti-Patterns" sections is copied directly from this transcript and checked against the source text word-for-word.

## Secondary Source — LIKELY (continuation, no new verbatim material)

**File**: same tarball → member `claude-export/normalized/conversations/3a87573e-ff17-4822-93b1-8554ce26abb9.md`
**Size**: 19,574 bytes (`wc -c`, confirmed)
**Conversation title**: "...pt.2" (continuation of the conversation above, explicitly linking back via `https://claude.ai/chat/f7154662-7772-4b23-a2bd-997afcfd91ab`)
**Created**: 2025-12-30T16:14:31Z
**Content**: Confirms the existence and naming of a 26-prompt "Crown Jewel" arsenal built from the same extraction (Prompts #16-26), plus a summary table restating Levinger's core insight ("Different psychological profiles need different story structures to move them"). Contains no new verbatim Levinger transcript text — the artifact bodies are again unrendered placeholders.
**Status**: LIKELY — confirms this is the second half of the same two-conversation source set the predecessor worker found, and corroborates the "12 emotional avatars" count and core methodology framing already sourced from the primary file. Not used for any direct quote.

## Ruled Out (false positives from the same tarball scan)

- `claude-export/normalized/conversations/09f02312-13b3-469c-9269-d5c59b6e7fc8.md` (572,794 bytes) — mentions "Sarah Levinger's Group ($97/month)" as a Facebook-group line item inside an unrelated monetization-plan document. Not a Levinger source.
- `claude-export/normalized/conversations/16ccff47-7a6d-4b89-9d00-6285ab8f11e7.md` (33,694 bytes) — a different creator's video transcript, mentions "I was speaking to Sarah Levinger a couple of weeks ago" in passing. Not Levinger's own words; not used.

Both ruled out only after opening and reading the surrounding context (not filename-only judgment), per the "false unrecoverable/0-byte claims were caught by adversarial verification" rule in ENVELOPE.md.

## Claim-by-Claim Status (genius.md + SKILL.md + workflows)

| Claim / Quote | Status | Basis |
|---|---|---|
| "Facebook video ads are turning into micro movies in 2026, and most marketers still don't know how to write one." | VERIFIED | Verbatim, primary source, transcript opening line |
| "The product in this particular ad only shows up for about 7 seconds dead center in the video." | VERIFIED | Verbatim, primary source |
| "Under every ad, every click, every micro decision that happens in your ad account, there's really only 12 emotional avatars that are driving the show." | VERIFIED | Verbatim, primary source |
| "Story first, product second." | VERIFIED | Verbatim, primary source (closing line) |
| "the same ancient ADA driven stone tablet" | VERIFIED | Verbatim, primary source (note: source transcript literally reads "ADA," almost certainly an auto-transcription mishearing of "AIDA" — quoted exactly as it appears, not corrected) |
| "the ad is going to collapse into just like, oh, okay, yeah, that's an ad. I'm just going to skip it. Scroll." | VERIFIED | Verbatim, primary source |
| "If you introduce it too late, performance is going to tank." | VERIFIED | Verbatim, primary source |
| "I think people hear story and they imagine like novels or TED talks. None of which is going to fit inside a short ad." | VERIFIED | Verbatim, primary source |
| "You don't need to memorize story frameworks. The rule is very, very simple here." | VERIFIED | Verbatim, primary source |
| "Make sure you resolve the story in some way that the audience can take something from it." | VERIFIED | Verbatim, primary source |
| "It's pattern recognition that their brain already knows, likes, and trusts." | VERIFIED | Verbatim, primary source |
| "Tell these stories like you're explaining someone's struggle and breakthrough to a friend." | VERIFIED | Verbatim, primary source |
| "What's the emotional job this ad is trying to accomplish?" (pre-existing in genius.md before this repair) | VERIFIED | Near-verbatim, primary source: "what's the emotional job this ad is trying to accomplish?" — casing normalized only |
| "I finally feel calm," "I'm no longer overwhelmed" (pre-existing) | VERIFIED | Verbatim, primary source |
| "this avatar needs to feel X, and this structure delivers X because Y" (SKILL.md / workflow 01-02 rationale template) | LIKELY | Not a Levinger quote — a synthesized rationale template built from her matching logic (avatar → needed feeling → structure). Presented in workflows as a stated-rationale format, not attributed to her as a direct quote. Flagged here so it is never mistaken for verbatim.
| Full 12-avatar taxonomy (only Avoider, Protector, Idealist, Validator, Builder named in source) | UNCONFIRMED | Levinger states the count ("12 emotional avatars") but names only 5 in the available transcript; the remaining 7 are not in any source found. genius.md's existing "Insight: The avatar set is a lens, not a lookup table" already treats this as proprietary/unconfirmed and instructs against fabricating the missing 7 — repair preserves that framing. |
| "Sarah Levinger — performance creative strategist" (SKILL.md description) | LIKELY | Consistent with how she's described across both source conversations' framing (no independent bio source consulted; not verified against an external professional profile). |
