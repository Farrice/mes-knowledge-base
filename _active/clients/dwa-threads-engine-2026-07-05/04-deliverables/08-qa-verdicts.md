# DWA Threads — QA Verdicts

_Scannable pass/fail summary of the 5-piece test kit. Full reasoning lives in the QA transcript; this table is the at-a-glance dashboard. Composite = average of the 5 axes, not a gate by itself — the veto conditions below are what actually block shipping._

**Veto conditions (any one blocks shipping regardless of composite):** an unhedged UNCONFIRMED claim stated as fact; an explicit income number/`$X/month` claim; a banned voice MOVE (twin-reveal, triple anaphora, >2 em-dashes, cheap question sign-off); a missing/late affiliate disclosure on a piece that carries a link.

| ID | Angle | Role | Verdict | Premise | Evidence | Voice | Structure | Market Resilience | Composite | Flags (hard) | Top fix |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-adherence-coach | A | Spearhead | SHIP_WITH_FIXES | 8 | 6 | 6 | 7 | 7 | 6.8 | Negation-then-reveal construction functionally = banned twin-reveal MOVE; timeline inconsistency (week two vs week three); LIKELY 40,000-affiliate stat stated as flat fact; zero disclosure token anywhere in the 5-post chain despite endorsing a paid course throughout | Rewrite the negation sentence in post 1 as one forward-moving statement; pick one quit-timeline number and use it consistently; add a light disclosure cue inside the chain itself, not only in the separate pinned post |
| 02-sahd-not-guru | B | Spearhead | SHIP_WITH_FIXES | 7 | 6 | 5 | 7 | 6 | 6.2 | Negate-then-redirect construction = banned twin-reveal MOVE; missing disqualify line (credential + zero-income-claims present, disqualifier absent — research doc requires all three together); DWA-specific causal claim stated as fact with no data behind it; em-dash self-check undercounted (claims 1, actual 2 — still under the 2-max limit but drifted) | Add a one-line disqualifier borrowed from Angle G to complete the required triad; soften the DWA-causal-claim line to disclosed professional opinion, not verdict; lock a deployment rule so post 1 never runs as a standalone original post outside the 3-post thread |
| 03-progressive-overload | C | Spearhead | SHIP_WITH_FIXES | 8 | 5 | 8 | 6 | 6 | 6.6 | **Hard Rule 1 violation** — contains explicit dollar figures framed as observed/typical outcomes ("$5K a month over three years," "the starting weight is one thousand dollars") with no hedge, reading as implied-earnings claims; close ("go load your first plate") under-specifies the actual mechanic (no named product, no link, no disclosure, no explicit next action) | Strip or de-quantify the dollar figures — reframe as niche marketing language, not achieved/expected outcomes; make the close name the actual mechanic (link + disclosure + receipt-DM bonus live on the pinned post); cut "Lambo money" even as a disqualifier — it echoes the exact burned trope it's trying to reject |
| 04-first-1k-belief-unlock | E | **Pinned offer post** | SHIP_WITH_FIXES | 8 | 5 | 6 | 6 | 6 | 6.2 | Asserts the UNCONFIRMED session-only-vs-cookie attribution mechanic as settled fact, framed as a transparency flex — highest-cost overclaim in the kit if wrong; contrast-pivot rhetoric in two lines is the twin-reveal MOVE folded into single sentences rather than fixed; length likely exceeds one Threads post, meaning the link-in-first-post same-session mechanic depends on confirming which numbered post actually carries the link | Verify session-only vs. cookie in the DWA portal before posting; until confirmed, describe buyer-facing behavior only ("buy through today's click"), not the technical claim; rewrite both contrast-pivot lines as straight declaratives; cut the stock "one thing nobody says out loud" insider-secret tell; specify exactly which post in the thread carries the link |
| 05-coach-not-buy | G | Integrity screen | SHIP_WITH_FIXES | 8 | 6 | 7 | 7 | 8 | 7.2 | None hard — this is the strongest construction in the kit (credential + disqualify + zero income claims + explicit "no countdown, no catch," photo direction deliberately anti-guru). Soft-only notes: never names the "scam" objection directly despite the frame being built for it; two closing lines across the piece share the same short-punch call-and-response cadence, bordering the banned twin-sentence aphoristic-ending pattern | Name the actual product instead of only "the AI marketing course I put my name behind"; add one direct line preempting the scam/pyramid association; vary the two closing cadences so neither reads as a template; confirm with Farrice whether the "told a client to leave, cash in hand" detail is literal or composite before it's used as an emotionally load-bearing beat |

## Cross-cutting pattern (applies to all 5 pieces)

Every piece in the kit shares one structural risk the individual QA passes flag repeatedly: **Threads' feed-consumption pattern means most viewers will only ever see post 1**, and post 1 in isolation is often pure behavioral insight with no money/action mechanic attached — technically compliant with Hard Rule 5 only because the full multi-post thread eventually pairs insight with mechanic. If a reader never taps to continue, the standalone impression can read as introspection/therapy rather than an offer-adjacent piece, which is exactly the failure mode research counter-read #2 warns about.

**Standing fix, not piece-specific:** every post 1 across the kit should carry a faint forward-signal — a half-beat that there's a mechanic coming — without diluting the hook itself. Track this as a template-level fix, not a one-off, before scaling past the 5-piece test kit.

## Ship gate

All 5 pieces are `SHIP_WITH_FIXES`, not `SHIP` and not `BLOCKED`. None are cleared to post as-is. The two fixes with the highest cost if skipped:

1. **03-progressive-overload's dollar figures** — this is the one clean Hard Rule 1 violation in the kit (implied earnings language), not a soft voice note. Fix before this piece goes anywhere near "post."
2. **04-first-1k-belief-unlock's unhedged UNCONFIRMED claim** — this is the pinned post, the highest-traffic single asset in the campaign, and the one place where getting caught overclaiming certainty (about a portal mechanic Farrice hasn't verified) does the most reputational damage. Verify in-portal before this pins.

---

## FIXES APPLIED (Opus final pass, 2026-07-05) — all 5 now SHIP-ready pending human gates

Every SHIP_WITH_FIXES flag above was resolved in the copy blocks:

| ID | What was fixed |
|---|---|
| 01-adherence-coach | Post 1 negation twin-reveal rewritten forward + forward-signal added ("it's the whole thing I fix"); timeline unified to "week two"; "40,000" hedged to "thousands"; DWA named; real disclosure token added to Post 5. |
| 02-sahd-not-guru | Post 1 twin-reveal + DWA-causal-claim rewritten to disclosed professional read ("in my experience it's rarely the material") + forward-signal; disqualifier added to Post 3 (completes credential+disqualify+zero-income triad); explicit disclosure added; echo removed from Post 2. |
| 03-progressive-overload | **Hard Rule 1 fixed** — implied-earnings dollar figures ("$5K/mo over three years," "one thousand dollars") stripped/de-quantified to goalpost + "your first sale" language; "Lambo money" trope cut; close now names DWA + routes to link/disclosure/receipt-DM on pinned post. |
| 04-first-1k-belief-unlock | **Restructured into a proper ≤500-char chain with the link in the pinned ROOT post**; unverified "session-not-cookie" claim rewritten to buyer-facing behavior only ("buy through today's click"); contrast-pivots straightened; "nobody says out loud" tell cut. |
| 05-coach-not-buy | Product named (Digital Wealth Academy); direct scam/pyramid pre-empt line added to Post 4; twin closing cadences varied; production note added flagging the "client left, cash in hand" anecdote for literal/composite confirmation. |

**Remaining gates are HUMAN, not copy** (Farrice-owned): (1) verify DWA portal facts — portal URL, processor/payout, attribution window; (2) paste the real affiliate link into 04; (3) confirm the Post-1 anecdote in 05 is true/fair-composite. Cross-cutting standing rule for scaling past the test kit: give every future Post 1 a forward-signal so it never reads as therapy in isolation.
