---
date: 2026-08-06
session: sam-vander-wielen-forge
tier: operator-guide
status: enriched
---

# Sam Vander Wielen Launch OS — What We Built 2026-08-06 and How to Use It

> A 61-minute Nathan Barry Show interview became a 12-workflow live-webinar launch capability the arsenal did not have. Ships **B-tier** — the blind pass is genuinely unrun, and the gap is named rather than hidden. Companion files: `skills/sam-vander-wielen/SKILL.md` (manifest) · `genius.md` (load first) · `references/source-ledger.md` (35-claim provenance) · `references/skill-system-contract.md` (contract + before/after proof) · `extractions/sam-vander-wielen/` (transcript, visual-context, full report) · `docs/solutions/2026-08-06-auto-caption-proper-nouns-poison-extraction-slug.md` (the scar).

## ⚡ If you only read 10 lines

1. `/sam-vander-wielen` is the front door; 11 `/sv-*` commands fire directly.
2. **Load `genius.md` before any workflow** — it carries the Recognition Test and the 5-level rubric everything else scores against.
3. **The Recognition Test:** *"Would a registrant who did not buy still feel like they got the better end of the deal?"* Fail → rebuild the asset, don't polish it.
4. **The Two-Minute Test:** say *"two minutes for a $X sale is [verdict]"* out loud. If absurd at your price, batch down or cut the non-scalable layer.
5. **Ship at rubric level 4 (Narrowed), aim for 5 (Relaxed Confidence).** Levels 1–2 get rebuilt.
6. The disqualifier only works if the reason **costs the seller something real** — a generic "right fit" line scores 3, not 4.
7. Cheapest first proof, today, $0: `/sv-subject-line-hero` on the next Parallax send.
8. All of Sam's figures ($500K/4 days, 60% attach, 583 videos) are **self-reported and hers** — never a user's projection. Every Quality Gate enforces this.
9. Two legal-adjacent claims in the source are **UNCONFIRMED** (`source-ledger.md` 34–35). Never assert them; the core AI mechanic needs no legal claim.
10. Branch `claude/vanderland-webinar-launch-forge` is **pushed but unmerged** — merge needs a registry *regenerate*, never a hand-merge.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/sam-vander-wielen` | Persona + full arsenal (front door) | You want the whole capability in context |
| `/sv-launch-system` | Dated launch calendar + honest economics model | A $1K+ product needs a launch or relaunch |
| `/sv-webinar-script` | Run-of-show + verbatim consent/disqualify/close beats | Writing a live session that ends in an offer |
| `/sv-showup-engine` | Automation map + 6-beat 2-min video script | Registrations are fine, attendance isn't |
| `/sv-unscalable-layer` | The designed 5% — acts, volume, batches, blocked hours | Automation freed hours and you don't know where to spend them |
| `/sv-order-bump-stack` | Multi-bump checkout + paste-ready copy | Checkout has 0–1 bumps |
| `/sv-newsletter-magnet` | 4 forecast posts + transparency variant | Growing a list with no lead magnet |
| `/sv-subject-line-hero` | 3 subject variants + preview text + 4 checks | Every send. Weak opens especially |
| `/sv-ai-objection-kill` | Teardown outline + kill shot + do-not-banish integration | "Why buy this if I can just use ChatGPT?" |
| `/sv-replay-engine` | One-live + private audio replay plan | Running multiple lives to cover time zones |
| `/sv-book-funnel-bridge` | Shoulder-topic thesis + webinar-close bonus play | A book/long asset isn't driving business |
| `/sv-launch-teardown` | Scored diagnostic → exactly ONE fix | A launch underperformed and why is unclear |
| `/sv-customer-personality-lock` | Temperament + constant doubt + the ceded buyer | Positioning is generic; ICP work reads flat |

*`/sv-ai-objection-kill` reaches via the front door only — no direct shim. The minter reports nothing to do and hand-writing wrappers is banned (arsenal-loop Invariant 2).*

## The mental model

**One idea makes the rest obvious: she automates 95% of the launch specifically so she can afford to be unscalable in the last 5% — and the 5% is what sells.** 583 personal videos and 329 handwritten notes are affordable only because *"there was nothing else for me to do."* Bolt the 5% onto an un-automated business and you get a burned-out founder, not a launch. That's why `/sv-unscalable-layer` gates on "is the machine built?" and refuses to proceed if it isn't.

**Second: never manufacture pressure — manufacture the feeling of having chosen.** Ask permission to pitch (a real question typed in chat), then narrow who may buy, with a reason that costs you something. Attendees report *"I didn't feel like I had to buy. I wanted to."*

**Third: patience is a conversion asset, not a tolerance.** Buyers convert on a ~6-month lag and she says so on camera. That posture — *"I'll be here"* — is structurally unavailable to anyone pivoting next quarter. It is the actual mechanism, not a personality trait.

**Fourth: market to the doubt, never against the substitute.** Her buyer's anxiety attached to borrowed contracts long before it attached to ChatGPT. Positioning built against the current substitute expires; positioning built on the durable doubt survives.

## The capability

**What it is.** Twelve workflows in three tiers (foundation / practitioner / stacking), each with an Output Schema and a Quality Gate, backed by `genius.md`, four references, twelve born-v2 execution prompts, and an `AGENT.md`. The mechanism is a sequenced launch: ~1-month teaser ramp → ONE live webinar → weaponized replay → 4-day cart, with a show-up engine and a designed non-scalable layer bolted to the founder's calendar.

**When to reach for it.** A product that **already exists** at **$1,000+**, a list (or paid path to registrations), and a founder willing to be personally present. That combination is the tell.

**When NOT to.** Net-new or unvalidated product → `/pat-flynn-validate-with-one-person` first; this model relaunches, it does not launch. Broken offer → `/offer-redteam` first; no launch mechanic repairs a bad offer. Sub-$500 → take only `/sv-subject-line-hero` and `/sv-newsletter-magnet`; the rest fails the Two-Minute Test. Show-rate *diagnosis* → `/jh-show-rate-diagnostics` first, then `/sv-showup-engine` to repair. Eight redirects are written into `SKILL.md`'s "When NOT to Use".

**How to invoke.**
```bash
/sam-vander-wielen                 # front door
/sv-launch-teardown                # a launch already exists → diagnose first
/sv-customer-personality-lock      # starting fresh → who, before what
/sv-subject-line-hero              # cheapest first proof — one email, today
```

**Worked example (from this session).** The behavior-changing proof in `references/skill-system-contract.md` takes a generic webinar open — *"stick around, I have an exclusive offer only for people on this live call"* (rubric level 2: manufactured urgency, nobody turned away, fails the Recognition Test) — and rebuilds it into the consent-then-disqualify open at level 4. The measurable change: the audience types a word, converting passive attendance into granted permission, then the self-costing disqualifier makes the offer something to qualify for.

**Honest edges.**
- **Blind pass NOT run.** The corpus needs verbatim published pieces; the available fetch tool returns summaries, and judging voice against a summary is a false pass. Ships B-tier. Close procedure + the two exact URLs: `extractions/sam-vander-wielen/reference-corpus/README.md`.
- **Single source, no cross-enrichment.** Mechanics she describes only briefly are correspondingly thin.
- **All figures self-reported.** Internally consistent and unusually specific, but unaudited.
- **Proof is a craft delta, not a revenue delta.** No launch has been run end-to-end. No revenue claim is made anywhere in the skill.
- **Compliance**: disqualification and temperament language carry real fair-housing/lending/employment risk. Both workflows flag it; do not port that language into Jen's listing copy without review.

## The scar worth remembering

Auto-captions mangled her surname as **"Vanderland"** consistently across all 2,093 segments — no self-consistency check catches that. The entire skill got built under the wrong slug before the verification gate caught it. A wrong slug is routing poison: `/extract` Extension Mode matches on it, so the next source would have created a duplicate expert forever.

**Rule, now carded:** never take a proper noun from auto-captions; verify expert identity off-source at Phase 1, corroborating on multiple identifiers (domain, product, podcast, publication cadence) — not by re-spelling the surname. Here five identifiers lined up and made the correction certain. Card: `docs/solutions/2026-08-06-auto-caption-proper-nouns-poison-extraction-slug.md`.

Related but distinct: `2026-07-07-transcript-only-extraction-generic-output.md` is about *depth*; this one is about *identity*.

## Composition — options, never a pipeline

| Stack with | What it adds | When it earns its cost |
|---|---|---|
| `/oversubscribed-launch-sales-system` | Priestley engineers demand exceeding supply | When registrations, not conversion, are the constraint |
| `/jh-show-rate-diagnostics` | Diagnosis before repair | Attendance is the presenting symptom |
| `/offer-redteam` | Offer integrity | Always, before a teardown, if the offer is unproven |
| `/icp-deep-dive`, `/avatar-machine` | Base profile | Run first; `/sv-customer-personality-lock` layers temperament on top |
| `/copy-engine`, `/writers-room` | Drafting muscle | Load `references/source-quotes.md` as the voice anchor |
| `/sean-dollwet-kdp-publishing` | Book production | Then `/sv-book-funnel-bridge` turns it into top-of-funnel |

**Composition rule:** Sam owns the launch function. One author per asset — never blend her disqualifier with a scarcity-first pitch in the same script.

## State + next

Branch `claude/vanderland-webinar-launch-forge` (pushed, **unmerged**), based on `b49f407dc`; main has advanced to `c8f605811`. Both regenerated the same registries — **take main's side on every generated file, then regenerate** (`sync_registries` → `mint_menu_wrappers` → `prompt_library build` → `wire_prompt_pointers` → `generate_slash_commands`) and confirm `skill_auditor.py check --skill sam-vander-wielen` still reports 7/7 before committing the merge.

Gates as shipped: skill_auditor **7/7 PASS** · renaissance_audit **0 fail** · verify_skill_system_contract **PASS** · menu parity **12/12**.

Future Sam Vander Wielen material → `/extract` **Extension Mode** against the existing slug. Never a second extraction.
