#!/usr/bin/env python3
"""cost_gate_hook.py — PreToolUse(Bash) hook: HARD money gate for paid APIs.

WHY: cost_gate.py + fal_budget_guard.py were documented as "MANDATORY" but
invocation depended on Claude remembering — the exact AI-memory-dependent
pattern this repo bans. This hook makes the gate physical: Bash commands that
match a paid-API pattern are intercepted; the gate's verdict decides.

Verdict translation (cost_gate.py check exit codes):
    0 (approved)        -> allow the call
    1 (denied)          -> BLOCK (exit 2) — caps are caps, no override
    2 (needs approval)  -> consume an unexpired token from
                           .agent/cost-gate-approvals.jsonl if present -> allow;
                           else BLOCK (exit 2) with approve instructions.

Fail-safe is ASYMMETRIC:
    - exception BEFORE a paid pattern matched -> exit 0 (never break normal Bash)
    - exception AFTER a paid pattern matched  -> exit 2 (a broken gate must not
      approve spend)

Wired via .claude/settings.local.json -> hooks.PreToolUse (matcher: Bash).
User decision 2026-06-09: this gate HARD-BLOCKS.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GATE = REPO_ROOT / "execution" / "cost_gate.py"

# Commands that ARE the gate / read-only surfaces — never intercept.
EXCLUDE = re.compile(
    r"fal_budget_guard\.py|cost_gate\.py|forge_gate\.py|--help|\bstatus\b|reset-daily|reset-session"
)

# Paid patterns -> (service, arg-parser). Order matters: first match wins.
def _seedance_service(cmd: str) -> str:
    m = re.search(r"--resolution[= ](\d+)p", cmd)
    if m:
        return f"fal-seedance-{m.group(1)}p"
    # Unparseable resolution defaults to the hard-blocked 1080p path.
    return "fal-seedance-1080p"


PAID_PATTERNS = [
    (re.compile(r"fal_video_seedance\.py"), _seedance_service),
    (re.compile(r"fal_video_kling\.py"), lambda c: "fal-kling"),
    (re.compile(r"(?:^|[\s/])gen\.sh|generate\.js"), lambda c: "fal-poster"),
    (re.compile(r"generate_image\.py"), lambda c: "fal-poster"),
    (re.compile(r"deep_research_client\.py|deep_research_engine\.py"),
     lambda c: "gemini-deep-research"),
    (re.compile(r"perplexity_client\.py.*--research|sonar-deep-research"),
     lambda c: "perplexity-research"),
]


def _passthrough_flags(cmd: str) -> list:
    """Carry --quality/--n/--duration through to the gate for honest estimates."""
    flags = []
    for name in ("quality", "n", "duration"):
        m = re.search(rf"--{name}[= ]([\w-]+)", cmd)
        if m:
            flags.append(f"--{name}={m.group(1)}")
    return flags


def main():
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        if payload.get("tool_name") != "Bash":
            sys.exit(0)
        cmd = (payload.get("tool_input") or {}).get("command", "") or ""
        if not cmd or EXCLUDE.search(cmd):
            sys.exit(0)
        service = None
        for pattern, to_service in PAID_PATTERNS:
            if pattern.search(cmd):
                service = to_service(cmd)
                break
        if service is None:
            sys.exit(0)
    except Exception:
        sys.exit(0)  # fail-open before a paid match

    # A paid pattern matched — from here on, failures fail CLOSED.
    try:
        proc = subprocess.run(
            ["python3", str(GATE), "check", f"--service={service}",
             f"--request={cmd[:160]}"] + _passthrough_flags(cmd),
            capture_output=True, text=True, timeout=30, cwd=str(REPO_ROOT),
        )
        out = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")

        if proc.returncode == 0:
            sys.exit(0)

        if proc.returncode == 2:
            # Above auto-approve threshold: honor a fresh user-approval token.
            sys.path.insert(0, str(REPO_ROOT / "execution"))
            from cost_gate import consume_approval
            if consume_approval(service):
                sys.exit(0)
            print(
                f"COST GATE — USER APPROVAL REQUIRED for '{service}'.\n{out.strip()}\n\n"
                f"Ask Farrice to approve the spend. ONLY after an explicit yes, run:\n"
                f"  python3 execution/cost_gate.py approve --service={service} "
                f"--request \"<what's being made>\"\nthen retry the original command "
                f"(token valid 15 min).",
                file=sys.stderr,
            )
            sys.exit(2)

        # returncode 1 (or anything else): hard denial, no override.
        print(
            f"COST GATE — DENIED for '{service}' (budget cap / blocked mode).\n"
            f"{out.strip()}\n\nThis is a hard cap. Do not retry or work around it; "
            f"surface the denial to Farrice.",
            file=sys.stderr,
        )
        sys.exit(2)
    except SystemExit:
        raise
    except Exception as e:
        print(
            f"COST GATE — gate errored after matching paid service '{service}' ({e}). "
            f"Failing CLOSED: a broken gate must not approve spend. "
            f"Run `python3 execution/cost_gate.py status` to diagnose.",
            file=sys.stderr,
        )
        sys.exit(2)


if __name__ == "__main__":
    main()
