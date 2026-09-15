"""Offline reference model for a decision-reconciliation protocol.

NOT a deployed hook, classifier, or document store. The session model supplies
semantic decisions. These functions check identity, provenance, preservation,
freshness, and the context exported to a writer. No network or filesystem writes.
"""
from __future__ import annotations

import copy
import hashlib
import json

ACTIVE = {"approved", "candidate", "reference"}
HISTORY = {"rejected", "superseded", "parked"}


class Conflict(ValueError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def initial(owner, purpose, goal):
    if not all(isinstance(s, str) and s.strip() for s in (owner, purpose, goal)):
        raise Conflict("Owner, purpose and goal must be explicit.")
    return {"owner": owner, "purpose": purpose, "goal": goal, "revision": 0,
            "feedback": [], "resolved": [], "items": {}, "next_action": None}


def receive(state, event):
    """Capture a user turn, without deciding what it means or inferring approval."""
    if not all(isinstance(event.get(k), str) and event[k].strip() for k in ("id", "text", "source")):
        raise Conflict("Feedback needs exact text, stable turn identity and a source.")
    existing = next((e for e in state["feedback"] if e["id"] == event["id"]), None)
    if existing:
        if existing != event:
            raise Conflict("A feedback identity was reused with different content.")
        return copy.deepcopy(state)
    out = copy.deepcopy(state)
    out["feedback"].append(copy.deepcopy(event))
    out["revision"] += 1
    return out


def pending(state):
    return [e for e in state["feedback"] if e["id"] not in state["resolved"]]


def evidence(state, citation):
    if not isinstance(citation, dict):
        raise Conflict("A decision requires feedback evidence.")
    event = next((e for e in state["feedback"] if e["id"] == citation.get("event")), None)
    quote = citation.get("quote")
    if not event or not isinstance(quote, str) or not quote.strip() or quote not in event["text"]:
        raise Conflict("Decision quote is absent from its cited user turn.")
    # Provenance only: a matching quote does NOT prove the model interpreted it correctly.


def reconcile(state, proposal, *, owner, purpose, expected_revision):
    """Validate a semantic proposal; never append a new CURRENT block to an old one.

    Production implementation must put receive/reconcile and the history journal
    inside the existing document-history transaction/lock. This model does not
    claim to implement filesystem concurrency or automatic semantic judgment.
    """
    if owner != state["owner"] or purpose != state["purpose"]:
        raise Conflict("Wrong task or artifact purpose.")
    if expected_revision != state["revision"]:
        raise Conflict("Stale revision; recover and reconcile new decisions before retrying.")
    awaiting = {e["id"] for e in pending(state)}
    resolutions = proposal.get("resolutions", [])
    ids = [r.get("event") for r in resolutions]
    if len(ids) != len(set(ids)) or set(ids) != awaiting:
        raise Conflict("Every pending turn needs one semantic disposition, including no-change.")
    for resolution in resolutions:
        evidence(state, resolution)
        if not resolution.get("effect"):
            raise Conflict("Disposition must explain its effect or why there is no change.")
    items = proposal.get("items", [])
    if not isinstance(items, list):
        raise Conflict("Items must be a list.")
    mapped = {}
    current_slots = set()
    for item in items:
        if not all(item.get(k) for k in ("id", "slot", "path", "sha256", "status")):
            raise Conflict("Each item needs identity, purpose slot, path, hash and status.")
        if item["id"] in mapped:
            raise Conflict("Duplicate item identity.")
        if item["status"] not in ACTIVE | HISTORY:
            raise Conflict("Unknown lifecycle state.")
        evidence(state, item.get("decision"))
        if item["status"] in {"approved", "candidate"}:
            if item["slot"] in current_slots:
                raise Conflict("Two current objects claim the same purpose slot.")
            current_slots.add(item["slot"])
        if item["status"] == "approved" and not item.get("approved_excerpt"):
            raise Conflict("Approved components need the exact preserved text or asset identity.")
        mapped[item["id"]] = copy.deepcopy(item)
    overrides = proposal.get("overrides", {})
    for item_id, old in state["items"].items():
        new = mapped.get(item_id)
        if new is None:
            raise Conflict("Never silently drop a registered item; retire it explicitly.")
        if old["status"] == "approved" and any(
                old.get(k) != new.get(k) for k in ("status", "path", "sha256", "approved_excerpt")):
            evidence(state, overrides.get(item_id))
            if overrides[item_id].get("event") not in awaiting:
                raise Conflict("Changing approved work needs a new decision, not a reused old quote.")
        if old["status"] in HISTORY and new["status"] in ACTIVE:
            evidence(state, overrides.get(item_id))
            if overrides[item_id].get("event") not in awaiting:
                raise Conflict("Restoring history requires a new explicit restoration decision.")
    goal = proposal.get("goal", state["goal"])
    if goal != state["goal"]:
        change = proposal.get("goal_change")
        evidence(state, change)
        if change.get("event") not in awaiting or change.get("kind") != "explicit-objective-change":
            raise Conflict("A refinement cannot silently replace the overall objective.")
    action = proposal.get("next_action")
    if action is not None:
        if not action.get("text") or not action.get("targets"):
            raise Conflict("Action needs text and explicit target identities.")
        for target in action["targets"]:
            if target not in mapped or mapped[target]["status"] not in ACTIVE:
                raise Conflict("Next action refers to retired, rejected or unknown work.")
    out = copy.deepcopy(state)
    out.update(items=mapped, goal=goal, next_action=action)
    out["resolved"] += ids
    out["revision"] += 1
    return out


def packet(state, observed_hashes):
    """Thin writer context; historical text is never included by default."""
    if pending(state):
        return {"status": "NEEDS_RECONCILIATION", "pending_turns": [e["id"] for e in pending(state)],
                "next_action": None}
    for item in state["items"].values():
        if item["status"] in ACTIVE and observed_hashes.get(item["path"]) != item["sha256"]:
            return {"status": "SOURCE_CHANGED", "path": item["path"], "next_action": None}
    active = [{k: item[k] for k in ("id", "slot", "path", "sha256", "status", "approved_excerpt") if k in item}
              for item in state["items"].values() if item["status"] in ACTIVE]
    return {"status": "CURRENT", "owner": state["owner"], "purpose": state["purpose"],
            "revision": state["revision"], "goal": state["goal"], "active": active,
            "next_action": state["next_action"], "state_digest": digest(state)}


def validate_handoff(handed, state, observed_hashes):
    current = packet(state, observed_hashes)
    if current["status"] != "CURRENT" or handed != current:
        raise Conflict("Handoff is stale, edited or bound to another task. Rebuild from reconciled state.")
    return True


def inspect_legacy(text):
    """Detect stacked current-version banners, not semantic rejection or quality."""
    import re
    markers = []
    for number, line in enumerate(text.splitlines(), 1):
        if re.search(r"(?:CURRENT|Current carousel|COPY PREVIEW|Latest:).*\bv0*\d+", line):
            markers.append({"line": number, "text": line[:240]})
    versions = set()
    for marker in markers:
        match = re.search(r"\bv0*(\d+)\b", marker["text"])
        if match:
            versions.add(int(match.group(1)))
    return {"finding": "COMPETING_CURRENT_LABELS" if len(versions) > 1 else "NO_STACK_DETECTED",
            "markers": markers, "distinct_versions": sorted(versions),
            "semantic_cause": "UNPROVEN; inspect decisions and actual consumer reads"}
