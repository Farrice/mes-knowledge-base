# ai marketing agents: hype vs. harness

> SYSTEM AUDIT · VIDEO × REPO · window: video 2026-08-05 · repo audited 2026-08-06 · lens: agents · outbound · content intelligence · sources: 44-min video + 2 full repo inventories + live actor tests · compiled: aug 6, 2026

cody schneider built two marketing agents live on greg isenberg's show. this is the honest audit: what he has that we don't, what we have that he doesn't, and what got built overnight so the gap is now mostly closed — without automating your reputation.

## the verdict
_IS HE BLOWING SMOKE?_
No — but he is not ahead of you architecturally. Cody's own definition of an agent is 'plain code on a cron job with an LLM attached where judgment is needed.' That is exactly your proven angle-map listening loop: 22 scheduled jobs, 3 of them spawning headless Claude, one log-verified daily run that scrapes, writes a brief, and commits while you sleep. His real edge was domain plumbing you lacked: engager scraping, enrichment, sending infrastructure. As of this morning the listening half of that edge is yours — and the sending half stays human by your own decision, which the audit says is the right call: nothing in this repo can send a message, and that is a feature protecting your reputation and deliverability, not a gap.

## his claims vs. what checked out
- **Reply rates are collapsing as AI volume floods inboxes; intent signals beat firmographics** [LIKELY] — Directionally consistent with the market; his fix — target people who ENGAGED with niche content ('a like is a hand-raise') — is a targeting doctrine, not a tool claim. Extracted as durable core. (https://www.youtube.com/watch?v=mD7JpNHLT70)
- **10–20 source creators ≈ 80% surface-area coverage of a niche audience** [UNCONFIRMED] — His stated heuristic from running this at scale; unverifiable externally but matches power-law audience overlap. Adopted as the sizing rule for your listening-creators config. (https://www.youtube.com/watch?v=mD7JpNHLT70)
- **One post yields ~63 deduped engagers via Apify apimaestro actors** [VERIFIED] — Replicated and beaten in your harness overnight: 4 posts → 229 unique engagers, $0.50 total, inside the existing $29/mo Apify budget. Both actors live-tested with verified input schemas. (https://www.youtube.com/watch?v=mD7JpNHLT70)
- **~$200/mo covers sending infra + inboxes for ~10,000 cold emails** [LIKELY] — Plausible market pricing (Instantly $97 tier + ~$100 domains/inboxes). NOT built: no SMTP, no ESP, no send tool exists anywhere in the repo — and you ruled sending stays human. Parked, not lost: logic captured in the era-bound appendix. (https://www.youtube.com/watch?v=mD7JpNHLT70)
- **'An agent is plain code on a cron job with an LLM attached where judgment is needed'** [VERIFIED] — This is your architecture already: launchd + deterministic Python + headless claude -p where judgment matters. The angle-map loop proved it in production Aug 5 (scraped, wrote GEO brief, committed 10 files, zero human touches). (https://www.youtube.com/watch?v=mD7JpNHLT70)
- **Organic engine: real source material → LLM drafts → scheduler → analytics remix loop** [VERIFIED] — You already own ~80% of this: voice card, thought-bank capture, LinkedIn content engines, blind-bar QA (he shows NO quality layer). Missing piece is only the scheduler/analytics loop — deferred to the Organic Engine build with your Lara×Cole hybrid pen. (https://www.youtube.com/watch?v=mD7JpNHLT70)

## what your harness actually runs without you
Twenty-two launchd jobs run on schedule. Nineteen are deterministic Python: memory harvest and decay, health audits, registry sync, social pulse scrapes, notion mirror. Three spawn a headless Claude: the angle-map listening engine (05:30 daily, log-proven), the zeitgeist daily brief (06:20 — loaded and healthy, first live fire is this morning), and the AFK mission runner (02:30, drains T1-tier cards only, with a regex net that refuses any card containing publish, send, post-to, payment, purchase, or deploy).

The honest gap the inventory surfaced: 235 expert personas and 406 skills are context loaded into sessions, not free-roaming employees — and your one runtime persona factory (agent-forge) mints markdown, not processes. That is by design (your 2026-05-25 ruling killed the subagent roster as a quality regression). The leverage move is not more skills; it is more scheduled loops that LOAD those skills and leave artifacts on your board — which is exactly what got built tonight.

## what got built overnight — and where it stops
each loop listens, drafts, and files a receipt. none of them can touch your reputation.
1. **Signal Scout — execution/signal_scout.py + two new Apify actors (post-reactions, post-comments)** — Listening-only. Test run: 4 posts → 229 scored engagers + resonance report + ICP-verbatim comment language for $0.50. Config: _active/linkedin/05-lead-gen/listening-creators.md (seeded with 2 verified handles — add your real 10–20).
2. **Angle Brief loop — com.antigravity.angle-brief, Mon/Thu 07:00** — Fuses scout resonance + zeitgeist lanes + thought-bank into one visual HTML brief of hook and content angles tied to live work. First supervised edition renders this morning; launchd owns it from Monday.
3. **Cody Schneider skill — skills/cody-schneider-signal-outbound/ + /cody commands** — Forge-grade extraction: signal doctrine and system-design workflows as durable core, tool stack quarantined in a dated era-bound appendix, waterfall and outbound blueprints preserved for the day you explicitly unlock outreach.
4. **Zeitgeist confirmed armed** — The 'not loaded' warning was stale — plist loaded, engine healthy, budget green ($0.84 spent of $29). First scheduled synthesis fires 06:20 today; its receipt is the log to check.
5. **NOT built, on purpose: sending, enrichment purchases, reply automation** — Your call, and the audit backs it: outbound send touches reputation and deliverability; enrichment costs ~$50–100/mo before a single dollar of demand is proven. Both revive only on your explicit unlock — the campaign's real blocker is the missing $750 payment URL, not automation.

## deploy blocks
**run the scout by hand (any creators, any time)**
```
python3 execution/signal_scout.py --creators justinwelsh,gisenberg --posts-per-creator 3
```
**read this week's intelligence**
```
open the briefs board: /briefs — angle briefs land Mon/Thu by 07:30; zeitgeist daily by 06:40
```
**deploy the extracted expert**
```
/cody-schneider-signal-outbound — or load skills/cody-schneider-signal-outbound/SKILL.md and pick a workflow
```

## what this isn't
_CAVEATS WORTH KEEPING_
Three things are wired but not yet battle-proven: the zeitgeist loop's first scheduled fire is this morning, the angle-brief loop's first unattended run is Monday, and the new actors' per-event pricing has one data point each — watch the first week of receipts in .agent/health/. The scout samples page one of engagement (up to 100 reactions + 100 comments per post), so mega-posts are sampled, not exhausted. One standing risk worth knowing: the Playwright browser tools in this session could technically drive a logged-in LinkedIn — no workflow uses them for that and nothing authorizes it, but the capability exists and is worth a future explicit gate. And the 80% coverage heuristic is Cody's experience, not a law — your creators file is the lever that decides signal quality.

## Source ledger
1. These AI Marketing Agents Get You Customers — Greg Isenberg × Cody Schneider — https://www.youtube.com/watch?v=mD7JpNHLT70 (retrieved 2026-08-06, VERIFIED; used for: all Cody claims; transcript 8,932 words + 100 frames on disk)
2. Repo inventory — agent infrastructure (22 launchd jobs, 3 headless loops, mission-runner gates) — file:///Users/farricecain/Google%20Antigravity/directives/orchestration-doctrine.md (retrieved 2026-08-06, VERIFIED; used for: autonomy audit; verified via launchctl list + run logs)
3. Repo inventory — outbound/extraction assets (no send capability anywhere) — file:///Users/farricecain/Google%20Antigravity/execution/apify_client.py (retrieved 2026-08-06, VERIFIED; used for: send-capability flag, Apify actor registry, budget state)
4. signal_scout.py live test receipt — file:///Users/farricecain/Google%20Antigravity/.agent/health/signal-scout-2026-08-06-test.json (retrieved 2026-08-06, VERIFIED; used for: 229-engager benchmark, $0.50 run cost)

## Context pack (agent feed)
- `directives/orchestration-doctrine.md` — Repo inventory — agent infrastructure (22 launchd jobs, 3 headless loops, mission-runner gates)
- `execution/apify_client.py` — Repo inventory — outbound/extraction assets (no send capability anywhere)
- `.agent/health/signal-scout-2026-08-06-test.json` — signal_scout.py live test receipt
- https://www.youtube.com/watch?v=mD7JpNHLT70 — isenberg × schneider · 02:27

_stack: yt-dlp · watch-plugin · apify · repo-grep_
