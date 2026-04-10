# Antigravity AI System - Proprietary License

**Copyright © 2025-2026 Farrice Cain. All Rights Reserved.**

This repository contains the Antigravity AI orchestration system, a proprietary framework for multi-agent AI coordination, expert skill extraction, and intelligent workflow routing.

---

## 1. Core System Components (Proprietary & Confidential)

The following components are **proprietary intellectual property** and may not be copied, modified, distributed, or used without explicit written permission from Farrice Cain:

### System Architecture & Protocols
- **`CLAUDE.md`** - System instructions and orchestration protocols
- **`GEMINI.md`** - Gemini-native system architecture
- **`JARVIS.md`** - Expert invocation and coordination protocols
- **`COUNCIL.md`** - Council configurations and expert registry (24 experts)
- **`DOMAIN_REGISTRY.md`** - Expert domain mapping and routing logic
- **`FARRICE.md`** - Personal context and brand architecture
- **`directives/`** directory - All system protocols including:
  - The Chain (intent-pipeline.md)
  - Context Engine (agent-loading-protocol.md)
  - Expert routing (expert_auto_routing.md)
  - Quality gates and feedback systems
  - Session state management
  - Sub-agent orchestration

### Proprietary Code & Integrations
- **`execution/notion_api.py`** - Notion API integration with version-pinning workaround
- **`execution/parallel_swarm.py`** - Multi-agent orchestration engine
- **`execution/chain_runner.py`** - Chain finalization and quality gate implementation
- **`.agent/`** directory - Session state, workflows, usage tracking
- **`councils/`** directory - Council configurations and coordination protocols

### Databases & Knowledge Architecture
- All Notion database schemas and integration patterns
- Knowledge organization methodology
- Expert extraction and skill synthesis processes

**Unauthorized copying, modification, distribution, reverse engineering, or commercial use of these components is strictly prohibited.**

---

## 2. Skills & Agents (Creative Commons BY-NC-SA 4.0)

Individual **skills** (in `skills/*/`) and **agents** (in `agents/*/`) are licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### You are free to:
- **Share** - Copy and redistribute the material in any medium or format
- **Adapt** - Remix, transform, and build upon the material

### Under the following terms:
- **Attribution** - You must give appropriate credit to Farrice Cain / Antigravity AI, provide a link to the license, and indicate if changes were made
- **NonCommercial** - You may not use the material for commercial purposes without written permission
- **ShareAlike** - If you remix, transform, or build upon the material, you must distribute your contributions under the same license

**Commercial licensing available** - Contact Farrice Cain for commercial use inquiries.

---

## 3. Execution Utilities (MIT License)

The following Python utilities in the `execution/` directory are licensed under the **MIT License** (see `execution/LICENSE-MIT`):

- `sync_registries.py`
- `skill_converter.py`
- `generate_image.py`
- General-purpose utility scripts (excludes notion_api.py, parallel_swarm.py, chain_runner.py)

**MIT License Summary**: Free to use, copy, modify, merge, publish, distribute, sublicense with attribution.

---

## 4. Third-Party Components

Some skills and resources in this repository are derived from published works, books, courses, and frameworks by experts in various fields. These extractions are:

1. **Transformative works** - Original analysis, synthesis, and workflow creation
2. **Educational use** - For personal AI system development and learning
3. **Attributed** - Source materials credited in skill documentation
4. **Not redistributing source content** - Only derived frameworks and methodologies

If you are a creator whose work has been analyzed in this system and have concerns, please contact Farrice Cain directly.

---

## 5. No Warranty

THE SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NONINFRINGEMENT.

---

## 6. Contact & Licensing Inquiries

**For commercial licensing, permissions, or inquiries:**
- Email: [Your contact email]
- GitHub: @Farrice
- Repository: github.com/Farrice/mes-knowledge-base (private)

---

## Summary Table

| Component | License Type | Commercial Use |
|-----------|-------------|----------------|
| Core System (directives/, CLAUDE.md, etc.) | Proprietary | Prohibited without permission |
| Skills & Agents (skills/, agents/) | CC BY-NC-SA 4.0 | Prohibited without permission |
| Select Utilities (execution/) | MIT | Permitted with attribution |
| Documentation & Research | Proprietary | Prohibited without permission |

**Last Updated:** April 2, 2026
**Version:** 1.0
