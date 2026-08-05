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
#
# ANCHORING RULE (2026-08-02, Farrice-acked commit): every pattern matches the
# INVOCATION SHAPE (launcher + script + args), never a bare filename. Evidenced
# failure this fixed: a read-only `head` mentioning fal_video_seedance.py was
# denied as fal-seedance-1080p, and a `grep` on a path containing gen.sh was
# denied as fal-poster. Golden corpus below (`python3 cost_gate_hook.py --self-test`)
# pins both directions; run it after ANY pattern edit.
def _seedance_service(cmd: str) -> str:
    m = re.search(r"--resolution[= ](\d+)p", cmd)
    if m:
        return f"fal-seedance-{m.group(1)}p"
    # Unparseable resolution defaults to the hard-blocked 1080p path.
    return "fal-seedance-1080p"


def _generic_service(cmd: str) -> str:
    """generate_media.py run — compute an honest --est-cost from the recipe file
    so cost_gate's delegate check has a real number (the engine re-checks with
    exact params internally; this is the outer, deterministic layer)."""
    est = 0.25  # conservative default when the recipe can't be read (forces approval lane)
    m = re.search(r"--model[= ](\S+)", cmd)
    if m:
        try:
            recipe = json.loads(
                (REPO_ROOT / "skills" / "generate" / "models" / (m.group(1) + ".json"))
                .read_text())
            table = (recipe.get("pricing") or {}).get("table") or {}
            price = table.get("default")
            unit = (recipe.get("pricing") or {}).get("unit")
            if price is not None:
                n = 1
                nm = re.search(r"--n[= ](\d+)", cmd)
                if nm:
                    n = int(nm.group(1))
                dur = 1
                dm = re.search(r"--param[= ]duration=(\d+)", cmd)
                if dm:
                    dur = int(dm.group(1))
                est = price * (dur if unit == "per_second" else n)
        except Exception:
            pass
    return f"fal-generic --est-cost={round(est, 4)}"


PAID_PATTERNS = [
    (re.compile(r"python3?\s+\S*fal_video_seedance\.py\b"), _seedance_service),
    (re.compile(r"python3?\s+\S*fal_video_kling\.py\b"), lambda c: "fal-kling"),
    (re.compile(r"(?:\bbash|\bsh)\s+\S*gen\.sh\b|(?:^|[;&|(]\s*)(?:\./|skills/)\S*gen\.sh\b"),
     lambda c: "fal-poster"),
    (re.compile(r"\bnode\s+\S*generate\.js\b"), lambda c: "fal-poster"),
    (re.compile(r"python3?\s+\S*generate_image\.py\b"), lambda c: "fal-poster"),
    (re.compile(r"python3?\s+\S*generate_media\.py\s+run\b"), _generic_service),
    (re.compile(r"python3?\s+\S*deep_research_(?:client|engine)\.py\b"),
     lambda c: "gemini-deep-research"),
    (re.compile(r"python3?\s+\S*perplexity_client\.py\s.*--research|curl\b[^|;]*sonar-deep-research"),
     lambda c: "perplexity-research"),
    (re.compile(r"python3?\s+\S*monid_client\.py\b"), lambda c: "monid"),
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
    # Resolvers may return "service --extra=flag ..." — first token is the
    # service id, the rest are extra gate args (e.g. fal-generic's --est-cost).
    service_parts = service.split()
    service = service_parts[0]
    extra_flags = service_parts[1:]
    try:
        proc = subprocess.run(
            ["python3", str(GATE), "check", f"--service={service}",
             f"--request={cmd[:160]}"] + extra_flags + _passthrough_flags(cmd),
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


def self_test() -> int:
    """Golden corpus for the anchored patterns. The first two MUST-NOT entries
    are the two read-only commands wrongly denied on 2026-08-02 (evidence for
    the anchoring change). Run after ANY pattern edit."""
    must_not_match = [
        # the two evidenced false positives (shapes, verbatim class):
        "head -50 execution/fal_video_seedance.py",
        "grep -n 'style' skills/fantastic-posters/gen.sh",
        # more read-only shapes that historically risk tripping filename matches:
        "sed -n '1,40p' execution/fal_video_kling.py",
        "cat execution/generate_image.py | wc -l",
        "grep -rn generate.js skills/fantastic-posters/",
        "ls -la execution/ | grep generate_media.py",
        "python3 execution/generate_media.py models",
        "python3 execution/generate_media.py quote --model recraft-v3 --prompt 'x'",
        "python3 execution/generate_media.py index --file out.png --model gpt-image-2",
        "grep -r 'sonar-deep-research' directives/",
        "git diff execution/fal_video_seedance.py",
    ]
    must_match = [
        ("python3 execution/fal_video_seedance.py --image a.png --prompt 'x' "
         "--duration 5 --resolution 480p", "fal-seedance-480p"),
        ("python3 execution/fal_video_kling.py --image a.png --prompt 'x' --duration 5",
         "fal-kling"),
        ("bash skills/fantastic-posters/gen.sh \"brief\" --style=swiss --quality=medium",
         "fal-poster"),
        ("cd skills/fantastic-posters && node generate.js \"brief\" --style=swiss",
         "fal-poster"),
        ("python3 execution/generate_image.py \"prompt\" --aspect 1:1", "fal-poster"),
        ("python3 execution/generate_media.py run --model recraft-v3 --prompt 'x'",
         "fal-generic"),
        ("skills/fantastic-posters/gen.sh \"brief\" --style=swiss", "fal-poster"),
    ]

    def resolve(cmd):
        if EXCLUDE.search(cmd):
            return None
        for pattern, to_service in PAID_PATTERNS:
            if pattern.search(cmd):
                return to_service(cmd).split()[0]
        return None

    failures = []
    for cmd in must_not_match:
        got = resolve(cmd)
        if got is not None:
            failures.append(f"FALSE POSITIVE: {cmd!r} -> {got}")
    for cmd, want in must_match:
        got = resolve(cmd)
        if got != want:
            failures.append(f"MISS: {cmd!r} -> {got} (want {want})")
    if failures:
        print("SELF-TEST FAIL")
        for f in failures:
            print(" ", f)
        return 1
    print(f"self-test: OK ({len(must_not_match)} negatives, {len(must_match)} positives)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    main()
