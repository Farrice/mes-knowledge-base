# Amendments to ENGINE-V2 from the outlier audit and the Alyssa Stalker extraction (record, 2026-09-02)

> **FOLDED 2026-09-02 (same evening), after both lanes merged into main.** ENGINE-V2 §4 (four jobs), §5 (format test), §8 (monthly rhythm), §10 (operator column), §11 (parity pointer), §13–15 (open items, vault, surface) now carry this content; `VAULT.md` exists. This file stays as the record of why.

Operator only. `ENGINE-V2.md` is the living operating doc and lives in lane `worktree-jen-engine-v2-weeks`; this lane (`worktree-broke-agent-2026-playbook-forge`) cannot edit it. Fold these in when that lane merges. Each amendment names the section, the evidence, and the exact text to add. Nothing here changes the deal, the look, the realism gate, or the reply layer.

## Merge order

1. `worktree-jen-engine-v2-weeks` first (ENGINE-V2, Valley Editions, weeks 1–2, edition-01).
2. This lane second (Alyssa skill, outlier audit, funnel math, Connect posts, these amendments). The only shared file is `_active/clients/jen-listings/CLAUDE.md` (one added row); no other overlap.

## A. §4 Districts: add a fourth job, **Connect** (evidence-backed)

**Evidence.** `04-deliverables/jen-outlier-audit.md`, public numbers 2026-09-02. Her account's outliers are all life-first: Coachella with a 2-year-old (17K views, 1,172 likes, 6.6× baseline), "if he won't hold the standard" (5,285 views, 79 comments), the pizza-and-Farrice origin story (3,131 views, 161 likes). Personal-lens hooks median 161 likes; property-first hooks median 78. The only real-estate post in window that broke out was the budget-vs-wishlist humor reel, 38 comments, 2.9× median: comfort content in Alyssa Stalker's sense (a feeling first, real estate second). Alyssa's own account grew 50% in a year on exactly this (source: `extractions/alyssa-stalker-agent-content-playbook/`).

**Why it isn't already covered.** Attract is place + price. Position is a market fact. Convert is a listing. None of the three has a slot for "what does the audience need to know about me in order to like me, trust me, and then work with me" (Alyssa, [09:32–09:40]). ENGINE-V2 §12 borrowed the 40/30/20/10 ratio whose 30% is "trust"; the districts table dropped it.

**Text to add to §4 (new row):**

| **Connect** (they get to know her) | ~20% (one of every five posts) | Her life and her feelings about the work, from the archive: "just breathe," "lipstick remodel," "everything works out," the Valley view she's a sucker for, the boy-mom-raver-realtor line. A feeling first, real estate second, offer last as permission. Never a tip in a comfort costume. | Send it to someone ("this is us"), or reply with a feeling: "same," "ugh, the numbers," "we're stuck." |

**Ratio adjustment:** Attract 35 / Position 30 / Connect 20 / Convert 15 while listings are active; Convert's slot goes to Position when there is no listing. First guess; the monthly read decides.

**Source of Connect copy:** the five voice memos and thirty-plus captions already transcribed. No new ask on Jen. First four posts: `04-deliverables/connect-posts-01/COPY.md`.

## B. §5 Formats: note the outlier evidence on format

Carousels are untested on her grid (zero in window). Alyssa reports carousels outperform reels "by far" for her and that single-image posts are back; Jen's own data cannot confirm or deny yet. Keep the two-beat photo card and add: **run one comfort post as a carousel and one as a single card in the same month and read the saves.** Do not decide format by taste; decide by the pulse.

## C. §8 Cadence: add the monthly rhythm (what Coffee & Contracts sells as "the dashboard")

| When | What | Who | Tool |
|---|---|---|---|
| Sunday | Week's drop into Drive 04 (3 posts, captions, day plan, saved replies) | us | `build_weeks.py` (v2 lane) |
| Sunday | Thumbs-up on the preview | Jen, 30 seconds | iMessage |
| Tue / Thu / Sat | Posts go out; same-evening replies from saved replies | Jen | Meta Business Suite later |
| Every Monday | Pulse: views, likes, comments per post appended to `06-system/pulse/` | script | `execution/jen_pulse.py` |
| 1st of month | Outlier audit on the month; name the attribute; set next month's Connect + Attract | us | `/alyssa-stalker-outlier-audit` |
| 1st of month | Four numbers from Farrice (qualified DMs, consults, signed, closed) into `FUNNEL-MATH.md` | Farrice | one text |
| 1st of month | Facts re-check on anything still live (comps, rates, FAIR Plan) | us | `FACTS.md` re-check column |
| 1st of month | One line to Jen: who wrote in, what's next. Never the funnel | us | iMessage |
| Quarterly | Twenty-minute car chat (framed as coffee) to refill the archive | Jen | voice memo, at most 4/yr |
| Quarterly | Sphere note to past clients and friends, framed as news | Jen sends, we draft | operator file only |

## D. New §14: The vault (so month 2 doesn't restart)

Every reusable Jen asset indexed by district with status, so the next month is assembled, not re-invented. Living file `06-system/VAULT.md` (create on merge):

| District | Asset | Status | Where |
|---|---|---|---|
| Attract | what $850K buys · $900K two zips | shipped weeks 1–2 | v2 lane, weeks 1–2 |
| Attract | Tarzana Edition 01 (5 frames + 5 grammar covers) | built, on canvas, awaiting his verdict (artifact b76c3b1c) | v2 lane, valley-editions |
| Position | not the number that matters · insurance before the offer · Tarzana median | shipped weeks 1–2 | v2 lane |
| Convert | Bothwell three structures · Armida (pending status) · Moonseed · Willis | shipped / banked | v2 lane + listing folders |
| Connect | just breathe · lipstick remodel · everything works out · not my thing | copy ready, render pending | this lane, connect-posts-01 |
| Reply layer | four saved replies · the valley file | shipped | v2 lane |
| Read loop | outlier audit · pulse · funnel math | live | this lane |

## E. §11 Coffee & Contracts parity (what we match, beat, and skip on purpose)

| C&C has | Ours | Verdict |
|---|---|---|
| Dashboard: her analytics + today's task | `jen_pulse.py` weekly numbers + Sunday drop | match, $0, and read by a person |
| Custom content calendar generator | goal-tagged month from `/alyssa-stalker-content-mix-planner` + weeks builder | beat: dated facts, her streets |
| Template vault by pillar | `VAULT.md` | match |
| Two style options per template | six Canva grammars in Valley Editions; first post of each month offered as two takes, she picks | match (§11 already adopts) |
| Caption generator with local nouns | copy engine with the realism gate | beat: verified places, not name-swaps |
| Lead magnets / email drips | the valley file (three one-pagers) + saved replies | match the function, skip the funnel software |
| Link-in-bio page | her linktr.ee | skip for now |
| Claude connector "run my weekly content dashboard" | the Monday pulse + 1st-of-month read | match |
| Community, weekly live audits | Farrice + this system | skip |
| Trending audio, manual posting | optional at post time | skip as a requirement |
| "5 minutes" effort frame | "thumbs-up + reply DMs" | match the frame exactly (memory `jen-hands-off-photo-look`) |

## F. §10 Scoreboard: keep hers, add ours

Hers stays: DMs with a street, a number, or a timeline, per month. Ours (operator only, `FUNNEL-MATH.md`): DMs per 1,000 views, consults, signed, closed. The first tells her it's working. The second tells us which stage to fix.

## G. Two corrections to the September carousel's failure diagnosis

The reset memo names the Canva carousel's failure as "no job." The outlier audit adds the second cause: the property was the hook. Every bottom-quartile post on her grid leads with the house; every top post leads with her or a feeling. The Convert district should keep that rule from the weeks 1–2 Bothwell reel (the thesis leads, the address follows), and the Moonseed caption body, which is comfort-shaped and was buried under a listing hook, is a ready Connect post if the order is flipped.
