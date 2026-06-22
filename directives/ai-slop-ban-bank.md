---
title: AI-Slop Ban Bank
status: canonical
supersedes:
  - feedback_ai-writing-tells.md
  - feedback_ai-structural-tells.md
expands:
  - feedback_no-cheap-question-signoffs.md
  - feedback_writing-excellence-rules.md
  - novelty-protect.md (Part A mascot reveals + Part B town-crier)
enforced_by: execution/prose_classifier.py
fires_at: Chain Step 5 (Produce) + Step 6 (Quality Gate, Expert Standard cap)
last_updated: 2026-06-21
---

## Purpose

The standard: prove AI can ship remarkable, pristine, high-taste content that is VOID of the cliches everyone else uses. Every entry below is a tell that exposes the machine: a word, a cadence, a structural reflex, or a register that a trained reader clocks instantly and an untrained reader feels as "off" without naming. This bank is the canonical no-fly list. It supersedes `feedback_ai-writing-tells.md` and `feedback_ai-structural-tells.md` and absorbs the novelty-protect mascot/town-crier families plus the no-cheap-signoffs alternatives. A piece that contains any Hard Ban below is not finished, regardless of its quality-gate composite. The em-dash and phrase rules govern SHIPPED posts and drafts; the tells quoted verbatim inside the tables below are labeled specimens, not commitments (a reference bank must show the patterns it forbids). The bank's own authorial prose ships zero of what it forbids.

Annotation key: **[CLASSIFIER]** = already caught deterministically by `prose_classifier.py`. **[NEW]** = judgment-only today; flagged for the enforcement appendix.

---

## 1. The Hard Bans

Absolute no-fly. One instance is a defect to fix before delivery.

### Openers

| Tell | Why it reads AI | Fix |
|---|---|---|
| "In today's fast-paced / digital / ever-evolving world…" and the era variants ("in the age of AI," "the evolving landscape of…") **[CLASSIFIER]** | Throat-clear that names a vague era to delay the point. Interchangeable across every topic ever written. | Cut the clause. Start on the concrete subject: "Most teams ship a feature without testing it." |
| "In the world of… / When it comes to… / The importance of…" **[CLASSIFIER]** | Essay-bot warm-up that says nothing. | Delete; lead with the claim. |
| "Are you struggling with…? / Have you ever wondered…? / Imagine a world…" **[CLASSIFIER]** | Reepl names "Are you struggling with" the single most common AI hook. Front-loads zero tension. | Promote the most surprising line in the draft to line one. |
| "Here's the thing…" / "Here's the thing about X" **[NEW]** | A bridge that announces substance is coming and adds none. Humans mid-thought just continue. | Delete. If the next sentence can't open the piece alone, there is no thing. |
| "Here's what happens when… / Here's what / why / how…" as a paragraph opener **[NEW]** | A dead crutch that announces the writing instead of doing it. | Open with the insight or the scene. Let the writing be the thing. |
| "Here's what nobody tells you / the part nobody talks about / nobody tells you this" **[NEW]** | Promises gatekept knowledge, pays off with a platitude. The gap is the tell. | Only keep the frame if the payoff is genuinely non-obvious to this specific audience — a mechanism, a number, a named exception. Otherwise cut. |
| "Most people think X. They're wrong." / "Everyone gets X wrong." **[NEW]** | A content-free strawman template — slot any topic in. dev.to: 38% of AI posts open this way. | Name a real belief held by a real group, grant its strongest form, then complicate it. |
| Rocket-emoji cold-open on a sweeping trend ("🚀 The wellness industry is changing faster than ever.") **[NEW]** | Decorative emoji + unfalsifiable trend that commits to nothing and names no one. | Open cold on a falsifiable specific: a number, a named brand, a thing that happened. |

### Connectives

| Tell | Why it reads AI | Fix |
|---|---|---|
| Furthermore / Moreover / Additionally — especially opening consecutive paragraphs **[CLASSIFIER]** | AI uses these at 2-3x human rate. A dozen transitions in 500 words flags. | Cut most. Good prose connects through logic, not signposts. |
| "That's where AI comes in." / "That's where X comes in." **[NEW]** | A hinge with no thought in it — the verbal scene-transition wipe of every problem→solution post. | Show the join with a mechanism: "An LLM reads the open-text answer the dropdown couldn't." |
| "Let me break it down. 👇" **[NEW]** | A template seam that stalls to announce structure. The arrow treats the reader as needing to be told to scroll. | Just start the breakdown. |
| "So, what does this mean for you?" **[NEW]** | A seam between "insight" and "takeaways." Announces the turn instead of executing it. | Cut it; let the takeaway hit. If you showed a real failure, the reader already feels the "what now." |
| Orphan "And…" line restating the prior line in fresh adjectives **[NEW]** | Manufactured momentum — chop a sentence, demote the conjunction to a line-start, let whitespace fake weight. | Cut, or let the second line deliver information the first couldn't. |

### Closers

| Tell | Why it reads AI | Fix |
|---|---|---|
| "What do you think? / Thoughts? / Agree or disagree? / What would you add? 👇" **[NEW]** | The laugh track of LinkedIn — tells people where to react instead of earning it. So ubiquitous it now *reduces* engagement. | End on your strongest sentence. A question is allowed only if it advances THIS post's exact argument and fails the transferability test (can't be pasted onto any other post). |
| "I'll wait." / "I said what I said." / "Say it louder for the people in the back." **[NEW]** | Performs combative confidence to imply a controversial take the content never delivered. | Let a contestable claim stand bare and take the disagreement in the comments. |
| "The question is: are you ready to embrace it?" **[NEW]** | A yes/no the reader can't answer to anyone. "Embrace" is the AI verb for "adopt." | Image close, declaration, or bookend to the opener. Ban "embrace" on sight. |
| Recap conclusion ("In conclusion… one thing is clear…") **[CLASSIFIER]** | ~82% of AI pieces end on a resolution closer that restates the opening. | End on an extension, image, or specific. Advance the thought or stop. |
| Mic-drop aphorism + deflation ("That's the whole letter." / "That's all I've got.") **[NEW]** | A closing aphorism followed by a shorter deflation is a recognizable AI sign-off gesture. | Voice-true close: image, declaration, earned silence, bookend admission. |
| Humblebrag / coffee-with-an-unnamed-CEO close ("Humbled and honored…" / "A Fortune 500 CEO told me one secret…") **[NEW]** | Wraps a flex in false modesty and unverifiable name-drops. AI has no real relationships, so it gestures at prestige. | Name the person (with permission), the actual thing said, what you did with it — or drop the brag. |

### Vocabulary

| Tell | Why it reads AI | Fix |
|---|---|---|
| The lexicon: delve, tapestry, landscape, leverage, robust, multifaceted, comprehensive, nuanced, paradigm, synergy, holistic, transformative, groundbreaking, cutting-edge, game-changing, unparalleled, myriad, plethora, foster, cultivate, harness, spearhead, streamline, embark, navigate, unlock, elevate, empower, reimagine, revolutionize **[CLASSIFIER]** | 5-10x over-represented in AI vs human writing; "delve" is the single most-detected. They cluster because they are the abstraction register a model defaults to when it has no specifics. | Plain verb/noun: delve→examine, leverage→use, foster→build, navigate→handle, elevate→raise, unlock→open. If it reads like a consulting deck, it reads AI. |
| The current-era cluster: ensuring, highlighting, showcasing, align with, reflects, supports **[NEW]** | A frozen 2023 ban list goes stale. GPT-4o-era output is clean on "delve" but reads "ensuring alignment while showcasing impact." "Ensuring" is the single strongest current word signal (4.3x). | Audit the current cluster, not just the legacy one. Say what the thing does. |
| "This changes everything / game-changer / paradigm shift / disruption" stacked **[CLASSIFIER]** | AI can't calibrate scale — it has no stake, so everything is maximal. A sentence with all four is nonsense. | Quantify the change or cut the adjective. "Cut onboarding from 6 days to 4 hours" is a game-changer without the phrase. |
| Atmosphere-by-adjective: "a quiet hum," "the ghost of a smile," "liminal space"; stock names (Elara, Kael, Voss) **[NEW]** | Hollow sensory vibes substituting for observed detail, even in concrete scenes. | One concrete observed detail you could smell/hear/touch. If you can't sense it, don't compare it. Rename stock characters. |
| Boosted "to be": "boasts," "serves as a testament," "stands as a cornerstone," "features" **[NEW]** | LLMs avoid plain is/has and reach for inflated substitutes. | Replace with is/has/was. Reserve "serves as" for when something literally functions as something else. |
| Doubled adjective hedge: "quieter and harder," "stranger and deeper" **[NEW]** | Two soft adjectives joined by "and harder/deeper" hedge meaning instead of committing to one precise word. | One specific adjective, or cut the pair. |

### Formatting

| Tell | Why it reads AI | Fix |
|---|---|---|
| Emoji as structure (🚀/💡/✅ prefixing headers or replacing bullets; arrows at line-ends) **[NEW]** | Humans rarely decorate structure. Emoji clustering at opener/transition/resolution/CTA joints is itself the fingerprint. | Strip emoji from structural elements. Keep one only if it does real semantic work. |
| Title Case headings + colon-headings ("Building A Robust Framework: Key Strategies") **[NEW]** | Reads as a press release. Editorial style is sentence case. | Sentence case, drop the colon crutch, add a heading only when the content needs the break. |
| Bold-phrase-colon list architecture (every bullet **Bold:** then a sentence) + random keyword bolding **[NEW]** | Mechanical inline-header lists; the bold lead-in often just echoes the section header. | Convert to prose or vary the list. Reserve bold for genuine emphasis. |
| Broetry: one-sentence-per-line with massive vertical whitespace **[NEW]** | Fused with bad-faith influencer posts; exists to force "see more" clicks, not to communicate. | Real paragraphs of two-to-three sentences, varied length. |
| Generic hashtag wall (#AI #Innovation #FutureOfWork) **[NEW]** | A 2018 reflex from training data; "#FutureOfWork" appears on AI posts about anything. | Zero hashtags, or 2-3 niche tags a real practitioner follows (#DTCsupplements over #Wellness). |
| Exclamation-point enthusiasm compensating for flat sentences **[NEW]** | Substitutes punctuation for tone. | Cut every exclamation point propping up a weak sentence. |
| Chatbot residue: "Great question! / Certainly! / I'd be happy to," orphan ** ## ---, smart quotes in code, oaicite/contentReference/turn0 tags **[NEW]** | Physical proof of pasting from a chat interface — near-certain authorship evidence, not suspicion. | Delete every preamble. Search drafts for "Sure," "Certainly," "Here's," and markup residue before publishing. |

### LinkedIn-genre

| Tell | Why it reads AI | Fix |
|---|---|---|
| Fake-vulnerable confession ("I got rejected by 12 clients before…" / "This is uncomfortable to admit, but…") **[NEW]** | The Zero Vulnerability Pattern: challenge→insight→triumph with no residual cost. Every beat flatters the author. | Keep a real cost on the page — a name, a number, a consequence that didn't resolve. |
| Fabricated stat ("78% of consumers prefer authentic brands") **[NEW] — FACTUAL VETO** | AI invents plausible-styled data with no source. 40-80% hallucination rates; 31% fabricated B2B citations. | Use your own data or a verified named source. This is a Factual Grounding veto, not a style note. |
| Fake research sample ("I asked 100 founders…" / "I analyzed 500 posts…") **[NEW]** | Suspiciously round samples the author never ran; no surprising finding ever emerges. | Show the messy specifics if you ran it. "Across the dozen-ish clients I've worked with" is honest. |
| "In 2026, X is no longer optional" **[NEW]** | FOMO template asserting inevitability without argument. Translation: "I have nothing to say but need to mention AI." | Replace with a specific falsifiable consequence you've seen. One before/after beats a calendar claim. |
| "X is dead, long live Y" **[NEW]** | Contrarian-obituary overstating a premise the writer can't substantiate; the replacement is whatever they're selling. | Precise claim about what changed and for whom, trade-off attached. |
| "AI won't replace you, but someone using AI will" **[NEW]** | Maximally-circulated slogan — literally the line AI produces about itself. Signals zero original thought. | Banish outright. If you want the tension, name what AI actually deleted vs augmented in your domain. |
| "Let that sink in." / "Read that again." **[NEW]** | Digital incense — instructs the reader to be impressed instead of earning it. Sits under statements of staggering obviousness. | Cut entirely. If the line is arresting, white space does the work. If it needs the cue, rewrite the line. |
| "Here's the part that should keep you up at night…" **[NEW]** | Borrows thriller cadence to manufacture stakes the content can't support. | State the observation at its actual size. |
| One-word drama line ("Wow." "Period." "Forever.") **[NEW]** | Typographic mic-drop signaling importance through layout, not content. Forces a "see more" click. | Earn it maybe once per piece, after a genuinely loaded sentence. |
| Suspiciously-even numbered list ("7 lessons that changed everything," each point 2-3 sentences) **[NEW]** | AI defaults to a tidy 5-7 list where no point runs longer or has a tangent. Real humans write unevenly. | Let points be wildly uneven, or pick the single best one and make the whole piece about it. |
| The whole-post skeleton: hook → blank → short line → numbered list → reflective question **[NEW]** | The macro-structure every LLM defaults to; LinkedIn's authenticity scoring penalizes it with reduced reach. | Break the skeleton, not just the words. Open with the conclusion, skip the list, or write one unbroken argument. |
| Mascot reveal — hedge-to-old ("this is really just X," "fundamentally nothing new") **[NEW]** | Confesses the new frame is the old thing in costume. The single most devastating novelty mistake — one line voids the build. | Scrub the hedge, never the fact. Grep kill-list: "this is really just," "as you probably know," "this has been around forever, but," "to be fair, this isn't new." |
| Mascot reveal — false modesty ("I'm no expert but," "this might be obvious but," "take this with a grain of salt") **[NEW]** | De-authorizes the reveal and pre-labels it un-new. | Flip to a confidence signal. Keep genuine humility, cut the illusion-killer. |
| Town-crier register (ALL-CAPS, "HUGE," "you NEED to," billboard energy) **[NEW]** | The salesy tone itself is a 2026 disqualifier independent of content. Audiences distrust anything that sounds like a billboard. | Gossip-whisperer register: lowercase, conspiratorial, magnitude under-claimed verbally, sharing-WITH not selling-TO. Lower the volume, never the truth. |

---

## 2. The Banned MOVES

These survive a word-level scan. They are structures, not strings — a phrase ban list will never catch them. Grep for the shape, not the vocabulary.

| Move | Signature | Why it reads AI | Fix |
|---|---|---|---|
| **Not-X-it's-Y antithesis** **[NEW]** | "It's not X. It's Y." / "It's not about the money. It's about freedom." / "This isn't a strategy. It's a movement." | The single most-fingerprinted AI move. AlphaSense tracked it in filings: ~50 mentions (2023) → 200+ (2025). Manufactures depth by negating the obvious and asserting the warm. | State the claim once, plainly. Keep at most one reframe per piece, and only if X is a belief someone actually holds. Grep: isn't / wasn't / "it's not" / "that's not" → if the next clause is a contrast-reveal, flatten it. |
| **Twin-sentence aphoristic ending** **[NEW]** | Declarative line, then a reversal that closes the paragraph: "The ambition didn't leave. It got honest." | Uniform across paragraphs, the declarative-then-reveal rhythm becomes a tell. | Read every paragraph's last sentence in sequence. If they're all reversals, flatten most. Not every paragraph earns a mic-drop. |
| **Triple-beat cadence** **[CLASSIFIER, partial]** | Three bullets per section, three adjectives per noun, "She doesn't cry. She doesn't rant." / "I believe X. I believe Y. I believe Z." | AI reflexively reaches for the rule-of-three to make thin analysis look comprehensive. (Classifier catches same-first-word line starts only; sentence-internal anaphora and in-paragraph triplets are NEW.) | Use the natural number. Keep one, cut two, or fuse into one sharp line. Four real points → list four. |
| **Future-prophecy parallelism** **[NEW]** | "The brands that win won't be X. They'll be Y." (matched-length negative/positive clauses) | Sounds oracular, predicts nothing testable. "Build trust" / "human connection" are the maximally safe payloads. | Make a prediction someone could bet against, with a name and a date. A real prophecy has a loser. |
| **Negation-correction + anaphora** **[NEW]** | "They don't just want products. They want personalization. They want to feel seen." | Escalating parallel sentences that sound like a crescendo while each adds nothing. The cadence is the only message. | Break the parallelism. Replace abstractions with an observable behavior: "They want the quiz to remember they said they're pregnant." |
| **Even metronome rhythm** **[CLASSIFIER]** | Three+ consecutive 17-23 word sentences, each opening subject-first. CV of sentence length < 0.3. | The longest-surviving tell across rewrites. Human prose runs CV ~0.5-0.9; AI ~0.2-0.4. Punctuation tweaks don't fix it. | Break the band: drop a three-word sentence, then let one run long and winding. Read aloud — machines fail the read-aloud test. |
| **Gerund significance tail** **[NEW]** | Sentences ending "…underscoring its significance," "…marking a pivotal moment," "…reflecting broader trends." | An "-ing" clause asserting abstract impact instead of earning it with a fact. AI does this at 2-5x human rate. | State the thing with a real subject and verb, or cut the clause. Earn significance with a fact, don't assert it with a gerund. |
| **Over-hedge / balanced neutrality** **[CLASSIFIER, partial]** | "While this has clear benefits, some may find it challenging under certain conditions." Every claim softened, every negative balanced in-sentence. | Trained to sound careful, AI refuses to commit. Diplomatic neutrality in every sentence reads as nobody home. (Classifier catches hedge density; the on-one-hand/other-hand balancing reflex is NEW.) | Pick a side. "This works, but it's slow." Inject a real stance somewhere. |
| **Despite-challenges template** **[NEW]** | "Despite facing significant challenges, the company continues to thrive and looks poised for future growth." | A template dropped in regardless of subject. | Name the actual challenge and the actual outcome with specifics. |
| **Italicized mid-paragraph thesis drop** **[NEW]** | *A self without friction is not a self.* | Flags importance instead of earning it through demonstration. | If a thesis is important enough to italicize, it's important enough to show. Cut the italics, demonstrate it. |
| **Mic-drop + deflation close** **[NEW]** | A loaded aphorism, then a shorter deflation line: "That's the whole practice." | A recognizable AI sign-off gesture. | Replace with a voice-true close. |
| **Whole-post abstraction** **[NEW]** | Zero proper nouns, numbers, or first-person specifics; swap the industry noun and every sentence still works. | The deepest tell. AI defaults to the safe center of the topic distribution because specificity is risk. | Anchor to at least one: a named brand, a real number, a dated event, or a first-person "here's what happened when I…" Specificity is the antidote to every tell at once. |
| **Cross-piece rhythm repetition** **[NEW]** | Two editions in one series sharing a closing gesture, opening bridge, or list-of-three. | When readers consume multiple pieces (they will, if it's good), repeated structure exposes the mask. | Cross-edition audit: diff closing gestures, opening moves, list-of-three usage. No two pieces share a move. |

---

## 3. Quick-Scan Checklist

Grep a draft for these before delivery. Any hit = stop and fix.

```
□  " — "                  em-dash count > 0 (Farrice tell; default ZERO, max 1)
□  isn't / wasn't / "it's not" / "that's not" → contrast-reveal in next clause?
□  "Here's the thing" / "Here's what/why/how" / "Here's how [adj] this is"
□  "Let that sink in" / "Read that again"
□  "the part that should keep you up" / "the part nobody warns/tells" / "the quiet part is"
□  "That's where ___ comes in"
□  "what does this mean for you" / "are you ready to"
□  "What do you think / Thoughts / Agree or disagree / 👇"  (closer)
□  "I'll wait" / "I said what I said"
□  "no longer optional" / "is dead" / "won't replace you but"
□  "this is really just" / "nothing new" / "I'm no expert but"  (mascot reveal)
□  delve / leverage / robust / landscape / foster / unlock / elevate / embrace
□  ensuring / showcasing / highlighting / align with  (current-era cluster)
□  "game-changer" / "changes everything" / "paradigm shift"
□  3 consecutive 17-23 word sentences (metronome)
□  3 bullets / 3 adjectives / 3 parallel clauses in a row (triple-beat)
□  paragraph endings: all aphoristic reversals?
□  emoji on headers/line-ends · Title Case headings · hashtag wall · ! marks
□  chatbot residue: "Certainly" / "Here's a breakdown" / oaicite / orphan ## **
□  SWAP TEST: replace the industry noun — does every sentence still work?
□  read aloud: smooth conveyor belt, or does it breathe?
```

---

## 4. Deterministic-Enforcement Appendix

For the engineer extending `execution/prose_classifier.py`. Follow the existing contract: module-level constant near L39-83, a `_check_<name>(text) -> Tuple[int, List[str]]` mirroring `_check_hedging` (L104), register in `classify_prose()` (L194) at the call block and the `signals.append` block. Verdict math sums whatever severities you append, so no change needed. Structural MOVES are higher-confidence than single words: weight them severity 2-3 (matching `rhythm_uniformity` at 2.0) so one contrast-reveal + one mic-drop can push to WARNING/FLAGGED, matching the "one mascot line voids the build" philosophy.

> **✅ FULLY SHIPPED 2026-06-21** in `prose_classifier.py` — both batches live and regression-tested (the four approved flagship/aha posts stay CLEAN; a genuinely human sample stays CLEAN; the tells FLAG):
> - **Batch 1:** `REVEAL_LEADINS`, `LINKEDIN_TROPES`, `GENERIC_QUESTION_CLOSE`, em-dash counter (>2), `_check_contrast_reveal` (It's-not-X-It's-Y + "no longer X; what wins is Y"), `arguably` typo fix.
> - **Batch 2:** `MASCOT_REVEALS` (sev 3/hit, near-binary), `MANUFACTURED_STAKES`, `HINGE_PHRASES`, `CURRENT_ERA_VOCAB` (overuse > 1), `DOUBLED_ADJ_HEDGE`, `TOWN_CRIER` (caps-runs + hype + exclamation density), `STRUCTURAL_EMOJI`, plus structural movers `_check_internal_anaphora` (stopword-filtered), `_check_aphoristic_endings` (>= 3 short-punch endings), `_check_gerund_tails`, `_check_micdrop_deflation`.
> - **Calibration (precision over recall):** function-word anaphora ("the" ×3) and natural "should scare you" relative clauses are deliberately excluded so legitimate human prose is never capped. Judgment-only layer still owned by a human/writers-room read: whole-post abstraction, even-metronome nuance, cross-piece repetition.

**Group A — regex/phrase signals (add as constant lists, fire on count>0 or a tuned threshold):**

| New constant | Patterns (whole-word, line-anchored where noted) | Threshold | Severity |
|---|---|---|---|
| `EM_DASH_COUNT` | count of ` — ` (spaced em-dash) | > 0 | 1.5 (Farrice's #1 personal tell; shipped despite the rule) |
| `REVEAL_LEADINS` | `^here'?s the thing`, `here'?s what (?:happens when|nobody)`, `here is the part nobody`, `here'?s the (?:kicker|part)`, `what nobody (?:tells|talks about)` | > 0 | 2.0 |
| `MANUFACTURED_STAKES` | `let that sink in`, `read that again`, `keep you up at night`, `say it louder` | > 0 | 2.0 |
| `HINGE_PHRASES` | `that'?s where \w+ comes? in`, `let me break it down`, `what does this mean for you`, `are you ready to (?:embrace|adopt)` | > 0 | 1.5 |
| `CURRENT_ERA_VOCAB` | `ensuring`, `showcasing`, `highlighting`, `align(?:ing|ed)? with`, `\bembrace\b` | > 1 | 1.0 |
| `DOUBLED_ADJ_HEDGE` | `\w+er and (?:harder|deeper|wider|stranger|quieter)\b` | > 0 | 1.5 |
| `GENERIC_QUESTION_CLOSE` | interrogative on the final non-blank line matching `(?:what do you think|thoughts|agree or disagree|what would you add)\??` | > 0 (final line only) | 2.0 |
| `MASCOT_REVEALS` | `this is really just`, `as you probably know`, `(?:this )?has been around forever`, `to be fair,? this isn'?t new`, `i'?m no expert but`, `(?:this )?might be obvious but`, `grain of salt` | > 0 | 3.0 (binary FAIL philosophy) |
| `TOWN_CRIER` | ALL-CAPS runs ≥3 words, `\bHUGE\b`, `you NEED to`, exclamation density > 1 per 100 words | > 0 | 1.5 |
| `STRUCTURAL_EMOJI` | emoji adjacent to a markdown header (`^#+ .*[\U0001F000-\U0001FAFF]`) or at line-end before a blank line | > 0 | 1.5 |

**Group B — structural-move signals (need sentence/paragraph segmentation; add a `_split_paragraphs` helper alongside `_split_sentences` at L85):**

| New detector | Logic | Severity |
|---|---|---|
| `_check_contrast_reveal` | sentence-pair scan: a sentence containing `isn'?t / wasn'?t / it'?s not / that'?s not` immediately followed by a short affirmative reframe sentence. | 3.0 |
| `_check_aphoristic_endings` | last sentence of each paragraph; flag when ≥2 paragraphs end on a short declarative-reversal pattern (`subject + did/didn't + verb. + subject + reversal.`). | 2.5 |
| `_check_internal_anaphora` | within a single paragraph, ≥3 sentences sharing identical first 1-2 words ("She doesn't… She doesn't…"). Closes the gap left by `_check_parallel_structure`, which only sees same-first-word *line* starts. | 2.0 |
| `_check_gerund_tails` | sentences ending in a comma + `-ing` clause (`,\s+\w+ing\b[^.]*[.]$`); flag when count > 1. | 1.5 |
| `_check_micdrop_deflation` | a one-to-three-word final paragraph immediately preceded by a loaded aphoristic sentence. | 2.0 |

**Group C — quick fix (do while in the file):** L54 `r"\bargually\b"` → `r"\barguably\b"` (current typo never matches).

---

*One coherent author writes the body; this bank is the floor every piece clears before delivery. The proof of standard is a document that contains none of what it forbids.*
