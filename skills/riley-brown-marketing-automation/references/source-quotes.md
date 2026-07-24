# Source Quotes & Claims Ledger — Riley Brown

Every claim in this skill traces to one of three verified Riley Brown videos + the frame-by-frame visual layer. Source tags: `[primary]` = "Codex Is Basically Running My Company Now" (2026-07-21); `[9-skills]` = "9 AI Agent Skills To Get Ahead of 99% of People"; `[news]` = "AI Agents Just Changed Forever: GLM 5.2, Codex Skills…"; `[visual]` = OCR of the primary video's screen (`extractions/riley-brown/visual-notes.md`). Auto-caption spellings preserved verbatim. **Nothing here is paraphrased into a number the source didn't say.**

---

## Direct Quotes Bank (25 — worth preserving)

1. `[primary]` "I run my entire startup inside Codeex and I use GBT 5.6... to do basically everything." — thesis / cold open.
2. `[primary]` "with coding, it's very easy to verify whether something is good or something is bad... Whereas content, it's subjective." — the verification gap (master key).
3. `[primary]` "over the last 3 years, even though AI's gotten so much smarter, it hasn't gotten any better at writing content." — why prompting isn't the fix.
4. `[primary]` "the only thing you need to do in order to create really good content is provide really good examples." — the doctrine, one line.
5. `[primary]` "we're giving a database or an API to the AI agent so that whenever it needs to create content like someone, it can just go find good examples." — retrieval layer.
6. `[primary]` "turn all of the his top performing videos into a skill. Call it Callaway top performing... so that I can write content in his style at any time." — creator-to-skill.
7. `[primary]` "this is all that is is just a file with those transcripts that we scraped." — skills are just files (the demystifier).
8. `[primary]` "I'll retain the exclusion evidence for every rejected sponsor/promotional post... those can be boosted. So it's like fake." — authenticity filter.
9. `[primary]` "the one metric that we can use... as a proxy for that is how long they've been running it. If you run an ad for nine months... presumably they're spending a lot of money keeping it alive for a good reason." — longest-running heuristic.
10. `[visual]` "'Why it works' is clearly labeled as an inference from creative durability — not proof of ROAS or profitability." — Codex's own epistemic honesty.
11. `[primary]` "I found that your limits will last quite a while if you use medium. This is a straightforward task." — effort-dialing.
12. `[primary]` "if you're on the $20 per month plan, you might only get a few of these props with this model." — cost reality (the ONLY plan-price figure Riley states).
13. `[primary]` "cal.com does not have an official plugin... get an API key paste it in and say create a skill that fully controls cow.com and it'll work one minute later." — zero-plugin bootstrapping.
14. `[primary]` "it's going to send me back a draft link where I can edit it and send it." — draft-link terminus.
15. `[primary]` "I want a draft link for all of these. I don't care how many it is." — batch-the-inbox.
16. `[primary]` "Would we ever do this word for word? We would change it more than this." — structure-theft, not copy-theft.
17. `[primary]` "please update the email draft skills so that you never say this or that... so you get it in its context." — correction written into the file.
18. `[9-skills]` "he who can describe what they want the best will inherit the world... the only enduring prompt hack is describing what you want." — describe, don't hack.
19. `[9-skills]` "I will tell the agent to do a thing, then... to make the thing better and then I'll just tell it to turn it into a skill." — skill-creation-by-doing.
20. `[9-skills]` "your skills will auto update... the future of AI agents is just auto updating skills depending on how you interact with it." — self-assembling skills.
21. `[9-skills]` "you need to become an industry expert... I understand what good looks like." — taste as the non-delegable input.
22. `[9-skills]` "If you're a good manager of people, you're going to become a good manager of agents." — foundations > tools.
23. `[9-skills]` "just for those nine prompts, it was around $250." — frontier cost / token budgeting (the ONLY dollar figure on model spend Riley states).
24. `[news]` "I recorded my screen and I taught Codex how to use Comet... and then I immediately turn into a skill." — record-and-replay.
25. `[news]` "this model... does not pass the vibe check... this was not one of those times." — the vibe-check standard for evaluating models.

---

## Claims Ledger (claim → source → verbatim anchor)

| Claim | Source | Verbatim anchor |
|---|---|---|
| The content-quality bottleneck is *verification*, not generation | `[primary]` | "with coding, it's very easy to verify... Whereas content, it's subjective" |
| Fix content quality with retrieved examples, not better prompts | `[primary]`/`[9-skills]` | "provide really good examples" / "the only enduring prompt hack is describing what you want" |
| A skill is a real file (may be a code pipeline), not a black box | `[primary]`/`[visual]` | "just a file with those transcripts" / on-screen `foreplay-competition/build_dataset.py` + 3 more |
| Codex ships first-class "New workflow" + "Memory (AGENTS.md)" commands | `[visual]` | frame_0156 slash-command palette |
| Exclude sponsored posts; keep exclusion evidence | `[primary]` | "not sponsored... I'll retain the exclusion evidence... those can be boosted. So it's like fake" |
| Ad duration is an inference proxy for ROAS, never proof | `[primary]`/`[visual]` | "a proxy... how long they've been running it" / "not proof of ROAS or profitability" |
| Per-task model + reasoning effort is a cost decision | `[primary]` | "5.6 soul... medium... straightforward task" / "turn up soul... extra high" |
| Frontier API cost is high; open-source via OpenRouter is the escape | `[9-skills]`/`[news]` | "around $250" for nine prompts / "GLM 5.2... open router... save five times" |
| Never auto-send; every action ends in an editable draft/link | `[primary]`/`[visual]` | "a draft link where I can edit it and send it" / Chorus prompt "keeping publishing... behind approval" |
| Batch email = one prompt, N voice-matched drafts | `[primary]` | "20 draft links. All of them sound like me" |
| No plugin? API key → "create a skill that fully controls X" | `[primary]` | "get an API key paste it in and say create a skill that fully controls cal.com" |
| Template-steal = structure reuse + brand swap, not word-for-word | `[primary]` | "Would we ever do this word for word? We would change it more than this" |
| **FAILURE to avoid**: the rebrand kept the competitor's real byline | `[visual]` | "Dr. Fahim Hussain" retained on the regenerated Chorus ad |
| Record a GUI workflow → Codex builds a computer-use skill | `[news]` | "Show me the Typefully draft process... it's creating this skill called manual tweet draft" |
| Promote useful one-offs to scheduled automations | `[9-skills]` | "would this be useful on a recurring basis... AI will just set up the automation" |
| Cloud agents live in iMessage/Slack, addressable like a teammate | `[9-skills]`/`[primary]` | "@chorus, I need you to do in-depth research on Alex Hormozi..." / "add this agent to your iMessage" |
| Notion DB is disposable staging; the skill is the durable asset | `[primary]` | "put the notion database just in the archive... just for testing purposes" |
| Taste is non-delegable — you can only delegate what you can judge | `[9-skills]` | "I would not be good at delegating [a DCF]... because I don't know what a good DCF analysis looks like" |
| Platforms enforce human review too | `[visual]` | Gmail AI-content banner; Buffer refuses to schedule until channel/caption/image resolve |

---

## What the Source Does NOT Establish (do not invent it)

- **No per-creator or per-scrape dollar prices.** ScrapeCreators/Foreplay/Firecrawl pricing was never stated by Riley. The only two dollar figures he gives are **"$250 for nine prompts"** and **"$20/month plan"** — both about model spend, not scraper APIs. Any "$10–50/creator", "$175–458/mo Foreplay", "$0.10/page Firecrawl" in earlier drafts was fabricated and is removed.
- **No engagement-score formula.** Riley never specifies "likes + 2×comments + 5×shares" or any weighting — that was invented. He ranks by "most engagement that are not sponsored" and by ad *duration*; nothing more precise is on record.
- **No timestamps beyond the video's own runtime.** The earlier "0:00–18:20 transcribed" scope and bracketed `[HH:MM]` citations in the old genius.md were placeholders from a half-transcript; the full transcript is now the source and quotes are tagged by *video*, not fabricated timecodes.
- **Meta Ad Library exposes no likes/views/spend/ROI for commercial ads** — runtime is the only free performance proxy. Leave those Notion fields blank; never fabricate a metric.
