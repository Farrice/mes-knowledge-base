# Walkthrough: Tim Runia — Story Compass Forge

## What Was Built

Operationalized Tim Runia's "Idea-to-Story Transformation" methodology into the `story-compass` skill domain — **Position 0** in the content pipeline. Every piece of content now has structural narrative GPS before it touches any depth, viral, or persuasion expert.

## Architecture Deployed

### Agent
| Component | Path |
|---|---|
| Agent Config | [AGENT.md](file:///Users/farricecain/Google%20Antigravity/agents/tim-runia/AGENT.md) |

### Skill Files
| Component | Path |
|---|---|
| Master Manifest | [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/SKILL.md) |
| Genius Context | [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/genius.md) |

### 13 Workflows (3 Tiers)

#### Tier 1 — Foundation (Diagnostic & Assembly)
| Slash Command | Workflow | Purpose |
|---|---|---|
| `/runia-compass` | [runia-compass.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-compass.md) | Master compass sentence generator |
| `/runia-story-test` | [runia-story-test.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-story-test.md) | Story vs. topic binary diagnostic |
| `/runia-tension-dig` | [runia-tension-dig.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-tension-dig.md) | Tension excavation for flat ideas |
| `/runia-change-engineer` | [runia-change-engineer.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-change-engineer.md) | Change mechanism builder for weak endings |

#### Tier 2 — Practitioner (Format-Specific Deployment)
| Slash Command | Workflow | Purpose |
|---|---|---|
| `/runia-video-script` | [runia-video-script.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-video-script.md) | Video script structure |
| `/runia-content-story` | [runia-content-story.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-content-story.md) | Written content story engine |
| `/runia-copy-narrative` | [runia-copy-narrative.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-copy-narrative.md) | Sales narrative backbone |
| `/runia-batch-compass` | [runia-batch-compass.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-batch-compass.md) | Batch process 5-20 ideas |
| `/runia-anticipation` | [runia-anticipation.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-anticipation.md) | Anticipation tension (not just conflict) |

#### Tier 3 — Stacking & Advanced
| Slash Command | Workflow | Purpose |
|---|---|---|
| `/runia-to-depth` | [runia-to-depth.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-to-depth.md) | Escalate to Connelly/Wright/Roth |
| `/runia-to-viral` | [runia-to-viral.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-to-viral.md) | Escalate to Puri/Kallaway |
| `/runia-rescue` | [runia-rescue.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-rescue.md) | Mid-creation rescue protocol |
| `/runia-series-compass` | [runia-series-compass.md](file:///Users/farricecain/Google%20Antigravity/skills/story-compass/workflows/runia-series-compass.md) | Multi-episode series arc architect |

## Core Methodology

**Story = Want + Tension + Change.** Missing any element = still a topic.

The **Compass Sentence** collapses a full story into one GPS sentence:
> *"[Character] wants [specific goal], but [specific tension], until [specific change with mechanism]."*

## Key Design Decisions

1. **Position 0**: Runia runs *before* all other content/storytelling experts. If raw material fails `/runia-story-test`, it's blocked from downstream processing until story-ready.
2. **Anticipation as tension**: Positive tension (reveals, launches, curiosity) is explicitly valid — not just conflict/struggle.
3. **Non-circular change enforcement**: Every compass sentence is checked for mechanism. "I wanted to start → I started" is rejected.
4. **Cross-expert stacking**: Two explicit pipelines route compass outputs into depth (Connelly/Wright/Roth) and virality (Puri/Kallaway).

## Verification

| Check | Result |
|---|---|
| Agent file exists | ✅ `agents/tim-runia/AGENT.md` |
| SKILL.md exists | ✅ `skills/story-compass/SKILL.md` |
| genius.md exists | ✅ `skills/story-compass/genius.md` |
| 13 workflow files | ✅ All present in `skills/story-compass/workflows/` |
| 13 slash commands | ✅ All present in `.agent/workflows/runia-*.md` |

## Remaining Registration

> [!NOTE]
> The `tim-runia` agent and `story-compass` skill are ready for registration in `AGENT_INDEX.md` and `SKILL_INDEX.md` during the next git sync session.
