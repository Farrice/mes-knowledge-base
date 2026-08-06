# Extraction Vision — Cody Schneider, Signal-Based Marketing Systems

**Source**: Greg Isenberg podcast, "These AI Marketing Agents Get You Customers" (44:00, published 2026-08-05). Transcript 8,932 words + 100 extracted frames (screen-share heavy).
**Extraction date**: 2026-08-06 · **Mode**: `/extract-forge`, overnight autonomy, checkpoints self-approved (see `forge-log.md`).
**Speaker verification**: Cody Schneider self-identifies at 00:52 ("I'm Cody Schneider. I'm going to be your guest today"). Frame 0069 shows his LinkedIn profile card: *Cody Schneider · Graphed.com — Deploy AI Agents for Marketing · 2,894 profile viewers · 36,190 post impressions*. Host is Greg Isenberg (transcript garbles as "Greg Eisingberg"). No transcription-tool misattribution risk.

---

## 1. Uniqueness Audit — what he does that no one on the roster does

The bench already holds outbound *messaging* (John Whiting), LinkedIn *authoring* (Lara Acosta), *agentic workflow assembly* (Nick Saraev), and *content psychology* (Kallaway). Nobody on the bench holds **targeting epistemology** — the question of *how you know who to talk to before you've written a word*.

Cody's answer is the whole extraction: **engagement is a hand-raise, and a hand-raise beats a firmographic**. Everyone else on the roster starts downstream of a list. He is the only source who treats the list itself as the creative act.

Three further non-duplications:

- **Sourcing math as a first-class discipline.** "There's a handful of outliers within any niche and everybody is engaging with those handful of outliers. If you just monitor those outliers, you're actually going to get 80% surface area coverage for that entire industry." Nobody else in the arsenal has stated a coverage law. Saraev builds pipes; Cody decides what's worth piping.
- **Token parsimony as architecture doctrine.** "You should not be paying Anthropic to do an API call. You should be paying them to make the software that uses CPU to do the API call." This is the exact inverse of the "token-max" default and it is a *cost-of-goods* position, not an aesthetic one. It sharpens every agent decision this repo makes.
- **Compliance lines drawn out loud.** He separates *acquiring* data (legal — you're buying from brokers) from *what you do with it* (the actual compliance surface), and voluntarily disclaims: "I don't think anyone would mistake you for a lawyer." Roster-wide, this candor about the line is rare and it makes the material safe to deploy.

## 2. Business Leverage Map (deployability × differentiation)

| | Low differentiation | High differentiation |
|---|---|---|
| **High deployability** | Inbox/sending mechanics (commodity, ages fast → era-bound appendix) | **Signal doctrine + creator-list design + resonance→angle** — deploys tomorrow against Proof-to-Market, already half-built as `execution/signal_scout.py` |
| **Low deployability** | Full SDR-in-a-box (Farrice does not send cold email) | **Marketing-as-code / agent-vs-automation frame** — reshapes how this repo builds *every* tool, slow burn, compounding |

The leverage concentrates hard in the top-right. Farrice's constraint (sends are human-only; reputation and distribution stay his) removes the bottom row entirely — which is *good*, because the bottom row is exactly the part that will be stale in six months.

**Direct business hit**: Proof-to-Market ($2,500 sprint, supplement/performance brands) needs a defensible answer to "how did you find me and why do you think I need this?" The signal doctrine *is* that answer — and it doubles as content intelligence, because the same pull that names the prospects also names the language they used in the comments (ICP verbatim, per the standing 2026-07-30 verdict).

## 3. Cross-Expert Stacking Map

| Stack | Compound output |
|---|---|
| Cody signal pull × **Lara Acosta** | Engager roster's top comment language → hook material written in her formats. The angle stops being invented. |
| Cody resonance report × **Kallaway** | Which topics actually pulled hand-raises → his psychology lens explains *why*, so the remix is principled not statistical |
| Cody 90-day remix × **Nicolas Cole** | Winner corpus → Cole's proven-format library for the remix pass; Cody supplies the *what*, Cole the *shape* |
| Cody agent-vs-automation × **Nick Saraev** | Saraev builds the automation; Cody decides which steps deserve inference at all. Direct cost reduction on every build. |
| Cody trapped-context mine × **writers-room** | Sales calls / Slack / lost-deal reasons as the source material Layer 0 has been missing |
| Cody ICP-fit gate × **Alex Hormozi** | Fit gate scored on money-model math (is this account even solvable at 2× CAC?) rather than title-matching |
| Cody earned-media arithmetic × **Daniel Priestley** | CPM-equivalent of organic reach as the argument for the oversubscribed-launch motion |

## 4. Gap Fill — what this adds to the roster

1. **A targeting epistemology.** First expert who answers "who?" with evidence rather than persona documents.
2. **A cost model for agency.** "An agent is code with a thinking loop and a live data stream" — plus the corollary that inference belongs only where judgment lives. This is a repo-wide governor.
3. **A listening/broadcasting bridge.** The same signal pull serves outbound targeting AND content angle discovery. Nothing else in the arsenal serves both halves from one artifact.
4. **A decomposition method for automating a role.** "What was the human doing?" — media buyer decomposed into research angles → make creative → test → prune losers, promote winners. That is a transferable procedure for turning any role into software.

## 5. Creative Direction (latitude 3 — autonomous)

- **Durable core, dated shell.** Per the binding recency rule: signal doctrine, sourcing math, waterfall *logic*, lane separation, agent-vs-automation, organic loop mechanics = skill core. Every named tool, actor, and dollar figure = `references/era-bound-2026-08-stack.md`, labeled and quarantined. A workflow that names a vendor in its body has failed the rule.
- **Listening-only posture in the build.** Farrice's decision (2026-08-06) is that outbound sends and DMs stay human. Workflows therefore produce *intelligence and drafts*, never dispatch. Reply-handling ships as a draft-only playbook. This is not a watering-down — it is the highest-leverage half, and it's the half that survives platform crackdowns.
- **Wire to what exists.** `execution/signal_scout.py` already implements the listening pipeline (creators file → engager roster + resonance report, Apify-budget-guarded). Workflows reference it; none invent parallel plumbing.
- **Depth target**: Mastery — 11 workflows across 3 tiers, 18 genius patterns, 8 signature moves.

## 6. Risks / honest limits

- **The source is one 44-minute conversation.** Rich but singular. Cody explicitly says "we don't have time today to go into all the specifics." Where he gestures rather than teaches (compliance detail, agent hosting specifics, LinkedIn DM tooling), the extraction marks it and does not invent.
- **Half the material has a shelf life measured in months.** Deliverability tactics, actor availability, and pricing will all move. Quarantined by design.
- **He is selling.** Graphed is his company; several named tools are disclosed partners ("they're a partner of ours"). Tool recommendations are treated as *disclosed-interest* signals, not neutral benchmarks — noted in the appendix.
