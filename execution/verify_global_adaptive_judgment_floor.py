#!/usr/bin/env python3
"""Verify the global Codex-native adaptive judgment floor."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GLOBAL_CODEX = Path("/Users/farricecain/.codex")
GLOBAL_AGENTS = Path("/Users/farricecain/.codex/AGENTS.md")
GLOBAL_RAW_INTENT = Path("/Users/farricecain/.codex/skills/raw-intent-bridge/SKILL.md")
GLOBAL_AUTOPILOT = Path("/Users/farricecain/.codex/skills/autopilot/SKILL.md")
OPERATING_CONTRACT = ROOT / "semantic_libraries/antigravity/primitives/operating-alignment-contract.md"
MAGIC_SET = ROOT / "semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md"
HOOK = ROOT / "execution/hooks/steering_loop_hook.py"

CANONICAL_OVERLAY_POINTER = (
    "/Users/farricecain/Google Antigravity/semantic_libraries/antigravity/primitives/"
    "systems-thinking-expertise-intelligence-overlay.md"
)
SYSTEMS_OVERLAY = Path(CANONICAL_OVERLAY_POINTER)

SHADOW_BEGIN = "<!-- BEGIN:global-systems-thinking-shadow -->"
SHADOW_END = "<!-- END:global-systems-thinking-shadow -->"
OVERLAY_SLUG = "systems-thinking-expertise-intelligence-overlay"

BANNED_OVERLAY_SURFACES = (
    GLOBAL_CODEX / "skills" / OVERLAY_SLUG,
    GLOBAL_CODEX / "skills" / f"source-command-{OVERLAY_SLUG}",
    GLOBAL_CODEX / "agents" / OVERLAY_SLUG,
    ROOT / ".agent" / "workflows" / f"{OVERLAY_SLUG}.md",
    ROOT / ".agents" / "skills" / OVERLAY_SLUG,
    ROOT / ".agents" / "skills" / f"source-command-{OVERLAY_SLUG}",
)

ROUTING_SURFACES = (
    GLOBAL_CODEX / "hooks.json",
    GLOBAL_CODEX / "config.toml",
    ROOT / ".codex" / "hooks.json",
    ROOT / "SLASH_COMMANDS.md",
    ROOT / "directives" / "routing-bindings.md",
    ROOT / "execution" / "control_route_classifier.py",
    ROOT / "execution" / "workflow_router.py",
    ROOT / "execution" / "routing_governor.py",
)

ACTIVE_SURFACE_ROOTS = (
    (GLOBAL_CODEX / "skills", "SKILL.md"),
    (GLOBAL_CODEX / "agents", "AGENT.md"),
    (ROOT / "skills", "SKILL.md"),
    (ROOT / ".agents" / "skills", "SKILL.md"),
    (ROOT / ".agent" / "workflows", "*.md"),
)

ALLOWED_OVERLAY_SURFACE_REFERENCES = {
    ROOT / ".agent" / "workflows" / "operator-school.md",
}

OVERLAY_REFERENCE_TOKENS = (
    OVERLAY_SLUG,
    "systems-thinking shadow companion",
    "systems thinking and expertise intelligence overlay",
)

RAW_STRATEGIC_PROMPT = (
    "I have been thinking about a messy product idea and I want help finding the real opportunity. "
    "I do not know whether the market exists, and I also need to know how to sell it. "
    "On top of that, how would we build it, what should we avoid, and what evidence would change the decision?"
)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing required surface: {path}")
    return path.read_text(encoding="utf-8")


def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def require(label: str, path: Path, needles: list[str]) -> None:
    text = " ".join(strip_html_comments(read(path)).lower().split())
    missing = [needle for needle in needles if " ".join(needle.lower().split()) not in text]
    if missing:
        fail(f"{label} missing: {', '.join(missing)}")


def extract_single_section(text: str, begin: str, end: str) -> str:
    if text.count(begin) != 1 or text.count(end) != 1:
        fail("global Systems-Thinking SHADOW markers must appear exactly once")
    start = text.index(begin) + len(begin)
    finish = text.index(end, start)
    return text[start:finish]


def check_global_agents() -> None:
    require(
        "global AGENTS",
        GLOBAL_AGENTS,
        [
            "Global Adaptive Judgment Floor",
            "Default the reasoning principles; adapt the workflow depth",
            "without magic words",
            "senior-partner pushback",
            "Evidence must change",
            "UNTESTED",
            "LOCKED",
            "PARKED",
            "NEXT ACTION",
            "raw-intent-bridge is optional",
            "private token-by-token chain-of-thought",
        ],
    )


def check_global_shadow_overlay() -> None:
    global_text = read(GLOBAL_AGENTS)
    if global_text.count(CANONICAL_OVERLAY_POINTER) != 1:
        fail("global AGENTS must contain exactly one canonical overlay pointer")

    section = strip_html_comments(extract_single_section(global_text, SHADOW_BEGIN, SHADOW_END))
    if section.count(CANONICAL_OVERLAY_POINTER) != 1:
        fail("active global SHADOW section must contain exactly one canonical overlay pointer")
    section_text = " ".join(section.lower().split())
    required = [
        "systems-thinking shadow companion",
        "root/main codex conductor",
        "cold-load",
        "pointer-level eligibility sniff",
        "cross-system downstream impact",
        "recurring shared foundation",
        "scarce craft ownership",
        "consequential ai review or recovery",
        "pressure to add permanent process after failure",
        "both gates are required",
        "canonical activation condition establishes eligibility",
        "plausible material change",
        "plausible decision change establishes activation",
        "if either is absent, do not load it",
        "genuine material fork",
        "preserve the native function owner",
        "stay silent when no decision changes",
        "material inherited premises",
        "nearest reversible step",
        "bundle dependent actions beyond the next safe step",
        "sole full-overlay activation owner",
        "do not load the primitive or source package",
        "recursively activate the overlay",
        "widen scope",
        "add rules",
        "keep the transcript and deep extraction cold",
        "full trace only for an explicit audit",
        "extra questions",
        "safe-work blocks",
        "mandatory fields or scores",
        "commands, routers, skills, agents, hooks",
        "automatic task creation",
        "visible framework theater",
        "reuse existing orchestration and delegation receipt fields",
        "create no new runtime schema",
    ]
    missing = [needle for needle in required if needle not in section_text]
    if missing:
        fail(f"global SHADOW companion missing: {', '.join(missing)}")

    global_contradictions = (
        "may block safe work",
        "must block safe work",
        "requires extra questions",
        "must ask extra questions",
        "mandatory trace",
        "mandatory readiness score",
        "subagents may recursively activate",
        "subagents should load the primitive",
        "override the native function owner",
        "status: `enforced`",
        "hot-load the primitive",
        "preload the transcript",
    )
    contradictions = [term for term in global_contradictions if term in section_text]
    if contradictions:
        fail(f"global SHADOW companion contains contradictory policy: {', '.join(contradictions)}")

    copied_definitions = [
        heading for heading in ("### Zoom", "### Craft", "### Pave", "### Own", "### Learn")
        if heading in section
    ]
    if copied_definitions:
        fail(f"global SHADOW companion copied canonical definitions: {', '.join(copied_definitions)}")

    overlay_text = strip_html_comments(read(SYSTEMS_OVERLAY))
    status_lines = [
        line.strip() for line in overlay_text.splitlines()
        if line.strip().startswith("Status:")
    ]
    if len(status_lines) != 1 or not status_lines[0].startswith("Status: `SHADOW`."):
        fail("canonical Systems-Thinking overlay must have exactly one active SHADOW status line")

    overlay_contradictions = (
        "status: `enforced`",
        "hard block",
        "mandatory score",
        "may block safe work",
        "must block safe work",
        "mandatory questions for clear tasks",
        "may hot-promote",
        "must hot-promote",
    )
    normalized_overlay = " ".join(overlay_text.lower().split())
    contradictions = [term for term in overlay_contradictions if term in normalized_overlay]
    if contradictions:
        fail(f"canonical Systems-Thinking overlay contains contradictory policy: {', '.join(contradictions)}")

    require(
        "canonical Systems-Thinking overlay",
        SYSTEMS_OVERLAY,
        [
            "companion intelligence primitive",
            "Keep this primitive cold and load it on demand",
            "Never ask extra questions merely to prove the overlay ran",
            "No integration transfers authority away from its existing contract",
            "block safe work",
            "add mandatory questions or fields to clear tasks",
            "create a universal readiness score",
            "hot-promote itself into a command, router, skill, agent, hook, or global mirror",
            "claim deployment success from file presence or verifier output alone",
            "Promotion requires three independent production receipts",
            "explicit Farrice approval",
            "If none changes, the overlay should remain silent",
        ],
    )


def check_no_competing_overlay_surfaces() -> None:
    created = [str(path) for path in BANNED_OVERLAY_SURFACES if path.exists()]
    if created:
        fail(f"competing global overlay surfaces exist: {', '.join(created)}")

    routed: list[str] = []
    for path in ROUTING_SURFACES:
        if path.exists() and any(token in read(path).lower() for token in OVERLAY_REFERENCE_TOKENS):
            routed.append(str(path))

    for root, pattern in ACTIVE_SURFACE_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob(pattern):
            if path in ALLOWED_OVERLAY_SURFACE_REFERENCES:
                continue
            text = read(path).lower()
            if any(token in text for token in OVERLAY_REFERENCE_TOKENS):
                routed.append(str(path))

    if routed:
        fail(f"overlay was added to a named command, skill, agent, hook, or routing surface: {', '.join(sorted(set(routed)))}")


def check_global_front_doors() -> None:
    require(
        "global raw-intent bridge",
        GLOBAL_RAW_INTENT,
        [
            "Automatic Trigger",
            "without a prefix",
            "optional explicit invocation",
            "inspect the compiled packet",
        ],
    )
    require(
        "global autopilot",
        GLOBAL_AUTOPILOT,
        [
            "Adaptive Judgment Floor",
            "operating-alignment-contract.md",
            "raw-intent-bridge is optional",
            "evidence changes the recommendation",
        ],
    )


def check_canonical_contract() -> None:
    require(
        "operating-alignment contract",
        OPERATING_CONTRACT,
        [
            "Adaptive Judgment Floor",
            "Default the reasoning principles; adapt the workflow depth",
            "Research earns inclusion only when it changes a decision",
            "VERIFIED",
            "UNTESTED",
            "LOCKED",
            "PARKED",
            "NEXT ACTION",
        ],
    )
    require(
        "magic preservation set",
        MAGIC_SET,
        [
            "Casual Gacha Copilot Market Verdict",
            "decision compression",
            "category activity from exact-offer demand",
            "without requiring a magic phrase",
        ],
    )


def check_prompt_hook() -> None:
    proc = subprocess.run(
        [sys.executable, str(HOOK), "test-mirror"],
        cwd=ROOT,
        text=True,
        input=RAW_STRATEGIC_PROMPT,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        fail(f"intent-mirror hook failed: {proc.stdout or proc.stderr}")
    if "fires: YES" not in proc.stdout or "INTENT MIRROR" not in proc.stdout:
        fail(f"raw strategic prompt did not trigger the intent mirror:\n{proc.stdout}")


def main() -> int:
    checks = [
        check_global_agents,
        check_global_shadow_overlay,
        check_no_competing_overlay_surfaces,
        check_global_front_doors,
        check_canonical_contract,
        check_prompt_hook,
    ]
    failures: list[str] = []
    for check in checks:
        try:
            check()
        except Exception as exc:  # noqa: BLE001 - verifier should report every failed surface.
            failures.append(f"{check.__name__}: {exc}")
    if failures:
        print("GLOBAL ADAPTIVE JUDGMENT FLOOR VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("GLOBAL ADAPTIVE JUDGMENT FLOOR VERIFICATION PASS")
    print("- raw strategic language triggers the intent mirror without a command prefix")
    print("- global Codex instructions carry the adaptive judgment floor")
    print("- Systems-Thinking overlay is a single cold SHADOW pointer with no named competing activation surface")
    print("- Google Antigravity retains the canonical contract and preservation exemplar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
