import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import working_context as wc
import install_working_context as installer
import job_board
from hooks import superseded_read_guard as guard

class IntegrationTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(); self.root=Path(self.temp.name); self.home=self.root/'codex'
  self.home.mkdir(); self.store=self.root/'store.sqlite3'; self.sid='codex:fixture-session'
 def tearDown(self):self.temp.cleanup()
 def test_install_preserves_other_handlers_and_is_idempotent(self):
  original={'hooks':{'PreToolUse':[{'matcher':'Bash','hooks':[{'type':'command','command':'existing-safe-guard'}]}]}}
  hp=self.home/'hooks.json'; hp.write_text(json.dumps(original)); ap=self.home/'AGENTS.md'; ap.write_text('Existing instructions\n')
  first=installer.install(self.home,wc.ROOT,True)
  self.assertEqual(json.loads(hp.read_text())['hooks']['PreToolUse'][0],original['hooks']['PreToolUse'][0])
  self.assertEqual(installer.install(self.home,wc.ROOT,True)['status'],'ALREADY_CURRENT')
  installer.rollback(first['receipt']); self.assertEqual(json.loads(hp.read_text()),original); self.assertEqual(ap.read_text(),'Existing instructions\n')
 def test_rollback_refuses_later_user_edits(self):
  first=installer.install(self.home,wc.ROOT,True)
  (self.home/'AGENTS.md').write_text('Later user edit')
  with self.assertRaises(ValueError):installer.rollback(first['receipt'])
 def test_filename_does_not_establish_authority(self):
  p=self.root/'2026-01-01-draft.md';p.write_text('A dated approved source')
  (self.root/'draft.md').write_text('Newer but unreviewed')
  self.assertIsNone(guard.inspect(p))
  Path(str(p)+'.metadata.json').write_text(json.dumps({'status':'superseded','superseded_by':'CANON.md'}))
  self.assertIn('CANON.md',guard.inspect(p))
 def test_explicit_archive_remains_history(self):
  p=self.root/'99-archive'/'CURRENT.md';p.parent.mkdir();p.write_text('Old copy')
  self.assertIn('ARCHIVED',guard.inspect(p))
 def test_job_bridge_preserves_goal_and_flags_pending(self):
  env={'WORKING_CONTEXT_STORE':str(self.store),'CODEX_THREAD_ID':'fixture-session'}
  with patch.dict(os.environ,env):
   wc.observe(self.sid,str(self.root),'Keep the entire goal.',path=self.store)
   self.assertIn('requires reconciliation',wc.job_context_note())
   wc.commit(self.sid,{'expected_revision':1,'resolutions':[{'turn':1,'quote':'entire goal','effect':'Preserve whole intent.'}], 'snapshot':{'intent':'Keep the entire goal.','working_brief':'Act within it.','preserved':[],'artifacts':[]}},self.store)
   self.assertIn('Keep the entire goal.',wc.job_context_note())
   with patch('working_context.job_context_note',return_value='\nCONTEXT_RECEIPT'):
    brief=job_board.brief_text('fixture', {'goal':'Whole goal'}, {'id':'L1'}, {}, 'write', 'astra')
    self.assertIn('Job goal: Whole goal',brief);self.assertTrue(brief.endswith('CONTEXT_RECEIPT'))
    carddir=self.root/'mission';carddir.mkdir();(carddir/'card.md').write_text('Original mission card')
    with patch.object(job_board,'read',return_value={'goal':'Whole goal','lanes':[]}), patch.object(job_board.mc,'mission_dir',return_value=carddir), patch.object(job_board,'open_packets',return_value=[]), patch.object(job_board,'packets',return_value=[]), patch.object(job_board,'trace_lines',return_value=[]):
     portable=job_board.portable_text('fixture','codex')
     self.assertIn('Original mission card',portable);self.assertTrue(portable.endswith('CONTEXT_RECEIPT'))
 def test_old_renderer_cannot_reinstall_old_snapshot(self):
  wc.observe(self.sid,str(self.root),'Goal',path=self.store)
  request={'expected_revision':1,'resolutions':[{'turn':1,'quote':'Goal','effect':'Set goal'}],'snapshot':{'intent':'Goal','working_brief':'First','preserved':[],'artifacts':[]},'write_root':str(self.root)}
  old=wc.commit(self.sid,request,self.store)
  wc.observe(self.sid,str(self.root),'Refine',path=self.store)
  request.update(expected_revision=3,resolutions=[{'turn':2,'quote':'Refine','effect':'Refine brief'}]);request['snapshot']['working_brief']='Second'
  wc.commit(self.sid,request,self.store);wc.render(old,self.store)
  state=wc.read(self.sid,self.store);self.assertEqual(state['status'],'CURRENT');self.assertIn('Second',Path(state['current_view']).read_text())
 def test_malformed_packet_is_explicit_fault(self):
  with self.assertRaises(wc.Conflict):wc.hook([], 'codex','Stop',self.store)
  with self.assertRaises(wc.Conflict):wc.commit(self.sid,[],self.store)

if __name__=='__main__':unittest.main()
