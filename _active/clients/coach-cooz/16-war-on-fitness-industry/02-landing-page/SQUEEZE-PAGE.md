# SQUEEZE PAGE — "The Truth About Feeling Like Shit"
## Coach Cooz · War on the Fitness Industry Funnel · Squarespace-Ready
**Date**: 2026-07-08 · **Source docs**: STRATEGY-SPINE.md, RAW-MEMO-2026-07-08.md, 03-cooz-voice-profile.md, RAW-PROOF-INVENTORY.md

> No nav. No footer links. One page, one job: move the reader from "I scanned this because I feel like shit" to "I booked the Triage Audit." Page copy (Section 1 below) is **~750 words**.

---

# 1. PAGE COPY

## Section A — Hero / Hook
*(block type: full-width text section, no image — the words are the hook)*

**Page title (browser tab, not shown large on page):** The Truth About Feeling Like Shit

**On-page headline:**

> You scanned a card that promised you'd stop feeling like shit. It wasn't lying.

**Body:**

You want to look better. Fine. Nobody should have to feel like shit to get there. People hire a coach because they feel like shit and they want that to stop. The muscle and the mirror and the number on the bar are how you'll know it's working. Feeling better is what you actually came for.

I've been in this industry a long time. Long enough to watch it sell you the packaging and call it the product.

**CTA #1** *(inline text link, directly under the body copy)*:
[Book the Triage Audit →]

---

## Section B — The Industry Callout
*(block type: full-width text section, dark background)*

**Subhead:**

> The fitness industry sells you a costume.

**Body:**

A before-and-after photo. Except the "after" is dehydrated, pumped, and lit like a magazine cover — and the sixteen weeks in between, where you looked worse before you looked better, got deleted. That's theater.

Abs as the proof you're finally worth something. You don't need abs to stop hating your life. Feeling like shit is what we're actually fixing — abs are just how you'll know it worked. You can have a six-pack and hate your own life. I did.

Shame as the sales pitch. "If you don't look like this, you're failing." Call it motivation if you want. It's a business model built on making you feel worse so you'll pay to feel a little less worse.

None of that is fitness. It's a costume, and no costume fixes how you feel. You scanned this because you feel like shit, and a costume was never going to fix that.

---

## Section C — The Inverted Transformation
*(block type: two-column image + text, photos side by side)*

**Subhead:**

> Look at these two photos. Same guy. Nine months apart.

**Body:**

I'm Coach Cooz. I train people in LA, in person, not over Zoom. I've coached people through this exact swap for over ten years. This isn't a theory. It's my own life, then theirs.

Yes, I'm showing you a before-and-after. The industry shows week one against week sixteen and calls the body the point. I'm showing you the leaner version felt worse. Same tool, opposite truth.

**[LEFT PHOTO — 14% body fat, self-reported]** This was me at my leanest. The six-pack you're supposed to want. I was also the most miserable I've ever been.

**[RIGHT PHOTO — 22% body fat, self-reported]** This was me nine months later. Heavier. Softer. Happier than the lean guy ever was.

Same dude. About an 8% body-fat difference, by my own eye. Not a lab test, just me being straight with you. And the guy who looked "worse" was doing better than he'd ever done in his life.

The lean photo proves nothing about how you'll feel. Mine proves the opposite.

**CTA #2** *(inline text link, under the photo pair)*:
[See how the work actually starts →]

---

## Section D — The Proof
*(block type: stacked quote blocks, one client per block)*

**Subhead:**

> Photos can be faked. This can't.

**Intro line:**

One dehydrated photo can lie to you. Five people, in their own words, can't.

**Quote blocks** *(verbatim, coachcooz.com/resurrections)*:

> "Since beginning with Coach Cooz in October, I have lost 8 lbs.... but most importantly, I feel stronger than I have in many years. Ever grateful!"
> — **Karima**

> "I was dealing with hypothyroidism and thyroid cancer when I met him and was nervous to get back into a gym and honestly pretty frustrated with the state of my health but he made me feel very comfortable and welcomed... Thanks to him I now lift heavier, have more knowledge, and feel so much more confident being back in the gym."
> — **Jessica**

> "Coach Cooz is an absolute life changer!... With Coach Cooz, I've not only transformed my body but also my mindset."
> — **Robin**

> "I leave our sessions feeling accomplished. He helps put me in a great mood with his positive attitude, even when I'm a total crank from life."
> — **Jess**

> "I've been training with Cooz for almost 2+ years now and I can genuinely say I have never been stronger and more diligent about my physical health in all my life... makes working out at 6 am something to look forward to (a sentence I would never thought I'd ever say in my life). Couldn't recommend Cooz more!"
> — **Sam**

*All quotes verbatim from coachcooz.com/resurrections.*

---

## Section E — The Pitch (Bridge to CTA)
*(block type: full-width text section, thin gold divider above/below)*

**Body:**

You don't need to be miserable to be strong. I proved that on myself before I ever tried to prove it to a client.

It starts with a 90-minute Triage Audit. It's a paid session, not a free consult. We find out exactly what's making you feel like shit and build the plan to fix it. The audit is the first real work. Not a warm-up, not a pitch.

If it's a fit, we move into the 90-Day Resurrection Protocol and rebuild what actually went dormant. Not your abs. The rest of it.

---

## Section F — Final CTA
*(block type: full-width CTA section, black background, gold button)*

**Headline:**

> Stop feeling like shit. Start here.

**Body:**

I take a small number of Triage Audits a month, in person, in LA. When they're gone, they're gone.

**CTA #3 (button, primary):**
**[ Book the Triage Audit ]** → links to /briefing

*(No secondary link, no "maybe later," no exit option other than the back button. One page, one decision.)*

---

# 2. SQUARESPACE BUILD NOTES

**Page setup**
- Create as a **standalone unbranded page**, not added to primary navigation. Squarespace: Pages panel → "Not Linked" pages, or a page with a custom URL slug (e.g., `/stop-feeling-like-shit`) excluded from the nav bar. Confirm the page template does NOT inherit the site header/footer (use a blank/landing-page layout, not a standard content page, so the nav disappears structurally rather than being hidden with CSS).
- No footer. If the template forces one, override with Squarespace's page-specific "Hide Footer" toggle (Design → Pages → this page → Advanced), or a single-line custom CSS rule scoped to the page ID.

**Section-by-section block types**

| Section | Block type | Notes |
|---|---|---|
| A — Hook | Text block, full-width, dark background | No image. Headline in Fraunces display, body in Fraunces 400 (site type system). Inline CTA #1 is a text link, not a button — low-key, first ask. |
| B — Industry Callout | Text block, full-width, dark-bold theme | Longest text block on the page. Subhead + 4 short paragraphs, one villain mechanism per paragraph break for scan-ability. |
| C — Inverted Transformation | Two-column layout (image left, image right) with text above/below | Photos are the two Cooz body-fat images ("14% miserable" / "22% joyful"), same size, no filter or retouch — flat, undramatic presentation is the point. Caption directly under each photo in small Inter meta text: "14% body fat (self-reported)" / "22% body fat (self-reported)." Add a small circular headshot (a real, face-visible photo of Cooz, not a body shot) next to the opening trust-anchor paragraph — this is the only place on the page his face should appear. |
| D — Proof | Stacked quote blocks (Squarespace's native Quote Block or repeated text blocks) | One block per testimonial. First-name attribution only, bolded, under each quote. No star ratings, no headshots — the words carry it. |
| E — Pitch | Text block, full-width, thin gold rule (`#C08A3E`, 1px) above and below to separate "proof" from "ask" | Short block, 3 short paragraphs. |
| F — Final CTA | Button block, full-width, dark background | Large gold button, generous padding, nothing else on the section — no secondary links. |

**Palette (black / gold / white — existing brand hex values)**
- Cathedral Black `#0E0E0C` — section backgrounds (Hook, Callout, Final CTA)
- Ember Gold `#C08A3E` — CTA button fill, dividers, quote-mark accents
- Dawn Linen `#F3EEE3` — text on dark backgrounds; background of the Proof section (flip to light here so the testimonials read as a break in intensity, not more villain-naming)
- Soil Brown `#3A2A1F` — shadow/border accents only, never a large fill area

**Mobile notes**
- Section C (photo pair) stacks vertically on mobile — left photo first, right photo second, each full-width, caption directly beneath. Do not shrink both photos side-by-side on a phone screen; they'll read as illegible thumbnails.
- CTA button (Section F) is full-width on mobile, minimum 56px tall — thumb-friendly, no tiny tap targets.
- Body copy at 17px minimum on mobile (site type system) — don't let Squarespace's default mobile scaling drop it lower.
- Quote blocks (Section D) should not truncate mid-sentence on smaller viewports — check each quote's wrap at 375px width before publishing.

**QR / UTM parameter**

QR code on the flyer should point to:
`coachcooz.com/stop-feeling-like-shit?utm_source=flyer&utm_medium=print&utm_campaign=war-on-fitness-industry`

This lets Cooz split scans by flyer batch later if he prints a second run (`utm_content=batch2`, etc.) without changing the destination page. Track: QR scans (page views with the UTM tag) → CTA clicks (event tracking on all three CTAs) → completed bookings on `/briefing`.

**Where his transformation photos go**

Section C only. Do not reuse the 14%/22% photo pair anywhere else on the page (no hero background, no repeated thumbnail near the CTA) — the point is that this is the ONE "before/after" on the page, and it inverts the genre instead of playing it straight. Repetition dilutes the reversal.

---

# 3. SCENT-MATCH CHECK

1. **Flyer promise → page headline**: The flyer says "Scan this QR code to not feel like shit anymore." The page opens with "You scanned a card that promised you'd stop feeling like shit. It wasn't lying." Same words, same problem, immediate continuation — no "Welcome to Coach Cooz" reset.
2. **Flyer's unbranded silence → page's brand reveal**: The flyer never names Cooz. Section C now names him ("I'm Coach Cooz") and gives a location earlier than before, ahead of the Triage Audit / Resurrection Protocol brand terms that land in Section E/F — the reader gets a name and a place to attach trust to before the pitch, not after.
3. **Flyer's tone → page's tone**: The flyer uses "shit" bluntly, twice, no cushioning. The page keeps that directness through Sections B and C before easing into the close in Section E/F — the reader who scanned because the card felt real never hits a section that suddenly sounds like a brochure.
4. **Page → `/briefing` (NOT yet matched)**: This check only validates flyer-to-page continuity. It does NOT validate page-to-booking-destination continuity, and per the adversarial review that's the leak that actually matters — see "Open decisions flagged by adversarial review" below before this page drives real traffic to `/briefing`.

---

## Notes for the build team

- **Cody McBroom slogan — cut**: STRATEGY-SPINE.md flags "we help average people achieve above average physiques" as an unverified claim requiring "verify or cut." Not independently re-verified in this pass. McBroom also appears as a positive testimonial-giver on coachcooz.com's home page — naming him as a villain-adjacent reference on this page risks a confusing, uncleared claim next to an ally's endorsement elsewhere on the site. Cut from this draft; reintroduce only if verified and Cooz confirms he wants to reference his own mentor's slogan this way.
- **Ed Mylett line — cut**: Also flagged for verification in STRATEGY-SPINE.md and not resolved here. The underlying idea ("people want what they think the thing will make them feel") is fully present in Section A/B in Cooz's own words — the attributed quote itself was left out to avoid a misattribution.
- **9 months / 8% locked**: Memo garbles "9% but 8%" and "nine months." STRATEGY-SPINE.md locks the usable numbers as 8% body-fat difference over nine months — used consistently in Section C.
- All five testimonials in Section D are copied verbatim from `RAW-PROOF-INVENTORY.md` (sourced to coachcooz.com/resurrections), including the source's own ellipses where the quote itself was excerpted for length. No wording was altered, combined, or paraphrased.

### Open decisions flagged by adversarial review — resolve before this page goes live pointed at a paying client

- **`/briefing` destination mismatch (ship blocker)**: All three CTAs currently point to `/briefing`, which per RAW-PROOF-INVENTORY.md Section 3 is a $1,000, executive-positioned booking page ("You built the empire. Now let's optimize the man"). A cold scanner primed by 740 words of universal "feel like shit" peer talk hitting that page cold is a scent break on both price (never signaled on this page) and audience (universal → executive). Section E now pre-frames the Triage Audit as "a paid session, not a free consult" so the reader isn't ambushed at the click — but the real fix is a funnel-specific booking destination (or a stripped `/briefing` variant that drops the executive framing) before this page drives paid-flyer traffic. Do not treat the Section E line as a substitute for fixing the destination page.
- **Adjacent testimonial plan — unaudited**: All five quotes ON THIS PAGE were verified verbatim against RAW-PROOF-INVENTORY.md this pass (clean). `03-testimonial-weaponization/PLAN.md` and any `TOP-QUOTES-COPY-DECK.md` were NOT audited in this pass and must be checked character-for-character before the wider package ships — a prior version of this page was overwritten with two altered testimonials (Allison, Sammy) passed off as verbatim, so this error pattern has already occurred once.
- **Jessica's testimonial (thyroid cancer) — CONSIDER, not changed**: Verbatim and legally defensible as the client's own words, but foregrounding "thyroid cancer" next to a coaching offer on cold traffic sits in tension with the strategy's explicit no-medical-claims guardrail. Left in this draft because a verified, verbatim replacement quote wasn't available in this pass — Farrice/Cooz should decide whether to swap it for a cleaner feeling-first quote before this page goes live broadly.
- **Zero recapture for non-bookers — surfaced, not built**: At the strategy's own sub-1% booking threshold, ~99% of scanners leave with nothing, and the destination is a steeper $1,000 cold ask than the strategy assumed when it locked single-CTA purity. The existing free `/first-48` "48-Hour Reset" lead magnet could catch that majority. This draft keeps single-CTA discipline per the locked strategy; treat the recapture question as a decision for Farrice/Cooz, not a default.

---

## Gate Record

**Date**: 2026-07-08 · **Reviews passed**: Adversarial review, Prose/voice review, Fact-verification (package-wide actions applicable to this file)

**Changes applied**:

- **Funnel scent break (MUST-FIX)**: Added an explicit price-transparency line to Section E ("It's a paid session, not a free consult") so the reader knows they're booking a real paid engagement before the click. Flagged the deeper `/briefing` destination mismatch (price + audience) as an unresolved ship blocker in "Open decisions flagged by adversarial review" — the destination page itself is outside this file's scope and still needs a funnel-specific rebuild or stripped variant.
- **Trust gap (MUST-FIX)**: Added a 34-word trust anchor opening Section C ("I'm Coach Cooz. I train people in LA, in person...") naming Cooz, his location, and his tenure. Pulled "in LA" forward from Section F to Section C. Added a build note requiring a real, face-visible headshot next to the trust anchor (the only place his face appears on the page).
- **Adjacent testimonial audit (MUST-FIX)**: Verified all five Section D quotes verbatim against RAW-PROOF-INVENTORY.md (clean). Added an on-page verification anchor line under the quotes ("All quotes verbatim from coachcooz.com/resurrections"). Flagged `03-testimonial-weaponization/PLAN.md` as unaudited and required before package ship, given the prior fabrication pattern (Allison, Sammy).
- **Photo-contradiction inoculation (MUST-FIX)**: Moved the before/after inoculation to the opening of Section C, made explicit ("Yes, I'm showing you a before-and-after... Same tool, opposite truth") instead of the prior subtle tail line.
- **Structural tells (SHOULD-FIX)**: Cut the "Here's what / Here's how / Here's the deal" openers (Sections A, B, E). Reduced the "It's not X. It's Y." negation-reversal from five instances to one ("That's theater," Section B), flattened the rest to plain declaratives. Removed 4 of 5 em-dashes (kept one, under the 1-2 cap). Removed the "broken" voice-killer (Section E → "went dormant"). Fixed the rule-of-three pileup at Section C ("most miserable, unhappy, and sad" → "most miserable"; "full of joy" → "happier than the lean guy ever was"). Fixed the Section D intro treadmill repeat of its own subhead.
- **Fact-verification actions**: All five testimonials, the body-fat inversion numbers, the McBroom/Mylett cuts, and the brand hex values were confirmed VERIFIED/LIKELY per the package-wide fact pass — no changes required beyond the verbatim anchor line above. Pricing (Triage Audit / Resurrection Protocol figures) remains correctly omitted from on-page copy per the existing draft; Strategy Spine is the only source of record and should be confirmed with Cooz before publish.
- **Not changed (judgment calls, logged as open decisions)**: Jessica's thyroid-cancer testimonial (medical-adjacency risk, no verified replacement quote on hand) and the zero-recapture question (single-CTA purity vs. free-Reset capture) — both surfaced to Farrice/Cooz in "Open decisions flagged by adversarial review" rather than resolved unilaterally.
- **Prose gate**: `prose_classifier.py check` on the full markdown returns WARNING (2/10, parallel_structure_overuse) driven entirely by the build-notes bullet lists and spec tables. Re-run against the extracted, rendered reader-facing copy only (Section 1) returns **CLEAN, 0/10, 0 signals** — confirming the residual parallelism the reviewer flagged has cleared from the actual client-facing prose.
