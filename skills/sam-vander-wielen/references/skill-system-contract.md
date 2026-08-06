# Skill System Contract — Sam Vander Wielen Launch System

*Produced by `/source-to-skill-system`, 2026-08-06. Implements `semantic_libraries/antigravity/primitives/skill-system-contract.md`.*

## Build Shape Decision

| Shape considered | Verdict |
|---|---|
| Component skill | Insufficient — 12 components need ordering and handoffs |
| Reference | No — the source teaches behavior, not context |
| Workflow | Insufficient — one command can't carry the whole launch |
| **Skill system** | ✅ **CHOSEN** — components exist and need composition with handoffs |
| Companion OS layer | **Rejected** — this source teaches *domain expertise* (launch mechanics), not how the harness should operate. A companion layer would wrongly push launch tactics into control-plane workflows. |
| Expert composition primitive | Not yet — one expert owns this function; revisit if Priestley/Haynes/Wendt get chained by default |
| No build | Rejected — arsenal gap confirmed (nearest match `/jh-show-rate-diagnostics`, score 22, diagnostics only) |

## Contract Fields

| Field | Value |
|---|---|
| **Source evidence** | YouTube `OMR73JQdsFQ` (The Nathan Barry Show, 61:20, pub. 2026-08-06). Local: `extractions/sam-vander-wielen/transcript.md` (334 turns, 14,627 words), `visual-context.md`, `extraction-report.md`. **Limits**: single source, no cross-enrichment; all figures self-reported; visual channel empty of craft; 2 legal claims UNCONFIRMED; expert name was caption-mangled and corrected off-source. Full ledger: `source-ledger.md`. |
| **Objective** | Give the harness a deployable live-webinar launch capability it did not have — from ramp through cart, at $1,000+ price points, without building a new product. |
| **Components** | 12 workflows (`skills/sam-vander-wielen/workflows/sv-*.md`) · `genius.md` · 4 references · 12 born-v2 prompts · `agents/sam-vander-wielen/AGENT.md` · front door `/sam-vander-wielen` · scripts: `mint_menu_wrappers.py`, `sync_registries.py`, `prompt_library.py`, `skill_auditor.py`, `blind_pass.py` |
| **Step order** | `/sv-customer-personality-lock` (who) → `/sv-launch-system` (architecture) → `/sv-webinar-script` (the room) → `/sv-showup-engine` (attendance) → `/sv-order-bump-stack` (checkout) → `/sv-replay-engine` (coverage) → `/sv-unscalable-layer` (the 5%) → `/sv-newsletter-magnet` + `/sv-subject-line-hero` (ongoing demand). Diagnostics (`/sv-launch-teardown`, `/sv-ai-objection-kill`, `/sv-book-funnel-bridge`) enter at any point. |
| **Inputs** | Product + price · list size · prior launch numbers · ad budget · team · founder hours available · target date · compliance context |
| **Outputs** | Dated launch calendar · webinar run-of-show with verbatim beats · automation map + video script · bump stack + checkout copy · replay plan · non-scalable schedule with blocked hours · growth loop |
| **Handoff summary** | Pass the **artifact plus the gate verdict**, never the upstream transcript. Boundary shape: `{deliverable path, rubric level reached, Recognition Test verdict, Two-Minute Test verdict, open risks}`. Downstream steps read `genius.md` + the named reference, never the full extraction. |
| **Composition rule** | Sam **owns the launch function**. Priestley (`/oversubscribed-launch-sales-system`) contributes demand engineering only. Haynes (`/jh-show-rate-diagnostics`) contributes diagnosis and hands the repair to `/sv-showup-engine`. `/offer-redteam` runs **before** any of this when the offer itself is suspect. Integration rule: **one author per asset** — never blend Sam's disqualifier with a scarcity-first pitch in the same script. |
| **Human checkpoint** | **(1)** Founder must personally consent to the non-scalable hours before `/sv-unscalable-layer` output is treated as a plan. **(2)** Any disqualification or temperament language entering housing, lending, employment, health, or finance copy requires compliance review. **(3)** Any client-facing use of Sam's figures requires the self-reported label. Skipped for local reversible edits. |
| **Validation** | `skill_auditor.py check --skill sam-vander-wielen` → **7/7 PASS** · `renaissance_audit.py` → **0 fail** · `mint_menu_wrappers.py` → 12/12 menu-reachable · `workflow_router.py search` surfaces `/sv-launch-system` ✅ · `blind_pass.py prepare` → **corpus unmet, gap named** |
| **Behavior-changing proof** | Before/after below — required because this is a sales/persuasion source |
| **Result surface** | Slash commands in the menu; front door `/sam-vander-wielen`; artifacts written where the invoking task lives. Reusable deliverables default to brief format per `readout-os`. |
| **Context policy** | **Hot**: nothing — long-tail by design. **On demand**: `genius.md` first, then the one matching workflow. **Cold**: `extraction-report.md`, `transcript.md`, `source-quotes.md` (loaded only for voice work or provenance checks). Never load the transcript into a downstream step. |
| **Reuse hook** | Extend, never rebuild. New Sam material → `/extract` Extension Mode against `sam-vander-wielen`. The **launch-system shape** (ramp → one live → replay → cart → 5%) is reusable for any expert-led launch and is the candidate spine if a second launch expert is ever extracted. |
| **Goal packet** | **Not required** — this source changes no self-improvement, maintenance, or evolution behavior. |
| **Agentic engineering packet** | **Not required** — this source changes no context policy, review loop, dependency safety, or source-truth behavior. It is domain capability only. |

---

## Behavior-Changing Proof (required — sales/persuasion source)

**Test**: the pitch-permission moment at the top of a live webinar. Same offer, same audience.

### BEFORE — what gets produced without this skill loaded

> "Hey everyone, thanks so much for being here! Before we dive in, I just want to let you know that at the end of today's training I'll be sharing an exclusive offer that's only available to people on this live call. So stick around to the end — you won't want to miss it. Now let's get into it!"

### Diagnosis

Scores **2 — Signposted** on the decision rubric. The pitch is announced, not permitted. "Exclusive," "only available," and "you won't want to miss it" are all manufactured urgency doing work that trust should do. Nobody is turned away, so nothing signals selectivity. It fails the Recognition Test: a non-buyer gets nothing here except a reason to feel they should have stayed.

### Source mechanic applied

Consent-Then-Disqualify (`genius.md` Pattern 2; verbatim at `source-quotes.md` [07:53]) — ask permission as a real chat question, then narrow the door with a reason **that costs the seller something real**.

### AFTER

> "Before we start — the next hour is going to be genuinely valuable whether or not you ever buy anything from me. You'll leave with the full [outcome], today.
>
> So let me ask: is it okay with you if at the very end I share what working with me looks like? Type **yes** in the comments if that's alright.
>
> [reads the yeses]
>
> Thank you. And to be clear — that's if it's a good fit for you **and for me**. I only take [N] of these a quarter, and I deliver every one of them myself. So if you're not the right fit, I'd genuinely rather you didn't buy — because I'm the one who has to sit with it on the back end.
>
> Alright. Let's get into it."

### Behavior delta

| Dimension | Before | After |
|---|---|---|
| Rubric level | 2 — Signposted | **4 — Narrowed** |
| Permission | Announced | Asked, granted in chat |
| Selectivity | None | Real, with a cost the seller bears |
| Urgency source | Manufactured ("exclusive", "don't miss") | Structural (capacity the seller actually has) |
| Recognition Test | FAIL — value framed as bait | **PASS** — value framed as unconditional |
| Status polarity | Audience is sold to | Audience qualifies |

The measurable change: the audience types a word, which converts passive attendance into a granted permission — and the disqualifier makes the offer something to qualify for. This is the mechanic behind *"I didn't feel like I had to buy. I wanted to."*

### Proof object / proof gap

**Proof object**: the transformation above is reproducible from `references/prompts-v2/webinar-run-of-show.md` — the prompt refuses to output level 4 unless a real seller cost is supplied, and marks the script level 3 honestly when none exists. That refusal is the enforcement.

**Proof gap — named honestly**: no *outcome* proof exists. Sam's 128-in-five-minutes is her result, on her list, and this system has not yet run a launch end-to-end for Farrice or a client. **The proof above is a craft delta, not a revenue delta.** No revenue claim is made or implied.

### Next gate

First real deployment. The lightest honest test is `/sv-subject-line-hero` on the next Parallax send — one email, measurable open-rate delta, zero build cost. Anything larger should wait for a live launch.

---

## Quality Gate Self-Check (`/source-to-skill-system`)

| Reject condition | Status |
|---|---|
| Giant all-purpose skill instead of components | ✅ 12 focused components, each with its own contract |
| New skill without checking existing routes | ✅ Arsenal checked before build; gap confirmed; 8 "When NOT to Use" redirects written |
| Skips source grounding | ✅ 35-claim ledger, timestamped, VERIFIED/LIKELY/UNCONFIRMED |
| Lacks handoff, checkpoint, or validation | ✅ All three defined above |
| Lacks behavior-changing proof | ✅ Before/after with diagnosis, mechanic, delta, proof object **and named gap** |
| Depends on hidden chat context | ✅ Everything on disk under `skills/` + `extractions/` |
| Mutation-capable evolution change without a Goal Packet | ✅ N/A — no evolution behavior touched |
| Agentic engineering turned into a broad new command | ✅ N/A — no control-plane change |
| New packages without a dependency safety gate | ✅ Zero new dependencies |
| Review loop without a finish line | ✅ Blind pass has an explicit unmet condition and a stated close procedure |

## Starter Route

```bash
/sam-vander-wielen                    # front door — persona + full arsenal
/sv-launch-teardown                   # if a launch already exists: diagnose first
/sv-customer-personality-lock         # if starting fresh: who, before what
/sv-subject-line-hero                 # cheapest first proof — one email, today
```

**First artifact**: a subscriber-as-hero subject line + preview text for the next send.
**Quality bar**: passes the curiosity check and the merge-tag read-aloud test.
**Reuse hook**: `/extract` Extension Mode when the next Sam Vander Wielen source appears.
