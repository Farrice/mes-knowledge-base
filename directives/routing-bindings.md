# Workflow Routing — Full Bindings Table

> Extracted from CLAUDE.md 2026-06-09 (rebuild). The UserPromptSubmit hook
> (`skill_router_hook.py`) matches every prompt against this table and surfaces the better
> route as a **suggestion with its reason**. Machine source of truth:
> `execution/routing_enforcer.py BINDINGS`. **Update BINDINGS and this table together.**
>
> **DISARMED 2026-07-27 (compass doctrine).** The enforcement trial that ran 2026-07-17 → 2026-07-27
> made binding violations **block the prompt** and demand a `!route` token. It is off, permanently,
> and does not re-arm on a date. Reason: on 2026-07-27 it matched the word "anaphora" inside a
> question *about a prose-classifier false positive* and force-routed it to a rhetoric workflow.
> A router that misreads the request and then blocks it costs more than it saves. State lives in
> `.agent/routing-enforce-trial.json`; events still log to `.agent/sessions/routing-enforce-log.jsonl`
> so the false-positive rate stays measurable.

If the task matches a domain below, the bound workflow is almost always the right call, and it's worth saying so out loud when the user names a different one. Origin: 2026-04-21 session degraded to 6/10 because `writers-room` was used instead of `/parallax`. **The user's explicit choice wins.** Name the better route in one sentence, then do what they asked.

| Domain signal | Expected workflow | Never substitute |
|---|---|---|
| **Any Scrapes job, raw text** ("scrapes", "run it through scrapes", "set up my templates", "template pool", "onboard my brand") | `/scrapes` — ONE door: classify the job → BRAND LOCK → the matching door below, or the template-pool onboarding, visual identity, brand voice, or a single tool. User's guide: `_active/harness/scrapes-skill-systems/USER-GUIDE.md` | Guessing the pipeline; guessing the brand; web-scraping tools (different word, different job) |
| **Carousel** for any brand ("carousel", "make a carousel", "linkedin/instagram carousel", "carousel for jen") | `/social-carousel` — BRAND LOCK (`scrapes_brand.py resolve`) → `research.py` brief into the Scrapes cache → OUR pens write caption + slide script (client: Alyssa hook-reframe + Luke Iha; Farrice: VOICE-CARD dial + Luke Iha; one integrator, one veto) → `claim_audit --strict` + `prose_classifier check` → Scrapes `00-social-content` Scenario A (designer, template pool, images, studios). Cost stated before any AI slide. [SCRAPES engine] | `ai-carousel-engine`, `generate-handcrafted-carousel`, freehand slide copy, guessing the brand |
| **Image-bearing social post** ("post with an image", "instagram post", "generate post", "social post for <client>") | `/social-post` — same lock + pens, Scrapes Scenario A for inference + single visual | `/ghostwrite` keeps Farrice's plain LinkedIn text posts; never a Scrapes draft in a client's voice |
| **Repurpose** ("repurpose this", "atomize this", "version for threads", "thread from this") | `/social-repurpose` — lock → Scrapes `mkt-content-repurposing` mechanics → our ICP-verbatim + voice check per platform → classifier. TEST FIRST vs `/atomize` (blind bar #3) | Literal copy across platforms; dropping the buyer's verbatim words |
| **Slide deck** ("slide deck", "make a deck", "create a presentation", "slides for") | `/deck-build` — lock → Scrapes `00-slides` + `viz-frontend-slides` on the brand's `tokens.json`; `claim_audit` veto on the outline | `presentation-build` (prose only); readouts/research briefs stay on `/briefs` (Ink + Steel Blue) |
| **Long-form video → shorts** ("youtube to shorts", "clips from this video", "reframe to 9:16") | `/video-to-shorts` — Scrapes `00-longform-to-shortform` (WhisperX, clip scoring, face-aware reframe, caption burn); publish OFF | Edit-bay-only cuts without scoring; any auto-post; TTS or voice clone |
| **Video → ebook / article** ("youtube to ebook", "video into an ebook", "article from this video") | `/video-to-ebook` — Scrapes `00-youtube-to-ebook` (their fact-checker runs) → OUR `claim_audit --strict` veto + `prose_classifier` before the PDF | Shipping their fact-check as the veto; skipping the human review step |
| Content production from scratch ("content ideas for", "what should I post", "hooks for", "content angles") | `/create` Stage 2 step 0 — reuse a same-day brief only with a passing current evidence receipt; otherwise request an on-demand `/deep-research-os --free-first` mission (`directives/live-data-grounding-protocol.md`) | Blank-page ideation from training memory; assuming a scheduled brief ran |
| Parallax Substack editions | `/parallax` | `writers-room` (diagnostic-on-draft only) |
| LinkedIn post from scratch | `/ghostwrite` or Lara Acosta skill | `writers-room` (refinement only) |
| Writers' room refinement of existing draft | `writers-room` | Production workflows |
| Rhetorical device / memorable line ("chiasmus", "saxon punch", "make it quotable", "make this line memorable", "rhetorical device", "anaphora", "epistrophe") | `/ward-rhetorical-engine` (Ward Farnsworth — classical devices on the line carrying the argument) | Generic rewrite without device craft |
| Theme-first / emotional architecture ("theme-first", "theme first writing", "emotional architecture", "make the reader feel", "restraint pass", "gravedigger angle", "tuesdays with morrie", "sentiment without sentimentality") | `/albom-theme-first-engine` (Mitch Albom — find the one human truth, build backward, earn the feeling through restraint) | Generic "write a story" (defers to writers-room / story-stack) |
| Go-Direct communications strategy ("go-direct", "go direct", "m3 matrix", "message-medium-messenger", "communications strategy", "comms strategy", "comms campaign", "crisis communications", "reality architect", "strategic wrongness") | `/lulu-m3-matrix` (Lulu Cheng Meservey — Message-Medium-Messenger matrix gravity-welled to one named business goal; load-bearing comms strategy before any asset) | Generic brand/messaging workflow without M3 architecture |
| DESIGN.md authoring / extract / synthesize / brand-system | `/design-md-synthesize` or `-extract` or `/brand-library` | Generic Tailwind/CSS |
| UI / component code from DESIGN.md | `/product-build` or `/component-build` | Hand-rolling without DESIGN.md |
| DESIGN.md lint / WCAG / refinement | `/design-md-validate` | Eyeballing — always run `npx @google/design.md lint` |
| Competitive intel needing JS-rendered pages / screenshots | `/competitor-intel` or `/spy-market` + Playwright | WebFetch (returns hydration shells) |
| Login-gated source verification | Playwright per `directives/browser-automation-safety.md` | WebFetch (returns login wall) |
| Video source material (23 video-aware workflows) | `python3 execution/fetch-video-context.py` per `directives/video-vision-protocol.md` | Transcript-only ingestion (visual hooks = 30-50% of meaning) |
| Brand Operating System / "BOS" / 6-layer brand build | `/build-bos` (7-phase via `skills/brand-operating-system/`) | Single-component skills alone |
| Discovery-backed brand direction / "moodboard from discovery evidence" / "three client directions" (`brand_direction_decision_spine`) | `/andrew-lane-design-systems` (Brand Direction Decision Spine: challenges → exploration → directions → proving surface); it may compose `/mood-board` for the actual visual-board construction | Standalone campaign, shoot, event, product, and non-brand boards stay `/mood-board`; `/build-bos` owns a requested full six-layer system |
| Standalone moodboard construction from a creative brief · campaign/shoot/event/product board · three materially different visual territories · blind taste choice (`mood_board_orchestrator`) | `/mood-board` — reference acquisition → three actual visual boards → one comparative proving surface → blind `Choose / Keep / Kill` → selected-direction handoff | Discovery-backed brand direction stays with `/andrew-lane-design-systems`; existing style-library characterization stays `/moodboard-sweep`; full BOS stays `/build-bos` |
| Multi-deliverable marketing/creative mission | `/supercomputer` (anchor-memory + cost gate) | Single-skill execution alone. Triggers: `directives/supercomputer-mode.md` |
| Gate-suppressed orchestration ("autopilot", "no gates", "just execute") | `/autopilot` — 3 gates only: G1 (intent <=2), G2 (cost >$5), G3 (prose FLAGGED at Expert Standard >=7) | `/supercomputer`, `/jcc-deploy` etc. |
| Context engineering / "engineer the conditions" / "make the behavior automatic" | `/ce-design` (Context Engineering OS in `skills/chase-hughes-context-engineering/`) | Single-tactic copy/LinkedIn workflow alone. Ethics gate: `execution/context_ethics_gate.py` |
| Build an avatar / ICP / manifold from scratch · "plot the market" · cold-start buyer intelligence | `/avatar-machine` (full cold-start → finished copy) or `/avatar-manifold` (intelligence only). **Phase 0 GROUND auto-fires** (`execution/avatar_manifold_runner.py`, gated by `research_quality_gate.py --strict`). Skip only with `--no-ground` + `--voc-file` | `icp-build`/`icp-research`/`icp-deep-dive` (reasoning-only; modeled language fails rubric crit 6) |
| Cold-start → converting copy (VSL/ad/email/landing from blank page) | `/copy-engine` — **Ground Once, Refine Free.** Grounds ONCE via `avatar_manifold_runner.py` (WARM reuse = $0), writes `warm_core`, assembles the 6 copy blocks, gates proof via `verify_proof_ledger.py`. Later iterations reuse the cache at $0 | Writing copy from ungrounded context. Refinement of EXISTING copy uses standalone copy-blocks workflows at $0 |
| Amazon KDP / first Book One / AI ebook without slop / market-first pen name | `/kdp-engine` → `/sean-dollwet-book-one-pilot` for a blank slate. The conductor owns demand, editorial, rights, AI disclosure, metadata, preview, organic launch, permission, and market proof. | Generic copy or anti-slop gates as the function owner; they are downstream quality checks only |
| New/changed offer, pricing, offer stack/spine ("new offer", "what should I charge", "launch an offer", "pivot the offer") | `/offer-redteam` (runs `offer_gate.py`, $0 and always exit-0 advisory) — worth running early because its one prior firing killed the $400 audit offer and modified Signal Pilot. **Compass, not gate (2026-07-27): never hold a build or a send waiting on it.** Run it alongside the work, or after | Skipping the red team entirely on a fresh offer (echo-chamber risk). Executing an already-red-teamed offer does not re-trigger |
| Dan Wang analytical essay ("friction map", "official story vs ground truth", "annual letter", "dan wang", "draft 1.5 of history", "anchor sentence essay", "literary cornerstone") | `/wang-friction-map` (Dan Wang — mine the gap between the official story and the ground truth before drafting, then hand forward to `/literary-cornerstone-sprint`, `/wang-anchor-sentence`, `/wang-musical-pass`) | Generic "essay"/"long-form" (defers to writers-room / story-stack) |
| Michael Connelly vivid writing ("telling detail", "michael connelly", "connelly", "pick the one detail", "show don't tell", "momentum audit", "good place(s) to stop") | `/telling-detail-engine` (Michael Connelly — pick the one detail that reveals character AND situation, show the tell instead of naming it, keep momentum sacred; hand forward to `/momentum-audit`, `/connelly-rewrite`, `/connelly-subtext`) | Generic "write a story"/"make it vivid" (defers to writers-room / depth-layer / story-stack) |
| Ocean Vuong perceptual writing ("ocean vuong", "estrangement engine", "defamiliarize", "defamiliarization", "species test", "perceptual rewrite", "anti-homogenization", "escape the median sentence", "make the familiar strange") | `/estrangement-engine` (Ocean Vuong — lead with the concrete image, make the familiar strange so the reader sees it for the first time, refuse the AI-median sentence on a hard honesty spine; hand forward to `/species-test`, `/cliche-rescue`, and cross-domain `/ocean-perceptual-copy`, `/ocean-brand-estrangement`, `/ocean-content-anti-slop`) | Generic "make it original"/"less AI-sounding" (defers to writers-room / depth-layer) |
| Bill Browder high-stakes narrative nonfiction ("bill browder", "browder", "next-sentence test", "make the dry material grip", "unputdownable nonfiction", "high-stakes narrative", "stakes escalation", "name the villain", "evidence as spine", "make finance gripping", "page-turner nonfiction") | `/browder-next-sentence-test` (Bill Browder — make dry/complex domain material grip by escalating real jeopardy, rendering the villain through documentary evidence, and pulling the reader into the next sentence on a load-bearing honesty spine; hand forward to `/browder-drama-excavation`, `/browder-stakes-architecture`, `/browder-villain-evidence`) | Generic "write a story"/"make it gripping" (defers to writers-room / depth-layer / story-stack) |
| Truthful lived-story mining ("my life is boring", "story material packet", "Safe Real Raw", "lived story material", "truthful personal story", "ordinary lived moment", "founder notes without making up", "without invented psychology") | `/jun-story-engine` (Jun Yuh — mine supplied lived material, let `FULL STORY`, `STORY FRAGMENT`, `NO STORY`, or `NEEDS SOURCE` win, then keep Jun on social output or hand cross-domain dosage to Shaan) | Generic "write a story" with an already-formed narrative; literary-story routes; inventing biography, motive, chronology, or transformation |
| Susan Orlean curiosity-driven literary journalism ("susan orlean", "orlean", "telling subject", "small overlooked subject", "find the story inside", "decide structure before writing", "structure before writing", "card structure", "three-phase process", "wait-what lead", "curiosity-driven literary journalism", "the orchid thief", "the library book") | `/orlean-telling-subject` (Susan Orlean — find the large theme hiding in a small overlooked subject, decide structure physically before any prose, protect the research/thinking/writing phases, lift saturation reporting into a told story; hand forward to `/orlean-card-structure`, `/orlean-three-phase-process`, `/orlean-yarn-engine`, `/orlean-wait-what-lead`, `/orlean-pull-the-punch`) | Generic "write a story"/"essay" (defers to writers-room / depth-layer / story-stack); dry/high-stakes material → Browder; lyric sportswriting → Wright Thompson; analytical essay → Dan Wang |
| Henry Shukman contemplative / wonder writing ("henry shukman", "shukman", "concrete doorway", "reopen the reader to wonder", "contemplative writing register", "presence over performance", "the romantic eye", "stillness in prose", "poetry as philosophy", "wonder of ordinary reality", "embodied word", "mythos register") | `/shukman-concrete-doorway` (Henry Shukman — reopen the reader to awe by carrying the largest feeling on one true concrete particular: presence over performance, the romantic eye, stillness, heart-first sincerity; hand forward to `/shukman-wonder-content`, `/shukman-presence-essay`, `/shukman-stillness-social`, `/shukman-embodied-word`, `/shukman-mythos-logos`) | Generic "write a story"/"make it poetic" (defers to writers-room / depth-layer); estrangement/strangeness → Ocean Vuong; sensory maximalism → Paul Harding |
| Paul Harding lyric perceptual fiction ("paul harding", "harding", "perception engine", "lyric perceptual prose", "sensory maximalism", "the two things", "counterpoint description", "improvisation over outlining", "the music of prose", "translate sensation onto the page", "describe reality vividly", "tinkers") | `/harding-perception-engine` (Paul Harding — describe reality vividly by slowing attention to the pre-linguistic instant and re-translating the raw seeing until the ordinary turns luminous: the two things, counterpoint, botanist's-precision-plus-calculus, the drummer's cadence, improvisation over outlining, persuasion by recognition; hand forward to `/harding-precision-wonder`, `/harding-two-things`, `/harding-counterpoint`, `/harding-improv-draft`, `/harding-cadence`, `/harding-distill`, `/harding-recognition-audit`) | Generic "write a story"/"describe this" (defers to writers-room / depth-layer); surgical economy/minimalism → Michael Connelly; estrangement/strangeness → Ocean Vuong; contemplative wonder → Henry Shukman |
| How-I-Write OS / master writing conductor ("how i write", "how-i-write", "writing os", "writing council", "compose the writers", "writing operating system") | `/how-i-write` (How-I-Write OS — diagnose intent → smallest sufficient altitude stack of the 10 How-I-Write experts + story-stack → ONE-voice draft → line + truth/clamp/prose/fact gates; composes existing experts, never rebuilds a writer. `/how-i-write-os` aliases the same conductor) | Single tactic (defers to the specific expert directly); rebuilding a writer from scratch |
| Farrice voice identity ("sound like me", "in my voice", "voice card", "voice os", "voice alignment", "voice ratchet", "voice compile", "make it sound like farrice") | `/voice-os` (Voice OS — persistent compiled voice card at `_active/farrice-brand/voice/VOICE-CARD.md` + 4-mode fidelity dial MIRROR/BLEND/STRETCH/OFF + felt-verdict calibration loop via `/voice-ratchet` → `/voice-compile`; a LAYER content workflows load, never a replacement for them) | Improvising Farrice's voice from training memory. Client voice work (Jen, Andrea, VOC mining) = OFF-mode, keeps its own routes |
| Multi-expert / collaborative / council work | `/convene` → `collective-genius-council.workflow.js` (presets: `/council` `/roundtable` `/strike` `/campaign` `/deploy-council`) | JCC plugin stubs, `execution/parallel_swarm.py` (deprecated) |
| Expert panel for an UNFAMILIAR/thin-roster domain, or tiered implementation roadmap as the deliverable ("assemble a panel", "expert assembly", "world-class panel", "I don't know this domain") | `/assemble` → `expert-assembly.workflow.js` (hybrid cast via `panel_cast.py`: roster where strong + bespoke composite personas where thin, `persona_stat_lint.py` gate, strategic/tactical/operational roadmap per `roadmap-schema.md`; `/panel-sync` reloads a pinned panel) | Roster-covered deliberation without a roadmap need (that's `/convene`); re-synthesizing a panel that `/panel-sync` can reload |
| Thin domain coverage + roadmap synthesis (hybrid roster + bespoke personas + tiered roadmap) | `/assemble` → `expert-assembly.workflow.js` (hybrid panel casting, composite persona synthesis, multi-round deliberation, 3-horizon observable roadmap with success criteria) | Single `/convene` council call (pure deliberation without coverage detection or roadmap); pure research without panel synthesis → `/deep-research-os --free-first` |
| Generic research · "deep research on X" · strategic intelligence | `/deep-research-os --free-first`: Codex native web and opened current sources first; bounded basic-depth Tavily Search/Extract and public RSS for identified gaps; local context and skills only after the live-evidence gate. Every result carries evidence, quality, quota, and value receipts. | Training-memory answers; `execution/research.py`, paid providers, Tavily Research, or research swarms without separate explicit authorization |
| Social/audience/trend listening ("what's happening in [niche]", "audience sentiment", "creator analysis", "#hashtag trends", "social listening", "social sentiment") | On-demand `/deep-research-os --free-first`: public native-web evidence, opened pages, bounded basic Tavily Search/Extract, and public RSS/Atom where useful. Inaccessible platform-private data remains an explicit evidence gap. | Apify actors; `/social-pulse` schedules; paid synthesis; invented private-platform coverage |
| New expert extraction ("extract this expert", `/extract`, `/extract-forge`) | `/extract` or `/extract-forge` directly — **never gated** (Farrice's standing decision 2026-06-09). `forge_gate.py status/record` = telemetry only | — |
| Persistent character / world / product-identity visual work ("persistent character", "face lock", "character sheet", "outfit swap", "scene plate", "story bible", "brand world visuals", "Seedance prompt", "AI video consistency") | Joey Cinema OS pipeline (`skills/joey-cinema-os/SKILL.md`, front door `/jcin-pipeline`) — `skills/banana-pro-director/SKILL.md` for character/product BUILDS (Banana Pro default, Higgsfield GPT-2 fidelity escalation, Soul two-step), `skills/cinema-worldbuilder-pro/SKILL.md` for Seedance video prompts. Per CLAUDE.md, `execution/creative_router.py` lane notes and this row update together | One-off people shots (stay `higgsfield-soul` via creative_router); `gpt-image-2-director` for faces — that skill's OpenAI GPT Image 2 is weak on faces and is NOT Joey's Higgsfield GPT-2 |
| Pay-as-you-go creative generation ("generate an image/video/voiceover", "make ads/assets/creative", model names — recraft, kling, seedance, nano banana, gpt image — multi-model comparison runs, "total budget $N" generation batches) | `/generate` (`skills/generate/SKILL.md` + `execution/generate_media.py`, model recipes `skills/generate/models/*.json`) — defers to creative_router binding lanes first (people → `higgsfield-soul`, style-family → `fantastic-posters`, persistent identity → `/jcin-pipeline`); paid video quotes + waits for explicit go; results land on `/assets-board`. Per CLAUDE.md, `execution/creative_router.py` lane notes and this row update together | Bypassing wrappers (one code path per model — `run` refuses wrapper-backed recipes); seedance-1080p (hard-blocked); raising a prompt-level budget without Farrice |
| Control-plane COMPLAINTS — hooks not firing, wrong default routing, Codex↔Claude parity drift, "check and repair the hook wiring", handcuffed/over-chained routes (`operator_system_audit` binding) | `/system-audit` (read-only proof → manual hook-equivalent gates → local repair) | Expert/content workflows. **Narrowed 2026-07-13**: bare "wiring"/"chained" removed from triggers — research missions and build-aspiration language ("worth wiring into the ladder") must NOT trip this; complaint-shaped compounds ("hook wiring", "not wired together", "handcuffed and chained") still do. Golden set: `execution/verify_control_intent.py` (BINDINGS_GOLDEN) |

## Non-Optional Phase Gates

**Avatar Machine Phase 0 GROUND is non-optional for cold-start builds.** Gemini Deep Research foundation + Apify VOC mining + FB Ad Library hooks + Recall grounding, floor-checked (≥15 source URLs, zero `[MODELED]`) by `research_quality_gate.py --strict`. Skip only with `--no-ground` + `--voc-file` (the "import, don't regenerate" path). Binding: `avatar_manifold_coldstart`.

**Parallax Phase 2.5 GROUND + ZEITGEIST is non-optional for Editions 02+.** Claim extraction, budget-tiered verification (Recall -> Perplexity), zeitgeist scan, halt/proceed gate. Skip only with explicit `--no-ground` (pure memoir, zero external factual surface). Origin: Edition 02 shipped 7 fabrications.

**Extractions are never gated** (standing decision 2026-06-09 — the freeze concept shipped and was reversed the same day at Farrice's direction). `forge_gate.py` survives only as usage telemetry: `status` shows the last extraction's production-use count in the monthly closeout; `record` registers a new extraction. Neither blocks anything.

## Manual Pre-Flight (when composing workflows yourself)

```bash
python3 execution/routing_enforcer.py check --request "<user request>" --workflow <chosen-workflow> --quiet
```

Non-zero exit = violation. `finalize()` also runs a post-hoc check.

---

## Appendix — machine bindings (GENERATED, do not hand-edit)

> Amnesty 2026-07-29: the header rule "update BINDINGS and this table together" was
> violated within weeks (7+ code-only bindings, 7 prose-only rows). Hand-sync drifts;
> this appendix is generated from `routing_enforcer.BINDINGS` — the machine list is
> authoritative for WHAT matches; the prose table above is authoritative for WHY.
> Rows above with no ID here are prose-only guidance (no machine twin) — that is fine.
> Regenerate: `python3 execution/routing_enforcer.py appendix`.

| Binding ID | Suggested workflow(s) | Signals |
|---|---|---|
| `operator_mission_control` | /mission | 6 |
| `operator_source_to_skill_system` | /source-to-skill-system | 9 |
| `kdp_book_one_coldstart` | /kdp-engine | 9 |
| `operator_search_content_mastery` | /search-content-mastery | 14 |
| `operator_system_audit` | /system-audit | 53 |
| `operator_steering_compass` | /steering-compass | 7 |
| `operator_expert_composition` | /expert-composition-governor | 6 |
| `operator_high_taste_output_os` | /high-taste-writing-os / high-taste-os | 70 |
| `operator_repeatability_spine` | /repeatability-spine | 33 |
| `parallax_editions` | /parallax | 6 |
| `linkedin_from_scratch` | /ghostwrite / lara-acosta-linkedin-ghostwriting / high-dwell | 6 |
| `writers_room_refinement` | /writers-room | 7 |
| `cold_start_converting_copy` | /copy-engine | 9 |
| `offer_redteam_gate` | /offer-redteam | 14 |
| `brand_operating_system` | /build-bos | 11 |
| `brand_direction_decision_spine` | /andrew-lane-design-systems | 23 |
| `mood_board_orchestrator` | /mood-board | 21 |
| `supercomputer_mission` | /supercomputer | 20 |
| `autopilot_orchestration` | /autopilot | 8 |
| `vertical_bootstrap` | /verticalize | 20 |
| `context_engineering` | /ce-design | 14 |
| `avatar_manifold_coldstart` | /avatar-manifold | 13 |
| `writing_ward_rhetoric` | /ward-rhetorical-engine | 7 |
| `lulu_go_direct_comms` | /lulu-m3-matrix | 10 |
| `writing_albom_theme_first` | /albom-theme-first-engine | 8 |
| `writing_wang_analytical` | /wang-friction-map | 8 |
| `writing_connelly_vivid` | /telling-detail-engine | 9 |
| `writing_ocean_perceptual` | /estrangement-engine | 9 |
| `writing_browder` | /browder-next-sentence-test | 12 |
| `jun_lived_story_material` | /jun-story-engine | 11 |
| `writing_orlean` | /orlean-telling-subject | 14 |
| `writing_shukman` | /shukman-concrete-doorway | 13 |
| `writing_harding` | /harding-perception-engine | 13 |
| `writing_how_i_write_os` | /how-i-write | 6 |
| `farrice_voice_alignment` | /voice-os / voice-ratchet / voice-compile / voice-audit | 12 |
| `content_production_live_grounding` | /create / zeitgeist / briefs | 12 |
| `deliverable_visual_delivery` | /briefs / briefing-room | 15 |
| `social_listening_free_first` | /deep-research-os | 13 |
| `unified_research` | /deep-research-os | 13 |
| `collective_genius` | /convene / collective-genius-council / council / roundtable / strike / campaign / deploy / jcc-deploy / assemble / expert-assembly / panel-sync | 16 |
| `jen_listing_package` | /listing-package | 11 |
