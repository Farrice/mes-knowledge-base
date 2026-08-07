#!/usr/bin/env python3
"""
Skill Auditor — Tier-grade 209 skill directories using heuristics + trace data.

Fix 3a from system audit (_active/harness/system-audit/audit-2026-04-24.md).

The audit found that skill quality variance is currently UNKNOWN — worse than
known-bad. This auditor produces an auditable A/B/C/REVIEW classification for
every skill so the next decision (archive C-tier? promote B-tier? leave alone?)
is grounded in evidence rather than vibes.

Tier definitions (per audit, mapped to observable signals):

    A-tier  → World-class workflow with real expert thinking encoded.
              Evidence: full structure (SKILL.md + genius.md + 3+ workflows + references/)
                        AND (recent traces with avg ≥7.5 OR referenced from
                            CLAUDE.md/COUNCIL.md/expert_router.py).

    B-tier  → Solid framework.
              Evidence: structurally complete (SKILL.md + (genius.md OR 3+ workflows))
                        AND (some traces OR cross-referenced).

    C-tier  → Generic prompt with expert label.
              Evidence: SKILL.md only OR <2 workflows AND no genius.md
                        AND no recent traces AND not cross-referenced.

    REVIEW  → Heuristics conflict (e.g., minimal structure but high trace scores;
              or full structure but never used). Needs human judgment.

The output is `evolution_store/skill_audit_<DATE>.md` plus a JSONL with
machine-readable per-skill records. SKILL_INDEX.md is updated separately by
a follow-up command (`update-index`) so the auditor stays read-only by default.

Usage:
    python3 execution/skill_auditor.py audit                    # Run audit, write report
    python3 execution/skill_auditor.py duplication              # Cross-ref skills × agents
    python3 execution/skill_auditor.py update-index --apply     # Annotate SKILL_INDEX.md with tier
    python3 execution/skill_auditor.py archive --tier C --apply # Move C-tier to _archive/skills/
"""

import sys
import json
import re
import argparse
import shutil
from pathlib import Path
from datetime import datetime, date, timedelta
from typing import Dict, List, Any, Optional, Set
from collections import defaultdict

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents"
ARCHIVE_DIR = ROOT / "_archive" / "skills"
TRACES_DIR = ROOT / "evolution_store" / "v2_traces"
SKILL_INDEX = ROOT / "SKILL_INDEX.md"
AUDIT_OUT_DIR = ROOT / "evolution_store"
CLAUDE_MD = ROOT / "CLAUDE.md"
COUNCIL_MD = ROOT / "COUNCIL.md"
EXPERT_ROUTER = ROOT / "execution" / "expert_router.py"

TIER_A_MIN_TRACE_SCORE = 7.5
TIER_TRACE_WINDOW_DAYS = 60

# UTILITY tier — Anthropic-provided or system-utility skills.
# These provide infrastructure (file conversion, design tools, code scaffolding)
# rather than expert thinking. They should NOT be archived as C-tier and should
# NOT be tier-graded against the expert quality rubric. Match by exact name.
UTILITY_SKILLS = {
    # Document/file conversion utilities (Anthropic-provided)
    "pdf", "docx", "pptx", "xlsx",
    # Design/visual scaffolding
    "algorithmic-art", "asset_generator", "brand-guidelines", "canvas-design",
    "creative-assembly", "creative-direction", "design-md", "frontend-design",
    "theme-factory", "remotion-video-creation", "slack-gif-creator",
    # Development/code utilities
    "doc-coauthoring", "gemini-api-dev", "mcp-builder", "react-components",
    "skill-creator", "stitch-loop", "swarm-commander", "web-artifacts-builder",
    "webapp-testing", "internal-comms",
    # Research/utility scaffolding
    "consumer-posture-research", "market_intelligence",
}


# ─────────────────────────────────────────────────────────
# Skill structural fingerprint
# ─────────────────────────────────────────────────────────

def fingerprint_skill(skill_dir: Path) -> Dict[str, Any]:
    """Inspect a skill directory and report structural signals."""
    has_skill_md = (skill_dir / "SKILL.md").exists()
    has_genius = (skill_dir / "genius.md").exists()
    workflows_dir = skill_dir / "workflows"
    references_dir = skill_dir / "references"

    workflow_files = []
    if workflows_dir.exists() and workflows_dir.is_dir():
        workflow_files = [p for p in workflows_dir.glob("*.md") if not p.name.startswith(".")]

    reference_count = 0
    if references_dir.exists() and references_dir.is_dir():
        reference_count = sum(1 for _ in references_dir.rglob("*") if _.is_file())

    skill_md_size = (skill_dir / "SKILL.md").stat().st_size if has_skill_md else 0
    genius_size = (skill_dir / "genius.md").stat().st_size if has_genius else 0

    return {
        "name": skill_dir.name,
        "has_skill_md": has_skill_md,
        "has_genius": has_genius,
        "skill_md_bytes": skill_md_size,
        "genius_bytes": genius_size,
        "workflow_count": len(workflow_files),
        "workflow_names": [p.stem for p in workflow_files],
        "reference_count": reference_count,
    }


# ─────────────────────────────────────────────────────────
# Craft standard checks (directives/skill-craft-standard.md)
# Cheap, deterministic, advisory only — never affects tier classification.
# (The SEVEN heartbeat checks below — six promoted 2026-07-09, menu_parity added 2026-07-25 — DO affect tier.)
# ─────────────────────────────────────────────────────────

HARDCODED_SCORE_RE = re.compile(r"--intent\s+[89]\b|expert-score\s+[89]\b|score.*[89]/10", re.IGNORECASE)


def craft_standard_flags(skill_dir: Path, fp: Dict[str, Any]) -> List[str]:
    """Flag cheap, deterministic craft-standard gaps (advisory, not tier-affecting)."""
    if fp["name"] in UTILITY_SKILLS:
        return []
    flags = []
    if not fp["has_genius"]:
        flags.append("no genius.md")
    if fp["workflow_count"] == 0:
        flags.append("zero workflows")
    skill_md = skill_dir / "SKILL.md"
    if skill_md.exists():
        text = skill_md.read_text(errors="ignore").lower()
        if "domain" not in text:
            flags.append("frontmatter missing domain")
        if "when_to_use" not in text:
            flags.append("frontmatter missing when_to_use")
    workflows_dir = skill_dir / "workflows"
    if workflows_dir.exists():
        for wf in workflows_dir.glob("*.md"):
            try:
                if HARDCODED_SCORE_RE.search(wf.read_text(errors="ignore")):
                    flags.append(f"hardcoded score pattern in {wf.name}")
                    break
            except Exception:
                pass
    return flags


# ─────────────────────────────────────────────────────────
# Heartbeat checks — tier-affecting (Harness Apex Wave 2, 2026-07-09)
#
# Seven checks: six from directives/skill-craft-standard.md §8 / embodiment-
# standard.md build checklist, promoted from advisory prose to real
# content checks (regex/structure, not vibes). Failing ≥2 caps the tier
# at B (A demotes to B; lower tiers unchanged). --advisory restores the
# old non-gating behavior — every advisory run is logged (compass-not-cage,
# never a silent bypass). UTILITY skills are exempt (not graded against
# the expert rubric).
# ─────────────────────────────────────────────────────────

HEARTBEAT_FAIL_CAP_THRESHOLD = 2   # failing this many checks caps the tier
HEARTBEAT_CAP_TIER = "B"
ADVISORY_LOG = ROOT / "evolution_store" / "skill_auditor_advisory_runs.jsonl"

# Entity regex calibrated in skill_census.py (E1: fabricated-number-proof,
# proper-noun bigrams deliberately removed 2026-07-02). Import to keep one
# source of truth; inline fallback mirrors it.
try:
    from skill_census import (ENTITY_RE as _ENTITY_RE,
                              NUMBERING_RE as _NUMBERING_RE,
                              SECTION_RE as _SECTION_RE,
                              sections_zero_entity as _sections_zero_entity)
except ImportError:
    _SECTION_RE = re.compile(r"^#{2,3}\s+", re.M)
    _ENTITY_RE = re.compile(
        r"\$\d|\d+%|\d{2,}|\d+\s?(?:x|lb|kg|kcal|min|hr|k)\b"
        r"|[\"“][^\"”\n]{6,}[\"”]|https?://")
    _NUMBERING_RE = re.compile(r"\b(?:pattern|step|phase|tier|level|check|rule)\s+\d+\b", re.I)

    def _sections_zero_entity(genius: str):
        idx = [m.start() for m in _SECTION_RE.finditer(genius)]
        if not idx:
            return 0, 0.0
        idx.append(len(genius))
        total, zero = 0, 0
        for a, b in zip(idx, idx[1:]):
            body = genius[a:b]
            if len(body.strip()) < 80:
                continue
            body = "\n".join(body.splitlines()[1:])
            body = _NUMBERING_RE.sub("", body)
            total += 1
            if not _ENTITY_RE.search(body):
                zero += 1
        return total, (zero / total if total else 0.0)

# Named-entity floor threshold: skill_census.grade() flags zero_entity_ratio
# ≥0.2 (calibrated 12/13 against the 2026-07-02 blind validation set).
HEARTBEAT_ZERO_ENTITY_MAX = 0.2

_HB_LIST_ITEM_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.+)", re.M)
_HB_HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$", re.M)
_HB_ANTI_HEADING_RE = re.compile(r"anti.?pattern", re.I)
_HB_ANTI_ITEM_RE = re.compile(r"\b(never|don'?t|do not|anti-pattern|failure mode)\b", re.I)
# "Source attribution" on an anti-pattern: a date, timestamp, URL, source: tag,
# verbatim quote, file path, or a named provenance word.
_HB_SOURCE_ATTR_RE = re.compile(
    r"\b\d{4}-\d{2}-\d{2}\b|\(\d{4}\)|\b20\d{2}\b|\d{1,2}:\d{2}"
    r"|https?://|\bsource\b|\bsourced\b|\bper\b\s+`|\.md\b"
    r"|\btranscript\b|\bepisode\b|\binterview\b|\bpodcast\b|\bvideo\b"
    r"|[\"“][^\"”\n]{6,}[\"”]", re.I)
_HB_INLINE_QUOTE_RE = re.compile(r"[\"“][^\"”\n]{40,}[\"”]")
_HB_BLOCKQUOTE_RE = re.compile(r"(?:^>.*\n?)+", re.M)
# Aligned with skill_census.RECOG_RE (calibrated 2026-07-02) + the craft-
# standard phrasings ("recognition test", "using <X> vocabulary").
_HB_RECOG_RE = re.compile(
    r"recognition test|recognize this as|distinguish (?:this|it) from"
    r"|(?:wearing|using) (?:\w+ )?vocabulary", re.I)
_HB_LABEL_RE = re.compile(r"\bVERIFIED\b|\bLIKELY\b|\bUNCONFIRMED\b")
# Contract concept, not one literal: claim-safe (the standard's own exemplar)
# writes "Output Requirements"; others write "Output Schema"/"Output Format";
# born-v2-era workflows write "Output Contract" (instrument false-negative found
# by the Wave 3 repair-fleet PoC, 2026-07-17 — see docs/solutions/
# 2026-07-17-repair-fleet-poc-three-failure-shapes.md).
_HB_OUTPUT_SCHEMA_RE = re.compile(r"output\s+(schema|format|requirements?|contract)", re.I)
_HB_QUALITY_GATE_RE = re.compile(r"quality\s+gate", re.I)
# Menu-parity (check 7, 2026-07-25): named exemptions + build-artifact filenames.
_MENU_EXEMPT_RE = re.compile(r"^\s*(?:menu_exempt\s*:|status\s*:\s*superseded\b|superseded_by\s*:)",
                             re.I | re.M)
_MENU_VARIANT_RE = re.compile(r"\.variant\.|\.pre-evolution\.|backup", re.I)
_MENU_SURFACES_CACHE: "tuple | None" = None


def _menu_surfaces():
    """(command_stems, wrapper_blob) across .claude/commands + .agent/workflows.
    Cached per process — the check runs per skill but the surfaces are global."""
    global _MENU_SURFACES_CACHE
    if _MENU_SURFACES_CACHE is not None:
        return _MENU_SURFACES_CACHE
    cmd_dir = ROOT / ".claude" / "commands"
    wf_dir = ROOT / ".agent" / "workflows"
    stems = {p.stem for p in cmd_dir.glob("*.md")} if cmd_dir.is_dir() else set()
    parts = []
    for d in (wf_dir, cmd_dir):
        if d.is_dir():
            for p in d.glob("*.md"):
                parts.append(_read_text(p))
    _MENU_SURFACES_CACHE = (stems, "\n".join(parts))
    return _MENU_SURFACES_CACHE


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _anti_pattern_items(genius: str) -> List[str]:
    """List items inside anti-pattern-titled sections; fallback = any list
    item anywhere whose text reads as a refusal (never/don't/anti-pattern)."""
    items: List[str] = []
    headings = list(_HB_HEADING_RE.finditer(genius))
    for i, m in enumerate(headings):
        if not _HB_ANTI_HEADING_RE.search(m.group(2)):
            continue
        level = len(m.group(1))
        end = len(genius)
        for nxt in headings[i + 1:]:
            if len(nxt.group(1)) <= level:
                end = nxt.start()
                break
        section = genius[m.end():end]
        items.extend(t.strip() for t in _HB_LIST_ITEM_RE.findall(section))
    if not items:
        items = [t.strip() for t in _HB_LIST_ITEM_RE.findall(genius)
                 if _HB_ANTI_ITEM_RE.search(t)]
    return items


def heartbeat_checks(skill_dir: Path, fp: Dict[str, Any]) -> List[Dict[str, Any]]:
    """The seven tier-affecting heartbeat checks (6 craft + menu_parity). Each individually reportable:
    [{"check", "passed", "detail"}, ...]."""
    genius = _read_text(skill_dir / "genius.md")
    skill_md = _read_text(skill_dir / "SKILL.md")
    references_dir = skill_dir / "references"
    workflows_dir = skill_dir / "workflows"
    checks: List[Dict[str, Any]] = []

    # 1. Anti-patterns ≥5 with source attribution (genius.md).
    anti_items = _anti_pattern_items(genius)
    sourced = [t for t in anti_items if _HB_SOURCE_ATTR_RE.search(t)]
    checks.append({
        "check": "anti_patterns_sourced",
        "passed": len(sourced) >= 5,
        "detail": f"{len(sourced)} source-attributed anti-pattern item(s) "
                  f"(of {len(anti_items)} found; need ≥5 with a date/quote/source anchor)",
    })

    # 2. ≥3 verbatim exemplars (quoted material) in genius.md.
    blockquotes = _HB_BLOCKQUOTE_RE.findall(genius)
    inline_quotes = _HB_INLINE_QUOTE_RE.findall(genius)
    exemplar_count = len(blockquotes) + len(inline_quotes)
    checks.append({
        "check": "verbatim_exemplars",
        "passed": exemplar_count >= 3,
        "detail": f"{len(blockquotes)} blockquote block(s) + {len(inline_quotes)} "
                  f"long inline quote(s) = {exemplar_count} (need ≥3 verbatim exemplars)",
    })

    # 3. Recognition-test section present (SKILL.md or genius.md).
    recog_hit = _HB_RECOG_RE.search(skill_md) or _HB_RECOG_RE.search(genius)
    checks.append({
        "check": "recognition_test",
        "passed": bool(recog_hit),
        "detail": (f"found: \"{recog_hit.group(0)}\"" if recog_hit
                   else "no recognition-test language in SKILL.md or genius.md "
                        "(\"would [expert] recognize this as theirs...\")"),
    })

    # 4. references/ source-ledger present.
    ledger_files = []
    labeled = False
    if references_dir.is_dir():
        for p in references_dir.rglob("*"):
            if not p.is_file():
                continue
            if re.search(r"ledger|source", p.name, re.I):
                ledger_files.append(p.name)
            elif not labeled and _HB_LABEL_RE.search(_read_text(p)):
                labeled = True
                ledger_files.append(f"{p.name} (VERIFIED/LIKELY/UNCONFIRMED labels)")
    genius_ledger = bool(re.search(r"source.?(ledger|caveats)", genius, re.I)) and _HB_LABEL_RE.search(genius)
    checks.append({
        "check": "source_ledger",
        "passed": bool(ledger_files) or bool(genius_ledger),
        "detail": (f"found: {', '.join(ledger_files[:3])}" if ledger_files
                   else ("genius.md carries a labeled source section" if genius_ledger
                         else "no references/*ledger*|*source* file, no VERIFIED/LIKELY/UNCONFIRMED "
                              "labels anywhere — unauditable for hallucinated authority")),
    })

    # 5. Named-entity floor per genius pattern (skill_census calibration).
    sections, zero_ratio = _sections_zero_entity(genius)
    checks.append({
        "check": "named_entity_floor",
        "passed": sections > 0 and zero_ratio <= HEARTBEAT_ZERO_ENTITY_MAX,
        "detail": f"{sections} pattern section(s), zero-entity ratio {zero_ratio:.2f} "
                  f"(max {HEARTBEAT_ZERO_ENTITY_MAX}; every pattern needs ≥1 proper noun/number/quote)",
    })

    # 6. Output Schema + Quality Gate present per workflow file.
    wf_files = sorted(workflows_dir.glob("*.md")) if workflows_dir.is_dir() else []
    missing_contract = []
    for wf in wf_files:
        text = _read_text(wf)
        gaps = []
        if not _HB_OUTPUT_SCHEMA_RE.search(text):
            gaps.append("Output Schema")
        if not _HB_QUALITY_GATE_RE.search(text):
            gaps.append("Quality Gate")
        if gaps:
            missing_contract.append(f"{wf.name} (missing {'+'.join(gaps)})")
    checks.append({
        "check": "workflow_contracts",
        "passed": bool(wf_files) and not missing_contract,
        "detail": (f"all {len(wf_files)} workflow file(s) carry Output Schema + Quality Gate"
                   if wf_files and not missing_contract
                   else (f"{len(missing_contract)}/{len(wf_files)} workflow file(s) missing contracts: "
                         + "; ".join(missing_contract[:5]) if wf_files
                         else "zero workflow files")),
    })

    # 7. Menu parity — every workflow reachable from the slash menu, or carries
    #    a NAMED exemption. Root-caused 2026-07-25 (riley-brown forge): 12 built
    #    workflows were fireable-but-not-in-menu because wrapper minting was a
    #    manual step. "Reachable" = same-stem command exists in .claude/commands/
    #    OR some wrapper/shim references skills/<skill>/workflows/<file>.
    #    Exempt = frontmatter carries `menu_exempt:` / `status: superseded` /
    #    `superseded_by:`, or the filename marks a variant/backup artifact.
    live_wfs = [w for w in wf_files
                if not _MENU_VARIANT_RE.search(w.name)]
    unreachable, exempt_count = [], 0
    if live_wfs:
        cmd_stems, wrapper_blob = _menu_surfaces()
        for wf in live_wfs:
            head = _read_text(wf)[:600]
            if _MENU_EXEMPT_RE.search(head):
                exempt_count += 1
                continue
            ref = f"skills/{skill_dir.name}/workflows/{wf.name}"
            if wf.stem in cmd_stems or ref in wrapper_blob:
                continue
            unreachable.append(wf.name)
    checks.append({
        "check": "menu_parity",
        "passed": bool(live_wfs) and not unreachable,
        "detail": (f"all {len(live_wfs)} live workflow(s) menu-reachable"
                   + (f" ({exempt_count} named-exempt)" if exempt_count else "")
                   if live_wfs and not unreachable
                   else (f"{len(unreachable)}/{len(live_wfs)} workflow(s) built but NOT fireable "
                         f"from the menu (no .agent/workflows wrapper, no .claude/commands shim, "
                         f"no `menu_exempt:` frontmatter): " + "; ".join(unreachable[:6])
                         if live_wfs else "zero workflow files")),
    })

    return checks


def heartbeat_failures(checks: List[Dict[str, Any]]) -> List[str]:
    return [c["check"] for c in checks if not c["passed"]]


def log_advisory_run(context: str) -> None:
    """Every --advisory run is logged — the escape hatch exists (compass-not-
    cage) but never silently."""
    try:
        ADVISORY_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(ADVISORY_LOG, "a") as f:
            f.write(json.dumps({
                "ts": datetime.now().isoformat(),
                "event": "heartbeat_advisory_run",
                "context": context,
            }) + "\n")
    except Exception:
        pass


# ─────────────────────────────────────────────────────────
# Trace-based recency / quality signal
# ─────────────────────────────────────────────────────────

# Build-time workflows whose traces certify the BUILD of a skill, not its
# production USE. Counting them let extract-forge self-certify new skills as
# "used" on ship day (root cause of Sean Macintyre's manufactured A-tier —
# see _active/harness/system-audit/02-research/sean-macintyre-audit-2026-06-09.md).
BUILD_WORKFLOWS = {"extract-forge", "extract"}


def load_skill_trace_signal(window_days: int = TIER_TRACE_WINDOW_DAYS) -> Dict[str, Dict[str, Any]]:
    """Aggregate v2 trace scores per skill/component within window.

    Traces produced by BUILD_WORKFLOWS are excluded: they score the extraction
    itself, not a production deployment of the skill.
    """
    if not TRACES_DIR.exists():
        return {}
    cutoff = datetime.now() - timedelta(days=window_days)
    bucket: Dict[str, List[float]] = defaultdict(list)
    for tf in TRACES_DIR.glob("trace_*.json"):
        try:
            mtime = datetime.fromtimestamp(tf.stat().st_mtime)
            if mtime < cutoff:
                continue
            with open(tf) as f:
                d = json.load(f)
            if (d.get("workflow") or "") in BUILD_WORKFLOWS:
                continue
            skill = d.get("component") or d.get("skill") or ""
            if not skill:
                continue
            comp = (d.get("quality") or {}).get("composite")
            if comp is None:
                continue
            bucket[skill].append(float(comp))
        except Exception:
            continue

    out = {}
    for skill, scores in bucket.items():
        out[skill] = {
            "trace_count": len(scores),
            "trace_avg": round(sum(scores) / len(scores), 2),
            "trace_min": min(scores),
            "trace_max": max(scores),
        }
    return out


# ─────────────────────────────────────────────────────────
# Cross-reference scan
# ─────────────────────────────────────────────────────────

def load_cross_references() -> Set[str]:
    """Skill names referenced from CLAUDE.md, COUNCIL.md, or expert_router.py.

    Detection layers, in order of specificity:
      1. Exact directory-name match (strongest)
      2. First-two-parts prefix match (e.g., "lara-acosta")
      3. First-part-only match (e.g., "kallaway", "dr-k") — requires length ≥3
         AND the source text must contain at least 2 occurrences (avoids
         false-positives on common short tokens).
    """
    refs: Set[str] = set()
    sources = []
    for source in [CLAUDE_MD, COUNCIL_MD, EXPERT_ROUTER]:
        if source.exists():
            try:
                sources.append(source.read_text(errors="ignore"))
            except Exception:
                pass
    combined = "\n".join(sources)

    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        name = skill_dir.name
        if name in combined:
            refs.add(name)
            continue
        parts = name.split("-")
        if len(parts) >= 2:
            two_part = "-".join(parts[:2])
            if len(two_part) >= 6 and two_part in combined:
                refs.add(name)
                continue
        # First-part only — needs length ≥3 AND ≥2 occurrences
        first = parts[0] if parts else ""
        if len(first) >= 3 and combined.count(first) >= 2:
            refs.add(name)
    return refs


# ─────────────────────────────────────────────────────────
# Tier classification
# ─────────────────────────────────────────────────────────

def classify_tier(fp: Dict[str, Any], trace: Optional[Dict[str, Any]],
                  cross_referenced: bool) -> Dict[str, Any]:
    """Return (tier, confidence, reasoning) for a skill."""
    reasons = []

    # UTILITY tier — Anthropic/system utilities. Bypass expert quality grading.
    if fp["name"] in UTILITY_SKILLS:
        return {
            "tier": "UTILITY",
            "confidence": "high",
            "reasoning": ["system/Anthropic utility skill — not graded against expert rubric"],
        }

    # Structural completeness
    full_structure = (
        fp["has_skill_md"]
        and fp["has_genius"]
        and fp["workflow_count"] >= 3
    )
    partial_structure = (
        fp["has_skill_md"]
        and (fp["has_genius"] or fp["workflow_count"] >= 3)
    )
    minimal_structure = fp["has_skill_md"] and not fp["has_genius"] and fp["workflow_count"] < 2

    # Trace signal
    has_traces = trace is not None and trace["trace_count"] > 0
    high_trace = has_traces and trace["trace_avg"] >= TIER_A_MIN_TRACE_SCORE
    low_trace = has_traces and trace["trace_avg"] < 6.0

    # Decision (tightened 2026-04-25 — A tier requires BOTH trace evidence
    # AND structure; cross-references alone are too generous because
    # expert_router.py mentions ~96 experts as routing entries, which is not
    # the same as load-bearing usage)
    if full_structure and high_trace:
        tier = "A"
        reasons.append(f"full structure ({fp['workflow_count']} workflows + genius.md)")
        reasons.append(f"trace avg {trace['trace_avg']} ≥ {TIER_A_MIN_TRACE_SCORE} ({trace['trace_count']} traces)")
        if cross_referenced:
            reasons.append("cross-referenced from CLAUDE/COUNCIL/router")
    elif full_structure and cross_referenced and not has_traces:
        # Full structure + cross-ref but never invoked = strong B (eligible to promote)
        tier = "B"
        reasons.append(f"full structure ({fp['workflow_count']} workflows + genius.md)")
        reasons.append("cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace")
    elif partial_structure and (has_traces or cross_referenced):
        tier = "B"
        if fp["has_genius"] and fp["workflow_count"] < 3:
            reasons.append("has genius.md but <3 workflows")
        elif fp["workflow_count"] >= 3 and not fp["has_genius"]:
            reasons.append(f"{fp['workflow_count']} workflows but no genius.md")
        if has_traces:
            reasons.append(f"{trace['trace_count']} traces, avg {trace['trace_avg']}")
        if cross_referenced and not has_traces:
            reasons.append("cross-referenced (no trace data)")
    elif full_structure and not has_traces and not cross_referenced:
        tier = "REVIEW"
        reasons.append("full structure but never used (no traces, no cross-references)")
    elif not fp["has_skill_md"]:
        # Truly missing structure — no SKILL.md = orphan/backup folder
        tier = "C"
        reasons.append("MISSING SKILL.md — likely orphan or backup folder")
    elif minimal_structure and not has_traces and not cross_referenced:
        # SKILL.md only, no genius, <2 workflows, no usage signal
        tier = "C"
        reasons.append("minimal structure (SKILL.md only) AND no traces AND no cross-references")
    elif partial_structure and not has_traces and not cross_referenced:
        # Has SKILL.md + (genius OR ≥3 workflows) but never invoked — judgment call
        tier = "REVIEW"
        reasons.append("partial structure (intentional but unused) — review priority")
    elif minimal_structure and (has_traces or cross_referenced):
        # SKILL.md only but has SOME usage signal — needs attention, not archive
        tier = "REVIEW"
        reasons.append("minimal structure but used — enrich with genius.md/workflows")
    elif low_trace:
        tier = "REVIEW"
        reasons.append(f"low trace scores (avg {trace['trace_avg']}) — degrading?")
    else:
        tier = "REVIEW"
        reasons.append("heuristic conflict — needs human judgment")

    # Confidence: high if multiple converging signals, low if conflict
    confidence = "high" if len(reasons) >= 2 else "medium"
    return {"tier": tier, "confidence": confidence, "reasoning": reasons}


# ─────────────────────────────────────────────────────────
# Audit driver
# ─────────────────────────────────────────────────────────

def run_audit(advisory: bool = False) -> Dict[str, Any]:
    if not SKILLS_DIR.exists():
        return {"error": "skills_dir_missing"}

    trace_signal = load_skill_trace_signal()
    cross_refs = load_cross_references()

    records: List[Dict[str, Any]] = []
    skill_dirs = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()])
    for skill_dir in skill_dirs:
        fp = fingerprint_skill(skill_dir)
        trace = trace_signal.get(skill_dir.name)
        cross_ref = skill_dir.name in cross_refs
        classification = classify_tier(fp, trace, cross_ref)
        craft_flags = craft_standard_flags(skill_dir, fp)
        rec = {**fp, "trace": trace, "cross_referenced": cross_ref, **classification, "craft_flags": craft_flags}

        # Heartbeat checks — tier-affecting (Wave 2 promotion, 2026-07-09).
        # Failing ≥2 caps the tier at B. UTILITY skills exempt. --advisory
        # keeps the report but skips the cap (logged by main()).
        if rec["tier"] != "UTILITY":
            hb = heartbeat_checks(skill_dir, fp)
            failures = heartbeat_failures(hb)
            rec["heartbeat"] = hb
            rec["heartbeat_failures"] = failures
            if (not advisory
                    and len(failures) >= HEARTBEAT_FAIL_CAP_THRESHOLD
                    and rec["tier"] == "A"):
                rec["tier"] = HEARTBEAT_CAP_TIER
                rec["heartbeat_capped"] = True
                rec["reasoning"].append(
                    f"HEARTBEAT CAP: failed {len(failures)}/7 tier-affecting checks "
                    f"({', '.join(failures)}) — capped at {HEARTBEAT_CAP_TIER} per "
                    "directives/skill-craft-standard.md")
        records.append(rec)

    # Summary
    tier_counts = defaultdict(int)
    for r in records:
        tier_counts[r["tier"]] += 1

    return {
        "total_skills": len(records),
        "tier_counts": dict(tier_counts),
        "records": records,
    }


def write_audit_report(audit: Dict[str, Any]) -> Path:
    today = date.today().isoformat()
    AUDIT_OUT_DIR.mkdir(parents=True, exist_ok=True)
    md_path = AUDIT_OUT_DIR / f"skill_audit_{today}.md"
    jsonl_path = AUDIT_OUT_DIR / f"skill_audit_{today}.jsonl"

    # JSONL
    with open(jsonl_path, "w") as f:
        for r in audit["records"]:
            f.write(json.dumps(r) + "\n")

    # Markdown report
    lines = [
        f"# Skill Audit — {today}",
        "",
        f"**Total skills**: {audit['total_skills']}",
        f"**Tier distribution**: " + ", ".join(f"{t}={n}" for t, n in sorted(audit['tier_counts'].items())),
        "",
        "## Methodology",
        "",
        "Tiers assigned by `execution/skill_auditor.py` using:",
        "- **Structure**: SKILL.md + genius.md + workflow count + references/",
        f"- **Trace signal**: v2_traces avg score over {TIER_TRACE_WINDOW_DAYS}d (≥{TIER_A_MIN_TRACE_SCORE} = strong)",
        "- **Cross-references**: CLAUDE.md, COUNCIL.md, expert_router.py mentions",
        "",
        "Tiers:",
        "- **A** — full structure + (high traces OR cross-referenced) → world-class with real expert thinking",
        "- **B** — partial structure + (some traces OR cross-referenced) → solid framework",
        "- **C** — minimal structure AND no traces AND no cross-references → archive candidate",
        "- **REVIEW** — heuristic conflict, low trace scores, or unused full-structure skills → human judgment",
        "",
    ]

    # Heartbeat checks — TIER-AFFECTING (Wave 2 promotion, 2026-07-09)
    hb_failing = [r for r in audit["records"]
                  if len(r.get("heartbeat_failures") or []) >= HEARTBEAT_FAIL_CAP_THRESHOLD]
    if hb_failing:
        capped = [r for r in hb_failing if r.get("heartbeat_capped")]
        lines += [
            "## Heartbeat Checks (`directives/skill-craft-standard.md` — TIER-AFFECTING)",
            "",
            f"6 checks: anti-patterns ≥5 sourced · ≥3 verbatim exemplars · recognition test · "
            f"source ledger · named-entity floor · workflow Output Schema+Quality Gate. "
            f"Failing ≥{HEARTBEAT_FAIL_CAP_THRESHOLD} caps the tier at {HEARTBEAT_CAP_TIER}.",
            "",
            f"{len(hb_failing)} skill(s) fail ≥{HEARTBEAT_FAIL_CAP_THRESHOLD} checks "
            f"({len(capped)} tier-capped this run):",
            "",
        ]
        lines += [f"- `{r['name']}`: {', '.join(r['heartbeat_failures'])}"
                  f"{' **[capped A→' + HEARTBEAT_CAP_TIER + ']**' if r.get('heartbeat_capped') else ''}"
                  for r in sorted(hb_failing, key=lambda x: x["name"])]
        lines.append("")

    # Craft standard flags — advisory only, per directives/skill-craft-standard.md
    flagged = [r for r in audit["records"] if r.get("craft_flags")]
    if flagged:
        lines += [
            "## Craft Standard Flags (`directives/skill-craft-standard.md` — advisory, not tier-affecting)",
            "",
            f"{len(flagged)} skills have at least one cheap deterministic gap:",
            "",
        ]
        lines += [f"- `{r['name']}`: {', '.join(r['craft_flags'])}" for r in sorted(flagged, key=lambda x: x["name"])]
        lines.append("")

    # CORE DRIFT — Production Core entries with no production traces in window.
    # This is the correction mechanism for the (provisional) core roster:
    # a core skill that stays trace-less should be demoted; a long-tail skill
    # earning traces should be promoted. Reviewed monthly via /weekly-closeout.
    core = load_production_core()
    if core:
        traced = {r["name"] for r in audit["records"] if (r.get("trace_count") or 0) > 0}
        drifting = sorted(c for c in core if c in {r["name"] for r in audit["records"]}
                          and c not in traced)
        lines += [
            "## CORE DRIFT (Production Core entries with zero traces in window)",
            "",
            f"{len(drifting)} of {len(core)} core entries have no production traces "
            f"in the last {TIER_TRACE_WINDOW_DAYS}d:",
            "",
        ]
        lines += [f"- {c}" for c in drifting] or ["- (none — core is fully active)"]
        lines += ["", "Action: if an entry stays here 2 consecutive months, demote it "
                      "from PRODUCTION_CORE.md; promote any long-tail skill with 3+ traces.", ""]

    # CONTEXT SIZE RATCHET (loop-repair #11, 2026-07-24, map-not-encyclopedia):
    # always-on context files may shrink freely but never grow silently.
    # Read-only measurement + a prune prompt; a human decides. Frontier-lab
    # doctrine: bloated rules files make the model ignore instructions.
    try:
        import json as _json
        ratchet_state = ROOT / ".agent" / "context-ratchet.json"
        watched = {
            "CLAUDE.md": ROOT / "CLAUDE.md",
            "MEMORY.md": Path.home() / ".claude" / "projects" /
                         "-Users-farricecain-Google-Antigravity" / "memory" / "MEMORY.md",
        }
        prev = _json.loads(ratchet_state.read_text()) if ratchet_state.exists() else {}
        now_sizes = {k: (p.stat().st_size if p.exists() else 0) for k, p in watched.items()}
        lines += ["## CONTEXT SIZE RATCHET (always-on files — shrink free, grow flagged)", ""]
        for k, size in now_sizes.items():
            prev_size = prev.get(k)
            if prev_size is None:
                lines.append(f"- {k}: {size:,}B (baseline recorded)")
            elif size > prev_size:
                lines.append(f"- ⚠️ {k} GREW {prev_size:,}B → {size:,}B (+{size - prev_size:,}B). "
                             "Prune test per addition: would removing it cause mistakes? "
                             "No → it goes to an on-demand file.")
            else:
                lines.append(f"- {k}: {size:,}B (≤ last scan — ratchet holds)")
        ratchet_state.write_text(_json.dumps(now_sizes, indent=1))
        lines.append("")
    except Exception:
        pass

    # Per-tier breakdown
    for tier in ["A", "B", "REVIEW", "C", "UTILITY"]:
        bucket = [r for r in audit["records"] if r["tier"] == tier]
        if not bucket:
            continue
        lines.append(f"## Tier {tier} ({len(bucket)} skills)")
        lines.append("")
        if tier == "A":
            lines.append("These are the system's strongest skills. Prioritize for promotion, ground-truth benchmarking, and revenue tracking.")
        elif tier == "B":
            lines.append("Solid skills that are working. Candidates for B→A promotion via genius.md enrichment or workflow expansion.")
        elif tier == "REVIEW":
            lines.append("Heuristics conflict — these need human eyes before tier finalization.")
        elif tier == "C":
            lines.append("Archive candidates. Low evidence of value. **Do not delete — move to `_archive/skills/` for provenance.** Review individually before archiving (some may be load-bearing user domain skills).")
        elif tier == "UTILITY":
            lines.append("Anthropic-provided or system utility skills. Provide infrastructure (file conversion, design scaffolding, code utilities) rather than expert thinking. **Do not archive** — these are kept for usage. Update `UTILITY_SKILLS` in `skill_auditor.py` to add new entries.")
        lines.append("")
        lines.append("| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |")
        lines.append("|---|---|---|---|---|---|")
        for r in sorted(bucket, key=lambda x: x["name"]):
            t = r.get("trace") or {}
            trace_str = f"{t.get('trace_count', 0)} (avg {t.get('trace_avg', '-')})" if t else "-"
            cross_str = "✓" if r["cross_referenced"] else ""
            reason = "; ".join(r["reasoning"][:3])
            lines.append(
                f"| `{r['name']}` | {r['workflow_count']} | {'✓' if r['has_genius'] else ''} | {trace_str} | {cross_str} | {reason} |"
            )
        lines.append("")

    lines.append("## Next steps")
    lines.append("")
    lines.append("1. **Review the REVIEW bucket manually** — these are the highest-information items.")
    lines.append("2. **Spot-check 3-5 A-tier classifications** — confirm the heuristics aren't generous.")
    lines.append("3. **Spot-check 3-5 C-tier classifications** — confirm nothing valuable is being archived.")
    lines.append("4. Run `python3 execution/skill_auditor.py archive --tier C --apply` to move C-tier (with confirmation prompt).")
    lines.append("5. Run `python3 execution/skill_auditor.py update-index --apply` to annotate SKILL_INDEX.md.")
    lines.append("")
    lines.append(f"Machine-readable records: `{jsonl_path.relative_to(ROOT)}`")

    md_path.write_text("\n".join(lines) + "\n")
    return md_path


# ─────────────────────────────────────────────────────────
# Duplication audit (skills × agents)
# ─────────────────────────────────────────────────────────

def run_duplication_audit() -> Dict[str, Any]:
    skill_names = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    agent_names = {p.name for p in AGENTS_DIR.iterdir() if p.is_dir()} if AGENTS_DIR.exists() else set()

    # Direct overlap
    direct_overlap = skill_names & agent_names

    # Expert-prefix overlap (e.g., skill "lara-acosta-ghostwriting" + agent "lara-acosta")
    skill_prefixes = defaultdict(list)
    for s in skill_names:
        parts = s.split("-")
        if len(parts) >= 2:
            prefix = "-".join(parts[:2])
            skill_prefixes[prefix].append(s)

    expert_overlap = []
    for agent in agent_names:
        if agent in skill_prefixes:
            expert_overlap.append({"agent": agent, "skills": skill_prefixes[agent]})

    return {
        "skill_count": len(skill_names),
        "agent_count": len(agent_names),
        "direct_overlap_count": len(direct_overlap),
        "direct_overlap": sorted(direct_overlap),
        "expert_prefix_overlap_count": len(expert_overlap),
        "expert_prefix_overlap_sample": expert_overlap[:20],
    }


# ─────────────────────────────────────────────────────────
# SKILL_INDEX.md annotation
# ─────────────────────────────────────────────────────────

def update_skill_index(records: List[Dict[str, Any]], apply: bool) -> Dict[str, Any]:
    """Append a tier-annotated section to SKILL_INDEX.md (or print preview)."""
    today = date.today().isoformat()
    by_tier = defaultdict(list)
    for r in records:
        by_tier[r["tier"]].append(r["name"])

    section = [
        "",
        f"## Tier Annotations (auto-generated {today})",
        "",
        f"From `execution/skill_auditor.py audit`. Total: {len(records)} skills.",
        "",
    ]
    for tier in ["A", "B", "REVIEW", "C", "UTILITY"]:
        names = sorted(by_tier.get(tier, []))
        section.append(f"### Tier {tier} ({len(names)})")
        section.append("")
        for n in names:
            section.append(f"- `{n}`")
        section.append("")

    if not apply:
        return {"preview": "\n".join(section[:30]) + "\n...", "would_write_lines": len(section)}

    # Append to SKILL_INDEX.md (don't replace — preserve auto-generated section above)
    if SKILL_INDEX.exists():
        existing = SKILL_INDEX.read_text()
        # Strip any prior auto-generated section
        marker = "## Tier Annotations (auto-generated"
        if marker in existing:
            existing = existing.split(marker)[0].rstrip() + "\n"
        SKILL_INDEX.write_text(existing + "\n".join(section))
    else:
        SKILL_INDEX.write_text("# Skill Registry Directory\n" + "\n".join(section))
    return {"applied": True, "path": str(SKILL_INDEX)}


# ─────────────────────────────────────────────────────────
# Archive C-tier
# ─────────────────────────────────────────────────────────

def load_production_core() -> set:
    """Production Core entries are protected from archiving (PRODUCTION_CORE.md)."""
    try:
        d = json.loads((ROOT / ".agent" / "production-core.json").read_text())
        return {e["id"] for k in ("skills", "workflows") for e in d.get(k, [])}
    except Exception:
        return set()


def _annotate_archived(skill_name: str) -> bool:
    """De-index a skill in place: add `status: archived` to SKILL.md frontmatter.

    Preferred over shutil.move — the skill stays on disk (zero token cost, zero
    wiki link breakage); find_skill.py and sync_registries.py skip archived
    status, which removes it from all runtime routing surfaces.
    """
    p = SKILLS_DIR / skill_name / "SKILL.md"
    if not p.exists():
        return False
    text = p.read_text(errors="ignore")
    if not text.startswith("---") or "status: archived" in text.split("---", 2)[1]:
        return False
    parts = text.split("---", 2)
    parts[1] = parts[1].rstrip("\n") + "\nstatus: archived\n"
    p.write_text("---" + parts[1] + "---" + parts[2])
    return True


def archive_tier(records: List[Dict[str, Any]], tier: str, apply: bool,
                 names: Optional[List[str]] = None, annotate: bool = False) -> Dict[str, Any]:
    core = load_production_core()
    targets = [r for r in records if r["tier"] == tier]
    if names:
        wanted = set(names)
        targets = [r for r in targets if r["name"] in wanted]
    protected = [r["name"] for r in targets if r["name"] in core]
    targets = [r for r in targets if r["name"] not in core]

    if not apply:
        return {
            "would_archive_count": len(targets),
            "mode": "annotate (de-index in place)" if annotate else "move",
            "destination": "frontmatter status: archived" if annotate else str(ARCHIVE_DIR),
            "core_protected_skipped": protected,
            "sample": [r["name"] for r in targets[:10]],
            "note": "Re-run with --apply to execute.",
        }

    moved = []
    errors = []
    if annotate:
        for r in targets:
            try:
                if _annotate_archived(r["name"]):
                    moved.append(r["name"])
            except Exception as e:
                errors.append({"skill": r["name"], "error": str(e)})
    else:
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        for r in targets:
            src = SKILLS_DIR / r["name"]
            dst = ARCHIVE_DIR / r["name"]
            if not src.exists():
                continue
            try:
                shutil.move(str(src), str(dst))
                moved.append(r["name"])
            except Exception as e:
                errors.append({"skill": r["name"], "error": str(e)})
    return {"applied": True, "mode": "annotate" if annotate else "move",
            "archived_count": len(moved), "archived": moved,
            "core_protected_skipped": protected, "errors": errors}


# ─────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Skill Auditor — tier-grade skill directories")
    sub = parser.add_subparsers(dest="command")

    aud = sub.add_parser("audit", help="Run audit and write report")
    aud.add_argument("--advisory", action="store_true",
                     help="Heartbeat checks report but do NOT cap tiers (old behavior; logged)")
    sub.add_parser("duplication", help="Cross-reference skills × agents")

    chk = sub.add_parser("check", help="Run the 7 tier-affecting heartbeat checks on ONE skill "
                                       "(gate mode for extract/extract-forge QC; exit 1 on ≥2 failures)")
    chk.add_argument("--skill", required=True, help="Skill directory name under skills/")
    chk.add_argument("--advisory", action="store_true",
                     help="Report failures without gating (exit 0; logged)")

    upd = sub.add_parser("update-index", help="Annotate SKILL_INDEX.md with tier classifications")
    upd.add_argument("--apply", action="store_true", help="Actually write (default: preview)")

    arc = sub.add_parser("archive", help="Archive skills of a given tier (annotate-in-place or move)")
    arc.add_argument("--tier", required=True, choices=["A", "B", "C", "REVIEW", "UTILITY"])
    arc.add_argument("--apply", action="store_true", help="Actually execute (default: preview)")
    arc.add_argument("--names", default="", help="Comma-separated skill names to limit to (within tier)")
    arc.add_argument("--annotate", action="store_true",
                     help="De-index in place via 'status: archived' frontmatter (preferred; zero link breakage)")

    args = parser.parse_args()

    if args.command == "audit":
        if args.advisory:
            log_advisory_run("audit --advisory (tier caps suppressed)")
        audit = run_audit(advisory=args.advisory)
        path = write_audit_report(audit)
        print(json.dumps({
            "total_skills": audit["total_skills"],
            "tier_counts": audit["tier_counts"],
            "advisory": args.advisory,
            "report": str(path),
        }, indent=2))

    elif args.command == "check":
        skill_dir = SKILLS_DIR / args.skill
        if not skill_dir.is_dir():
            print(f"ERROR: skills/{args.skill} not found")
            sys.exit(1)
        fp = fingerprint_skill(skill_dir)
        if fp["name"] in UTILITY_SKILLS:
            print(f"{args.skill}: UTILITY skill — exempt from heartbeat grading")
            sys.exit(0)
        checks = heartbeat_checks(skill_dir, fp)
        failures = heartbeat_failures(checks)
        print(f"Heartbeat check — skills/{args.skill} "
              f"(directives/skill-craft-standard.md, tier-affecting)")
        for c in checks:
            print(f"  [{'PASS' if c['passed'] else 'FAIL'}] {c['check']}: {c['detail']}")
        print(f"  → {len(failures)}/7 failing"
              + (f" ({', '.join(failures)})" if failures else ""))
        if len(failures) >= HEARTBEAT_FAIL_CAP_THRESHOLD:
            if args.advisory:
                log_advisory_run(f"check --skill {args.skill} --advisory "
                                 f"({len(failures)} failures, gate suppressed)")
                print(f"  ADVISORY MODE — would cap tier at {HEARTBEAT_CAP_TIER} "
                      f"(≥{HEARTBEAT_FAIL_CAP_THRESHOLD} failures); logged to "
                      f"{ADVISORY_LOG.relative_to(ROOT)}. Exit 0.")
                sys.exit(0)
            print(f"  GATE: tier capped at {HEARTBEAT_CAP_TIER} — fix the failing checks "
                  "or ship with the gap named (embodiment-standard.md FAIL path). Exit 1.")
            sys.exit(1)
        print("  GATE: clear.")
        sys.exit(0)

    elif args.command == "duplication":
        print(json.dumps(run_duplication_audit(), indent=2))

    elif args.command == "update-index":
        audit = run_audit()
        result = update_skill_index(audit["records"], apply=args.apply)
        print(json.dumps(result, indent=2))

    elif args.command == "archive":
        audit = run_audit()
        names = [n.strip() for n in args.names.split(",") if n.strip()] or None
        result = archive_tier(audit["records"], tier=args.tier, apply=args.apply,
                              names=names, annotate=args.annotate)
        print(json.dumps(result, indent=2))

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
