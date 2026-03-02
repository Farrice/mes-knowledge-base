# Sherwin Wu — Genius Patterns

## 1. The Escape Hatch Removal Principle
**What They Do**: Forces innovation by eliminating fallback options. OpenAI has an internal team maintaining a 100% Codex-written codebase with NO manual coding escape hatch.

**Executable Behavior**: When adopting a new paradigm (AI agents, new workflow, new tool), deliberately remove the ability to fall back to old methods. This forces you to solve problems *within* the new paradigm rather than retreating to comfort. Problems become "how do I get the agent to do this?" not "I'll just do it manually."

**Deploy When**: You've committed to AI-first workflows but keep reverting to manual methods. When you want to discover the real limitations and best practices of a tool rather than bailing at the first friction.

**Success Metric**: You're discovering and documenting novel solutions within the new paradigm. Your team has built practices and workarounds that are genuinely innovative, not just copies of old methods with AI slapped on.

---

## 2. The Sorcerer's Apprentice Awareness
**What They Do**: Holds two competing truths simultaneously — AI tools are "wizardry" providing extraordinary leverage AND they require mature oversight to prevent cascading failures. Draws from SICP's 1980s programming-as-sorcery metaphor.

**Executable Behavior**: When managing multiple AI agents/threads, maintain the "wizard, not apprentice" posture. Know what each agent is doing at all times. Don't dispatch and sleep. Use seniority and domain knowledge to steer, not just delegate blindly. The moment you lose track of what your agents are doing, you've become the apprentice.

**Deploy When**: Managing 10-20 parallel Codex threads. Running multiple AI workflows. Any scenario where AI is doing work semi-autonomously and you feel the urge to "set it and forget it."

**Success Metric**: You can articulate what each agent is doing and why at any moment. No "brooms going crazy" moments where output has drifted without your awareness.

---

## 3. Context-as-Bottleneck Diagnosis
**What They Do**: When AI agents fail, immediately looks at what information the agent was *missing*, not what the agent did wrong. Frames failure as an information architecture problem, not a model capability problem.

**Executable Behavior**: When an AI agent produces bad output, don't blame the model. Audit: (1) What context was available? (2) What tribal knowledge was in your head but not in the codebase? (3) What documentation, comments, or MD files could bridge the gap? Fix the context, then re-run.

**Deploy When**: Any AI agent interaction that produces suboptimal results. Codex/Cursor/Claude failures. Agent workflow debugging. Before concluding "this model isn't good enough."

**Success Metric**: You have a growing repository of encoded context (MD files, code comments, skills files) that makes agents progressively more successful on the same types of tasks.

---

## 4. The Scaffolding Impermanence Principle
**What They Do**: Views ALL current tooling and frameworks as temporary scaffolding that models will eventually consume. "The models will eat your scaffolding for breakfast."

**Executable Behavior**: When building tools, products, or workflows around AI limitations, explicitly tag them as scaffolding. Ask: "Will a smarter model make this unnecessary?" Build for where models are going, not where they are. Invest deeply only in capabilities the model genuinely can't replicate (data access, distribution, domain expertise, UX).

**Deploy When**: Product architecture decisions. Feature prioritization. Deciding what to build vs. what to wait for. Evaluating AI startup investments. Assessing your own competitive moat.

**Success Metric**: Your product gets BETTER as models improve, not obsolete. You're positioned so model upgrades are tailwinds, not headwinds.

---

## 5. The Surgeon Management Model
**What They Do**: Treats every engineer as a surgeon — his job is to anticipate what tools they need before they ask. Spends 50%+ of time with top 10% of performers. Looks around organizational corners to pre-clear blockers.

**Executable Behavior**: As a manager or team lead: (1) Identify your top 10% performers, (2) Spend more than half your 1:1 and unstructured time with them, (3) Actively anticipate and remove blockers before they surface, (4) Let top performers explore and evangelize — their knowledge-sharing creates org-wide multipliers.

**Deploy When**: Engineering management. Team leadership. Any role where you're responsible for others' output. Client management where some clients are disproportionately valuable.

**Success Metric**: Top performers feel like they have "an army supporting them" when it's really just you. They're unblocked before they even realize they're about to be blocked.

---

## 6. The Bottom-Up AI Adoption Flywheel
**What They Do**: Identifies that successful AI deployments require BOTH top-down executive buy-in AND bottom-up practitioner evangelism. Pure top-down mandates produce negative ROI.

**Executable Behavior**: When deploying AI in any organization: (1) Secure executive sponsorship (budget + mandate), (2) Find the "technical-adjacent" enthusiasts — people who aren't engineers but are excited about AI, (3) Form a tiger team of these enthusiasts, (4) Let them explore, build practices, and knowledge-share, (5) Create excitement and pull adoption rather than pushing mandates.

**Deploy When**: Enterprise AI transformation. Selling AI consulting services. Deploying AI tools in non-tech companies. Any org with >20 people trying to adopt AI.

**Success Metric**: Employees are adopting AI tools out of genuine enthusiasm and demonstrated value, not compliance with performance reviews.

---

## 7. The N-Order Effect Thinking
**What They Do**: Doesn't stop at first-order predictions. When given "one-person billion-dollar startup," immediately cascades to 2nd, 3rd, 4th order effects: micro-company explosion → bespoke vertical SaaS boom → VC ecosystem transformation → distribution becomes king.

**Executable Behavior**: For any major AI trend, force yourself through 4 orders of effect: (1) What happens first? (2) What does THAT cause? (3) What does THAT unlock or destroy? (4) What new equilibrium emerges? The real opportunities are at orders 2-4, where competition is drastically lower.

**Deploy When**: Market analysis. Startup ideation. Investment decisions. Strategic planning. Content creation about AI trends. Any time you catch yourself making a first-order prediction.

**Success Metric**: You're identifying opportunities at the 2nd and 3rd order level — where timing advantages are larger — while everyone else piles into the obvious first-order play.

---

## 8. The Bitter Lesson Applied to Product
**What They Do**: Extends AI's "bitter lesson" (less architecture, more compute = better) to product building. Models eat scaffolding. Vector stores → file-based search. Agent frameworks → trust the model. The trend always favors simpler abstractions + smarter models.

**Executable Behavior**: When designing AI products: (1) Default to the simplest possible scaffolding, (2) Give the model tools, not constraints, (3) Assume the current "right way" will be obsolete in 12-18 months, (4) Bet on model capability improvement, not on your clever workarounds.

**Deploy When**: AI product development. Architecture decisions. Build vs. wait decisions. Evaluating whether a feature should be model-native or application-scaffolded.

**Success Metric**: Your product's core value proposition doesn't rely on compensating for model limitations. Each model upgrade makes your product better, not worse.
