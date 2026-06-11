# Deep Research Report: AI Skill/Plugin Package Demand And Farrice's Wedge

- Date: 2026-05-27
- Objective: validate whether AI skill/plugin packages are real buyer demand, who buys them, what they pay for, what is slop, and what wedge Farrice can own.
- Source Ledger: _active/deep-research-os/02-research/ai-skill-plugin-market-source-ledger-2026-05-27.md
- Research stack executed: Virtuoso Orchestration, Gemini Deep Research Max, Apify Reddit social listening, live web verification.
- Research stack attempted but blocked: Perplexity API returned an insufficient-quota response, so it is not used as evidence.
- Real Codex subagents spawned: false.

## Verdict

**Offer-market fit verdict: proceed, but do not lead with generic prompt packs.** Verified evidence supports demand for reusable AI skills, workflow kits, and agent capability packages. The strongest wedge is not selling prompts. It is **repairing and packaging repeatable AI work into verified, portable execution kits that install cleanly, trigger reliably, and prove they are not slop.**

**Confidence: medium-high.** The category has real supply, real user pull, and early marketplace payment behavior. The limitation is that paid demand is still thin at the standalone skill-file level; the faster cash path is a service-first diagnostic and implementation sprint that later becomes a sellable skill/plugin bundle.

## Claim Labels

- verified: source-backed from official docs, marketplaces, papers, or opened pages.
- directional: real signal but not statistically representative.
- inference: strategy conclusion from multiple signals.
- unverified: not proven by this run.

## Virtuoso Trace

| Field | Result |
|---|---|
| Primary route | `/deep-research-os` |
| Owner | Deep Research OS |
| Support stack considered | research-intelligence-agent, deep-research, research-swarm, parallel-research, research-quality-gate |
| Support stack executed | Gemini Deep Research Max, Apify Reddit, live web verification, quality gate |
| Expert lenses applied | market intelligence, ICP deep canvass, competitor wedge, anti-slop quality gate |
| Subagent packets prepared | deep research, competitive intelligence, ICP canvass |
| Real subagents spawned | false |
| External actions | research provider calls only; no publishing, DMs, connector writes, or marketplace writes |

## Market Map

| Category | Buyer Promise | Evidence | Pricing Signal | Wedge Implication |
|---|---|---|---|---|
| Prompt marketplaces | Buy individual prompts or subscribe to prompt libraries. | PromptBase says it offers 270k prompts, 450k+ users, and visible prompt prices such as 2.99 USD to 6.99 USD. https://promptbase.com/ | verified: commodity prompt prices cluster around impulse-buy pricing on PromptBase. https://promptbase.com/ | Competing here as a generic seller is low-margin. Use it as distribution, not the main strategy. |
| Prompt subscriptions | Heavy users want many prompts with less purchase friction. | PromptBase Select gives buyers 10 downloads per month for 14 USD annual monthly equivalent or 19 USD monthly, and creators earn 1 USD per subscriber download. https://promptbase.com/blog/promptbase-select-creators | verified: subscriptions are aimed at agencies, heavy users, and power buyers. https://promptbase.com/blog/promptbase-select-creators | Bundle logic matters, but the economics are small unless volume exists. |
| SKILL.md marketplaces | Buy portable agent skills that work across Claude, Codex, Cursor, Gemini CLI, and other tools. | Agensi positions itself as an AI agent skill marketplace for one-time purchases and instant downloads. https://www.agensi.io/ | verified: Agensi says skills work across Claude Code, OpenClaw, Codex CLI, Cursor, and 20+ agents. https://www.agensi.io/ | Portability is a demand driver. Farrice's assets should be cross-agent where possible. |
| Skill pricing guides | Creators need practical pricing, not theory. | Agensi's guide says single-purpose skills sell at 3 to 9 USD and comprehensive multi-file skills at 12 to 25 USD; creators keep 80% of each sale. https://www.agensi.io/learn/how-to-price-skill-md-skills | verified: a plain SKILL.md is treated as lower value than a kit with scripts, references, examples, and documentation. https://www.agensi.io/learn/how-to-price-skill-md-skills | Sell complete verified kits, not naked markdown. |
| Paid CLI marketplaces | Buyers want one-command install and validation. | SkillHQ says buyers install validated Claude Code SKILL.md packages and Custom GPT configs with one CLI command, while creators earn 85% of each sale. https://skillhq.dev/ | verified: SkillHQ's public positioning is "paid marketplace," "validated," and "single CLI command." https://skillhq.dev/ | Installation friction is part of the product, not an afterthought. |
| Agent-native workflow platforms | Users want skills to execute end-to-end, not just advise. | Manus markets agent skills as custom workflows executed in a secure sandbox, with one-click import and a team library. https://manus.im/features/agent-skills | verified: Manus docs show building from successful interactions, uploading skills, importing from GitHub, and slash-command invocation. https://manus.im/docs/features/skills | The product promise should move from "prompt" to "workflow that runs." |
| Open skill ecosystems | Supply is large and quality uneven. | An arXiv paper analyzes 40,285 publicly listed skills and notes redundancy, supply-demand imbalance, and safety risks. https://arxiv.org/abs/2602.08004 | verified: SkillsBench reports 47,150 unique skills from 6,323 repositories and a mean quality score of 6.2 out of 12. https://www.skillsbench.ai/skillsbench.pdf | Quality verification is a wedge because supply alone is noisy. |
| Security and governance | Buyers fear hidden unsafe instructions and bad automation. | A SKILL.md supply-chain paper frames skills as modular filesystem packages whose natural-language metadata can affect admission, surfacing, selection, and loading. https://arxiv.org/abs/2605.11418 | verified: security risk is a real category issue, not just user anxiety. https://arxiv.org/abs/2605.11418 | Add security scan, permissions boundary, test prompts, and failure receipts to every paid kit. |

## ICP Deep Canvass

| ICP | What They Believe | Trigger Event | What They Pay For | Resistance | Offer Angle |
|---|---|---|---|---|---|
| AI power user / developer | Skills are useful, but random markdown from GitHub feels risky. | They waste time searching, auditing YAML, or debugging triggers. | verified: one-command install, validation, security scan, exact workflow fit. https://skillhq.dev/ | Directional Reddit objection: why pay when free alternatives exist? https://www.reddit.com/r/ClaudeCode/comments/1sulwsg/i_built_a_skill_marketplace_because_i_was_tired/ | Verified skill kit for one painful workflow, with tests and install receipt. |
| Solo operator / service provider | AI helps, but the output still needs too much rescue. | They keep re-explaining the same process or editing generic output. | inference: a diagnostic that turns one repeated AI failure into a repeatable workflow kit. | They do not know how to install or maintain skills. | Turn one messy workflow into a reusable agent-ready kit. |
| Agency / consultant | They need reusable delivery assets, not bespoke prompt chaos. | They repeat onboarding, research, audits, reports, or content ops across clients. | verified: bundles and comprehensive skills can justify higher pricing when scripts, references, examples, and docs are included. https://www.agensi.io/learn/how-to-price-skill-md-skills | Fear of commoditizing their method or leaking client logic. | Private client delivery skill library with proof receipts and permission gates. |
| Internal ops / RevOps / GTM builder | Generic automation breaks when judgment is required. | They need research, enrichment, scoring, CRM hygiene, or support triage with judgment. | verified: Manus positions skills as reusable workflows that execute in a secure environment. https://manus.im/features/agent-skills | Governance, audit logs, and data boundaries. | Outcome-specific workflow kit with validation, refusal rules, and audit trail. |
| Low-end prompt buyers | They want shortcuts without learning prompt engineering. | They buy cheap packs or prompt tools to stop staring at blank screens. | directional: prompt-pack Reddit language emphasizes under-10-USD shortcuts and prompts that actually work. https://www.reddit.com/r/u_MillionaireMindset62/comments/1thwnie/nohype_technical_analysis_of_easy_prompt_creator/ | Low trust, high hype, low budget. | Use this segment for lead magnets, not the premium wedge. |

## Social Listening Ledger

| Source | Speaker Class | Signal | Confidence | Implication |
|---|---|---|---|---|
| Reddit via Apify: Claude skills worth installing. https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/ | Claude power user | "Most publicly available skills hurt more than they help." | directional direct quote | Quality and selectivity are core objections. Sell fewer, stronger kits. |
| Reddit via Apify: same thread. https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/ | Claude power user | "Trigger reliability is not guaranteed." | directional direct quote | Every kit needs explicit invocation, trigger tests, and fallback instructions. |
| Reddit via Apify: same thread. https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/ | Claude power user | "The difference between output with and without this skill is not subtle." | directional direct quote | Before/after demos can sell if they are specific and credible. |
| Reddit via Apify: Agensi update. https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/ | Marketplace builder | Users asked for more skills, better discovery, security, and clearer information before download. | directional summary | Trust and discovery are product features. |
| Reddit via Apify: Agensi update. https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/ | Marketplace builder | Skills grew from 6 to 80+, downloads crossed 300, and first paid sales came in. https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/ | directional metric | Early demand exists, but scale is still emerging. |
| Reddit via Apify: Agensi agent-native post. https://www.reddit.com/r/AIAgentsInAction/comments/1tdbvrg/i_built_an_agentnative_marketplace_for_ai_skills/ | Marketplace builder | Reports 18,000+ active users, 350+ skills, 80+ creators, 41 paid transactions, and asks what would make people pay 5 to 15 USD. https://www.reddit.com/r/AIAgentsInAction/comments/1tdbvrg/i_built_an_agentnative_marketplace_for_ai_skills/ | directional metric | Usage can outrun paid conversion; the paid wedge must be sharper than "browse skills." |
| Reddit via Apify: SkillHQ post. https://www.reddit.com/r/SideProject/comments/1su8v82/im_building_a_cli_marketplace_for_claude_code/ | Marketplace builder | Developer buyers resist subscriptions but accept one-time purchases with clear ROI; narrow skills beat vague ones. https://www.reddit.com/r/SideProject/comments/1su8v82/im_building_a_cli_marketplace_for_claude_code/ | directional summary | Use one-time productized offers and name the exact workflow pain. |
| Reddit via Apify: Agensi paid skepticism. https://www.reddit.com/r/ClaudeCode/comments/1sulwsg/i_built_a_skill_marketplace_because_i_was_tired/ | Skeptical buyer | "Why would anyone pay 10$ for a skill when things like gsd etc are free?" | directional direct quote | Generic paid skills will face brutal free-alternative pressure. |
| Reddit via Apify: Agensi paid skepticism. https://www.reddit.com/r/ClaudeCode/comments/1sulwsg/i_built_a_skill_marketplace_because_i_was_tired/ | Skeptical community member | "This sub is just becoming one gigantic collection of 'Look at me, buy my vibe'." | directional direct quote | Promotional framing creates resistance. Lead with proof and useful teardown, not hype. |
| Reddit via Apify: prompt-pack thread. https://www.reddit.com/r/u_MillionaireMindset62/comments/1thwnie/nohype_technical_analysis_of_easy_prompt_creator/ | Low-end prompt seller / affiliate | "People are starving for prompts that actually work." | directional direct quote | The bottom market sells pain relief, but its language is hype-heavy and trust-poor. |
| Reddit via Apify: SillyTavern preset thread surfaced by prompt-pack query. https://www.reddit.com/r/SillyTavernAI/comments/1tkpter/nemo_engine_v10_celebrating_1_year/ | AI preset user | User says the system sounds cool but complicated and wants it to prevent repetitive output without constant manual pushing. | directional summary | Buyers want complex systems made usable, with controls and plain-language installation. |

## What Buyers Actually Pay For

| Paid Object | Buyer Expectation | Evidence | Farrice Packaging Rule |
|---|---|---|---|
| Single-purpose skill | One exact recurring task, fast install, low risk. | Agensi prices single-purpose skills at 3 to 9 USD. https://www.agensi.io/learn/how-to-price-skill-md-skills | Use as lead product or marketplace test, not the premium core. |
| Comprehensive skill kit | SKILL.md plus scripts, examples, references, README, and validation. | Agensi prices comprehensive skills at 12 to 25 USD. https://www.agensi.io/learn/how-to-price-skill-md-skills | This is the minimum viable paid digital product. |
| Validated CLI skill package | One-command install, license check, validation before listing. | SkillHQ's public offer centers on paid validated packages and 1-command install. https://skillhq.dev/ | Productize install and test receipts. |
| Prompt pack | Cheap creative or productivity shortcut. | PromptBase shows many prompt prices around 2.99 to 6.99 USD. https://promptbase.com/ | Use for distribution and discovery, not authority positioning. |
| Custom workflow rescue | Diagnose one messy AI workflow and turn it into a repeatable kit. | inference from buyer pain across Agensi, SkillHQ, Manus, Reddit, and local service-first assets. | This should be the first cash offer: 49 to 99 USD teardown, 250 USD diagnostic, 500 to 1,000 USD implementation sprint. |

## Slop Definition

AI skill/plugin slop is not just ugly writing. In this category, slop means:

| Slop Type | Signal | Evidence | How Farrice Avoids It |
|---|---|---|---|
| Generic prompt library | Many prompts, little context, no verification. | PromptBase volume and low price points show prompt supply is abundant. https://promptbase.com/ | Sell outcome-specific kits, not broad libraries. |
| Untrusted markdown | Buyer must inspect YAML, hidden instructions, and dangerous commands. | Reddit marketplace posts repeatedly cite security scans and trust as needed features. https://www.reddit.com/r/ClaudeCode/comments/1sulwsg/i_built_a_skill_marketplace_because_i_was_tired/ | Include permission boundary, secret scan checklist, and refusal rules. |
| Poor trigger design | Skill does not fire when needed or fires when irrelevant. | Claude docs say descriptions help Claude decide when to load skills; Reddit users complain trigger reliability is not deterministic. https://code.claude.com/docs/en/skills | Include trigger tests and explicit slash command fallback. |
| No install path | Buyer has to figure out folders, commands, or imports. | Manus and SkillHQ both sell simplicity through one-click or one-command install. https://manus.im/docs/features/skills https://skillhq.dev/ | Every offer includes install receipt and known-working check. |
| No proof of output improvement | Skill looks good on paper but does not improve real outputs. | Agensi update says surfacing which skills perform well remains unsolved. https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/ | Include before/after task evidence, not just skill names. |
| Security blind spot | Skill registry or selection can become a supply-chain risk. | SKILL.md supply-chain risk paper identifies semantic supply-chain risk. https://arxiv.org/abs/2605.11418 | Security and permission gates become sales features. |

## Competitor Wedge

| Competitor Type | Strength | Gap | Farrice Wedge |
|---|---|---|---|
| PromptBase-style marketplace | Traffic, simple purchase behavior, huge prompt catalog. https://promptbase.com/ | Prompts are cheap and often not integrated into workflows. | Move buyers from prompt to verified workflow kit. |
| Agensi-style SKILL.md marketplace | Category focus, cross-agent standard, creator economics. https://www.agensi.io/ | Paid conversion appears early but thin; discovery and proof remain open gaps. https://www.reddit.com/r/AIAgentsInAction/comments/1tdbvrg/i_built_an_agentnative_marketplace_for_ai_skills/ | Proof-backed premium kits with install, validation, and buyer-ready documentation. |
| SkillHQ-style CLI marketplace | Paid positioning, one-command install, anti-piracy. https://skillhq.dev/ | Developer-first framing may miss service operators and creative/business workflows. | Business workflow rescue kits for creators, agencies, and solo operators. |
| Manus | Strong execution story, sandbox, team libraries. https://manus.im/features/agent-skills | Platform-bound; users still need excellent workflow design and curation. | Portable orchestration method that works inside Codex/Claude/Manus-style environments. |
| Free GitHub/community skills | Free supply and fast copying. | Trust, curation, security, and proof are inconsistent. SkillsBench mean quality score is 6.2 out of 12. https://www.skillsbench.ai/skillsbench.pdf | Trust premium: tested, narrow, installable, documented, and maintained. |

## Wedge Farrice Can Own

**Name:** Guessproof Skill/Workflow Rescue.

**Positioning:** Stop re-explaining the same AI task. Send me one AI workflow that keeps failing, drifting, or producing generic output. I will diagnose where the AI is guessing, capture the hidden judgment, and turn it into a reusable skill/workflow kit with validation.

**Why this wedge fits the evidence:**

- verified: Claude and Manus both normalize skills as reusable, slash-invocable, portable workflow units. https://code.claude.com/docs/en/skills https://manus.im/docs/features/skills
- verified: marketplaces already price simple skills cheaply and comprehensive skills higher when they include references, scripts, and examples. https://www.agensi.io/learn/how-to-price-skill-md-skills
- directional: buyers and builders are asking for security, discovery, clarity, and proof that a skill works. https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/
- inference: service-first delivery lets Farrice capture cash faster than waiting for passive marketplace sales.

## Offer-Market Fit Decision

| Decision | Verdict |
|---|---|
| Is there buyer demand? | verified/directional yes: OpenAI, Claude, Manus, Agensi, SkillHQ, PromptBase, papers, and Reddit all show category activity. |
| Is standalone skill-file revenue enough by itself? | directional no: marketplace posts show paid transactions but also thin willingness to pay and free-alternative pushback. |
| Should Farrice build a broad marketplace first? | inference no: marketplaces already exist; the faster edge is better taste, better proof, and better workflow rescue. |
| Should Farrice sell skill/plugin packages? | yes, after each package is born from a real painful workflow and carries validation receipts. |
| Best first offer | 49 to 99 USD AI Workflow Misfire Teardown, then 250 USD Guessproof Diagnostic, then 500 to 1,000 USD implementation sprint. |
| Best eventual digital product | 12 to 25 USD narrow verified skill kit, or 29 to 99 USD bundle with install guide, examples, tests, and update promise. |

## Immediate Monetization Path

1. **Use the service-first wedge.** Post or DM a simple ask: Send me one AI workflow that still needs human rescue. I will find the guessing point and give you a reusable fix map.
2. **Sell the teardown before the bundle.** Price the first public teardown at 49 to 99 USD. Deliver a one-page diagnosis, before/after prompt or skill sample, and three validation tests.
3. **Upsell implementation.** If the workflow matters to the buyer, offer the 500 to 1,000 USD implementation sprint: SKILL.md, workflow file, install instructions, test prompts, risk gates, and handoff.
4. **Turn paid rescues into products.** After three similar paid rescues, extract the common pattern into a verified skill kit and list it on Agensi, SkillHQ, PromptBase Agent Skills, or Gumroad.
5. **Avoid hype language.** The category has enough buy-my-vibe resistance. Lead with receipts: exact workflow, exact failure, exact fix, exact proof.

## What Would Change The Verdict

- Contradicted if: three direct paid teardown offers get no replies from warm AI builders, agencies, or operators.
- Contradicted if: buyers say they like the idea but refuse to share real workflows due to privacy or trust.
- Strengthened if: one buyer pays for a diagnostic within 72 hours.
- Strengthened if: two marketplace listings with before/after proof convert at 12 to 25 USD without personal selling.
- Strengthened if: one agency asks for private workflow-kit implementation instead of a public product.

## Source Appendix

- https://openai.com/index/introducing-the-gpt-store/
- https://support.claude.com/en/articles/12512176-what-are-skills
- https://code.claude.com/docs/en/skills
- https://agentskills.io/
- https://manus.im/features/agent-skills
- https://manus.im/docs/features/skills
- https://promptbase.com/
- https://promptbase.com/blog/promptbase-select-creators
- https://www.agensi.io/
- https://www.agensi.io/learn/how-to-price-skill-md-skills
- https://www.agensi.io/browse
- https://skillhq.dev/
- https://skillpacks.dev/
- https://www.producthunt.com/products/manus-skills
- https://arxiv.org/abs/2602.08004
- https://arxiv.org/abs/2605.11418
- https://www.skillsbench.ai/skillsbench.pdf
- https://www.reddit.com/r/claude/comments/1rkjqjf/i_built_a_marketplace_for_skillmd_skills_because/
- https://www.reddit.com/r/ClaudeCode/comments/1rr5pvd/i_built_a_marketplace_for_skillmd_files_heres/
- https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/
- https://www.reddit.com/r/AIAgentsInAction/comments/1tdbvrg/i_built_an_agentnative_marketplace_for_ai_skills/
- https://www.reddit.com/r/SideProject/comments/1su8v82/im_building_a_cli_marketplace_for_claude_code/
- https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/
- https://www.reddit.com/r/u_MillionaireMindset62/comments/1thwnie/nohype_technical_analysis_of_easy_prompt_creator/
- https://www.reddit.com/r/ClaudeCode/comments/1sulwsg/i_built_a_skill_marketplace_because_i_was_tired/
