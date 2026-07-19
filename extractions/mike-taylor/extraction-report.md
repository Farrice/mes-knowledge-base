# Mike Taylor — Synthetic Customer Research: Extraction Report

## Source

- **Primary**: "This AI Prompt Gets You Customer Insights in 5 Minutes (Free Tool)" — *Marketing Against the Grain* (Kieran Flanagan + Kipp Bodnar, HubSpot Podcast Network), YouTube `2f7pUdn1miE`. Guest: **Mike Taylor**.
- **Duration**: 33:13. **Fidelity**: WATCHED — full native-caption transcript (6,916 words, 918 segments) + 20 extracted frames spanning 00:00-32:51, read directly with the `Read` tool (not transcript-only).
- **Secondary (enrichment, third-party attribution — LIKELY band)**: `app.vexpower.com` course page, `brilliantexperience.com` interview, `twosetai.com` insight piece, `every.to` podcast writeup, `duckduckgo.com` search corroboration for Ask Rally / Vexpower identity.
- **Recall card**: `ce789f0b-9c63-4775-b0b7-c44edad29e23` (saved 2025-09-03) — the near-lost trace that triggered this forge.

## Expert Identification (VERIFIED)

**Mike Taylor** — co-author, O'Reilly's *Prompt Engineering for Generative AI* (with James Phoenix); creator of Vexpower marketing-education courses (450,000+ students across Vexpower/Udemy per secondary corroboration); co-founder of **Ask Rally** (`askrally.com`), a "virtual audience simulator for synthetic market research" — the exact app category Kieran speculates about mid-episode, confirming Taylor built the thing he was demoing a prototype of on the show. Introduced on-air by the hosts as "an expert in all things prompt engineering [who] actually wrote the book on prompt engineering." Not the transcription tool — confirmed by video title, channel (Marketing Against the Grain / HubSpot Podcast Network), on-screen identity, and cross-source corroboration.

## Fidelity Achieved

**WATCHED** (video-context tier). 20 frames extracted (scene-change selection across the full 33-min runtime); two frames delivered genuinely visual-only exemplars not recoverable from audio alone:
- `frame_0041` (t=09:43): the actual NotebookLM screen — "Vexpower Consumer Transcripts," 13 sources, participant name **"Rhys Fisher"** visible in the source list. Confirms his own company name and a real interviewee, absent from the spoken transcript.
- `frame_0049` (t=20:56): the actual ChatGPT output screen — the 10-item "Demographic Personas" list (Small Business Owner, Marketing Manager, Startup Founder, Sales Executive, Freelance Digital Marketer, Nonprofit Director, Enterprise IT Manager, Solopreneur, Customer Success Manager, Content Creator) and the start of "Individual Persona Responses" ("1. Small Business Owner: 'I prefer 'Grow without the guesswork' because it addresses my need...'").

No cost gate was hit on `fetch-video-context.py`; the >10-min auto-skip was deliberately overridden per the extraction brief (`--max-duration 2400`).

## Genius Patterns (17 — see `skills/mike-taylor-synthetic-research/genius.md` for full mechanism writeups)

All patterns below carry verbatim timestamped quotes in the genius.md and source-quotes.md files. Frequency = how many distinct moments in the 33-min episode reinforce the pattern (not a source-count across other Taylor material).

1. Roleplay-Then-Aggregate core mechanism (freq: 3 — stated, demonstrated, re-explained at 20:26 callback)
2. "Joint Anonymous Answer" aggregation instruction (freq: 2 — exact phrase + demonstrated result)
3. Two-Step Prompt Architecture: Scene-Set then Ask (freq: 2)
4. Product-Category Substitution for unknown brands (freq: 1, explicit caveat)
5. Persona list as a targeting-discovery byproduct (freq: 2)
6. Grounding Ladder — three accuracy tiers (LIKELY, secondary source: TwoSetAI)
7. Self-Consistency Ceiling (LIKELY, secondary source: TwoSetAI)
8. Distribution vs. Individual Accuracy split (freq: 1 primary + LIKELY secondary elaboration)
9. Sycophancy/Bias Trap (LIKELY, secondary source: TwoSetAI)
10. The "Vegan Problem" thread contamination (LIKELY, secondary source: TwoSetAI)
11. Real-Transcript Roleplay / Voice-of-Customer engine (freq: 3, VERIFIED — visual + spoken)
12. Sense-Check Before the Real Ask (freq: 1, VERIFIED)
13. Latent-Demand Mining Prompt + drill-down loop (freq: 2, VERIFIED)
14. The "Secret Source" Differentiation Principle (freq: 1, VERIFIED)
15. Personalization Cascade — segment to individual, insight not final copy (freq: 1, VERIFIED)
16. Research-Stack Handoff — tool-to-strength routing (freq: 2, VERIFIED)
17. "99 Questions You Can't Afford to Ask" triage logic (freq: 1, VERIFIED — this is the line `buyer-council.md` already quotes)

## Hidden Knowledge (6 items)

- Non-text data (video/podcast transcripts) is comparatively under-represented in LLM training data vs. blog/text — repurposing your own recorded calls is a higher-differentiation move than prompting on text alone.
- The workflow (notes from calls → blog posts) is not new; AI removes what was previously manual editorial labor, it doesn't invent the technique.
- Voice-of-customer teams are traditionally an enterprise-only function (HubSpot-scale); recording + roleplay democratizes that capability for any company that records its calls.
- "Directionally correct" is the actual bar for a copy decision, not statistical significance — but AB-testing is still the closing step, never skipped.
- AI-visibility measurement (his "AI Search Creator" tool) reframes brand-awareness research itself — counting model-output mention frequency approximates unaided awareness "within a margin of error" of a real study.
- He treats winning outputs as disposable/replicable, not IP to protect — releasing the "Grow without the guesswork" tagline live on air signals the tool is positioned as a research/insight instrument, not a copy-generation moat.

## Hall of Fame Exemplars (5)

1. HubSpot headline test — "Grow better with HubSpot" vs "Grow without the guesswork," 10 personas, ~60/40 aggregate split, individual dissent preserved by role.
2. Vexpower/NotebookLM real-transcript panel — 13 sources incl. "Rhys Fisher," tested a course idea against real recorded customers without recontacting them.
3. On-screen persona list + individual responses (frame_0049) — the actual artifact, not a description of one.
4. Ask Rally's "lightsaber kit at 2am" hallucination (LIKELY, secondary) — the canonical individual-vs-aggregate accuracy illustration.
5. The $8-12K / weeks-to-months focus-group cost frame, cross-checked via Google Deep Research live on the show ("average company does about two focus groups a year").

## Signature Moves (8)

Set-the-scene-then-ask · close with the exact joint-anonymous-answer phrase · category-substitution for obscure brands · ground upward before trusting upward · isolate personas pre-aggregation · mine the angle, write the copy yourself · route each AI assistant to its strength · drill down one level on the single most interesting latent-demand finding.

## Cross-Pollination Candidates

- **Geoff Woods (Pattern 6/8, stakeholder simulation + anti-sycophancy)** — Taylor's Sycophancy/Bias Trap is the same failure mode Woods' Pattern 8 names; both independently arrive at "cast the panel adversarial, never agreeable by default."
- **Jeremy Haynes cold-offer stakeholder handshake** — the dissent-preservation discipline in `haynes-handshake-geoff-stakeholder.md` and this skill's Distribution vs. Individual Accuracy split are structurally the same guardrail against consensus-averaging.
- **Corey McClain persona engineering** — McClain's narrative-prose persona depth is the natural "Tier 2→Tier 1" grounding upgrade path when a Taylor panel needs more than an 80-120 word card.

## What This Extraction Adds That Buyer-Council Didn't Already Have

`buyer-council.md` TRIAGE mode already carries Taylor's surface mechanic (10 personas → individual → joint-anonymous-answer) and the $8-12K boundary line. This extraction goes deeper into research design and validity theory buyer-council never touched: the three-tier grounding ladder, the self-consistency accuracy ceiling, the vegan-problem thread-contamination fix, the distribution-vs-individual accuracy split, and the tool-to-strength research-stack sequencing. Buyer-council remains the fast operational front door; this skill is the deep source it should cite when a call requires more than a 5-minute triage.
