import os
import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

CHECKPOINT_DIR = ".agent/checkpoints"
SESSION_STATE_PATH = ".agent/session-state.md"

def _get_checkpoint_path(workflow_name: str) -> str:
    """Returns the absolute path to the checkpoint file for a given workflow."""
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in workflow_name)
    return os.path.join(CHECKPOINT_DIR, f"{safe_name}.json")

def save_checkpoint(workflow_name: str, step: str, data: Any) -> None:
    """
    Persist state after each successful step in a workflow.
    
    Args:
        workflow_name: A unique identifier for the workflow execution.
        step: The name or identifier of the completed step.
        data: JSON-serializable context or data to save.
    """
    checkpoint_path = _get_checkpoint_path(workflow_name)
    
    checkpoint_data: Dict[str, Any] = {"step": step, "data": data}
    
    with open(checkpoint_path, 'w', encoding='utf-8') as f:
        json.dump(checkpoint_data, f, indent=2)

def load_checkpoint(workflow_name: str) -> Optional[Dict[str, Any]]:
    """
    Resume from the last successful step.
    
    Args:
        workflow_name: A unique identifier for the workflow execution.
        
    Returns:
        A dictionary containing the last completed 'step' and its 'data',
        or None if no checkpoint exists.
    """
    checkpoint_path = _get_checkpoint_path(workflow_name)
    
    if not os.path.exists(checkpoint_path):
        return None
        
    try:
        with open(checkpoint_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Corrupt or unreadable checkpoint
        return None

def clear_checkpoint(workflow_name: str) -> bool:
    """
    Clean up after successful completion of a workflow.
    
    Args:
        workflow_name: A unique identifier for the workflow execution.
        
    Returns:
        True if the checkpoint was found and deleted, False otherwise.
    """
    checkpoint_path = _get_checkpoint_path(workflow_name)
    
    if os.path.exists(checkpoint_path):
        try:
            os.remove(checkpoint_path)
            return True
        except OSError:
            pass
    return False


# --- Session State Anchors (Anti-Drift) ---
# Protocol: directives/session-state-protocol.md

def save_session_state(
    active_task: str,
    decisions: Optional[List[Dict[str, str]]] = None,
    experts_deployed: Optional[List[Dict[str, str]]] = None,
    key_findings: Optional[List[str]] = None,
    files_modified: Optional[List[Dict[str, str]]] = None,
    current_phase: str = "",
    next_steps: Optional[List[str]] = None,
    intent: Optional[Dict[str, str]] = None,
) -> str:
    """
    Write a session state anchor to survive context compaction.

    Args:
        active_task: 1-2 sentence description of current work.
        decisions: List of {"decision": ..., "choice": ..., "rationale": ...}.
        experts_deployed: List of {"name": ..., "contribution": ...}.
        key_findings: List of 1-line finding strings.
        files_modified: List of {"path": ..., "description": ...}.
        current_phase: Where we are in the workflow.
        next_steps: List of next action strings.
        intent: Optional {"deliverable": ..., "audience": ..., "success_criteria": ...}.

    Returns:
        The path to the written state file.
    """
    os.makedirs(os.path.dirname(SESSION_STATE_PATH), exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# Session State Anchor",
        f"> Last updated: {timestamp}",
        "",
        "## Active Task",
        active_task,
        "",
    ]

    if intent:
        lines.extend([
            "## Intent (Validated)",
            f"- **Deliverable**: {intent.get('deliverable', 'TBD')}",
            f"- **Audience**: {intent.get('audience', 'TBD')}",
            f"- **Success criteria**: {intent.get('success_criteria', 'TBD')}",
            "",
        ])

    if decisions:
        lines.append("## Decisions Made")
        for d in decisions:
            lines.append(f"- **{d['decision']}**: {d['choice']} — {d.get('rationale', '')}")
        lines.append("")

    if experts_deployed:
        lines.append("## Experts Deployed")
        for e in experts_deployed:
            lines.append(f"- **{e['name']}**: {e['contribution']}")
        lines.append("")

    if key_findings:
        lines.append("## Key Findings (Compressed)")
        for f in key_findings:
            lines.append(f"- {f}")
        lines.append("")

    if files_modified:
        lines.append("## Files Created/Modified This Session")
        for fm in files_modified:
            lines.append(f"- `{fm['path']}`: {fm['description']}")
        lines.append("")

    if current_phase:
        lines.extend(["## Current Phase", current_phase, ""])

    if next_steps:
        lines.append("## Next Steps")
        for i, step in enumerate(next_steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    content = "\n".join(lines)
    with open(SESSION_STATE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return SESSION_STATE_PATH


def load_session_state() -> Optional[str]:
    """
    Read the session state anchor file.

    Returns:
        The contents of the state file as a string, or None if it doesn't exist.
    """
    if not os.path.exists(SESSION_STATE_PATH):
        return None

    try:
        with open(SESSION_STATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except IOError:
        return None


def clear_session_state() -> bool:
    """
    Remove the session state file (e.g., when a session completes cleanly).

    Returns:
        True if removed, False if it didn't exist or couldn't be removed.
    """
    if os.path.exists(SESSION_STATE_PATH):
        try:
            os.remove(SESSION_STATE_PATH)
            return True
        except OSError:
            pass
    return False


# --- 3-Mode Compaction ---
# Protocol: directives/session-state-protocol.md § 3-Mode Compaction

COMPACTION_MODES = {
    "full": "Full Compaction — replace all context with 9-section anchor",
    "partial_older": "Partial Older — summarize old turns, keep recent 8 verbatim",
    "partial_recent": "Partial Recent — keep old context, summarize new direction",
}


def compact_session_state(
    mode: str,
    active_task: str,
    prior_context_summary: str = "",
    direction_change: Optional[Dict[str, str]] = None,
    recent_user_messages: Optional[List[str]] = None,
    decisions: Optional[List[Dict[str, str]]] = None,
    experts_deployed: Optional[List[Dict[str, str]]] = None,
    key_findings: Optional[List[str]] = None,
    files_modified: Optional[List[Dict[str, str]]] = None,
    current_phase: str = "",
    next_steps: Optional[List[str]] = None,
    intent: Optional[Dict[str, str]] = None,
    user_state: str = "",
    hot_context: Optional[List[Dict[str, str]]] = None,
) -> str:
    """
    Write a compacted session state anchor using the specified compaction mode.

    Modes:
        - "full": Complete context replacement. All 9 sections written fresh.
        - "partial_older": Old turns summarized, recent turns preserved verbatim.
        - "partial_recent": Old context kept, new direction summarized.

    Args:
        mode: One of "full", "partial_older", "partial_recent".
        active_task: Current task description.
        prior_context_summary: Compressed summary of older context (modes: full, partial_older).
        direction_change: Dict with keys: original_approach, pivot_trigger, new_direction,
                          carries_forward (mode: partial_recent).
        recent_user_messages: Verbatim recent user messages to preserve (all modes).
        decisions: List of decision dicts (all modes — always preserved).
        experts_deployed: List of expert dicts (all modes — always preserved).
        key_findings: Compressed findings (all modes).
        files_modified: File paths and descriptions (all modes — always preserved).
        current_phase: Current chain/workflow phase.
        next_steps: Next actions.
        intent: Validated intent dict.
        user_state: Frustration tier if detected ("tier_1", "tier_2", "tier_3", or "").
        hot_context: List of {"name": ..., "tier": ..., "files": ...} for hot experts.

    Returns:
        Path to the written state file.
    """
    if mode not in COMPACTION_MODES:
        raise ValueError(f"Invalid compaction mode: {mode}. Use one of: {list(COMPACTION_MODES.keys())}")

    os.makedirs(os.path.dirname(SESSION_STATE_PATH), exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# Session State Anchor",
        f"> Last updated: {timestamp}",
        f"> Compaction mode: **{mode}** — {COMPACTION_MODES[mode]}",
        "",
        "## Active Task",
        active_task,
        "",
    ]

    # --- User State (frustration tracking) ---
    if user_state:
        lines.extend([
            "## User State",
            f"- **Frustration level**: {user_state}",
            f"- **Behavior shift**: Active — see `directives/user-state-awareness.md`",
            "",
        ])

    # --- Intent ---
    if intent:
        lines.extend([
            "## Intent (Validated)",
            f"- **Deliverable**: {intent.get('deliverable', 'TBD')}",
            f"- **Audience**: {intent.get('audience', 'TBD')}",
            f"- **Success criteria**: {intent.get('success_criteria', 'TBD')}",
            "",
        ])

    # --- Mode-specific sections ---
    if mode == "partial_older" and prior_context_summary:
        lines.extend([
            "## Prior Context (Summarized)",
            prior_context_summary,
            "",
        ])

    if mode == "partial_recent" and direction_change:
        lines.extend([
            "## Direction Change",
            f"- **Original approach**: {direction_change.get('original_approach', '')}",
            f"- **Pivot trigger**: {direction_change.get('pivot_trigger', '')}",
            f"- **New direction**: {direction_change.get('new_direction', '')}",
            f"- **What carries forward**: {direction_change.get('carries_forward', '')}",
            "",
        ])

    # --- Always-preserved sections ---
    if decisions:
        lines.append("## Decisions Made")
        for d in decisions:
            lines.append(f"- **{d['decision']}**: {d['choice']} — {d.get('rationale', '')}")
        lines.append("")

    if experts_deployed:
        lines.append("## Experts Deployed")
        for e in experts_deployed:
            lines.append(f"- **{e['name']}**: {e['contribution']}")
        lines.append("")

    if hot_context:
        lines.append("## Hot Context Stack")
        for h in hot_context:
            lines.append(f"- {h['name']} | Tier {h.get('tier', '1')} | Files: {h.get('files', 'SKILL.md')}")
        lines.append("")

    if key_findings:
        lines.append("## Key Findings (Compressed)")
        for f in key_findings:
            lines.append(f"- {f}")
        lines.append("")

    if files_modified:
        lines.append("## Files Created/Modified This Session")
        for fm in files_modified:
            lines.append(f"- `{fm['path']}`: {fm['description']}")
        lines.append("")

    if current_phase:
        lines.extend(["## Current Phase", current_phase, ""])

    if next_steps:
        lines.append("## Next Steps")
        for i, step in enumerate(next_steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    # --- Verbatim user messages (all modes) ---
    if recent_user_messages:
        lines.append("## Recent User Messages (Verbatim)")
        for msg in recent_user_messages[-5:]:  # Keep last 5 max
            lines.append(f"> {msg}")
            lines.append("")

    content = "\n".join(lines)
    with open(SESSION_STATE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return SESSION_STATE_PATH


def detect_compaction_mode(
    turns_count: int,
    user_changed_direction: bool = False,
    spawning_sub_agent: bool = False,
) -> str:
    """
    Automatically detect the optimal compaction mode based on session state.

    Args:
        turns_count: Total turns in the conversation so far.
        user_changed_direction: Whether the user pivoted mid-session.
        spawning_sub_agent: Whether we're about to spawn a sub-agent.

    Returns:
        One of "full", "partial_older", "partial_recent".
    """
    if spawning_sub_agent:
        return "full"
    if user_changed_direction:
        return "partial_recent"
    if turns_count > 10:
        return "partial_older"
    return "full"  # Default for short sessions


# --- Frustration Detection ---
# Protocol: directives/user-state-awareness.md

FRUSTRATION_TIER_1 = [
    "this isn't working", "that's wrong", "you already",
    "i already told you", "i said", "that's not what i asked",
    "not what i wanted", "try again", "please just", "just do it",
    "stop asking", "stop suggesting", "why can't you", "why won't you",
    "this is broken", "you keep", "no, i meant", "wrong",
    "ugh", "sigh", "come on", "ffs", "wtf", "smh",
]

FRUSTRATION_TIER_2 = [
    "fine", "whatever", "sure", "ok", "nope",
]

FRUSTRATION_TIER_3 = [
    "forget it", "never mind", "i'll do it myself",
    "this is useless", "nevermind",
]


def detect_frustration(user_message: str) -> Optional[str]:
    """
    Detect user frustration level from a message.

    Returns:
        "tier_1", "tier_2", "tier_3", or None if no frustration detected.
    """
    msg = user_message.lower().strip()

    # Tier 3 first (most severe)
    for phrase in FRUSTRATION_TIER_3:
        if phrase in msg:
            return "tier_3"

    # Tier 1 (explicit frustration)
    for phrase in FRUSTRATION_TIER_1:
        if phrase in msg:
            return "tier_1"

    # Tier 2 (only for very short messages — these are ambiguous in longer contexts)
    if len(msg.split()) <= 3:
        for phrase in FRUSTRATION_TIER_2:
            if msg == phrase or msg == phrase + ".":
                return "tier_2"

    return None

