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
