---
date: 2026-08-04
session: insight-brief
tier: operator-guide
status: enriched
---

# Angle Map Listening Engine — What We Built 2026-07-31→08-04 and How to Use It

> This session fused the health-performance GEO daily brief and the insight brief into ONE scheduled listening engine (v4.0), then upgraded it to a content factory (v4.1): story-seat composition bench, rotating finished-format calendar, four-tag assets, a content vault with queue states, and a two-ring identity-level audience/ICP dossier. Companion files: engine spec `_active/health-performance-ip-library/AUTOMATION_PROMPT.md` · standard-setting brief `_active/health-performance-ip-library/daily/2026-07-31-angle-map-listening-brief.md` · ring definitions `_active/linkedin/04-deliverables/context-os/08-TWO-RING-RESONANCE-DOSSIER.md`.

## ⚡ If you only read 10 lines

1. The engine runs daily at **05:30 local** via `com.antigravity.angle-map-listening`; log: `_active/health-performance-ip-library/06-system/listening-run.log` — check it FIRST if a brief is missing.
2. Your COS morning brief now carries a **🎧 Industry listening** section from `daily/LATEST-EXEC-CUT.md` (fresh ≤1 day, silent when stale).
3. Every brief = **Daily Core** (3-min read: tension · promises-not-kept receipts · thesis · post seed · delta line) + one **rotating deep focus** (Mon audience → Sun education chapter; Fri = weekly synthesis).
4. Finished assets land in `_active/farrice-brand/content/vault/` as `status: READY`; flip to POSTED by editing the file + `INDEX.md` row when you publish.
5. Every asset carries four tags: content pillar (Proof|Thesis) · narrative pillar (P1-P5) · bucket · **ring** (Outer|Inner|Bridge — defined in dossier 08).
6. The old cloud routine "Daily Health-Performance Market Brief" is **paused** (re-enable at claude.ai/code/routines); local runs replaced it because cloud was proxy-blocked (zero Reddit reads).
7. Social listening spend: standing approval within **Apify $29/mo + Perplexity $30/mo**; scrape check: `python3 execution/apify_client.py budget-status`.
8. Targeted Reddit verbatim: `python3 execution/apify_client.py reddit "subreddit:Supplements <query>" --limit 12` (~$0.01/call; the `--subreddit` flag adds a frontpage URL, the `subreddit:` operator actually filters search).
9. Doctrine line: **the engine feeds canon, never edits it** — living docs 03/07 get dated append-only deltas; promotion into canon bodies is an explicit curation session.
10. The vault stocks faster than the 3-5/week posting ceiling on purpose — vault is the magazine, the queue is the gate.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `launchctl list \| grep angle-map-listening` | job registration status | brief didn't land; confirm the job is loaded |
| `tail -50 "_active/health-performance-ip-library/06-system/listening-run.log"` | run transcript incl. lock claims + exit codes | diagnosing a missed/failed 05:30 run |
| `zsh execution/angle_map_listening_run.sh` | a full engine run NOW (claims tree lock; skips if a session is live) | manual re-run after a failure or a missed day |
| `python3 execution/apify_client.py budget-status` | month spend vs $29 cap | before a heavy scrape day |
| `python3 execution/apify_client.py reddit "subreddit:X <q>" --limit N` | verbatim buyer threads as JSON | you need real buyer language for a receipt |
| `cat _active/farrice-brand/content/vault/INDEX.md` | vault state table | picking what to post today |
| `/resume insight-brief` | this thread's pinned handoff | continuing the work-stream |
| `/content-queue` | idea-queue ops (separate layer) | curating WHAT to post from vault stock |

## The mental model

**One engine, four accumulators.** Each daily run does research once, then feeds four places at once: the brief you read (education), the vault (ready-to-post content), the living docs (compounding audience/ICP truth), and the ledgers (receipts). Nothing terminates in the brief — that's the flywheel.

**Two rings, one bridge.** Outer-ring content resonates broad (relatable, perspective-shifting, better-off-after-reading); inner-ring content makes the founder see their own private sentence. The offer converts at the bridge: "we need more creative" is the identity-safe version of "my conviction doesn't survive the trip to the page" (dossier 08's core finding). Content resonates broad, converts narrow.

**Proof decays; angles should lean on the least-decayed surface.** The week's education synthesis: a supplement brand's five proof surfaces (study, review, badge, felt effect, shelf) decay independently. This is both a content series ("Proof That Survives Checking") and a client diagnostic.

## Capability: the scheduled engine (v4.1)

- **What it is:** a headless `claude -p` run at 05:30 executing `AUTOMATION_PROMPT.md` in full — market scan, Apify-first listening, angle scoring with repetition penalty, Daily Core + deep focus, vault filing, living-doc deltas, Drive mirror. The runner (`execution/angle_map_listening_run.sh`) claims the session lock first and **skips the day** if another writer holds the tree (logged, never silent corruption).
- **When to reach for it:** you don't — it runs itself. Reach for the *log* when the COS 🎧 section is missing.
- **When NOT to:** don't hand-run it while another session is live (it will skip anyway — the lock is the guard). Don't re-enable the cloud routine alongside it: that's the duplicate-brief collision of 07-30/07-31 again.
- **Worked example:** the 2026-07-31 inaugural run — 4 Apify calls ($0.032), 4 verbatim receipts, VERIFIED Neutonic raise, drawer post + essay + video script filed READY, W31 synthesis, Drive doc exported. Verdict: good.
- **Honest edges:** runs 08-01→08-04 are **unverified** (next session's first check); a slept-through 05:30 fires on wake (launchd default), so late briefs are normal, missing ones are not. Headless permission mode is `acceptEdits` — an engine step needing an unapproved tool degrades rather than prompts.

## Capability: the content vault

- **What it is:** `_active/farrice-brand/content/vault/` — one dated file per FINISHED asset with frontmatter (`status`, four tags, source brief, format) + `INDEX.md` table. States: READY → POSTED → outcome note.
- **When to reach for it:** every posting day — pick by ring/bucket balance, not recency. Week-2 POV batch (campaign #6) should pull from here first.
- **When NOT to:** don't file outlines or seeds — finished assets only; seeds live in the briefs.
- **Honest edges:** state flips are manual (you or a session edits the file + row); no automation marks POSTED. Only 3 assets stocked so far; the ratchet is the rotating-format calendar.

## Capability: the two-ring dossier (08)

- **What it is:** identity-level ICP + engagement-audience map extending doc 07 — resistance under the objections, buying-moment states as hours, outer-ring segments with save/share psychology, the Bridge Message, a language map.
- **When to reach for it:** before writing any hook, DM, or POV post — ring-tag against it; when a draft feels generic, check it against the four better-off takeaway types (Monday diagnostic / meeting sentence / protective boundary / shame-reducing permission — none present = commentary, kill it).
- **When NOT to:** never quote its founder-side "private language" as real customer voice — it is composite and labeled; real verbatim is consumer-side only until 3 qualified DMs land (the update trigger).
- **Honest edges:** the whole inner-ring layer is inference until DMs generate real founder language; the one measurement gap: add "who sent you this?" to DM intake or forwards stay unmeasurable.

## Composition options (never forced wiring)

| Stacks with | When it earns its cost |
|---|---|
| `/content-queue` (idea layer) | vault stock exceeds ~10 READY and selection needs curation discipline |
| `/voice-compile` | before any pen session drafting from vault seeds (14 verdicts pending now) |
| `/social-listen` deep runs | a Wednesday promises-deep-dive needs more than the engine's default scrape budget |
| Market Pulse routine (2x/wk, still enabled) | overlap review pending — consolidation candidate, not urgent |

## Honest state at close

Shipped and verified: engine spec v4.1, launchd job loaded, Apify pipe live-proven, vault + 3 READY assets, dossier canonical, inaugural brief exported to Drive, cloud routine paused, cloud W31 content recovered as `-cloud-run` variants. Unverified: whether 08-01→08-04 runs fired. Open: 3 diverged branches (2 live Codex threads — coordinate, don't merge blind), DM-send status vs the 07-31 commitment, COS weekly 2d overdue.
