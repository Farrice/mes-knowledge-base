import json
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'execution'))
from content_analysis_live_trial import AUTH, Denied, payload, run, validate

class Trial(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.calls=0
 def tearDown(self):self.tmp.cleanup()
 def provider(self,p):
  self.calls+=1
  return {'status':'completed','usage':{'total_input_tokens':100,'total_output_tokens':5,'total_tokens':108,'total_thought_tokens':3}}
 def test_no_authority_no_state(self):
  with self.assertRaises(Denied):run(payload('a'),'',self.root,self.provider)
  self.assertEqual(list(self.root.iterdir()),[])
 def test_same_request_is_cached(self):
  self.assertFalse(run(payload('a'),AUTH,self.root,self.provider)['cached'])
  self.assertTrue(run(payload('a'),AUTH,self.root,self.provider)['cached']);self.assertEqual(self.calls,1)
 def test_six_attempts_no_released_reservation(self):
  for i in range(6):run(payload(str(i)),AUTH,self.root,self.provider)
  with self.assertRaises(Denied):run(payload('7'),AUTH,self.root,self.provider)
  self.assertEqual(self.calls,6)
  d=json.loads((self.root/'ledger.json').read_text());self.assertEqual(sum(c['reserved_micro_usd'] for c in d['calls']),7500000)
 def test_uncertain_result_blocks_changed_request(self):
  with self.assertRaises(Denied):run(payload('a'),AUTH,self.root,lambda _: {})
  with self.assertRaises(Denied):run(payload('b'),AUTH,self.root,self.provider)
  self.assertEqual(self.calls,0)
 def test_interruption_survives(self):
  def crash(_):raise KeyboardInterrupt()
  with self.assertRaises(KeyboardInterrupt):run(payload('a'),AUTH,self.root,crash)
  with self.assertRaises(Denied):run(payload('a'),AUTH,self.root,self.provider)
 def test_envelope_rejects_agentic_tools_other_source_and_model(self):
  for change in [lambda p:p['input'][0].update(uri='https://example.com/v'),lambda p:p['input'][0].update(processing='agentic'),lambda p:p.update(model='other'),lambda p:p.update(tools=[{'type':'google_search'}])]:
   p=payload('a');change(p)
   with self.assertRaises(Denied):validate(p)
 def test_tool_usage_does_not_pass_as_static(self):
  def wrong(p):
   r=self.provider(p);r['usage']['total_tool_use_tokens']=1;return r
  with self.assertRaises(Denied):run(payload('a'),AUTH,self.root,wrong)
 def test_full_timeline_and_thought_accounting(self):
  p=payload('a');v=p['input'][0];self.assertEqual(v['processing']['start_offset'],'0s');self.assertEqual(v['processing']['end_offset'],'9908s')
  r=run(p,AUTH,self.root,self.provider);self.assertEqual(r['receipt']['conservative_usage_cost_usd'],.000105)
 def test_recovered_real_usage_is_not_zero_cost_or_complete(self):
  fixture=Path(__file__).resolve().parents[1]/'extractions/paddy-galloway/youtube-masterclass/gemini-recovered-response.json'
  response=json.loads(fixture.read_text())
  with self.assertRaisesRegex(Denied,'conflicting input'):
   run(payload('real response counter check'),AUTH,self.root,lambda _:response)
  with self.assertRaises(Denied):run(payload('new request'),AUTH,self.root,self.provider)
  self.assertEqual(self.calls,0)
 def test_nonterminal_response_does_not_cache_as_complete(self):
  def pending(p):
   r=self.provider(p);r['status']='in_progress';return r
  with self.assertRaisesRegex(Denied,'not completed'):run(payload('a'),AUTH,self.root,pending)
 def test_underreported_totals_block(self):
  def wrong(p):
   r=self.provider(p);r['usage']['total_tokens']=1;return r
  with self.assertRaisesRegex(Denied,'inconsistent usage'):run(payload('a'),AUTH,self.root,wrong)
 def test_existing_dispatch_lock_prevents_second_transport(self):
  import fcntl
  with (self.root/'single-flight.lock').open('a') as lock:
   fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
   with self.assertRaisesRegex(Denied,'another request'):
    run(payload('a'),AUTH,self.root,self.provider)
  self.assertEqual(self.calls,0)
  self.assertFalse((self.root/'ledger.json').exists())
if __name__=='__main__':unittest.main()
