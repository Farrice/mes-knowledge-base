# Funnel math — from posts to closings (operator only; never shown to Jen as numbers)

Living doc. Update the input column monthly from the pulse (`06-system/pulse/`) and from what Jen tells Farrice about DMs, consults, and signed clients. Every rate below is a placeholder until her own number replaces it. Labels: HERS (from Jen or her account), VERIFIED (public source), UNCONFIRMED (industry rule of thumb, replace first).

Presentation rule (memory `jen-presentation-framing`): she never sees "3 closings a month" on a slide. She sees the four-stage funnel with blanks she fills. This file is where the blanks get their first guess.

## 1. Where she starts (2026-09-02)

| Input | Value | Label |
|---|---|---|
| Closings per month now | 0 to 1, mostly referral, some co-listed with the team | HERS (Farrice, 2026-09-02) |
| Followers | 2,660 (+53 since 2026-04-03) | VERIFIED (public grid) |
| Median reel views / likes / comments (last 3.5 months) | 2,578 / 107 / 13 | VERIFIED (`04-deliverables/jen-outlier-audit.md`) |
| Reels per week | ~1 | VERIFIED |
| Qualified DMs per month from posts (a street, a number, a timeline) | unknown; her posts end "let's chat" without a reason to write, so likely near zero | UNCONFIRMED, ask her for last month's count |
| Referral / sphere leads per month | unknown | ask |
| Team listing flow (MyHouseSellers, Equity Union; Marty Azoulay ~$1B career) | 2 to 4 active team listings at a time; she co-lists some | HERS / VERIFIED (Bothwell, Armida) |

## 2. The chain, and the first-guess rates

A closing comes from a signed client. A signed client comes from a consult. A consult comes from a real conversation. A conversation comes from a DM with a reason in it, or from someone who already knows her.

| Stage | Rate (first guess) | Label | What moves it |
|---|---|---|---|
| Qualified DM → real conversation (she replies same evening, they reply back) | 60% | UNCONFIRMED | saved replies + the valley file; same-evening rule |
| Conversation → consult (call, coffee, or a showing) | 35% | UNCONFIRMED | the "send me the street" ask gives her a concrete next step to offer |
| Consult → signed buyer or listing agreement | 50% | UNCONFIRMED | her strength already; she closes people who meet her |
| Signed → closed within 90 days | 60% (buyers fall out; sellers closer to 80%) | UNCONFIRMED | market; not a content lever |
| **Compound: qualified DM → closing** | **≈ 6%** | derived | **about 1 closing per 16 qualified DMs** |
| Referral / past client → closing | 25 to 35% | UNCONFIRMED | quarterly note; the "too busy" perception |

## 3. What three closings a month actually requires

| Source mix | Closings | Inputs needed per month |
|---|---|---|
| Referral + sphere + team listing flow (today's engine, made deliberate) | 1.5 | ~5 referral conversations + her share of team listings |
| Content-sourced DMs through the reply layer | 1.5 | ~25 qualified DMs from posts |
| **Total** | **3** | |

25 qualified DMs a month from an account doing ~2,600 views a post means roughly one qualified DM per 1,300 views at today's 12 posts a month, or a DM rate near 1% of viewers. That is high for cold reach. The realistic path is both levers at once:

- **Reach lever**: the outlier audit says her account moves on life-first hooks (17K, 5.3K views) and flatlines on property-first hooks (1.6K to 1.9K). A Connect district plus local content with the price signal is the cheapest way to lift median views toward 5K to 8K, which the Valley agents in the deep research already do at her follower tier (LIKELY, Gemini-sourced).
- **DM lever**: every post ends with a reason to write (a street, a number, a quote). Weeks 1 and 2 already do this. The number to watch is DMs per 1,000 views, not views.
- **Sphere lever** (off-screen, operator only): a quarterly note to past clients and friends, framed as news, not an ask. Her under-asking is the private read; the content quietly compensates.

## 4. The ramp (first guess, replace monthly)

| Month | Posts | Median views | Qualified DMs | Consults | Signed | Closings (content) | Closings (referral + team) | Total |
|---|---|---|---|---|---|---|---|---|
| Sept 2026 | 12 | 2,600 → 3,500 | 3 to 6 | 1 to 2 | 1 | 0 | 1 | 1 |
| Oct | 13 | 4,000 | 8 | 3 | 1 to 2 | 0 to 1 | 1 | 1 to 2 |
| Nov | 13 | 5,000 | 12 | 4 | 2 | 1 | 1 | 2 |
| Dec | 12 | 5,500 | 14 | 5 | 2 | 1 | 1 to 2 | 2 to 3 |
| Q1 2027 | 13/mo | 6,000 to 8,000 | 20 to 25 | 7 to 9 | 3 to 4 | 1 to 2 | 1.5 | **3** |

Coffee & Contracts' own honesty in the webinar: leads at roughly three months, "not a quick win," "go all in for 90 days." This ramp is that claim applied to her numbers. If Q1 2027 arrives and content closings are still zero, the funnel tells you which stage broke: views (reach lever), DMs per 1,000 views (ask lever), or consult rate (reply layer). Fix that stage, not the whole system.

## 5. What content cannot do

- It cannot close. She closes. The reply layer is where a DM becomes a consult, and that is her thumb on her phone the same evening.
- It cannot replace the sphere. Half the goal comes from people who already know her. That half needs the quarterly note and the team's listing flow, not another post.
- It cannot be judged by likes. The scoreboard she'll believe (ENGINE-V2 §10) stays: DMs with a street, a number, or a timeline, per month. This file adds the operator's second column: consults and signed, so the 6% compound can be replaced with hers.

## 6. Monthly read (first of the month, operator)

1. Run the pulse (`execution/jen_pulse.py`) for views, likes, comments per post; append to `06-system/pulse/`.
2. Ask Farrice for the month's DM count with a reason in it, consults, signed, closed. Four numbers, one text.
3. Replace the UNCONFIRMED rates above with hers. Re-derive the compound.
4. Run `/alyssa-stalker-outlier-audit` on the month. Name the attribute. Feed next month's Connect and Attract slots.
5. Write one line to Jen, in her frame: "here's who wrote in this month, and what we're posting next." Never the funnel.
