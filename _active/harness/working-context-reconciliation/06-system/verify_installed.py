#!/usr/bin/env python3
"""Synthetic installed-command replay. This does NOT attest native event firing."""
import json, os, shlex, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path('/Users/farricecain/Google Antigravity')
sys.path.insert(0,str(ROOT/'execution'))
import working_context as wc
hooks=json.loads((Path.home()/'.codex/hooks.json').read_text())['hooks']
commands={event: [h['command'] for group in groups for h in group['hooks'] if str(ROOT/'execution/working_context.py') in h.get('command','')] for event,groups in hooks.items()}
assert all(len(commands.get(e,[]))==1 for e in ('SessionStart','UserPromptSubmit','PreToolUse','PostToolUse','PreCompact','PostCompact','Stop'))
with tempfile.TemporaryDirectory(prefix='context-installed-probe-') as td:
 store=Path(td)/'isolated-probe.sqlite3'
 env={**os.environ,'WORKING_CONTEXT_STORE':str(store),'PYTHONDONTWRITEBYTECODE':'1'}
 sid='codex:synthetic-installed-probe'
 counts={}
 def fire(event,**extra):
  payload={'session_id':'synthetic-installed-probe','cwd':td,**extra}
  r=subprocess.run(shlex.split(commands[event][0]),input=json.dumps(payload),env=env,text=True,capture_output=True,timeout=15,check=True)
  counts[event]=counts.get(event,0)+1
  out=json.loads(r.stdout) if r.stdout.strip() else {}
  assert 'FAULT' not in r.stdout,(event,r.stdout)
  if 'hookSpecificOutput' in out:assert out['hookSpecificOutput']['hookEventName']==event
  return out
 fire('SessionStart')
 for n,text in enumerate(['Build the complete system.','Keep accepted components.','Refine the interface.','Preserve the research question.','Shorten the plan.','Status only.','Integrate the constraint.','Keep the commercial goal.','Restore the approved section.','Finish the authorized deployment.'],1):
  fire('UserPromptSubmit',prompt=text,turn_id='probe-'+str(n))
  fire('PreToolUse',tool_name='exec_command',tool_input={'cmd':'read state'})
  if n==3:
   assert fire('Stop',stop_hook_active=False)['decision']=='block'
   assert fire('Stop',stop_hook_active=True)=={}
  state=wc.read(sid,store)
  request={'expected_revision':state['revision'],'resolutions':[{'turn':n,'quote':text,'effect':'Synthetic fixture interpretation: preserve whole intent.'}]}
  if n==1:request.update(snapshot={'intent':'Build the complete system.','working_brief':'Integrate changes within the whole goal.','preserved':[],'artifacts':[]},write_root=td)
  wc.commit(sid,request,store)
  fire('PostToolUse',tool_name='apply_patch')
  if n==5:
   fire('PreCompact');fire('PostCompact');fire('SessionStart',source='resume')
  assert fire('Stop')=={}
 assert wc.read(sid,store)['status']=='CURRENT'
 print(json.dumps({'proof_kind':'SYNTHETIC_INSTALLED_COMMAND_REPLAY','turns':10,'commands':counts,'status':'PASS','native_event_firing':'NOT_PROVEN','semantic_interpretation':'MANUAL_FIXTURE','model_calls':0,'user_tasks_created':0},indent=2))
