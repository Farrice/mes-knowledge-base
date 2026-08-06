---
date: 2026-08-06
session: marketing-intelligence-engine
tier: operator-guide
status: enriched
---

# Marketing Intelligence Engine — What We Built 2026-08-06 and How to Use It

> Overnight build off the Isenberg × Cody Schneider video: Cody forged as a deployable expert (11 workflows, blind-pass verified), a listening-only LinkedIn Signal Scout wired into Apify, a Mon/Thu Angle Brief loop that turns niche engagement into hook/content angles on the briefs board, and the grounding audit that separates his hype from our harness. Companions: `deliverables/research-briefs/night-shift-2026-08-06/` (deploy card) · `deliverables/research-briefs/ai-marketing-agents-hype-vs-harness/` (the audit) · `skills/cody-schneider-signal-outbound/` (the doctrine).

## ⚡ If you only read 10 lines

- Doctrine line: **engagement is a hand-raise** — who engaged beats who fits the firmographic; and **sends stay human, permanently, until you explicitly unlock otherwise.**
- Run the scout: `python3 execution/signal_scout.py` (reads `_active/linkedin-launch/05-lead-gen/listening-creators.md`).
- That creators file is the quality lever — 10–20 creators your BUYER follows; it's still a 2-handle seed. Fill it via `/creator-aperture`.
- Scout output: `engager-rosters/ROSTER-YYYY-MM-DD.md` — resonance table + ICP-verbatim quotes + scored roster (comment=3, reaction=1, ICP title +2).
- Test-run economics: 4 posts → 229 engagers → **$0.50**, inside the $29/mo Apify budget; receipts in `.agent/health/signal-scout-*.json`.
- Angle Brief lands on the board Mon/Thu by ~07:30 (`com.antigravity.angle-brief`); zeitgeist daily by ~06:40. Check: `tail -20 .agent/angle-brief-run.log`.
- Deploy Cody: `/cody-schneider` (front door) · `/resonance-to-angle` (roster → angles) · `/agent-or-automation` (deflate any "we need an agent" idea).
- Every loop claims the session lock or skips — never work the tree while expecting a loop to also run.
- Long videos: skip `fetch-video-context.py` (600s cap) — invoke the watch plugin script directly.
- Nothing built here can contact anyone; the DM-draft queue was killed by decision, not deferred by laziness.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/signal_scout.py` | Roster + resonance + ICP verbatim from the creators file | Weekly listening, or before writing anything for the niche |
| `python3 execution/signal_scout.py --creators a,b --posts-per-creator 3` | Same, ad-hoc creator set | Testing a new creator before adding them to the file |
| `python3 execution/signal_scout.py --posts "<url>"` | Engagement autopsy of specific posts | A post popped and you want who + why |
| `python3 execution/apify_client.py linkedin-post-reactions "<post>" --limit 100` | Raw reactor list (name, headline, profile) | Direct actor access, no scoring |
| `python3 execution/apify_client.py linkedin-post-comments "<post>" --limit 100` | Raw comments + author + stats | Mining comment language only |
| `/cody-schneider` | Expert front door, routes to 11 workflows | Any signal/outbound/organic-engine design question |
| `/resonance-to-angle` | Content angles from a scout roster | After every scout run |
| `/creator-aperture` | The 10–20 creator list, buyer-follows rule | Now — the seed list is 2 handles |
| `/engager-signal-audit` | Judgment gate on a fresh pull before any spend | A roster looks big but you're not sure it's real |
| `python3 execution/render_brief.py <brief.json>` | House-style HTML brief on the board | Any research that deserves better than markdown |
| `tail -20 .agent/zeitgeist-run.log .agent/angle-brief-run.log` | Loop receipts | Morning check that the unattended runs fired |

## The mental model

**1. An agent is code on a cron with an LLM where judgment is needed.** Cody's definition, and the audit's verdict was that this is already our architecture (launchd + deterministic Python + headless `claude -p`). The gap was never capability — it was pointing existing loops at the market. So we didn't build an "agent platform"; we added one deterministic scraper and one synthesis prompt to a proven runner pattern.

**2. Listening and sending are different machines, and only one exists here.** The scout, the actors, the briefs — all read-only against the world. Every receipt logs `contacted_anyone: false`. This is a design boundary (Farrice, 2026-08-06: reputation and distribution stay human), enforced by absence: there is no send code to misfire.

**3. The brief is the product.** Raw rosters and packs are inputs; the thing Farrice actually consumes is the rendered HTML brief with evidence rows, confidence labels, and copy-paste deploy blocks. Anything this engine learns that doesn't land on the board effectively doesn't exist.

## Capability: Signal Scout (listening-only)

**What it is.** `execution/signal_scout.py` — deterministic Python, no LLM. Reads creators from the config file → pulls each one's recent posts (`apimaestro/linkedin-profile-posts`) → pulls who reacted and who commented (two actors added this session, schemas verified against `builds/default/openapi.json`) → dedupes by profile URL → scores (comment=3, reaction=1, +2 ICP-title regex match) → writes `ROSTER-YYYY-MM-DD.md` + `.json` to `_active/linkedin-launch/05-lead-gen/engager-rosters/` and a receipt to `.agent/health/`.

**When to reach for it.** Before writing content for the niche (the resonance table shows which hooks pulled hand-raises, in whose words); before any manual prospecting session (the roster is a ranked list of people who just publicly cared about your topic).

**When NOT to.** Don't run it daily — engagement doesn't churn that fast and the Mon/Thu cadence already covers it; ad-hoc runs are for new creators or hot posts. Don't use it as a DM list generator — that lane is closed by decision, and `/engager-signal-audit` exists to gate any human prospecting judgment.

**Worked example (live).** Test run 2026-08-06: `justinwelsh` + `gisenberg`, 2 posts each, 30 engagers sampled per post → 229 unique engagers, $0.50, and the ICP-verbatim section surfaced lines like *"money only comes with handcuffs"* that went straight into Angle Brief 001's Parallax angle.

**Honest edges.** Samples page 1 only (≤100 reactions + ≤100 comments per post) — mega-posts are sampled, not exhausted. ~85% of reactor profile URLs come back URN-obfuscated (the extraction's own discriminator caught this) — the roster's value is signal + language more than clickable profiles. One pricing datapoint so far; watch the first week of receipts. Hard rail: `MAX_ACTOR_CALLS = 80` per run, plus the $5/run and $29/mo guards inherited from `apify_client.py`.

## Capability: Angle Brief loop

**What it is.** `com.antigravity.angle-brief` (launchd, Mon/Thu 07:00) → `execution/angle_brief_run.sh`: claims the session lock or skips → refreshes the scout → headless `claude -p` executes `_active/farrice-brand/04-deliverables/ANGLE-BRIEF-PROMPT.md` → brief JSON → `render_brief.py` → board. The prompt mandates voice card + Kallaway hook masters + a Diandra hook reference (hooks only), prose-classifier checks on every deploy hook, and confidence labels on every claim.

**When to reach for it.** You don't — it reaches for you. Read it Mon/Thu with coffee; edition 001 (supervised) is the shape: thesis → evidence rows → ICP verbatim → 5–8 angles tied to live work → 2–3 CLEAN hooks.

**When NOT to.** If you need angles today off fresh data, don't wait for Thursday — run the scout manually, then `/resonance-to-angle` in-session. The loop is cadence, not a gate.

**Honest edges.** First unattended run is Monday — unproven until its log line exists. If a live session holds the tree lock at 07:00, the run skips cleanly and logs it (by design, one writer per tree). Brief quality is bounded by the creators file.

## Capability: Cody Schneider skill

**What it is.** `skills/cody-schneider-signal-outbound/` — 11 workflows in 3 tiers (T1 signal doctrine: `signal-system-blueprint`, `creator-aperture`, `engager-signal-audit`, `resonance-to-angle` · T2 system design: `waterfall-design`, `outbound-infra-blueprint`, `reply-playbook` (draft-only), `organic-engine`, `winner-remix-90` · T3 meta: `agent-or-automation`, `marketing-as-code-audit`), plus `genius.md` (his reasoning patterns, anti-patterns with transcript anchors) and `references/era-bound-2026-08-stack.md` (every vendor and price, quarantined and dated). Blind pass EVAL-062 PASS against his own live demo; auditor 0/7 failing.

**When to reach for it.** Designing any listening/outbound/organic system — for you or a client (the T2 blueprints are client-deliverable design knowledge even though we don't run sending). `/agent-or-automation` is the cheapest workflow in the arsenal for deflating an over-engineered automation idea.

**When NOT to.** Don't use it to justify building outreach automation here — the skill itself carries the house constraint. Don't re-watch or re-extract the video; extend from `extractions/cody-schneider-signal-outbound/` (2-piece solo-channel reference corpus already collected).

**Honest edges.** Single-source doctrine corpus (one interview; the two solo transcripts verify voice, not new doctrine). His 10–20-creators ≈ 80%-coverage heuristic is UNCONFIRMED — first real test is comparing two scout runs after the creators file is filled. Named vendors are partly his disclosed partners (flagged ⚠︎ in the appendix).

## Composition (options, not pipeline)

| Stack | When it earns its cost |
|---|---|
| Scout → `/resonance-to-angle` → `/enchant` or writers-room | Turning a resonance row into a shipped post at craft floor |
| Scout ICP verbatim → campaign copy (ICP-verbatim rule) | Any Cash Launch asset — their words, exactly |
| Angle Brief + zeitgeist lanes | The Monday planning read; zeitgeist = world, angle brief = niche |
| `/creator-aperture` → listening-creators.md → scout | The onboarding move for any NEW niche (Jen's lane is a candidate) |
| Cody T2 blueprints + Proof-to-Market offer | Client-facing system-design deliverables without running sends |

## Open items this guide inherits

Real creators file (10–20, both lanes) · Organic Engine v1 (hybrid Lara×Cole pen card — taste pass BEFORE wiring) · first unattended receipts for zeitgeist + angle-brief · Playwright LinkedIn gate decision · the $750 payment URL, which no amount of intelligence replaces.
