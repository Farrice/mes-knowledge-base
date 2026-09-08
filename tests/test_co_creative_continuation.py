"""Real operator regressions plus nearby creative and permission controls."""
import importlib.util
import io
import json
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'execution'))
import codex_operator_preflight as codex
import autopilot_runtime_preflight as autopilot
import co_creative_launchpad as launchpad
from control_intent import classify_control_intent
import skill_router_hook as router

ACTUAL_REQUEST = """All right, let's execute restore memory and add execution records. Let's complete the private Scrapes audit, and let's prove better work.

I want your help to envision how we elevate and enhance the system, hobble it, and get rid of contradictions and things that are restraining the system from operating as intended. I think we have plenty of system history and session threads for you to understand what my intent is and what I'm going for here.

I think one thing that is evident is that I thought we had some type of co-creative work with each other, where you would reiterate what I said or give me a brief for understanding before going off to execute a task. I know now that we're working on our Antigravity workspace that should be working, but I don't know. I'm just trying to come up with ways to be able to work with you better and get better results, or remarkable results instantly, instead of having to do so much back-and-forth work all the time."""

def test_actual_request_has_one_owner_and_retains_requested_outcomes():
    packet = codex.build_preflight(ACTUAL_REQUEST)
    lp = packet['co_creative_launchpad']
    assert packet['chosen_path']['owner'] == lp['route_bias']['primary'] == lp['handoff']['route'] == 'system-audit'
    assert packet['execution_decision']['can_execute_now'] is True
    assert lp['pause_or_run']['requires_pause'] is False
    assert lp['questions_that_change_execution'] == []
    for phrase in ('restore memory', 'execution records', 'private Scrapes audit', 'prove better work'):
        assert phrase in lp['center']

@pytest.mark.parametrize('query', [
    'Write a fictional story about restoring someone\'s memory.',
    'Write a buyer-first Reel script for Jen about homes.',
    'Help me improve the opening hook of this newsletter.',
])
def test_creative_requests_do_not_become_system_repairs(query):
    assert classify_control_intent(query)['route'] != 'system-audit'

@pytest.mark.parametrize('query,expected', [
    ('Draft a buyer-first Reel script for Jen about San Fernando Valley homes. Do not publish it or spend money.', []),
    ('Write a buyer-first draft without paid tools.', []),
    ('Create a publisher brief.', []),
    ('Do not publish it, but spend money on the render.', ['paid or quota-heavy tool']),
    ('Never spend money; then publish the approved post.', ['external write']),
    ('Do not publish yet; then publish after approval.', ['external write']),
])
def test_shared_risk_parser_preserves_prohibitions_and_later_actions(query, expected):
    assert codex.risk_reasons(query) == expected
    assert bool(autopilot.risk_reasons(query, 'auto')) == bool(expected)
    assert launchpad.pause_or_run(query=query, missing=[], clarity_score=100)['requires_pause'] == bool(expected)

def test_question_reply_keeps_owner_and_new_instruction_remains_visible(monkeypatch):
    reply = '<send_user_message_question_reply>' + json.dumps([{'question': 'Which failures? Positioning? OS?', 'answer': 'All of the above.'}]) + '</send_user_message_question_reply>'
    seen = []
    def resolve(prompt, _):
        seen.append(prompt)
        raise SystemExit(0)  # Stop before any state-writing hook branch.
    monkeypatch.setattr(router, 'resolve_explicit_command_alias', resolve)
    for prompt, expected in [(reply, []), (reply + '\nRun /system-audit on execution records.', ['Run /system-audit on execution records.'])]:
        seen.clear()
        monkeypatch.setattr(sys, 'stdin', io.StringIO(json.dumps({'prompt': prompt})))
        with pytest.raises(SystemExit):
            router.main()
        assert seen == expected

def test_existing_repeatability_owner_is_preserved():
    assert launchpad.route_bias('Repair intent routing drift', 'repeatability-spine')['primary'] == 'repeatability-spine'

@pytest.mark.parametrize('query', [
    'Draft a message, then email it to Jen.',
    'Prepare the report and email it to Jen.',
    'Review the message and DM the client.',
])
def test_draft_noun_does_not_hide_later_external_action(query):
    assert 'external write' in codex.risk_reasons(query)

@pytest.mark.parametrize('query', [
    'Write a post about why Agentic OS is useful.',
    'Draft an article about problems with session memory in fictional robots.',
])
def test_runtime_topic_in_content_is_not_system_repair(query):
    assert classify_control_intent(query)['route'] != 'system-audit'
