---
date: 2026-07-25
session: bc-arsenal-install
tier: operator-guide
status: enriched
---

# Briar Cochran Content Science — What We Built 2026-07-25 and How to Use It

> This session turned two Briar Cochran YouTube videos into a 12-workflow content OS (`/bc-*`),
> ran it once against Farrice's real LinkedIn launch, and hardened `/scrape-creator` against the
> two bugs the run exposed. The skill decides **which ideas enter production** — it sits upstream
> of every hook/retention skill in the roster. Companion files: `skills/briar-cochran-content-science/`
> (SKILL.md + genius.md + 12 workflows + 8 v2 prompts) · `_active/linkedin-launch/04-deliverables/content-os/BC-ARSENAL-INSTALL-2026-07-25.md`
> (the LinkedIn install pack) · `extractions/briar-cochran/` (extraction-era artifacts) ·
> `docs/solutions/2026-07-25-social-intel-date-normalization-and-watch-url-parse.md`.

## ⚡ If you only read 10 lines

1. Front door: `/briar-cochran` (persona + arsenal). Flagship: `/bc-idea-gate`, `/bc-ideation-hour`, `/bc-arsenal-week`, `/bc-win-audit`.
2. **Outlier math is the whole discipline**: `views ÷ that creator's own baseline`. Act at **≥3-5×**. 100K views on a 200K-baseline account is a *flop*.
3. **Idea gate = 3 circles, all three or rework**: Proper TAM (sized to the declared goal) × Specific Psychology (insider perk-up words) × Unique/Novel.
4. **Declare the goal before sizing TAM.** A 10K-view post can beat a 250K-view post — that's the point, not a consolation.
5. **Arsenal rules**: 3-6 attempts before discarding · ≈**4:3** winners-to-tests · **≥70/30 floor** · 4-6 week lifecycle · **never an all-winners week**.
6. **Bench your winners on purpose** — repetition converts winners into auto-scroll triggers. The arsenal is a rationing device, not a trophy case.
7. **Win audit runs in strict order**: Topic → Format → Hook → Body. One primary variable or the audit failed.
8. Farrice's LinkedIn is **cold-start**: week 1 is all-test, the 4:3 ratio phases in once 3+ winners bank on real data.
9. **BURNED keywords for his ICP**: "personal brand" and "niche down" — identity threats, usable only when subverted.
10. First thing to run: `python3 execution/social_intel.py status`, then `/bc-ideation-hour` on a Sunday.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/briar-cochran` | Persona + tier-gated arsenal load | You want Briar's judgment across a whole session |
| `/bc-idea-gate` | PASS/REWORK/KILL per idea + rewritten ideas | A content queue needs honest verdicts before production |
| `/bc-ideation-hour` | 10+ idea cards, each with a named signal source | The Sunday sacred hour; you're staring at an empty week |
| `/bc-arsenal-week` | Weekly slate + updated arsenal ledger | Planning the week; deciding what to bench |
| `/bc-win-audit` | Variable-isolated postmortem + arsenal entries | Any post ≥2× baseline (standing trigger) |
| `/bc-tam` | Goal-matched TAM verdict + resized idea | An idea feels "too broad" or a viral post brought junk followers |
| `/bc-keyword-snipe` | 10-20 entry keyword ledger w/ temperature | New niche or client; keywords feel generic |
| `/bc-outlier-scan` | Baseline-relative outlier table + routes | Someone shares an "inspiring" post and you need the truth |
| `/bc-contextualize` | 4-layer transfer verdict + engineered twist | Before adapting ANY borrowed idea |
| `/bc-signal-mine` | Idea cards from sales calls, emails, DMs, comments | You have real business surfaces but aren't mining them |
| `/bc-keyword-cascade` | Kolby-style belonging-piece script | Audience-locating post; testing a fresh keyword ledger |
| `/bc-intel-bridge` | Ideation run off the Social Intelligence DB | Creators already scraped; you want deterministic baselines |
| `/bc-arsenal-install` | Full account OS install pack | New account or client onboarding |

## The mental model

**Three ideas make the rest obvious.**

**1. Content is an evidence pipeline, not a creativity lottery.** Briar's line: "Content is not a
game of guessing, it's a game of knowing. Start at one, not zero." Nothing enters production
without a named signal source. This is why the ideation hour precedes the slate, and why "I think
this is a good idea" is a rejected input.

**2. Topics beat hooks — because trust collapsed.** His stack ranks Topics → Formats →
Curiosity/Storytelling → Data analysis. In a low-trust feed, overt hooks read as manipulation, so
"the best hooks are non-hooks. They are just good ideas" stated in insider language. That's why
this skill sits *upstream* of Kallaway/Diandra/Jenny rather than competing with them.

**3. The constraint is fatigue, not supply.** Everyone optimizes the artifact; Briar optimizes the
*portfolio*. Winners get banked, rationed, and deliberately benched, because repetition turns a
winner into an auto-scroll trigger ("shadow banned by the follower," not the platform). Every
number in the arsenal rules exists to protect against that.

## The idea gate + outlier math

**What it is**: Two mechanisms that decide what's real. The Venn scores an idea on Proper TAM ×
Specific Psychology × Unique/Novel — center is "psychological alignment," the audience's ears
perking up. The outlier check computes `views ÷ the creator's own baseline average`, excluding
their own outliers from that average.

**When to reach for it**: Any time production is about to start, and any time someone says "this
went viral, we should do this."

**When NOT to**: Don't run `/bc-idea-gate` on an idea you haven't sourced — you'll get a GUESS flag
and a routing note, which is a slower path to `/bc-ideation-hour`. Go there directly. And don't use
this to analyze *why* a specific piece worked at the craft level — that's `alex-content-science`'s
Detail Stack, which is cheaper for that job.

**How to invoke**: `/bc-idea-gate` (needs ideas + niche + **declared goal per idea**) ·
`/bc-outlier-scan` (needs candidates + baseline data). Prompts:
`skills/briar-cochran-content-science/references/prompts-v2/idea-gate-scorecard.md` and
`outlier-scan-report.md`.

**Worked example**: This session's `/bc-win-audit` on Briar's own "Law of Probability" video —
baseline ≈1,500 from his recent set, actual 4,217 = **~2.8×**, verdict TOPIC primary at medium
confidence, with an isolating test designed (same framing at his standard 16-min length).
See `extractions/briar-cochran-content-science/blind-pass-sample-win-audit.md`.

**Honest edges**: The insider read-aloud is a judgment call, not a checkable rule — it's why
`/bc-keyword-snipe` demands source evidence per keyword. LinkedIn has no Apify actor in our
contract, so `/bc-outlier-scan` on LinkedIn creators is manual (reactions as the baseline proxy).

## The arsenal loop + win audit

**What it is**: Briar's adaptation of Chris Rock's club-to-Madison-Square-Garden joke testing —
broken where it fails, because content has no single key event ("we play Madison Square Garden
every single night"). So the loop is infinite: test 3-6 times, bank winners, run ≈4:3
winners-to-tests, never below 70/30, bench surplus winners, expect a 4-6 week content lifecycle.
The win audit feeds it by isolating one variable per outlier into four separate arsenals (topics,
formats, hook principles, body principles).

**When to reach for it**: Weekly planning, and every post that clearly outruns its siblings.

**When NOT to**: Not on a brand-new account for ratio purposes — cold start is correctly all-test
for weeks 1-4, and pretending you have "proven winners" on zero data is the failure mode. Also not
a substitute for analytics dashboards *at scale*: Briar's own line is that retention curves and
watch-time ratios become useful once you average ~100K views. Below that, the ledger is the 80%.

**How to invoke**: `/bc-arsenal-week` (needs ledger state + slots + Venn-passed candidates) ·
`/bc-win-audit` (needs the piece + performance **vs baseline** + comment signal). Prompts:
`arsenal-week-plan.md`, `win-audit-report.md`.

**Worked example**: Farrice's LinkedIn week 1 — 4 slots, **all tests**, ledger instantiated empty,
signal-backed candidates listed separately from "winners" (his pinned contrarian>value verdict and
the 9/10 JJ post are pre-signal, not proven on this account). See the install pack §4-5.

**Honest edges**: The 4:3 ratio and 3-6 attempt rule are Briar's stated numbers, not independently
validated on Farrice's accounts. Treat them as the starting configuration to be ratcheted by real
win audits.

## The LinkedIn arsenal install (live deployment)

**What it is**: The productized install — through-line + CCN sketch, a 14-entry keyword ledger
built from verbatim ICP-dossier language, a five-input source map with real named sources, an
instantiated arsenal ledger, week-1 slate, follower-quality dashboard, and an anti-pattern
contract naming Farrice's specific temptations.

**When to reach for it**: New account or client onboarding — it's the one-pass version of six
other workflows.

**When NOT to**: Not for a weekly refresh (that's `/bc-arsenal-week` at a fraction of the cost),
and not on an account whose funnel/goal mix is undecided — the TAM logic collapses without a
declared goal.

**How to invoke**: `/bc-arsenal-install`. Deliverable lives at
`_active/linkedin-launch/04-deliverables/content-os/BC-ARSENAL-INSTALL-2026-07-25.md`.

**Worked example**: Week-1 slate = Mon "I stopped saying personal brand" (subverts a BURNED
keyword) · Wed "Referrals… until they don't" · Thu "Brilliant in a room. Ghost online." (first
LinkedIn test of the cascade belonging close) · Fri the 40-minutes→20-seconds receipt post.

**Honest edges**: **The baseline dashboard is unfilled** — nothing in this system can read
Farrice's LinkedIn analytics, so followers/impressions/reactions/DMs are a 5-minute manual
capture. Until it's filled, outlier thresholds are uncomputable and win audits fall back to
"relative to this week's median." Subreddit member counts in the source map are candidates flagged
verify-first.

## `/scrape-creator` hardening (the bugs the run found)

**What it is**: Two fixes to `execution/social_intel.py`. `_to_date()` now parses and validates
every date shape the actors emit (ISO, `YYYYMMDD`, epoch, human `"8 Jul 2026"`) and omits the field
rather than sending malformed values — previously it truncated to 10 chars, producing `"23 Jul 202"`
and making Notion reject the entire page. `clean_handle()` now detects single-video URL markers
(`/watch`, `youtu.be/`, `/shorts/`, `/reel(s)/`, `/video/`, `/p/`), resolves them to the uploader
handle via yt-dlp at $0, and exits loudly if it can't — previously it passed `watch` through as a
creator handle and scraped a stranger's channel.

**When to reach for it**: Nothing to invoke — it's a hardening. Just know that pasting a video URL
now works, and prints a NOTE telling you what it resolved to.

**How to verify**: `python3 -c "from execution.social_intel import clean_handle;
print(clean_handle('https://www.youtube.com/watch?v=4aAQJ2jF-uc'))"` → resolves to
`BriarCochranShortForm`.

**Honest edges**: The guard resolves to the *channel*, then scrapes that channel's recent posts up
to `--limit` — it does not fetch only the one video you pasted. If your target isn't in the recent
window, backfill with the module's own `build_properties`/`build_body_blocks` (pattern in the
solution card). Two junk Notion pages from the original failure are renamed
`🗑️ [MIS-SCRAPE — SAFE TO DELETE]` and still need Farrice to delete them (the archive call is
permission-blocked and the Notion MCP cannot trash).

## Composition table (options, never a pipeline)

| Stack with | When it earns its cost |
|---|---|
| `alex-content-science` (Detail Stack) | An outlier passed `/bc-outlier-scan` and you want the invisible craft decisions behind it |
| `kallaway-*` / `diandra-*` | A gated idea needs packaging — Briar picks the topic, they craft the hook |
| `/scrape-creator` → `/bc-intel-bridge` | You track 10+ creators and want baselines computed instead of eyeballed |
| `voice-os` (VOICE-CARD + BLEND) | Any output ships under Farrice's own name — binding, not optional |
| `/writers-room` + `/ghostwrite` | Turning a slate slot into a production-grade post (writers-room is the default ≥500 chars) |
| `/voice-ratchet` | Farrice gives a felt verdict on a slate post — bank it so the ledger compounds |

## Status + what's pending

- **Tier: B.** Heartbeat gate 6/6 clear, renaissance audit 0 fail, blind pass EVAL-056 **model-judged**
  PASS. **A-tier requires Farrice's own blind pass** — do not call it A-tier before that lands.
- **Claim hygiene**: Briar's self-reported scale is UNCONFIRMED and internally inconsistent (250M
  views/month in one video, ~1B/year in another). Deploy the methodology; never cite his numbers.
- Resume with `/resume bc-arsenal-install`.
