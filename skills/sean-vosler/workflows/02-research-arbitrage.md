---
description: Run the full sourcing engine in one session — trending-structure mining, Amazon subtitle mining, community review mining, and live-ad anatomy — producing a validated language bank of headline skeletons, statements, empathy bullets, and objections.
---

# Research Arbitrage → Validated Language Bank

The market has already voted on this language. Every method here rides an existing ranking mechanism instead of raw search — **the sort-order is the research tool.** Best-seller rank, "most helpful" votes, and ad run-length are free conversion data. "Companies don't leave poorly converting ads running for long."

## Pre-Flight Gate

1. **This workflow IS the mining pass** required by Hard Veto 1. Nothing downstream (01, 03, 04) may draft without its output. Run it before any copy work, never after.
2. **SMART objective written first** (Pattern 7 — Objective Before Tactics, p42): "In this [medium] I want to convince my reader that [specific feature] is better for accomplishing [specific task] than their current method…" Every method in the book begins "Step 1: define your objective." Objective-less mining collects trivia.
3. **Niche + adjacent surfaces named.** One in-niche category and at least one adjacent bestseller (adjacent titles carry the audience without the direct-competitor blind spots).
4. **Ad research availability declared.** AdvertSuite or equivalent live-ad archive available → run Method 4. Not available → say so in the deliverable rather than substituting invented ad data.

## Skill Acquisition

- `skills/sean-vosler/genius.md` — always. Patterns 1 (Research Arbitrage First) and 11 (Annotate-in-Place); Hidden Knowledge items 1 (sort-order) and 2 (same surface, stacked methods).
- `references/frameworks.md` §1 (6-Step Forming Headlines, master formula, sub-title mining, headline function checklist, 32-prompt Imitation Game), §2 (Community Arbitrage 5-step, bullet formula, Advertising Anatomy + 30-question checklist), §8 (Gold Ring 5-stage pipeline), §11 word banks.
- Bank shipping into Farrice-voiced copy? Load `_active/farrice-brand/voice/VOICE-CARD.md` as a **layer** at the assembly step only — never during mining. Mined language is evidence; voice-fitting it too early destroys the provenance.
- **Before fetching any surface, get its route**: `python3 execution/surface_router.py route "<surface>"` — prints the working tool chain, cost, known walls, and escalation (e.g., Reddit = Playwright + in-page `.json` fetch; WebFetch is blocked there). One failed hop max; escalate via the registry, never retry the same wall. Miners' dispatch briefs carry the printed route per surface.

## Execution

**1. Imitation Game — trending-structure mining (headline skeletons).**
Aggregators: digg, reddit, news.google, medium, buzzfeed, cracked. The whole discipline is one line: *"focus less on what's being said, and more on how it's structured."*
Six steps: **Brief** (objective + desired action) → **Research** (pull high-engagement headlines regardless of topic) → **Formulate** (strip to skeleton: "The [noun] Who Perfected The [topic]") → **Develop** (interrogate WHY it works — curiosity? belief-confirmation? open loop?) → **Adapt** (plug in audience + topic) → **Expand / "feed the need"** — mint a *family* from one skeleton by swapping the psychological modifier: **Modifier = End Result + Time Frame**, plus variants keyed to Fear of Loss / Fear of Change / Fear of Unknown + Hope.
Master formula: **Attention Grabbing Headline = "Audience Identifier" + "Hook" + "Benefit."** Jobs: headline = capture attention + frame problem; sub-headline = hint at solution + address main objection.
Function checklist — each candidate must do ≥1 of: Conjure Curiosity / Provoke Thought / Confirm Suspicion / Create Intrigue / Promise Powerfully / Question Reality — **and** pull the reader down the page. Legal rule carried from ad research: emulate FORM; never lift words and structure together.

**2. Amazon subtitle mining (promises).**
"Don't judge a book by its cover… judge by its subtitle." Best-sellers in-niche, sorted by rank → collect subtitles → tag each by persuasion mode (**Contrarian / Intriguing / Inspiring / Powerful Promise**) → abstract to skeleton ("A [adjective] Approach to [enticing promise]") → repopulate for your audience → expand with a consequence clause. The subtitle is the promise carrier; the title is branding.

**3. Community Arbitrage — review mining (empathy language). Same visit, second method.**
1. Pick an adjacent bestseller.
2. Read the **"most helpful"** reviews — top ~10 pasted verbatim into one doc. Never sort by recent.
3. **Two-color highlight**: **YELLOW = the reader's inner dialogue / self-talk. RED = emotional pull.**
4. Extract each highlighted **Statement** and rephrase twice: (a) as a Statement hook (headline candidate), (b) as an **empathy bullet** — *"[Empathetic question echoing their self-talk]? [Solution] helps you [benefit], without [objection/cost]."* Example shape: "Feel like you've put your personal growth on the back burner for too long? …"
5. Assemble a test block: Headline + soft-CTA sub-head + 4 bullets + hard CTA (+ authority quote).
Governing rule: *"If it's true, and it's a benefit to the reader, it's worth sharing."*
**Bullet formula for every bullet in the bank: (Feature) + (Benefit) + (Benefit of that benefit)** — and layer 3 stays unstated in final copy, converted to an imagination trigger (Hard Veto 5). Register/checkout pages take the hook-bullet variant instead: short open-loop curiosity bullets.

**4. Advertising Anatomy — live-ad mining (structure + objections), when available.**
Objective → keyword search across Ad Text / Comments / Landing Page Text → sort by engagement, then by **Running Longest** → tighten filters progressively. Capture per ad, six items: full screenshot, verbatim text doc, landing link, landing screenshot, more-info screenshot, top comments. File into Trello — columns = keywords, cards = ads, search params logged on the card.
Then run the **30-question Advertising Emulation checklist** per ad: target, funnel goal, price, attention grabber, benefits, engagement driver, mood, dream inspired, thesis, story, contrarian view, emotions, lessons, CTA, warnings, facts, authority, desires, enemy, pains, entertainment, objections handled, repetition, associations, fears + hopes, what was effective, what was ineffective.
The comment threads are the objection bank — the highest-value and most-skipped half of this method.

**5. Same-surface stacking.** One session feeds all four banks simultaneously. Amazon serves subtitle mining AND review mining in a single visit; AdvertSuite serves structure AND objections. Do not run these as four separate sessions.

**6. Gold Ring refinement.** Mine broadly with no filtering → first separation (relevant vs. adjacent-for-later) → **smelt against a PRE-SET standard** (set it before mining; the guards are research-loop time-sink, missed vitals, and disinformation) → refine into structure → craft into the delivered bank. "A gold ring crafted by Cartier is worth much more than the raw gold."

**7. Annotate the bank.** Function-tag every captured artifact with the beat it can serve (Acknowledgement / Aggravate / Angst / objection / proof). Untaggable material is filler — cut it.

`Execution prompt: references/prompts-v2/research-arbitrage-language-bank.md — honor its Output Contract.`

## Content Type Adaptations

| Deliverable the bank feeds | Emphasize | Bank shape |
|---|---|---|
| Sales page | Subtitle mining (promise) + review mining (empathy bullets) | Full four-bank set; 15+ bullets, 10+ objections |
| Email sequence | Review-mined self-talk statements (subject lines) + comment objections | Statement bank weighted; one objection per email |
| Social long-form | Imitation Game skeletons + trending structure; run the 32 prompts | Headline family per post idea; light bullet bank |
| Paid ads | Advertising Anatomy + 30-question checklist; longest-running only | Structure teardowns + hook bank + comment-mined objections |
| Cold-traffic VSL / webinar | Review mining for stakes language + ad comments for objections | Objection bank weighted heaviest |

## Output Requirements

A single `language-bank.md` containing:
- SMART objective sentence and the pre-set smelting standard.
- **Headline skeleton bank**: each skeleton + its source URL + why-it-works note + the minted family (End Result+Time Frame / Fear of Loss / Fear of Change / Fear of Unknown+Hope).
- **Subtitle bank**: subtitle + persuasion-mode tag + abstracted skeleton + repopulated version.
- **Statement bank**: verbatim highlighted statements, marked YELLOW (self-talk) or RED (emotional pull), each with source review.
- **Empathy bullet bank**: every statement converted through the empathy-bullet template and the *(Feature)+(Benefit)+(Benefit of that benefit)* formula.
- **Objection bank**: from ad comments and review criticism, each mapped to one of the 7 objection types.
- **Ad teardowns** (if run): six captured items + 30-question answers per ad. If ad research was unavailable, state that plainly — do not fabricate ad data.
- Provenance column on every row: source URL, sort mechanism used, capture date.
- `Execution prompt: references/prompts-v2/research-arbitrage-language-bank.md — honor its Output Contract.`

## Quality Gate

1. **Ranking-lens check (Hidden Knowledge 1).** Every surface was mined through a sort order — best-seller rank, "most helpful," or Running Longest. Anything mined by recency alone = FAIL.
2. **Provenance completeness (Hard Veto 1).** 100% of bank rows carry a source. Zero invented persona language, zero paraphrase presented as verbatim.
3. **Bullet formula compliance.** Every bullet has all three layers, with layer 3 held for the imagination trigger downstream (Hard Veto 5).
4. **Stacking check (Hidden Knowledge 2).** One session produced headline + bullet + objection banks together, not sequential single-purpose passes.
5. **Family, not a single.** Every retained skeleton yields a testable headline family, not one line.
6. **Emulate form, not words.** No captured competitor copy reproduced with both its wording and its structure intact; unverified stats in mined material carried forward flagged, never as fact (Hard Veto 6).
