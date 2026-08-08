---
date: 2026-08-08
session: oren-dara-ad-psychology
tier: operator-guide
status: enriched
---

# Ad Psychology Engine — What We Built 2026-07-19 and How to Use It

> Forge-tier extraction of the Oren John × Dara Denney Cannes 2026 video (FFU45SKaeYM) into `skills/oren-dara-ad-psychology/` — the psychology layer UNDER format selection — plus its first three deployments: a MyBPM ad pair (static spec + shoot-ready video script), three LinkedIn founder-mirror concepts, and the Proof-to-Market Ad Psychology Audit module. Companions: `skills/oren-dara-ad-psychology/genius.md` (the spine), `extractions/oren-dara-ad-psychology/` (report, amplification, blind-pass), handoff thread `oren-dara-ad-psychology`.

## ⚡ If you only read 10 lines

1. `/adpsy-tactic-select` is the front door: brand × persona × awareness → 2-3 of six psychological tactics, each with a concept seed quoting real customer voice.
2. The doctrine line: an ad converts cold traffic when it's the **safe, justified, credible, or proven** container for something the customer already thinks — you license desire, never inject it.
3. This skill picks the mechanism; `dara-denney-meta-ads` picks the vessel. Always hand off in that order.
4. Hard vetoes (auto-fail): shock-for-shock · golden-nugget review that fails the lived-experience test (URO case) · fake authority · claim without demonstration · competitor-library ideation.
5. The multiplier is the comment section: predict it before shipping (tactics 1/3/6), mine it 7-14 days after (`/adpsy-comment-mine` → virtue map → iterate in days).
6. "We don't look at our competitor ads anymore" — ideate from what YOUR audience loves organically (`/adpsy-organic-flywheel`).
7. Pending on MyBPM: render is gate-blocked (gemini-image + higgsfield-nano both CLEAR at $0.05-0.10 — approve and run the 3-variation batch).
8. Pending on LinkedIn: two practitioner receipts (nine-homepage sweep + $40K story anchor) before any concept posts.
9. Pending on the skill: Farrice's blind-pass verdict for A-tier (EVAL-048 is model-judged only).
10. Known bug flagged: `creative_router.py` regex matches "no people" as a *people* task → mis-routes to higgsfield-soul.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/oren-dara` | Expert front door (persona + full arsenal) | Any ad-psychology work, unsure which workflow |
| `/adpsy-tactic-select` | Ranked tactic brief w/ seeds + predicted comments | New brand/persona, or ads feel generic |
| `/adpsy-taboo-ad` | Taboo concept + veto log + comment design | Category has unsaid customer truths |
| `/adpsy-justification-math` | Cost-per-use math + "we're not cheap" filter | Price is the #1 objection, AOV ≥ $100 |
| `/adpsy-armchair-investigation` | Investigation script + AI casting + rage-bait plan | Rip-off-energy category |
| `/adpsy-prove-it` | 2-3 demonstration concepts (straight/extreme/trend) | Claim is physically demonstrable |
| `/adpsy-credible-explainer` | Authority plan (chain-mine + set staging + pre-seed) | Trust gap; "we can't do expert ads" |
| `/adpsy-visual-psych` | Multiples/grid/comparison visual spec | Concept is message-heavy, no visual layer |
| `/adpsy-comment-mine` | Virtue map + verbatim vernacular bank + iteration briefs | Any ad live ≥1 week |
| `/adpsy-organic-flywheel` | Organic→paid replication loop | Ideation still starts from competitor libraries |
| `/adpsy-strategy-sprint` | Dara's 6-part operating cadence instantiated | Standing up/auditing a creative operation |

## The mental model

**Two skills, one machine.** `oren-dara-ad-psychology` answers WHY a stranger converts (mechanism); `dara-denney-meta-ads` answers HOW it ships (format, hooks, statics, production, test plans). Concept flows psychology → vessel, learnings flow back comments → next tactic round. Running vessel-first is the old failure this retires.

**The customer already said it.** Every strong concept is traceable to a real line — review, comment, group-chat register, organic post. If you can't quote the source, the concept is invented; if the actual customer wouldn't say the line out loud, it's the strategist's golden nugget (the URO "We are having sex all over the house" failure — Dara: "a woman who has this problem would never think to say that").

**Comments are the product.** Taboo ads pay off in "you said what I couldn't"; investigations work because "people are getting infuriated in the comments"; authority ads anchor on the expert who replies. Design the thread, then mine it — the mechanic ad's comments revealed an honesty obsession (Bible verses included) and virtue-led iterations spiked within a day.

## Capabilities shipped

### The skill (10 workflows + 10 born-v2 prompts)
- **What it is**: six frame-verified tactics (taboo/mirroring, justification math, armchair investigation, prove-it, visual psychology, credible explainer) + two loops (organic flywheel in, comment mining out) + Dara's 6-part cadence. Every workflow carries a Pre-Flight Gate, quality rubric scoring, and an execution prompt with an Output Contract.
- **When NOT to**: organic-only brand content (route kallaway/oren-content), pure static production with a locked concept (route `/dara-static-engine`), luxury insider positioning (route `oren-luxury-psychology`).
- **Honest edges**: single-source extraction (6,915 words — fidelity capped at what's quoted in `references/source-quotes.md`); blind pass is model-judged pending Farrice; three speaker-attributed facts stay UNCONFIRMED (Zach Stuck/Hollow Socks, doctor-visit minutes, "Air" Maury spin-off).

### MyBPM deployment (first chain proof)
- **What it is**: `_active/mybpm/mybpm-merch-os-run-1/04-deliverables/11-*.md` + `12-*.md` — the Sunday/Monday tee ad pair. Mirroring tactic (the double life: "Nobody at Monday standup knows where I was at 4:00 AM Sunday"), split-screen visual psych, KEEP verdict from the 1-second gate, yapper script with substance-reference hard line.
- **Worked example of**: tactic-select → taboo build → dara 3-layer → comprehension audit, end to end.
- **Honest edges**: render blocked at the cost gate (approve-then-run); customer voice is community-lexicon, pre-launch (MEDIUM); one-raver register check owed before spend.

### LinkedIn founder-mirror concepts + P2M audit module
- **What it is**: `_active/farrice-brand/content/bank/2026-07-19-adpsy-founder-mirror-concepts.md` (3 concepts from the personal-yes founder's private register, prose CLEAN 0/10) + `_active/linkedin/02-offer/AD-PSYCHOLOGY-AUDIT-MODULE.md` (six-tactic diagnostic as a Stage-2 sprint module; three questions double as live walkthrough demos).
- **Honest edges**: concepts are cards, not final posts — writers-room pass owed; two practitioner receipts gate publication; module unpriced standalone by design (never the lead).

## Composition (options, not pipeline)

| Stack | Earns its cost when |
|---|---|
| `/adpsy-*` → `dara-denney-meta-ads` | Always — the default mechanism→vessel handoff |
| `/adpsy-comment-mine` → `/dara-winning-hooks` | A winner is live and its vernacular bank is fresh |
| `/adpsy-justification-math` → `oren-luxury-psychology` | Premium/masstige price-objection work |
| Audit module → Stress-Test Walkthrough | Cold-tier demo needs a live tangible moment |
