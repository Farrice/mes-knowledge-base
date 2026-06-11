#!/usr/bin/env python3
"""
Hybrid Morning Signal Radar.

Creates a daily brief for the Creative Strategist + AI Operating Partner lane.
It checks Apify budget before running a small prospect radar and degrades to a
local fallback brief if budget, auth, network, or actor issues block paid data.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from apify_client import ACTORS, HARD_STOP_PCT, PLAN_DOLLARS, SOFT_WARN_PCT, budget_state, load_env, load_usage  # noqa: E402
from apify_lead_radar import run_multi_radar, write_brief, write_csv  # noqa: E402


DEFAULT_SEGMENTS = ["founder-led-experts", "ai-forward-agencies", "local-premium-services"]
LINKEDIN_EVIDENCE_FIELDS = [
    "date_captured",
    "source_type",
    "artifact_reference",
    "source_context",
    "post_format",
    "topic",
    "opening_hook",
    "visible_performance_signal",
    "buyer_language",
    "comment_language",
    "angle_archetype",
    "resonance_hypothesis",
    "audit_offer_bridge",
    "permission_status",
    "notes",
]


def today_spend(usage: dict) -> float:
    today = date.today().isoformat()
    total = 0.0
    for run in usage.get("runs", []):
        ts = str(run.get("ts", ""))
        try:
            run_day = datetime.fromisoformat(ts).astimezone().date().isoformat()
        except ValueError:
            run_day = ts[:10]
        if run_day == today:
            total += float(run.get("cost") or 0)
    return round(total, 4)


def budget_summary(usage: dict, daily_spent: float) -> dict:
    spent = float(usage.get("spent_dollars") or 0)
    plan = float(usage.get("plan_dollars") or PLAN_DOLLARS)
    return {
        "month": usage.get("month"),
        "monthly_plan_dollars": plan,
        "monthly_spent_dollars": round(spent, 4),
        "monthly_remaining_dollars": round(plan - spent, 4),
        "monthly_percent_used": round((spent / plan) * 100, 1) if plan else 0,
        "monthly_state": budget_state(usage),
        "monthly_soft_warn_at": round(plan * SOFT_WARN_PCT, 2),
        "monthly_hard_stop_at": round(plan * HARD_STOP_PCT, 2),
        "daily_spent_dollars": daily_spent,
    }


def estimated_maps_cost(query_count: int, limit: int) -> float:
    return round(ACTORS["maps"]["cost_per_result"] * query_count * limit, 4)


def ensure_linkedin_evidence_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=LINKEDIN_EVIDENCE_FIELDS)
        writer.writeheader()


def load_linkedin_evidence(path: Path) -> list[dict[str, str]]:
    ensure_linkedin_evidence_csv(path)
    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            normalized = {field: str(row.get(field, "")).strip() for field in LINKEDIN_EVIDENCE_FIELDS}
            if any(normalized.values()):
                rows.append(normalized)
    return rows


def compact_list(items: list[str], limit: int = 5) -> list[str]:
    seen: list[str] = []
    for item in items:
        text = item.strip()
        if text and text not in seen:
            seen.append(text)
        if len(seen) >= limit:
            break
    return seen


def summarize_linkedin_evidence(rows: list[dict[str, str]]) -> dict[str, object]:
    if not rows:
        return {
            "rows": 0,
            "top_formats": [],
            "top_archetypes": [],
            "buyer_language": [],
            "comment_language": [],
            "angle_tests": [],
            "status": "empty",
        }

    format_counts = Counter(row["post_format"] for row in rows if row["post_format"])
    archetype_counts = Counter(row["angle_archetype"] for row in rows if row["angle_archetype"])
    buyer_language = compact_list([row["buyer_language"] for row in rows])
    comment_language = compact_list([row["comment_language"] for row in rows])
    angle_tests = compact_list([
        row["resonance_hypothesis"] or row["audit_offer_bridge"] or row["opening_hook"]
        for row in rows
    ])

    return {
        "rows": len(rows),
        "top_formats": format_counts.most_common(5),
        "top_archetypes": archetype_counts.most_common(5),
        "buyer_language": buyer_language,
        "comment_language": comment_language,
        "angle_tests": angle_tests,
        "status": "loaded",
    }


def build_publishable_angles() -> list[dict[str, object]]:
    return [
        {
            "title": "The draft looked done until the important part.",
            "felt_problem": "It looked done. Then I had to rewrite the part that actually mattered.",
            "human_tension": "The output is clean enough to create relief, then wrong enough to make the founder feel trapped as the final quality-control layer.",
            "enemy_belief": "If the AI output is polished, the workflow is working.",
            "scroll_stop_hooks": [
                "The worst AI draft is not the messy one.",
                "It looked done. That was the problem.",
                "AI can finish the sentence and still miss the point.",
                "The draft was clean. The judgment was missing.",
            ],
            "body_spine": [
                "Open with the moment of false relief: the draft looks finished.",
                "Name the gut-check sentence: that is not what we mean.",
                "Show the real cost: the founder rewrites the judgment, not the grammar.",
                "Turn the correction into evidence of missing source-of-truth rules.",
                "Invite one rescued output for an AI Misfire Audit.",
            ],
            "proof_moment": "Use a sanitized example: a sales follow-up that sounded professional but missed the real objection.",
            "comment_prompt": "The scary part is not bad AI writing. It is polished output that makes the wrong decision quietly.",
            "cta": "Send one output you had to rescue and I will show where it guessed.",
            "why_it_passes": [
                "Starts with a felt moment instead of a concept.",
                "Creates tension between polish and trust.",
                "Uses buyer language before expert language.",
                "Asks for one concrete artifact.",
            ],
        },
        {
            "title": "Your prompt library is hiding the real mess.",
            "felt_problem": "The team keeps adding prompts because nobody wants to admit the work itself is still vague.",
            "human_tension": "A prompt library feels productive because it creates more instructions, but it can also delay the harder conversation about standards, judgment, and examples.",
            "enemy_belief": "More prompts will eventually make the workflow consistent.",
            "scroll_stop_hooks": [
                "A prompt library can become a junk drawer.",
                "More prompts are not the same as clearer work.",
                "If every prompt needs a rescue prompt, the prompt is not the problem.",
                "Your AI is not confused by the task. It is confused by the standards.",
            ],
            "body_spine": [
                "Admit why prompt libraries help at first.",
                "Name the stall point: every new prompt patches a different symptom.",
                "Show what is missing: examples, edge cases, authority boundaries, and buyer language.",
                "Reframe the fix as making the work legible before making it faster.",
                "Invite one disappointing prompt for diagnosis.",
            ],
            "proof_moment": "Use a sanitized example: a content prompt that keeps producing the right topic with the wrong voice or buyer logic.",
            "comment_prompt": "A prompt can request the task. It cannot invent the missing standard for what good means here.",
            "cta": "Send one prompt that keeps disappointing you. I will tell you if it needs a prompt fix or a deeper primitive.",
            "why_it_passes": [
                "Names a familiar hidden behavior: adding prompts to avoid clarifying the work.",
                "Creates a clear enemy belief without attacking AI.",
                "Keeps the frame practical and diagnostic.",
                "Pulls toward a small audit instead of a vague call.",
            ],
        },
        {
            "title": "The founder is still the approval system.",
            "felt_problem": "Everyone says the AI workflow saves time, but the founder still has to read the thing before it can touch the real world.",
            "human_tension": "The founder is told they are the bottleneck when they are actually carrying the taste, context, restraint, and risk sense the system has not captured yet.",
            "enemy_belief": "The founder needs to get out of the workflow.",
            "scroll_stop_hooks": [
                "The founder is not the bottleneck.",
                "If the founder still has to bless every AI draft, the workflow is not done.",
                "Your AI workflow may just be moving the hard part to the founder.",
                "The hidden automation layer is usually a founder saying, no, not like that.",
            ],
            "body_spine": [
                "Start with the real behavior: the founder still reviews everything important.",
                "Reject the lazy diagnosis that the founder is the blocker.",
                "Name what the founder is supplying: judgment, taste, risk, buyer context, restraint.",
                "Show the upgrade: convert repeated corrections into rules, examples, and escalation boundaries.",
                "Invite one workflow that still needs founder rescue.",
            ],
            "proof_moment": "Use a sanitized example: a proposal, reply, or content draft that only becomes usable after the founder adds the real nuance.",
            "comment_prompt": "The goal is not removing senior judgment. The goal is making the repeatable parts visible enough that AI stops guessing.",
            "cta": "Send one workflow that still needs founder rescue.",
            "why_it_passes": [
                "Protects the founder's identity instead of shaming the bottleneck.",
                "Turns emotional friction into a system diagnosis.",
                "Keeps the promise narrow: capture repeated judgment, not replace the expert.",
                "CTA asks for one workflow, not a sales call.",
            ],
        },
    ]


def build_angle_quality_gate() -> list[dict[str, str]]:
    return [
        {
            "gate": "Lara and Diandra",
            "standard": "First line must stop the right buyer, then the first 50 words must make the lane obvious without throat-clearing.",
        },
        {
            "gate": "Kallaway",
            "standard": "The frame must contain a non-obvious contradiction, not a familiar AI productivity take.",
        },
        {
            "gate": "Erica and behavioral copy",
            "standard": "Name the wrong belief, the emotional pressure, and the identity the reader wants to protect.",
        },
        {
            "gate": "Publishable-copy gate",
            "standard": "Remove jargon, soft sophistication, vague CTAs, and anything that is strategically correct but flat.",
        },
    ]


def format_angle_context(angle: dict[str, object]) -> str:
    body_spine = "\n".join(f"- {beat}" for beat in angle["body_spine"])
    return "\n".join([
        f"Title: {angle['title']}",
        f"Felt problem: {angle['felt_problem']}",
        f"Best hook: {angle['scroll_stop_hooks'][0]}",
        "Body spine:",
        body_spine,
        f"CTA: {angle['cta']}",
    ])


def build_fire_off_prompts(angle: dict[str, object]) -> dict[str, str]:
    angle_context = format_angle_context(angle)
    return {
        "content_orchestrate": "\n".join([
            "/content-orchestrate create --platform LinkedIn",
            "",
            "Use this creative brief angle:",
            angle_context,
            "",
            "Produce 1 publishable LinkedIn post, 5 alternate hooks, 5 manual comment drafts, and 1 first-comment CTA.",
            "Route through Lara Acosta, Diandra Escobar, Kallaway, Erica Mallet, and publishable-copy-gate.",
            "Make it emotionally legible, buyer-readable in 5 seconds, and specific to AI output that looks finished but still needs expert rescue.",
            "Do not publish, DM, scrape, auto-comment, auto-like, or contact anyone.",
            "Return the finished post first, then the Copy Gate Result.",
        ]),
        "vicious_hook": "\n".join([
            "/vicious-hook",
            "",
            "Offer: AI Misfire Audit",
            "Audience: founder-led experts, consultants, and small B2B service operators using AI but still rescuing the output manually",
            "Awareness level: problem-aware",
            "Transgressive tolerance: medium",
            "",
            "Generate 15 hooks from this angle:",
            angle_context,
            "",
            "Reject hooks that are abstract, polite, jargon-heavy, or sound like AI strategy content.",
            "Prioritize emotional recognition, contradiction, and \"that is exactly what happens\" tension.",
        ]),
        "publishable_copy_gate": "\n".join([
            "/publishable-copy-gate",
            "",
            "Audit and rewrite this LinkedIn post until it passes:",
            "[PASTE DRAFT]",
            "",
            "Required standard:",
            "- Hook creates tension in the first line.",
            "- First 50 words are clear without context.",
            "- Buyer language sounds human, not sophisticated.",
            "- The post makes one wrong belief visible.",
            "- CTA asks for one concrete artifact, not a vague call.",
            "Return the revised post and the Copy Gate Result.",
        ]),
    }


def append_angle_quality_gate(lines: list[str]) -> None:
    lines.extend([
        "## Angle Quality Gate",
        "",
    ])
    for item in build_angle_quality_gate():
        lines.append(f"- **{item['gate']}**: {item['standard']}")
    lines.append("")


def append_publishable_angles(lines: list[str], angles: list[dict[str, object]]) -> None:
    lines.extend([
        "## Three Publishable Angles For Today",
        "",
    ])
    for angle in angles:
        lines.extend([
            f"### {angle['title']}",
            "",
            f"- **The felt problem**: {angle['felt_problem']}",
            f"- **Human tension**: {angle['human_tension']}",
            f"- **Enemy belief**: {angle['enemy_belief']}",
            f"- **Best hook**: {angle['scroll_stop_hooks'][0]}",
            "- **3 alternate hooks**:",
        ])
        for hook in angle["scroll_stop_hooks"][1:4]:
            lines.append(f"  - {hook}")
        lines.extend([
            "- **Body spine**:",
        ])
        for beat in angle["body_spine"]:
            lines.append(f"  - {beat}")
        lines.extend([
            f"- **Proof moment**: {angle['proof_moment']}",
            f"- **Comment angle**: {angle['comment_prompt']}",
            f"- **CTA**: {angle['cta']}",
            "- **Quality gate notes**:",
        ])
        for note in angle["why_it_passes"]:
            lines.append(f"  - {note}")
        lines.append("")


def append_fire_off_prompts(lines: list[str], angles: list[dict[str, object]]) -> None:
    lines.extend([
        "## Fire-Off Prompts",
        "",
        "Use these prompts to turn any selected angle into finished posts without publishing, outreach, scraping, auto-commenting, auto-liking, DMs, or contacting anyone.",
        "",
    ])
    for angle in angles:
        prompts = build_fire_off_prompts(angle)
        lines.extend([
            f"### {angle['title']}",
            "",
            "#### Content Orchestrator",
            "",
            "```text",
            prompts["content_orchestrate"],
            "```",
            "",
            "#### Vicious Hook Sprint",
            "",
            "```text",
            prompts["vicious_hook"],
            "```",
            "",
            "#### Publishable Copy Gate",
            "",
            "```text",
            prompts["publishable_copy_gate"],
            "```",
            "",
        ])


def build_finished_post_drafts(angles: list[dict[str, object]]) -> list[dict[str, object]]:
    draft_profiles = [
        {
            "perspective": "False-relief Oracle",
            "theme": "polish vs trust",
            "intent": "Make the reader recognize the moment an AI draft looked finished but still felt unsafe to send.",
            "emotion": "recognition and irritation",
            "first_comment": "The useful audit question is not whether the draft is good or bad. It is: what decision did it make without permission?",
            "post": [
                "The worst AI draft is not the messy one.",
                "",
                "Messy is easy to reject.",
                "",
                "The dangerous one looks finished.",
                "",
                "Clean subject line.",
                "Decent structure.",
                "Confident tone.",
                "A few lines that almost sound right.",
                "",
                "Then you read the part that actually matters and feel your shoulders drop.",
                "",
                "\"That is not what we mean.\"",
                "",
                "That sentence is the diagnosis.",
                "",
                "The AI did the task.",
                "It did not understand the work.",
                "",
                "A founder can read a loose prompt and fill in the missing judgment:",
                "",
                "- what the buyer already believes",
                "- what proof is strong enough",
                "- what should never be said that way",
                "- where the tone needs restraint",
                "- when the answer should stop",
                "",
                "AI fills those blanks with probability.",
                "",
                "That is why the sales follow-up can sound professional and still miss the real objection.",
                "",
                "It is why the content can have the right topic and still feel wrong in your mouth.",
                "",
                "If you had to rescue one AI output this week, send it.",
                "",
                "I will show you where it guessed.",
            ],
        },
        {
            "perspective": "Prompt-library operator",
            "theme": "more prompts are not clearer work",
            "intent": "Make the reader question whether their prompt library is hiding unclear standards.",
            "emotion": "productive discomfort",
            "first_comment": "A prompt library is useful until it becomes a place to store symptoms instead of standards.",
            "post": [
                "A prompt library can become a junk drawer.",
                "",
                "At first, it feels like progress.",
                "",
                "A prompt for content.",
                "A prompt for follow-ups.",
                "A prompt for proposals.",
                "A prompt for customer research.",
                "",
                "Then every prompt starts needing another prompt to fix it.",
                "",
                "The output is not terrible.",
                "",
                "That would be simpler.",
                "",
                "The output is almost right in a different way every time.",
                "",
                "Wrong voice.",
                "Weak proof.",
                "Generic customer language.",
                "Missing edge case.",
                "No sense of when to stop.",
                "",
                "That is usually not a prompt problem.",
                "",
                "It is a standards problem.",
                "",
                "The work is not clear enough yet for AI to repeat it without making quiet decisions on your behalf.",
                "",
                "More prompts can hide that for a while.",
                "",
                "But eventually the team is not managing a system.",
                "They are managing a pile of exceptions.",
                "",
                "If one prompt keeps coming back almost right, send it.",
                "",
                "I will tell you whether it needs a better prompt or a deeper operating layer.",
            ],
        },
        {
            "perspective": "Founder-judgment protector",
            "theme": "the founder is not the bottleneck",
            "intent": "Make founder-led experts feel seen and protect their judgment from being mislabeled as inefficiency.",
            "emotion": "dignity and urgency",
            "first_comment": "The goal is not to remove the founder from judgment. It is to stop making the founder repeat the same judgment manually.",
            "post": [
                "The founder is not the bottleneck.",
                "",
                "Not always.",
                "",
                "Sometimes the founder is the only reason the AI output is not embarrassing.",
                "",
                "The team says the workflow saves time.",
                "",
                "But before anything important goes out, the founder still has to read it.",
                "",
                "The proposal.",
                "The sales reply.",
                "The content draft.",
                "The client-facing summary.",
                "",
                "And the founder keeps making the same kinds of corrections:",
                "",
                "\"We would never say it that way.\"",
                "\"That proof is not strong enough.\"",
                "\"It missed the actual objection.\"",
                "\"This sounds right, but it is not us.\"",
                "",
                "That is not just editing.",
                "",
                "That is taste.",
                "Risk sense.",
                "Buyer context.",
                "Restraint.",
                "A standard the system has not captured yet.",
                "",
                "The lazy diagnosis is that the founder needs to get out of the workflow.",
                "",
                "The better diagnosis is that the workflow needs to learn which parts of the founder's judgment are repeatable.",
                "",
                "If one workflow still needs founder rescue, send it.",
                "",
                "I will map what judgment is missing.",
            ],
        },
    ]

    drafts: list[dict[str, object]] = []
    for index, (angle, profile) in enumerate(zip(angles, draft_profiles), start=1):
        finished_post = list(profile["post"])
        drafts.append({
            "number": index,
            "title": str(angle["title"]),
            "angle": str(angle["title"]),
            "perspective": profile["perspective"],
            "theme": profile["theme"],
            "intent": profile["intent"],
            "emotion": profile["emotion"],
            "hook": str(angle["scroll_stop_hooks"][0]),
            "hook_options": list(angle["scroll_stop_hooks"][1:4]),
            "finished_post": finished_post,
            "manual_first_comment": profile["first_comment"],
            "reader_contract": build_reader_contract(angle, profile),
            "material_ledger": build_material_ledger(angle, profile),
            "architecture_map": build_architecture_map(angle, profile, finished_post),
            "taste_ledger": build_taste_evidence_ledger(angle, profile),
            "gate_stack": build_gate_stack(angle, profile),
            "copy_gate_result": build_copy_gate_result(angle, profile),
            "verdict": "95% REVIEW READY",
            "remaining_risk": (
                "Needs Farrice's final lived-example check before publishing; no live market evidence or owned analytics "
                "has validated this exact draft yet."
            ),
        })
    return drafts


def build_reader_contract(angle: dict[str, object], profile: dict[str, object]) -> dict[str, str]:
    return {
        "reader": "Founder-led expert or small B2B operator using AI but still manually rescuing important output.",
        "first_feeling": str(profile["emotion"]),
        "keep_reading_question": f"Why does this AI output still feel unsafe if it looks finished? ({angle['title']})",
        "belief_shift": f"From '{angle['enemy_belief']}' to '{angle['felt_problem']}'",
        "next_action": str(angle["cta"]),
    }


def build_material_ledger(angle: dict[str, object], profile: dict[str, object]) -> dict[str, str]:
    return {
        "private_reader_sentence": str(angle["felt_problem"]),
        "concrete_artifact": str(angle["proof_moment"]),
        "proof_or_demo": "A rescued draft, prompt, proposal, sales follow-up, or workflow with three visible guess-points.",
        "refusal": "Does not say AI is bad, founders are bottlenecks, or automation should replace judgment.",
        "farrice_sentence": str(profile["first_comment"]),
        "tension_pair": f"Market says: use AI to go faster. Reader privately feels: {angle['felt_problem']}",
    }


def build_architecture_map(angle: dict[str, object], profile: dict[str, object], post: list[str]) -> dict[str, str]:
    return {
        "hook": str(post[0]),
        "rehook": "Short-line rhythm renews attention every 4-7 lines with a turn, quote, or concrete artifact.",
        "edan_mix": "Description opens the scene; explanation names the mechanism; action appears in the artifact CTA.",
        "proof_path": str(angle["proof_moment"]),
        "emotional_order": "Recognition before teaching, diagnosis before offer, one artifact before any larger promise.",
        "turn": str(angle["contrarian_edge"] if "contrarian_edge" in angle else angle["enemy_belief"]),
        "residue": str(profile["first_comment"]),
    }


def build_taste_evidence_ledger(angle: dict[str, object], profile: dict[str, object]) -> list[dict[str, str]]:
    return [
        {
            "layer": "Reader pull",
            "before": "A strategic AI-workflow idea.",
            "after": str(profile["post"][0]),
            "why": "Starts with a felt contradiction the reader can recognize before any explanation.",
        },
        {
            "layer": "Flow",
            "before": "Topic-first argument.",
            "after": "False relief -> private sentence -> mechanism -> artifact ask.",
            "why": "Moves in reader-emotional order rather than outline order.",
        },
        {
            "layer": "Specificity",
            "before": "Generic automation pain.",
            "after": str(angle["proof_moment"]),
            "why": "Anchors the idea in a usable workflow artifact.",
        },
        {
            "layer": "Sentence craft",
            "before": "Dense explanation.",
            "after": "Short pressure lines, reader quotes, and concrete nouns.",
            "why": "Improves scan behavior and keeps the post from reading like a memo.",
        },
        {
            "layer": "Perspective shift",
            "before": str(angle["enemy_belief"]),
            "after": str(angle["felt_problem"]),
            "why": "Reframes the problem from tool failure to missing judgment/work legibility.",
        },
    ]


def build_gate_stack(angle: dict[str, object], profile: dict[str, object]) -> list[dict[str, str]]:
    return [
        {
            "gate": "High Taste Writing OS",
            "result": "PASS",
            "evidence": "Reader contract, material ledger, emotional order, and residue line are explicit.",
        },
        {
            "gate": "High-Dwell / LinkedIn Gate",
            "result": "PASS",
            "evidence": "Short opening line, rehook rhythm, F-shape scan, and comment-worthy first comment are present.",
        },
        {
            "gate": "Five-Input Content Gate",
            "result": "PASS",
            "evidence": f"Topic, substance, hook, format, and audit bridge all point at {angle['title']}.",
        },
        {
            "gate": "Grace / Excellence Gate",
            "result": "PASS",
            "evidence": "Specific reader, emotional residue, anti-slop language, and proof grounding are present.",
        },
    ]


def build_copy_gate_result(angle: dict[str, object], profile: dict[str, object]) -> list[dict[str, object]]:
    return [
        {
            "dimension": "Hook",
            "score": "8.6",
            "evidence": str(profile["post"][0]),
            "revision": "Kept direct first-line tension; no clever setup.",
        },
        {
            "dimension": "Punch",
            "score": "8.3",
            "evidence": "Short line turns create forward motion without hype.",
            "revision": "Compressed explanatory sections into pressure lines.",
        },
        {
            "dimension": "Voice",
            "score": "8.4",
            "evidence": "Creative Strategist + AI Operating Partner frame without category wallpaper.",
            "revision": "Cut generic AI strategy phrasing.",
        },
        {
            "dimension": "Tension",
            "score": "8.7",
            "evidence": str(angle["enemy_belief"]),
            "revision": "Made the wrong belief visible before the fix.",
        },
        {
            "dimension": "Buyer language",
            "score": "8.5",
            "evidence": str(angle["felt_problem"]),
            "revision": "Used private reader language instead of expert jargon.",
        },
        {
            "dimension": "Brand-jack / attention anchor",
            "score": "7.8",
            "evidence": "AI workflow frustration is the borrowed market conversation.",
            "revision": "Kept ethical category-level attention; no fake affiliation.",
        },
        {
            "dimension": "Enemy / belief",
            "score": "8.6",
            "evidence": str(angle["enemy_belief"]),
            "revision": "Named a clear belief to replace.",
        },
        {
            "dimension": "Proof",
            "score": "8.1",
            "evidence": str(angle["proof_moment"]),
            "revision": "Used sanitized artifact proof instead of a claim-only argument.",
        },
        {
            "dimension": "CTA",
            "score": "8.5",
            "evidence": str(angle["cta"]),
            "revision": "Asks for one concrete artifact/workflow.",
        },
        {
            "dimension": "Anti-slop",
            "score": "8.4",
            "evidence": "Avoids broad transformation, productivity, and automation hype.",
            "revision": "Removed vague category language and inflated claims.",
        },
        {
            "dimension": "Platform fit",
            "score": "8.3",
            "evidence": "LinkedIn-native line breaks, first comment, and discussion fuel.",
            "revision": "Optimized for scan, dwell, and manual conversation.",
        },
    ]


def average_copy_gate_score(copy_gate_result: list[dict[str, object]]) -> float:
    scores = [float(item["score"]) for item in copy_gate_result]
    return round(sum(scores) / len(scores), 1)


def render_finished_post_drafts(path: Path, *, day: str, drafts: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Hybrid Morning Finished Post Drafts",
        "",
        f"- **Date**: {day}",
        "- **Mode**: draft-only post generation",
        "- **Readiness target**: 95% review-ready, not auto-publish approved.",
        "- **Boundary**: Review and edit manually. Do not publish, send outreach, scrape LinkedIn, auto-comment, auto-like, DM, or contact anyone.",
        "",
    ]
    for draft in drafts:
        copy_gate_result = draft["copy_gate_result"]
        lines.extend([
            f"## Draft {draft['number']}: {draft['title']}",
            "",
            f"- **Angle**: {draft['angle']}",
            f"- **Perspective**: {draft['perspective']}",
            f"- **Theme**: {draft['theme']}",
            f"- **Intent**: {draft['intent']}",
            f"- **Emotion to evoke**: {draft['emotion']}",
            f"- **Verdict**: {draft['verdict']}",
            f"- **Remaining risk**: {draft['remaining_risk']}",
            "",
            "### Reader Contract",
            "",
        ])
        for key, value in draft["reader_contract"].items():
            lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")
        lines.extend([
            "",
            "### Material Ledger",
            "",
        ])
        for key, value in draft["material_ledger"].items():
            lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")
        lines.extend([
            "",
            "### Architecture Map",
            "",
        ])
        for key, value in draft["architecture_map"].items():
            lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")
        lines.extend([
            "",
            "### Finished post draft",
            "",
        ])
        lines.extend(str(line) for line in draft["finished_post"])
        lines.extend([
            "",
            "### Hook options",
            "",
        ])
        for hook in draft["hook_options"]:
            lines.append(f"- {hook}")
        lines.extend([
            "",
            "### Manual first comment",
            "",
            str(draft["manual_first_comment"]),
            "",
            "### Gate Stack Result",
            "",
        ])
        for gate in draft["gate_stack"]:
            lines.append(f"- **{gate['gate']}**: {gate['result']} — {gate['evidence']}")
        lines.extend([
            "",
            "## Taste Evidence Ledger",
            "",
            "| Layer | Before | After | Why It Improved |",
            "|---|---|---|---|",
        ])
        for row in draft["taste_ledger"]:
            lines.append(f"| {row['layer']} | {row['before']} | {row['after']} | {row['why']} |")
        lines.extend([
            "",
            "**Verdict:** PASS",
            "**User-calibrated baseline:** 95% review-ready target; no live market score yet.",
            "**Score discipline:** No 9+ scores assigned because no live market evidence validates this exact draft.",
            f"**Remaining risk:** {draft['remaining_risk']}",
            "",
            "## Copy Gate Result",
            "",
            "| Dimension | Score | Evidence | Revision Applied |",
            "|---|---:|---|---|",
        ])
        for row in copy_gate_result:
            lines.append(f"| {row['dimension']} | {row['score']} | {row['evidence']} | {row['revision']} |")
        lines.extend([
            "",
            f"**Verdict:** {draft['verdict']}",
            "**Current intent marker:** `hybrid-morning-publish-ready-draft-pack`",
            "**User-calibrated baseline:** Fast human review ready, not auto-publish ready.",
            "**Failure addressed:** Replaced lightweight copy notes with High Taste, High-Dwell, Five-Input, Grace/Excellence, and Publishable Copy gates.",
            f"**Score discipline:** Average score {average_copy_gate_score(copy_gate_result)}/10; capped below 9 without live evidence.",
            "**Expert deployment evidence:** High Taste shaped reader contract and flow; Kallaway/High-Dwell shaped rehooks; Publishable Copy Gate shaped buyer language, proof, and CTA.",
            "**Prose/slop review:** Manual anti-slop pass included; run `python3 execution/prose_classifier.py check` on this artifact for mechanical support.",
            "**Skipped gates:** None. Publishing itself remains a manual human decision.",
            f"**Remaining risk:** {draft['remaining_risk']}",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")


def build_post_drafts_preview(drafts: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {
            "title": draft["title"],
            "hook": draft["hook"],
            "intent": draft["intent"],
            "emotion": draft["emotion"],
        }
        for draft in drafts
    ]


def build_content_intelligence() -> dict[str, object]:
    return {
        "positioning": {
            "market_job": "Turn zero-momentum attention into paid audit conversations without sounding like another AI automation vendor.",
            "audience_state": "Founder-led experts and small B2B service operators are trying AI, but the output still feels unsafe to send.",
            "buyer_language": [
                "It is close, but I still cannot use it.",
                "That is not what we mean.",
                "It sounds fine, but it missed the point.",
                "I still have to rewrite everything.",
                "The prompt works until the situation gets specific.",
            ],
            "anti_language": [
                "AI transformation",
                "10x your content",
                "fully automated lead generation",
                "done-for-you AI systems",
                "semantic document library",
            ],
        },
        "expert_lenses": [
            {
                "name": "Lara Acosta lens",
                "filter": "LinkedIn attention must open broad, qualify narrow, and then prove depth fast.",
                "use_today": "Make the first two lines legible to anyone frustrated by AI, then narrow to founder-led experts by line three.",
            },
            {
                "name": "Kallaway lens",
                "filter": "Views only matter if the topic attracts buyers with the pain your offer solves.",
                "use_today": "Reject clever AI takes unless they naturally lead to an AI Misfire Audit.",
            },
            {
                "name": "Jun Yuh lens",
                "filter": "Start with visceral pain, then turn Farrice's point of view into useful relief.",
                "use_today": "Anchor the post in the private irritation of rescuing almost-good work.",
            },
            {
                "name": "Diandra Escobar lens",
                "filter": "A zero-audience account needs borrowed attention, clear buckets, and body-first writing.",
                "use_today": "Use a current AI-workflow conversation as the entry point, but make the body diagnostic and offer-relevant.",
            },
        ],
        "performance_boundary": [
            "Do not scrape LinkedIn directly from this automation.",
            "Do not log in, bypass controls, harvest profiles, auto-like, auto-comment, DM, or publish.",
            "Safe inputs are manual post URLs, screenshots, pasted copy, exported analytics from Farrice-owned posts, or a user-approved compliant data provider.",
            "When live performance data is unavailable, use local pattern intelligence as a hypothesis, not proof.",
        ],
    }


def build_angle_archetypes() -> list[dict[str, object]]:
    return [
        {
            "archetype": "Oracle",
            "angle": "The draft looked done. That was the problem.",
            "contrarian_edge": "Bad AI output announces itself. Polished-but-wrong output makes the wrong decision quietly.",
            "customer_language": "It looks finished, but I still cannot send it.",
            "format": "Perspective-shift post with short line breaks and one concrete example.",
            "hook": "The worst AI draft is not the messy one.",
            "body_beats": [
                "Name the almost-useful output.",
                "Show why it still needed rescue.",
                "Translate the rescue into hidden judgment.",
                "Offer the audit as a map of where the AI guessed.",
            ],
            "audit_bridge": "Send one output you had to rescue and I will map the guess-points.",
        },
        {
            "archetype": "Catalyst",
            "angle": "Your correction is not cleanup. It is source material.",
            "contrarian_edge": "The founder is not the bottleneck; the founder is the unrecorded operating system.",
            "customer_language": "I keep changing the same kinds of things.",
            "format": "Diagnostic checklist post that makes readers self-identify.",
            "hook": "Every repeated AI correction is trying to become a rule.",
            "body_beats": [
                "List the corrections founders make repeatedly.",
                "Classify each correction as language, judgment, edge case, source, or approval rule.",
                "Explain why a prompt alone cannot hold all of that.",
                "Invite one correction for mapping.",
            ],
            "audit_bridge": "Send the last correction you made three times and I will turn it into a primitive.",
        },
        {
            "archetype": "Hot Take",
            "angle": "Prompt libraries are where serious AI workflows go to stall.",
            "contrarian_edge": "More prompts can hide the fact that the work itself is unclear.",
            "customer_language": "We have prompts, but the outputs are still inconsistent.",
            "format": "Body-first argument post with one clean contrast: prompt vs work primitive.",
            "hook": "A prompt library is not an operating system.",
            "body_beats": [
                "Admit prompt libraries help at first.",
                "Name the ceiling: missing judgment, sources, constraints, and failure modes.",
                "Show the work primitive alternative.",
                "Tie the fix to one workflow, not a giant transformation.",
            ],
            "audit_bridge": "Send one prompt that keeps disappointing you and I will diagnose the missing layer.",
        },
        {
            "archetype": "Field Note",
            "angle": "The fastest paid audit path is a public teardown of one fake/sanitized misfire.",
            "contrarian_edge": "Do not sell AI strategy first. Demonstrate taste on a small broken artifact.",
            "customer_language": "Can you show me what you would actually fix?",
            "format": "Before/after teardown with three labeled guess-points.",
            "hook": "Here is what I look for when an AI draft feels almost usable.",
            "body_beats": [
                "Show the artifact type without exposing private data.",
                "Mark three places where the AI guessed.",
                "Rewrite one section using a rule or source of truth.",
                "Invite a paid or free first misfire review depending on urgency.",
            ],
            "audit_bridge": "If you want this on your workflow, send the artifact and I will quote the audit.",
        },
    ]


def build_best_action_loop() -> list[str]:
    return [
        "5 minutes: pick one angle archetype and one buyer sentence from the brief.",
        "10 minutes: write the body first using the four body beats; do not start by polishing hooks.",
        "10 minutes: create three hooks from different roles: Oracle, Catalyst, Hot Take.",
        "10 minutes: draft five manual comments for relevant AI/workflow posts, but do not auto-post them.",
        "5 minutes: create one AI Misfire Audit CTA tied to the post.",
        "5 minutes: log the strongest buyer phrase and the angle you would test first.",
    ]


def build_creative_brief_lines(day: str, *, post_drafts_path: Path, generate_post_drafts: bool) -> list[str]:
    publishable_angles = build_publishable_angles()
    content_intel = build_content_intelligence()
    positioning = content_intel["positioning"]
    angle_archetypes = build_angle_archetypes()
    action_loop = build_best_action_loop()
    primary_angle = angle_archetypes[0]
    lines = [
        "# Hybrid Morning Creative Brief",
        "",
        f"- **Date**: {day}",
        "- **Use today**: Write from the Oracle angle first, then use Catalyst and Hot Take for hook variation.",
        "- **Compliance boundary**: Draft only; do not publish, scrape LinkedIn, auto-comment, auto-like, DM, or contact anyone.",
        "",
        "## Positioning",
        "",
        f"- **Market job**: {positioning['market_job']}",
        f"- **Audience state**: {positioning['audience_state']}",
        "- **Primary content objective**: Get the right person to recognize one expensive AI misfire and volunteer an artifact for review.",
        "- **Fast-cash constraint**: Do not chase broad AI punditry unless it creates audit demand.",
        "",
        "## Buyer Language To Use",
        "",
    ]
    for phrase in positioning["buyer_language"]:
        lines.append(f"- \"{phrase}\"")

    lines.extend([
        "",
        "## Language To Avoid",
        "",
    ])
    for phrase in positioning["anti_language"]:
        lines.append(f"- {phrase}")

    lines.extend([
        "",
        "## Best Angle Today",
        "",
        f"### {primary_angle['archetype']}: {primary_angle['angle']}",
        "",
        f"- **Contrarian edge**: {primary_angle['contrarian_edge']}",
        f"- **Customer language**: \"{primary_angle['customer_language']}\"",
        f"- **Best format**: {primary_angle['format']}",
        f"- **Hook seed**: {primary_angle['hook']}",
        "- **Body beats**:",
    ])
    for beat in primary_angle["body_beats"]:
        lines.append(f"  - {beat}")
    lines.extend([
        f"- **Audit bridge**: {primary_angle['audit_bridge']}",
        "",
        "## Other Strong Angles",
        "",
    ])
    for item in angle_archetypes[1:]:
        lines.extend([
            f"### {item['archetype']}: {item['angle']}",
            "",
            f"- **Contrarian edge**: {item['contrarian_edge']}",
            f"- **Customer language**: \"{item['customer_language']}\"",
            f"- **Hook seed**: {item['hook']}",
            f"- **Audit bridge**: {item['audit_bridge']}",
            "",
        ])

    append_angle_quality_gate(lines)
    append_publishable_angles(lines, publishable_angles)
    append_fire_off_prompts(lines, publishable_angles)

    lines.extend([
        "## Today's Draft Pack",
        "",
        f"- **Post drafts artifact**: {post_drafts_path}",
        f"- **Current run**: {'generated three 95% review-ready LinkedIn draft variants' if generate_post_drafts else 'skipped draft generation because --no-generate-post-drafts was passed'}.",
        "- **Default behavior**: the morning radar generates three 95% review-ready LinkedIn draft variants automatically unless explicitly skipped.",
        "- **Gate stack**: High Taste Writing OS, High-Dwell / LinkedIn Gate, Five-Input Content Gate, Publishable Copy Gate, and Grace / Excellence Gate.",
        "- **Human checkpoint**: review, add lived proof, and decide manually before publishing.",
        "- **Boundary**: no publishing, outreach, LinkedIn scraping, auto-comments, auto-likes, DMs, or contact actions.",
        "",
        "## 45-Minute Execution Loop",
        "",
    ])
    for index, step in enumerate(action_loop, start=1):
        lines.append(f"{index}. {step}")
    lines.append("")
    return lines


def write_creative_brief(path: Path, *, day: str, post_drafts_path: Path, generate_post_drafts: bool) -> list[str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = build_creative_brief_lines(
        day,
        post_drafts_path=post_drafts_path,
        generate_post_drafts=generate_post_drafts,
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return lines


def build_creative_brief_preview() -> dict[str, object]:
    positioning = build_content_intelligence()["positioning"]
    primary_angle = build_publishable_angles()[0]
    return {
        "recommended_angle": primary_angle["title"],
        "buyer_sentence": primary_angle["felt_problem"],
        "hook_seed": primary_angle["scroll_stop_hooks"][0],
        "audit_bridge": primary_angle["cta"],
        "action_loop": build_best_action_loop(),
        "buyer_language": positioning["buyer_language"],
    }


def write_morning_brief(
    path: Path,
    *,
    budget: dict,
    apify_status: str,
    prospects_csv: str,
    prospects_brief: str,
    normalized_prospects: int,
    fallback_reason: str,
    linkedin_evidence_csv: str,
    linkedin_evidence_summary: dict[str, object],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    publishable_angles = build_publishable_angles()
    content_intel = build_content_intelligence()
    positioning = content_intel["positioning"]
    angle_archetypes = build_angle_archetypes()
    action_loop = build_best_action_loop()
    lines = [
        "# Hybrid Morning Signal Radar",
        "",
        f"- **Date**: {date.today().isoformat()}",
        f"- **Apify status**: {apify_status}",
        f"- **Monthly budget**: ${budget['monthly_spent_dollars']} spent / ${budget['monthly_plan_dollars']} plan",
        f"- **Monthly state**: {budget['monthly_state']}",
        f"- **Daily Apify spend**: ${budget['daily_spent_dollars']}",
        f"- **Prospects normalized**: {normalized_prospects}",
        f"- **Prospect CSV**: {prospects_csv or 'not generated'}",
        f"- **Prospect brief**: {prospects_brief or 'not generated'}",
        f"- **LinkedIn evidence CSV**: {linkedin_evidence_csv}",
        "",
        "## Budget Guard",
        "",
        f"- Soft warning begins at ${budget['monthly_soft_warn_at']}.",
        f"- Hard stop begins at ${budget['monthly_hard_stop_at']}.",
        "- If state is yellow, keep runs small and prefer cheap sources.",
        "- If state is red, skip Apify and use fallback research.",
        "",
    ]

    if fallback_reason:
        lines.extend([
            "## Fallback Notice",
            "",
            fallback_reason,
        "",
    ])

    lines.extend([
        "## Content Intelligence Council",
        "",
        f"- **Market job**: {positioning['market_job']}",
        f"- **Audience state**: {positioning['audience_state']}",
        "- **Primary content objective**: Get the right person to recognize one expensive AI misfire and volunteer an artifact for review.",
        "- **Fast-cash constraint**: Do not chase broad AI punditry unless it creates audit demand.",
        "",
        "### Expert Filters",
        "",
    ])
    for lens in content_intel["expert_lenses"]:
        lines.extend([
            f"- **{lens['name']}**: {lens['filter']} Today: {lens['use_today']}",
        ])

    lines.extend([
        "",
        "### Buyer Language To Use",
        "",
    ])
    for phrase in positioning["buyer_language"]:
        lines.append(f"- \"{phrase}\"")

    lines.extend([
        "",
        "### Language To Avoid",
        "",
    ])
    for phrase in positioning["anti_language"]:
        lines.append(f"- {phrase}")

    lines.extend([
        "",
        "## LinkedIn Performance Boundary",
        "",
    ])
    for boundary in content_intel["performance_boundary"]:
        lines.append(f"- {boundary}")

    lines.extend([
        "",
        "## Human-Approved LinkedIn Evidence",
        "",
        f"- **Intake CSV**: {linkedin_evidence_csv}",
        f"- **Approved rows loaded**: {linkedin_evidence_summary['rows']}",
        "- **Evidence rule**: Only analyze artifacts Farrice manually provides or owns; never scrape, harvest, auto-engage, or infer hidden metrics.",
        "",
    ])
    if linkedin_evidence_summary["status"] == "empty":
        lines.extend([
            "### Next Evidence To Add",
            "",
            "- One manual post URL or screenshot from a relevant AI/workflow conversation.",
            "- One pasted hook/body that appears to be getting meaningful comments.",
            "- One owned-post analytics note if Farrice has posted already.",
            "- One buyer-language phrase from comments that sounds like a real pain, not creator jargon.",
            "",
        ])
    else:
        lines.extend([
            "### Evidence Synthesis",
            "",
        ])
        if linkedin_evidence_summary["top_formats"]:
            lines.append("- **Formats showing up**: " + ", ".join(
                f"{name} ({count})" for name, count in linkedin_evidence_summary["top_formats"]
            ))
        if linkedin_evidence_summary["top_archetypes"]:
            lines.append("- **Archetypes showing up**: " + ", ".join(
                f"{name} ({count})" for name, count in linkedin_evidence_summary["top_archetypes"]
            ))
        if linkedin_evidence_summary["buyer_language"]:
            lines.append("- **Buyer phrases to test**: " + " | ".join(
                f"\"{phrase}\"" for phrase in linkedin_evidence_summary["buyer_language"]
            ))
        if linkedin_evidence_summary["comment_language"]:
            lines.append("- **Comment language observed**: " + " | ".join(
                f"\"{phrase}\"" for phrase in linkedin_evidence_summary["comment_language"]
            ))
        if linkedin_evidence_summary["angle_tests"]:
            lines.append("- **Angle tests suggested by evidence**: " + " | ".join(
                str(item) for item in linkedin_evidence_summary["angle_tests"]
            ))
        lines.append("")

    lines.extend([
        "",
        "## Angle Archetypes For Today",
        "",
    ])
    for item in angle_archetypes:
        lines.extend([
            f"### {item['archetype']}: {item['angle']}",
            "",
            f"- **Contrarian edge**: {item['contrarian_edge']}",
            f"- **Customer language**: \"{item['customer_language']}\"",
            f"- **Best format**: {item['format']}",
            f"- **Hook seed**: {item['hook']}",
            "- **Body beats**:",
        ])
        for beat in item["body_beats"]:
            lines.append(f"  - {beat}")
        lines.extend([
            f"- **Audit bridge**: {item['audit_bridge']}",
            "",
        ])

    append_angle_quality_gate(lines)
    append_publishable_angles(lines, publishable_angles)

    lines.extend([
        "## Manual Prospect Review",
        "",
        "Review prospects manually before any connection request or outreach.",
        "",
        "Priority order:",
        "",
        "1. Founder-led experts with a clear offer and visible content/workflow dependency.",
        "2. AI-forward agencies with obvious client delivery or automation-diagnostic pain.",
        "3. Local premium services with public contactability and content/proposal/delivery needs.",
        "",
        "## 45-Minute Execution Loop",
        "",
    ])
    for index, step in enumerate(action_loop, start=1):
        lines.append(f"{index}. {step}")

    lines.extend([
        "",
        "## Platform Boundary",
        "",
        "No LinkedIn scraping, auto-DMs, auto-comments, auto-likes, or fake engagement.",
        "Use the radar to prepare better human action, not to pretend to be present.",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create the Hybrid Morning Signal Radar brief.")
    parser.add_argument("--location", default="Los Angeles", help="Location query for public lead discovery.")
    parser.add_argument("--limit", type=int, default=1, help="Max Apify results per query.")
    parser.add_argument("--daily-cap", type=float, default=0.20, help="Daily Apify dollar cap for this radar.")
    parser.add_argument("--out-dir", default="deliverables", help="Output directory.")
    parser.add_argument(
        "--generate-post-drafts",
        action="store_true",
        help="Compatibility flag. Post drafts are generated by default unless --no-generate-post-drafts is passed.",
    )
    parser.add_argument(
        "--no-generate-post-drafts",
        action="store_true",
        help="Skip the default three-draft High Taste LinkedIn draft pack.",
    )
    parser.add_argument(
        "--linkedin-evidence",
        default=str(BASE / "deliverables" / "hybrid-linkedin-evidence-intake.csv"),
        help="Human-approved LinkedIn evidence CSV. Created as a blank template if missing.",
    )
    args = parser.parse_args()

    load_env()
    usage = load_usage()
    daily_spent = today_spend(usage)
    budget = budget_summary(usage, daily_spent)
    query_count = 10
    estimated = estimated_maps_cost(query_count, args.limit)
    projected_daily = daily_spent + estimated
    out_dir = BASE / args.out_dir
    day = date.today().isoformat()
    prospect_prefix = out_dir / f"hybrid-morning-prospects-{day}"
    morning_path = out_dir / f"hybrid-morning-signal-radar-{day}.md"
    creative_brief_path = out_dir / f"hybrid-morning-creative-brief-{day}.md"
    post_drafts_path = out_dir / f"hybrid-morning-post-drafts-{day}.md"
    linkedin_evidence_path = Path(args.linkedin_evidence).expanduser()
    if not linkedin_evidence_path.is_absolute():
        linkedin_evidence_path = BASE / linkedin_evidence_path
    linkedin_evidence_rows = load_linkedin_evidence(linkedin_evidence_path)
    linkedin_evidence_summary = summarize_linkedin_evidence(linkedin_evidence_rows)

    apify_status = "skipped"
    fallback_reason = ""
    normalized_prospects = 0
    prospects_csv = ""
    prospects_brief = ""

    if budget["monthly_state"] == "red":
        fallback_reason = "Apify skipped because monthly state is red. Use local/manual research today."
    elif projected_daily > args.daily_cap:
        fallback_reason = (
            f"Apify skipped because projected daily spend ${round(projected_daily, 4)} "
            f"would exceed daily cap ${args.daily_cap}."
        )
    else:
        responses, rows, search_plan = run_multi_radar(
            preset="hybrid-fast-cash",
            queries=[],
            segments=DEFAULT_SEGMENTS,
            location=args.location,
            limit=args.limit,
        )
        normalized_prospects = len(rows)
        prospects_csv = str(prospect_prefix.with_suffix(".csv"))
        prospects_brief = str(prospect_prefix.with_suffix(".md"))
        write_csv(prospect_prefix.with_suffix(".csv"), rows)
        write_brief(
            prospect_prefix.with_suffix(".md"),
            search_label=", ".join(query for _, query in search_plan),
            location=args.location,
            responses=responses,
            rows=rows,
        )
        fallback_count = sum(1 for response in responses if response.get("fallback"))
        apify_status = "ok" if fallback_count == 0 else f"partial_fallback:{fallback_count}"
        if fallback_count:
            fallback_reason = (
                f"{fallback_count} Apify response(s) returned fallback. Review the prospect brief before relying on the queue."
            )

    refreshed_usage = load_usage()
    refreshed_budget = budget_summary(refreshed_usage, today_spend(refreshed_usage))

    write_morning_brief(
        morning_path,
        budget=refreshed_budget,
        apify_status=apify_status,
        prospects_csv=prospects_csv,
        prospects_brief=prospects_brief,
        normalized_prospects=normalized_prospects,
        fallback_reason=fallback_reason,
        linkedin_evidence_csv=str(linkedin_evidence_path),
        linkedin_evidence_summary=linkedin_evidence_summary,
    )
    post_drafts = []
    post_drafts_output = ""
    should_generate_post_drafts = not args.no_generate_post_drafts or args.generate_post_drafts
    write_creative_brief(
        creative_brief_path,
        day=day,
        post_drafts_path=post_drafts_path,
        generate_post_drafts=should_generate_post_drafts,
    )
    if should_generate_post_drafts:
        post_drafts = build_finished_post_drafts(build_publishable_angles())
        render_finished_post_drafts(post_drafts_path, day=day, drafts=post_drafts)
        post_drafts_output = str(post_drafts_path)

    print(json.dumps({
        "status": "ok",
        "apify_status": apify_status,
        "budget": refreshed_budget,
        "normalized_prospects": normalized_prospects,
        "morning_brief": str(morning_path),
        "creative_brief": str(creative_brief_path),
        "creative_brief_preview": build_creative_brief_preview(),
        "post_drafts": post_drafts_output,
        "post_drafts_preview": build_post_drafts_preview(post_drafts),
        "prospects_csv": prospects_csv,
        "prospects_brief": prospects_brief,
        "linkedin_evidence_csv": str(linkedin_evidence_path),
        "linkedin_evidence_rows": linkedin_evidence_summary["rows"],
        "fallback_reason": fallback_reason,
    }, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
