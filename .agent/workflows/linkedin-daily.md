---
description: Daily LinkedIn zeitgeist briefing + voice-gated post production engine (metaprompt v2)
---

# /linkedin-daily — LinkedIn Domination OS: Daily Engine

The daily operating loop for Farrice's LinkedIn launch. Produces a receipt-backed zeitgeist briefing, a contrarian opportunity map, voice-gated post draft(s), and a zero-audience distribution plan — and feeds yesterday's results back into today's decisions.

This workflow IS the metaprompt. It replaces static persona prompts with a context-load list: identity, voice, ICP, and hook mechanics come from the live source files below, never from a pasted profile paragraph.

## Usage

```
/linkedin-daily                  # full daily run (briefing + 1 post)
/linkedin-daily --first-run      # launch mode: briefing + 3 starter posts (one per active pillar)
/linkedin-daily --no-post        # briefing + commenting plan only (non-posting days)
/linkedin-daily --skip-research  # reuse most recent briefing's research (same-day re-runs)
/linkedin-daily --posts 2        # override post count
```

**Cost ceiling per run: $0.10.** Tavily/WebSearch primary ($0). One Perplexity call max (≤$0.25) only if free search is thin — and only with explicit note in the Cost Ledger.

---

## Steps

### 0. Init

- Resolve today's date → output target `_active/linkedin-launch/daily/briefing-YYYY-MM-DD.md`
- Create `_active/linkedin-launch/daily/` if missing
- Parse flags

### 1. Context Load (non-negotiable — this is what makes the output Farrice's, not a template's)

Read ALL of:

| File | What it supplies |
|---|---|
| `FARRICE.md` | Interest stack, tribal vocabulary, avatar, integration rules (80/20, Inclusion Insurance, Revelation Sequence) |
| `_active/linkedin-launch/content-os.md` | Pillars, buckets, semantic lanes, rotation schedule, 90-day arc, distribution motion |
| `_active/farrice-brand/CLAUDE.md` | Voice rules — banned moves, required moves (SOURCE OF TRUTH) |
| `_active/farrice-brand/thought-bank/pov-anchors.md` | POV anchors 1-5 (incl. no-cheap-question-closes, private-language rule) |
| `_active/linkedin-launch/voice-gate.md` | The pass/fail gate run before any draft ships |
| `_active/linkedin-launch/research/deep-icp-profile-invisible-expert.md` | ICP beliefs/identity-resistance/stages-of-change + Bridge Message |
| `knowledge/synthesis/the-persuasion-stack.md` | 4-layer build: Single Truth → Mechanism → Matched Proof → Identity Dissolution |
| `_active/linkedin-launch/daily/performance-log.md` | Last 7 entries + Carry-Forward Directives |
| Yesterday's `daily/briefing-*.md` (if exists) | Continuity; never repeat an angle within 7 days |

Chain Step 4 compliance (content domain — ≥2 skill files per `directives/content_creation_gate.md`):

- `skills/diandra-escobar-linkedin-growth/references/hook-format-library.md` (REAL character ceilings + width model)
- `skills/linkedin-2026-format-arbitrage/SKILL.md` + `genius.md` (360 Brew depth-signal physics)
- `python3 execution/memory_retrieve.py "linkedin daily post <today's lane>" --top 10`
- Recall grounding: `mcp__recall__search` on today's lane topic (silent skip if unavailable or <2 cards)
- Optional Tier 2 when the post is narrative-heavy: `skills/lara-acosta-linkedin-mastery/genius.md`; when contrarian: `skills/diandra-escobar-linkedin-growth/workflows/04-hot-take-post-generator.md`

### 2. Feedback Ratchet

1. Read `performance-log.md`. For any post older than 24h missing metrics, ask Farrice for 3 numbers: impressions, comments, profile views (+ saves if visible). Manual entry, 30 seconds. If he doesn't have them, mark `pending` and move on — never invent metrics.
2. Append metrics to the log.
3. Derive 1-3 **Carry-Forward Directives** from accumulated rows (e.g., "Dense hooks outperforming Punchy in Lane A 3:1 — bias Dense this week", "Corrective-exercise metaphor posts drive profile views — keep", "Retire X angle, flatlined twice"). Write them into the log's Carry-Forward block. Today's choices MUST honor active directives.

### 3. Research Sprint (receipts or it didn't happen)

Run these query templates via tavily-search / WebSearch (free first):

| # | Query template | Feeds briefing section |
|---|---|---|
| R1 | `LinkedIn algorithm change OR reach OR format update <current month year>` | Algorithm & Format Watch |
| R2 | `AI hype backlash OR "AI slop" OR AI replacing creatives debate <this week>` | AI-Discourse Narrative Map |
| R3 | `solopreneur OR creator economy OR consultant trend <current month year>` | Zeitgeist Pulse (ICP world) |
| R4 | `<today's lane topic> LinkedIn what's working` | Contrarian gap scan |

Capture for every claim kept: **source URL + publication date + one-line quote/paraphrase**. Discard anything undated or >60 days old unless explicitly framed as background.

### 4. Verification Pass (Chain Step 5.5 — fixes the fabricated-citation failure mode)

- Build a claim inventory from Steps 3 findings.
- Label each: **VERIFIED** (2+ independent sources or primary source) / **LIKELY** (1 credible source) / **UNCONFIRMED**.
- UNCONFIRMED claims: may appear in the briefing WITH the label, may NEVER appear in a post draft.
- Algorithm claims get extra skepticism — most "LinkedIn algorithm update" posts are creators guessing. Distinguish "LinkedIn announced" (primary) from "creators report" (pattern) from "one guru claims" (cut).
- No receipt = the claim does not ship. A thinner, true briefing beats a dense, invented one.

### 5. Compose Briefing → `daily/briefing-YYYY-MM-DD.md`

Use exactly this skeleton:

```markdown
# LinkedIn Daily Briefing — YYYY-MM-DD

## 1. Zeitgeist Pulse
[3-5 bullets. What moved in the ICP's world. Receipt + label inline per bullet.]

## 2. Algorithm & Format Watch
[What's verifiably changed or compounding. Which formats are wallpapering (saturated)
and which break pattern this week. Cite hook-format-library Wallpaper Effect.]

## 3. AI-Discourse Narrative Map
- **What the feed believes:** [dominant narrative — fear-mongering, AI-bro spectacle, slop panic]
- **What's actually true:** [grounded counter-read, receipts]
- **Farrice's wedge:** [where his deep-practitioner POV cuts against both the bashers AND the bros]

## 4. Contrarian Opportunity of the Day
[ONE opening. The single truth (one sentence), why today (zeitgeist hook),
which pillar it belongs to, identity-resistance note from ICP profile.]

## 5. Today's Assignment
Lane: [A/B per content-os rotation] | Pillar: [P1-P4] | Bucket: [Growth/Authority/Conversion/Personal]
Density: [LOW/MEDIUM/HIGH per barbell — check the week's mix]
Format: [post format + hook format, honoring Carry-Forward Directives]

## 6. Draft Post(s)
[Final voice-gated drafts — see Steps 6-7. Paste-ready, zero commentary inside the block.]

## 7. Distribution Plan (zero-audience motion)
[10 comment targets: 5 large accounts in-lane + 5 peer accounts. For each: who/why/the
angle of a substantive comment that adds a missing mechanism — never "great post".
15-min reply-window note for own post.]

## 8. Cost & Receipts Ledger
[Searches run, $ spent, every receipt URL + label.]
```

### 6. Post Production (skip on --no-post)

For each post (default 1; `--first-run` = 3, one per active pillar, P4 held back per Revelation Sequence):

1. **Persuasion Stack build** (in order): Single Truth (one sentence, write it first) → Mechanism (the WHY — this is where Farrice's frameworks live) → Matched Proof (one telling specific; never fabricate — if no real number exists, use experiential proof) → Identity Dissolution (speak to the ICP's identity resistance using their private language, per POV anchor #5).
2. **80/20 + Inclusion Insurance**: 80% core value, 20% interest flavor; bridge phrases for non-sharers; density per barbell.
3. **Hook**: generate 3 candidates in 2+ different formats from `hook-format-library.md`, character-count each against the REAL ceilings (Dense 140-160 no breaks · Punchy ≤50/≤50 · Bomb ≤50 · Stacked lines ≤60 · 210 max total · no questions · no em dashes · never fabricate numbers). Pick the strongest gap.
4. **Body**: pull-through to the last line; one idea per post; close with a voice-true close (image / declaration / bookend admission / concrete future / naming what they feel) — NEVER a generic question.

### 7. Voice Gate + Hook Check (pass/fail — fail = REGENERATE, not patch)

Run `_active/linkedin-launch/voice-gate.md` top to bottom. Hard requirements:

- Zero banned structural moves (twin-sentence endings, triple anaphora, "It's not X. It's Y.", "Here's what/why" openers, mic-drop deflation, cheap question close)
- ≤2 em dashes per post (0 in hooks)
- Cross-piece variance: no two posts in a 7-day window share a closing structure or hook format (check yesterday's briefing + log)
- Hook passes character ceiling for its declared format (count it, show the count)
- Private-language test: at least one line only Farrice's audience would write; zero lines any creator in the category could have written for the load-bearing sentences
- Every factual claim in the post is VERIFIED or LIKELY

### 8. Ship Package

- Embed final draft(s) in briefing §6; append a `drafted` row per post to `performance-log.md` (date, pillar, lane, bucket, format, hook format, density, metrics=pending)
- Print Farrice's 3-line to-do: publish + 15-min comment-reply window · run the §7 commenting plan · drop yesterday's 3 numbers into tomorrow's run

### 9. Finalize (Chain Step 6)

```bash
python3 execution/chain_runner.py finalize "LinkedIn daily briefing + N post(s) — YYYY-MM-DD" \
    --expert diandra-escobar --skill diandra-escobar-linkedin-growth --workflow linkedin-daily \
    --type Content --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --sub-agents [measured] \
    --notes "[what worked] | Factual Grounding: [1-10] | Verification: [PASS/PARTIAL]"
```

Factual Grounding veto applies: scored <6 = the briefing's claims get re-verified before delivery.

---

## Error Handling

- **Research returns thin/nothing**: ship the briefing with fewer, truer bullets + a note. Never pad with training-memory "trends".
- **Bash/scripts unavailable** (classifier outage, etc.): proceed with reads + drafts; queue memory_retrieve + finalize as a printed to-do for retry.
- **No metrics from Farrice 3+ days running**: flag it in §5 — the ratchet is the system's learning loop; without it this is a content cannon, not an engine.
- **Hook fails ceiling twice**: drop the angle entirely, write a different hook on a different angle (Rewrite Before Relabel rule).

## Output Files

```
_active/linkedin-launch/daily/briefing-YYYY-MM-DD.md   # the daily deliverable
_active/linkedin-launch/daily/performance-log.md        # rolling ratchet (append)
```
