#!/usr/bin/env python3
"""Check or align global Operator Core wrappers with Antigravity source truth."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "autopilot.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-autopilot" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_AUTOPILOT = Path.home() / ".codex" / "skills" / "autopilot" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-autopilot" / "SKILL.md"
ANTIGRAVITY_WORKFLOW = "/Users/farricecain/Google Antigravity/.agent/workflows/autopilot.md"


COMMON_REQUIREMENTS = (
    "3 Next Prompts",
    "Operator Lesson",
    "Next-time prompt",
    "Subagent worth it?",
    "Reuse hook",
    "real Codex subagents require explicit authorization",
)

PATH_REQUIREMENTS = {
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        ANTIGRAVITY_WORKFLOW,
        "compatibility/front-door wrapper",
        "Recommended task title",
        "Expected outcome",
        "Quality bar",
        "materially different",
    ),
    GLOBAL_AUTOPILOT: COMMON_REQUIREMENTS
    + (
        ANTIGRAVITY_WORKFLOW,
        "compatibility/front-door wrapper",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ANTIGRAVITY_WORKFLOW,
        "compatibility alias",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/autopilot.md",
        "canonical behavior source",
    ),
}


GLOBAL_AUTOPILOT_BLOCK = f"""## Operator Core Alignment

This global skill is intentionally thin. The behavior source of truth for
Antigravity work remains:

`{ANTIGRAVITY_WORKFLOW}`

For meaningful Autopilot work, preserve the current Operator Core standard from
that workflow:

- include `3 Next Prompts` for substantial closeouts: Use Now, Harden, Expand
- include the full `Operator Lesson`
- include `Next-time prompt`
- include `Subagent worth it?`
- include `Reuse hook`
- real Codex subagents require explicit authorization
- keep this global skill as a compatibility/front-door wrapper, not a competing behavior contract
"""


GLOBAL_WRAPPER_BLOCK = f"""## Operator Core Alignment

This wrapper is intentionally thin. It delegates behavior to the global
Autopilot front door and, for Antigravity work, to the canonical project
workflow:

`{ANTIGRAVITY_WORKFLOW}`

It must preserve the current Operator Core standard: `3 Next Prompts`,
`Operator Lesson`, `Next-time prompt`, `Subagent worth it?`, `Reuse hook`, and
the rule that real Codex subagents require explicit authorization.
"""


LOCAL_WRAPPER_BLOCK = """## Operator Core Alignment

This project wrapper follows `.agent/workflows/autopilot.md` as the canonical
behavior source. It must preserve `3 Next Prompts`, `Operator Lesson`,
`Next-time prompt`, `Subagent worth it?`, `Reuse hook`, and the rule that real
Codex subagents require explicit authorization.
"""


GLOBAL_NEXT_PROMPTS_BLOCK = """## Three Contextual Next Prompts

After a meaningful response with a real next decision, give exactly three
ranked, session-specific recommendations. Keep them compact. Tiny answers and
turns with no useful continuation may omit them.

The recommendations must help finish the current job, close a consequential
gap, or elevate the result toward a more remarkable outcome. They are not
engagement bait and must be materially different leverage moves, never three
paraphrases of "continue."

Quality contract:

- Preserve the session's actual intent, evidence, constraints, and unfinished
  work. Generic advice that could follow any chat fails.
- Rank the best next move first. The other two should offer materially
  different leverage, such as stronger proof, a better artifact, creative
  elevation, productization, automation, or a wider opportunity.
- Surface a visible `Recommended task title` using
  `[Domain]: [Specific Object] - [Outcome]`; setting the native title alone is
  not a substitute for showing the retrieval label to Farrice.
- Every move names a concrete outcome, explains why it is recommended, includes
  a copy-ready prompt, states an explicit `Expected outcome`, and gives one
  inspectable `Quality bar`.
- An expected outcome must name the artifact, decision, proof event, or changed
  state that will exist. "More clarity" or "improved output" alone fails.
- Reveal useful capabilities naturally, but do not dump tools, agents, skills,
  or workflows unless they change the decision.
- If the best next action is safe, local, and already authorized, execute it
  instead of using a recommendation to hand the work back.
- State an approval boundary only when one genuinely exists.
- `Use Now`, `Harden`, and `Expand` may guide coverage internally, but visible
  titles must name the actual outcomes rather than repeat canned labels.

Preferred visible shape:

```markdown
**Recommended task title:** [Domain]: [Specific Object] - [Outcome]

## 3 Next Prompts
1. **[Specific outcome]** — [why this is the best next move now]
   **Prompt:** "[copy-ready continuation]"
   **Expected outcome:** [artifact, decision, proof event, or changed state]
   **Quality bar:** [one inspectable acceptance criterion]
2. **[Different leverage move]** — [gap closed or capability gained]
   **Prompt:** "[copy-ready continuation]"
   **Expected outcome:** [artifact, decision, proof event, or changed state]
   **Quality bar:** [one inspectable acceptance criterion]
3. **[Creative or strategic elevation]** — [larger outcome made possible]
   **Prompt:** "[copy-ready continuation]"
   **Expected outcome:** [artifact, decision, proof event, or changed state]
   **Quality bar:** [one inspectable acceptance criterion]
```
"""


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def ensure_block(text: str, block: str, anchor: str) -> str:
    heading = block.splitlines()[0]
    if heading in text:
        return text
    if anchor not in text:
        return text.rstrip() + "\n\n" + block.rstrip() + "\n"
    return text.replace(anchor, anchor.rstrip() + "\n\n" + block.rstrip() + "\n", 1)


def align_global_agents(text: str) -> str:
    section_pattern = re.compile(
        r"## Three Contextual Next Prompts\n.*?(?=\n## Compact Operator Lesson)",
        flags=re.DOTALL,
    )
    text, replacements = section_pattern.subn(GLOBAL_NEXT_PROMPTS_BLOCK.rstrip() + "\n", text, count=1)
    if replacements != 1:
        raise AssertionError("global AGENTS alignment could not replace Three Contextual Next Prompts")
    canonical_line = f"The canonical Antigravity Autopilot workflow is `{ANTIGRAVITY_WORKFLOW}`."
    if canonical_line not in text:
        text = text.replace(
            "## Global Autopilot Front Door\n",
            "## Global Autopilot Front Door\n\n"
            f"{canonical_line} "
            "The global Autopilot skill is a compatibility/front-door wrapper, not a competing behavior contract.\n",
            1,
        )
    text = text.replace(
        "Close with steering by default: Use Now, Harden, Expand.",
        "Close with steering by default: 3 Next Prompts using Use Now, Harden, and Expand.",
    )
    text = text.replace(
        "Preferred full closeout shape:",
        "Preferred full closeout shape:",
    )
    text = text.replace("## Steering\n", "## 3 Next Prompts\n", 1)
    text = text.replace("   - **Move:** [concrete next action]", "   - **When to use:** [condition that makes this the right next move]", 1)
    text = text.replace("   - **Why it matters:** [why this moves the work forward]", "   - **Why this is recommended:** [why this moves the work forward]", 1)
    text = text.replace("   - **First artifact:** [what gets produced]", "   - **Prompt:** [copy-paste continuation prompt]\n   - **Expected output:** [what gets produced]", 1)
    text = text.replace("   - **Move:** [validation, proof, cleanup, or risk-reduction step]", "   - **When to use:** [condition that makes hardening the right next move]", 1)
    text = text.replace("   - **Why it matters:** [risk reduced or reliability gained]", "   - **Why this is recommended:** [risk reduced or reliability gained]", 1)
    text = text.replace("   - **First artifact:** [what gets produced]", "   - **Prompt:** [copy-paste continuation prompt]\n   - **Expected output:** [what gets produced]", 1)
    text = text.replace("   - **Move:** [next capability, asset, offer, workflow, or system step]", "   - **When to use:** [condition that makes expansion the right next move]", 1)
    text = text.replace("   - **Why it matters:** [upside or compounding value]", "   - **Why this is recommended:** [upside or compounding value]", 1)
    text = text.replace("   - **First artifact:** [what gets produced]", "   - **Prompt:** [copy-paste continuation prompt]\n   - **Expected output:** [what gets produced]", 1)
    if "real Codex subagents require explicit authorization" not in text:
        text = text.replace(
            "- Do not spawn real Codex subagents unless the user explicitly authorizes delegation, parallel agents, or subagents.",
            "- Do not spawn real Codex subagents unless the user explicitly authorizes delegation, parallel agents, or subagents; real Codex subagents require explicit authorization.",
        )
    if "compatibility/front-door wrapper" not in text:
        text = text.replace(
            "The global compatibility wrapper lives at `/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md` for existing command-style invocations.",
            "The global compatibility/front-door wrapper lives at `/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md` for existing command-style invocations.",
        )
    if "3 Next Prompts" not in text:
        raise AssertionError("global AGENTS alignment failed to add 3 Next Prompts")
    return text


def align_global_autopilot(text: str) -> str:
    if "\n## Quality Gate\n\n## Operator Core Alignment" in text:
        text = text.replace("\n## Quality Gate\n\n## Operator Core Alignment", "\n## Operator Core Alignment", 1)
        text = text.replace("\n\nBefore final delivery", "\n\n## Quality Gate\n\nBefore final delivery", 1)
    return text


def align_global_wrapper(text: str) -> str:
    text = text.replace("\n Plugin packaging requests must go\n", "\n\nPlugin packaging requests must go\n")
    return text


def align_local_wrapper(text: str) -> str:
    misplaced = f"\n## Command Template\n\n{LOCAL_WRAPPER_BLOCK.rstrip()}\n\n"
    if misplaced in text:
        text = text.replace(misplaced, f"\n{LOCAL_WRAPPER_BLOCK.rstrip()}\n\n## Command Template\n\n", 1)
    return text


def align_file(path: Path, block: str, anchor: str) -> bool:
    original = read(path)
    if path == GLOBAL_AGENTS:
        updated = align_global_agents(original)
    else:
        updated = ensure_block(original, block, anchor)
    if path == GLOBAL_AUTOPILOT:
        updated = align_global_autopilot(updated)
    if path == GLOBAL_WRAPPER:
        updated = align_global_wrapper(updated)
    if path == LOCAL_WRAPPER:
        updated = align_local_wrapper(updated)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def apply_alignment() -> list[str]:
    changed = []
    if align_file(GLOBAL_AGENTS, "", "Preferred full closeout shape:"):
        changed.append(str(GLOBAL_AGENTS))
    if align_file(GLOBAL_AUTOPILOT, GLOBAL_AUTOPILOT_BLOCK, "## Quality Gate"):
        changed.append(str(GLOBAL_AUTOPILOT))
    if align_file(GLOBAL_WRAPPER, GLOBAL_WRAPPER_BLOCK, "When blocked, include a copy-paste Run Prompt."):
        changed.append(str(GLOBAL_WRAPPER))
    if align_file(LOCAL_WRAPPER, LOCAL_WRAPPER_BLOCK, "## Command Template"):
        changed.append(str(LOCAL_WRAPPER.relative_to(ROOT)))
    return changed


def check_alignment() -> list[str]:
    failures = []
    for label, path in (
        ("global AGENTS", GLOBAL_AGENTS),
        ("global autopilot", GLOBAL_AUTOPILOT),
        ("global source-command-autopilot", GLOBAL_WRAPPER),
        ("local source-command-autopilot", LOCAL_WRAPPER),
    ):
        text = read(path)
        normalized = re.sub(r"\s+", " ", text)
        for snippet in PATH_REQUIREMENTS[path]:
            if re.sub(r"\s+", " ", snippet) not in normalized:
                failures.append(f"{label} missing: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align global Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global/local Operator Core surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("GLOBAL OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("GLOBAL OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("GLOBAL OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
