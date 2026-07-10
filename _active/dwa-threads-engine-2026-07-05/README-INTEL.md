# DWA Threads Engine — Intel Run, 2026-07-05

Executive brief and index for the second intel wave (files 10-17). Built on real scraped social data (Reddit, TikTok, YouTube, IG) captured 2026-07-05 via Apify — total spend ~$0.74. QA verdict: **SHIP_WITH_FIXES** (full detail: `04-deliverables/17-intel-qa.md`).

---

## Headline Findings

### VoC / ICP verdict (10-voice-of-customer.md)

CONFIRMS the core psychology (scam-reflex, course-graveyard shame, "why buy through you," identity-repair > money) but CORRECTS three structural assumptions:

1. The population is bimodal, not one skeptic persona — a credulous cohort begs strangers for links with zero due diligence in the same threads, and the anti-guru frame will never convert them (nor should it try to, per Path A).
2. DWA's most visible real-world resale base is moms selling to moms, not male "Mark, 33" — the ICP's gender-flex hedge was correct and should be leaned into, not treated as a footnote.
3. A more business-literate secondary segment exists (comparing DWA vs DBA vs UBC on "positioning"/"offer clarity") that doesn't fit Mark's "doesn't know what a funnel is" framing at all.

Everything else — fears, private language, objection structure — holds up almost verbatim against real quotes.

### Competitor white-space verdict (11-competitor-inventory.md, 14-strategy-fortification.md)

Partly open, and weaker than assumed on the SAHD layer specifically. Anti-guru/behavioral-change framing is confirmed open with high confidence — every real post reviewed (60+60 TikTok videos plus 12 real IG posts from the most-developed competitor) defaults to income-flex reveals, faceless MRR kits, or DM-gate hype with zero coaching credential, zero readiness screen, and zero behavior-science mechanism.

But the identity layer is not silent-and-empty the way the thesis implied: the SAHM persona is a sustained, repeat-poster throughline for at least two named accounts (not just a hashtag), and one real, actively-posting, face-forward dad-of-4 (@officialloucameron) already occupies adjacent territory — family-provider dad content — even though he frames it as breadwinner freedom-flex rather than present-tense caregiving.

The strategic takeaway: the specific stay-at-home-dad + credentialed-behavior-change combination is genuinely unclaimed, but it's open because almost nobody is playing it, not because the space is proven-hot with zero supply — and Farrice needs to differentiate from Lou Cameron's dad-coded but hype-heavy, credential-free, DM-gated approach specifically, not just from generic SAHM competitors.

**Booleans:** `antiguru_confirmed = true` · `sahd_confirmed = false` · `behavioral_confirmed = true`

---

## File Index

| File | What it is |
|---|---|
| `02-research/10-voice-of-customer.md` | Real Reddit/TikTok VoC pull — validates + corrects the ICP |
| `02-research/11-competitor-inventory.md` | ~15 named TikTok/IG competitors, credential/mechanism audit |
| `02-research/12-trending-bestpractices.md` | Format/hook patterns from 60+60 real TikTok videos |
| `02-research/13-postpurchase-sentiment.md` | What happens after people buy DWA/DBA/UBC — real reviews/threads |
| `02-research/14-strategy-fortification.md` | Whitespace bet re-tested against real data, self-flags the Threads-native gap |
| `04-deliverables/15-product-ladder-pairings.md` | Offer ladder mapped to the corrected ICP and confirmed whitespace |
| `04-deliverables/16-standalone-product-concept.md` | "The 14-Day Ship Sprint" $47 product spec + demo-sell-build pre-sale gate |
| `04-deliverables/17-intel-qa.md` | Adversarial QA verdict — compliance leaks, validation gaps, risk ranking |
| `intel/` | Raw Apify scrapes (Reddit threads, TikTok/IG post JSON, YouTube pulls) |
| `intel/digests/` | Condensed, sourced digests of the raw scrapes used to write 10-16 |

---

## QA Verdict

**SHIP_WITH_FIXES** — see `04-deliverables/17-intel-qa.md` for the full compliance check, validation status, whitespace holdout, and ranked risks. Two compliance leaks found (product name implies an outcome; a cross-offer income figure isn't quarantined), plus a labeling gap between confirmed and hypothesized mechanisms. None require new research — all are editable in the existing docs.

---

## What To Do Next (top 3 evidence-driven moves)

1. **Fix the name before anything ships publicly.** Rename "Ship the First Sale" to an outcome-agnostic alternative (e.g., "The 14-Day Ship Sprint") or add an explicit outcome-promise check to the connotation/trademark gate — this is the single highest-severity open item.
2. **Write to the corrected ICP, not the original one.** Lean into the mom-to-mom resale reality and the bimodal skeptic/credulous split when drafting Threads copy — don't let "Mark, 33" override what the real data showed. Route through `/copy-engine` or `/ghostwrite` with `02-research/10-voice-of-customer.md` loaded.
3. **Spot-check Threads before trusting the whitespace verdict as platform-confirmed.** A lightweight manual pull of 10-20 Threads accounts in this space closes the single largest evidence gap in the whole pack before spend or scheduling commits to the anti-guru+SAHD angle.

---

## Data Gaps (known, self-disclosed)

- **Trustpilot bot-walled** — could not scrape post-purchase review sentiment from Trustpilot directly; `02-research/13-postpurchase-sentiment.md` relies on Reddit/forum threads instead.
- **YouTube transcripts didn't capture** — video content was identified but transcript text wasn't retrievable; findings from YouTube are visual/metadata-only, not quote-level.
- **Zero Threads-native data** — every competitor and trend conclusion is ported from TikTok/IG/Reddit by inference; no direct Threads scrape exists in this pack (see QA risk #2).
