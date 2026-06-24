---
description: Produce Parallax Substack editions — trending research, briefing, drafting, prompt packs, LinkedIn cross-promo. Full pipeline from zero to publish-ready.
tier: system
---

# `/parallax` — The Parallax Production Engine (v1.0)

Produces publish-ready Substack editions for Parallax at will. Each run: trending topic research, Farrice briefing, edition drafting with expert stacks, prompt pack engineering, and LinkedIn cross-promotion assets.

## Quick Start

```
/parallax                          # Full pipeline — research → brief → draft → publish-ready
/parallax --topic "AI emotions"    # Skip research — Farrice already has a topic
/parallax --batch 3                # Produce 3 editions in one session
/parallax --quick                  # Skip research + briefing — Farrice provides raw take directly
```

---

## What This Produces (Per Edition)

1. **The Edition** — 800-1200 word essay, Parallax voice, anti-slop certified (Phase 3)
2. **The Prompt Pack** — Single-prompt coaching session (Nate B. Jones / IP Flywheel standard) (Phase 4)
3. **5 Substack Notes** — Trailer-quality launch-week batch following the Notes Trailer Playbook (Phase 4.5). The 5 archetypes: Origin Wound (T-2), Asset Drop (T+0 AM), Counterintuitive Truth (T+0 PM, restack-bait), Public Reckoning (T+2-3), Bridge (T+5-6). Voice-compatibility-tested.
4. **3 LinkedIn Posts** — Insight variant, prompt teaser, output screenshot concept (Phase 5)
5. **Package File** — Canonical ship file at `parallax-packages/0N-[slug].md` with everything inlined for one-scroll review and direct copy-paste to Substack (Phase 5.5)

---

## The Publication: Parallax

- **Name**: Parallax — "For people who see everything from more than one angle."
- **Author**: Farrice "Fresh" Cain
- **Audience**: Multi-passionate people, polymaths, nerds, gamers, fitness people
- **Core thesis**: Your interests aren't scattered. They're ingredients. Nobody told you the recipe yet.
- **Format**: Essay + prompt pack per edition. The essay creates the insight. The prompt pack creates the transformation.

---

## Phase 1: RESEARCH (Skip with `--topic` or `--quick`)

**Time**: 5-10 min (AI only, no Farrice time)

Scan the current zeitgeist for brandjack opportunities:

1. Deploy Perplexity (check budget at `.agent/perplexity-usage.json` first):
   - "trending topics [current week] personal development technology culture"
   - "what's viral on Substack this week"
   - "creator economy solopreneur news this week"
   - Any domain-specific trends (AI, gaming, fitness, spirituality, parenting)

2. Scan Substack trending, LinkedIn solopreneur/creator conversations

3. For each topic found, score on:
   - **Existing attention** (High/Medium/Low): Is there a conversation to jack?
   - **Polymath angle**: Can Farrice connect this to 2+ of his interest domains in a way nobody else is?
   - **Prompt pack potential**: What micro-transformation pairs with this topic?

4. Present **5-8 trending topics** as a concise briefing to Farrice:

```
TOPIC: [Name]
Why it's trending: [1-2 sentences]
The Parallax angle: [How Farrice uniquely sees this]
Prompt pack concept: [What the coaching session would do]
Brandjack potential: [High/Medium/Low]
```

**HALT. Wait for Farrice to select a topic (or topics if `--batch`).**

---

## Phase 2: BRIEFING + RAW TAKE (Skip with `--quick`)

**Time**: 5-10 min Farrice time

Once Farrice selects a topic:

1. Present a **concise but nuanced briefing** on the selected topic:
   - Key facts, data points, quotes worth referencing
   - What the mainstream conversation is saying
   - The angles nobody is taking (the Parallax opportunity)
   - Which of Farrice's interest domains intersect with this topic
   - Suggested edition arc position (Identity / Pain / Depth / Power / Permission)

2. Ask Farrice: **"What's your take? What do you want to say about this that nobody else is saying?"**

3. Capture his raw take (voice note, bullets, stream of consciousness — all valid)

**HALT. Wait for Farrice's raw take before drafting.**

---

## Phase 2.5: GROUND + ZEITGEIST CHECK (MANDATORY for Editions 02+)

**Time**: 10-15 min (AI-only, then 60-90s Farrice review of the Grounding Report)
**Fires**: Automatically after Phase 2, BEFORE Phase 3 plan mode
**Purpose**: Kill fabrications and cultural inaccuracies before they reach the plan file. Every anchor that enters Phase 3 is either VERIFIED (external source) or VERIFIED-FROM-USER (Farrice's personal experience). No exceptions.
**Bypass**: Only via `--no-ground` flag (Edition 01 pure-personal pattern). Not Farrice's call to skip mid-session; this is the pre-draft gate that makes /parallax one-shot reliable.

**Browser tools available in Phase 2.5**: For PERSON, BRAND, and EVENT claims where the primary source is JS-rendered (LinkedIn profiles, modern brand sites, festival lineup pages, news sites with dynamic content) or login-gated, Playwright (`mcp__playwright__browser_navigate` + `browser_evaluate` or `browser_take_screenshot`) is the highest-fidelity verification path. Use it as a tier above `perplexity_ask` when the claim is high-stakes (named public figure, specific quote, exact date) and the source URL is known. WebFetch on these surfaces returns hydration shells that lead to false UNCONFIRMED labels. See `directives/browser-automation-routing.md` for the full decision matrix; `directives/browser-automation-safety.md` governs Tier 2 actions (none should fire during verification — Phase 2.5 is read-only).

**Video tools available in Phase 2.5**: When a claim references a specific video moment (a DJ's set, a viral clip, a livestream, a music video sequence, an interview moment), `execution/fetch-video-context.py` is the canonical evidence path — it pulls actual frames from the source video that can be cited as VERIFIED evidence. **This directly addresses the Edition 02 fabrication failure mode** (Madeon set citation hallucinated visual details that didn't exist). When a video claim must be verified, fetch frames first, then verify the claim against the actual frames before tagging it VERIFIED. See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). Wrapper auto-skips non-video sources, >10min videos.

```bash
# Example: verify a "Madeon at <festival>" claim
// turbo
python3 execution/fetch-video-context.py "<festival-set-youtube-url>" "verify-$(echo "$url" | shasum | head -c 8)" || true
# Then read extractions/verify-*/visual-context.md and 5-10 frames before tagging VERIFIED
```

### 2.5.0 — Short-Circuit Detection (runs first, before any tool call)

Scan the raw take + topic + planned anchors for **External Factual Surface**:
- Named people other than Farrice's immediate circle (Jen, JJ, Ryan, Laarni, close family)
- Named brands, products, companies
- Events/dates (a specific weekend, paper, product launch, news moment)
- Statistics or "X% of people" / "N years of" claims
- Direct quotes from others (the nephew, a stranger, a thought leader)
- Cultural moments (a viral post, a trend, a news story)
- Technical/scientific claims (a study, a paper, an AI capability)

**If External Factual Surface == 0** (pure personal edition, Ed 01 Manifesto pattern):
- Skip Step 2.5.2 (full verification) entirely
- Run abbreviated Step 2.5.3 (one `perplexity_ask` for zeitgeist around the theme)
- Deliver abbreviated Grounding Report: "PURE PERSONAL — no external claims to verify"
- Total time: 3-5 min

**If External Factual Surface ≥ 1**: Run full Phase 2.5 below.

### 2.5.1 — Claim Extraction (5 min, no tools)

Produce a claim ledger. Every extracted claim gets a row:

| ID | Claim | Category | Source in Raw Take | Verification Route |
|----|-------|----------|---------------------|---------------------|
| C1 | [exact claim] | PERSON / BRAND / EVENT / STAT / QUOTE / CULTURAL / TECHNICAL / PERSONAL | [quoted phrase or "planned anchor"] | RECALL / PERPLEXITY-ASK / PERPLEXITY-RESEARCH / HUNT-TRENDS / NONE |

**Extraction rules:**
1. Separate composite claims. "I saw Bad Bunny at Coachella W2" → C1 PERSONAL (Farrice attended Coachella W2, NO-VERIFY) + C2 EVENT (Bad Bunny performed at Coachella W2 2026, VERIFY).
2. TECHNICAL category requires: paper title, authors, venue, year, DOI/URL, one-sentence conclusion. If any missing → auto-label FABRICATED-RISK.
3. Any hedge language from Farrice ("I think", "I vaguely remember", "something like") → auto-flag UNCONFIRMED even if category is PERSONAL.
4. Implicit directional claims ("the drag was from X to Y") → convert to explicit claims before extraction. CULTURAL framings often hide direction.

**Inner-circle list (NO-VERIFY for PERSON category)**: Jen (wife), JJ (son), Ryan (best friend, JJ's godfather), Laarni, close family referred to by first name. Extended references get verified.

### 2.5.2 — Verification Routing (6-8 min, parallel where possible)

**Budget check FIRST** (read `.agent/perplexity-usage.json`):

| Remaining | Action |
|-----------|--------|
| ≥$5 | Full Phase 2.5 — up to $1.25 per edition, 12-18 Sonar Pro queries + 1 Deep Research for TECHNICAL |
| $2-5 | Sonar only (no Sonar Pro, no Deep Research). Cap 8 queries. Collapse aggressively. |
| $0.50-2 | Recall-first. Perplexity reserved for TECHNICAL + top 3 risk claims. Max 4 queries. |
| <$0.50 | **Recall-only grounding.** All external claims not hitting Recall auto-label UNCONFIRMED → Farrice decides per claim. Surface budget state in Grounding Report header. |
| Would bust mid-run | Stop, deliver partial report tagged "PARTIAL — budget cap hit at claim N/M." |

**Routing matrix** (fire parallel-eligible calls in ONE assistant message for concurrency):

| Category | Primary | Fallback | Parallel? |
|----------|---------|----------|-----------|
| PERSON | `mcp__recall__search` + `perplexity_ask` | `search_web` | Yes |
| BRAND | `perplexity_ask` | `search_web` | Yes |
| EVENT | `perplexity_ask` (recency filter) | `search_web` site-specific | Yes |
| STAT | **Gemini Deep Research** (primary source citation) | `perplexity_research` (Perplexity fallback) → `search_web` + `read_url_content` | No |
| QUOTE | `perplexity_ask` (exact phrase, quoted) | `search_web` quoted | Yes |
| CULTURAL | `perplexity_ask` (live sentiment) OR reuse `/hunt-trends` Track B if Phase 1 ran | `search_web` site:reddit.com + site:twitter.com | Yes |
| TECHNICAL | **Gemini Deep Research** + citation audit (6 fields required) | `perplexity_research` (Perplexity fallback) → `perplexity_ask` + `read_url_content` | No |
| PERSONAL | NONE (logged, skipped) | — | — |

**Collapsing rule**: Group same-category claims into single multi-part queries. 3 EVENT claims = 1 query. Saves budget.

**Recall-first for Farrice's orbit**: PERSON and CULTURAL claims about figures in the creator economy, gaming, spirituality, fitness — hit `mcp__recall__search` first. 2+ high-signal cards = skip Perplexity for that claim.

**Parallel agent deploy** (`/parallel-research`): only when ≥8 external claims across ≥3 categories. Otherwise direct Perplexity calls are faster and cheaper.

**TECHNICAL rigor**: The paper query MUST return title + authors + venue + year + DOI/URL + one-sentence conclusion. Missing any → FABRICATED-RISK. This catches the Ed 04 "Berkeley paper on 7 AI models fawning" pattern directly.

**Log every Perplexity call to `.agent/perplexity-usage.json`.**

### 2.5.3 — Zeitgeist Check (2-3 min, PARALLEL with 2.5.2)

Fires in the same assistant message as the 2.5.2 verification calls.

Single `perplexity_ask` with recency filter (last 7 days):

```
"What is the current online conversation (last 7 days) saying about [TOPIC]?
Include: (a) the dominant narrative on Reddit/X/Substack, (b) the
counter-narrative or contrarian takes, (c) any developments that would
change how someone should write about this, (d) what angle is already
saturated vs. what's being missed. Cite 6-10 sources."
```

If `/hunt-trends` already ran in Phase 1, reuse that output instead.

**Zeitgeist output format**:

```
## Zeitgeist Check: [TOPIC]

**Dominant narrative right now**: [1-2 sentences]
**Counter-narrative**: [1-2 sentences]
**Recent developments (last 7 days)**: [bullets]
**Already saturated takes**: [avoid these angles]
**Underexploited angles**: [what's open]
**Farrice's stated angle vs. zeitgeist**:
   ALIGNED / DIFFERENTIATED-AND-DEFENSIBLE / CONTRARIAN-REQUIRES-MORE-PROOF / FLAT-WRONG-ON-FACTS
```

**Gate behavior**: FLAT-WRONG-ON-FACTS → halt, require pivot before plan mode. CONTRARIAN-REQUIRES-MORE-PROOF → Phase 3 plan must include proof architecture (Luke Iha Proof Ladder auto-loads).

### 2.5.4 — Grounding Report (single delivery to Farrice, 60-90s review)

```
# Grounding Report: Edition [XX] — [topic]

**Budget**: $[X.XX] used / $[Y.YY] remaining this month
**Claims**: [N] total | [M] external-verifiable | [P] personal (skipped)
**Verdict**: ALL-CLEAR / PIVOTS-REQUIRED / HALT-AND-RETHINK

## Claim Ledger

| ID | Claim | Category | Status | Source / Note |
|----|-------|----------|--------|---------------|
| C1 | Bad Bunny headlined Coachella W2 2026 | EVENT | VERIFIED | Pitchfork + Coachella.com |
| C2 | Olivia Rodrigo 2am walk | EVENT | FABRICATED-RISK | No coverage. Suggest: cut or reframe as personal memory |
| C3 | UC Berkeley paper on 7 AI models fawning | TECHNICAL | FABRICATED-RISK | No such paper. Closest real: [title + URL]. Suggest: pivot anchor |
| C4 | "15 years of Dash Star hype" | STAT | LIKELY-WRONG | Song released ~2023. Actual: ~3 years. Suggest: correct or cut timeframe |
| C5 | Farrice attended Coachella W2 | PERSONAL | NOT-VERIFIED (personal) | Trust user |

### Status legend
- VERIFIED: 2+ independent sources. Use freely.
- LIKELY: 1 credible source. Usable with single-line hedge.
- UNCONFIRMED: Couldn't verify. User's call: cut / soften / proceed with personal tag.
- LIKELY-WRONG: Evidence contradicts. Recommend: correct or cut.
- FABRICATED-RISK: No support AND claim is falsifiable. Recommend: cut or pivot.
- PERSONAL: Not externally verifiable. Trust user.

## Zeitgeist Check
[Insert 2.5.3 output]

## Recommended Pivots (if any FABRICATED-RISK or LIKELY-WRONG)

1. **C2** → cut OR reframe as "I remember walking back around 2am"
2. **C3** → replace with [verified real paper], OR cut paper anchor, use different proof borrow
3. **C4** → correct to "3 years of hype" OR cut timeframe entirely

## Gate Decision

- 0 FABRICATED-RISK + 0 LIKELY-WRONG → ALL-CLEAR. Proceed to Phase 3 plan mode.
- 1-3 FABRICATED-RISK/LIKELY-WRONG → PIVOTS-REQUIRED. Present pivots, HALT for Farrice.
- ≥4 FABRICATED-RISK/LIKELY-WRONG OR Zeitgeist = FLAT-WRONG → HALT-AND-RETHINK. Topic's factual foundation too thin; recommend different topic or deeper research before draft.
```

### 2.5.5 — Halt/Proceed Gate

Farrice's options:
1. **Approve all** → proceed to Phase 3. VERIFIED/LIKELY claims enter the plan as "verified anchor facts."
2. **Apply pivots** → accept proposed substitutions. Updated ledger replaces originals. Proceed.
3. **Manual edit** → Farrice writes his own substitutions. Capture, proceed.
4. **Abort topic** → return to Phase 1 or Phase 2 with a different topic.

**What enters Phase 3's plan**:
- VERIFIED claims → "3-5 verified anchor facts" as VERIFIED (from Phase 2.5)
- LIKELY claims → enter as LIKELY with source URL in plan comment
- PERSONAL claims → enter as VERIFIED-FROM-USER
- **UNCONFIRMED / FABRICATED-RISK / LIKELY-WRONG claims → PROHIBITED from plan. Replaced per pivots or cut.**

### 2.5.6 — Expert Stack Integration

Phase 2.5's output modifies Phase 3's expert loading:
- **TECHNICAL claims exist** → auto-load Luke Iha Proof Ladder for weaving the verified paper correctly
- **CULTURAL / EVENT claims dominate** → auto-load Shaan Puri Storytelling (cultural pulse) + optionally `.agent/workflows/jackpost.md` reference

### 2.5.7 — Phase 3 Audit Additions

The Pre-Delivery Mechanical Audit in Phase 3 grows a new grep check:
```bash
# Grep the draft against the FABRICATED-RISK and LIKELY-WRONG claims from Phase 2.5
# ANY hit = automatic rewrite before delivery
```

If a claim that was flagged in Phase 2.5 slipped into a draft variant, it gets caught before Farrice sees it.

---

## Phase 3: DRAFT THE EDITION

**Time**: 10-15 min (AI), 5-10 min Farrice review

### Plan Mode Entry (MANDATORY for Editions 02+)

For Edition 01 (first in a publication) you may draft directly after Phase 2 raw take.

For **Editions 02 and onward** (anything that must cohere with prior Parallax work), **enter plan mode before drafting**. The plan file captures:

1. **Theme under 10 words** — the single thing this edition is about
2. **Tether** — the anchor scene every section returns to
3. **3-5 verified anchor facts** — pulled from Farrice's raw take, each labeled VERIFIED-FROM-USER or UNCONFIRMED
4. **Voice markers to preserve** — specific phrases, rhythm patterns, imperfections from his raw take

**Stanton architecture pass (the spine the edition is built on)** — before drafting, run `/stanton-premise-sentence` (the one true sentence: character + conflict + conclusion, used as a litmus not an outline), `/stanton-spine` (the edition's protagonist wiring + one-liner), and `/stanton-change-engine` (the five-second change the reader moves through). The Theme/Tether above are the *topic*; this is what makes the reader *move*. Load `skills/andrew-stanton-audience-engineering/genius.md`. The premise never appears on the page — it organizes every section invisibly.
5. **Banned patterns especially at risk** — which of the structural-tells are most likely to appear in this particular topic (e.g., contrast-reveals are especially tempting for cultural-commentary pieces)
6. **Subject line + preview text options** (2-3 of each)
7. **Cross-edition trope diff plan** — which moves from prior editions are off-limits

Present the plan. Farrice approves or edits. **No drafting until the plan is approved.** The plan catches factual fabrications, voice drift, and structural collisions BEFORE they're written into prose.

### 3-Variant Production Rule (MANDATORY for all editions)

**Never produce a single draft and present it as the draft.** Farrice's content voice calibration (see MEMORY) requires 3 variants so he can pick, combine, or Frankenstein the best parts. One draft = pressure to "get it right on the first try," which collapses into over-performed safe writing and costs iterations on the back end.

**For full editions (800-1200 words): produce 3 COMPLETE DRAFTS, each written from a distinct angle / perspective / worldview.** Not three openings with the same body. Three full drafts, front to back, that make different choices.

**How to differentiate the three drafts** (pick the three that best fit the topic — don't force the same triple every time):

| Dimension | Variant A | Variant B | Variant C |
|---|---|---|---|
| **Angle** | Personal / confessional (memoir first) | Observational / critical (outside-in, pattern-spotting) | Framework / coaching (teach the reader a lens) |
| **Opening** | Scene, emotional anchor first | Claim or observation first | Contrarian challenge to a reader belief first |
| **Voice** | Vulnerable / intimate | Analytical / wry | Punchy / directive |
| **Worldview** | The parent's lens (JJ, Jen, family stakes) | The strategist's lens (system patterns) | The contrarian's lens (fighting the default narrative) |
| **Structure** | Linear narrative | Braided (scene → idea → scene) | Thesis + three proofs |
| **Close** | Return to the opening scene | Zoom to the pattern | Hand the reader a tool |

Pick the three dimensions of contrast that serve THIS edition's topic best. Don't copy the matrix literally every time — use it as a generator. The goal is that the 3 drafts feel written by 3 different versions of the author, not the same author three times.

**Deliverable per edition:** All three drafts, clearly labeled (Variant A / B / C), each with a 1-line "strength" summary and a "my lean" recommendation. Farrice picks one outright OR names specific beats he wants combined from multiple variants ("V-A's opening + V-C's close + V-B's insight beat"). Then assemble the final draft from his selection.

**For short sections** (single-paragraph rewrites when an approved draft needs one beat refined): produce **3 variants of that section only** — scope matches the ask.

**When to skip variants**: Only when Farrice explicitly says "just draft it" or "one pass is fine." Default is always 3 variants.

**Origin**: Farrice content-voice-calibration memory (3-variant creative process), reinforced and expanded in Ed 03 session 2026-04-21. Farrice clarified: "3 variant of the entire drafts not just the sections... each with different angles and perspectives and world-views."

### Expert Loading

Load based on topic domain (check Hot Context first):
- **Default stack (ALWAYS load for editions 02+)**:
  - Nicolas Cole (`skills/nicolas-cole-newsletter-flywheel/`) — sentence craft, newsletter architecture
  - Kallaway (`skills/kallaway-content-psychology/`) — dopamine ladder, hooks, anticipation engineering
  - **Erica Mallet** (`skills/erica-mallet-brand-magnetism/`) — Enemy Effect, belief architecture, tribal resonance
  - **Luke Iha Proof Ladder** (`skills/luke-iha-proof-ladder/`) — proof borrowing from brands, papers, cultural events (critical for newsjacking/brandjacking editions)
  - **David Bayer Radical Distillation** (`skills/david-bayer-elite-communication/genius.md` — load signature move 5 + "Distill up, don't dumb down" pattern only, not the full skill) — the texture layer that makes every insight land. Distill UP (deeper truth, simpler words), never dumb DOWN. Reader feels "I already knew that, I just needed someone to say it," not "wow, he's smart." One everyday analogy carries 90% of a complex idea. This is the always-on delivery filter the other experts get spoken through.
- **If newsjacking a cultural moment** (Ed 02 Coachella, Ed 04 Berkeley paper, any trending topic): + `skills/shaan-puri-storytelling/` (cultural pulse) + reference `.agent/workflows/jackpost.md` for borrowed-attention patterns
- **If brandjacking a specific brand or product** (Ed 03 EllaOla): + `skills/harry-dry-copywriting/` (examples-driven punch) + reference `.agent/workflows/proof-braid-engine.md` for weaving proof naturally
- **If AI/tech topic**: + `skills/seth-godin-ideavirus/` (category creation, spreadability)
- **If inner work/psychology**: + Steven Pressfield (narrative physics)
- **If gaming/anime**: Deploy tribal vocabulary from FARRICE.md
- **If spirituality**: Deploy Neville Goddard / Joe Dispenza frameworks from FARRICE.md
- **If fitness**: Deploy training science from Farrice's 18 years

**Why the default stack matters**: Parallax editions rely on borrowing cultural pulse and/or proof to land their insight. Ed 02 borrowed the Coachella/Bieber cultural moment. Ed 03 brandjacked EllaOla. Ed 04 will borrow from a Berkeley paper. Without Luke Iha Proof Ladder + Erica Mallet's Enemy Effect in the default stack, the writer drifts into abstract essay-voice instead of grounded proof-borrowed commentary. The Ed 02-03 session surfaced this gap.

### Drafting Rules

Read and enforce ALL of these:

**Voice DNA** (from FARRICE.md + memory):
- Show, never tell. Specific over general. Earned authority, not claimed.
- No guru energy. "What I discovered" not "what you should do"
- Comedy beats after heavy insights
- Imperfection IS the voice — not every sentence polished

**Anti-Slop Filter** (MANDATORY):
- Banned phrases: "Let's dive in," "game-changer," "transformative," "innovative," "moreover," "furthermore," "delve," "tapestry," "nuance" (as filler), "In today's fast-paced"
- Banned lead-ins: "Here's what happens when," "Because here's what nobody tells you about," any "Here's what/why/how..." paragraph opener, "Here's where..."
- Banned structural patterns: Green checkmark lists, "It's not X. It's Y." repeated, calm/balanced/earnest throughout
- Required markers: specific detail that couldn't be fabricated, opinion that could alienate, imperfect sentence structure, vocabulary matching Farrice's speaking voice

**AI Tell Prevention** (from memory/feedback_ai-writing-tells.md + feedback_writing-excellence-rules.md):
- Em dashes: max 1-2 per entire edition. Farrice doesn't use them naturally.
- Bridge phrases: NEVER repeat the same bridge across editions. Vary every time.
- Jargon: any technical term max 2-3 uses per edition, then switch to plain language
- Cross-edition trope audit: if producing multiple editions, search for repeated structures

**Radical Distillation** (David Bayer texture — always-on, runs on every edition):
- Distill UP, never dumb DOWN. Take the big idea and say it in the plainest, most human words available — short sentences, one idea at a time. The reader should feel "I already knew that, I just needed someone to say it," NOT "wow, he's smart."
- One everyday analogy carries 90% of a complex concept. ("A cage with better lighting" did this for the whole Manifesto thesis.) Find the one image that makes the abstraction instantly gut-level, then trust it.
- The "which means…" test: keep asking "which means…" until you hit what actually matters to the reader, then lead with that. Concrete over abstract every time ("be present for dinner at 5," not "achieve work-life integration").
- Failure tells (rewrite on sight): jargon, multi-clause sentences the reader has to work to parse, abstraction where a picture would land, anything that sounds like a presentation instead of one friend explaining it to another. If it lands in the head and not the gut, it failed.

**Quality Standards**:
- Hook grips cold readers immediately (standalone excellence — each piece works alone)
- Every word pulls its weight — no dead space, no drag
- Tightness pass before delivery — if a paragraph works in 2 sentences, cut to 2
- **Stanton clamp-audit (engagement pass)** — walk the edition beat by beat at reader's pace; mark each place attention would drop (the beach ball) and re-clamp it (open a debt / withhold the outcome / inject a change / cut exposition). "Polished but flat" is an unclamped draft, not a finished one. Run `/stanton-clamp-audit`; slips cluster at section seams and right after the best line, where the reader feels permission to stop.

### Edition Structure

```
Subject line: [6-10 words, curiosity-driven]
Preview text: [1 sentence complement]

[ESSAY — 800-1200 words]
- Opening: hook that creates tension requiring resolution
- Body: one core idea explored with depth, 2-3 sections
- Bridge: connect insight to reader's situation
- Prompt pack introduction: 2-3 sentences, links to pack
- Close: tease next edition + CTA (rotate: reply, share, forward)

Footer:
Written by Farrice Cain
Parallax — see everything from more than one angle.
```

### Pre-Delivery Mechanical Audit (MANDATORY — run BEFORE presenting)

Before showing the draft to Farrice, run these greps on the draft file. Any failure means REWRITE and re-audit — do not present a failing draft with caveats.

```bash
FILE="_active/farrice-brand/content/substack-v2-drafts/[XX]-[slug].md"

# 1. Em-dash count (body only, target 0-2)
awk 'NR>10 && !/Parallax — see/' "$FILE" | grep -c " — "

# 2. Contrast-reveal scan — flag any "isn't"/"wasn't"/"it's not"/"that's not"
#    followed by a reveal sentence pattern
awk 'NR>10' "$FILE" | grep -niE "isn't|wasn't|it's not|that's not"

# 3. Italicized aphorism check — standalone *...* lines (excluding metadata/signature)
grep -nE '^\*[^*]+\*$' "$FILE"

# 4. "Here's the thing / Here is the part / Here's what" framings — must be 0
grep -ciE "here's the thing|here is the part|here's what happens|here's what"

# 5. Triple-beat anaphora — 3+ consecutive sentences starting with same word
#    (run Python script from Ed 02 audit in plans/additional-edits-this-line-fluffy-cake.md)
```

**Audit checklist:**
- [ ] Em-dashes in body: ≤ 2 (Farrice prefers 0)
- [ ] No contrast-reveal patterns (banned per memory/feedback_ai-structural-tells.md)
- [ ] No standalone italicized aphoristic lines (ban)
- [ ] No "Here's the thing" / "Here's what happens" framings (ban)
- [ ] No 3-beat anaphora (ban)
- [ ] Cross-edition trope diff against prior Parallax editions: no shared closing gestures, no shared opening moves, no reused anaphoric structures

If any check fails: rewrite the offending passage, re-run the full audit, then deliver. Do NOT present a draft that fails any check "with acknowledgment" — that burns trust.

### Delivery

Present draft to Farrice with:
1. The draft (ready to paste into Substack)
2. Anti-slop report: banned phrases eliminated, required markers present
3. Mechanical audit results: all checks PASS
4. Voice note: any lines rewritten for voice + why

**HALT. Wait for Farrice's approval or edits.**

---

## Phase 4: ENGINEER THE PROMPT PACK

**Time**: 10 min (AI)

### The Standard (IP Flywheel / Nate B. Jones quality)

Each prompt pack is a **single prompt** that runs a complete coaching session:

1. **Expert role**: AI given specific methodology, not generic advice
2. **Phase 1 — Excavation**: 2-3 questions asked one at a time (user just answers honestly)
3. **Phase 2 — Analysis**: AI does all pattern recognition and insight generation itself
4. **Output**: Structured, actionable, screenshot-worthy — clear headers, specific deliverables

### Prompt Pack Architecture

```
Expert Role: [Specific to this edition's domain — not generic]
Methodology: [Embed Farrice's actual coaching frameworks, not surface-level self-assessment]
Excavation Questions (3, asked sequentially):
  1. [Experiential question — describe a moment, not a category]
  2. [Probing question — goes deeper into what they revealed]
  3. [Contrast question — reveals the gap between current and ideal state]
Analysis Output (AI produces all of this):
  A. [Diagnostic map of current state]
  B. [Pattern identification — what they can't see about themselves]
  C. [Specific action architecture — not advice, a SYSTEM]
  D. [One thing to do tonight/tomorrow]
```

### Quality Gate for Prompt Packs

Every pack must pass:
1. **The Zero-Knowledge Test**: Would someone with NO AI experience get a transformational result?
2. **The Coaching Test**: Does this prompt do what Farrice would do in a 30-min coaching session?
3. **The Screenshot Test**: Is the output structured enough that someone would screenshot and share it?
4. **The Reuse Test**: Would they run this again in 3 months and get different, valuable results?

### File Format

Write to: `_active/farrice-brand/content/prompt-packs/[XX]-[slug].md`
Structure: Title + metadata → "How This Works" → The Prompt (code block) → "What to Expect" → "Commentary" → "Advanced Variation"

---

## Phase 4.5: NOTES TRAILER BATCH (Updated 2026-04-27 — v1.2)

**Time**: 8-12 min (AI)
**Authority**: [_active/farrice-brand/content/parallax-packages/NOTES_TRAILER_PLAYBOOK.md](../../_active/farrice-brand/content/parallax-packages/NOTES_TRAILER_PLAYBOOK.md) v1.2

Generate the 5-Note launch-week batch that primes readers for this edition. Notes are **trailers, not clips** — original compositions in manifesto voice, not extractions from the edition.

### The narrative spine (use this first — playbook v1.2 Section 0)

Every Note follows: **Scene or confession → Reframe that changes how you see it → Quiet invitation.**

If the spine doesn't fit (e.g., Asset Drop where the asset itself is the middle beat), fall back to the WHAT/HOW/WHY trailer formula in playbook v1.1.

### The 5 voice rules (non-negotiable, every Note)

1. Open with the thing itself, never the setup.
2. Confession beats observation. Insert Farrice into the story.
3. Vary rhythm — short punches + long pressure-builders.
4. Never summarize what the reader will find. The link is for people already walking through the door.
5. Slot-machine close — every Note worth reading on its own.

### Generation procedure

1. **Load playbook + edition draft**: Read `NOTES_TRAILER_PLAYBOOK.md` Section 0 (spine + voice rules + 4 canonical examples from Ed 01 launch) and the just-finished edition body. Identify the edition's most quotable line (Counterintuitive Truth archetype) and its central thesis (Bridge archetype).

2. **Generate 5 Notes, one per archetype** — each obeys the Scene → Reframe → Invitation spine:
   - **Note 1 — Origin Wound** (T-2): Vulnerable scene from before the thesis was discovered. Reframe hints at the edition's central insight. Invitation = drop date.
   - **Note 2 — Asset Drop** (T+0 morning): Scene = the question or framework itself; Reframe = the recognition the asset triggers; Invitation = edition link. Copy-Paste Asset = 3.4x conversion lift.
   - **Note 3 — Counterintuitive Truth** (T+0 evening): Scene opens with the manifesto's signature line. Reframe = personal confession that grounds it. Invitation = "That's what Edition X is about" + link. Restack-bait — line must hold quoted out of context.
   - **Note 4 — Public Reckoning** (T+2-3): Scene = vulnerable admission, different angle from Note 1. Reframe = what that admission reveals about the work. Invitation = soft, screenshot-quality close.
   - **Note 5 — Bridge** (T+5-6): Scene from the next edition's territory. Reframe = the question that edition asks. Invitation = drop date, NO LINK (anticipation is the payoff).

3. **Run Voice Compatibility Test on each Note** (5 questions, all must pass):
   - Concrete opening test (first 7-10 words contain specific element — scene, not setup)
   - Authorship test (could only have been written by Farrice — confession present)
   - Rhythm test (varies within Note: long → short or vice versa)
   - Slot machine test (uncertain payoff close, NOT vending machine, NOT summary)
   - Standalone test (worth reading without the edition link)

4. **Run cross-batch audit**:
   - Em dash count across all 5 Notes: target 0, max 1
   - Italicized words: 0 or 1 per Note, never phrases
   - Structural variance: all 5 Notes use distinct opening patterns and closing gestures
   - Statement hooks only (no question hooks — 52% conversion penalty per 19,471-Note research)
   - Length: 32-63 words per Note (Bridge can be tighter)
   - No banned moves: no "It's not X. It's Y." reveals, no twin-sentence aphoristic endings, no triple-beat anaphora unless quoted from manifesto
   - **Confession check**: at least 3 of 5 Notes contain explicit first-person confession ("I spent years…", "I have a son", "I used to…"). Pure-observation Notes are weaker.

5. **Assign cadence**: Each Note gets a scheduling target (T-2, T+0 morning, T+0 evening, T+2-3, T+5-6). If the next edition drops sooner than T+6, compress the Bridge forward (Ed 01 → Ed 02 example: Bridge moved to T+0 evening, day before Ed 02 drop).

### Anti-patterns (kill on sight)

- Question hooks → 52% conversion penalty
- "Edition X is live" announcements → vending-machine pattern
- Verbatim extracts from edition without re-composition → clip behavior
- Generic "subscribe to my newsletter" CTAs → use value-rooted invitations
- More than 1 em dash → AI tell per existing voice rules
- **Summary in the closer** ("Edition X covers A, B, and C") → violates voice rule 4 (never summarize what the reader will find)

### Substack technical reference (production-critical — playbook v1.2 Section 0.5)

| Topic | Truth |
|---|---|
| Notes scheduling | Native since March 2026. Calendar icon in composer. Scheduled lives in Drafts tab. Edit by clicking schedule banner. |
| Post card auto-embed | Paste Substack URL → auto-expands as post card. No manual embed needed. |
| Pages vs Posts | Pages = permanent/evergreen but DON'T show in sections/feeds/emails. Posts = visible everywhere. **Prompt Packs must ship as Posts in the "Prompt Packs" section, NOT as Pages**, for section visibility. |
| First-line truncation | Mobile ~200 chars before "…read more." First 7-10 words carry load. |
| Email digest selection | Algorithmic. First 50 chars must work as standalone hook. |

### Output

5 Notes with archetype labels, scheduling targets, and Voice Test status. These get assembled into the package file in Phase 5.5.

---

## Phase 5: GENERATE CROSS-PROMOTION ASSETS

**Time**: 5 min (AI)

For each edition, produce 3 LinkedIn post variants:

### Variant A: The Insight Post
Extract the core insight from the edition. Reframe for LinkedIn's broader audience. End with: "I broke this down deeper in my newsletter — link in first comment."

### Variant B: The Prompt Teaser
Show a preview of what the prompt pack does (not the full prompt). Describe the transformation: "I built a prompt that [does X]. Here's what happened when I ran it..." CTA: "Get the full prompt pack — link in first comment."

### Variant C: The Output Screenshot Concept
Describe what a screenshot of the prompt output would look like. Include the hook: "I ran this prompt and here's what came back..." (For actual posting, Farrice runs the prompt himself and screenshots the real output.)

> **Note**: Substack Notes are NOT generated here. Notes are produced in Phase 4.5 via the Notes Trailer Playbook (5 archetypes, voice-compatibility-tested). LinkedIn variants in this phase are separate cross-platform assets.

Write to: `_active/farrice-brand/content/linkedin-posts/parallax-[edition-number]/`

---

## Phase 5.5: PACKAGE ASSEMBLY (New — 2026-04-25)

**Time**: 3-5 min (AI)

Assemble everything produced in Phases 3-5 into a single canonical package file at `_active/farrice-brand/content/parallax-packages/0N-[slug].md`. This is the file Farrice opens at ship time — top-to-bottom review, copy-paste to Substack, sync to Notion.

### Procedure

1. **Copy `_template.md`** to a new file: `parallax-packages/0N-[slug].md` (matching the edition number and slug)
2. **Fill metadata**: edition number, title, slug, status=`review`, target publish date, source paths
3. **Inline the edition body** (from Phase 3) into the Substack Post block
4. **Inline the prompt pack** (from Phase 4) at the bottom of the Substack Post body — embedded in the same post, not a separate post
5. **Inline the 5 Notes** (from Phase 4.5) into the Notes Batch section, each with archetype label, scheduling cadence, and pre-checked Voice Test boxes
6. **Pre-fill the ship checklist** items that are auto-verifiable (subject line length, voice rules passed, etc.) — leave human-verifiable items unchecked (mobile preview, prompt pack tested in Claude/ChatGPT)
7. **Fill the Notion sync checklist** with the actual `notion_api.py vault-create` command pre-baked with this edition's title and domain

### What this produces

A single 350-500 line package file Farrice can open, scroll through top-to-bottom, copy-paste from, and ship in one sitting. No file-hopping. No re-formatting at ship time.

### Status flow

`draft → review → scheduled → published → archived`

Status is updated in the metadata header as the package moves through the pipeline.

### Optional: Cover-art generation

After the package is assembled, optionally generate a Substack header image via `skills/fantastic-posters/`. Recommended styles by edition mood:
- Memoir / contemplative → `editorial-fashion`, `documentary-portrait`, `surreal-dreamscape`
- Counterintuitive / sharp → `swiss-minimal-typo`, `saul-bass-minimal`, `bauhaus-geometric`
- Cultural / nostalgic → `vintage-travel`, `art-deco`, `ukiyo-e`
- Cyber / future → `vaporwave-synth`, `neon-noir-cyberpunk`

Default quality: `medium` ($0.04/image). **Always pre-flight via `python3 execution/fal_budget_guard.py check --quality=medium --n=1`.** Output saved to `_active/farrice-brand/content/substack-v2-drafts/[edition]/cover.png`. Workflow file: `skills/fantastic-posters/workflows/deliverable-cover.md`.

---

## Phase 6: FINALIZE

Run the chain finalization:

```bash
python3 execution/chain_runner.py finalize "Parallax Edition [X]: [title]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow parallax \
    --type Content \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what the edition covers]"
```

---

## Reference Files

**Voice & Standards**:
- `FARRICE.md` — identity, interests, tribal vocabulary, avatar, voice
- `memory/feedback_ai-writing-tells.md` — banned AI patterns (em dashes, lead-ins)
- `memory/feedback_writing-excellence-rules.md` — hooks, jargon, tightness, trope variance
- `memory/content-voice-calibration.md` — full voice rules

**Expert Skills** (load as needed):
- `skills/nicolas-cole-newsletter-flywheel/` — newsletter architecture, prompt-as-product
- `skills/kallaway-content-psychology/` — dopamine ladder, hooks, C.A.P. Fit
- `skills/steven-pressfield-narrative-mastery/` — manifesto engine, narrative physics
- `skills/seth-godin-ideavirus/` — virusworthiness, SVA, sneezer strategy

**Existing Editions** (for cross-edition trope audit):
- `_active/farrice-brand/content/substack-v2-drafts/` — all published editions
- `_active/farrice-brand/content/prompt-packs/` — all published prompt packs

**Strategy**:
- `_active/farrice-brand/content/substack-v2-strategy.md` — publication setup, growth tactics
- `research_outputs/substack-brandjack-trends-april-2026.md` — initial trending report

---

## Batch Mode (`--batch N`)

When producing multiple editions:
1. Run Phase 1 research ONCE, present all topics
2. Farrice selects N topics and gives raw takes for each
3. Draft all N editions, running cross-edition trope audit
4. Engineer N prompt packs
5. Generate N x 3 LinkedIn posts
6. Finalize all at once

This is the one-man-army mode. Research once, produce at scale.
