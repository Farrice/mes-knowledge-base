# PROVENANCE — donald-miller-cognitive-load repair (Wave 3, Lane 4, Batch 5)

Anchor → source file + location table for every new/changed claim in this repair. All anchors are into `extractions/donald-miller/transcript.txt` (34,611 bytes; single unbroken paragraph, no line numbers — locations given as approximate character offset and segment name). Full VERIFIED/LIKELY/UNCONFIRMED reasoning lives in `references/source-ledger.md`; this table is the flat anchor index the adversarial verifier can check quote-by-quote.

| Anchor (genius.md section) | Quote used | Char offset (approx.) | Segment |
|---|---|---|---|
| Model Calibration | "Look out the nearest window. If it's dirty, call this number." | ~9,180 | Window washer |
| Model Calibration | "That's information for you to tell your mother-in-law." | ~6,420 | Men's Shop autopsy |
| How Miller Thinks / Confusion Law | "The confused mind says no. If I don't understand what you're talking about, I'm going to say no." | ~2,880 | Opening |
| Three-Phase Campaign intro | "You check all three, your business will grow." | ~330 | Opening (first ~400 chars) |
| Phase 3 / House Diagnostic | "you incentivize me to go inside" | ~14,650 | House metaphor |
| House Diagnostic | "Would you go into this house? This house looks like a haunted house." | ~14,780 | House metaphor |
| GP5 | "they just work together like chords on a guitar and you can use them anywhere you want to write really great songs" | ~23,900 | Money-app segment |
| GP7 | "You're missing the front step sound bites. You're missing the enlightenment collateral, and you're not incentivizing people to go inside." | ~14,560 | House metaphor |
| GP8 | "Drowning in coffee shop chaos. Stop doing everything yourself." / 18 clicks / "Losing baristas faster than you can hire. It doesn't have to be this way." / 125 clicks / 600% | ~10,500–11,090 | Stay Golden coffee shop A/B |
| GP10 | "I would expect book sales would be 100% over what they projected because we simplified the message." | ~28,600 | Book launch / talent recruiting |
| Anti-Patterns AN-1 | "on a scale of 1 to 100 where style meets purpose adds 20 pounds. You want it to be zero." | ~6,090 | Men's Shop autopsy |
| Anti-Patterns AN-2 | "That's information for you to tell your mother-in-law. It is not information that I need as a customer." | ~6,420 | Men's Shop autopsy |
| Anti-Patterns AN-3 | "My mission is to buy clothes. You're telling me about your mission. I'm not interested. That doesn't help me survive. I'm glad you're on a mission, but tell that to your staff. Don't tell it to your customer." | ~6,480 | Men's Shop autopsy |
| Anti-Patterns AN-4 | "What's a modern human? I mean, basically, you're telling me you don't dress dead people. You dress people who are alive. Great to know." | ~6,800 | Men's Shop autopsy |
| Anti-Patterns AN-5 | "You're trying to make some sort of positive impact. That's very vague. I don't understand. That adds 10 pounds." / "What is everything, right? Is it walking my dog? Like, what's everything? I don't know what everything is. It's vague. Therefore, high cognitive load." | ~7,260 / ~10,600 | Men's Shop autopsy + coffee-shop A/B |
| Anti-Patterns AN-6 | "You can only choose one problem or the story can't be about three problems. It's got to be about one problem. So, commas are not your friend." | ~31,160 | Coffee-subscription campaign |
| Anti-Patterns AN-7 | "what is a relationship with money? You're introducing a complicated concept." | ~22,470 | Money-app segment |
| HK6 | "They like that so much it became their tagline. Get good with money." | ~23,150 | Money-app segment |
| HK7 | "you're not there to think. You're there to turn off your brain, maybe learn something automatically." | ~24,400 | Scroll segment |
| HK8 | "it's exactly what your business looks like because you don't have a three-phase messaging campaign" | ~14,900 | House metaphor |
| Exemplar 1 (money-app) | "a cult-like following" / "the CEO Todd" / "a 400% increase in their social media interest" | ~22,080 / ~24,140 / ~24,200 | Money-app segment |
| Exemplar 3 (Stay Golden) | "a great coffee shop called Stay Golden" | ~10,190 | Coffee-shop A/B |

All offsets computed by direct `str.find()` against the file as read in this repair session; a verifier can reproduce every location by opening `extractions/donald-miller/transcript.txt` and searching for the quoted text (the file has no line breaks, so offsets will drift slightly with any future edit to the file but the quoted strings themselves are exact substrings as of this repair).

## Not sourced from claude-export tarball

Unlike the sibling `donald-miller-storybrand` repair, this skill's fixes did not need `_archive/claude-export-2026-07-01.tar.gz` — `extractions/donald-miller/transcript.txt` alone contained every quote needed for the anti-patterns section and the entity-floor enrichments. No claude-export files were opened for this repair.
