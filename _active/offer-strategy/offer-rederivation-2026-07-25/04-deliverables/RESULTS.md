# Offer Re-Derivation: Results

> ⚠️ **RECON-GRADE — not decision-grade.** Retro-labeled 2026-07-26 under the depth
> contract. This report was produced by a single-pass swarm whose evidence was never
> independently attacked, and **zero of its 87 gathered source URLs survived into this
> document**. It fails `research_quality_gate.py validate --depth deep` (0 sources / 0
> domains). Its four price anchors were independently re-verified live on 2026-07-26
> (see DEPTH-FIX-PROOF.md) and those hold. Everything else here is preliminary.

**Run:** 2026-07-25. 12 agents, 0 errors, ~1.5M tokens. Six evidence sweeps, then three paths, then three adversarial attacks.
**Verdict on all three paths: KILLED.** Read that as the run working, not failing.

---

## The finding

Three attackers, each given one path and no knowledge of the others, each prescribed the same fix.

**Strategy does not hold an invoice. Assets do. Strategy is why the assets are good.**

Every priced offer the sweeps found in this category prices asset volume and lists creative strategy as an included feature line:

| Seller | Price | What's on the invoice | Where strategy sits |
|---|---|---|---|
| DTC.SUPPLY "Ignite" | $950 / 2 weeks | 15 static ads (5 concepts × 3 ratios), 1 SKU | bundled |
| CREVARI "Creative Autopsy" | $1,000 / 5 days | teardown + saturation map + 3 unclaimed angles + 1 scripted concept | **this IS the product** |
| CREVARI pilot | $4,000/mo | 15-25 finished creatives | bundled |
| Dribbble DTC retainer | $3,200/mo | 20 ad concepts + 3 copy variations each | "creative strategy included" |
| Darkroom | $5K-$15K/mo | 15-40 statics + video | listed, **not itemized** |

And the only rate figure in the whole sweep drawn from actual bookings rather than a pricing guide: **YunoJuno, Creative Strategist, $69/hour.**

That number killed the retainer path on its own. Path B priced insight at $2,500/mo for roughly 10 hours of work, which comes to $250/hour, or 3.6× the measured market rate, charged by someone with zero vertical proof. Its only supporting evidence was a *payroll* posting (HealFast, $2,000-$5,000/mo part-time). A company that puts $2-5K/mo on headcount does not automatically put $2,500/mo on an outside vendor for a fraction of that scope.

---

## What each path was, and what killed it

**Path A, "Three Ads Your Category Isn't Running."** $750, 3 days. An angle-gap map built from the Meta Ad Library: what every competitor is arguing, and the two or three arguments nobody is making.
*Killed because:* the map is the giveaway rather than the product. Angle mapping is close to table stakes in DTC, and a $49/mo tool competes on that exact axis. The attacker's fix was to flip it, make the map free, and sell the ads the map points at.

**Path B, "Unclaimed," the monthly angle supply.** $1,000 first drop, then $2,500/mo standing.
*Killed hardest.* Six fatal flaws. The recurring revenue was the entire thesis, and it's the one number with no evidence anywhere behind it. No pure-insight retainer in the evidence renews, because every retainer with a published price is volume-backed. Fletch, the closest documented case, sells a one-time sprint and has never attempted a retainer. The prescribed fix was to cut the retainer and keep the one-time drop.

**Path C, "Source Material," persona and desire intelligence.** $1,500, 5 days. Mined buyer segments from real reviews and ad comments, on the thesis that AI removed production as the constraint so the constraint moved upstream to the quality of the input layer.
*Killed because:* it planned to split-test intelligence-only against intelligence-plus-assets, when the evidence had already settled that question. The fix was to run only the assets-included arm and stop spending a small sample on the arm that already lost.

**Path C also answered Q2, and the answer is no.** The POV as literally stated has no budget attached. "Brand voice guidelines" is a $750 commodity on a live WebFX page. "Make our AI sound human" is solved by $14-20/mo SaaS. "Fix the AI content" is a $36.06/hr wage on ZipRecruiter. Indeed lists roughly 14 brand-voice jobs and **zero** framed around AI content quality.

The POV stays. It's the wedge, the content, and the reason someone follows. It just isn't the invoice.

---

## What survived

Assemble the three prescribed fixes and they produce one shape, arrived at by all three attackers independently rather than invented as a fourth option here.

**Free front:** a named-brand teardown. An angle and saturation map of one brand's live Meta creative against 8-10 competitors, sent to the named growth lead and published. It serves as the proof, the prospecting, and the content engine already chosen, all at once.

**Paid entry: $950-$1,200, delivered in about 5 days.** The gap brief *plus* 5-8 finished static ads written and built into the named gap. Not concepts. Finished, runnable assets with the copy on them.

Evidence for every element of that:
- The price matches DTC.SUPPLY's proven $950 fixed-scope shape and CREVARI's proven $1,000 paid-teardown entry.
- **$1,000 is the same-day, single-manager approval ceiling** for companies under $10M revenue (Tallyfy approval matrix). Anything from $1,001 to $5,000 requires a senior manager and 1-2 additional business days. Pricing at $950-$1,000 keeps the invoice on the buyer's own desk.
- CREVARI proves a paid teardown at exactly $1,000 is a real product someone already sells.
- The buyer is qualified for free before a single message: brands with 15-20+ ads currently live in the Meta Ad Library, several running 30+ days. That filter enforces "already spending on this problem" mechanically.

**No retainer yet.** The retainer is where every unproven insight-only offer in the evidence dies. It gets offered after two or three one-time deliveries demonstrate renewal appetite, not before.

---

## The copy question, answered by the data

The 5-8 finished static ads **are copy.** Hooks, headlines, body, the argument on the image.

So the strength Farrice named, copywriting and messaging strategy and content strategy, is not adjacent to this offer. It's the deliverable. Strategy decides which argument to make, copy makes it land, and the ad is what the invoice describes. That's the only configuration the evidence supports, and it happens to be the one that puts his best skill on the receipt.

---

## The biggest risk, named plainly

**Every path shared one weakest link, and it isn't the offer. It's the channel.**

FletchPMM is the only operator who documented the teardown-to-paid motion end to end. Two facts from that record cut against an 18-day sprint:

1. It worked through **accretion**, at 3-4 posts a week producing a steady flow of **inbound**.
2. **Cold outreach specifically failed for them.** That's their own published account, not an inference.

An 18-day cold sprint runs the variant documented to fail and skips the variant documented to work. That doesn't make it unwinnable, but it does make the kill numbers load-bearing rather than decorative.

Second-order risk, also unresolved: the tag-the-subject teardown mechanic is verified in B2B SaaS, selling to founders. Whether a DTC growth lead reacts the same way to a public critique of their live paid creative is untested in anything sourceable.

---

## The gates

| Gate | When | Test | Read |
|---|---|---|---|
| 1 | 48 hours | 12 personalized teardowns sent | Fewer than 3 replies of any kind means the message is wrong, not the price. Rewrite the opening, send 12 more, change nothing else. |
| 2 | Day 10 | 20 teardown-attached sends | Fewer than 3 substantive replies (a question, an intro, a price objection — not a thank-you) means the artifact isn't landing. |
| 3 | Day 11 | 60 qualified personalized sends | Zero paid orders kills the cold DTC motion. Stop sending cold that day. Work only the warm list and anyone who replied but didn't buy. |
| 4 | Day 14 | $0 collected | Hard stop on the channel, not the offer. |

---

## Claim ledger

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Fixed-scope DTC creative packages sell at $950-$1,000 | **VERIFIED** | DTC.SUPPLY live page; CREVARI live page |
| 2 | A paid teardown at $1,000 is an existing product | **VERIFIED** | CREVARI "Creative Autopsy," live page |
| 3 | $1,000 is the same-day single-manager approval ceiling under $10M revenue | **VERIFIED** | Tallyfy approval-limits matrix |
| 4 | Creative strategy is bundled, never itemized, in published rate cards | **VERIFIED** | Darkroom published pricing; Dribbble retainer; CREVARI pilot |
| 5 | Measured creative-strategist rate is $69/hour | **VERIFIED** | YunoJuno, stated as real booking data |
| 6 | "AI hollowed out our brand voice" has no budget line | **VERIFIED as no** | WebFX $750 brand-voice page; $14-20/mo humanizer SaaS; ZipRecruiter $36.06/hr; ~14 Indeed brand-voice jobs, zero AI-quality-framed |
| 7 | A pure-insight monthly retainer renews in this category | **UNCONFIRMED — no supporting instance found** | every priced retainer in the sweep is volume-backed |
| 8 | The teardown-to-paid motion transfers from B2B SaaS to DTC | **UNCONFIRMED** | Fletch documented in SaaS only; no DTC instance sourced |
| 9 | Cold outreach works for this motion | **EVIDENCE AGAINST** | Fletch's cold outreach failed; their inbound accretion worked |
| 10 | Brands transact at four figures without procurement | **LIKELY** | Upwork fixed-price postings at $1,500 and $2,000, 2026 |

---

## The named loser

**Path B, the $2,500/mo standing retainer.** Not merely the weakest of three. Actively disproven. Its core number had one payroll data point behind it and contradicts the only real booking data in the sweep. Do not resurrect it in any renamed form until a one-time version has sold two or three times and a buyer has asked for the next one unprompted.
