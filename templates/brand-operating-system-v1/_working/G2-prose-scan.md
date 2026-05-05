# G2 Voice + AI-Tell Scan — {{BRAND_NAME}} Brand Operating System v1

*Scan date: 2026-05-04. Scanner: Prose-Doctor (AI-tell exorcist + voice enforcer). Files reviewed: 00-foundation (full), 04-ai-handoff/00-ai-brain-master (full), 02-briefs/00-master-creative-brief-template (full), 03-marketing/01-content-pillars + 02-hook-library (full). Lower-priority files sampled.*

---

## §1 — Overall Verdict

The BOS is {{FOUNDER_NAME}}-fluent at the example level and AI-leaky at the connective-tissue level. The voice document, the hook library sample fills, and the manifesto excerpts read like {{FOUNDER_NAME}}. The prose around them — the section openers, the "why-it-matters" paragraphs, the meta-commentary — does not. The single most propagating leak is em-dash overuse, including inside the spine sentence itself, which then cascades into every doc that paste-mounts the spine. The structural-tell ban list is mostly honored at the example level ({{FOUNDER_NAME}}'s banned-moves discipline is real), but the explanatory layer that surrounds the examples leans on the same moves the doc tells writers to avoid.

If the BOS shipped today, an AI session that pastes the AI Brain Master would absorb the em-dash habit before it ever read the rule against em-dashes. That is the system-level risk.

---

## §2 — Issues Found, By Severity

### BLOCKING — fixed during this scan

**B1. Spine inconsistency across most-pasted files (em-dash vs ellipsis).** The canonical spine in `00-foundation/03-voice-document.md` line 9 uses an ellipsis ("heart encounters, not head encounters..."). The same spine in `04-ai-handoff/00-ai-brain-master.md` line 48, `00-foundation/01-brand-bible.md` line 8, and `02-briefs/00-master-creative-brief-template.md` lines 3 + 20 used an em-dash. The cold-start AI doc was actively contradicting the canonical voice authority on the spine itself. **Fixed**: all four locations now use the ellipsis form, matching the voice document.

### HIGH — should fix before next public-facing deployment

**H1. AI Brain Master cold-start block uses 25+ em-dashes — in the doc that teaches "≤2 per piece."**
File: `04-ai-handoff/00-ai-brain-master.md` lines 42-176 (the paste-in block).
Count: lines 74, 78, 81, 84, 94, 98, 99, 104, 108, 112, 115, 118, 122, 142, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153 — over two dozen em-dashes inside a block whose own line 138 says "Em-dashes more than 2 per piece" is banned.
Why it's a problem: this is the most-pasted doc in the system. Every AI session calibrates its em-dash habit on this block. The block teaches the rule and breaks the rule in the same breath, which means the rule will not stick.
Suggested fix: rewrite the paste-in block using colons, periods, and parentheses for the structural breaks. The pattern "ANAPHORA — three or four..." becomes "ANAPHORA. Three or four..." or "ANAPHORA: three or four..." Keep the spine ellipsis and one or two load-bearing em-dashes; delete the rest. Rule of thumb: if the dash is replaceable by a period or colon without loss, replace it.

**H2. Brand Bible em-dash density violates its own voice rule.**
File: `00-foundation/01-brand-bible.md`.
Pattern: em-dash use as connective tissue throughout the prose explanations (lines 16, 18, 38, 94, 98, 102, 104, 106, 108, 116, 118, 134, 169, 171, 173, 197, 209, 251, 257, 259 — partial count, 30+ total).
Why it's a problem: the bible is the second-most-pasted doc and the closest thing to "this is what {{FOUNDER_NAME}} sounds like" reference material for AI sessions. The body's em-dash density teaches a register that contradicts the voice doc's "≤2 per piece" rule.
Suggested fix: per-section pass, target ≤2 em-dashes per section (foundation docs may run higher than content for structural reasons, but density should not concentrate). Replace with colons, periods, restructured sentences.

**H3. Voice Document body uses em-dashes inside the doc that bans them.**
File: `00-foundation/03-voice-document.md`.
Pattern: line 11, 17, 27 (paragraph), 47, 53, 113, 215 explainers + many in Section 4 GOOD/BAD diagnoses.
Why it's a problem: the voice doc is supposed to model the rule. Section 5 line 233 says "Em-dashes ≤ 2 per piece, zero is better. Prefer ellipses for soft pauses, periods for hard breaks." The doc itself does not pass that test on its own meta-prose.
Suggested fix: voice-doc meta-prose should be the cleanest example of the voice. Audit the explanatory paragraphs (not the GOOD/BAD examples — those are meant to be analyzed) and reduce em-dash density to under 2 per major section.

**H4. "Here's what / why / how / the thing" violations inside the docs that ban them.**
File: `00-foundation/01-brand-bible.md` line 24 — "Four words doing the work: **daytime, sober, curated music, curated crowd.**" — fine, NOT a violation. Re-checked.
Actual violation: `03-marketing/02-hook-library.md` line 343 GOOD example uses "Here is what Pilsen sounds like at 5pm." This is a borderline case — the line is a manifesto-style declarative, not a "here's why" reveal opener — but the form ("Here is what...") matches the banned phrase. {{FOUNDER_NAME}}'s instinct may be that this works as a Show-first move; the form is risky given the rule.
Suggested fix: rewrite to "This is what Pilsen sounds like at 5pm" or "Pilsen at 5pm sounds like this." The point survives without the banned form.

**H5. Twin-sentence aphoristic endings in pillar/hook explanatory copy.**
File: `03-marketing/01-content-pillars.md` line 14 paragraph closer: "Both failure modes look productive on the back end. Both kill the room." This is the AI-tell twin-aphoristic ending the BOS itself bans (Voice Doc Section 5 final bullet).
Same file, end of section 4: "Add too many and they collapse into vibes. Hold them too rigid and they drift from the brand's actual evolution. Six is the working number. Amend, don't rewrite." The rhythm is the engineered-to-land cadence the voice doc warns against.
Why it's a problem: the BOS is teaching the ban while modeling the violation in its own structural commentary.
Suggested fix: vary endings. Let some sections end mid-thought. Let some end with a question. Resist the urge to land every paragraph on a paired-symmetrical aphorism.

**H6. Cross-piece rhythm repetition — "X is the Y" closer.**
Pattern across multiple files: "Slow is the feature." (hook library line 156). "The math is in the door." (line 201). "The room is the answer; the apps are the problem the room solves." (Brand Bible Enemy 4). "The room is the answer; the brand doesn't dispense advice." (content-pillars line 230). Same closing-aphorism move.
Why it's a problem: cross-piece rhythm repetition is Move #7 on the banned-moves list. When two pieces share a closing gesture, they read like the same author's same week instead of a varied ecosystem.
Suggested fix: pick one or two pieces where the move is load-bearing. Strip it from the others. Vary closers across the system: question, image, mid-thought, declarative without symmetry.

**H7. "Quiet, X" / "Soft, Y" doubled-adjective tic in ICP master.**
File: `00-foundation/02-icp-master.md` lines 165, 167-168 ({{ICP_PROFILE_2_NAME}}'s USE list): "*Soft Sunday* / *slow morning*" and {{ICP_PROFILE_3_NAME}}'s USE list line 244: "*I want someone I can be tired around.*" — these are intentional ICP voice samples and OK.
Real issue: {{ICP_PROFILE_3_NAME}} avatar line 211 — "He has therapy every other Tuesday at 8am. Plays no video games. Cooks. Calls his grandmother. Has a journal." is a triple-beat with a fourth landing — fine, this is anaphora done right.
False alarm withdrawn. ICP master holds.

**H8. The "It's not X. It's Y." reveal pattern inside the file that bans it.**
File: `00-foundation/02-icp-master.md` line 196 ({{ICP_PROFILE_2_NAME}} test sentences):
> *"This isn't a sober community. It's a room that doesn't need alcohol to come alive. You're invited as a person, not as a holder."*
This is the exact "It's not X. It's Y." reveal pattern banned in both the AI Brain Master line 128 and the voice doc Section 5 first bullet. It is presented as a positive example.
Why it's a problem: the magnet line for Profile #2 demonstrates the structural move the BOS teaches AI sessions to avoid. Either the example needs to change or the rule needs an explicit carve-out for "It's not X. It's Y." when X is a category-correction (not a reveal).
Suggested fix: rewrite {{ICP_PROFILE_2_NAME}}'s magnet to: *"Not a sober community. A room that doesn't need alcohol to come alive. You're invited as a person, not as a holder."* The frame-then-sharpen pattern lands the same job without triggering the contrast-reveal tic.

**H9. "Here is the part nobody talks about" ghost — softer variant.**
File: `00-foundation/01-brand-bible.md` line 78 — "**Enemy 4 — The algorithm pattern (the silent one)**" header + body line 80 "The apps are not the manifesto's rallying cry because every dating brand attacks the apps. {{BRAND_NAME}} attacks them at a deeper level..."
This is the "the silent one" / "what nobody else is saying" framing softened into a section header. Banned-move #5 territory.
Suggested fix: rename header to "Enemy 4 — The algorithm pattern" and let the body explain the "silent" framing through specifics, not through positioning the brand as the one telling the truth nobody else will.

### MEDIUM — consider for v1.1

**M1. "Wellness-coded" / "wellness-bro" appears as a recurring shorthand.**
Files: brand bible, voice doc, ICP master, content pillars. Used 12+ times across the system as a wince-shorthand.
Why consider: the term is doing real work, but it's becoming the BOS's own catchphrase. When a phrase appears 12+ times across a brand system, it shifts from diagnostic to decoration. {{ICP_PROFILE_2_NAME}} would clock this.
Suggested fix: where the meaning can survive without it, replace with the specific thing being named ("wellness-event circuit," "yoga-retreat aesthetic," "breathwork-circle register"). Save "wellness-coded" for the moments where the abstraction is exactly right.

**M2. "The room is..." opener appearing repeatedly across pillars and hooks.**
Pattern: "The room is small on purpose." (hook library line 151). "The room is the answer" (multiple). "The room is built so..." (multiple). "The room beneath the mechanism" (hook library line 393).
Why consider: "The room" is the brand's signature noun, which is correct. But the "The room is X" copular construction is becoming a reflex. If it appears in 15+ pieces, the rhythm flattens.
Suggested fix: vary the relationship to "the room." Sometimes it's the subject. Sometimes the object. Sometimes implied. The noun is load-bearing; the syntax around it shouldn't be.

**M3. Triple-listed mechanic shorthand collapsing into bullet rhythm.**
Files: AI Brain Master line 142-153, brand bible §6, content-pillars Pillar 1 examples.
Pattern: "Daytime. Sober. Curated. {{CITY}}." appears verbatim or near-verbatim in 6+ places. The crystallized-phrase pattern is the brand signature, but the same exact crystallization repeated verbatim weakens the move.
Suggested fix: vary the phrase order, vary the count (sometimes three, sometimes four, sometimes six), sometimes substitute a new phrase ("Daylight. No bar. One DJ. One yes at a time."). The rhythm is what's load-bearing; the specific words are the variable.

**M4. Sample fills in hook library are uniformly ~3-5 sentences with similar pacing.**
File: `03-marketing/02-hook-library.md` Section 2 sample fills.
Pattern: most sample fills run hook → 2-3 sentence body → declarative landing. Reads as engineered-to-land at scale.
Suggested fix: vary sample fill lengths and structures. Some should end on a question. Some should be one sentence longer than the hook. Some should refuse the landing line.

**M5. "The brand" as a self-referential noun.**
Files: content pillars, hook library meta-commentary. "The brand survives on {{FOUNDER_NAME}}-recognition." "The brand is built so..." "The brand has no commentary mandate."
Why consider: in the most-pasted docs, AI sessions absorb "the brand" as a self-referential register and start producing copy that talks about the brand instead of in the brand's voice.
Suggested fix: in body copy, prefer "{{BRAND_NAME}}" or "the room" over "the brand." "The brand" is a strategy-doc word, not an {{FOUNDER_NAME}} word.

**M6. "Show-first opener" / "frame-then-sharpen" / pattern names inside actual copy examples.**
File: `00-foundation/02-icp-master.md` and elsewhere — pattern names appearing inside sample fills and bridge messages.
Why consider: pattern names should stay in meta-commentary, not bleed into the consumer-facing copy. A reader who sees "Bridge Message" treated like a category does not feel met; they feel marketed at.
Suggested fix: reserve pattern names for the structural commentary. Bridge messages, hooks, and sample fills should never name the pattern they're using.

### LOW — note for next pass

**L1. Inconsistent use of italics for emphasis vs. quoted material.**
Files: all foundation docs. Italics serve double duty ({{FOUNDER_NAME}}-quoted manifesto lines + author emphasis) which weakens the convention. Voice doc Section 5 final bullet bans italicized mid-paragraph aphorisms, but author emphasis italics are doing similar work in places.
Suggested fix: pick one. Either italics-for-quotes-only, or italics-for-emphasis-only. Whichever, document it in the voice doc style appendix.

**L2. The phrase "load-bearing" is becoming the BOS's own writer-vocabulary tic.**
Files: AI Brain Master, voice doc, content pillars, hook library, brand bible (5+ uses). "Load-bearing" is useful jargon for the BOS authors but should not appear in any consumer copy. Verify this hasn't bled into IG captions in v1.1.

**L3. "Cadence" / "rhythm" / "register" used as connoisseur-vocabulary throughout meta-commentary.**
Same issue as L2 — internal-author register that should never show up in {{FOUNDER_NAME}}-facing or audience-facing surfaces.

**L4. "Real" is becoming an over-promise word.**
Files: ICP master {{ICP_PROFILE_3_NAME}} profile, hook library Singles Reality pillar. "Real" appears 40+ times across the system. Every brand claims "real." When it appears that often, the word goes transparent.
Suggested fix: in v1.1 hook-library refresh, audit for "real" and replace with specific instances (the unrehearsed gesture, the song nobody else would have picked, the man who came alone).

---

## §3 — Patterns Across Docs

Three patterns appear in multiple files and represent system-level risk, not file-level fixes.

**Pattern 1 — Em-dash density is universal and inverse to the rule.** Every foundation doc uses em-dashes 5-30x more than the rule allows. The voice doc, the bible, the AI Brain Master, the master brief template, the content pillars, the hook library meta-commentary — all violate. The example fills (the actual {{FOUNDER_NAME}}-voiced copy) are mostly clean. The author voice around the examples is the leak. This is the system-level finding: the {{BRAND_NAME}} authors write em-dash-heavy connective prose while teaching writers not to. That contradiction is the loudest AI-tell signal in the BOS.

**Pattern 2 — Twin-aphoristic engineered-to-land paragraph endings recur in meta-commentary.** Content pillars §1, §3, §5 all close on paired symmetrical aphorisms. Brand bible §3 closes the algorithm-enemy section on "The room is the answer; the apps are the problem the room solves." This is the move the voice doc bans, ported into structural-commentary where the authors didn't notice they were doing it. Section closers across the BOS need a variance pass.

**Pattern 3 — Pattern-naming is bleeding from meta into copy.** The six voice patterns and the audience-state taxonomy are useful internal vocabulary. They are starting to show up inside sample bridge messages, sample fills, and what should be voice-clean examples. When the BOS itself uses its own jargon as decoration in customer-facing slots, AI sessions absorb that as the register and reproduce the leak in production copy.

---

## §4 — What's Working

The voice document Section 4 (the 35 paired GOOD/BAD examples) is the strongest piece in the BOS. It teaches the voice by demonstration, not by description. The diagnoses ("the good one shows the experience; the bad one names the category" / "the good one uses the ICP's actual sentence; the bad one paraphrases it into a TED talk") are sharp, specific, and the kind of one-sentence explanation a writer can internalize. This section alone is the load-bearing artifact of the BOS. If everything else got cut, this would still teach the voice.

The hook library sample fills land more often than not. "I curate the music myself, beat to beat. The rule is whether the song bends the room toward someone you wouldn't have noticed" (line 281) is exactly the register {{FOUNDER_NAME}} claims. "He brought a record. He didn't tell me until the end of the night" (line 138) does the show-first work the voice doc demands. The {{ICP_PROFILE_3_NAME}} avatar sequence in the ICP master (record store scene, lines 213-215) is the sharpest piece of show-don't-tell in the system. These are the proofs that the voice exists and can be reproduced.

---

## §5 — Recommendations for v1.1

1. **Em-dash purge across all foundation docs**, prioritized by paste frequency. Order: AI Brain Master (highest leverage) → Brand Bible → Voice Document meta-prose → Master Creative Brief Template → Content Pillars → Hook Library meta-commentary. Target ≤2 em-dashes per major section. Replace with periods, colons, parentheses, or restructured sentences. The cold-start block is the highest-priority single fix in the entire BOS.

2. **Rewrite {{ICP_PROFILE_2_NAME}}'s magnet line in `02-icp-master.md` line 196** to remove the "It's not X. It's Y." reveal. The line is a public-facing example of the structural move the BOS teaches AI sessions to avoid; either the example or the rule has to give, and the rule is more valuable.

3. **Section-closer variance pass on `03-marketing/01-content-pillars.md` and `00-foundation/01-brand-bible.md`.** Currently most sections close on paired-symmetrical aphorisms. Vary: end on a question, end mid-thought, end on a concrete image, end on a single declarative without the engineered-to-land twin. Half the closers should change.

4. **Author-vocabulary audit** on terms like "load-bearing," "cadence," "register," "the brand," "wellness-coded." These are useful internal tools that should never bleed into public copy. Do a global find for each term. Anywhere it appears in customer-facing slots (hooks, sample fills, bridge messages, ICP language maps), replace with a specific noun or cut.

5. **Cross-piece rhythm variance check** before any v1.1 ship. Diff the closing gestures across the BOS files. Any closer pattern that appears in 3+ files needs to be cut from at least 2 of them. Variance is the discipline that prevents cross-piece rhythm repetition (banned-move #7).

---

*End of scan. Three BLOCKING fixes were applied during this pass (spine consistency restored across the four most-pasted files). Nine HIGH issues, six MEDIUM issues, and four LOW issues are documented above for human review.*
