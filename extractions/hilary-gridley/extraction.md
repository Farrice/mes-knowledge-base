# HILLARY GIDLEY — Mastery Extraction (Deep / Forge)

## Content Assessment

- **Source**: Marketing Against the Grain podcast (HubSpot), ~40 min video, 8,716-word transcript
- **Expert**: Hilary Gridley — led teams + AI adoption at Whoop; creator of "How to Be a Super Manager with AI" (Maven, running since Feb 2025, hundreds of managers); hills.substack.com
- **Secondary voice**: Kipp Bodnar (host, HubSpot CMO) — 3 attributable frameworks from upcoming book *Loop* (w/ Kieran Flanagan, Sept release). Kept in `references/loop-frameworks.md`, never blended (one author per body).
- **Domain**: AI-era management systems — judgment encoding, quality-bar articulation, anti-slop org design
- **Depth Tier**: Deep (forced — forge; corpus ≥8k RICH)
- **Genius Patterns**: 14 identified
- **Hidden Knowledge**: 7 tacit insights
- **Existing Overlap**: All current anti-slop assets are output-side detectors (prose_classifier, /anti-slop-audit, /oren-anti-slop-classifier, /satori-anti-ai-slop). `context-profile-architect` = machine-structure layer for profiles (complementary, downstream). No judgment-encoding pipeline exists in the roster.
- **Fidelity**: transcript-only (40-min video > visual cap); talking-head + one narrated slide → minimal loss. Blind-pass ceiling per Watch-to-Embody applies.

## Executive Summary

- **Core Genius**: Slop is not a tooling failure — it's an unarticulated quality bar. Gridley converts a manager's tacit judgment into narrow, deployable feedback tools via a repeatable pipeline (edit pairs → pattern extraction → plain-English pass/fail rubric → system prompt), so the bar exists *before* work is produced and the manager stops being the iteration bottleneck.
- **What Makes Them Different**: Everyone else fights slop at the output (detectors, bans, audits). She fights it at the *management layer* — upstream, structural, and teachable. Her tools are deliberately narrow ("editor for emails to an executive that you need a yes on"), derived from real edit history rather than generic principles, and designed to pass the kick-the-crutch test: remove the tool and the team is still better.
- **Deployable Skills**: mint evaluator tools from any before/after corpus; articulate "what good looks like" at 3 altitudes; redesign any workflow AI-native (backward from end state, nothing-is-a-surprise, one-step-further); run accountability-not-method conversations; install graduated iteration feedback ("too AI-generated, keep going").
- **Hidden Knowledge Captured**: the tool is a byproduct — the clarity ritual is the real product; AI's role in rubric mining is pattern-legibility, not quality knowledge; feedback tools change the social economics of iteration.

## Genius Patterns

### 1. Edit-Pair Rubric Mining (CROWN JEWEL)
- **What They Do Unconsciously**: Never introspects her standards directly ("I don't think I could tell you at this moment [what I look for]"). Instead externalizes them from evidence: a doc with Column A (drafts people sent her) and Column B (her revisions), uploaded with "what is the difference between column A and column B? What are the edits I make over and over? Help me spot the patterns."
- **Executable Behavior**: Collect ≥5 before/after pairs of one artifact type → ask AI to name recurring edit patterns → "turn those rules into criteria — give me five" → "write out in plain English what passing versus failing each criterion looks like" → "write that rubric as a prompt I can paste into a custom GPT / skill."
- **Deployment Context**: Any artifact class where an expert's edits exist: emails, briefs, posts, PRDs, ad scripts, code review.
- **Success Metric**: The rubric names patterns the expert recognizes as theirs but couldn't have listed cold; outputs judged against it match the expert's own verdicts.

### 2. Purpose-Driven Tool Scoping (Anti-Second-Brain)
- **What They Do Unconsciously**: Refuses the general clone. "I was NOT like, I'm going to make a second Hilary... I made this as specific as: an editor for emails that you are sending to an executive that you need to get a yes on. I've made dozens of these and they're all that specific."
- **Executable Behavior**: Scope every tool to one artifact × one audience × one outcome. Breadth comes from the *fleet* (dozens of narrow tools), never from one wide tool.
- **Deployment Context**: Any time someone proposes "an AI that knows everything about X."
- **Success Metric**: Tool name states artifact + audience + outcome; a user never wonders what to upload.

### 3. Backward-From-AI-Native Design
- **What They Do Unconsciously**: Rejects incrementalism reflexively. "We're past the point of starting from where we are today and adding some AI here and there... imagine a year in the future, your team is working in an AI-native way — what does a day in their life look like? Work backward from there."
- **Executable Behavior**: Fix the horizon (1 year), write the day-in-the-life at that horizon, then derive today's build order from the gap — never "which current task can AI do?"
- **Deployment Context**: AI adoption planning, team roadmaps, harness design.
- **Success Metric**: The plan contains capabilities that don't map 1:1 to any current task.

### 4. Nothing-Is-A-Surprise Principle
- **What They Do Unconsciously**: In her redesigns, every trigger that today requires noticing, being alerted, or going to find is converted to a proactively served signal. "If nothing was a surprise... the system has flagged this somehow."
- **Executable Behavior**: List every reactive trigger in a workflow; for each, name the agent/monitor that would surface it before a human asks.
- **Deployment Context**: Workflow redesign, competitive monitoring, ops.
- **Success Metric**: Count of workflow entry points that begin with a human discovering something → driven toward zero.

### 5. One-Step-Further Laddering
- **What They Do Unconsciously**: At every step asks "what if AI did the next thing? What if it went even further?" — and repeats until the human's only remaining moves are taste and judgment. Her worked example ladders: flag → 3 angles → landing-page mockups per angle → conversion estimates from site data → human picks → system cascades to ad copy + emails → CEO update with results ETA.
- **Executable Behavior**: For each workflow step, extend the AI's reach one station past comfortable, then again; stop only where a genuine taste/judgment decision lives.
- **Deployment Context**: Any workflow map; pairs with Pattern 4.
- **Success Metric**: Human touchpoints remaining are all choose/judge/approve moves, not assemble/fetch/format moves.

### 6. Concrete-Detail Vision Painting
- **What They Do Unconsciously**: Paints the future state "very concrete to the point of: what are the data sources this pulls from, what is the exact next action the AI does, what is the role of the human." Purpose is psychological: "reduces the fear, uncertainty and doubt... gives them confidence in you... gives them something to work toward."
- **Executable Behavior**: Every AI-native vision names data sources, exact next actions, and the human's role — no hand-waving verbs.
- **Deployment Context**: Change management, team briefings, harness specs.
- **Success Metric**: A team member can point at the picture and say which seat is theirs.

### 7. Three-Layer Quality Stack
- **What They Do Unconsciously**: Manages "all the way up and down the stack": (L1) how people spend their time / how they work → (L2) which 10 of the 100 possible projects are the right ones → (L3) per-artifact, what does good look like. Names L2 as the *other* slop: "I built these 10 applications that nobody's ever going to see or use... because I thought it was cool and only I thought it was cool."
- **Executable Behavior**: Audit each layer separately; never let per-artifact polish excuse portfolio slop or vice versa.
- **Deployment Context**: Quarterly planning, team audits, self-audit.
- **Success Metric**: Can answer at all three altitudes without conflating them.

### 8. Accountability-Not-Method Conversations
- **What They Do Unconsciously**: Refuses to police tool usage. "The job has never really been about the work — it's always been about accountability for the work." Thought experiment: you could always have secretly contracted your work out; the only reason anyone would know is if it wasn't good. "But you're still accountable... I see a lot of confusion — 'I told my team to use AI and now they're making all this bad stuff' — that's too focused on HOW to do the work. Have the conversation about what you're accountable for and what good looks like."
- **Executable Behavior**: Replace "how are you using AI" reviews with "what are you accountable for / what does good look like" contracts.
- **Deployment Context**: Slop confrontations, role definitions, delegation to agents.
- **Success Metric**: Zero conversations about tool choice; all conversations about outcome quality.

### 9. Graduated Iteration Feedback ("Too AI-Generated, Keep Going")
- **What They Do Unconsciously**: Breaks the bad/good binary that makes feedback feel like a character verdict. "It's not 'hey this is bad, you made slop, you're a bad person.' It's 'okay, this is a first take — it doesn't seem like you've put a ton of thought into it, so I'm not going to put a ton of thought into it. Take another pass, put your spin on it, then I'll sit down and put my spin on it.'"
- **Executable Behavior**: Feedback vocabulary: name the state (first take / too AI-generated), state the reciprocity (thought-in matches thought-back), assign the next pass, promise your pass after theirs.
- **Deployment Context**: Any received slop; installing shot→feedback→improve culture.
- **Success Metric**: Iteration count per artifact rises; defensiveness incidents fall.

### 10. Kick-the-Crutch Tool Design
- **What They Do Unconsciously**: Designs every tool as a teacher. "Build these tools in such a way that they are teaching your team how to do a good job and what good looks like — such that if you kicked the crutch out tomorrow they wouldn't be like 'oh no, I haven't learned anything.'"
- **Executable Behavior**: Feedback tools must show the criteria and the why, not just rewrite; test = would 6 months of use leave the person better with the tool removed?
- **Deployment Context**: Every tool build; procurement decisions.
- **Success Metric**: Team members start pre-empting the tool's feedback before running it.

### 11. Virtuous-Cycle / Slop-Doom-Loop Model
- **What They Do Unconsciously**: Sees org quality as a bidirectional flywheel: "teams that get better make the systems get better, which makes the people get better... versus cognitive rot where everyone outsources judgment, nobody questions outputs — people get worse, systems get worse, slop doom loop."
- **Executable Behavior**: Diagnose which direction the flywheel spins before any tooling intervention; tooling amplifies the current direction.
- **Deployment Context**: Org diagnosis, adoption strategy.
- **Success Metric**: Interventions target the spin direction, not the symptom.

### 12. Codify-Before-AI Dividend
- **What They Do Unconsciously**: Tests every AI practice against a no-AI world. "Even if we had no AI, if you took the time to assemble something like that and disseminated it, everything would improve immediately... I laugh with all this AI stuff because it's just good leadership and management."
- **Executable Behavior**: If a codification (context file, quality bar, taste profile) wouldn't help a purely human team, it's not context — it's prompt hackery. Build the ones that pay both ways.
- **Deployment Context**: Prioritizing which context/canon to build first.
- **Success Metric**: Artifacts get cited by humans in human-only settings.

### 13. Domain-Experts-Build Principle
- **What They Do Unconsciously**: "You need the domain experts to be the ones figuring out how to do this work... pulling in somebody from engineering who has no marketing expertise is not going to do a good job. So it kind of has to start decentralized" — then names the resulting failure modes (conflicting context, no canon, no bar) as the management problem to solve *without* recentralizing the building.
- **Executable Behavior**: Keep tool-building in domain hands; centralize only canon (source of truth) and the quality bar.
- **Deployment Context**: Org AI strategy, client engagements.
- **Success Metric**: Canon is shared; building stays distributed.

### 14. Editor-Not-Author Deployment (with Kipp, converged)
- **What They Do Unconsciously**: Splits work at the differentiation line: "the cognitive energy to get from 0 to 80% is a lot and it's not that differentiated. The differentiation comes in exercising your judgment and taste to get it from good to great. If good lands on your desk and your job becomes getting everything to great — that's a great way to work." Explicitly warns against over-focusing on automation ("starts the job AND finishes the job").
- **Executable Behavior**: Route the undifferentiated 0→80 to AI; reserve human cycles for 80→great; never automate the judgment station.
- **Deployment Context**: Every personal and team workflow split.
- **Success Metric**: Humans spend most cycles choosing between options and elevating, not assembling.

## Hidden Knowledge

- **The tool is a byproduct; the clarity is the product**: "I get so much clarity by going through this as a manager... even if you don't make any tools out of this, even if you just have conversations where you say that to people — you're going to be a better manager." The pipeline's real output is an articulated standard; the GPT is its container.
- **AI's role in rubric mining is legibility, not taste**: "AI is very good at spotting patterns." The standard lives in the edits; the model only makes it nameable. This is why generic "evaluate my email" prompts produce slop feedback — no evidence base.
- **Slop is a legibility event for management**: "If you're not really sure what you do or what value you bring, that is going to be made very apparent in the AI era." The slop wave doesn't create bad management, it exposes it. ("If you're just saying 'run this by Claude,' what value are you bringing?")
- **Feedback tools change the social economics of iteration**: waiting for manager feedback is slow AND socially expensive (inbox pile-up, gatekeeper dynamics). A tool makes iteration instant and shame-free — which is what actually installs the iterative culture.
- **Pick the demo artifact with asymmetric downside**: she teaches with *internal emails* — the "silly example" — because everyone has had their day blown up by one bad exec email ("Is it cool if we move the launch date?" → "No. Not even a little."). Small artifact, catastrophic tail = maximum buy-in.
- **Context is calibrated, not maximized**: "Here's every A/B test we've ever run, knock yourself out — that's not helpful. Likewise no information." Deciding what to *withhold* is the core management skill, identical for humans and agents.
- **Concreteness is a credibility instrument**: the detailed future-state picture exists to make the *manager* believable ("it gives them confidence in you because it seems like you know what you're doing") — vagueness reads as cluelessness and breeds spaghetti-at-the-wall AI behavior.

## Hall of Fame Exemplars

### Exemplar 1: The Executive Editor (complete tool build, end to end)
- **Context**: Her team kept torching their own work with bad exec emails (launch-date email → CEO detonation). She didn't want to edit emails forever.
- **The Example**: A custom GPT: paste a draft email to an executive → pass/fail per criterion + what to improve + suggested rewrites. Standards mined from her own edit history (Column A/B). Criteria surfaced: leads with the message in the first sentence; actionable; tone right; "is every single word adding clarity rather than ambiguity." Instructions written as plain-English rubric → pasted as system prompt. "Anyone has access to your brain."
- **What makes this excellent**: Every principle in one artifact — narrow scope (email × executive × get-a-yes), evidence-derived standards, plain-English pass/fail, actionable rewrites, manager-out-of-the-loop iteration, teaching residue.

### Exemplar 2: The Competitive-Response Redesign (AI-native situation rebuild)
- **Context**: Slide she teaches from. Situation: "Your CEO asks: why does a competitor's new campaign sound exactly like our positioning?"
- **The Example**: Today: reactive scramble — pull up their site, piece together socials, dump into a doc, whiteboard, photos nobody revisits, brief a designer, CEO pestering. AI-native: agent continuously scans competitor messaging vs yours → proactive flag → proposes 3 response angles, each with a landing-page mockup and a conversion estimate from your site data → human picks by taste → system updates the page and cascades ad copy + email sequences → "a couple hours, maybe less" → reply to CEO: "We're on top of it. New page shipped. Here's what we expect. Results in a week."
- **What makes this excellent**: Perfect demonstration of nothing-is-a-surprise + one-step-further + named data sources + the human seat as pure judgment. The situation didn't change; everything after it did.

### Exemplar 3: The Rubric-Mining Dialogue (verbatim method)
- **Context**: Answering "how did you actually build this?"
- **The Example**: "I literally had a document — in one column draft emails people had sent me, in the other my revisions. I uploaded it and said: what is the difference between column A and column B? What are you noticing about the edits I make over and over? Help me spot the patterns... Then: turn those rules into criteria — give me five criteria — and write out in plain English what passing versus failing looks like. Then you have a rubric, and you can run anything against a rubric... write that rubric as a prompt I can paste into a custom GPT or a skill. It's just English."
- **What makes this excellent**: The full pipeline in her own words — the calibration anchor for every evaluator-minting workflow in this skill.

### Anti-Exemplar: "Run It By Claude" Management
- **What mediocre looks like**: "Hey, run this by Claude before you send it" (no encoded standard — "there's no me in that equation"); the "second Hilary" general brain anyone can upload anything to; the builder who ships 10 apps nobody uses; the manager whose feedback is a bad/good verdict.
- **Why it fails**: No evidence-derived standard → generic feedback → outsourced judgment → cognitive rot → slop doom loop. Violates every criterion in the rubric below.

## Signature Moves

- **Backward-Paint**: First move on any AI question is to describe the AI-native end state in concrete detail, then derive the path. Never audits current tasks first. → **Deploy when**: any "how should we use AI for X" ask.
- **The Column A/B Upload**: Never introspects standards — assembles before/after evidence and asks the model to name the difference. → **Deploy when**: any "what does good look like" question that stalls.
- **One-Step-Further Probe**: Reflexively asks "and what if it went even further?" at each workflow station until only judgment remains. → **Deploy when**: mapping any workflow.
- **Narrow-Name the Tool**: Names tools as artifact × audience × outcome before building ("executive editor," not "email helper"). → **Deploy when**: any tool scoping moment.
- **Plain-English Pass/Fail First**: Writes what passing and failing look like in prose before anything becomes a prompt. → **Deploy when**: converting standards to tools.
- **Reciprocity Feedback Line**: "It doesn't seem like you put a ton of thought into this, so I'm not going to put a ton of thought into it — take another pass." → **Deploy when**: receiving slop.
- **Accountability Pivot**: Redirects every tool-usage complaint to "what are you accountable for and what does good look like." → **Deploy when**: AI-policing conversations start.

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| **Purpose specificity** | Tool has a stated use case | One artifact × one audience × one outcome in the name | Fleet of narrow tools; users never wonder what to upload |
| **Standard provenance** | Principles listed from memory | Derived from ≥5 real edit pairs | Continuously re-mined as new edits accumulate; expert recognizes patterns as theirs but couldn't have listed them cold |
| **Pass/fail legibility** | Criteria named | Plain-English passing vs failing per criterion | A new hire could self-grade accurately on day one |
| **Feedback actionability** | Verdict given | Verdict + what to improve | Verdict + suggested rewrites in the expert's register |
| **Teaching residue** | Tool assists | Tool explains its criteria | Kick-the-crutch: users pre-empt the feedback; removing the tool leaves them better |
| **Proactivity** | Workflow documented | Reactive triggers identified | Nothing is a surprise: every signal proactively served; entry points requiring human discovery → zero |
| **Human seat clarity** | "Human in the loop" asserted | Human decision points listed | Every remaining human touch is choose/judge/elevate; data sources and exact AI next-actions named |
| **Layer coverage** | Per-artifact quality addressed | Artifact + project-selection layers | All three layers (time / portfolio / artifact) managed distinctly |

## Methodology (progression)

1. **Diagnose** (slop roots + flywheel direction + three-layer audit) → produce: org/team slop diagnosis
2. **Articulate** (what does good look like — bar-setting ritual, backward-paint the AI-native day) → produce: quality bars + vision picture
3. **Encode** (edit-pair mining → criteria → plain-English rubric → system prompt) → produce: deployed evaluator tool
4. **Redesign** (situation mapping, nothing-is-a-surprise, one-step-further) → produce: AI-native workflow spec
5. **Install** (accountability contracts, graduated feedback vocabulary, iteration loops) → produce: operating culture
6. **Compound** (fleet of narrow tools; re-mine as edits accumulate; kick-the-crutch audits) → produce: the virtuous cycle

## Applied Intelligence

### Capability Unlocks
- **Evaluator-tool factory**: mint pass/fail feedback tools from ANY before/after corpus — including Farrice's felt-verdict logs, voice-ratchet history, and taste-calibration data already on disk.
- **AI-native redesign engine**: convert any reactive workflow into a proactive, one-step-further spec with named data sources and human judgment seats.
- **Client productization**: "we encode your judgment into tools your team uses" is a sellable engagement (Proof-to-Market adjacent); the Taste Profile (see Loop reference) is the flagship deliverable of that engagement.

### Market Signals
- Post-adoption pain has shifted (her course data, Feb 2025 → now): from "how do we get people to use AI" to "what do we do about the slop" — the market for quality-bar/judgment-encoding services is opening exactly where tool-adoption services are saturating.
- Managers as buyers: the fear is legibility ("what value do I bring") — offers that make managers *more* essential (their judgment, everywhere, on demand) sell; offers that route around them don't.

### System Enhancements
- The edit-pair pipeline is a general taste-compiler for this harness: every logged Farrice verdict is Column A/B feed. Bridge workflow ships in this skill.
- Nothing-is-a-surprise is an audit lens for the existing hook/launchd layer: which signals still require Farrice to notice?

## Implementation Pathway
- **24-Hour Quickstart**: Run the bar-setting ritual on one artifact class; mine one edit-pair corpus; deploy first evaluator tool.
- **7-Day Sprint**: Fleet of 3 evaluators (highest-asymmetric-downside artifacts first); one AI-native situation redesign shipped.
- **30-Day Integration**: Accountability contracts + graduated feedback installed; kick-the-crutch audit on all tools; Taste Profile productized offer drafted.
