# Source Ledger — Matthew Volkwyn Copywriting

Ground truth for `skills/matthew-volkwyn-copywriting/` is four YouTube video transcripts (captured via Merlin AI, pasted into claude.ai extraction conversations), recovered from `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes). No `extractions/` folder exists for this expert — the tarball's `claude-export/normalized/conversations/` .md files are the only recoverable primary source. Located via Python `tarfile` per-member content scan for the name fragment `volkwyn` (no filename matches; 8 content matches out of 7,720 scanned members).

## Source Files (verified present, sizes recorded via `wc -c`)

| File (in `claude-export/normalized/conversations/`) | Size (bytes) | Video | Captured |
|---|---|---|---|
| `322ccc3e-29b8-4b12-a56f-9f096fc1b6e6.md` | 67,539 | "This Undefeated Formula Will Upgrade Your Copy Forever" (youtube.com/watch?v=MitGHiVLyDs) | 2025-12-16 |
| `3a833402-8557-46ee-9d4e-d79348682f5b.md` | 43,370 | same video, earlier extraction pass | 2025-11-08 |
| `4800d2a3-a469-4bef-b03c-a8b450b8a93c.md` | 44,435 | same video, mid extraction pass | 2025-11-28 |
| `a758766f-5abe-4753-b4c8-f9c6ce01c1cb.md` | 119,251 | "Why Most Copywriters Should QUIT Before 2026" (youtube.com/watch?v=wLKzjypbLV8) | 2025-11-28 |
| `279b2893-89e5-49ca-a549-f389828f4f05.md` | 73,577 | "The Highest Paying Copywriting Project In The World" (youtube.com/watch?v=yq5L4UJY8CE) | 2026-01-04 |
| `2d0d2d75-be44-4afb-b6c1-fe24e83c3eee.md` | 102,159 | "The Complete Guide To Successful Copywriting In 2026" (youtube.com/watch?v=yHVFm78w4f8), earlier pass | 2026-01-29 |
| `ba9ec284-2b99-400c-95c7-b68039c481ff.md` | 147,345 | same video, later/final pass | 2026-01-30 |
| `claude-export/raw/batch-0001/conversations.json` | 867,859,945 | raw JSON containing all of the above pre-normalization | n/a |

Note on transcript quality: the Merlin AI ASR renders the word "close" (as in sales close) as **"clothes"** throughout — e.g. "the conditional clothes, the assumptive clothes, the crossroad clothes, the direct clothes, the hidden clothes." Confirmed as a homophone transcription artifact by cross-reading surrounding sentences about email closes/CTAs, not a distinct claim. Normalized to "close" in the skill files.

## Claims — VERIFIED / LIKELY / UNCONFIRMED

| Claim | Label | Anchor |
|---|---|---|
| Four-element audit (Hook, Flow, Close, Voice) as Volkwyn's self-critique method | VERIFIED | `322ccc3e...md`: "There are four things I would recommend that you start with when you critique your own copy. The first one is hooks... [Flow]... Close... Voice." |
| Dual-lens hook standard (emotionally compelling + intellectually interesting) | VERIFIED | `322ccc3e...md`: "a hook needs to have a benefit... emotionally compelling but you also need something that's intellectually interesting" |
| "How to make money online" vs. "16-year-old made $300 yesterday from his bed" example | VERIFIED | `322ccc3e...md`, verbatim match |
| "Reverse pyramid fitness system" vs. "reverse pyramid for 3 weeks and lost 10 lb" example | VERIFIED | `322ccc3e...md`, verbatim match |
| Three subconscious questions: "Have I seen this before? / Why do I care? / So what?" | VERIFIED | `322ccc3e...md`, verbatim sequence |
| Three-question flow model: "what is this? / what does that have to do with me? / what should I do about it?" | VERIFIED | `322ccc3e...md`, verbatim (three separate passages) |
| Five named closes: conditional, assumptive, crossroad, direct, hidden | VERIFIED | `322ccc3e...md` + `3a833402...md` + `4800d2a3...md` (three independent transcript captures agree, modulo the "close"/"clothes" ASR artifact) |
| "Click here" bare-link close as the default failure | VERIFIED | `322ccc3e...md`: "it's kind of like click here" |
| 8/10 submission threshold | VERIFIED | `322ccc3e...md`: "I would not submit stuff until I feel like... it's an 8 out of 10" |
| Generic Copy Test ("could I use this for any business") | VERIFIED | `322ccc3e...md`: "can I use this copy and use it for any business and it'll still work. If you can, then the copy is kind of generic." |
| Voice Trinity: Style / Personality / Values | VERIFIED | `322ccc3e...md`: "there are three elements to voice" (Style/Personality/Values enumerated in the extraction artifact built from the same transcript) |
| "Never break the magic" — one off-voice line ends reader trust | VERIFIED | `322ccc3e...md`: "if you break the magic and it becomes obvious that it's not them, then they don't trust you anymore... they won't read the emails" |
| "You don't have an income problem, you have a skill problem" (client's phrase) | VERIFIED | `322ccc3e...md` / `3a833402...md`: "one of my old clients loves saying you don't have an income problem you have a skill problem" |
| Dan Martell's "build the team and the team will build the business" | VERIFIED | `322ccc3e...md` / `3a833402...md`: "When I was writing for Dan Martell he would say something like build the team and the team will build the business" |
| Seven years freelancing before coaching | VERIFIED | `a758766f...md`: "I've actually been running a freelance business myself as a copywriter for I think I ran it for seven years" |
| ~99% coaching satisfaction rate, ~2 refunds on record | VERIFIED | `a758766f...md`: "99% satisfaction client success rate... I can only think of two... refunds on record in the entire time I've done the coaching" |
| Nine months to close first client | VERIFIED | `a758766f...md`: "When I started it took me 9 months to close my first copyrightiting client" |
| Two-to-three emails, ~$200K in ~16 hours, last email ~40% of revenue | VERIFIED | `a758766f...md`: "we generated like a fifth of a million dollars... in 16 hours by from like these three emails... the last email it generated like $80,000. So, I think that's like a what 40% of the revenue." ($80K / ~$200K ≈ 40%, internally consistent) |
| Full-stack copywriter demand / "sorry I only do email" no longer sufficient | VERIFIED | `a758766f...md`: "they wanted a copywriter who could do more than just email... they want you to have the full stack copyrightiting skill set" |
| Systems vs. strategy distinction (numbered steps vs. overall approach) | VERIFIED | `a758766f...md`: "a system is different to a strategy because a strategy is the overall approach... the system[atized version]... more" |
| Mass cold outreach / "copy gurus" flooding the market, damaging email-copy demand | VERIFIED | `279b2893...md`: "they all sent thousands and thousands of cold outreach emails... They would burn the email list. They would write bad copy. They would damage the brand." |
| "200+ private copywriters coached" (used in SKILL.md/genius.md/AGENT.md) | LIKELY | Volkwyn's own number in `2d0d2d75...md` / `ba9ec284...md` is "in 2025, we helped 100 private clients and another 300 copers through our courses" (100 private + 300 course = 400 total, not a clean "200+ privately coached" figure). "200+ private copywriters" appears only in the AI extraction's own summary metadata (`a758766f...md` header), not in Volkwyn's spoken words. Downgraded from the skill's implicit VERIFIED framing — the underlying scale claim (hundreds coached, high satisfaction) holds, but the exact "200+" figure is the extraction tool's paraphrase, not a direct quote. |
| "AI amplifies skill, it doesn't create it" (as a direct Volkwyn line) | LIKELY | Closest source is `322ccc3e...md`: "this is one of the things AI can't [do]... if you know what you're doing. But this is why we still need copyrighters..." — the concept is Volkwyn's, the crisp phrasing in the skill is a paraphrase/compression, not verbatim. |
| Volkwyn "refused to become a beginner-dream copy guru" | LIKELY | `a758766f...md` confirms he was asked directly "why you decided to not go the copy guru way" and answers at length about reputation and longevity; the skill's framing ("despite having the positioning to print money doing it") is a fair synthesis of that answer, not a single quote. |
| Any claim of an "extractions/" source file for this expert | UNCONFIRMED — CORRECTED | No `extractions/` directory entry exists for Volkwyn (`ls extractions/ | grep -i volk` returns nothing). SKILL.md's `source: claude.ai export 2026-07-01` header is accurate; ground truth lives only in the tarball, not in `extractions/`. This ledger corrects any prior implicit assumption of an extractions-folder source. |

## Search Method (per envelope discipline)

1. `ls extractions/ | grep -i volkwyn` and `grep -i matthew` — zero matches (confirmed with a second listing of all 193 top-level `extractions/` entries).
2. `find . -iname "*volkwyn*"` — confirmed only `agents/matthew-volkwyn/`, `skills/matthew-volkwyn-copywriting/`, and `.claude/commands/` matches; no standalone transcript file anywhere in the repo outside the tarball.
3. Located `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `ls -la`).
4. Python `tarfile.open(..., 'r:gz')`, iterated all 7,720 file members (name fragment `volkwyn`, no punctuation, case-folded) — 0 filename matches.
5. Full per-member content scan (decode as UTF-8, case-fold, search `volkwyn`) across all 7,720 members — 8 matches, sizes recorded above via Python `len(data)` (equivalent to `wc -c`).
6. Extracted the 7 normalized `.md` matches to scratchpad; verified each with `wc -c` and `grep -io -c volkwyn` before quoting; did not open the 868MB raw JSON (redundant with the normalized `.md` files, which are the intended readable source).
7. Every quote used in `genius.md`'s Anti-Patterns section and every VERIFIED row above was located with `str.find()` against the raw extracted text and read with ±150-300 char context before being copied — no quote was taken from the skill's own prior text without re-finding it in source.
