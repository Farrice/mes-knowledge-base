# Guessproof Buyer Objection Source Ledger

Retrieval date: 2026-05-27

This ledger supports the buyer-objection pass for the Guessproof Skill/Workflow Rescue offer.

## Execution Receipt

| Tool | Status | Evidence Produced | Notes |
|---|---|---|---|
| Virtuoso Orchestration | Executed | Routed objective to `/deep-research-os`. | Real subagents spawned: false. |
| Prior verified market verdict | Loaded | Used as baseline wedge and price-ladder context. | Local file: `_active/deep-research-os/04-deliverables/ai-skill-plugin-market-verdict-2026-05-27.md`. |
| Apify Reddit | Executed | Three targeted Reddit pulls for paid skills, free alternatives, prompt-pack/slop objections, and Claude skill bloat. | Some results were noisy; only relevant threads are included below. |
| Live web | Executed | Opened Agensi, SkillHQ, PromptBase, Claude docs, and relevant Reddit threads. | Direct URLs used in final synthesis. |
| Perplexity | Not executed | Not used. | Previous run showed API `insufficient_quota`; not retried for this focused pass. |

## Sources

| ID | Status | Source | URL | Evidence Use |
|---|---|---|---|---|
| S01 | verified | Prior market verdict | _active/deep-research-os/04-deliverables/ai-skill-plugin-market-verdict-2026-05-27.md | Baseline wedge, prior source map, and offer-market fit verdict. |
| S02 | verified | Agensi pricing guide | https://www.agensi.io/learn/how-to-price-skill-md-skills | Pricing bands, free-skill trust path, higher value of scripts/examples/README. |
| S03 | verified | Agensi homepage | https://www.agensi.io/ | Cross-agent marketplace promise and one-time purchase positioning. |
| S04 | verified | SkillHQ homepage | https://skillhq.dev/ | Paid marketplace, one-command install, validation, anti-piracy, seller economics. |
| S05 | verified | PromptBase homepage | https://promptbase.com/ | Prompt marketplace scale, prompt price ranges, and new agent-skills category. |
| S06 | verified | Claude Code skills docs | https://code.claude.com/docs/en/skills | Skill mechanics, direct invocation, dynamic context, progressive loading, and test flow. |
| S07 | directional | Reddit: Claude security audit question | https://www.reddit.com/r/ClaudeCode/comments/1sfxq2p/claude_security_how_to_audit_plugins_and_skills/ | Security, quality, bloat, testing, and vague-prompt objections. |
| S08 | directional | Reddit: paid prompt skepticism | https://www.reddit.com/r/PromptEngineering/comments/1li9p1s/what_are_your_thoughts_on_buying_prompt_from/ | Money-grab objection against PromptBase-style products. |
| S09 | directional | Reddit: prompt packs good? | https://www.reddit.com/r/AIPrompt_Exchange/comments/1sacezo/are_prompt_packs_good/ | Prompt-pack format skepticism. |
| S10 | directional | Reddit: SkillHQ marketplace learnings | https://www.reddit.com/r/SideProject/comments/1su8v82/im_building_a_cli_marketplace_for_claude_code/ | One-time purchase preference, narrow skill naming, ROI clarity. |
| S11 | directional | Reddit: Claude skill cleanup | https://www.reddit.com/r/ClaudeAI/comments/1snreri/top_claude_skills_for_opus_47_after_cleaning_up/ | Context bloat, trigger usefulness, explicit invocation, and keep/delete criteria. |
| S12 | directional | Reddit: Claude skills worth installing | https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/ | Trigger reliability and quality-selectivity objection. |
| S13 | directional | Reddit: Agensi update | https://www.reddit.com/r/claude/comments/1sclm8h/update_on_the_skillmd_marketplace_i_built_what/ | Discovery, security, clearer skill info, and proof-performance gap. |
| S14 | directional | Reddit: Agensi paid/free alternative skepticism | https://www.reddit.com/r/ClaudeCode/comments/1sulwsg/i_built_a_skill_marketplace_because_i_was_tired/ | Free-alternative objection and self-promotion resistance. |
| S15 | directional | Reddit: skill-audit/security auditor | https://www.reddit.com/r/ClaudeCode/comments/1qr3zc7/nobody_checks_whats_inside_claude_code_skills/ | Security fear: skills can expose shell, files, env vars, credentials. |
| S16 | directional | Reddit: prompt-pack/slop critique | https://www.reddit.com/r/aiwars/comments/1l6spyk/who_is_ai_a_tool_for/ | Ethical/craft objection and low-trust AI slop framing. |
| S17 | directional | Reddit: SEO skills anti-slop pack | https://www.reddit.com/r/ClaudeAI/comments/1skc1h5/opensourced_11_claude_skills_for_seo_page_audits/ | Shows anti-slop rulesets are already a selling/feedback point. |
| S18 | directional | Reddit: Agent-native marketplace metrics | https://www.reddit.com/r/AIAgentsInAction/comments/1tdbvrg/i_built_an_agentnative_marketplace_for_ai_skills/ | Usage versus paid-conversion tension; marketplace asks what would make people pay. |

## Evidence Handling

- verified: directly source-backed from official docs, marketplace pages, or local verified artifacts.
- directional: real community/market signal, but not statistically representative.
- inference: strategy conclusion from multiple verified/directional signals.
- unverified: not proven in this pass.
