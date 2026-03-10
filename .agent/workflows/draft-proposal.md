---
description: "Draft a tailored freelance proposal from a job description — auto-matches skills, pulls proof points, writes in Farrice's voice"
---

# /draft-proposal — Freelance Proposal Generator

Paste a job description, get a copy-paste-ready proposal. Auto-detects which skill domain fits, loads the right proof points, and writes in Farrice's authentic voice.

## Usage

```
/draft-proposal [paste job description]
/draft-proposal --platform upwork [job description]
/draft-proposal --hat copywriter [job description]
```

**Examples:**
- `/draft-proposal` then paste a job listing — auto-detect everything
- `/draft-proposal --platform freelancer` then paste — force platform formatting
- `/draft-proposal --hat ai-architect` then paste — force a specific angle

---

## Execution

### 1. Parse the Job Description
// turbo
Extract these fields from the pasted text:

- **Title**: Job title or project name
- **Platform**: Detect from URL or keywords (Upwork, Freelancer.com, LinkedIn, WWR, Contra, PeoplePerHour, email/DM)
- **Budget/Rate**: Fixed price or hourly range
- **Required Skills**: Technical requirements, tools, methodologies mentioned
- **Deliverables**: What the client expects to receive
- **Timeline**: Deadline or expected duration
- **Client Info**: Company name, industry, any context clues

If a URL is provided instead of pasted text: use WebFetch to pull the listing content.

If the description is too vague to write a targeted proposal (missing both deliverables AND skills), ask ONE clarifying question:
> "What's the main deliverable they want? That'll let me target the proposal."

Otherwise, proceed — incomplete info is normal on freelance platforms.

### 2. Skill Match (Auto-Route)
// turbo
Score the job against 6 skill domains. Match using keywords from the listing:

| Domain | Match Keywords |
|--------|---------------|
| **AI Prompt Engineering** | GPT, prompt, ChatGPT, Claude, system prompt, custom GPT, AI tool, LLM, fine-tune |
| **AI Agent/Automation** | agent, automation, n8n, Zapier, Make.com, workflow, MCP, API, integration, pipeline, bot |
| **Copywriting** | sales page, funnel, email sequence, landing page, conversion, copy, VSL, direct response |
| **Content Strategy** | LinkedIn, ghostwriting, content calendar, thought leadership, brand content, social media strategy |
| **Sales Psychology** | persuasion, psychology, objection, identity, coaching, course, program, webinar, launch |
| **AI Consulting** | AI strategy, implementation, ChatGPT for business, AI adoption, digital transformation, AI training |

**Scoring**: Count keyword hits per domain. Pick the top 1-2 domains. If tied, prefer the domain with the higher rate range.

If `--hat` flag was provided, override the auto-match and use the specified domain.

**Announce the match:**
> "Routing to **[Domain]** — [1-sentence reason]. Writing as **[hat name]**."

### 3. Load Context (Conditional on Matched Domain)

**Always read** `FARRICE.md` (lines 1-30) for voice calibration.

Then load domain-specific files:

| Domain | Read These Files |
|--------|-----------------|
| AI Prompt Engineering | Count directories in `skills/` (for "110 skills" proof), count directories in `agents/` |
| AI Agent/Automation | `execution/parallel_swarm.py` (first 30 lines for architecture proof) |
| Copywriting | `skills/cardinal-mason-conversion-copy/SKILL.md` (capabilities overview) |
| Content Strategy | `skills/ghostwriting-voice-engine/SKILL.md` (capabilities overview) |
| Sales Psychology | `skills/jeremy-miner-identity-persuasion/genius.md` (first 50 lines for pattern proof) |
| AI Consulting | Count directories in `skills/` and `agents/`, count files in `extractions/` |

### 4. Select Proof Points

Based on matched domain, pick 2-3 proof points. These are REAL capabilities — never fabricate.

**AI/Technical proof pool:**
- 110 completion-engine skills across 63 expert domains
- 95 expert agents with structured memory and invocation protocols
- Parallel execution pipeline (async batch processing, retry logic, token budget management)
- 3-layer architecture: skill definition → genius context → workflow execution
- Production prompt engineering — not wrappers, context-engineered systems

**Copywriting/Content proof pool:**
- 28 coded persuasion patterns (identity-first architecture, frame engineering, consequence stacking)
- Full content packages built: positioning → sales page → email sequences → coaching frameworks
- McKinsey-grade strategy briefs produced for niche markets
- Ghostwriting voice capture pipeline with 10-point authenticity checklist

**Consulting/Training proof pool:**
- 6+ months systematically extracting and codifying expert methodologies
- Production-level evaluation rubrics for 63 different expert domains
- Custom quality gates: methodology fidelity, reasoning integrity, production readiness
- Daily workflow involves designing complex tasks, evaluating AI outputs, and prompt architecture

### 5. Draft the Proposal

**Voice rules (Farrice's authentic voice):**
- Warm, direct, confident — like talking to a smart friend, not pitching a client
- Lead with THEIR problem, not your resume
- Show you actually read their listing — reference a specific detail
- One concrete proof point from your system (not vague "years of experience")
- Clear deliverable + timeline — clients hire clarity
- No jargon dumping, no buzzword stacking
- Short sign-off: "— Farrice"

**Proposal structure (300-500 words max):**

```
[HOOK — 1-2 sentences]
Reference something specific from their listing that shows you read it.
Connect it to why you stopped scrolling / why this caught your attention.

[WHY I'M THE FIT — 3-4 sentences]
Connect your specific experience to their stated need.
Be concrete: "I've built X" not "I have experience in X."

[WHAT I'D DELIVER — bullet list]
- Deliverable 1 with timeline
- Deliverable 2 with timeline
- Deliverable 3 with timeline
(Match their stated requirements. Add one bonus they didn't ask for but would value.)

[PROOF POINT — 2-3 sentences]
One specific example from your system that proves you can do this.
Numbers are better than adjectives.

[NEXT STEP — 1 sentence]
What you need from them to get started. Makes it easy to reply.

— Farrice
```

**Platform-specific formatting:**

- **Upwork**: Keep under 300 words. First line is the ONLY thing visible in the proposal preview — make it count. No "Dear Hiring Manager." No attachments mention.
- **Freelancer.com**: Can go to 500 words. For large projects, propose a pilot/phased approach (Phase 1 = small deliverable to prove quality, Phase 2 = full scope).
- **LinkedIn / Email / DM**: More conversational. Can reference their profile, shared connections, or recent posts if relevant. Include a subject line suggestion.
- **We Work Remotely / RemoteOK**: Structure as a cover letter with clear sections (Background, Relevant Experience, Availability, Why This Role).
- **Contra / PeoplePerHour**: Mid-length (200-400 words). Focus on portfolio-style proof — what you've built, not what you know.

### 6. Pricing Guidance

Based on the job's posted budget and matched skill domain:

| Domain | Hourly Range | Fixed Project Range |
|--------|-------------|-------------------|
| AI Prompt Engineering | $75–150/hr | $500–3,000 |
| AI Agent/Automation | $100–200/hr | $1,000–10,000 |
| Copywriting | $50–100/hr | $500–3,000 |
| Content Strategy | $75–150/hr | $2,000–5,000/mo |
| Sales Psychology | $75–125/hr | $1,000–5,000 |
| AI Consulting | $100–250/hr | $2,000–15,000 |

**Bid logic:**
- If client posted a budget within your range: bid at or slightly above their midpoint
- If client budget is below your range: bid at the low end of YOUR range with a scope-reduction note ("For $X, I'd deliver [reduced scope]. For the full scope, $Y is more realistic.")
- If no budget posted: bid at your midpoint with "flexible based on scope" language
- For first projects on a new platform: consider bidding 10-20% below your range to land the review

### 7. Output

Present the proposal in a clean, copy-paste-ready block:

```markdown
---
## PROPOSAL (Copy/Paste Ready)
---

[Full proposal text here]

— Farrice
```

Then add the notes section:

```markdown
---
## Proposal Notes (for Farrice only — do not paste)
- **Platform**: [detected or specified]
- **Skill domain**: [matched domain(s)]
- **Hat**: [AI Architect / Copywriter / Content Strategist / Sales Psychologist / AI Consultant]
- **Proof points used**: [which specific ones]
- **Suggested bid**: $[amount] — [1-sentence rationale]
- **Confidence**: [High/Medium/Low] — [why]
- **Customize before sending**: [specific things Farrice should personalize — client name, company details, portfolio links]
```

---

## Dependencies

| Asset | Path | Purpose |
|-------|------|---------|
| Personal context | `FARRICE.md` | Voice calibration, background |
| Domain routing | `DOMAIN_REGISTRY.md` | Skill matching reference |
| Jeremy Miner genius | `skills/jeremy-miner-identity-persuasion/genius.md` | Sales psychology proof |
| Cardinal Mason skill | `skills/cardinal-mason-conversion-copy/SKILL.md` | Copywriting proof |
| GVE skill | `skills/ghostwriting-voice-engine/SKILL.md` | Content strategy proof |
| Parallel swarm | `execution/parallel_swarm.py` | AI automation proof |

---

## Chain Compatibility

- **Standalone** (primary use): Paste a job listing, get a proposal
- **Chains from**: Manus.ai gig-hunter output, manual browsing, Upwork job alerts
- **Chains to**: Manual submission on platform (copy/paste the proposal)
- **Batch mode**: Run multiple times for different listings — each invocation is independent

---

## Notes

- Proposals are NOT saved to disk by default — they're displayed for copy/paste. If Farrice wants to save, he can copy to `.tmp/proposals/`.
- The quality gate from `directives/quality_gate.md` runs silently on the proposal output.
- If a listing matches multiple domains equally, pick the one with the higher rate range (optimize for revenue).
- Never fabricate capabilities. If Farrice doesn't have a matching skill, say so and recommend either passing on the listing or being transparent about learning curve.
