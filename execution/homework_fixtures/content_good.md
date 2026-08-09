# Known-good content fixture

This file exists so the `content` floor predicate has a healthy specimen to
accept. It reads like an ordinary working document because that is exactly what
it needs to be: several paragraphs of plain prose, long enough to clear the
stub threshold, with no placeholder text and no merge-conflict markers.

The prose here is deliberately plain. The second layer of the content floor
runs the repository's own ban-bank classifier over this text, so the fixture
must stay free of the phrases that classifier rejects. Short sentences help.
So does writing the way a person writes when they are explaining a thing to a
colleague and not performing for one.

If the predicate ever rejects this file, that is a false red, and the
standard_floor self-test will fail loudly — which is the point. A reporter that
cries wolf loses the operator's trust as fast as one that sleeps through the
burglary.
