---
description: Farrice's GEO/SEO health-brand content machine — one front door. Daily: pick a pillar/angle from the evergreen engine, prime the raw take, cook + gate + bridge to the AUDIT DM. Whenever: --rebuild the engine, --full a new vertical.
---

# /geo-content — The GEO Content Machine (single front door)

One command so you never have to remember which workflows to chain. It loads the right context every time, points at the evergreen **Content Engine**, and produces voice-gated posts that speak to the ICP and bridge to the offer — or rebuilds the engine when the market moves. Built 2026-06-23 from the `/linkedin-daily` + `/quality-content` + `/recommend` sequence, pre-wired so it runs correctly without you thinking about it.

> **The whole system is grounded in three persistent files — this command always loads them:**
> - `_active/linkedin-launch/content-engine/CONTENT-ENGINE.md` — the 5 pillars, 35 seeds, raw-take questions, brief scaffold, cadence, 30/60/90 arc
> - `_active/linkedin-launch/research/MARKET-ICP-DOSSIER-2026-06.md` — buyer truth (avatars, awareness ladder, VoC, the 5 fears, labeled facts)
> - `_active/linkedin-launch/offers/CANONICAL-OFFER-BRIEF.md` — the offer every post bridges to (funnel = `DM me "AUDIT"`)

## Usage / Modes

```
/geo-content                    # DAILY DEPLOY (default): rotate to today's pillar → prime raw take → cook 3 variants → gate → bridge
/geo-content --topic "X"        # skip selection; cook this angle/raw thought now
/geo-content "<raw voice-note text>"   # paste your raw take; go straight to cook
/geo-content --pillar P3        # force a pillar (P1 New Shelf · P2 Proof · P3 Average · P4 Human Premium · P5 Notebook)
/geo-content --map              # just show the engine + today's recommended angle (no cook)
/geo-content --rebuild          # regenerate the 5-pillar engine (positioning shift / quarterly refresh)
/geo-content --full             # the whole sequence for a NEW vertical/reposition: research → offer+launch package → engine
```

**Cost ceiling:** $0.10/run (daily). tavily/WebSearch primary; one Perplexity call max if free search is thin.

---

## ALWAYS-LOAD CONTEXT (the spine — never skip)

| File | Supplies |
|---|---|
| `content-engine/CONTENT-ENGINE.md` | the pillar to pick, the angle's seed + raw-take questions, the cadence rules |
| `research/MARKET-ICP-DOSSIER-2026-06.md` | avatars (Dana/Marcus), the 5 fears, VoC wince lines, the labeled VERIFIED facts |
| `offers/CANONICAL-OFFER-BRIEF.md` | the funnel + which offer each pillar bridges to + the first-comment CTA |
| `_active/farrice-brand/CLAUDE.md` + `_active/linkedin-launch/voice-gate.md` | voice law (banned MOVES, required moves), pass/fail gate |
| `_active/linkedin-launch/daily/performance-log.md` | last 7 posts (rotation: never repeat a hook format / close / avatar inside 7 days) |
| `offers/lead-gen-playbook.md` | the weekly teardown (keystone) + the 10-comment plan + the pipeline tally |

**Voice law (pass/fail, from the dossier's craft section):** Cognitive Signature (Paradox Reveal → False-Frame Demolition → Reframe Landing) · scene-first, story-before-insight, reader-as-protagonist · embodied metaphors from HIS domains only (coaching/training/gaming/parenting/behavior-change) · recognition closes, never a cheap-question close · BANNED MOVES: "It's not X. It's Y." negate-then-reveal, twin-sentence aphoristic endings, triple anaphora, "Here's what/why" openers, mic-drop deflation · ≤2 em dashes (0 in hooks) · the word is **named/cited/carried** ("GEO/AEO" second) · reassure the human, indict the machine. "Polished but flat" = FAIL.

---

## MODE: DAILY DEPLOY (default)

1. **Load context** (table above).
2. **Rotation check.** Read `performance-log.md` + the barbell (Mon = hard pillar P1/P2/P3 · Wed = named-brand teardown, the keystone · Fri = human rail P4/P5). Pick today's pillar; never repeat a hook format, close structure, or avatar inside 7 days. Honor the 30/60/90 arc (`CONTENT-ENGINE.md` §30/60/90).
3. **Surface the recommendation.** Today's pillar + 1–2 candidate angles from that pillar's 7 seeds. Optionally layer a *current* zeitgeist hook — run `/linkedin-daily` Track A/B research if a live moment fits the angle (receipts + VERIFIED/LIKELY labels; never pad with training-memory trends).
4. **Prime the raw take.** Present the chosen angle's **raw-take questions** (they're in the engine, tuned to his life). **HALT — wait for his voice note / bullets / one strong sentence.** The raw take is the soul of the cook; capture his exact phrases verbatim. (`--topic` / pasted raw take skips the halt.)
5. **Cook 3 variants** (Parallax 3-variant rule; or 1 if `--topic` is precise). Each: scene-first open → Cognitive Signature → his lived stake → embodied metaphor → one VERIFIED fact woven as an *artifact he noticed* (never the lead citation) → recognition close. Hooks char-counted to the real ceilings (Dense 140–160 · Punchy ≤50/≤50 · Bomb ≤50 · Stacked ≤60/line · no questions, no em dashes).
6. **Gate (pass/fail — fail = regenerate the section, never patch).** Voice-gate + Aha gate (name the before→after belief shift) + Empathy gate (does it say their truth better than they could?) + `python3 execution/prose_classifier.py check <file>` + `fact-verifier` on any named claim. No UNCONFIRMED stat ships (never the "60.7%"/"58%").
7. **Bridge.** First comment = a value/mechanism line + the pillar's offer bridge + `DM me "AUDIT" for a free teardown.` Body never sells.
8. **Ship + log.** Append a `drafted` row to `performance-log.md` (date, pillar, avatar, hook, close, cook method, metrics=pending). Print the 3-line to-do: publish + 15-min reply window · run the 10-comment plan (`lead-gen-playbook.md` §4) · drop yesterday's numbers next run. Remind: **1 named-brand teardown this week** (the keystone — `lead-gen-playbook.md` §2).
9. **Finalize (Chain Step 6).** `chain_runner.py finalize ... --workflow geo-content --type Content`.

> Shortcut: once the pillar + angle + raw take are chosen, you may delegate the cook to `/linkedin-daily --topic "<angle>"` (its full Parallax machinery), then run the bridge + log here. `/geo-content` is the wrapper that guarantees the *right* pillar/angle/offer-bridge every time.

---

## MODE: --map (no cook)

Load context, run the rotation check, and print: today's recommended pillar + its 7 angle seeds + the one you'd pick + its raw-take questions. Stop. (Use when Farrice wants to choose and write himself.)

---

## MODE: --rebuild (regenerate the engine)

Use when positioning shifts, the dossier is refreshed, or the engine feels stale (~quarterly). **Don't rebuild what's working — extend it.** Re-run the 5-pillar generation via the **Workflow tool**, grounded in the current `MARKET-ICP-DOSSIER`, `CANONICAL-OFFER-BRIEF`, and voice law:

- **5 pillars** (P1 The New Shelf · P2 Proof the Machine Can Carry · P3 Average Is a Choice · P4 The Human Premium · P5 The Operator's Notebook), generated in **parallel** — each writes its file: pillar definition (belief broken · ICP fear · emotion · lead avatar · offer bridge · "say it better" line) + 2–3 themes + **7 angle/idea seeds** (hooks char-counted · wince line · structural move · offer bridge · 2–3 raw-take questions tuned to his life) + **1 fully-cooked, voice-gated ready-to-post exemplar**.
- **QA phase:** a `prose-doctor` pass on the 5 exemplars (banned moves, em dashes, hook ceilings, private-language test; fix in place).
- **Synthesis phase:** rewrite `content-engine/CONTENT-ENGINE.md` (how-to, pillar table, all 5 pillars inlined, the 8-field Creative-Brief Scaffold + worked example, the barbell cadence, the 30/60/90 arc, the inbound section) **and** `content-engine/ready-to-post-starter-pack.md` (the 5 cooked exemplars sequenced as a 2-week run; no launch-deck dupes).
- Pillar agents must use a subagent type with the **Write** tool (the default workflow agent — NOT `master-copywriter`, which lacks Write). Bound each agent: write to file, return a ≤120-word confirmation (prevents the long-return hang).

Output: `content-engine/CONTENT-ENGINE.md` + `ready-to-post-starter-pack.md` + 5 `_pillar-*.md`. Finalize via Chain.

---

## MODE: --full (whole sequence — new vertical or major reposition)

The end-to-end deploy that ran 2026-06-23. Three phases via the Workflow tool, each gated, **research first as a barrier** so everything downstream speaks the buyer's language:

1. **Research foundation** → `research/MARKET-ICP-DOSSIER-<period>.md` (parallel: identity-level ICP avatars + audience/awareness ladder · GEO/AI-search market truth with labeled facts · competitive landscape + the gap · Voice-of-Customer language bank → synthesize the Bridge Message).
2. **Build package** → `CANONICAL-OFFER-BRIEF` · `LAUNCH-DECK` · `featured-section-and-profile` · `lead-magnet` · `claim-safe-citation-audit` TEMPLATE + EXAMPLE · `lead-gen-playbook` · `START-HERE` (all consuming the dossier; DM-only funnel; pilot pricing).
3. **Content engine** → the `--rebuild` flow above.

Then offer to mirror the deliverables into the Google Drive archive (folder `Farrice — GEO-SEO Health Brand Launch`) via the claude.ai Drive MCP `create_file` (text/markdown → Doc). See `MEMORY.md` → "Drive Export via MCP Fallback" (gws `--upload` is faithful but the Bash sandbox flakily strips PATH; MCP needs no shell).

---

## Output files
```
_active/linkedin-launch/daily/briefing-YYYY-MM-DD.md        # daily deploy briefing + variants (if cooked)
_active/linkedin-launch/daily/performance-log.md            # rolling ratchet (append)
_active/linkedin-launch/content-engine/CONTENT-ENGINE.md    # the engine (rebuilt on --rebuild)
_active/linkedin-launch/content-engine/ready-to-post-starter-pack.md
```

## Error handling
- **No raw take (not --topic):** present `--map` and HALT. The engine is a co-pilot; without the raw take the cook caps at competent-but-flat.
- **Engine missing/stale:** run `--rebuild` first.
- **Shell strips PATH (python3/gws "not found"):** the prose gate / finalize may fail in a degraded Bash invocation — re-run the Bash step (a fresh invocation usually has a healthy shell), or dispatch a `prose-doctor` subagent (no shell). Never skip the gate silently.
- **Hook/variant fails the gate twice:** drop the angle, cook a different seed (Rewrite Before Relabel).
