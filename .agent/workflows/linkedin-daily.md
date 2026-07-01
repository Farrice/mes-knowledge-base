---
description: Daily LinkedIn zeitgeist + brandjack engine (Parallax-modeled) — research → opportunity menu + raw-take priming → cook 3 variants → gate
---

# /linkedin-daily — LinkedIn Domination OS: Daily Engine (v2 — Parallax-modeled)

The daily operating loop for Farrice's LinkedIn launch. This is a **co-pilot, not a content cannon.** v1 auto-picked an angle and auto-drafted — which produced competent, polished, *flat* posts (the failure mode Farrice named on 2026-06-15: "dry, void of tension, sterile, all the AI tropes"). v2 is modeled on what `/parallax` does right: surface a menu of brandjack/newsjack opportunities, **prime Farrice's brain with talking points + raw-take questions, get his real perspective, THEN cook** — so his narrative and storytelling are *in* the piece, not approximated around it.

This workflow IS the metaprompt. Identity, voice, ICP, and hook mechanics come from live source files (Step 1), never a pasted profile paragraph.

## Usage

```
/linkedin-daily                  # full loop: research → opportunity menu → HALT for raw take → cook 3 variants
/linkedin-daily --auto           # no halt: generate a raw-take starter for the top opportunity, cook anyway (lower ceiling — use when Farrice is away)
/linkedin-daily --topic "X"      # skip research; Farrice already has the moment; go straight to priming + cook
/linkedin-daily --no-post        # briefing + opportunity menu + commenting plan only (no cook)
/linkedin-daily --posts N        # override variant count (default 3, Parallax 3-variant rule)
```

**Cost ceiling per run: $0.10.** tavily/WebSearch primary ($0). One Perplexity call max (≤$0.25) only if free search is thin — note it in the Cost Ledger.

---

## The Spine (what makes output alive, not sterile)

Every post descends into **specificity** instead of climbing the abstraction ladder. The sterile shape is *claim → citation → generic question* (the reader watches from outside). The Parallax shape is *specific moment → tension held → confession pivot → embodied metaphor → the insight arrives through recognition → declaration/image close*. The reader is the protagonist; Farrice enters as the voice naming what they already feel. See the loaded craft brief (Step 1) for the live mechanics with real exemplars.

---

## Steps

### 0. Init
- Resolve today's date → output `_active/linkedin-launch/06-automation/daily/briefing-YYYY-MM-DD.md`; create `daily/` if missing. Parse flags.

### 1. Context Load (non-negotiable — this is what makes the output Farrice's)

Read ALL of:

| File | Supplies |
|---|---|
| `_active/farrice-brand/CLAUDE.md` | Voice rules — banned MOVES, required moves, anti-patterns (SOURCE OF TRUTH). "Structurally sound but flat = 5/10." |
| `_active/farrice-brand/thought-bank/pov-anchors.md` | POV anchors (no-cheap-question-closes, private-language rule) |
| `FARRICE.md` | Interest stack, tribal vocabulary, avatar, 80/20 + Inclusion Insurance + Revelation Sequence |
| `_active/linkedin-launch/04-content-os/CONTENT-OS.md` | Pillars, lanes, rotation, barbell, 90-day arc, distribution motion |
| `_active/linkedin-launch/04-content-os/voice-gate.md` | Pass/fail gate run before any draft ships |
| `_active/linkedin-launch/01-research/deep-icp-profile-invisible-expert.md` | ICP beliefs / identity-resistance / Bridge Message |
| `knowledge/synthesis/the-persuasion-stack.md` | Single Truth → Mechanism → Matched Proof → Identity Dissolution |
| `_active/linkedin-launch/06-automation/daily/performance-log.md` | Last 7 entries + Carry-Forward Directives |
| Yesterday's `daily/briefing-*.md` + most recent post set | Continuity; never repeat an angle, hook format, or close structure within 7 days |

**Voice + cognitive-signature layer (load the depth — this is the antidote to flat AND what makes it world-class):**
- `skills/fresh-voice-system/genius.md` — **THE depth engine.** Load the **Cognitive Signature** (Paradox Reveal → False-Frame Demolition → Reframe Landing = the "Goddamn That's True" sequence), the "value is the new generic / story-first, insight-second" principle, and the **AI-stigma reframe** (lead with the transformation + brand truth, never tool-talk).
- Parallax exemplars (live voice texture): `_active/farrice-brand/content/linkedin-posts/parallax-launch-week/`, `.../2026-05-05-jj-manipulation-variants.md` (9/10), `.../substack-v2-drafts/02-anti-hustle.md` + `03-filter-babel.md`. Extract: scene-first openings, confession pivot, embodied metaphors (performance/training/gaming — never abstract), varied rhythm, recognition closes.
- Aha layer: invoke `aha-engine` / `kobi-brown` (cognitive-change architecture) so the cook targets a real perception shift, not information.
- **Empathy + brand-intel layer (front-and-center, every run):** `_active/linkedin-launch/01-research/icp-emotional-map.md` — the ICP's **broken promises**, the **2am replaceability fear**, the **daily lived life**, and the rule *reassure the human, indict the machine*; plus the latest `daily/brand-radar-*.md` (named-brand specifics for narrative/tension/authority) and `_active/linkedin-launch/00-start-here/CREATIVE-BOOK.md` (the operating frame). If no current Brand Radar exists, run `/farrice-engine radar` first.

Chain Step 4 compliance (content domain — ≥2 skill files per `directives/content_creation_gate.md`):
- `skills/diandra-escobar-linkedin-growth/references/hook-format-library.md` (REAL hook ceilings) + `hook-writing-rules.md`
- `skills/linkedin-2026-format-arbitrage/SKILL.md` (360 Brew / sequential-recommender depth physics)
- `python3 execution/memory_retrieve.py "linkedin daily post <today's lane/moment>" --top 10`
- Recall grounding: `mcp__recall__search` on today's moment (silent skip if <2 cards)
- Narrative cook → optionally load `skills/nicolas-cole-newsletter-flywheel/` (sentence craft) + `skills/shaan-puri-storytelling/` (cultural pulse) when brandjacking, per the `/parallax` default stack.

### 2. Feedback Ratchet
1. Read `performance-log.md`. For posts >24h missing metrics, ask Farrice for: impressions, **out-of-network %**, comments, profile views (+ saves if visible). Manual, 30 sec. No numbers → mark `pending`, never invent.
2. Append metrics.
3. Derive 1-3 **Carry-Forward Directives** (e.g., "confession-pivot posts drive profile views — keep"; "Lane A authority outperforming reach 2:1 this week"). Today's choices honor active directives.

### 3. Research Sprint (receipts or it didn't happen)

**Research layer = Apify-first, deterministic fallback** (per `directives/apify-usage-policy.md`; Apify is budgeted/green and self-governs — never blocks): use `python3 execution/apify_client.py {instagram|reddit|web} ...` for RAW data the web can't reach — brand IG content + winning formats, Reddit sentiment/pain in the vertical, JS-rendered brand/career pages. The wrapper returns `{"fallback": true}` on budget exhaustion → reroute to `execution/research.py` → Perplexity → tavily/WebSearch. **Always report which tool produced each finding.** Run free web search for everything else. Two tracks:

**Track A — Zeitgeist & platform:**
| # | Query | Feeds |
|---|---|---|
| R1 | `LinkedIn algorithm OR reach OR format update <month year>` | Algorithm & Format Watch |
| R2 | `AI hype backlash OR "AI slop" OR AI replacing creatives <this week>` | AI-Discourse Narrative Map |
| R3 | `solopreneur OR creator economy OR consultant trend <month year>` | ICP-world Pulse |

**Track B — Industry (marketing / copywriting / creative strategy — for authority-jacking):**
| # | Query | Feeds |
|---|---|---|
| R4 | `big brand OR agency AI campaign OR restructure <month year>` (named: WPP, Publicis, Omnicom, Coca-Cola, Nike, Meta ad AI) | Industry Watch (brand moves) |
| R5 | `AI marketing failure OR backlash OR copywriters/agencies layoffs <recent>` | Industry Watch (failures + practitioner pain) |
| R6 | `creative strategy AI taste craft commoditization <recent>` (Ad Age, Campaign, Digiday, The Drum) | Industry Watch (insider discourse) |

Capture per kept claim: **source URL + date + one-line quote**. Discard undated / >60 days unless explicit background.

### 4. Verification Pass (Chain 5.5 — kills the fabricated-citation failure)
Claim inventory → label **VERIFIED** (2+ independent or primary) / **LIKELY** (1 credible) / **UNCONFIRMED**. Named brands/people/figures = MUST verify (Parallax Phase 2.5 rigor). UNCONFIRMED may appear in the briefing WITH label, never in a post. Algorithm + precise-stat claims get extra skepticism (distinguish "announced" / "creators report" / "one guru claims"). No receipt = does not ship.

### 5. The Creative Daily Brief (Parallax-grade — a creative partner, not a topic menu)

Hand Farrice a full creative brief so he brings only his raw take. Open with the **macro layer**, then the opportunities. No stitching — this is the heart of the daily run.

**A. The Players** — who/what is moving today (named, from Brand Radar + research + zeitgeist): which Top-10 brands posted/launched/stumbled, what the category is doing, what the AI-discourse is doing.

**B. The Themes** — the 2-3 recurring creative themes available today (e.g., sameness/divergence, the replaceability fear, taste-as-moat, the compliance gate, founder-truth).

**C. The Emotional Target** (from `icp-emotional-map.md`) — what the decision-maker FEELS right now, the **emotion to evoke** (recognition / validated taste / earned hope), and the front-and-center triad: a **broken promise** to name, a **deepest problem** to speak to, a **daily-life** moment to anchor in. Rule: *reassure the human, indict the machine.*

**D. The Full Breakout** — how to turn today's material into great content: the structural move (which Cognitive Signature beats), the named specifics to weave in, the "say it better than they can" line to aim for.

Then build **3-5 opportunities** Farrice can borrow attention from — the asset he loves; it primes his brain so his narrative + contrarian POV come out naturally. For EACH:

```
### OPPORTUNITY N: [punchy name]
**The moment** (receipt): [what happened] — [URL] — [date] — [VERIFIED/LIKELY]
**Why it's hot right now**: [the attention there is to borrow, 1-2 lines]
**Jack type**: Newsjack / Brandjack / Authority-jack / Trendjack
**The angle only you can take**: [Farrice's practitioner-depth wedge — the read no basher or bro can give]
**Emotion to evoke + what they feel**: [the target emotion + the ICP's underlying feeling from `icp-emotional-map.md` — the broken promise / fear / daily-life moment this touches]
**Pillar/Lane fit**: [P1-P4 / Lane A or B]
**Prime your brain (raw-take questions — answer ANY in a voice note / bullets)**:
  1. [experiential — recall a specific MOMENT, not a category]
  2. [opinion/contrarian — what do you actually think nobody's saying?]
  3. [stakes/contrast — who gets hurt, who wins, what's the cost]
  4. [emotional — what does the reader feel at 11pm about this, and what would let them feel SEEN?]
**Talking-point kindling** (NOT finished copy — sparks): [2-3 sharp fragments/angles]
```

**HALT (default mode): present the menu, wait for Farrice's raw take** — which opportunity, plus his stream-of-consciousness perspective (voice note, bullets, a single strong sentence — all valid). The raw take is the soul of the cook; capture his exact phrases, rhythm, and imperfections verbatim.

**`--auto` mode only:** pick the top opportunity by zeitgeist heat × pillar fit, generate a 4-6 line "raw-take starter" in Farrice's documented voice/POV from FARRICE.md + pov-anchors, label it clearly as AI-inferred, and proceed — flagging that the ceiling is lower without his real take.

### 6. Compose Briefing → `daily/briefing-YYYY-MM-DD.md`

```markdown
# LinkedIn Daily Briefing — YYYY-MM-DD

## 1. Zeitgeist Pulse        [3-5 bullets, receipt + label inline]
## 2. Algorithm & Format Watch   [verifiable shifts; saturated vs pattern-breaking formats]
## 3. AI-Discourse Narrative Map   [feed believes / actually true / Farrice's wedge]
## 4. Industry Watch (marketing · copy · creative strategy)
   - **Big brands & AI**: [named, dated moves — WPP, Coca-Cola, Meta, etc.]
   - **Failures & practitioner pain**: [the human cost, receipted]
   - **Insider discourse**: [the smart-room argument + the contrarian wedge]
## 5. Brandjack / Newsjack Opportunity Menu   [3-5, full priming format from Step 5]
## 6. Today's Assignment   [lane/pillar/bucket/density per barbell; hook + close format honoring variance + Carry-Forward]
## 7. Draft Variants   [the cook — Step 7; paste-ready, zero commentary inside the block]
## 8. Distribution Plan   [10 comment targets carrying the day's wedge; 15-min reply window]
## 9. Cost & Receipts Ledger   [searches, $ spent, every receipt URL + label]
```

### 7. The Cook — Parallax 3-Variant Production (skip on --no-post)

**Default: 3 complete variants, each a different COOKING METHOD** (Parallax 3-variant rule — never one draft presented as the draft). Three full posts that feel written by three versions of Farrice, not one post three ways. Pick the three contrasts that fit today's moment:

| | Variant A | Variant B | Variant C |
|---|---|---|---|
| Cook | Confessional / memoir-pivot | Observational / pattern-spotting | Framework / contrarian POV |
| Opening | Scene, emotional anchor | Specific artifact / news moment | First-person ritual or a teaching scene |
| Lens | The coach / parent | The strategist | The contrarian who teaches a lens |
| Close | Recognition / bookend | Declaration / zoom-to-pattern | Hand-the-reader-a-tool |

For EACH variant, build through the **Persuasion Stack** carrying Farrice's raw take as the spine, threaded on the **Cognitive Signature** (this is the intellectual engine of the depth — `fresh-voice-system/genius.md`):
- **Paradox Reveal** → name the hidden contradiction where a strength IS the weakness ("a tool that could make you unmistakable, and you used it to disappear into the average").
- **False-Frame Demolition** → take the thing "everyone says" and expose its broken premise with an absurd-but-exact analogy.
- **Reframe Landing** → replace it with a deeper lens that changes how the reader sees the whole problem — the "Goddamn That's True" moment. (Not every short post needs all three; the full sequence is the strongest version.)

Layered through the build:
1. **Single truth** (one sentence — write it first). Make it a Stanton **premise-sentence**: character + conflict + conclusion (`/stanton-premise-sentence`), held as the litmus every line is audited against — a true sentence the post *proves*, not a topic it covers.
2. **Scene-first open** — a specific moment with sensory/physical detail; hold tension 1-2 beats before naming the point. Weave the verified brandjack receipt in as the artifact, never as a lead citation. Story first, insight second.
3. **Confession pivot** — drop Farrice's lived stake (his raw take, his 18 years, his actual practice) so the universal arrives through the specific.
4. **Embodied metaphor** — from his domains (coaching, training, gaming, parenting, behavior change). Max 1 corrective-exercise metaphor per post; never the hook two posts running; never abstract.
5. **Matched proof** — one telling specific; experiential proof when no real number exists; every real-world claim VERIFIED/LIKELY.
6. **Recognition close** — image / declaration / bookend / concrete future / naming what they feel. NEVER a transferable question.

**Hook** (when the variant uses a discrete hook): 3 candidates in 2+ formats from `hook-format-library.md`, char-counted against REAL ceilings (Dense 140-160 no breaks · Punchy ≤50/≤50 · Bomb ≤50 · Stacked ≤60/line · 210 max · no questions · no em dashes · never fabricate numbers).

### 8. Voice Gate + Mechanical Audit (pass/fail — fail = REGENERATE the section, never patch)

Run `_active/linkedin-launch/04-content-os/voice-gate.md` top to bottom, PLUS the Parallax mechanical checks:
- **The Aha gate (the apex bar — fail if it only informs).** Name the specific perception shift the piece creates: the reader's belief BEFORE → the belief AFTER. If you can't name a real before/after, it's information, not transformation — regenerate. Confirm the Cognitive Signature is doing work (at least a Reframe Landing). The standard: a reader is *left better off* and would come back (addictive-in-a-good-way), not just nodding.
- **The Empathy gate (the trust/authority engine — fail if it doesn't make them feel seen).** Does the piece articulate the ICP's truth/worldview/problem **better than they could themselves** ("he gets it better than my own team")? Name the broken-promise / deepest-problem / daily-life moment it touches (`icp-emotional-map.md`). Enforce *reassure the human, indict the machine* — flag any line that shames or makes the decision-maker feel MORE replaceable. If it only informs or impresses, it fails.
- **"Polished but flat" is a FAIL, not a pass.** Each piece must have a beating center (a real moment, a real stake) — not just clean sentences.
- **Stanton clamp-audit (line-to-line pull) — `/stanton-clamp-audit`.** Walk each variant beat by beat: does every line make the reader want the next? Mark the first glance-up line and re-clamp it (open a debt, withhold the outcome, inject a change, or cut exposition). On LinkedIn the unclamp tolerance is near zero — one flat line and they scroll. The last line stays open so the reader finishes it, never a tidy bow.
- Zero banned MOVES: "It's not X. It's Y." negate-then-reveal (check load-bearing lines hardest — it hides there), twin-sentence aphoristic endings, triple-beat anaphora, "Here's what/why" + "here is the part nobody" openers, mic-drop deflation, cheap/transferable question close (paste test).
- ≤2 em dashes per piece (0 in hooks); no filler (actually, just, very, really, basically, literally, honestly).
- **Cross-variant + cross-window variance**: the 3 variants share no opening move, close structure, or central metaphor; none collides with the last 7 days of posts.
- Hook within its declared ceiling (count it, show the count).
- **Private-language test**: ≥1 line only Farrice could write per variant; rewrite any load-bearing line a generic creator could have written.
- Independent pass recommended: dispatch `prose-doctor` (voice/tells) + `fact-verifier` (named claims) before delivery.

### 9. Ship Package
- Embed final variants in briefing §7; append a `drafted` row per shipped variant to `performance-log.md` (date, pillar, lane, bucket, cook method, hook/close, density, metrics=pending).
- Print Farrice's 3-line to-do: publish + 15-min reply window · run §8 commenting plan · drop yesterday's numbers next run.

### 10. Finalize (Chain Step 6)
```bash
python3 execution/chain_runner.py finalize "LinkedIn daily — YYYY-MM-DD [moment]" \
    --expert nicolas-cole --skill nicolas-cole-newsletter-flywheel --workflow linkedin-daily \
    --type Content --intent [1-10] --expert-score [1-10] --adversarial [1-10] --sub-agents [measured] \
    --notes "[what worked] | Factual Grounding: [1-10] | Verification: [PASS/PARTIAL]"
```
Factual Grounding veto: scored <6 = re-verify before delivery.

---

## Error Handling
- **Research thin**: ship fewer, truer opportunities + a note. Never pad with training-memory "trends."
- **Farrice gives no raw take (and not --auto)**: present the menu and HALT; the engine is a co-pilot — without his take the cook caps at competent-but-flat (the exact thing we're fixing).
- **No metrics 3+ days**: flag in §6; the ratchet is the learning loop.
- **Hook/variant fails the gate twice**: drop the angle, new cook on a different opportunity (Rewrite Before Relabel).

## Output Files
```
_active/linkedin-launch/06-automation/daily/briefing-YYYY-MM-DD.md     # daily deliverable (incl. opportunity menu + variants)
_active/linkedin-launch/06-automation/daily/performance-log.md          # rolling ratchet (append)
```
