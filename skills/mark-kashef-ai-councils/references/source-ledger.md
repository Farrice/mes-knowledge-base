# Mark Kashef AI Councils — Source Ledger

Every claim in `genius.md`, `SKILL.md`, and the workflow files traced to its
source, claim-by-claim, with a confidence label. Ground truth = the two files
under `extractions/mark-kashef/` (the only extraction directory matching this
expert):

| File | Size (bytes, `wc -c`) | Role |
|---|---|---|
| `extractions/mark-kashef/transcript.txt` | 27,910 | Primary source — full transcript of Kashef's "7 Agent Team Use Cases" YouTube video. Added to repo 2026-03-02 (`git log --diff-filter=A`). No publish date found inside the source itself. |
| `extractions/mark-kashef/extraction-report.md` | 6,254 | MES 3.0 extraction pass over the transcript — patterns, tacit knowledge, methodology. Also added 2026-03-02. |

No other Mark Kashef extraction directory (`mark-kashef-banana-squad`,
`mark-kashef-claude-claw`, `mark-kashef-perfect-agentic-os-kit`,
`mark-kashef-visual-design`) overlaps this skill's council/orchestration
content — checked by directory listing, not assumed.

## Claim-by-Claim

| Claim (as it appears in the skill) | Label | Source |
|---|---|---|
| "spawn agents" produces siloed sub-agents; "create an agent team" produces communicating teammates | VERIFIED | transcript.txt: "If you just say spawn agents, it could get confused between sub aents, which are very different in the way they work versus agent teams." |
| 3-to-5 agents is the sweet spot; more causes diminishing returns/token burn | VERIFIED | transcript.txt: "the rule of thumb, by the way, from anthropic is three to five agents is the sweet spot. Anything beyond that can lead to diminishing returns, overengineering, overthinking, and most importantly, a huge consumption of tokens." (Kashef attributes this rule of thumb to Anthropic; we have not independently verified Anthropic published this exact figure — the claim is VERIFIED as *something Kashef said*, LIKELY as an accurate Anthropic guideline.) |
| Agents converging on the same angle without a forced share-first step | VERIFIED | transcript.txt: "there seems to be heavy overlap. All three picked the three-level loading system and the kitchen analogy skills plus MCPs. I need to wait for the Twitter writers picks before I assign unique lead angles." |
| Council-generated copy still needs a "desopify" pass for AI tells | VERIFIED | transcript.txt: "I don't see too many M dashes... Looks decent, but still AI." / "you could desopify it with the right instructions." |
| Over-specifying steps Claude Code would infer anyway wastes prompt effort | VERIFIED | transcript.txt: "Now this is overkill. It would figure it out on its own. But again, the less thinking you have to make cloud code do, the more accurate the results." |
| Name exact roles instead of leaving agent choice to the LLM | VERIFIED | extraction-report.md, Methodology step 3: "Do not leave the agent choice up to the LLM. Specify roles like `competitor analyst`, `financial modeler`, `devil's advocate`." |
| Pitch-deck team = researcher, slidewriter, designer; "spawn three teammates with task dependencies" | VERIFIED | transcript.txt, pitch-deck use case |
| "each one has a markdown file of the full synthesis" | VERIFIED | transcript.txt, competitive-intel use case |
| $7,500 boot camp council keeps a Devil's Advocate seat | VERIFIED | transcript.txt, AI advisory board use case: "the devil's advocate who takes all the analysis and steps in to say maybe you shouldn't do this at all" |
| Pitch-deck build ran "150,000 tokens"; comparable technical tasks can run "300,000 tokens" | VERIFIED | transcript.txt |
| RFP build ran "180,000 tokens" | VERIFIED | transcript.txt (referenced in workflow/reference material, not directly quoted in genius.md — included here for completeness) |
| Boot camp council = market researcher, financial modeler, devil's advocate, competitive strategist, audience analyst | VERIFIED | transcript.txt |
| RFP deliverables: "the capability matrix of everyone in the company obviously hypothetical" + "the full proposal that you can review in pure markdown" | VERIFIED | transcript.txt |
| OpenClaw/MarkClaw build: architect, Telegram interface, skill router, memory, CLI teammates; "takes around probably 20 to 30 minutes to go from zero till the very end" | VERIFIED | transcript.txt |
| Boot camp conditional recommendation: "Start with a $2,000 course. Then upgrade to $7,500 within four to six months." | VERIFIED | transcript.txt |
| Single-phrase invocation example: "create an agent team to build a 12 slide pitch deck" | VERIFIED | transcript.txt |
| RFP firm context fed to the council: "15 person AI consulting firm," "40 plus projects" | VERIFIED | transcript.txt |
| "Anti-Sycophancy Architecture," "Behavioral Mandates Over Personality," "Shared Reasoning File," "Domain-Specific Council Configuration" as named patterns | LIKELY | These are the extraction pass's naming/synthesis of Kashef's demonstrated behavior in genius-patterns.md and hidden-knowledge.md (already in the skill pre-repair) — the underlying behaviors are VERIFIED in transcript.txt, but the pattern *names* are the extractor's labels, not Kashef's own terminology. No transcript quote uses these exact phrases.
| "Calibration Through Tracking" (Tacit 7) — tracking agent predictions over time to fine-tune mandates | UNCONFIRMED | No transcript passage describes prediction tracking across sessions. This tacit appears to be extrapolated/inferred rather than directly observed in the source. Flagged here rather than silently treated as sourced. |
| "Single-Phrase Invocation" as a formal "protocol" with named councils ("Strategy decision → Business Council") | LIKELY | The single-phrase mechanic ("create an agent team...") is VERIFIED; the specific "Business Council" naming convention in Pattern 6's example is illustrative, not a literal Kashef quote. |
| Hall of Fame Exemplars 1 & 2 (Go/No-Go council, Full-Stack Marketing assembly line) as fully worked scenarios | LIKELY | Composited/illustrative scenarios built from real patterns and role names Kashef uses (devil's advocate, market researcher, human tollbooth, etc.), not verbatim transcript scenes. The component parts are VERIFIED; the specific scenario framing is synthesized. |
| Anti-Exemplar ("The Agreeable Brainstorm") | UNCONFIRMED as a Kashef statement | This is a constructed counter-example illustrating what Pattern 4 / Tacit 1 fails to look like. Not sourced to a transcript quote — kept as pedagogical scaffolding, not attributed to Kashef.

## Notes on the "no source" rule

Before writing any UNCONFIRMED label above, `extractions/mark-kashef/` was
read in full (both files, sizes recorded via `wc -c` above) and cross-checked
against the exact phrase in question. No claim in this ledger is marked
UNCONFIRMED without first searching the transcript for a matching quote and
failing to find one.
