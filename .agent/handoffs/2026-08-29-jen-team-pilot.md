---
thread: clients
status: active
resume_hint: Jen-Team Pilot pickup: all assets shipped+approved; refine carousels / demand pass / Jay interview; Farrice pitching today
branch: main
pin: false
---

# Handoff — jen-team-pilot (fresh-session resume)

## Purpose
30-day trial: sell the Listing Launch Kit ($200 founding, standard $450) to 3 agents on Jen's team; proof-of-concept that pulls Jen back onto her own system. Target $300-600; needs two yeses. HARD SCOPE RULE: productized kit, never a content agency.

## Current State
All shipped, all living in `_active/clients/jen-team-pilot/`:
- `OFFER-BRIEF.md` — offer, terms, pitch DMs, 6-step delivery run, 30-day plan, kill criteria, objections (incl. VA positioning: team pays a VA ~$1,200-1,400/mo — position caliber jump, never knock the VA, takeover only on their initiative)
- `PITCH-DAY.md` — today's run of show (Jen show-and-ask script + 3 DMs + checklist)
- `AGENT-INTAKE.md` — Part A brand intake (once per agent → brand card) + Part B listing intake (per kit)
- `agents/jen-brand-card.md` — Jen dual-lane tokens scraped from live IG (@_jiing warm editorial + House Sellers quiet-luxury print) + approved v2 carousel design system
- `demo-kit/` — sample kit (fictional 1234 Hazeltine, artifact a178e2f1) in Farrice's Premium Minimal brand
- `poc-carousels/` — 12-slide dual-lane carousel canvas (artifact fa99084f, Claude Design editor, per-slide PNG export; `gen_slides.py` regenerates; `CLAUDE-DESIGN-HANDOFF.md` = master prompt + copy deck for the desktop app; VERDICT: good)
- `PARTNER-BUNDLE.md` — Jay (@justjaysunfilms) video bundle thesis, tier sketch (numbers UNCONFIRMED), 30-min conversation agenda; OPTION not dependency; craft skill at `skills/jay-sun-films-video-craft/SKILL.md` (partial — interview gaps listed)
- Harness: `skills/mike-sherrard-realtor-branding/workflows/04-market-demand-carousel-system.md` (extracted from his Claude Design video — demand research → editorial design contract → carousel grammar)
Verdicts logged: offer brief good; carousels v1 "like framing, elevate design" → v2 approved good. Fair-housing lint PASS on everything. Missions logged in `.agent/missions.jsonl` (jen-team-pilot-offer, jen-poc-carousels).

## Do-NOT-Rebuild
The offer, sample kit, carousels, intake, brand card, design system, and Sherrard workflow are DONE — refine in place, never regenerate from scratch. Carousel edits: edit `poc-carousels/gen_slides.py` → regenerate → re-seed via design-skill helper → republish SAME artifact URL (fa99084f). B4 stays "have covered" (factual). Copy deck is final unless Farrice says otherwise.

## Remaining Priority
Farrice's physical moves: export 12 PNGs to phone → Jen show-and-ask (permission + gift carousels) → 3 DMs → first $200 → run intake + first kit. Session work if asked: refine carousels per Jen's reaction, run SFV demand pass for kit #1, Jay interview → complete his skill + lock bundle tiers.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-08-29-clients.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
