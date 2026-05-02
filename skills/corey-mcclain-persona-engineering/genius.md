# Corey McClain — Genius Context
## Persona-First Context Engineering

---

## Core Genius

Corey McClain discovered that AI agents produce categorically superior outputs when given a **narrative identity** — not a role description, but a full life document with backstory, worldview, voice, and messy human details. The same model, same logic, same tools — but living inside a different world — produces work that crosses the line from "technically accurate" to "recognizably distinct." He formalized this into the LLMP framework: Logic, Library, Memory, Persona — where Persona is the 4th layer that envelops and elevates everything beneath it.

**What makes him different**: He doesn't treat persona as cosmetic branding on top of an agent. He treats it as a **structural performance layer** that changes how attention mechanisms allocate weight across the context window. The backstory — the dog named Rusty, the divorce, the mockta on weekends — has zero apparent bearing on the task. But it creates a "narrative container" that focuses the model in ways that specs alone cannot. He proved this experimentally with side-by-side comparisons across identical tasks.

---

## Genius Patterns

### 1. The Persona-as-Container Principle
The persona doesn't replace logic, library, or memory. It **envelops** them. Think of it less as a layer and more as an atmosphere — a pressure system that shapes everything the model produces within it. The agent doesn't reference the persona details in its output. It never mentions the dog or the family. But the presence of that narrative context changes the texture of every decision the model makes.

- **Executable Behavior**: Write persona documents that never appear in output but permanently alter output quality
- **Deploy when**: Building any agent expected to produce content, copy, design direction, or creative work
- **Success Metric**: Output is distinct enough that you could identify which persona produced it in a blind test

### 2. The Life Document (Not a Prompt)
What Corey writes is not a prompt. It's a biography fragment. Identity. Backstory — where they came from, family pressures, struggles. Worldview. Voice. The distinction matters because prompts instruct; life documents immerse. The model doesn't follow a persona instruction — it inhabits a persona context.

- **Executable Behavior**: Write 500-2000 word narrative documents covering identity, origin, formation, values, contradictions, and voice — in prose, not bullet specs
- **Deploy when**: Creating a new agent or upgrading an existing one from "functional" to "distinctive"
- **Success Metric**: The document reads like the opening chapter of a novel about a real person, not like a system prompt

### 3. The Specs-to-Narrative Conversion
You can take 500 characters of specs and rewrite them in narrative form and get better results from the narrative version. Every time. Narrative transportation (Green & Brock, 2002) works on transformers the same way it works on humans — the model's attention shifts from surface-pattern matching to contextualized inference when immersed in story.

- **Executable Behavior**: Convert any existing role/spec prompt into narrative prose and A/B test the outputs
- **Deploy when**: Any agent producing generic, "floor-level" outputs despite good logic and tooling
- **Success Metric**: Output moves from technically accurate to opinionated, textured, and recognizable

### 4. The Messy Details Principle
The magic lives in the details that have no apparent connection to the task. Walking the dog. Drinking mockta. Mom calling too much. Dad being supportive but distant. Being the oldest of six siblings. Thinking about a career change. These details create what Corey calls "a real person, even if it's fictional." The messier and more contradictory the details, the richer the container.

- **Executable Behavior**: For every persona, include 5-10 details that have zero logical connection to the agent's function
- **Deploy when**: Always. This is non-negotiable in Corey's methodology.
- **Success Metric**: Someone reading just the persona document cannot immediately guess what task the agent performs

### 5. Transistory vs. Steady-State Installation
Two deployment modes. Transistory: persona embedded directly in a prompt for one-off use. Disposable, fast, no setup, good for testing. Steady-state: persona written into a markdown file, uploaded to a workspace, persistent across conversations. Compounds over time as memory accumulates and you refine the document.

- **Executable Behavior**: Start every new persona as transistory (in-prompt). If the output quality is strong, promote to steady-state (workspace file)
- **Deploy when**: Transistory for experiments and one-offs. Steady-state for any agent you'll use more than 3 times.
- **Success Metric**: Steady-state agents produce measurably better outputs at week 4 than week 1

### 6. The Worldview-as-Decision-Engine
A persona's worldview implies a value system, which implies decisions. When two different personas face the same problem, they reach different audiences because their worldview filtered the solution space differently. This is not about "tone" — it's about the invisible pre-filtering that happens before a single word is generated.

- **Executable Behavior**: Write 3-5 worldview beliefs for every persona that constrain how they approach problems and what they prioritize
- **Deploy when**: Marketing agents, content agents, strategy agents — anywhere audience alignment matters
- **Success Metric**: Give the same task to two differently-worldviewed personas and get genuinely different (not just tonally different) outputs

### 7. The Anti-Default Principle
AI always gives you a response at the default floor. It's never trying to give you the best answer — it's giving you the "good enough" answer. The persona's function is to raise the floor. It forces the model off the default distribution into a specific, curated output space. Generic disappears. Distinct emerges.

- **Executable Behavior**: After installing a persona, test by running the exact same task with and without it. If the outputs are similar, the persona is too thin.
- **Deploy when**: Evaluating any persona installation
- **Success Metric**: Blind comparison reveals clear qualitative gap between persona vs. vanilla outputs

### 8. The Claude Insight
Claude is not the LLM — Claude is a personality profile installed on top of Anthropic's LLM. This is why Claude feels different from competing models. Corey uses this as proof-of-concept: if a personality layer makes Claude categorically more engaging than a raw model, then installing your own personality layers on any model should produce similar elevation.

- **Executable Behavior**: Study how Claude's personality manifests (tone, preferences, ethical stance) as a reference implementation for your own persona design
- **Deploy when**: Designing persona documents — use Claude as a benchmark for what "personality-elevated AI" feels like
- **Success Metric**: Your persona-installed agent feels as distinct from vanilla ChatGPT as Claude does

### 9. The Prada Principle (Luxury Doesn't Sell — It States)
When output quality is genuinely high, the copy doesn't need to sell. Prada's $6,500 dress page lists materials and measurements — no "flattering fit, effortless confidence." The persona-installed agent produced marketing copy that approached luxury-brand restraint: "Feels as good as it looks" instead of feature-dumping. The persona elevated the agent's taste to where it stopped trying to convince and started simply presenting.

- **Executable Behavior**: Evaluate agent output against the Prada test — is it selling or stating? If selling, the persona needs more sophistication in its worldview.
- **Deploy when**: Marketing, brand, and copy agents
- **Success Metric**: Output resembles what a $500/hr creative director would approve, not what a template would produce

### 10. The Router-Persona Integration
The persona lives in a markdown file. The router prompt references it. The model reads the persona first (or last — Corey says it's your choice), then executes the logic. The persona is always running in the background. It never surfaces in outputs explicitly. It's architectural, not decorative.

- **Executable Behavior**: Place persona file reference in router prompt's context loading sequence
- **Deploy when**: Every steady-state agent deployment
- **Success Metric**: Agent never mentions its own persona details, but outputs reflect them

---

## Hidden Knowledge

### 1. English Is Just as Good as Python
"These are large language models. It doesn't matter if it's Python, if it's C++ or any other coding language or if it's just plain English... English is just as good as C++ with a large language model." Markdown files are not "glorified" — they are the native language of instruction for LLMs. The old-establishment bias toward code-based agent definitions is a hangover from pre-LLM engineering.

### 2. The 65/35 Art-Science Split
Persona engineering is 65% art, 35% science. There's logic and order behind creativity, but the methodology resists full systematization. This is important because it means the quality ceiling is determined by creative taste, not technical precision.

### 3. The Memory Trap
"None of the memory systems that are being provided right now are going to hold up long term." OpenAI, Claude, and Gemini's built-in memory is insufficient. Corey built his own memory system with custom tagging for relevant recall — not reading through everything ever recorded, but pulling back specific memories when needed.

### 4. The PII-Strip Method
"You can take a real person, strip away their personal identifiable information, and then use that persona." Real people make better personas than fictional ones because their contradictions are authentic. But the PII must be removed. This is a practical shortcut for persona creation.

### 5. The Compound Effect
Steady-state personas "just get better" over time. Memory helps them improve. You rewrite them. You fine-tune things. This is the long-game argument — a persona installed today is an investment that compounds with every conversation.

### 6. The Worldview-Audience Alignment
"If I was marketing a product... I would try to think about who my audience is and if I was creating a persona for a marketing agent, then that persona would be generated in a fashion that the marketing assets, the copy, whatever they create, is going to appeal to that audience." The persona is not just about the agent's identity — it's reverse-engineered from the desired audience.

### 7. The Cyberpunk Origin
The Makoshi concept came from Cyberpunk 2077 — a portable shrine housing a digitized mind. Corey was trying to capture and maintain AI intelligence state around a particular topic, preventing the quality fluctuation that happens across sessions. The game metaphor became the architecture.

---

## Hall of Fame Exemplars

### Exemplar 1: The Aar Vance Marketing Asset
- **Context**: Same model (ChatGPT 5.5 extended thinking), same task ("create a marketing asset that sells a dress to women 25-35 for evening out"), vanilla vs. persona-installed
- **The Example**: Vanilla produced "Made for the night out / Flattering fit, effortless confidence / Your go-to dress for dinner, drinks, and everything after / Sleek silhouette, comfortable stretch, day-to-night polish." Vance produced a named collection, more intentional image composition (model looking away, city backdrop without building obstruction), copy organized into separate lines instead of run-on paragraph, and a single restrained tagline: "Feels as good as it looks."
- **What makes this excellent**: The comparison proves the persona effect is not about changing what the model says, but about changing *how it thinks about what to say*. The persona didn't add information — it added taste. The output moved from commodity marketing to luxury positioning without any explicit instruction to do so.

### Exemplar 2: The Transistory Freestyle
- **Context**: Corey deleted both previous conversations to prevent contamination, then freestyled a persona directly in-prompt: a graphic designer from inner-city Chicago, high school dropout, bad relationships, found passion in design, drinks mockta, walks her dog, reads self-help, annoying mom, supportive dad, oldest of six, considering midlife change.
- **The Example**: The freestyle persona — created in 60 seconds with zero planning — produced output that Corey rated between the vanilla and the fully-developed Vance persona. It introduced a brand name ("Nor Avenue"), a sub-brand ("Avenue Lounge"), the phrase "being seen," and compositional choices superior to vanilla.
- **What makes this excellent**: Proves that even a rough, improvised persona outperforms no persona. The barrier to entry is near-zero. You don't need a polished document — you need a *real person* described in enough detail to create a narrative container.

### Anti-Exemplar: The Vanilla Floor
- **What mediocre looks like**: "Beautiful image, made for the night out, flattering fit, effortless confidence, your go-to dress for dinner, drinks, and everything after. Sleek silhouette, comfortable stretch, day-to-night polish. Shop now." Run-on paragraph. Feature-dumping. Generic imagery (model looking at headline, building in frame). No brand identity. No restraint.
- **Why it fails**: This is the "default floor" — technically accurate, deployable, but indistinguishable from what any other user would get from the same model with the same task. It sells when it should state. It describes when it should evoke. It's "good enough" — which is the problem Corey's entire methodology exists to solve.

---

## Signature Moves

1. **The Life Document Write**: Write a persona as a biography fragment — prose narrative covering identity, origin, formation, worldview, voice, and messy details. Not a spec sheet. A life. → **Deploy when**: Creating any new agent or upgrading a generic one

2. **The Transistory Test**: Before committing to a full persona document, freestyle a rough backstory directly in a prompt, run a real task, and evaluate. If the output quality jumps, promote to steady-state. → **Deploy when**: Exploring whether a persona approach is worth the investment for a specific use case

3. **The Prada Comparison**: After generating output, compare it against what a luxury brand would publish. Is the agent selling or stating? If selling, the persona needs more sophistication. → **Deploy when**: Evaluating any marketing, copy, or design agent output

4. **The Controlled Delete**: Delete conversations and regenerate to prevent contamination when A/B testing persona vs. vanilla. Clean-room testing is essential for honest comparison. → **Deploy when**: Validating that the persona (not conversation history) is driving quality improvement

5. **The Worldview Reverse-Engineering**: Start with the target audience, then design the persona's worldview to naturally produce content that resonates with that audience. The persona is audience-shaped, not self-expression. → **Deploy when**: Building marketing or content agents for specific demographics

---

## Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| **Persona Depth** | Name, age, role, basic traits | Backstory + worldview + voice defined | Full life document with contradictions, messy details, and formation narrative |
| **Output Distinction** | Slightly different tone from vanilla | Recognizable style across multiple outputs | Blind-testable — you can identify which persona produced which output |
| **Narrative Transportation** | Persona reads like a character sheet | Persona reads like a profile | Persona reads like the first chapter of a novel about a real person |
| **Worldview Coherence** | Values listed but not integrated | Values shape some decisions | Every output decision traces back to worldview beliefs |
| **Voice Texture** | Vocabulary constraints set | Cadence + forbidden phrases defined | Voice is tactile — you can hear the person speaking when you read the output |
| **Task Independence** | Persona details somewhat related to task | Persona details partially unrelated to task | Most persona details have zero apparent connection to the task, yet elevate it |
| **Deployment Maturity** | One-off prompt installation | Workspace file with basic refinement | Steady-state installation with memory integration, compounding over time |

---

## Methodology: The LLMP Build Sequence

### Level 1 — Logic
What governs the work. Steps, rules, constraints, workflow sequence. This is the "what to do and how to do it" layer.

### Level 2 — Library
What the agent draws from. Tools, templates, knowledge base, examples, references, files. This is few-shot prompting embedded into everything it does — quality control through demonstration.

### Level 3 — Memory
How the agent remembers and recalls. Not platform-provided memory (which won't hold up long-term), but a custom memory base with its own tagging system. Pull back relevant memories on demand, not read through everything ever recorded.

### Level 4 — Persona
The installed life. Identity, backstory, worldview, voice, messy human details. This is the container that envelops Levels 1-3. It doesn't replace anything — it elevates everything. The booster pack. The narrative transportation layer that shifts the model off its default distribution.

**Build order**: Logic first → Library second → Memory third → Persona last (but Persona is the most important).

---

## Applied Intelligence

### Capability Unlocks
1. **Agent Identity Architecture**: Build agents whose outputs are indistinguishable from a specific human practitioner
2. **Quality Floor Elevation**: Permanently raise the baseline output quality of any agent by 30-50% through persona installation
3. **State Preservation**: Capture and maintain expert intelligence state across sessions using the Makoshi protocol
4. **Audience-Shaped Agents**: Reverse-engineer persona worldviews from target audience psychology for precision content

### System Enhancements
- Every Antigravity agent can receive a persona layer → system-wide output quality improvement
- Ghostwriting voice extraction → persona installation pipeline (extract voice → write life document → install persona)
- Client consulting productization: "Persona Installation" as a $2K-$5K standalone deliverable
