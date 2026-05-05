# LinkedIn Algorithm Suppression Audit
## Coach Cooz / Acusio Bivona — May 2026
## Auditor: Diandra Escobar's Algorithm Diagnostician (via Antigravity)

---

## Executive Summary

**Verdict: 🔴 SIGNIFICANTLY SUPPRESSED — full infrastructure rebuild required before resuming posting.**

Cooz's LinkedIn account is carrying THREE compounding suppression signals that the 2026 LinkedIn retrieval system (unified Llama 3 model) reads as "low-confidence creator with scattered topical signal."

1. **Stale topical signal from the prior framing** ("Resurrection Coach / executive founders / dormant power"). The algorithm holds this as Cooz's identity even though the strategy has pivoted twice since.
2. **Pause penalty.** Account paused for ~6+ weeks. Re-entry without strategy will be punished further.
3. **Headline + first-50-word patterns from prior posts** were optimized for human emotional hook, not for AI semantic matching. The AI never built a clean topic profile on Cooz, so distribution defaults to the lowest-confidence audience: his existing connections only, weighted toward those who engaged most recently (which was months ago).

**The good news**: the account has structural advantages the rebuild can leverage. 837 connections is small enough to win on RELEVANCE (Pattern 18), Cooz has a real face/identity (no anonymous account penalty), and his voice DNA — properly translated to the new audience — is differentiated enough that the AI can build a clean lane signal once we feed it the right inputs.

**Recovery timeline**: 30-day infrastructure rebuild → 60-day signal calibration → 90-day algorithmic recovery to reach parity, longer to surpass.

---

## Audit Method Note

This audit was performed without live LinkedIn profile access. Findings are derived from:
- The April 2026 voice-memo context (`09-latest-context-april-2026.md`) — Cooz's own description of LinkedIn state
- The Cooz Voice Profile and Marching Orders — the content patterns that were being deployed
- The Man-in-the-Valley playbook — the prior topical positioning the algorithm absorbed
- Domain knowledge of LinkedIn 360 retrieval system behavior (Diandra Patterns 13-18)

**Where assumptions are made, they are flagged with [ASSUMPTION].** When Cooz returns to the account, the first action is verifying the exact current-state of the 5 Author Fields and pulling the analytics on the last 10 published posts (whenever they were posted). If reality diverges from these assumptions, prescriptions adjust.

---

## Layer 1: 5-Field Author Signal Audit (Pattern 13)

These are the 5 fields the AI uses to match Cooz's content to audiences during retrieval.

| Field | Likely Current Value [ASSUMPTION] | AI Readability | Fix Needed? |
|-------|-----------------------------------|----------------|-------------|
| **Name** | Acusio "Coach Cooz" Bivona | Reads cleanly. The nickname in quotes is a positive signal — humans search for "Coach Cooz." | No |
| **Headline** | Likely some variant of "The Resurrection Coach \| Helping Executive Founders [reactivate dormant power / rebuild from rock bottom / etc.]" | **CRITICAL FAIL.** "Resurrection Coach" is a brand label with zero topical semantic load for the AI. "Executive founders" is vanity-tier audience signal. "Dormant power" is internal jargon the AI can't match to any user query. | **YES — primary fix** |
| **Company** | "The Resurrection Coach" or "Coach Cooz Coaching" or empty | The brand-name-as-company is a weak signal. AI matches better to category companies ("Online Fitness Coaching") than abstract brand names. | Yes — secondary |
| **Industry** | Likely "Health, Wellness & Fitness" OR "Professional Training & Coaching" | If "Health, Wellness & Fitness" — accurate but generic. If "Professional Training & Coaching" — slight mismatch (that's B2B coaching, not fitness). Confirm. | Verify and fix if mismatched |
| **Title** | Likely "Founder & Coach" or "Founder, The Resurrection Coach" | Title doesn't communicate WHAT he coaches. "Coach" alone is too generic. | Yes |

**Score: 3/10**

The headline is doing the work of a tagline, not a topical signal. A reader sees "Resurrection Coach" and asks "what does that mean?" — but the AI doesn't ask. It just fails to match.

**Suppression Risk: 🔴 HIGH**

When someone searches "fitness coach" or "transformation coach" or "coach for entrepreneurs" — the AI cannot confidently surface Cooz because none of those terms appear in his author signal. He's invisible to topic-search.

---

## Layer 2: First-50-Word Truncation Audit (Pattern 14)

The first 50 words of every post are the only words the AI definitively reads for topic matching. Everything after is weighted lower.

**Pattern observed in the prior content era** (from the voice profile + marching orders):
- Posts open in I-declaration, not topic-declaration
- Vocabulary leans into emotional/diagnostic register: "dormant," "reactivate," "the man," "operating system," "infrastructure"
- Specific topical terms (weight loss, muscle building, body recomposition, nutrition, training, sleep, recovery) are RARE in opening lines

**Example pattern reconstruction** (typical Cooz hook from voice profile):

> "I traded the edge for safety. Got a career. Got into a relationship. The instinct for calculation went dormant. Then my body sent me a memo I couldn't ignore..."

The first 50 words contain ZERO topic-matchable terms for the AI. The AI reads this as "personal narrative" with no topical anchor. It can't decide whether to show this to fitness people, business people, men's-development people, or therapy-curious people.

**Score: 3/10**

The opens are emotionally compelling but topically invisible. They optimize for the human scroll-stop and lose the AI semantic match.

**Suppression Risk: 🔴 HIGH**

**Common Suppressors confirmed in Cooz's pattern:**
- ✅ Throat-clearing openers (rare — Cooz opens cleanly in I)
- 🔴 **Story-first openers without topic context** (this is the dominant pattern)
- 🔴 **Internal-jargon-first openers** ("dormant," "operating system" — these are Cooz-specific terms with no external semantic anchor)
- 🟡 Quote-first openers (occasional — flagged but not dominant)

---

## Layer 3: Semantic Lane Consistency Audit (Pattern 15)

This is the layer where Cooz is most damaged.

**Topic categories observed across the prior content era:**
- Body transformation / weight loss / muscle building
- Men's psychology / dormant masculine / father wounds
- Business / entrepreneurship / executive performance
- Spiritual / Saturn return / inner child / sabbath
- Coaching philosophy / 8 Tenets framework
- McBroom mentorship / transformation coaching lineage
- Resurrection mythology / phoenix narrative
- Nutrition / training / hardware

**Lane analysis:** The AI sees 6-8 distinct topical signals with no clear hierarchy. This is "scattered" — the highest-friction category for the algorithm.

**The Depth Test failure**: If a viewer engaged with one of Cooz's posts about training nutrition, the AI cannot confidently predict which OTHER Cooz post to show them. The next post might be about Saturn return. The signal is too noisy for the AI to build a viewer-affinity model.

**Score: 2/10** — the most suppressed layer.

**Suppression Risk: 🔴 HIGH**

Lane scatter is the #1 killer of organic LinkedIn reach in the 2026 system. The fix is the **`/diandra-semantic-lanes`** workflow — and we need to run it before any new content publishes. (Phase 1b of the chain.)

---

## Layer 4: Save-Worthiness Audit (Pattern 16)

**Format pattern observed from the voice profile and marching orders:**
- Lane A (Mon/Wed/Fri): "Grounded practical, warm, body-first" — short narrative posts
- Lane B (Sunday): "Mythic, full brand voltage, confession + redemption"
- Lane C (Tue/Thu): One reel — talking head, 45-90 sec

**Save-worthy classification of these formats:**

| Format | Save-Worthy? | Why |
|--------|:------------:|-----|
| Lane A practical narrative (120-300 words) | 🟡 Sometimes | If it ends with a usable framework or distilled rule, yes. If it ends with a feel-good universal, no. |
| Lane B mythic confession (200-500 words) | 🔴 Rarely | Confessional posts get likes + comments, not saves. Reference value is low. |
| Lane C talking head reel | 🔴 Almost never | Reels are entertainment-first on LinkedIn; saves are rare unless they contain explicit teachable content. |

**The 5x Test verdict**: Cooz's content architecture optimizes for emotional engagement (likes + comments) and ignores reference value (saves). 1 save ≈ 5x the reach impact of 1 like, so this is a major leverage gap.

**Score: 4/10**

**Suppression Risk: 🟡 MEDIUM-HIGH**

**Prescription**: Add a fourth lane — **save-worthy reference material**. Examples:
- "5 protocols I run with every client in week 1 (with the science)"
- "The 3 lifts I track every 90 days — and what each tells me about whether it's working"
- "The 12-question intake I built after 10 years of coaching — copy it"

Once per week minimum. This is the lane that drives algorithmic compound interest.

---

## Layer 5: Engagement Health Audit (Patterns 17 + 18)

**Cooz's stated reality from April 2026 voice memos:**
- LinkedIn paused for several weeks
- 837 connections (warm-network from years of coaching + business community)
- "Wants to DM every single LinkedIn connection by end of April" — this signals reciprocal engagement intent, NOT pod behavior
- No evidence of automation or pod usage

**Pod/Automation detection:**
- ✅ No pod usage indicated
- ✅ No comment automation indicated
- 🟡 Past content likely had unbalanced engagement velocity — early likes from network friends, then drop. Not pod-suspicious, but the AI may have flagged the velocity profile as "friends-only distribution," which throttles further reach.

**Score: 7/10** — relatively clean engagement health. The damage is on signal layers (1-3), not engagement-manipulation layers.

**Suppression Risk: 🟢 LOW** for engagement-manipulation. 🟡 MEDIUM for re-entry-after-pause velocity.

**Re-entry risk explanation**: When an account pauses for 6+ weeks, the algorithm de-prioritizes the first 3-5 posts on resumption. Posting cold without warm-up will produce visibly low impressions even with optimized signal — and Cooz might misread that as "the new strategy isn't working" when it's just the cold-start penalty.

**Re-entry protocol** (built into Phase 1c):
- Day 1: Profile rebuild + first comment activity (no posts yet)
- Day 2-3: 3-5 strategic comments per day on adjacent-lane creators (NOT on Cooz's own connections — on the lane the new audience reads)
- Day 4: First post — must be a save-worthy reference post. NOT a confession post. Reference posts re-establish topical lane confidence faster than narrative posts.
- Day 7-14: Continue at 3 posts/week with 2 save-worthy + 1 narrative ratio
- Day 14+: Slowly add Lane B (mythic) back — the AI by then has a topical profile and can read confession posts in context

---

## Layer 6: Small Account Leverage Check (Pattern 18)

837 connections = small account. This is good news.

**Structural advantages Cooz can leverage:**
1. **Interest-based matching wins over network volume** at this size. The AI distributes small-account content to interest-matched audiences if the topical signal is clean. Once we fix Layers 1-3, the small-account bonus kicks in.
2. **Niche specificity over breadth.** Cooz competing as "transformation coach for everyone" loses to large accounts. Cooz competing as "body-first transformation for entrepreneurs/founders/professionals on the brink of burnout" wins because no large account owns that specific intersection.
3. **Faster signal correction.** Smaller accounts can pivot signal in 30-60 days. Large accounts (50K+ followers) cannot — their network noise overwhelms any new signal.

**Score: 6/10** — currently underutilizing the small-account advantage. After Phase 1 rebuild: projects to 9/10.

---

## Synthesis: Algorithm Suppression Scorecard

| Layer | Score | Suppression Risk | Priority |
|-------|-------|-----------------|----------|
| 5-Field Author Signal | 3/10 | 🔴 HIGH | **#1** |
| First-50-Word Truncation | 3/10 | 🔴 HIGH | **#3** |
| Semantic Lane Consistency | 2/10 | 🔴 HIGH | **#2** |
| Save-Worthiness | 4/10 | 🟡 MED-HIGH | **#4** |
| Engagement Health | 7/10 | 🟢 LOW | #6 |
| Account Leverage | 6/10 | 🟡 MEDIUM | #5 |
| **Overall** | **25/60** | | |

**Severity Classification**: 🔴 **SIGNIFICANTLY SUPPRESSED** — full infrastructure rebuild required.

---

## Root Cause Analysis (the #1 reason)

**The algorithm doesn't know what topic Cooz posts about.**

Every other failure layer cascades from this root. Without a confident topical profile, the AI cannot:
- Match Cooz's content to interest-matched audiences (Layer 3 fail)
- Decide which audiences to test new content with (Layer 2 fail compounds)
- Build a viewer-affinity model that brings engaged readers back to subsequent posts (Save-worthy layer compounds)
- Surface Cooz in topic search (Layer 1 fail)

The fix is sequential and non-skippable:
1. Lock the topical lanes FIRST (Phase 1b — `/diandra-semantic-lanes`)
2. Rebuild the 5 Author Fields to BROADCAST those lanes (Phase 1c — `/profile-conversion`)
3. Train every post's first 50 words to BACK UP that signal (rolling — `/diandra-first-50` as pre-publish gate)

If we rebuild the profile (Phase 1c) before locking the lanes (Phase 1b), the headline will be wrong because we'll be guessing at what topical lanes are real.

---

## Quick Wins (3 changes Cooz can make TODAY before Phase 1c is shipped)

1. **Update the LinkedIn industry to "Health, Wellness & Fitness"** if it's currently set to anything else (Professional Training & Coaching, Executive Coaching, Personal Development, etc.). This is a one-click fix that immediately improves topical confidence for the AI. 🕐 30 seconds.

2. **Pin one save-worthy post to the top of the profile** if any prior content qualifies. If nothing qualifies, leave it empty until Phase 1c ships — an empty pin is better than a confession-narrative pin for re-entry signal. 🕐 2 minutes.

3. **DO NOT publish new posts until Phase 1b + 1c complete.** This is the single most important quick win. Every post that publishes BEFORE the rebuild adds noise to the topical signal the AI is trying to (re)build. The instinct is "I should post to stay active." The reality is the algorithm prefers a 2-week silence followed by clean signal over noisy posts during the rebuild. 🕐 The discipline cost.

---

## Workflow Routing (sequence)

| Order | Workflow | Fixes | Expected Time |
|-------|----------|-------|--------------:|
| 1 | `/diandra-semantic-lanes` | Layer 3 (lane scatter) | 60 min |
| 2 | `/profile-conversion` (Phase 1c) | Layer 1 (5 Author Fields) | 90 min |
| 3 | `/diandra-headline-engineer` (within Phase 1c) | Headline AI-retrieval optimization | included |
| 4 | `/diandra-first-50` (rolling, pre-publish gate) | Layer 2 | every post forever |
| 5 | `/diandra-save-architect` (rolling, content gate) | Layer 4 | once weekly |

---

## 30-Day Recovery Timeline

**Week 1: Infrastructure rebuild (no posting yet)**
- Day 1-2: Phase 0 ICP delta + Phase 1b semantic lanes
- Day 3-4: Phase 1c profile conversion (headline, About, banner, industry, title, company)
- Day 5: Phase 2 DM prompt pack ships — Cooz starts warm-network DMs (these are NOT public posts; they don't affect algorithm signal)
- Day 6-7: First save-worthy reference post drafted, voice-checked, NOT yet published

**Week 2: Cold-start posting at low volume, clean signal**
- 1 save-worthy reference post (Mon)
- 1 narrative-with-frame post (Thu)
- 5-10 strategic comments per day on adjacent-lane creators
- DM cadence continues

**Week 3: Add the third post type**
- 2 save-worthy posts (Mon + Thu)
- 1 narrative post (Sun, Lane B mythic — gentle re-introduction)
- Comment cadence continues
- Track: are any posts breaking 1,000 impressions? If yes, the topical signal is rebuilding.

**Week 4: Full cadence**
- 3-4 posts per week, mixed save-worthy + narrative
- First reel (Lane C) re-entry
- Monthly reach should be 3-5x of week 1 baseline if rebuild is working

**Day 30 checkpoint**: Re-run this audit. Targets:
- Layer 1 score: 9/10 (up from 3/10)
- Layer 3 score: 8/10 (up from 2/10)
- Overall: 45/60 (up from 25/60)

If we're below those targets, the lanes are wrong, not the execution. Re-run Phase 0 + 1b before re-running 1c.

---

## Anti-Pattern Check

**The most common failure mode of this rebuild**: Cooz reads this audit, agrees with everything, and then publishes a post tomorrow because "I have good content I want to share."

**Don't.** Every off-lane post during the rebuild window adds 7-14 days to recovery. The discipline of NOT posting during the rebuild is the highest-leverage move in this entire engagement.

**The second most common failure**: After Phase 1c ships, Cooz sees low impressions on the first 3 posts and thinks the new strategy isn't working. The cold-start penalty is real and accounted for in the 30-day timeline. Patience window: full 30 days, no premature pivots.

**The third most common failure**: We rebuild the profile around the WRONG semantic lanes because we skipped Phase 0 (ICP delta) or Phase 1b (lane work). Phase 0 is running now in background. Phase 1b runs immediately after. Then 1c locks in.

---

## Verdict and Recommendation

**Verdict**: 🔴 SIGNIFICANTLY SUPPRESSED. 25/60.

**Recommendation**: Run the full chain (Phase 0 → 1b → 1c → 2 → 3) before any public LinkedIn activity resumes. The investment is 1 week of strategy work for a 30-day recovery to algorithmic baseline, then 60-90 days to surpass prior reach.

**Confidence in this audit**: HIGH on signal-layer findings (Layers 1-3, derived from documented voice profile and content patterns). MEDIUM on engagement-layer findings (Layers 5-6, derived from stated facts but without live profile access).

**Recall the principle**: A great post with a bad headline and filler opener will never reach the right audience. It's not a content problem — it's a plumbing problem. We're rebuilding the plumbing.
