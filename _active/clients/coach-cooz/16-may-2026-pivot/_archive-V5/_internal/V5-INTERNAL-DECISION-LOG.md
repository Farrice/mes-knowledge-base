# V5 — INTERNAL DECISION LOG

## Internal-only · Farrice reference · The "why" behind every V5 decision
## NOT for Cooz — the audit trail stays here so the client-facing docs stay clean

---

## Major Decisions and Rationale

### Decision 1 — Archive ALL V4 work (V4-00 through V4-06 + 15/16/17 N1) plus all V2/V3 working files

**Why**: User feedback (verbatim): *"I can't give this to Cooz. It's not structured well enough. If he fed this to his AI for knowledge documents or references, that would be a problem."*

V4 was internally rigorous (deep research, customer voice mining, adversarial red-team, ship-5-hold-3 architecture) but externally unusable as a client handoff. Audit trail visible in every doc — HOLD banners, "Fix 2 applied" notes, V3-vs-V4 comparisons baked into copy. Cooz couldn't paste any of it into his AI as a knowledge document because the AI inherits the process confusion.

**Result**: All V4 + V2/V3 docs moved to `_archive-V4/` (29 files). V5 active surface is 4 client-facing docs + 4 internal docs only.

---

### Decision 2 — Use curated expert personas, NOT .claude/agents/ subagents

**Why**: User feedback (verbatim): *"we have been defaulting to our sub-agents, which are decent but not as good as our expert personas and expert agents that we have on file. I want us to divert from using those sub-agents so hard, because I feel like that's been part of the problem as to why we're getting subpar replies. I've had to do so much more editing than I've ever imagined lately."*

V4 had used master-copywriter, prose-doctor, adversarial-reviewer, expert-extractor, synthesis-engine, icp-deep-canvasser, competitive-intel as Agent-tool subagents. V5 used direct main-thread tooling instead.

**Personas loaded as Tier 2 thinking lenses**:
- Phase 1 (mechanism mining): Lara Acosta · Nicolas Cole · Sean Macintyre · Kallaway · April Dunford · Rory Sutherland
- Phase 1.5 (testimonial mining): Ron Lynch
- Phase 2 (Burbank engine): David McRaney · Chris Cimorelli · Sabri Suby · Daniel Priestley · Andrew Dun
- Phase 3 (content production): Lara Acosta · Nicolas Cole · Maria Wendt · Rory Sutherland · Kallaway · Sean Macintyre

**Research tooling**: Direct Perplexity research (3 batched competitive-mining queries + 1 Burbank channel query) — NO competitive-intel or deep-research subagent wrappers.

---

### Decision 3 — Competitive mining for STRUCTURAL MECHANISMS, not content templates

**Why**: User feedback (verbatim): *"I want us to actually mine competitors, not just because they're competitors, but for content that actually works on LinkedIn that we can position uniquely for him, with his angle and his perspective on how this offer is going to go. We don't want to get some copycats of things that work for you, the competitors, where he just joins the noise."*

V5 extracted underlying physics (mechanism-first opener · specific real-names+numbers · numbered framework · identity-shift closer · demonstration authority · story-led proof post) and tagged each with Cooz's UNIQUE-ANGLE REFRAME so he stands out as a different category instead of joining the noise.

**Test applied**: For each mechanism — "If a reader saw a competitor's post AND Cooz's post in the same scroll, what makes Cooz's read as a different category, not a copy?" If a mechanism failed that test, it was killed.

---

### Decision 4 — Drop the 3 female-buyer-mirror creators from the sampling list

**Why**: User feedback (verbatim): *"I don't want us to do any of this defense mode thing with Cooz being Burbank's local female trainer. We abandon that; we don't need that!"*

V5 sampled 7 creators: Daily Body Coach, Dan Go, Don Saladino, Andy Galpin, Bedros Keuilian, Mark Bell, Cody McBroom. Removed: Lacee Lazoff, Anne Marie Chaker, Hailey Barragan (their value was in female-buyer-voice surface — V5 doesn't need that).

**Result**: V5 sampling list aligned to Cooz's actual book — Hollywood vertical (Saladino), executive vertical (Daily Body Coach), evidence-based coach IP (McBroom — Cooz's actual mentor), elite strength (Bell, with Carron client analog), science authority (Galpin), high-frequency platform-cascade (Dan Go), and consistency-business mechanic (Keuilian).

---

### Decision 5 — Female-tactical positioning entirely killed

**V4 had**: B.2 female-tactical bridge ("You came back to a body you don't recognize"), female-pro lane in Burbank acquisition channels, female-coded landing copy.

**V5 has**: NONE of those. Brand positions Cooz directly as The Resurrection Coach for high-performing professionals — gender-neutral by virtue of who he actually serves. Female testimonials (Mari, Sam, Paige, Jessica, Patricia, Karima) live in the testimonial library as PROOF the work delivers, not as a separate positioning angle.

**Why**: Cooz is a male coach with a male coach's voice. Brand stands. Women hire him because the work is good, not because the marketing was engineered to make them feel addressed.

---

### Decision 6 — Mike (M.G., 9 yrs) is the V5 non-relational long-arc anchor

**V4-05 caught**: 7-year retention claim in headline rested on a single relational tie (Robin, Cooz's father). Skeptical prospect would notice and downgrade.

**V5 fix**: User-provided 18-testimonial doc revealed Mike has been with Cooz for 9 years — district manager 33 yrs at Ferguson Plumbing, recently fired Jan 2026. Plus Sammy (Mike's son) at 4+ yrs, Corey at 4 yrs, Carron at 3 yrs.

**Result**: V5 headline retention claim restored to **"9 years of practice. Long-arc clients I've kept for 4, 5, 8, 9 years."** Anchored by 5 named long-arc clients, only one relational. Solves the V4-05 hidden risk completely.

---

### Decision 7 — Brave Choice methodology surfaced as the proprietary frame

**V4 had**: Strategist-invented framings (Body-First OS, Substrate Rebuild, Executive System Architecture).

**V5 has**: Brave Choice methodology — Cooz's OWN naming, named verbatim by Robin ("Brave Choice methods"), already documented in `07-client-artifacts-pdfs/Coach Cooz-Online-brave_transformation_content_templates.pdf`.

**Why**: This is Cooz's actual proprietary frame. It's owned, not borrowed. It's verified by an 8-year client. It's already in his content templates PDF. V5 simply surfaces what was already there.

---

### Decision 8 — Voice register sourced from testimonials backstory + voice-calibration-real.md, NOT from Cooz's recent LinkedIn posts

**V4 had**: 17-N1-KNOWLEDGE-VOICE-SAMPLES.md sampled 10 verbatim Cooz LinkedIn posts that have zero engagement. We were teaching Gemini to pattern-match the voice that isn't working.

**V5 has**: V5-COOZ-TRUE-VOICE.md grounded in three sources:
1. The 18-testimonial backstory voice (the real Cooz writing about real clients in his actual register — specific, story-led, slightly self-deprecating, slightly funny)
2. `voice-calibration-real.md` (April 2026 — explicitly replaced the V3 jargon-era voice guide with Cooz's actual texts and natural-speech phrases)
3. Robin's testimonial verbatim ("Brave Choice methods") for proprietary methodology naming

**Why**: The testimonials backstory voice + the earlier-truer voice doc are the version of Cooz that hasn't been writing-for-LinkedIn-and-failing. That register is what V5 amplifies. The recent LinkedIn posts that get zero engagement are evidence of what's NOT working — sampled NOWHERE in V5.

---

### Decision 9 — Resurrection Fit gym (2503 N Ontario St, Burbank) flagged as coincidental brand-alignment partnership opportunity

**Discovery during Burbank channel research**: A gym at 2503 N Ontario St, Burbank is literally called "Resurrection Fit" (resurrection-fit.com). They explicitly market as designed for personal trainers who want operational autonomy with 100% profit retention (space-rental model, not employment).

**Why this matters**: The brand alignment is too good to ignore. Cooz is "The Resurrection Coach." Resurrection Fit is the gym structurally built for independent coaches. If the partnership lands, it becomes Cooz's physical hub + free brand reinforcement.

**V5 action**: Channel 3 of V5-BURBANK-ENGINE.md — Cooz emails them in Week 1.

---

### Decision 10 — Ship architecture: 4 client-facing + 4 internal-only

**Client-facing (Cooz reads these)**:
1. V5-COOZ-HANDOFF.md (master orientation, ~2,400 words)
2. V5-BURBANK-ENGINE.md (60-day in-person acquisition plan, ~2,800 words)
3. V5-LINKEDIN-CONTENT-SYSTEM.md (10 paste-ready posts + templates + calendar, ~3,800 words)
4. V5-NOTEBOOK-KNOWLEDGE.md (single Gemini Notebook 1 knowledge doc, ~2,400 words)

**Internal-only (Farrice reads these)**:
1. V5-COOZ-TRUE-VOICE.md (voice register triangulated from 3 sources)
2. V5-WINNING-MECHANISMS.md (6 durable mechanisms + Cooz's unique angle for each)
3. V5-TESTIMONIAL-LIBRARY.md (18 testimonials structured by avatar + use case)
4. V5-INTERNAL-DECISION-LOG.md (this file)

**Total V5 word count**: ~28,000 words across 8 docs. (V4 was ~140,000 words across 8 docs. V5 is 5x denser, more decisive, less audit-trailed.)

---

### Decision 11 — Killed V4 HOLD pieces entirely (didn't rebuild them in V5)

**V4-05 had flagged 3 HOLD pieces**: B.2 female-tactical bridge, Pathway A In-Person Burbank pitch (315-deadlift fabricated scene), Hero G "lost first long-term client at week 6" fabricated specifics.

**V5 resolution**:
- B.2 — KILLED (per Caveat 3, no defensive female-trainer positioning)
- Pathway A scene — REPLACED with Mike's 9-year executive arc as the load-bearing case study (V5 Post #4)
- Hero G week-6 scene — REPLACED with structurally similar Lane 2 confessional content built on Cooz's verified register (V5 Post #2)

**Why**: V5 doesn't relitigate V4. Where V4 had unverified specifics, V5 substitutes with verified testimonials. No HOLD banners visible to Cooz.

---

## V5 vs V4 Comparison (one table)

| Dimension | V4 | V5 |
|---|---|---|
| Composite quality score | 7.7/10 (with 3 HOLDs) | TBD via finalize |
| Total word count across docs | ~140,000 | ~28,000 |
| Client-facing docs | 7 (V4-00 through V4-06) | 4 (V5-COOZ-HANDOFF + V5-BURBANK-ENGINE + V5-LINKEDIN-CONTENT-SYSTEM + V5-NOTEBOOK-KNOWLEDGE) |
| Audit trail visible to client | YES (HOLD banners, "Fix 2 applied," V3 comparisons) | NO |
| Long-arc client anchors | 1 (Robin, relational) | 5 (Mike, Robin, Sammy, Corey, Carron — 4 non-relational) |
| Female-tactical positioning | Yes (B.2 on HOLD) | Killed entirely |
| Brand methodology naming | "Body-First OS" / "Substrate Rebuild" / strategist-invented | Brave Choice (Cooz's proprietary, Robin verbatim) |
| Sub-agent reliance | High (master-copywriter, prose-doctor, adversarial-reviewer, etc) | None — main-thread + expert-personas only |
| Voice anchor | Cooz's 10 underperforming LinkedIn posts | Testimonials-backstory voice + voice-calibration-real.md + Brave Choice templates PDF |
| In-person engine doc | None | V5-BURBANK-ENGINE.md (5-channel 60-day plan) |
| Competitive mining intent | Verify ICP | Extract structural mechanisms + reposition with unique angle |

---

## What V5 Bets On

The V5 plan rests on 5 testable assumptions. Each will be measured at the Week 4 checkpoint.

1. **The 5 long-arc clients (Mike, Robin, Corey, Sam, Carron) will produce 6-12 warm intros if asked.** Highest-leverage assumption. If false, Channel 1 collapses.

2. **Resurrection Fit (the Burbank gym with the brand-aligned name) is willing to discuss an independent-trainer partnership.** Coincidence is too perfect to not test. If they're hostile or already saturated with trainers, Channel 3 reduces to standard gym membership at Crunch or Equinox.

3. **The testimonials-backstory voice + Brave Choice methodology actually performs better on LinkedIn than the V3/V4 strategist register.** Will measure via engagement rate per post over 4 weeks. Target: ≥3% (currently ~0%).

4. **Hollywood production network is reachable through Buzz/Corey/Sam without paid sponsorship.** If insular industry circles reject cold-introduction warm-introductions despite client referrals, Channel 2 reduces to long-tail GBP visibility.

5. **A 28-day paid trial offer at $97-$197 converts at 5-15% to ongoing $1,275-1,500/mo coaching.** Optional Channel 5 (paid ads) test starts Week 5+. If conversion below 5%, kill the paid funnel.

---

## What's Missing / Future V6 Watch

1. **The Resurrection Series podcast** as distribution layer. V5 noted it as "secondary engine future" but didn't build a podcast plan. Worth a V6 phase if podcast guesting in Weeks 3-4 surfaces interest.

2. **Substack / newsletter** as owned-audience layer. Daily Body Coach + Dan Go both use newsletters as bypass-algorithm distribution. Worth piloting in Q3 2026 once LinkedIn engine is producing baseline reach.

3. **Notion + Daily Body Coach-style cold outreach at scale.** $10K/month case study from lemlist. Premature for V5 (lock the warm-referral engine first) but worth Q4 2026 as growth layer.

4. **Brand visual system update.** V4 had 18-N2-VISUAL-GENERATOR-SETUP, 19-N2-NANO-BANANA-PACK, 20-N2-VISUAL-BRAND-LANGUAGE archived to _archive-V4. V5 deferred visual brand work. Worth revisiting once content engine has 30 days of post performance data — visual system should be informed by what's working textually.

5. **Brian's case study production.** Mentioned in V3 archive as "in production." Status unknown for V5. If Brian's transformation is shippable, that becomes Lane 3 case study #4 + reduces dependency on single hero (Mike).

---

## ONE SENTENCE

V5 strips V4 to its load-bearing truths (Cooz's testimonials-backstory voice + 5 long-arc client anchors + Brave Choice methodology + Resurrection brand) and builds 4 clean client-facing docs and 4 internal-only docs that respect Cooz's actual position — male coach, in-person Burbank primary, online secondary, no defensive positioning, structural mechanisms uniquely repositioned, expert personas as thinking lenses instead of subagents.
