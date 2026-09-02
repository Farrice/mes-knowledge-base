# Jen Engine v2 — "done for her," built to get DMs from Valley buyers and sellers

Living doc. Replaces the September plan's operating model. Copy rules, fair-housing floor, her verbatim lines, and the saved replies carry over unchanged. Operator-only; nothing here is shown to Jen as a system.

## 1. Identity (the niche is the place, not the person)

**"Your Valley agent. $800K and up, buying or selling."** (her seat's line; use it on the profile in her lowercase register.)

Why this holds, six seats agreeing: the place does the belonging, the price does the sorting. A seller readying a $900K listing and a first-timer at $800K read the same post as theirs. Nothing on the grid is organized by buyer type or by transaction. "Buy or sell" is a detail inside a post, never a pillar.

Guardrail (her own pushback): an $800K floor with no ceiling still reads first-timer-ish. Captions and asks stay neutral: "talk numbers," "send me the street," never "your first home."

## 2. The deal (what she does, what we do)

**She does:** a thumbs-up on the week's posts (30 seconds), same-evening replies from the saved replies, and posting the files (until we have account access). Optional, when she feels like it: a ten-minute drive filming twenty clips, or a fifteen-second talking clip at a listing door.

**We do:** research, writing, photos, motion, captions, the weekly folder in Drive, reading what comes back, next month's plan.

**Never:** a recurring ask, a template for her to fill, a word she hasn't approved, a topic that fails the realism gate.

## 3. The realism gate (the condo lesson)

Every topic passes three questions before writing starts. Any "no" kills it.
1. Would she say this to a client, in these words?
2. Can a stranger in the Valley act on it *at the stage they're at*? (California reality: HOA documents, disclosures, inspections arrive in escrow, after acceptance. Pre-offer content can only ask for what a stranger has: an address, a street, a number, a question.)
3. Is every fact dated and sourced, or hers?

Verdicts so far: condo (building must qualify) dead. Rail dead (a "blocks people skip" line she won't say, plus footage she won't reliably shoot). Insurance before the offer: passes. Rates and "just breathe": passes, her words.

## 4. Districts (one identity, four jobs)

| Job | Share of posts | What it is | Reader's real action |
|---|---|---|---|
| **Attract** (locals share it) | ~35% | Valley place content with the price signal in the hook. "what $850K buys in tarzana this month." "send this to a future valley homeowner." Never a pure local guide with no price or place qualifier: reach with nobody in it. | Share it, save it, or DM a street or a number. |
| **Position** (she knows this market) | ~30% | One market fact translated both ways, buyer and seller, over her photo. A market read in her calm register. "What you see vs. what you don't see" over a listing photo. | DM to talk numbers or ask what a nearby home is worth. |
| **Connect** (they get to know her) | ~20% (one post in five) | Her life and her feelings about the work, from the archive: "just breathe," "lipstick remodel," "everything works out," the Valley view she's a sucker for. A feeling first, real estate second, the offer last as permission. Never a tip in a comfort costume. | Send it to someone ("this is us"), or reply with a feeling: "same," "ugh, the numbers," "we're stuck." |
| **Convert** (a real next step) | ~15% while listings are active; its slot goes to Position when there is none | Her active listings and just-solds. Address, one unexpected feature, a showing to book. Her walk-to-the-door clip when she films one. | DM for a private showing. |

Insurance and rates posts sit in Position. Client stories only with permission and only real.

Why Connect exists (added 2026-09-02, from `04-deliverables/jen-outlier-audit.md`): her account's outliers are all life-first (Coachella with a 2-year-old 17K views, "if he won't hold the standard" 5,285, the pizza-and-Farrice story 3,131); property-first hooks sit in the bottom quartile (1,618 to 1,907 views, 46 to 97 likes). The one real-estate post that broke out in window was the budget-vs-wishlist humor reel (38 comments, 2.9× median), which is Connect-shaped. Connect copy comes from the five voice memos and thirty-plus captions already transcribed; no new ask on Jen. First four posts: `04-deliverables/connect-posts-01/COPY.md`. Ratios are a first guess; the monthly read (§8) decides.

## 5. Formats (ranked by what she'll post and what works)

1. **Photo-motion reel** over her listing photography. Slow pan, one serif line, nothing else on the frame. Zero filming. (All six seats' top pick.)
2. **Single-frame or two-beat photo card.** Full-bleed photo, white serif, one handwritten line, her lockup. Carousels only when there are new photos per slide; never the same photo six times.
3. **Drive B-roll reel** with a serif hook, when she's filmed clips. Optional fuel, never the bottleneck.
4. **Her talking, occasional.** Fifteen seconds at a listing door, a walkable line. Once per listing, never weekly.

Format test (added 2026-09-02): carousels are untested on her grid (zero in the last 3.5 months). Alyssa Stalker reports carousels beat reels "by far" for her and that single-image posts are back; Jen's own numbers cannot confirm or deny yet. Run one Connect post as a carousel and one as a single card in the same month and read the saves. Format is decided by the pulse, not by taste.

## 6. The look: Valley Native · Photo, plus the legibility rule

Full-bleed photograph, dark wash for contrast, white serif headline (Playfair Display), one handwritten accent (Caveat), Jost for body, her name lockup at the foot. **Legibility rule:** one big line per frame, high contrast, a clean shot behind the text. The Coffee & Contracts winners worked despite bad legibility; ours works because of good legibility. Generator: `04-deliverables/2026-09-01-september-carousels/gen_photo.py` (extend it, never fork it). The line-drawing system stays on the shelf.

## 7. Photos and footage

Sources, in order: her listing photography (Drive folder 01), her portraits and life (03), the cleared Valley pool (`img/`), her monthly drive clips (02) when they exist. Nothing stock-looking. Nothing warm-orange.

Drive: **Jen · Content Drop** https://drive.google.com/drive/folders/1yMVTQdZ0TkfieKPckwidJJ3Ci9m0s2iZ (01 listings · 02 phone clips · 03 portraits · 04 ready to post, by week · READ ME).

## 8. Weekly output and cadence

Three posts a week: one attract, one position, and one connect or convert (convert when a listing is live, connect otherwise; over a month the four districts land near §4's shares). Delivered Sunday in `04 · ready to post / week-of-YYYY-MM-DD` as files plus a captions text file and a one-line day plan. Post times: mornings 7–9 or evenings 6–8 (industry guidance, LIKELY; we'll read her own numbers after month one).

The monthly rhythm (added 2026-09-02; this is what Coffee & Contracts sells as "the dashboard"):

| When | What | Who | Tool |
|---|---|---|---|
| Sunday | Week's drop into Drive 04 (3 posts, captions, day plan, saved replies) | us | `04-deliverables/2026-09-06-engine-v2-weeks-1-2/build_weeks.py` (extend its WEEKS list) |
| Sunday | Thumbs-up on the preview | Jen, 30 seconds | iMessage |
| Tue / Thu / Sat | Posts go out; same-evening replies from saved replies | Jen | Meta Business Suite later |
| Every Monday | Pulse: views, likes, comments per post appended to `06-system/pulse/` | script | `python3 execution/jen_pulse.py` |
| 1st of month | Outlier audit on the month; name the attribute; set next month's Connect and Attract | us | `/alyssa-stalker-outlier-audit` |
| 1st of month | Four numbers from Farrice (qualified DMs, consults, signed, closed) into `FUNNEL-MATH.md`; replace the placeholder rates with hers | Farrice | one text |
| 1st of month | Facts re-check on anything still live (comps, rates, FAIR Plan) | us | `FACTS.md` re-check column |
| 1st of month | One line to Jen: who wrote in, what's next. Never the funnel | us | iMessage |
| Quarterly | Twenty-minute car chat, framed as coffee, to refill the archive | Jen | voice memo, at most 4 a year |
| Quarterly | Sphere note to past clients and friends, framed as news | Jen sends, we draft | operator file only |

## 9. The reply layer (the part Coffee & Contracts doesn't have)

Every post ends with the door open: a street, a number, a question, or "hi." Saved replies cover the four arrivals: an address, a "what's mine worth," a "we're looking this fall," a "hi." The valley file (three one-pagers) rebuilt in the photo look is what she sends to anyone who writes. Pinned post: who she helps and the file.

## 10. Scoreboard she'll believe

DMs with a street, a number, or a timeline, per month. Shares from local accounts as the leading indicator. Nothing else reported to her.

Our column (operator only, `FUNNEL-MATH.md`): DMs per 1,000 views, consults, signed, closed. Hers tells her it's working; ours tells us which stage to fix. First-guess compound: about one closing per 16 qualified DMs, every rate UNCONFIRMED until hers replaces it.

## 11. Better than Coffee & Contracts, specifically

Theirs: placeholders, self-serve, generic captions with local nouns swapped in, no reply layer, no realism gate. Ours: finished posts written for her streets with dated facts, her veto inside the loop, her photos, saved replies and the file behind every post, and a monthly read of what came back. Adopt from them: the "5 minutes" effort frame, two style options on the first few posts so she picks, photo-first surface, local shareables with a price signal added.

Feature-by-feature parity (match / beat / skip): `2026-09-02-engine-v2-amendments-from-outlier-audit.md` §E. Their dashboard is our Monday pulse; their calendar generator is `/alyssa-stalker-content-mix-planner` plus the weeks builder; their template vault is `VAULT.md` (§14). Skipped on purpose: link-in-bio software, keyword DM automation, trending audio as a requirement, the community.

## 12. What the research added (Gemini Deep Research, 47 sources, 2026-09-02; record in `2026-09-02-deep-research-what-works-valley-agents.md`)

Confirms the seats; adds these. Numbers are Gemini-sourced, mostly labelled "inferred" in the report itself; VERIFY before any number reaches Jen or a post.

- **Named Valley agents already running our formats.** Brian Cooper (Woodland Hills, Winnetka): "What $900K buys in Woodland Hills, 2026" series plus personal storytelling. Dan Hendrix (Van Nuys, Burbank, Tarzana): the downsizer reframing hook, "$999,000 and proof that perfection doesn't need to be massive," captions that voice the viewer's own sentence ("I want to downsize, I don't want upkeep"). Rosalyne Cohen (Sherman Oaks, Woodland Hills): ADU-potential content for $1M buyers who need rental income to make the number work. Dylan Good (Chernov Team): SEO keywords in captions, raw over cinematic. Study their grids before writing month one; steal structure, never words.
- **Place-led beats buyer-type, per the report:** hyperlocal pages rank higher and produce more leads than generic ones; generic "LA market" posts get punished; a specific city plus price band reads as authority, not a cage. The fear is answered in the data, not just by the seats.
- **"What $X buys" is the top lead format for this band:** it filters the unqualified before they cost engagement and resets expectations before the DM. Needs real comps weekly (public listing data; VERIFY).
- **"Send this to a future…" is reach with mixed intent** unless grounded: pair it with three practical lines for a Valley buyer this year, or don't run it.
- **Neighborhood POV reels (15–30s rapid cuts, local spots, text on screen) earn saves**, which is retargeting: the saver sees her next post. This is the drive-clip format, and why the drive matters.
- **Ratio top agents use (report's source, one YouTube practitioner):** 40% awareness, 30% trust, 20% local authority, 10% hard conversion. Our 40/40/20 is close; keep convert at 20 only while she has active listings.
- **Legibility rules for serif-over-photo:** negative space behind the type (sky, wall, out-of-focus foliage), a 10–15% dark overlay or gradient, white serif headline paired with a geometric sans for the details (Playfair with Jost or Montserrat). One idea per frame. This is now the design rule in section 6; her Canva carousel broke it by stacking bullets over a busy room.
- **Coffee & Contracts, honestly:** $74/mo, 5,000+ members, no auto-posting, generic templates get "near-zero reach" unposted-as-is, members who win customize heavily, post 15+ times a month, and see leads at roughly three months. Members use templates for stories and carousels and original reels as the discovery engine. That's our design already, minus the subscription.
- **Keyword-comment automation (ManyChat) is how the top accounts capture.** Jen finds keyword CTAs cheesy; we keep the street-or-number ask and the saved replies instead. Revisit only if reply volume outgrows her evenings.

## 13. Open items

- Real comps for "what $X buys" posts: public listing data each week (label VERIFY until pulled).
- Her listing photography into Drive folder 01 (Farrice).
- Account access for scheduling and numbers (later). Until then the Monday pulse reads public numbers only (views, likes, comments); saves, reach, and follows need her Insights.
- Deep-research findings to fold in: `2026-09-02-deep-research-what-works-valley-agents.md`.
- Farrice's verdict on Tarzana · Edition 01 (canvas b76c3b1c), then plates A–E behind the cost gate.
- Render the four Connect posts (`04-deliverables/connect-posts-01/COPY.md`) into weeks 3–6 as the Connect slot; Jen's thumbs-up on the Jen-seat lines and the "$80 million" line.

## 14. The vault

Every reusable asset, indexed by district with a status, lives in `VAULT.md` (living). Month two is assembled from the vault, not re-invented. Add a row when a post ships, a set renders, or a reply gets saved.

## 15. The surface, current

The look in §6 is the rule; the current generator family is `06-system/valley-editions/` (`DESIGN.md`, `CANVA-GRAMMAR.md`, `editions.py`, six Canva grammars, her photo bank). Weekly cards and reels still build through `build_weeks.py`, which imports the September `gen_photo.py`. One family, two entry points; never a third generator.
