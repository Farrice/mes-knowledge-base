import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'execution'))
from routing_enforcer import match_bindings
class PropertyVideoRouting(unittest.TestCase):
 def test_finished_video_uses_production(self):
  for text in ['Make a Bradford-style vertical video from this listing URL','Create a property listing video for Jen','Produce a calm property walkthrough','Make a vertical real estate video from these photos']:
   with self.subTest(text=text):self.assertEqual(match_bindings(text)[0]['workflow'],'jen-property-video')
 def test_copy_and_weekly_work_not_stolen(self):
  for text in ['listing hooks and scripts for Jen','Create a listing package from this listing URL','Caption only for this property video','Video script only for this listing video','Build Jen week 2026-09-21','Make a product launch video']:
   with self.subTest(text=text):self.assertNotIn('jen_property_video',[r['binding_id'] for r in match_bindings(text)])
if __name__=='__main__':unittest.main()
