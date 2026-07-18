# Source Ledger — henrik-werdelin-portfolio-entrepreneurship

Ground truth for this skill is **not** under `extractions/` — `ls extractions/ | grep -i
werdelin` returns nothing (confirmed this repair pass, exit code 1, no match against
the full `extractions/` listing). SKILL.md's own frontmatter already names the correct
source: `source: claude.ai export 2026-07-01`. That export is `_archive/claude-export-
2026-07-01.tar.gz` (332,779,255 bytes — confirmed via `ls -la`, not 0-byte, not
unrecoverable). The four Werdelin-titled conversations inside it were located via
`_active/claude-export/index.json` (which lists conversation metadata + `md_path`
pointers) and extracted from the tarball this pass with `tar -xzf ... claude-export/
normalized/conversations/<id>.md`:

| File (in tarball) | Size | Content |
|---|---|---|
| `fab47f59-569e-49c8-ba8a-29ea621fe9f9.md` | 89,824 bytes | Full raw YouTube transcript (timestamped, `MM:SS -` format) of "Everyone's an AI Founder Now. Here's What Set Some Apart." — the primary anchor source for this pass; all timestamp citations below reference this file. |
| `156550f6-a849-4598-91b7-25d096d72413.md` | 105,691 bytes | Same underlying interview, different transcript capture (untimestamped, prose-run) titled "Building AI Agents That Launch a Million Businesses," plus the original MES 3.0 extraction conversation (genius patterns, prompts) built from it. Used to cross-verify quotes already present in genius.md/SKILL.md. |
| `55425dfe-df69-4a74-adb1-cb2c60fd6434.md` | 25,431 bytes | Follow-on extraction conversation (Five Ps prompting framework request) — no new raw transcript, analysis-only. |
| `94abf42c-387a-400a-8062-89cf5c3d9382.md` | 10,241 bytes | Follow-on extraction conversation (continuation of crown-jewel prompts) — no new raw transcript, analysis-only. |

VERIFIED = quote located verbatim via `grep -n` against the extracted `.md` file, cited
with file + timestamp/line. LIKELY = a plausible bio/context fact not independently
locatable in the transcript text this pass. UNCONFIRMED = no anchor found; flagged, not
asserted.

## Bio / Identity Claims

| Claim | Label | Basis |
|---|---|---|
| Henrik Werdelin is co-founder of Prehype (startup studio) | VERIFIED | Transcript intro, `fab47f59...md`: "co-founder of the Startup Studio Prehype." |
| Co-founder of BarkBox | VERIFIED | Transcript, `fab47f59...md`: "the co-founder of Barkbox." |
| Co-founder of Autos (AI entrepreneurship platform) | VERIFIED | Transcript, `fab47f59...md`: "he's one of the co-founders of Autos, which has the goal to help millions of people become entrepreneurs with AI." |
| Author of a book on relationship capital (referred to in-transcript as "Me by Customer") | LIKELY | Transcript line ~2019 area, `fab47f59...md`: "I wrote this book called Me by Customer." Auto-transcription quality on proper nouns is imperfect elsewhere in this file (e.g. "Prehype" renders as "prehab," a company named "Ro" renders as "Rorow"), so the exact title is carried as spoken but not cross-checked against a second, cleaner source this pass. |
| Podcast "Beyond the Prompt" with Stanford Professor Jeremy Oley | LIKELY | Transcript, `fab47f59...md`: "I have a podcast called Beyond the Prompt with Stanford Professor Jeremy Oley." Same auto-transcription caveat — the professor's name may be mis-rendered by the transcript tool; not independently verified against a second source this pass. |
| Host of the interview is Dan Shipper (Every / "AI & I") | LIKELY | Inferred from the outro reference "Dan Shipper as the captain of the spaceship" and prior familiarity ("his startup studio prehype is actually where my company ever came from" — points to Every, Dan Shipper's company). Not independently verified this pass. |
| "Ro" (men's telehealth company referenced as coming out of Prehype) | UNCONFIRMED | Transcript renders the company name as "Rorow" (auto-transcription artifact): "you take Rorow, which obviously also came out of the prehab world... they basically solve medical problems for men... hair loss or ED or or weight loss." This reads as the real company Ro (formerly Roman), but the transcript text itself does not spell the name cleanly enough to assert it — flagged UNCONFIRMED rather than silently corrected. Not used as a named entity anywhere in genius.md/SKILL.md for this reason. |

## Genius Patterns / Anti-Patterns — Quote Verification

| Claim / Quote | Label | Basis |
|---|---|---|
| "You can't start with an idea. You can't start with a technology. You can't start with a market size. You have to start with who do you want to serve for the next 10 years" | VERIFIED | `fab47f59...md` transcript body (embedded in human turn, ~line 30); matches `156550f6...md` line 30 verbatim. |
| Five Ps: "these are five ways you can look at yourself and figure out where do I have something innate in me that I can extract from and then build something around" | VERIFIED | `fab47f59...md` transcript body; matches `156550f6...md` line 30. |
| "60% of Americans say they like to start something only ~8% does" / donkeycorn definition | LIKELY (discrepancy flagged) | Both independent transcript captures of this passage — `fab47f59...md` timestamp 11:42–11:55 and `156550f6...md` (same passage) — literally read "60% of Americans say they like to start something only 80% does," not 8%. Read literally this is incoherent (80% doing exceeds 60% wanting to), so it is almost certainly a mis-hearing of "8%" by the transcription tool, and genius.md/SKILL.md's existing "~8%" figure is the sensible reading. But because neither source file actually contains the digit sequence "8%" in this passage (only "80%"), this is downgraded from VERIFIED to LIKELY rather than certified as an exact-match quote — flagged for the adversarial verifier rather than silently corrected. |
| Relationship capital 3 Ds (Depth/Density/Durability) + "if you look at everything that came out of prehype over 15 years, it's basically these relationship capital companies" | VERIFIED | `fab47f59...md` timestamp 16:30 ("prehype over 15 years, it's basically") through the Depth/Density/Durability explanation later in the same turn. |
| Nike Hotel vs Hilton Shoe test | VERIFIED | `fab47f59...md` transcript body (embedded in human turn and repeated by Werdelin later): "you can imagine what a Nike hotel would look like, but it's very difficult to compute what a Hilton shoe would be." |
| Dunbar Squared ("dumbba square," ~22,500 TAM) | VERIFIED | `fab47f59...md` transcript body: "the dumba rule is going to work in an AI world too but it's going to be uh exponential so we call it dumbba square so that the tam of a good customer group is 150 lifted in seconds so 200 20,500" [auto-transcription garbles "150 squared" and "22,500"; genius.md/SKILL.md use the corrected math (150² = 22,500), which is arithmetically what the passage is describing]. |
| Cool Shit Paradox quote | VERIFIED | `fab47f59...md` transcript body: "every time that I try to build something to make it successful, I end up not building something great. And every time I basically go for I want to build cool [bleeped] with people I like, then I end up doing something that seems to resonate with people." |
| Label Model / royalty structure | VERIFIED | `fab47f59...md` timestamp 59:53–59:56: "we take a royalty. So we don't take equity in their business. We just take a royalty on the top line." |
| Supporting Actor / Motown studio model | VERIFIED | `fab47f59...md` transcript body: "if you really study the Mottown of the world or um um the one in London... where Beatles had their stuff and there's one in Sweden where Max Martin kind of did a lot of like the... pop music." (genius.md's "Motown model" phrase is the correct spelling of the transcript's "Mottown" auto-caption artifact.) |
| Multi-agent venture architecture quote | VERIFIED | `fab47f59...md` transcript body: "there won't be that many one agent businesses... a founder will serve a customer and then they will have multiple agents that will have to be part of this portfolio of tools that they offer to their customers." |
| In-Between Time / post-IPO conference anecdote | VERIFIED | `fab47f59...md` timestamp 24:36–25:00: "after we went public I took a little bit of time where I didn't do much... I went to this very high-end conference and my feeling was that I had like a year where I still would be invited back to that... I got really worried of losing relevancy." |
| Micro-Moments framework | VERIFIED | `fab47f59...md` transcript body: "I did this thing where I wrote down all them what I call micromones... these 30 kind of concrete periods where I've done stuff and then I started to use that as a way to measure options." (genius.md's "inventory the last 90 days" is a reasonable operationalization, not a direct quote — the transcript gives "30" moments, not a 90-day window; the 90-day figure is not independently verified against this transcript and should be read as a suggested cadence, not a Werdelin-stated number.) |
| ChatGPT vs Instagram "for you page" contrast | VERIFIED | `fab47f59...md` timestamp 51:17–51:23: "if I asked you know ChatGPT to make me a for you page versus my Instagram for you page. Chbt is super wholesome and Instagram is like the trashiest slop." [transcript renders "ChatGPT" as "Chbt" in the second instance — auto-caption artifact, corrected in genius.md]. |
| "The club of people who think about new stuff" | VERIFIED | `fab47f59...md` transcript body: "the the the urge and need to be part of that club of people who think about new stuff." |
| Startups as a way of life vs means to an end | VERIFIED | `fab47f59...md` timestamp 27:52–28:34: "there's a there's two ways of running companies. It's um startups as a means to an end and startups as a way of life... you don't need to get away. I don't need to have that like one final like it's over I'm out." |
| VC-Defined Focus Dogma anti-pattern | VERIFIED | `fab47f59...md` timestamp 2:30–2:34: "this thing about uh oh you have to focus and and and so having a portfolio sucks." |
| EIR Mistake anti-pattern | VERIFIED | `fab47f59...md` timestamp 15:31–15:44: "the mistake that I see a lot of people do when they come to me and they're like I'm going to do an EIR thing is they are they're running one business... in a totally different area with a totally different customer." |
| Cat Box Trap anti-pattern | VERIFIED | `fab47f59...md` timestamp 16:38–16:48: "We never defined ourselves as a company that puts stuff in boxes cuz then our next business would have been the cat box." |
| Putting On A Show anti-pattern | VERIFIED | `fab47f59...md` timestamp 20:56–21:14: "I'm just putting on a show so that I can like raise the next around for the next year or so... I don't really love whatever I'm doing, but I'm just going to put on a show." |
| Revealed-Preference Optimization anti-pattern | VERIFIED | `fab47f59...md` timestamp 50:31–50:50: "the social web operated on... revealed preference... the reality is that you're always going to click on a car crash and so that's where things go. They get more extreme." |
| MBTI-as-settled-science anti-pattern | VERIFIED | `fab47f59...md` timestamp 54:04–54:20: "this whole thing had been debunked and you shouldn't use it at all. I think it's useful if you like it's useful if you think about it as um a story that you can try on." |

## Notes for the adversarial verifier

- Every VERIFIED quote above can be located with `grep -n "<distinctive fragment>"
  claude-export/normalized/conversations/fab47f59-569e-49c8-ba8a-29ea621fe9f9.md` after
  extracting that path from `_archive/claude-export-2026-07-01.tar.gz` (this repair
  pass extracted it to a scratch dir; the tarball itself is untouched, read-only).
- This is a raw, non-professional auto-transcription (Merlin AI transcript of a YouTube
  video) — several proper nouns render corrupted ("Prehype" → "prehab," "Ro" → "Rorow,"
  "Mottown" for Motown, "Chbt" for ChatGPT, "dumba"/"dumbba" for Dunbar). Where genius.md
  or SKILL.md use the corrected spelling, that correction is noted above; the "Ro"/
  "Rorow" company identity specifically was judged too uncertain to assert and is
  UNCONFIRMED, not used as a named entity in the repaired files.
- No claim in the repaired genius.md is asserted as VERIFIED without appearing in this
  table.
