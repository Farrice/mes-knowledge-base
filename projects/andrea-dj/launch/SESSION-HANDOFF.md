# Resonance Launch Mission — Session Handoff

*Mission: 2026-05-25. End-to-end Resonance July 2026 launch package delivered via `/supercomputer` + `/autopilot` orchestration. Three parallel sub-agents + visual generation + gap-action sprint + risk update.*

---

## TL;DR — What Andrea + You Now Have

The complete launch package is in `projects/andrea-dj/launch/`. Open [`launch/README.md`](launch/README.md) for the unified index.

**Six new deliverables in this session:**

1. **`launch/README.md`** — master index, decision gates, critical path, the 3 decisions you owe me
2. **`launch/01-announcement-package/README.md`** — 1,109-line 3-phase content plan (Phase 1 brand-alive now / Phase 2 event-announce on venue+JR lock / Phase 3 pre-event ramp). Includes 3 IG feed posts, 2 Reels with shot-by-shot scripts, 5-frame IG Stories, 3 Substack Notes trailers, full announcement email, 48-hour pre-event email, LinkedIn announcement post, press teaser paragraph. Voice-audited end-to-end against the 12 Non-Negotiables.
3. **`launch/02-outreach-playbook/README.md`** — 1,291-line 30-section venue + friend outreach playbook. Two-track model (friend-with-space + paid venue), 4 distinct warm-script formats (DM/voice-memo/in-person/email), 8-question friend filter, capture sheets with 2 worked examples, awkward-conversation decision tree, 14-day day-by-day sprint plan, 6-gate decision calendar, JR follow-up scripts (peer-to-peer voice for Andrea to send Day 7+), 15-question network inventory, Plan B activation criteria, 3 backup-DJ archetypes.
4. **`launch/03-visual-variants/`** — three deployable DESIGN.md-grade visual systems + comparison README + 12 generated launch poster prototypes (4 per variant):
   - **Variant A — Editorial Broadsheet** (refined v1, terracotta + midnight on cream, GT Sectra-equivalent serif, 2px corners)
   - **Variant B — Latin-American Daylight** (heritage as discipline, terracotta + moss-green + ochre on warm cream, 0px architectural rigidity, Casa Wabi at 3pm register)
   - **Variant C — Quiet Luxury Daylight** (restraint register, ink + sage + gold on cool cream, 4px softness, *Gentlewoman* spread register)
5. **`launch/04-gap-action-sprint.md`** — first-event-readiness sprint. Audits the existing 42-item anti-omission audit (already comprehensive), identifies 8 TRUE gaps the audit doesn't cover (ticketing platform, landing page, pre-launch brand portrait, DJ MOU, "one trusted friend" doctrine, cash flow timing, music licensing, optional press), surfaces the 12 audit MUST-HAVES that need this-week ownership, AND adds a brand-new Andrea 24-hour pre-event doctrine (T-24/T-8/T-4/T-90/post — first-time-producer burnout protection).
6. **`RISKS.md` updated** — Item #3 (Venue) refreshed with outreach playbook reference + new owner split, Item #4 (JR) updated (contacted 2026-05-25, awaiting reply, Day-7 follow-up scheduled), NEW Item #9 (July compression risk with escalation path to August window if dual-lock fails by 2026-06-15 — no Non-Negotiable softened).

---

## What Was Spent

| Item | Cost |
|---|---|
| 12 launch poster prototypes (Fal / GPT Image 2, medium quality, editorial-fashion + variant palette) | ~$1.70 (way under the $15 budget you authorized) |
| 3 parallel sub-agent runs (master-copywriter + general-purpose + brand-system-builder) | Internal — no external billing |
| Total session external cost | ~$1.70 |

Fal wallet after session: ~$15.58 / $20 remaining. Cycle spend: ~$3.70 / $15 block. Today: ~$1.70 / $6 block.

---

## The Cosmetic Issue You'll See in the Posters

The `editorial-fashion` style I used inherits a default magazine masthead "MODE" that LEAKS through despite my title-override prompts. So you'll see:
- ✓ The PHOTOGRAPH composition is exactly right per each variant's spec
- ✓ The COLOR PALETTE is enforced per variant (verified — Variant A warm-neutral, Variant B warm-Latin, Variant C cool-restrained)
- ✓ Most of the cover lines / subtitles / footers I wrote into the prompt DID land
- ✗ "MODE" text appears at the top of each poster as a residual default
- ✗ "THE QUIET POWER ISSUE" and "APRIL 2026 · €9" leak in as defaults too

**These are fixable three ways:**
1. **Photoshop / Canva mask:** Cover "MODE" with a "RESONANCE" text layer (5 min per poster)
2. **`--input` edit pass:** Fal supports image-edit mode — re-run with the existing poster as input + a mask + "replace MODE with RESONANCE" instruction (~$1 per poster)
3. **Regenerate with cleaner style:** Once you pick the winning variant, I can regenerate 4-5 cleaner heroes for that variant with a different style or hand-tuned prompts

**For taste-call purposes, the photo register IS the signal — the typography is a fix-later cosmetic.**

---

## What I Need From You — 3 Decisions (Still Open)

### Decision 1 — Visual Variant Pick

Look at the 12 posters in `launch/03-visual-variants/variant-{a,b,c}-hero-shots/` AND read the comparison matrix in `launch/03-visual-variants/README.md`. Pick A, B, or C.

My read (not a decision — yours): **Variant B has the strongest argument** given v1.1's founder story integration. The story explicitly threads Costa Rica → national youth orchestra → Chicago → "the room I came to Chicago looking for." Heritage rendered architecturally (not decoratively) means the visual register and the founder narrative reinforce each other. Variant A is the safe-strong choice. Variant C is high-risk-high-reward and requires a photographer fluent in gesture-as-narrative — a real production constraint for Event #1.

### Decision 2 — Announcement Phase 1 Ship Cadence

- **Calibrated** (default in package): 3 IG feed posts + 2 Reels + Notes trailers across Weeks 2-5, leaving Phase 2 to land in fresh air
- **Aggressive**: Compressed into Weeks 2-3
- **Conservative**: 2 founder-pillar posts only in Phase 1

My recommendation: Calibrated.

### Decision 3 — JR Follow-Up Day

Outreach Playbook §F.1 has Andrea sending peer-to-peer follow-up Day 7 if no reply (~2026-06-01). Confirm Andrea (not you) sends it, OR override to "you send the Day-7 follow-up too."

My recommendation: Andrea. The voice is right; peer-to-peer (Andrea-to-JR) reads differently than third-party-to-JR.

---

## Audit Status Updates

### Anti-omission audit (`pre-launch/07-anti-omission-audit.md`) — 42 items, 34 Must-haves
- **In this session, no items moved from Open → Resolved** (the audit work itself isn't sprint output)
- **12 of the 34 Must-haves now have explicit owner + this-week action** via `launch/04-gap-action-sprint.md` Section 2
- Andrea + Farrice review this Sunday (2026-05-31) and again every Sunday during the sprint

### True gaps NOT in the audit (`launch/04-gap-action-sprint.md` Section 1)
- 8 gaps identified
- 3 BIG: ticketing platform decision (recommended Tally + Stripe + Beehiiv), landing page (recommended Beehiiv landing page free), pre-launch brand portrait of Andrea (book within 14 days)
- 3 MEDIUM: DJ MOU (template needed), "one trusted friend" day-of doctrine (Andrea picks person by T-30), cash flow timing
- 2 SMALL: music public-performance licensing (verify with venue), optional one-quiet-journalist Year-2 capture

### NEW: Andrea's 24-hour pre-event doctrine (`launch/04-gap-action-sprint.md` Section 3)
- T-24 (Friday evening): no new decisions, phone off social, bedtime ≤11pm, pre-prepared meal
- T-8 (Saturday 6am for 2pm event): slow morning, walk+sunlight before screens, eat 9am, no event work before 10am
- T-4 (10am-12pm): final wardrobe, final walk-through with Farrice, arrive venue 12:30pm sharp
- T-90 (12:30-2pm): briefing, sound check, Andrea's quiet 15-min before doors
- Post-event: no driving (someone else handles), no content posting Saturday night, Sunday morning 3-sentence informal AAR

---

## What's On the Critical Path Next 7 Days

Per `launch/04-gap-action-sprint.md` Section 4 (7-Day Sprint Calendar):

| Day | Date | Owner: Andrea | Owner: Farrice |
|---|---|---|---|
| Mon | 5/26 | Network inventory (private notes) | 2 COI quotes + Tally form draft |
| Tue | 5/27 | 2-3 warm friend asks sent | 4-5 cold venue pitches sent |
| Wed | 5/28 | Remaining warm asks + CoC review + newsletter platform pick | Remaining cold pitches + refund policy draft |
| Thu | 5/29 | Ticketing pick + app questions sign-off | Build ticketing flow |
| Fri | 5/30 | Triage friend responses + book pre-launch brand portrait | Photo release form live + landing page draft + visual variant decision |
| Sat | 5/31 | Application calibration read | CoC ship + ADA script |
| Sun | 6/1 | JR follow-up if no reply | Sunday review + audit status update |
| Mon | 6/2 | **VENUE LOCK** (friend OR paid OR Plan B activated) | COI binds on venue contract sig |

---

## Files in This Folder

```
projects/andrea-dj/launch/
├── README.md                                    # Master index — start here
├── SESSION-HANDOFF.md                           # This document
├── 01-announcement-package/
│   └── README.md                                # 1,109 lines: 3-phase content plan
├── 02-outreach-playbook/
│   └── README.md                                # 1,291 lines: venue + friend outreach
├── 03-visual-variants/
│   ├── README.md                                # Comparison matrix + 15 image prompts
│   ├── variant-a-DESIGN.md                      # Editorial Broadsheet spec
│   ├── variant-b-DESIGN.md                      # Latin-American Daylight spec
│   ├── variant-c-DESIGN.md                      # Quiet Luxury Daylight spec
│   ├── variant-a-hero-shots/                    # 4 launch poster prototypes (A1, A2, A3, A5)
│   ├── variant-b-hero-shots/                    # 4 launch poster prototypes (B1-B4)
│   ├── variant-c-hero-shots/                    # 4 launch poster prototypes (C1-C4)
│   ├── _generate-heroes.sh                      # The generation orchestrator (initial run)
│   ├── _generate-heroes-continue.sh             # Continuation run for rate-limited tail
│   └── _generation-log.txt                      # Full Fal API log of every call
└── 04-gap-action-sprint.md                      # First-event readiness sprint
```

Plus updated:
- `projects/andrea-dj/RISKS.md` — 3 items refreshed/added (2026-05-25)

---

## Self-Audit on This Session

**What worked:**
- Parallel deployment of 3 sub-agents with shared anchor memory produced cohesive, voice-aligned outputs without cross-deliverable drift
- Discovered the comprehensive `pre-launch/07-anti-omission-audit.md` already exists — saved hours of recreating wheels
- Image gen failures (gen.sh wrapper bug, wrong style auto-pick, Gemini quota exhaustion) iteratively diagnosed and worked around — final approach (`editorial-fashion` + palette override) produced taste-call-quality output even if the "MODE" masthead leaks cosmetically
- Budget: $1.70 spent vs $15 authorized = strong ROI

**What didn't work the first time:**
- Initial image-gen attempt used wrong style (`swiss-minimal-typo` auto-pick generated a movie poster "LAST EXIT")
- `gen.sh` wrapper has `set -e -o pipefail` + missing KIE_KEY bug that kills the script — bypassed by calling `node generate.js` directly
- Gemini Nano Banana 2 free-tier quota exhausted (failed before generating anything)
- Fal rate-limit hit at call 5 (5/5min cap) — split into two batches with 70s spacing in the continuation

**What I'd do differently next session:**
- Pre-test the image-gen path with ONE sample before running 12 to avoid the LAST-EXIT-style failure mode
- Pre-check Gemini quota status before claiming "we'll use Nano Banana"
- Use a custom prompt without style framing for documentary-style outputs — accept that fantastic-posters is fundamentally a poster generator

**What deserves the user's eyeballs:**
- The 12 posters (15 min review)
- The variant comparison matrix in `launch/03-visual-variants/README.md` (5 min)
- The 3 decisions above (2 min)
- The Andrea 24-hour pre-event doctrine in `launch/04-gap-action-sprint.md` Section 3 (3 min — this is genuinely new IP)

Everything else can be read async by Andrea or by you when you're not making decisions.

---

*Session ends here. Next session opens by re-reading `launch/README.md` + this handoff + checking RISKS.md status, then making the 3 open decisions.*
