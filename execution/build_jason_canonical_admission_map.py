#!/usr/bin/env python3
"""Build and check the canonical Jason master-layer admission manifest.

The ordinary Jason skill remains available for its native practitioner work.
This manifest controls only what may be imported into the buyer-psychology
master layer as generative decision intelligence or factual support.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/jason-fladlien-marketing"
WORKFLOWS = SKILL / "workflows"
PROMPTS = SKILL / "references/prompts"
PROMPTS_V2 = SKILL / "references/prompts-v2"
LEGACY_PROMPTS = SKILL / "references/_legacy-prompts"
LAYER = ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer"
SEED = LAYER / "legacy-admission-map.json"
OUT_JSON = LAYER / "canonical-admission-map.json"
OUT_MD = LAYER / "canonical-admission-map.md"

STATUSES = {"ADMIT", "DEFENSIVE-LITERACY-ONLY", "EXCLUDE-FROM-MASTER"}

NEW_WORKFLOWS = {
    "best-90-minutes.md": (
        "ADMIT",
        "disclose the teaching and offer agendas, deliver standalone value, and preserve a voluntary next step",
        "time-or-money framing and selling sequence remain practitioner craft, not evidence or permission pressure",
    ),
    "conversational-pattern-bank.md": (
        "DEFENSIVE-LITERACY-ONLY",
        "detect linking, identity, commitment, elicitation, and presupposition patterns",
        "pattern injection can hide influence or turn buyer language into an unearned commitment",
    ),
    "game-selection-advantage-audit.md": (
        "ADMIT",
        "test game viability, observable advantage, and a reversible beta before persuasion",
        "advantage remains a hypothesis until buyer behavior, sales, and collection are separately observed",
    ),
    "offer-adoption-and-proof-loop.md": (
        "ADMIT",
        "design supported early wins, routine safeguards, consented check-ins, and permissioned proof capture",
        "adoption signals are not testimonial permission, causal proof, retention, or market demand",
    ),
    "offer-anatomy-tie-down-architecture.md": (
        "ADMIT",
        "make core, cost, bonus, risk, scarcity, terms, and buyer responsibilities explicit",
        "tie-downs, urgency, scarcity, anchors, and guarantees are excluded unless truthful, material, and autonomy-safe",
    ),
    "offer-terms-diagnostic-and-rebuild.md": (
        "ADMIT",
        "diagnose evidenced Time, Effort, Routine, Money, and Status burdens before adding persuasion",
        "buyer burden may not be invented; no term, lever, ratio, or offer change is universally preferred",
    ),
    "one-sitting-product-machine.md": (
        "EXCLUDE-FROM-MASTER",
        "none",
        "product-production velocity is not a distinct buyer-decision mechanism and adds no evidence calibration",
    ),
    "point-architecture-engine.md": (
        "ADMIT",
        "sequence proofable teaching points with explicit setup, payoff, and voluntary comprehension checks",
        "emotional ratios and commitment density remain practitioner heuristics and may not manufacture agreement",
    ),
    "set-setting-outcome-reframe.md": (
        "DEFENSIVE-LITERACY-ONLY",
        "detect context-setting and ideal-versus-realistic outcome reframes",
        "set and setting language can overframe the receiver or make an unsupported outcome feel inevitable",
    ),
    "tie-down-density-pass.md": (
        "DEFENSIVE-LITERACY-ONLY",
        "detect repeated agreement, commitment, and compliance-loading patterns",
        "density targets and gap bisection can convert comprehension checks into pressure",
    ),
    "webinar-campaign-architecture.md": (
        "ADMIT",
        "build a disclosed, source-traceable teaching-to-offer sequence with proof and risk boundaries",
        "advertised close rates, scarcity, price effects, and causal conversion claims remain unverified",
    ),
}

CANONICAL_WORKFLOW_OVERRIDES = {
    "hypnotic-writing-patterns-engine.md": (
        "DEFENSIVE-LITERACY-ONLY",
        "detect embedded-command, presupposition, pacing, and future-pacing patterns",
        "the canonical expansion still includes covert-command and subconscious-influence mechanics that are not admitted for generation",
    ),
    "incomparable-offer-architect.md": (
        "ADMIT",
        "competitor census, complementary deliverables, truthful comparison, and TERMS-aware burden reduction",
        "modality stacking, replacement-cost anchors, and incomparability claims require evidence and may not create fulfillment or choice burden",
    ),
    "spoken-copy-live-close-architecture.md": (
        "DEFENSIVE-LITERACY-ONLY",
        "detect validate-reframe-close sequencing and preserve explicit buyer questions",
        "spoken pacing, objection redirection, and embedded influence can suppress a material no or manufacture commitment",
    ),
}

BORN_V2 = {
    "best-90-minutes-blueprint.md": NEW_WORKFLOWS["best-90-minutes.md"],
    "conversational-pattern-bank.md": NEW_WORKFLOWS["conversational-pattern-bank.md"],
    "offer-adoption-and-proof-loop.md": NEW_WORKFLOWS["offer-adoption-and-proof-loop.md"],
    "offer-terms-diagnostic-and-rebuild.md": NEW_WORKFLOWS["offer-terms-diagnostic-and-rebuild.md"],
    "point-architecture-engine.md": NEW_WORKFLOWS["point-architecture-engine.md"],
    "set-setting-reframe.md": NEW_WORKFLOWS["set-setting-outcome-reframe.md"],
    "tie-down-density-pass.md": NEW_WORKFLOWS["tie-down-density-pass.md"],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_seed() -> dict[str, dict[str, str]]:
    data = json.loads(SEED.read_text(encoding="utf-8"))
    return {item["path"]: item for item in data["entries"]}


def entry(path: Path, surface: str, policy: tuple[str, str, str], inherited_from: str | None = None) -> dict[str, str]:
    status, safe_kernel, risk_anchor = policy
    if status not in STATUSES:
        raise ValueError(f"invalid status for {path}: {status}")
    record = {
        "path": path.relative_to(ROOT).as_posix(),
        "surface": surface,
        "surface_role": surface,
        "status": status,
        "safe_kernel": safe_kernel,
        "risk_anchor": risk_anchor,
        "sha256": sha256(path),
    }
    if inherited_from:
        record["inherited_from"] = inherited_from
        record["derivation"] = "structure-pure-refactor"
    else:
        record["derivation"] = "canonical-original"
    record["review_state"] = "CANONICAL-ADJUDICATED"
    return record


def build() -> dict[str, object]:
    seed = load_seed()
    entries: list[dict[str, str]] = []

    for path in sorted(WORKFLOWS.glob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if path.name in CANONICAL_WORKFLOW_OVERRIDES:
            policy = CANONICAL_WORKFLOW_OVERRIDES[path.name]
        elif rel in seed:
            item = seed[rel]
            policy = (item["status"], item["safe_kernel"], item["risk_anchor"])
        else:
            policy = NEW_WORKFLOWS[path.name]
        entries.append(entry(path, "workflow", policy))

    prompt_seed: dict[str, dict[str, str]] = {}
    for path in sorted(PROMPTS.glob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        item = seed[rel]
        prompt_seed[path.name] = item
        policy = (item["status"], item["safe_kernel"], item["risk_anchor"])
        entries.append(entry(path, "compatibility-prompt", policy))

    for path in sorted(PROMPTS_V2.glob("*.md")):
        if path.name in BORN_V2:
            entries.append(entry(path, "prompt-v2-born", BORN_V2[path.name]))
            continue
        source = prompt_seed[path.name]
        source_path = f"skills/jason-fladlien-marketing/references/prompts/{path.name}"
        policy = (
            source["status"],
            source["safe_kernel"],
            "Structure-pure formatting does not upgrade evidence or ethics; inherited boundary: "
            + source["risk_anchor"],
        )
        entries.append(entry(path, "prompt-v2-refactor", policy, inherited_from=source_path))

    legacy = sorted(LEGACY_PROMPTS.glob("*.md"))
    prompt_files = sorted(PROMPTS.glob("*.md"))
    duplicate_failures = [
        path.name
        for path in prompt_files
        if not (LEGACY_PROMPTS / path.name).exists()
        or sha256(path) != sha256(LEGACY_PROMPTS / path.name)
    ]
    if len(legacy) != len(prompt_files) or duplicate_failures:
        raise ValueError(f"legacy prompt mirror drift: {duplicate_failures}")

    by_status = Counter(item["status"] for item in entries)
    by_surface = Counter(item["surface"] for item in entries)
    return {
        "schema_version": "2.0",
        "scope": "buyer-psychology-master-layer-admission-only",
        "authority": "Google Antigravity canonical Jason package",
        "policy": (
            "ADMIT permits only the named safe kernel. Defensive-only material may be used to detect and replace a pattern. "
            "Excluded material may not support generation or factual claims. Structure-pure formatting and duplicate files add no evidence weight."
        ),
        "summary": {
            "entries": len(entries),
            "by_surface": dict(sorted(by_surface.items())),
            "by_status": dict(sorted(by_status.items())),
            "legacy_duplicate_files": len(legacy),
            "legacy_duplicate_evidence_weight": 0,
        },
        "entries": sorted(entries, key=lambda item: item["path"]),
    }


def render_md(data: dict[str, object]) -> str:
    summary = data["summary"]
    lines = [
        "# Jason Canonical Admission and Quarantine Map",
        "",
        "**Status:** cold defensive manifest",
        "**Authority:** Google Antigravity canonical Jason package",
        "**Scope:** buyer-psychology master-layer admission only",
        "",
        "## Verdict",
        "",
        "The canonical Jason package remains available for its native practitioner work. This manifest controls the smaller question: what may enter the source-grounded buyer-psychology master layer.",
        "",
        f"It covers **{summary['entries']} non-duplicate surfaces**: 38 workflows, 26 compatibility prompts, and 33 preferred structure-pure v2 prompts. The 26 `_legacy-prompts` files are byte-identical mirrors and contribute zero additional evidence.",
        "",
        "| Admission class | Count | Generative use in master layer |",
        "|---|---:|---|",
        f"| `ADMIT` | {summary['by_status'].get('ADMIT', 0)} | Only the named safe kernel |",
        f"| `DEFENSIVE-LITERACY-ONLY` | {summary['by_status'].get('DEFENSIVE-LITERACY-ONLY', 0)} | Detection, red-team analysis, and nearest safe replacement only |",
        f"| `EXCLUDE-FROM-MASTER` | {summary['by_status'].get('EXCLUDE-FROM-MASTER', 0)} | None |",
        "",
        "`ADMIT` never imports embedded ratios, clinical or neuroscience authority, inferred hidden motives, fabricated examples, pressure, scarcity, guarantees, or conversion claims. A v2 Output Contract improves execution structure; it does not corroborate its source.",
        "",
        "## Canonical Inventory",
        "",
        "| Surface | Path | Status | Permitted kernel | Risk boundary |",
        "|---|---|---|---|---|",
    ]
    for item in data["entries"]:
        lines.append(
            f"| {item['surface']} | `{item['path']}` | `{item['status']}` | {item['safe_kernel']} | {item['risk_anchor']} |"
        )
    lines.extend(
        [
            "",
            "## Runtime Boundary",
            "",
            "This map is cold. It does not remove or rewrite canonical Jason workflows and prompts, create a route, or upgrade practitioner claims. The situation compiler may cite only admitted safe kernels. Defensive material may be loaded only for a named audit. Excluded material may not support a generative mechanism or factual claim.",
            "",
            "## Verification",
            "",
            "Run `python3 execution/build_jason_canonical_admission_map.py --check`. It fails on missing or extra canonical surfaces, content drift, v2/source mismatch, legacy duplicate drift, or generated-manifest drift.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    json_text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    md_text = render_md(data)
    if args.check:
        failures = []
        if not OUT_JSON.exists() or OUT_JSON.read_text(encoding="utf-8") != json_text:
            failures.append(str(OUT_JSON.relative_to(ROOT)))
        if not OUT_MD.exists() or OUT_MD.read_text(encoding="utf-8") != md_text:
            failures.append(str(OUT_MD.relative_to(ROOT)))
        if failures:
            print("FAIL: canonical Jason admission manifest drift")
            for path in failures:
                print(f"- {path}")
            return 1
        print("PASS: canonical Jason admission manifest")
        print(f"- surfaces: {data['summary']['entries']}")
        print(f"- status counts: {data['summary']['by_status']}")
        print(f"- legacy duplicates: {data['summary']['legacy_duplicate_files']} (evidence weight 0)")
        return 0
    OUT_JSON.write_text(json_text, encoding="utf-8")
    OUT_MD.write_text(md_text, encoding="utf-8")
    print(f"WROTE {OUT_JSON.relative_to(ROOT)}")
    print(f"WROTE {OUT_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
