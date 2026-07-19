# Source Ledger — creative-campaign-strategy (Ron Lynch)

Ground truth = `extractions/ron-lynch/transcript.txt` (single file, 67,446 bytes,
read in full for this repair pass, 2026-07-17). No other `extractions/` file
matches this expert (`ls extractions/ | grep -i lynch` returns one hit: the
directory `ron-lynch/` containing only `transcript.txt`). Claim-by-claim below;
VERIFIED = quote/fact appears verbatim or near-verbatim in the transcript,
LIKELY = consistent with the transcript's account but paraphrased/inferred,
UNCONFIRMED = not present in the transcript and not independently checked.

## Anti-Patterns section (genius.md, new)

| Item | Label | Anchor |
|---|---|---|
| Feature-first vacation pitch ("Nine out of 10 agency campaigns...pool...bar") | VERIFIED | transcript.txt, vacation-destination passage (Bahamas/Jamaica/Hawaii exchange) |
| "I can't" filter / receptive-filter quote | VERIFIED | transcript.txt, "As long as you hold that thought..." passage |
| George Foreman Grill families-vs-actual-buyer misfire | VERIFIED | transcript.txt, George Foreman Grill passage ("antithesis of families") |
| Strategy-vs-copywriting distinction quote | VERIFIED | transcript.txt, "there's definitely many copyriters that they think strategy means..." passage |
| Copywriters quitting at the visual column, fear of production | VERIFIED | transcript.txt, "that's the thing that terrifies copywriters..." passage |
| Coca-Cola actual-behavior vs. sold-identity | VERIFIED | transcript.txt, "what do Coca-Cola drinkers really do?" passage |
| Cost-of-acquisition optimization vs. cost-to-zero | VERIFIED | transcript.txt, "Most people enter a business and they go, I need to figure out how much it costs to acquire a customer..." passage |

## Recognition Test + How to Use This Skill sections (genius.md, new)

Not sourced-claim sections — calibration/verification framing written fresh
against the patterns already VERIFIED elsewhere in this ledger (identity-first
naming, the 14-20 page brief standard, the GoPro "bravery" reframe). No new
factual claims introduced.

## Pre-existing genius.md claims audited during this pass

| Claim | Label | Anchor |
|---|---|---|
| GoPro $600K → $6M (yr 1) → $16M (yr 2) | VERIFIED | transcript.txt, opening GoPro passage + contest-mechanism passage |
| GoPro sold "bravery," product named "Hero" | VERIFIED | transcript.txt, "we didn't sell cameras...we sold bravery" |
| 100,000 user-generated commercials | VERIFIED | transcript.txt, "suddenly we had 100,000 commercials running" |
| Daily contest giving away one $300 camera at cost of goods | VERIFIED | transcript.txt, "give away one $300 camera when you were giving it away at the cost of goods" |
| Cooking appliance billions in revenue; food-first sell | VERIFIED | transcript.txt, "I've sold literally billions of dollars in cooking appliances...I always start with great food" |
| One 4-day shoot → $80M/yr for 5 years, $20-30K/month royalty | VERIFIED | transcript.txt, "they sold $80 million a year for five years...getting a check for 20, 30 grand" |
| Age 34 < $100K/yr → age 36 > $1M/yr | VERIFIED | transcript.txt, "When I was 34, I made less than $100,000 a year. When I was 36, I made over a million dollars a year." |
| Radio station $10,000 mystery-clue contest (60 days) | VERIFIED | transcript.txt, "$10,000 in your city and every day at 2:00...driving people to your station...for 60 days" |
| 14-20 page creative brief standard | LIKELY | transcript.txt confirms Ron teaches "how to develop a creative and strategic brief" as a 13-week program deliverable; the specific "14-20 page" / "15-page template" figures are not stated verbatim in the transcript — retained from the pre-existing skill as LIKELY (consistent with his documented brief-as-business-plan philosophy), not independently verified against a second source |
| 3-Question Pre-Qualification (USP/pricing/demonstration) | LIKELY | Consistent with transcript's demonstrability/pricing-mechanics emphasis (Foreman Grill, GoPro mounts) but the specific 3-question framing is not a verbatim transcript passage |
| $30-40K test weekend | UNCONFIRMED | Not present anywhere in transcript.txt; no corroborating source in `extractions/` |
| Sunglasses-on-ponytail audition story, SAG card | VERIFIED | transcript.txt, "I took my sunglasses and I put them on backwards on top of my ponytail..." passage |
| Billy Mays / Total Trolley exemplar and "very good creative" quote | UNCONFIRMED | Not present anywhere in transcript.txt. Flagged inline in genius.md Exemplar 4 during this repair pass — this is the clearest instance of provenance that could not be corroborated and should be treated as unverified, not fabricated-and-hidden |
| "Bonfire Enterprises" / "Guthy-Renker Ventures" incubation-arm naming | UNCONFIRMED | Not present anywhere in transcript.txt. The underlying *behavior* (scout products, write brief, produce creative, negotiate royalty) is VERIFIED via the "copywriting is a hijack" passage; the company names are not |
| "Big Baby Agency" branding, BigBabyAgency.com, "Marketing Mercenary" 9-week program | UNCONFIRMED | Not present anywhere in transcript.txt. Transcript confirms a "mercenary program" (unnamed) and a separate "13 weeks" coaching cohort — the 9-week figure and all proper nouns in this cluster are unconfirmed |
| *Buy Now: Creative Marketing that Gets Your Product Sold* (book title) | UNCONFIRMED | Not present anywhere in transcript.txt |
| Cost + royalty deal model ("I'll do it for this and a little royalty") | VERIFIED | transcript.txt, "I'll do it for this and a little royalty...they make $100 million and I make two" |
| Inverted pyramid org (customer top, CEO bottom, two decision types) | VERIFIED | transcript.txt, "most companies start as a pyramid with a pharaoh on top...successful company inverts" passage |
| Screenwriter background, Kathleen Kennedy / Steven Spielberg encouragement | VERIFIED | transcript.txt, "I wrote 10 or 20 movies before I wrote my first ad...Kathleen Kennedy and Steven Spielberg" |

## Method

1. `ls extractions/ | grep -i lynch` → confirmed single source: `extractions/ron-lynch/transcript.txt`.
2. `wc -c extractions/ron-lynch/transcript.txt` → 67,446 bytes (file is real, non-empty, fully readable — not a broken/0-byte extraction).
3. Read the transcript in full (single Read call, no truncation) and cross-checked every genius.md claim against it.
4. Claims with no matching passage were labeled UNCONFIRMED, not silently dropped — flagged inline in genius.md at the exact section where they occur so a reader hits the caveat in context, not just in this ledger.

## Amplification pass 2026-07-18 (three new workflows + prompts)

Ground truth unchanged: `extractions/ron-lynch/transcript.txt`, re-read in full
for this pass. New workflow/prompt quotes, claim-by-claim:

| Item (workflow) | Label | Anchor |
|---|---|---|
| "selling an identity... We sold bravery" (copy-pass F1) | VERIFIED | transcript.txt, GoPro identity passage (appears twice: cold open + mid-interview) |
| "write in the customer's voice... inside the head of the person who will be receiving this" (copy-pass F2) | VERIFIED | transcript.txt, customer-voice passage after screenwriting exchange |
| Chess-player-to-checkers-player register, "edge of authority... compassion and empathy" (copy-pass F3) | VERIFIED | transcript.txt, doctor-voice/authority passage |
| "complicated idea... into metaphor form... That's when you become excellent" (copy-pass F4) | VERIFIED | transcript.txt, metaphor/Jordan Peterson/Jesus passage |
| "I write the right side of the script. I write the visuals" + double-your-salary line (copy-pass F5) | VERIFIED | transcript.txt, closing "I'm not a copywriter, I'm a writer" passage |
| "you want to make this. Oh, you need the appliance to do it" (copy-pass F5) | VERIFIED | transcript.txt, food-first appliance passage |
| "I know the beginning and the end, but I don't know the middle" + "taking dictation / watching the movie" (receive-the-draft S2-S3) | VERIFIED | transcript.txt, Kennedy & Spielberg passage (appears twice: cold open + full version) |
| "All great art comes from beyond" + turned-off filter of acceptance (receive-the-draft S1) | VERIFIED | transcript.txt, receptive-filter exchange |
| "If I hear an I can't, that's an alarm bell" + "with risk comes reward" (receive-the-draft S1) | VERIFIED | transcript.txt, rewriting-stories passage |
| Doors-in-the-pool: "The first one is always agonizing... water starts flooding in... becomes part of your identity" (receive-the-draft S4) | VERIFIED | transcript.txt, dry-pool metaphor passage |
| "internal defiance. Otherwise, you're complacent" (receive-the-draft S4) | VERIFIED | transcript.txt, same passage, following lines |
| "flow state is magic... It's that or it's rest" (receive-the-draft S3) | VERIFIED | transcript.txt, flow-state passage (cold open + full version) |
| Strategist's Bible: crowd parse, "three benefits and one audience... 10 times with 10 different audiences... all roads lead to Rome... three different offers to match their personal economics" (umbrella-map S1-S5) | VERIFIED | transcript.txt, "Now strategist is..." passage |
| Beachhead sequencing: "the customer we have to win first... backfill to here's the language" (umbrella-map S3, S5) | VERIFIED | transcript.txt, umbrella/strategist-department passage |
| "a financial game as much as it is a creative game" (umbrella-map S3) | VERIFIED | transcript.txt, same passage |
| "marketing business of their business... marketing soap business" (umbrella-map S6) | VERIFIED | transcript.txt, soap-business passage |
| Winners-data-mining "That's copywriting" anti-pattern (umbrella-map header) | VERIFIED | transcript.txt, strategy-vs-copywriting exchange (already anchored in Anti-Patterns section above) |
| George Foreman wrong-hypothesis example (umbrella-map prompt, Creative Latitude) | VERIFIED | transcript.txt, George Foreman Grill passage (already anchored above) |

## Expansion pass 2026-07-19 (Sources 2-3)

New ground truth: `extractions/ron-lynch/transcript-2-dOM.txt` (Marketing Misfits
w/ Norm Farrar & Kevin King, 12,885 words, youtube dOM-_4JHRRE) and
`transcript-3-V8BD.txt` (Joe Polish / Genius Network, 9,175 words, youtube
V8BDV3KLt5U) — both read in full this pass. Visual context: transcript-2 frames
fetched (100, talking-head podcast, no on-screen artifacts — transcript carries
the material); transcript-3 video download failed (captions complete).

| Item | Label | Anchor |
|---|---|---|
| Four $100M+ shows then four zeros; "quit thinking I was the magic... picking really poor products based upon my ego" (GP-13) | VERIFIED | transcript-2, failure passage; retold transcript-3 ("I was picking me... Pop.") |
| Little Red Riding Hood testimonial relay (GP-14) | VERIFIED | transcript-2, testimonial passage |
| $20-bill/$100-bill increments, $19.95/39.95/59.95/99.95 ladder, "left 10 bucks on the table", 14 test versions (GP-15) | VERIFIED | transcript-2, pricing passage |
| Innovation/Audience/Margin/Story criteria + highest-retail anchor + Walmart 50% (GP-16) | VERIFIED | transcript-3, cold open + $25K-day passage |
| $1,000 coffee, 80% knockout, $5K/$25K consult ladder, 20-40 page document (GP-17) | VERIFIED | transcript-3, coffee passage |
| Character-traits test, 2,600 employees, keeper/walk tells, integrity both halves (GP-18) | VERIFIED | transcript-3, test passage |
| Mac-and-cheese repositioning kiosk; Circle "finally your favorite beverage" (GP-19) | VERIFIED | transcript-3, grocery + Circle passages |
| 28:30 infomercial anatomy (tease/acts/commercial at 7-8 + 21/radical demo ~25) | VERIFIED | transcript-2, structure passage |
| Billy Mays over-the-top demonstration doctrine | VERIFIED | transcript-2 ("make it over the top and outlandish") |
| Sunk-time close; "the industry actually took over everything"; TikTok = short-form infomercial (HK-13) | VERIFIED | transcript-2, cold open + evolution passage |
| Trust default + snake/Eve apple-taste (HK-14) | VERIFIED | transcript-2, trust passage |
| "It's not even the food, it's the reaction" (HK-15) | VERIFIED | transcript-2 |
| Attention's two doors: super-familiar / never-seen (HK-16) | VERIFIED | transcript-2, attention passage |
| "Choice causes confusion and confusion creates no's" + multi-cooker flop | VERIFIED | transcript-2, failure exchange |
| $5.5B DRTV, 85-100 long-form, 350-400 short-form, 70+ brands, first show $80M/6mo | VERIFIED-IN-SOURCE | transcript-3 host bio + transcript-2 self-report; not independently confirmed outside the interviews |
| Lars and the Real Girl option story (no writing credit) | VERIFIED-IN-SOURCE | transcript-2, origin passage; external verification not performed |
| Jeff Bridges "write — the writers are always working"; Kathleen Kennedy via Dana Middleton check-stand story | VERIFIED-IN-SOURCE | transcript-2 + transcript-3 (told in both) |
