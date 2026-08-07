# Mission Brief Library — The 10 Kashef Briefs, Antigravity-Mapped

The 10 mission-brief prompt bodies from `assets/wargame-folder-template/tasks/*.md` are byte-identical to the PDF ("The Laundry List") originals — Kashef's language is intact below, unaltered. What's new here is the placeholder-mapping layer: where each `{{PLACEHOLDER}}` points inside this system, so `/wargame-brief` and `/wargame-batch` can fill a brief from real Antigravity resources instead of writing cold. Domain tag, effort tag, and "you get" line are reproduced verbatim from the PDF (`extractions/wargame-source/laundry-list-notes.md`).

Full brief text lives at `assets/wargame-folder-template/tasks/NN-slug.md` — this file quotes only the placeholder-bearing lines needed to build the map; read the source file for the complete brief before drafting.

---

## 01 — Build the Website
**Domain**: CODE · **Effort**: XHIGH · **Executor**: cheaper executor (Sonnet)
**You get**: *"the site build fought on paper, every move with its expected observation and failure branch."*
**Source**: `assets/wargame-folder-template/tasks/01-website.md`

| Placeholder | Maps to |
|---|---|
| `{{BUSINESS}}` | Client CLAUDE.md identity line (`_active/jen-listings/CLAUDE.md`, `_active/andrea-dj/CLAUDE.md`, or equivalent) |
| `{{PROBLEM}}` | Farrice's stated pain point, or a `competitive-intel` finding if the gap isn't self-evident |
| `{{AUDIENCE}}` | Deep ICP profile (`_active/linkedin/research/deep-icp-profile-invisible-expert.md` or client-specific ICP doc) |
| `{{CTA}}` | Decided at `/wargame-brief` time — one CTA only, never inherited from a vague ask |
| `{{LIST THEM}}` (sections) | Site IA, frozen before wargaming per Heuristic 2 |
| `{{URL OR DESCRIPTION}}` (reference) | Actual URL/screenshot Farrice supplies, or a `brand-system-builder`/`mood-board` output |

---

## 02 — Write the Copy
**Domain**: COPY · **Effort**: HIGH · **Executor**: a mid-tier model
**You get**: *"the copy mission wargamed, section order, voice risks, and the skeptic pass pre-planned."*
**Source**: `assets/wargame-folder-template/tasks/02-copy.md`

| Placeholder | Maps to |
|---|---|
| `{{PAGE}}` | The page/asset in question — often the site from mission 01 |
| `{{ICP}}` | Deep ICP profile, or `icp-deep-canvasser` agent output for identity-level depth |
| `{{STATE OF MIND}}` | `icp-deep-canvasser` identity-resistance mapping — never guessed from demographics alone |
| `{{CTA}}` | Same singular-CTA rule as mission 01 |
| `{{THREE ADJECTIVES}}` / `{{WRITER OR BRAND YOU ADMIRE}}` | `content-voice-calibration.md` or the client's own voice-calibration doc |

---

## 03 — Set Up Local AI
**Domain**: LOCAL AI · **Effort**: HIGH · **Executor**: Claude Code on a cheaper model
**You get**: *"your exact machine's local stack wargamed, runtime, models, quants, fallbacks, and the speed checks."*
**Source**: `assets/wargame-folder-template/tasks/03-localai.md`

| Placeholder | Maps to |
|---|---|
| `{{OS AND VERSION}}` / `{{CHIP}}` / `{{RAM}}` / `{{GPU/VRAM}}` / `{{FREE DISK}}` | Actual machine specs, read-only recon (e.g. `system_profiler`, `sysctl`) — never assumed from a generic spec sheet |
| `{{USE CASES}}` | Farrice's stated use cases, verbatim — no invented scope |
| `{{LOW/MEDIUM/HIGH}}` patience | Farrice's stated tolerance for tinkering, asked directly if unstated |

---

## 04 — The Tax Strategy Review
**Domain**: FINANCE · **Effort**: XHIGH · **Executor**: Opus
**You get**: *"the tax memo route with every unverifiable number flagged RECON NEEDED before your accountant sees it."*
**Source**: `assets/wargame-folder-template/tasks/04-tax.md`

| Placeholder | Maps to |
|---|---|
| `{{ENTITY TYPE}}` / `{{JURISDICTION}}` / `{{REVENUE}}` / `{{STRUCTURE NOTES}}` | Farrice's actual entity/financial facts — never inferred or estimated silently |
| `{{STATEMENTS/EXPENSE CATEGORIES}}` | Real financial statements supplied directly; if absent, the mission is BLOCKED, not estimated |

Evidence rule carried into every wargame on this domain, verbatim: "Anything you cannot verify from my materials gets marked unverified." Highest-consequence domain in the set — XHIGH is non-negotiable here.

---

## 05 — Refine the High-Ticket Offer
**Domain**: OFFER DESIGN · **Effort**: XHIGH · **Executor**: a mid-tier model
**You get**: *"the offer rebuild wargamed, buyer counterattacks and their patches already fought."*
**Source**: `assets/wargame-folder-template/tasks/05-offer.md`

| Placeholder | Maps to |
|---|---|
| `{{PROGRAM}}` / `{{PRICE}}` | Current offer stack, or the PMF offer brief (`_active/pmf-offer-shelf/04-deliverables/offer-map/PMF-OFFER-BRIEF.md`) — surface, don't regenerate |
| `{{ICP}}` | Deep ICP profile |
| `{{X}}%` close rate / `{{LIST THEM HONESTLY}}` objections | Farrice's actual numbers and honest objection list — never smoothed into "strong close rate" |
| `{{PASTE}}` current pitch | The live sales page/pitch text, read directly |

**Binding note**: per THE PATH DECISION (2026-07-01, council 7-0), no repositioning or new offers get built until $5K/mo is COLLECTED — this mission refines an EXISTING offer's pitch, it does not open a repositioning discussion. Surface that binding before wargaming if the ask drifts toward "new offer."

---

## 06 — Upgrade the Chatbot From Real Conversations
**Domain**: AI SYSTEMS · **Effort**: HIGH · **Executor**: Sonnet
**You get**: *"the chatbot upgrade route, failure patterns quoted, rewrite moves with expected outcomes."*
**Source**: `assets/wargame-folder-template/tasks/06-chatbot.md`

| Placeholder | Maps to |
|---|---|
| `{{N}}` transcripts / `{{FILES OR PASTE}}` | Actual transcript files, read in full — never sampled or summarized from memory |
| `{{CHATBOT PURPOSE}}` | Stated purpose from the system in question |
| `{{PASTE}}` system prompt | The live system prompt, read directly, not paraphrased |

**Carries the platform landmine**: this is the mission the PDF's WATCH OUT box attaches to — "do not ask the model to explain its thinking... ask for artifacts, findings, quotes, and rewrites." Enforce this rule with extra care here since transcript analysis invites "explain why it failed" phrasing.

---

## 07 — Hunt the Bugs
**Domain**: CODE · **Effort**: XHIGH · **Executor**: Claude Code on a cheaper model
**You get**: *"a bug-hunt wargame, candidate bugs ranked with the exact verification run for each."*
**Source**: `assets/wargame-folder-template/tasks/07-bugs.md`

| Placeholder | Maps to |
|---|---|
| `{{PATH}}` | The actual repo path in this monorepo |
| `{{N}}` findings | The count Farrice sets, or the model's own severity-ranked cutoff if unspecified |

Evidence rule, verbatim: "If you cannot point to evidence, it does not go in the report" — every bug wargamed here needs a reproduction command or failing-test path named, not just a description.

---

## 08 — Build the Financial Model
**Domain**: FINANCE · **Effort**: HIGH · **Executor**: a mid-tier model
**You get**: *"the model build wargamed, formulas, levers, and sensitivity checks pre-fought."*
**Source**: `assets/wargame-folder-template/tasks/08-model.md`

| Placeholder | Maps to |
|---|---|
| `{{BUSINESS}}` / `{{NAME}}.xlsx` | Client/project identity + the file's actual save name |
| `{{REVENUE STREAMS}}` / `{{COST LINES}}` / `{{ASSUMPTIONS}}` | Real inputs Farrice supplies — never invented placeholder numbers |
| `{{LEVERS}}` | The 3 levers Farrice is most likely to change, named explicitly, not assumed |

---

## 09 — Tear Down the Competition
**Domain**: RESEARCH · **Effort**: HIGH · **Executor**: Opus
**You get**: *"the teardown route, sources to pull, conflicts expected, and the gap-map criteria set."*
**Source**: `assets/wargame-folder-template/tasks/09-competitors.md`

| Placeholder | Maps to |
|---|---|
| `{{BUSINESS}}` | The positioning subject |
| `{{3 TO 5 NAMES OR URLS}}` | Named competitors, or a `competitive-intel` agent pass if the list needs discovery first |
| `{{ICP}}` | Deep ICP profile — the gap-map's "what does {{ICP}} want that nobody credibly owns" question depends on it being real, not assumed |

Evidence rule, verbatim: "Anything you cannot verify gets marked unverified rather than smoothed over... Where sources conflict, say so instead of averaging."

---

## 10 — Map the Automation
**Domain**: OPERATIONS · **Effort**: HIGH · **Executor**: Claude Code on a cheaper model
**You get**: *"the automation blueprint wargamed, checkpoints, what breaks first, and abort lines per phase."*
**Source**: `assets/wargame-folder-template/tasks/10-automation.md`

| Placeholder | Maps to |
|---|---|
| `{{DESCRIBE IT STEP BY STEP, WITH THE TOOLS EACH STEP TOUCHES}}` | The actual manual process, elicited in full via `/wargame-recon` if Farrice hasn't already written it out — this is the single richest placeholder in the set and the easiest to under-specify |

Sequencing rule carried verbatim: build order starts with "the step that saves the most time per week," and every phase gets its own runnable acceptance check before the next phase starts.

---

## Cross-Mission Notes

- **Effort tags are load-bearing, not decorative.** XHIGH (01-website, 04-tax, 05-offer, 07-bugs) marks the missions where a wrong turn is expensive enough that the drafting pass should never degrade, even under budget pressure (`goal-and-loop-contracts.md` effort economics). HIGH missions can absorb more refinement-loop degradation before the stakes justify pushback.
- **Every domain has an evidence-rule variant** — "if you cannot quote it, it does not exist" (06), "if you cannot point to evidence, it does not go in the report" (07), "anything you cannot verify gets marked unverified" (04, 09). `/wargame-brief` step 5 picks the register matching the domain rather than inventing a new one.
- **`{{BUSINESS}}` and `{{ICP}}` recur across 6 of the 10 missions** (01, 02, 05, 08, 09, plus implicit ICP framing in 06) — a client project's CLAUDE.md and deep-ICP profile, once loaded, answer most of the placeholder surface for that client's entire mission portfolio.
