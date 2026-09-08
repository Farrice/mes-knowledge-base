"""Tool events, not status prose, establish observable execution evidence."""
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'execution'))
from tool_event import normalize_event, event_status, full_read_paths
spec = importlib.util.spec_from_file_location('ledger_under_test', ROOT / 'execution/hooks/session_ledger_hook.py')
ledger_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ledger_module)

@pytest.fixture
def recorder(tmp_path, monkeypatch):
    monkeypatch.setattr(ledger_module, 'SESSIONS_DIR', tmp_path / 'sessions')
    state = ledger_module._load('fixture')
    monkeypatch.setattr(ledger_module, '_load', lambda _: state)
    monkeypatch.setattr(ledger_module, '_save', lambda _: None)
    monkeypatch.setattr(ledger_module, '_is_expert_skill', lambda _: True)
    monkeypatch.setattr(ledger_module, '_detect_birth_wiring', lambda _: None)
    def reconcile(ledger, name):
        ledger['reconciled_skill'] = name
        ledger['pending_routing'] = None
        return True
    monkeypatch.setattr(ledger_module, '_reconcile_routing_feedback', reconcile)
    def run(tool, tin, response, **extra):
        payload = dict(session_id='fixture', cwd=str(ROOT), tool_name=tool,
                       tool_input=tin, tool_response=response, **extra)
        with pytest.raises(SystemExit) as exc:
            ledger_module.handle_posttool(payload)
        assert exc.value.code == 0
        return state
    return run, state

@pytest.mark.parametrize('tool,tin,response', [
    ('exec_command', {'cmd': 'cat skills/test-expert/SKILL.md'}, {'exit_code': 0, 'output': 'skill contents'}),
    ('Bash', {'command': 'cat skills/test-expert/SKILL.md'}, {'stdout': 'skill contents'}),
    ('Read', {'file_path': str(ROOT / 'skills/test-expert/SKILL.md')}, {'content': 'skill contents'}),
])
def test_complete_reads_reconcile_route(recorder, tool, tin, response):
    run, state = recorder
    state['pending_routing'] = {'suggested': 'test-expert'}
    run(tool, tin, response)
    assert state['manifest']['skills_full'] == ['test-expert']
    assert state['reconciled_skill'] == 'test-expert'
    assert state['pending_routing'] is None
    assert any(d['type'] == 'skill_loaded' for d in state['debts'])

@pytest.mark.parametrize('command,response', [
    ('head -10 skills/test-expert/SKILL.md', {'exit_code': 0, 'output': 'partial'}),
    ('cat skills/test-expert/SKILL.md | head', {'exit_code': 0, 'output': 'partial'}),
    ('cat skills/test-expert/SKILL.md', {'exit_code': 0, 'output': 'tokens truncated'}),
    ('cat skills/test-expert/SKILL.md', {'exit_code': 2, 'output': ''}),
    ('cat skills/test-expert/SKILL.md', {'session_id': 123, 'output': 'still running'}),
])
def test_partial_failed_and_running_reads_never_claim_full(recorder, command, response):
    run, state = recorder
    run('exec_command', {'cmd': command}, response)
    assert state['manifest']['skills_full'] == []
    assert not any(d['type'] == 'skill_loaded' for d in state['debts'])

def test_sliced_native_read_is_not_full(recorder):
    run, state = recorder
    run('Read', {'file_path': str(ROOT / 'skills/test-expert/SKILL.md'), 'limit': 10}, {'content': 'slice'})
    assert state['manifest']['skills_full'] == []

@pytest.mark.parametrize('tool,tin,response', [
    ('Write', {'file_path': str(ROOT / '_active/proof.md')}, {'success': True}),
    ('apply_patch', '*** Begin Patch\n*** Add File: _active/proof.md\n+proof\n*** End Patch', {'output': 'Success. Updated the following files:'}),
])
def test_absolute_lane_and_patch_artifacts_are_recorded(recorder, tool, tin, response):
    run, state = recorder
    run(tool, tin, response)
    assert state['produced'] is True
    assert len(state['produced_paths']) == 1

@pytest.mark.parametrize('response', [{'isError': True}, {}, {'output': 'Error: patch rejected'}])
def test_unproven_or_failed_patch_never_claims_production(recorder, response):
    run, state = recorder
    run('apply_patch', {'input': '*** Add File: _active/proof.md'}, response)
    assert state['produced'] is False

@pytest.mark.parametrize('path', ['.agent/state.md', '.tmp/work.md', 'memory/notes.md', '/tmp/external-proof.md'])
def test_internal_and_external_files_do_not_count_as_workspace_deliverables(recorder, path):
    run, state = recorder
    run('Write', {'file_path': path}, {'success': True})
    assert state['produced'] is False

def test_exit_codes_and_recovery_are_not_inferred_from_text(recorder):
    run, state = recorder
    for _ in range(3):
        run('exec_command', {'cmd': 'python3 check.py'}, {'exit_code': 7, 'output': ''})
    assert state['bash_fail_streak'] == 3
    run('exec_command', {'cmd': 'python3 check.py'}, {'session_id': 42, 'output': ''})
    assert state['bash_fail_streak'] == 3
    run('exec_command', {'cmd': 'python3 check.py'}, {'exit_code': 0, 'output': 'Error: is a fixture string'})
    assert state['bash_fail_streak'] == 0
    assert state['learning_debt'][0]['streak'] == 3

def test_claude_semantic_no_matches_is_preserved(recorder):
    run, state = recorder
    run('Bash', {'command': 'rg needle'}, {'stdout': '', 'returnCodeInterpretation': 'No matches found'})
    assert state['execution_records'][-1]['status'] == 'succeeded'

def test_spawn_count_only_success_and_dedupes_delivery(recorder):
    run, state = recorder
    run('collaboration.spawn_agent', {'task_name': 'audit'}, {'agent_id': 'a1'}, tool_use_id='call1')
    run('collaboration.spawn_agent', {'task_name': 'audit'}, {'agent_id': 'a1'}, tool_use_id='call1')
    run('spawn_agent', {'task_name': 'audit'}, {'isError': True}, tool_use_id='call2')
    assert state['subagent_spawns'] == 1

def test_running_then_completion_same_id_is_not_dropped(recorder):
    run, state = recorder
    run('exec_command', {'cmd': 'false'}, {'session_id': 1}, call_id='cmd1')
    run('exec_command', {'cmd': 'false'}, {'exit_code': 1}, call_id='cmd1')
    assert state['bash_fail_streak'] == 1
    assert len(state['execution_records']) == 2

def test_receipt_markers_in_command_cannot_claim_closeout(recorder):
    run, state = recorder
    run('exec_command', {'cmd': "rg 'CLOSEOUT SPINE COMPLETE' execution/end_session_closeout.py"}, {'exit_code': 0, 'output': ''})
    assert state['closeout_ran'] is False
    run('exec_command', {'cmd': "echo chain_runner.py finalize CHAIN FINALIZE"}, {'exit_code': 1, 'output': 'CHAIN FINALIZE'})
    assert state['finalized_at'] is None

def test_adapter_resolves_active_root_before_normalizing(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location('runner', ROOT / '.codex/tools/codex_hook_runner.py')
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    (tmp_path / '.agent/workflows').mkdir(parents=True)
    (tmp_path / 'execution/hooks').mkdir(parents=True)
    (tmp_path / 'CODEX.md').write_text('fixture')
    (tmp_path / 'execution/hooks/session_ledger_hook.py').write_text('fixture')
    monkeypatch.setattr(sys, 'argv', ['runner', 'session-ledger', 'posttool'])
    import io
    monkeypatch.setattr(sys, 'stdin', io.StringIO(json.dumps({'cwd': str(tmp_path), 'tool_name': 'exec_command', 'tool_input': {'cmd': 'true'}})))
    captured = {}
    def call(args, **kwargs):
        captured.update(kwargs)
        return type('Result', (), dict(returncode=0, stdout='', stderr=''))()
    monkeypatch.setattr(runner.subprocess, 'run', call)
    assert runner.main() == 0
    assert captured['cwd'] == str(tmp_path)
    assert json.loads(captured['input'])['tool_input']['command'] == 'true'

@pytest.mark.parametrize('command,output', [
    ('echo chain_runner.py finalize CHAIN FINALIZE', 'CHAIN FINALIZE'),
    ('cat execution/end_session_closeout.py', 'print("CLOSEOUT SPINE COMPLETE")'),
    ('echo memory_facade.py prose_classifier.py', 'memory_facade.py prose_classifier.py'),
    ('echo solution_recorder.py save', 'SOLUTION CARD SAVED: docs/solutions/fake.md'),
    ('echo handoff_store.py pin', 'pinned: fake'),
])
def test_printed_or_read_markers_cannot_forge_execution(recorder, command, output):
    run, state = recorder
    run('exec_command', {'cmd': command}, {'exit_code': 0, 'output': output})
    assert state['finalized_at'] is None
    assert state['closeout_ran'] is False
    assert state['manifest']['gates_run'] == []
    assert state['solution_cards_saved'] == 0
    assert state['session_pinned'] is False

def test_actual_invocation_and_marker_create_receipt(recorder):
    run, state = recorder
    run('exec_command', {'cmd': 'python3 -B execution/chain_runner.py finalize proof'}, {'exit_code': 0, 'output': '  CHAIN FINALIZE — Steps 6-7 Complete'})
    assert state['finalized_at']
    assert state['manifest']['gates_run'] == ['chain_runner']

def test_external_same_named_skill_is_not_attributed_to_workspace(recorder):
    run, state = recorder
    run('Read', {'file_path': '/private/tmp/other/skills/test-expert/SKILL.md'}, {'content': 'different source'})
    assert state['manifest']['skills_full'] == []
    assert state['debts'] == []
    assert state['execution_records'][-1]['full_read_paths']

def test_native_poll_completion_retains_command_and_counts_failure_once(recorder):
    run, state = recorder
    run('exec_command', {'cmd': 'python3 execution/check.py'}, {'session_id': 99, 'output': ''})
    run('write_stdin', {'session_id': 99, 'chars': ''}, {'exit_code': 7, 'output': ''})
    run('write_stdin', {'session_id': 99, 'chars': ''}, {'exit_code': 7, 'output': ''})
    assert state['bash_fail_streak'] == 1
    assert state['execution_records'][-1]['tool'] == 'write_stdin'

def test_truncated_native_read_response_is_not_full(recorder):
    run, state = recorder
    run('Read', {'file_path': str(ROOT / 'skills/test-expert/SKILL.md')}, {'file': {'numLines': 2000, 'totalLines': 3000}})
    assert state['manifest']['skills_full'] == []


def test_real_adapter_and_ledger_process_write_execution_record(tmp_path):
    import shutil
    import subprocess
    for rel in ('.codex/tools/codex_hook_runner.py', 'execution/tool_event.py', 'execution/hooks/session_ledger_hook.py'):
        dest = tmp_path / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, dest)
    (tmp_path / 'CODEX.md').write_text('isolated transport fixture')
    (tmp_path / '.agent/workflows').mkdir(parents=True)
    payload = {'session_id': 'adapter-fixture', 'cwd': str(tmp_path),
               'tool_name': 'exec_command', 'tool_input': {'cmd': 'false'},
               'tool_response': {'exit_code': 7, 'output': ''}}
    proc = subprocess.run([sys.executable, str(tmp_path / '.codex/tools/codex_hook_runner.py'), 'session-ledger', 'posttool'],
                          input=json.dumps(payload), capture_output=True, text=True, check=True)
    saved = json.loads((tmp_path / '.agent/sessions/ledger-adapter-fixture.json').read_text())
    assert saved['bash_fail_streak'] == 1
    assert saved['execution_records'][-1]['exit_code'] == 7
    assert saved['execution_records'][-1]['status'] == 'failed'


def test_foreign_script_basename_cannot_forge_workspace_receipt(recorder):
    run, state = recorder
    run('exec_command', {'cmd': 'python3 /tmp/chain_runner.py finalize fake'}, {'exit_code': 0, 'output': 'CHAIN FINALIZE'})
    assert state['finalized_at'] is None
    assert state['manifest']['gates_run'] == []
