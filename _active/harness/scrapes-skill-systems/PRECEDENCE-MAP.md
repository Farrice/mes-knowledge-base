# Scrapes Skill Systems — Precedence Map (LIVING)

*Owner: Farrice. Built 2026-09-02 from a mechanical overlap scan of the 36 installed skills against `skills/`, `.agent/workflows/`, `execution/`, and the three `extractions/agentic-os-*` folders (which are captures of Simon Scrapes' own two videos, so the imitations they seeded are what this map retires or keeps). Update in place as blind bars land.*

## The verdict scale

| Verdict | Meaning |
|---|---|
| **FLIP NOW** | Scrapes skill becomes the working tool for this job. Ours stays on disk, gets `routing: long-tail` or a pointer, never deleted. |
| **TEST FIRST** | Same input through both; Farrice taps the winner; then flip or keep. |
| **KEEP OURS** | Our version carries expert depth or canon the Scrapes skill does not; Scrapes skill stays available as a utility. |
| **DO NOT USE** | Conflicts with a binding rule (sends stay human; Apify retired) or needs a service we don't run. |

## Where the line actually falls

Scrapes wins on **mechanized pipelines with real code**: video clip selection and face-aware reframing, caption burning, transcript-to-article, slide rendering, image search, screenshot annotation, diagram generation. Our equivalents in those spots are prose workflows or thinner scripts.

Ours wins on **expert depth in Farrice's own domain**: positioning (Dunford + Proof-to-Market canon), ICP (McRaney deep canvass + the battle card), brand voice (30,606-message register atlas), research with receipts (Gemini Deep Research + zeitgeist engine), anti-slop (the ban bank is canon), extraction (MES 3.0 is the repo's core competence).

The bridge: Scrapes skills read `brand_context/`. We populated it from our canon. So the Scrapes pipelines run on our depth without either side being edited.

## The 36, one row each

| Scrapes skill | Job | Nearest ours | Verdict | Why |
|---|---|---|---|---|
| 00-social-content | 7-scenario orchestrator → post + carousel images | `social-content-studio`, `content-orchestrate`, Jen carousel engine | **TEST FIRST** | Their carousel mechanics (designer audits, template pools, real logos) beat ours; hook craft and voice must come from brand_context. Blind bar #1. |
| 00-longform-to-shortform | YouTube → clips → reframe → captions → render | `video-studio`, `edit_bay.py`, `transcribe_local.py` | **FLIP NOW (publish off)** | Edit bay has no face tracking or clip scoring. Run with the post step disabled; his VO only, no TTS. |
| 00-slides | topic/outline/transcript → HTML deck + PDF | `presentation-build` | **FLIP NOW** | Ours is a prose workflow; theirs renders. Briefs and readouts stay on the Ink + Steel Blue readout OS. |
| 00-youtube-to-ebook | video → fact-checked editorial PDF | `fetch-transcript.py` + `grounding-pass` + `pdf` | **FLIP NOW** | No end-to-end equivalent. `prose_classifier.py check` before ship. |
| meta-skill-creator | create/modify/eval skills | `skill-creator`, `/extract`, `/extract-forge` | **KEEP OURS (test evals)** | Extraction is our moat. Their eval/benchmark mode is worth a look; creation stays MES 3.0. |
| meta-skill-system-creator | chain skills into installable packages | `source-to-skill-system`, `skill-forge`, `plugin-forge` | **KEEP OURS** | Borrow the PACKAGE.yaml + install.sh pattern if we ever ship kits. |
| mkt-brand-voice | build voice profile (4 modes, schema JSON) | `voice-os`, `voice-document`, VOICE-CARD | **KEEP OURS as source; theirs as adapter** | brand_context is populated from our canon. For client brands (Jen, Gigi, Andrea) their URL/folder import is worth a TEST. |
| mkt-content-analytics | pull post performance via Zernio | `log_performance.py`, dakota audit | **DO NOT USE** | Needs Zernio. |
| mkt-content-repurposing | one piece → 8 platform-native posts | `atomize`, `multi-format-repurposing-engine`, `content-remix` | **TEST FIRST** | Same job; theirs is more mechanical, ours carries platform dials. Blind bar #3. |
| mkt-icp | build/refine ICP → icp.md | `icp-build`, `icp-deep-dive`, battle card, dossier | **KEEP OURS** | Ours is identity-level and verified. Their icp.md is the exchange format only. |
| mkt-longform-article | transcript → magazine editorial | `nonfiction-outline-architect` | **FLIP NOW** | Nothing of ours does transcript-to-feature end to end. Voice via brand_context; classifier before ship. |
| mkt-positioning | 3–5 angles → positioning.md | `april-dunford-positioning`, Proof-to-Market OS, offer wargame | **KEEP OURS** | Positioning is canon and ratified; do not regenerate. |
| mkt-short-form-posting | transcribe → titles/hashtags → post | `video-studio` package stage | **DO NOT USE for posting; package generation only** | Sends stay human. |
| mkt-visual-identity | tokens.json + templates from references | `design-md-extract-*`, `design-md-synthesize` | **FLIP for the pipeline** | 00-social-content requires its tokens.json and approved templates. Feed it `parallax-design-system/DESIGN.md`. Farrice drives the approval gates. |
| mkt-youtube-content-package | title/desc/keywords/timestamps/thumbnails | `video-studio` | **FLIP (publish off)** | Package generation is better than ours; the Zernio post step stays off. |
| str-trending-research | last-30-days trends across Reddit/X/web | `zeitgeist_engine.py`, `research.py`, `deep-research-os`, `social_pulse.py` | **KEEP OURS** | Ours carries receipts and the factual veto. Theirs wants XAI/Groq keys we don't hold. |
| tool-fact-checker | structured claim verification | `grounding-pass`, `claim_audit.py`, `claim_risk_scan.py` | **TEST FIRST as second pass** | Ours remains the veto. Their pipeline mode could catch what ours misses. |
| tool-humanizer | strip 50+ AI tells, voice-match mode | `prose_classifier.py`, ban bank, `slop-check` | **TEST FIRST (ours stays the gate)** | Ban bank is canon. Their deep mode reads voice-profile.md, so it could replace hand rewrite passes. Blind bar #2. |
| tool-image-search | credential-free stock/meme search | none | **FLIP NOW** | Gap filled. |
| tool-linkedin-scraper | fetch LinkedIn posts via Apify | `apify_client.py` | **DO NOT USE** | Apify retired 2026-08-27. |
| tool-pdf-generator | markdown → clean PDF | `pdf` skill | **FLIP NOW for plain docs** | Readout briefs keep the readout OS. |
| tool-publisher | publish via Zernio | `publishable_copy_guard.py` | **DO NOT USE** | Sends stay human. Our guard still runs on outbound copy. |
| tool-screenshot-annotator | circles/highlights on screenshots | none | **FLIP NOW** | Gap filled; teardown assets. |
| tool-transcription | WhisperX, word-level JSON | `transcribe_local.py` | **FLIP inside the video pipeline; TEST standalone** | Word-level JSON is what caption burning needs. |
| tool-video-screenshots | key-moment frames | `video-frame-ledger`, `video-visual-ocr` | **KEEP OURS for study; theirs inside pipelines** | Our ledgers go deeper for extraction work. |
| tool-video-upload | HandBrake compress + upload | `edit_bay.py` transcode | **DO NOT USE upload; compress is fine** | Upload is a publish step. |
| tool-web-screenshot | multi-backend page capture | `design-md-extract-from-url` Playwright | **FLIP NOW as utility** | Playwright already installed. |
| tool-youtube | channel list / transcript / metadata | `fetch-transcript.py`, `youtube-video-context-analysis` | **FLIP for channel + metadata modes** | Ours only fetches transcripts. Channel mode needs YOUTUBE_API_KEY. |
| tool-zernio-social | post to 12+ platforms | none | **DO NOT USE** | Sends stay human. |
| vid-clip-extractor | face-aware 16:9 → 9:16 (OpenCV DNN) | `edit_bay.py` presets | **FLIP NOW** | Edit bay has no face tracking. Extend edit_bay to call it. |
| vid-clip-selection | 5-category clip scoring from transcript | `video-studio` rough cut | **FLIP NOW** | No scoring model of ours. |
| vid-ffmpeg-edit | burn ASS captions + PNG overlays | `edit_bay.py` | **FLIP NOW** | Word-level phrase captions with brand highlight color. |
| viz-excalidraw-diagram | Excalidraw JSON diagrams | none | **FLIP NOW** | Gap filled. |
| viz-frontend-slides | branded HTML decks, 20 principles | `presentation-build` | **FLIP NOW** | Paired with 00-slides. |
| viz-hyperframes | HTML/GSAP → MP4 motion graphics | `video-studio` HyperFrames stage | **TEST FIRST** | Same engine; theirs ships a composition library. Likely flip. |
| viz-image-gen | 6-element framework, GPT Image / Gemini | `banana-pro-director`, `gpt-image-2-director`, craft-map masters | **TEST FIRST (craft gate binding)** | Our masters are the craft floor. Their framework can wrap execution. Cost gate applies. GPT Image needs OPENAI_API_KEY (not on file); Gemini path works today. |

## Craft-room routing (Farrice, 2026-09-02: "blend, don't ignore Luke and the other copywriters")

The Scrapes pipelines own the **machinery**: scenario detection, research gathering, slide arc, visual planning, rendering, humanizer pass. At the copy seams they hand off to **our pens**, never to their own generic prompt:

| Seam in the Scrapes pipeline | What it wants | Who actually writes it |
|---|---|---|
| Phase 5.3a hook (`carousel-first-slide-copywriting.md`) | a formula (value inversion, numeric absurdity, common-sense betrayal, threatened identity) + a mechanism (curiosity gap, expectation inversion, world collision) | **Alyssa Stalker hook-reframe** (Topic + Who + Lens) for placement, **Luke Iha vicious-hooks** (consequence first, open loop, Germanic words, stakes) for grip; the Scrapes formulas are the shape check. For Farrice's own brand: VOICE-CARD dial + Luke Iha; Georgi/Cole only when the piece is long-form. |
| Phase 5.0 caption / body | voice-profile.md | the brand's voice canon (Jen: her verbatim lines + ENGINE-V2; Farrice: VOICE-CARD + register atlas) |
| Phase 5.5 / 6 humanizer | `tool-humanizer` | `prose_classifier.py` is the gate; humanizer may run first, never instead |
| Phase 5.0.5 visual planning | `ssc-designer` | ssc-designer when the brand has a template pool; the brand's own renderer (Jen: `valley-editions/editions.py`) when it does not |

Rule: one integrator writes, one check vetoes (the brand-as-itself seat). Never six seats on one hook (his 2026-09-02 correction: "expert soup"). Evidence from the first client run: v1 hook written from the Scrapes formulas alone scored 6/10 by Farrice; v2 with Alyssa + Luke integrated is the take to judge.

1. **Carousel:** one supplement teardown → `/00-social-content` scenario A vs the current Jen/LinkedIn carousel path. Judge: hook slide, visual floor, voice.
2. **De-slop:** one flagged draft → `/tool-humanizer deep` vs a hand pass against the ban bank, both then run through `prose_classifier.py check`. Judge: score delta and whether his voice survived.
3. **Repurpose:** one Parallax edition → `/mkt-content-repurposing` vs `/atomize`. Judge: platform fit and ICP verbatim retention.

## What this retires from the imitation era

The Scrapes-derived imitations in `extractions/agentic-os-integration/` (the pattern-inventory and delta analysis) are now historical. Anything built from them that duplicates a FLIP NOW row above gets `routing: long-tail` in its frontmatter after its blind bar, never deletion. Nothing gets demoted on feel.
