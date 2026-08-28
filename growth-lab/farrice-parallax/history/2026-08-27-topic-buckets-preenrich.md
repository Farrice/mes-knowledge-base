# Topic Buckets · farrice-parallax

**Data tier: FRESH.** Pack: `.agent/outlier-radar/packs/farrice-parallax/latest.json` · 2026-08-27T19:38Z · Produced 2026-08-27 · Workflow: gb-topic-scan. Companion data core: `top-50.md` (ranked table, ✓/✗ verdicts, receipts). Outlier = N× that channel's own normal views-per-day, defined inline so no reader has to look it up.

## Working set

50 ranked rows screened with visible verdicts: 25 carry ✓, 25 stay struck in rank position with reasons (see `top-50.md`). The pack caps at 50, so no backfill pool exists beyond it; the working set is the qualified 25. Exclusions itemized: wrong avatar/aspirant 7 · off-niche 5 · too-broad/craft-source 5 · celebrity-lifestyle 2 · stale tutorials 2 · tangential news 1 · vendor promo 1 · wrong vertical 1 · Ring-5 motivational 1. Cost of this triage: $0, two radar runs, ~9 minutes of fetch time.

## Velocity + trend

The pack holds two snapshots taken 64 minutes apart, so `velocity_vpd_7d` is unreadable this run (values 0.0 or noise). Trend direction below is therefore computed from publish-date recency of each bucket's rows, labeled as such, and marked for upgrade at the next natural refresh: `python3 execution/outlier_radar.py refresh --niche farrice-parallax` (run it a day or more out; the velocity column lights up from real deltas).

## Topic buckets (6, clustered by what the avatar cares about)

| Bucket | Rows | Median outlier | Max | Trend (recency basis) | Top examples | Why it works (mechanism) |
|---|---|---|---|---|---|---|
| **A · Mechanism Waves** | 3 | 12.0× | 21.8× | Rising: all rows Jul–Aug 2026 | [Claude × Meta ads](https://www.youtube.com/watch?v=ReYEYoLsppk) 21.8× · [Claude × Shopify](https://www.youtube.com/watch?v=Ih5RapM8XKw) 12.0× · [AI ad cloning](https://www.youtube.com/watch?v=80qVcoGUkN4) 3.8× | **New-tool hope** (LIKELY, inferred from hooks: "changes are absolutely mind-blowing"): each wave promises the mechanism that finally fixes acquisition. Feeds the buyer's mechanism-buying belief from the dossier |
| **B · Platform Shift** | 3 | 13.7× | 64.2× | Steady: Mar–Aug 2026 spread | [Amazon control-loss](https://www.youtube.com/watch?v=CpIZPIbU0cU) 64.2× · [Forget Meta, 7 platforms](https://www.youtube.com/watch?v=ZhSL5A_xEJI) 13.7× · [Instagram updates](https://www.youtube.com/watch?v=dU_U1Pmmu5c) 5.5× | **Chaos vigilance** (VERIFIED in transcript CpIZPIbU0cU: "the most powerful company in retail is genuinely terrified"): fear of being blindsided by a platform you depend on |
| **C · Founder Proof Stories** | 7 | 5.7× | 15.9× | Steady: Jul 2025–Aug 2026 | [Quad Lock exit](https://www.youtube.com/watch?v=CERZXt6lpxk) 15.9× · [Viral Cookie](https://www.youtube.com/watch?v=nowcsh1wDzE) 9.7× · [$1B garage brand](https://www.youtube.com/watch?v=IYmChAiW9PY) 7.7× | **Possibility witness** (VERIFIED in CERZ transcript: "no investors, no playbook, just an idea"): the viewer borrows belief from a body that did it. Note the depth quote inside: "scale was going to fix their unit economics… I don't think that ever happened once" |
| **D · Operator Discipline** | 7 | 6.4× | 14.2× | Rising: 6 of 7 rows Aug 2026 | [Scale CPG](https://www.youtube.com/watch?v=6psqtXu4u88) 14.2× · [Leadership/org design](https://www.youtube.com/watch?v=pEH86Bji_IY) 13.3× · [Haus incrementality](https://www.youtube.com/watch?v=Jl5jCVogRcY) 3.6× | **Competence armor** (LIKELY, grounded in the brand-lead's dossier fear of being blamed): operators consume discipline content to stay defensible in the room |
| **E · In-Lane Supplement Ops** | 2 | 4.0× | 4.1× | Thin: both Jun–Aug 2026 | [Grüns marketing pod](https://www.youtube.com/watch?v=fiWsNWyPFp4) 4.1× · [Taste Salud build](https://www.youtube.com/watch?v=zeJF6EeicwA) 3.9× | **Insider mirror** (LIKELY): the operating founder finally sees his own category on screen. Thinnest bucket in the pool, and that thinness is the point (below) |
| **F · Conversion Tactics** | 3 | 6.8× | 19.9× | Mixed: 2025 + 2026 rows | [Product-page blueprint](https://www.youtube.com/watch?v=8eHZqKtnymY) 19.9× · [Ecom offer survey](https://www.youtube.com/watch?v=RHZ39WfEuM0) 6.8× · [Charge 30× more](https://www.youtube.com/watch?v=WwijQ1TYbw8) 3.9× | **Fix-it-now utility** (LIKELY from hook shapes): a named template promises same-day improvement |

**Trap callouts, printed beside the rows they disarm:**
- Bucket B's 64.2× ceiling: two of three rows are @mywifequitherjob. That is **a person winning, not a topic winning**; treat B's median (13.7×) as inflated by one channel's news-jack franchise.
- Bucket C: five of seven rows are @foundr. Same person-effect; the *story shape* is the transferable asset, not the topic.
- Bucket E's thinness is not weakness evidence: the in-lane audience is small on YouTube (watering holes run 8K–30K subs). Zero breakouts in-lane says "no incumbent has cracked it," which reads with W1/W2 as opportunity, and honestly: it also means no demand proof. Both readings stay on the table until batch 3.

## Format buckets (descriptive only; selection in gb-format-find)

From `format_hint` clustering across the 50: specific-number promise (23 rows) · concrete-declarative news/analysis (17) · tutorial-system (4) · question (1) · warning (1) · condition-free (1). The dominant skeletons: compression promise ("Learn 97% of X in N minutes"), listicle-rank, news-jack shift analysis, founder-journey interview. Carried to gb-format-find with receipts.

## Bullseye overlay + conversion column

Shape of the pool: winners cluster at Rings 3–4 (buckets A–D, broad DTC audiences); the in-lane Ring-2 bucket (E) is the thinnest. The niche's data skews broad, so the operator must consciously **protect the narrow picks** rather than chase "what's working": chasing this pool as-is would drift the channel to Ring 4 in a month.

| Bucket | Ring | Feeds (bullseye bucket → offer) | "Working =" carried from overlay | Or honestly |
|---|---|---|---|---|
| A · Mechanism Waves | 4 | The Fix Aisle → none direct | ≥1 outlier ≥3× per 2 batches + ≥30% engagers Rings 2–4 | Reach-only |
| B · Platform Shift | 4 | The Fix Aisle (skeleton donor) → none direct | same as A | Reach-only; craft value high |
| C · Founder Proof Stories | 4→2 | The Counter Files / The Convert (story spine) → Angle Map | ≥1 "this is my buyer" reply per batch | Craft donor for proof content |
| D · Operator Discipline | 2–3 | The Data Mirage (bench) → Angle Map | ≥2 agency-burned replies per batch | Trust engine material |
| E · In-Lane Supplement Ops | 2 | The Defensible Claim + The Counter Files → Sprint via Angle Map | ≥2 claims/launch DMs per batch | The money lane; thin pool, protected pick |
| F · Conversion Tactics | 3–4 | Launch Math (bench) → Sprint | ≥1 budget-decision DM per batch | Utility lane |

## The 3 picks (positioning chooses from the pool performance built)

**1 · The Defensible Claim (narrow, Ring 2).** Performance: no direct pool evidence; the lane has zero rows, which is the W1 finding, not a performance endorsement. Positioning fit: claims the only empty belief slot on the wheel. Substance advantage: 18 years + claim-science depth nobody in the pool carries (whitespace grid §2). Conversion: strongest offer linkage on the board (Sprint's named deliverable answers pain #7's exact words). The honest label: this pick is a positioning bet with conversion logic, not a data-crowned winner; batches 1–3 are its demand probe, kill/keep already written.

**2 · The Counter Files (narrow, Ring 2).** Performance: bucket C proves the proof-story mechanism holds at 5.7× median across 7 rows, and bucket E proves the in-lane mirror lands (4.0× median on tiny channels). Positioning fit: W4, the proof register incumbents cannot copy. Substance advantage: the counter years are lived, not researched. Conversion: trust engine for the Angle Map. A high-performance trap avoided here: imitating foundr's exit-story topics would be chasing bucket C's person-effect without their guests.

**3 · The Fix Aisle (broad, Ring 4).** Performance: buckets A+B are the pool's strongest current wave (A rising, all rows Jul–Aug 2026; ceiling 64.2× on B's skeleton). Positioning fit: W3, granting the mechanism then naming the unmade decision, so the reach engine installs the belief instead of merely borrowing the wave. Substance advantage: he runs a 90-agent system; he can demo any mechanism honestly before critiquing it. Conversion: none direct, flagged reach-only, fenced by the engager-ring check.

Rank ordered the pool; positioning picked from it. Passing on B's 64.2× ceiling as a *topic* (Amazon retail news) while borrowing it as a *skeleton* is the two-zone rule working as designed. The two filter questions were applied to every ✓ row: worth the Formulator-Founder's scarce attention, and building trust toward a $750/$2,500 decision.

## Refresh note

Re-scan at ~45 days (2026-10-11) or on any `gb-refresh` flag. Velocity upgrade available sooner: one refresh run ≥1 day out.

## Blind spots

- **Coverage:** YouTube measured; TikTok `none`; Instagram `none`. LinkedIn, where the actual conversions happen, is outside the radar entirely. Wrong conclusion invited: "these buckets are what works for this business." They are what works for *attention in the adjacent YouTube ecosystem*; conversion truth lives in his DM log.
- **Conversion invisibility:** the pack sees views. Before crowning any bucket a conversion winner, check that the DMs and comments actually come from operating founders or brand leads, not aspirants; bucket A/B engagement especially skews aspirant.
- **Person-effects:** flagged inline on B and C above.
- **Maturity:** no verdict on any video at 24 hours; no bucket demotion before batches 2–3 (rules printed on the bullseye tracker).

---

*State: 50 rows screened with visible verdicts, 6 buckets built with mechanisms and receipts, trio validated with four-factor reasoning. Next: `gb-format-find`, choosing the vehicles that carry all three buckets.*
