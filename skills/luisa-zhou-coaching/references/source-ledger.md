# Source Ledger — luisa-zhou-coaching

Ground truth for this skill is a set of six Luisa Zhou YouTube-video transcripts (Merlin AI transcription), each pasted verbatim into a claude.ai conversation and captured in the 2026-07-01 claude.ai export. All six live inside `_archive/claude-export-2026-07-01.tar.gz`, under `claude-export/normalized/conversations/<id>.md`. That archive is not a text file — it was searched with a Python `tarfile` per-member scan (name-fragment match on `luisa`/`zhou`, then full-text scan of every `.json`/`.md`/`.txt`/`.jsonl` member) rather than grep, and sizes below are the actual member sizes recorded by that scan, not estimates.

## Sources Consulted

| # | Video (title as transcribed) | YouTube ID | Conversation file | Size (bytes) | Captured |
|---|---|---|---|---|---|
| 1 | First Coaching Session Structure (3 Steps to Blow New Clients Away) | L1wQZotVmqA | `967f235a-8451-4f78-8829-8f397caff137.md` | 31,946 | 2025-05-07 |
| 2 | Design Your First Coaching Package in 10 Minutes | WD7DDcEGgYs | `90061dbb-d598-4c64-9974-c8d9bbdeef75.md` | 31,050 | 2025-09-27 |
| 3 | Design your first coaching package in 10 minutes (duplicate capture) | WD7DDcEGgYs | `381c07d3-bd50-4c41-a620-217d0073408f.md` | 26,422 | 2025-05-07 |
| 4 | How to Start Your Online Coaching Business TODAY (4 Simple Steps) | AnuPv8Pz-Kc | `03a11a83-418f-46ed-84f3-4e50e1c14d49.md` | 26,022 | 2025-05-07 |
| 5 | How to Start Your Online Coaching Business TODAY (duplicate capture) | AnuPv8Pz-Kc | `83c7a5f4-48a9-46dd-bbf0-7f021d3565e0.md` | 35,294 | 2025-08-10 |
| 6 | Get Insanely Fast at Content Creation (it's so simple) | 6AWyl7OKnrU | `1da08d35-b3b8-4168-8f82-7ef7dd0ff90c.md` | 27,563 | 2025-05-07 |
| 7 | First Coaching Session Structure (duplicate capture) | L1wQZotVmqA | `1592e1e8-8f1c-4224-9f60-f56f442fe933.md` | 33,761 | 2025-08-10 |

Rows 1/7, 2/3, and 4/5 are the same underlying video re-pasted into a second conversation on a different date — used only to cross-check the transcript text was stable, not as independent sources. Not used for this skill's claims (checked, no unique load-bearing content for the current pattern set): `4cedeb8e` (niche-finding video), `bf57e346` (niche-in-one-sentence video), `295335b3`/`4941e3c5`/`296823c3`/`ce178f75`/`e10d064e`/`b6c518dc` (client-acquisition/storytelling videos — a plausible source for a future "getting clients" workflow, not consulted for the current three), `a4bf3c97` (unrelated Coach Cooz LinkedIn strategy — a `luisazhou.com` blog link inside it is what tripped the name-fragment scan), `f12761ef` ("Comprehensive Principles for Injury Rehabilitation" — unrelated, false-positive name match), `4e1a9d26`/`c91c74d9` (Coach Cooz ad strategy, unrelated), and `claude-export/raw/batch-0001/conversations.json` (867MB master raw export containing all of the above pre-normalization — the normalized `.md` files above are the readable form of the same content, so the raw JSON was not separately re-parsed).

## Claim-by-Claim Verification

All patterns and insights currently in `genius.md`, plus the eight new Anti-Pattern items, were checked against the verbatim transcript text (the human-turn transcript paste, not the assistant's downstream MES/KACE extraction commentary in the same conversation, which is a prior AI pass and not primary source). Every claim below is **VERIFIED** — matched to an exact or near-exact quote in a transcript. No claim required an UNCONFIRMED label.

| Claim (genius.md) | Status | Source |
|---|---|---|
| Coach-sulting definition + "why not teach someone how to fish and give them dinner, too?" | VERIFIED | `967f235a`, 7:33–8:43 |
| Coach-sulting reframed as anti-scam positioning ("people are going to think that you're a scam") | VERIFIED | `03a11a83`, 1:39–1:65 |
| Welcome questionnaire: 2-business-day rule, favorite questions, "you are so mean" origin story | VERIFIED | `967f235a`, 0:26–4:24 |
| The Three S's (Share / Strategy / Specific actions), health-coach sugar-cleanse example | VERIFIED | `967f235a`, 4:34–7:13 |
| Teach clients to be coachable, "I'm here to teach you how to fish," "help them to help you help them" | VERIFIED | `967f235a`, 9:04–10:02 |
| Boundaries: channel/frequency/response-time, checking messages once a day, burnout warning | VERIFIED | `967f235a`, 11:05–12:43 |
| Experience Is the Qualification: Excel origin, "if you're in one, you already know," routing question | VERIFIED | `03a11a83`, 0:14–3:40 |
| Pick a Start, Not a Forever: gray sofa / "next Facebook" / two wasted years / "taking imperfect action beats perfect planning" | VERIFIED | `03a11a83`, 3:53–6:38 |
| 3-Month container structure, weekly calls + async channel, reverse-engineered milestones | VERIFIED | `90061dbb`, 0:36–4:37 / `03a11a83`, 6:48–8:33 |
| $1,500 price point, $5,000 first client (hourly formula), 30 rejections, "lowest price I'd offer without resenting my clients" | VERIFIED | `03a11a83`, 9:21–9:58 |
| Free Taster Session, Rich Litvin's *The Prosperous Coach*, 2-hour → 30–60 min compression, "You have helped me so much for free. How can I hire you?" | VERIFIED | `03a11a83`, 12:40–14:56 |
| Systematize knowledge in plain Google Docs; first clients' docs → $3,000 group program | VERIFIED | `967f235a`, 10:04–10:46 |
| Rapid Content Engine: story bank (*Storyworthy*), Elizabeth Gilbert quote, Hook/Meat/CTA, Stephen King / Dan Kennedy references, 45-min timer + 5-min warning, "good enough is good enough," draft-out-loud rule | VERIFIED | `1da08d35`, 0:00–10:25 |
| "Being a great coach is not about knowing all the information in the world. It's about knowing how to customize what you know for your client." | VERIFIED | `967f235a`, 0:38–0:48 |
| "Sales only feel scary until after you've done it… another day, another no." | VERIFIED | `03a11a83`, 11:37 (another day, another no) / 11:53 (sales only feel scary) |
| "Until you make that first sale, you do not have a business." | VERIFIED | `03a11a83`, 10:48–10:53 |
| Abstract-offer tangibility test ("what are the tangible changes in their day-to-day?") | VERIFIED | `03a11a83`, 4:46–5:03 |
| SKILL.md: "10+ years coaching," "3,500+ coaches trained," "five-figure private coaching fully booked for years" | VERIFIED | `967f235a`, 3:41–3:43 (10 years) + `03a11a83`, 3:07–3:12 (3,500+) + `967f235a`, 8:17–8:21 (five-figure/fully booked) |
| Anti-Pattern items (8, listed in genius.md) | VERIFIED | See timestamp citations inline on each bullet |

## Labels Used

- **VERIFIED** — matched to an exact or paraphrase-stable quote in a primary transcript, confirmed by direct file read (not grep-only).
- **LIKELY** — not used in this pass; nothing fell in this tier.
- **UNCONFIRMED** — not used in this pass; nothing in the current genius.md/SKILL.md content lacked a locatable transcript match.

No sources were reported as absent/missing without a file read confirming the negative — the four false-positive name-match files (`a4bf3c97`, `f12761ef`, `4e1a9d26`, `c91c74d9`) were opened and checked, not assumed irrelevant from filename alone.
