#!/usr/bin/env python3
"""Deterministic contract verifier for the Kieran Content Signal Loop."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]


PATHS = {
    "profile_workflow": ROOT / "skills/kieran-flanagan-audience-intelligence/workflows/05-winning-content-profile.md",
    "profile_prompt": ROOT / "skills/kieran-flanagan-audience-intelligence/references/prompts-v2/winning-content-profile.md",
    "ideas_workflow": ROOT / "skills/kieran-flanagan-content-engine/workflows/09-content-signal-ideation.md",
    "ideas_prompt": ROOT / "skills/kieran-flanagan-content-engine/references/prompts-v2/content-signal-ideation.md",
    "queue_workflow": ROOT / "skills/kieran-flanagan-content-ops/workflows/04-content-queue.md",
    "queue_prompt": ROOT / "skills/kieran-flanagan-content-ops/references/prompts-v2/content-queue-session.md",
    "orchestrate": ROOT / "skills/kieran-flanagan-content-ops/workflows/01-content-orchestrate.md",
    "feedback": ROOT / "skills/kieran-flanagan-content-ops/workflows/02-content-feedback.md",
    "review": ROOT / "skills/kieran-flanagan-content-ops/workflows/03-content-review-cycle.md",
    "profile_wrapper": ROOT / ".agent/workflows/content-winning-profile.md",
    "ideas_wrapper": ROOT / ".agent/workflows/content-ideas.md",
    "queue_wrapper": ROOT / ".agent/workflows/content-queue.md",
    "slash_index": ROOT / "SLASH_COMMANDS.md",
}


def load_files():
    missing = [str(path.relative_to(ROOT)) for path in PATHS.values() if not path.exists()]
    if missing:
        for item in missing:
            print(f"[FAIL] missing production file: {item}")
        raise SystemExit(1)
    return {name: path.read_text(encoding="utf-8") for name, path in PATHS.items()}


def contains_all(text, required):
    haystack = text.casefold()
    return all(fragment.casefold() in haystack for fragment in required)


def main():
    files = load_files()
    fixtures = [
        (
            "platform_omission",
            contains_all(
                files["ideas_workflow"] + files["ideas_prompt"],
                ["recommended platform", "every idea card", "platform test"],
            ),
        ),
        (
            "no_metrics_provisional",
            contains_all(
                files["profile_workflow"] + files["profile_prompt"],
                ["provisional", "performance data is absent", "no invented performance"],
            ),
        ),
        (
            "stale_profile_confidence",
            contains_all(
                files["ideas_workflow"] + files["ideas_prompt"],
                ["stale", "lower confidence", "freshness"],
            ),
        ),
        (
            "pattern_not_topic",
            contains_all(
                files["profile_workflow"] + files["ideas_workflow"],
                ["repeated topic", "patterns, not topics", "semantically duplicating"],
            ),
        ),
        (
            "human_selection_gate",
            contains_all(
                files["ideas_workflow"] + files["queue_workflow"] + files["orchestrate"],
                ["do not mutate the content queue", "explicit human selection", "add-selected"],
            ),
        ),
        (
            "tombstone_continuity",
            contains_all(
                files["queue_workflow"] + files["queue_prompt"],
                ["tombstone", "fingerprint", "does not return unchanged"],
            ),
        ),
        (
            "trend_window",
            contains_all(
                files["ideas_workflow"] + files["ideas_prompt"],
                ["requested window", "out-of-window", "historical context"],
            ),
        ),
        (
            "finished_content_veto",
            contains_all(
                files["ideas_workflow"] + files["ideas_prompt"] + files["queue_workflow"],
                ["finished-content veto", "no completed", "never generate finished content"],
            ),
        ),
        (
            "cross_session_state",
            all(
                "[STATE_ROOT]" in files[name]
                for name in (
                    "profile_workflow",
                    "ideas_workflow",
                    "queue_workflow",
                    "profile_wrapper",
                    "ideas_wrapper",
                    "queue_wrapper",
                )
            ),
        ),
        (
            "monthly_delta_approval",
            contains_all(
                files["feedback"] + files["review"],
                ["do not write the profile directly", "monthly review", "increment profile version"],
            ),
        ),
    ]

    failed = []
    for name, passed in fixtures:
        label = "PASS" if passed else "FAIL"
        print(f"[{label}] {name}")
        if not passed:
            failed.append(name)

    command_wiring = contains_all(
        files["slash_index"],
        ["/content-winning-profile", "/content-ideas", "/content-queue"],
    )
    print(f"[{'PASS' if command_wiring else 'FAIL'}] command_wiring")
    if not command_wiring:
        failed.append("command_wiring")

    if failed:
        print(f"\nContent Signal Loop verification: FAIL ({len(failed)} failure(s))")
        return 1

    print(f"\nContent Signal Loop verification: PASS ({len(fixtures)} fixtures + command wiring)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
