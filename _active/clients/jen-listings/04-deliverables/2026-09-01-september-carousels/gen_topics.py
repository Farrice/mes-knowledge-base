#!/usr/bin/env python3
"""Five first-time-buyer topics for Jen's voice memos (2026-09-02): one instinctive question each, plus the shape her
sixty seconds turns into (the reel, the carousel). Valley Native cards T1..T5 + a forwardable text (TOPICS-for-jen.md).
Her words are the blanks; nothing here asserts a number."""
import pathlib
from gen_valley import HEAD, SERIF, SIGN, FRAME, INK, STEEL, SOFT, CREAM, HAIR, GREY, DIMC, RULED, stamp_mark, it

OUT = pathlib.Path(__file__).parent


def mast():
    return f'''  <div style="position: relative; display: flex; flex-direction: column; gap: 22px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {INK};">@_JIING</span>
      <span style="font-size: 23px; letter-spacing: 0.24em; color: {DIMC};">VOICE MEMO TOPICS</span>
    </div>
    <div style="height: 1px; background: {HAIR};"></div>
    <div style="display: flex; align-items: center; gap: 18px; padding-top: 2px;">
      {stamp_mark(44, INK)}
      <div style="display: flex; flex-direction: column; gap: 3px;">
        <span style="{SIGN} font-size: 22px; font-weight: 600; letter-spacing: 0.2em; color: {INK};">FIRST-TIME BUYERS</span>
        <span style="{SIGN} font-size: 15px; letter-spacing: 0.28em; color: {GREY};">FROM THE VALLEY</span>
      </div>
    </div>
  </div>'''


def col(title, lines, fill=False):
    body = "".join(
        f'<div style="display: flex; gap: 14px; align-items: baseline;"><span style="{SIGN} font-size: 14px; font-weight: 600; letter-spacing: 0.18em; color: {STEEL}; width: 74px; flex: none;">{k}</span>'
        f'<span style="font-size: 21px; line-height: 1.38; color: {INK if strong else GREY}; font-weight: {600 if strong else 400};">{t}</span></div>'
        for k, t, strong in lines)
    return f'''<div style="flex: 1; display: flex; flex-direction: column; gap: 13px; border: 2px solid {INK}; background: {"#FFFFFF" if fill else "transparent"}; padding: 24px 26px;">
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL}; margin-bottom: 4px;">{title}</div>{body}</div>'''


def card(n, title, why, question, reel, carousel):
    return f'''<div style="{FRAME} background: {CREAM}; display: flex; flex-direction: column; justify-content: space-between; padding: 90px 100px;">
{mast()}
  <div style="position: relative; display: flex; flex-direction: column; gap: 26px;">
    <div style="font-size: 56px; font-weight: 600; line-height: 1.12; color: {INK}; letter-spacing: -0.015em;">{title}</div>
    <div style="font-size: 23px; line-height: 1.5; color: {GREY};">{why}</div>
    <div style="display: flex; flex-direction: column; gap: 12px; background: {INK}; padding: 30px 34px;">
      <div style="{SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.22em; color: #9FB4CC;">THE MEMO &#183; SIXTY SECONDS &#183; FIRST THING THAT COMES OUT</div>
      <div style="{SERIF} font-style: italic; font-size: 36px; line-height: 1.32; color: {CREAM};">{question}</div>
    </div>
    <div style="display: flex; gap: 22px;">
      {col("THE REEL &#183; 40 SECONDS", reel, fill=True)}
      {col("THE CAROUSEL &#183; 7 SLIDES", carousel)}
    </div>
  </div>
  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 22px; letter-spacing: 0.22em; color: {DIMC};">YOUR WORDS FILL THE BLANKS</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {DIMC};">{n}&#8202;/&#8202;5</span>
  </div>
</div>'''


Y = "[your words]"
topics = [
    dict(
        title=f'the 20% down {it("myth.")}',
        why="the reason most renters never call anyone. you already correct this one in your captions; the memo makes it a whole post.",
        question="someone at dinner says &#8220;we&#8217;d buy, but we don&#8217;t have 20% down.&#8221; what comes out of your mouth?",
        reel=[("HOOK", "you don&#8217;t need 20% down. you never did.", True), ("BEAT 1", f"what people actually put down in the valley {Y}", False),
              ("BEAT 2", f"the one thing that matters more than the down payment {Y}", False), ("BEAT 3", f"what changes when the number is smaller {Y}", False),
              ("CLOSE", "&#8220;i&#8217;m here for you. that&#8217;s my job.&#8221;", True)],
        carousel=[("1", "cover: the myth, in the buyer&#8217;s words", False), ("2", "the keyed map: four ways people actually buy here", False),
                  ("3", f"the number people really put down {Y}", False), ("4", "dark slide: the sentence a lender said to you once", False),
                  ("5", f"what a smaller down payment costs, and what it buys {Y}", False), ("6", "the mistake: waiting to save while prices move", False),
                  ("7", "close: &#8220;tell me what you&#8217;ve saved. we&#8217;ll go from there.&#8221;", True)],
    ),
    dict(
        title=f'what your rent {it("already buys.")}',
        why="the math every renter runs at 11pm and gets wrong. real valley numbers, from you, not a calculator.",
        question="a friend pays around $3,000 a month in rent and thinks buying is out of reach. walk them through it the way you would in the car.",
        reel=[("HOOK", "your rent is a mortgage. just not yours.", True), ("BEAT 1", f"what $3,000 a month is in a payment, roughly {Y}", False),
              ("BEAT 2", f"the part of the payment renters forget goes to them {Y}", False), ("BEAT 3", f"where in the valley that payment lands {Y}", False),
              ("CLOSE", "&#8220;send me your rent number. i&#8217;ll show you the other side.&#8221;", True)],
        carousel=[("1", "cover: the rent number, big", False), ("2", "the keyed map: four neighborhoods that payment reaches", False),
                  ("3", f"the payment, side by side {Y}", False), ("4", "dark slide: what stays yours each month", False),
                  ("5", f"the one cost renters don&#8217;t see coming {Y}", False), ("6", "the honest part: when renting is the right call", False),
                  ("7", "close: her close + &#8220;my DMs are open&#8221;", True)],
    ),
    dict(
        title=f'&#8220;i don&#8217;t think {it("we&#8217;re ready.")}&#8221;',
        why="the fear under every first-time buyer: am i being irresponsible? you talk people through this weekly. nobody sees it.",
        question="what do you say to the couple who&#8217;s been &#8220;almost ready&#8221; for two years?",
        reel=[("HOOK", "nobody feels ready. that&#8217;s not the test.", True), ("BEAT 1", f"what ready actually looks like, in your experience {Y}", False),
              ("BEAT 2", f"the thing people wait for that never comes {Y}", False), ("BEAT 3", f"the first small step, the one that costs nothing {Y}", False),
              ("CLOSE", "&#8220;everything works out exactly the way it&#8217;s supposed to.&#8221;", True)],
        carousel=[("1", "cover: the sentence, in their words", False), ("2", "the keyed map: four things ready is not", False),
                  ("3", f"what ready is {Y}", False), ("4", "dark slide: the couple who waited, what it cost", False),
                  ("5", f"the first step {Y}", False), ("6", "the reframe: you don&#8217;t decide today, you find out today", False),
                  ("7", "close: &#8220;just breathe&#8221; + her close", True)],
    ),
    dict(
        title=f'the thirty days after {it("yes.")}',
        why="offer accepted is where first-timers panic and nobody warned them. the timeline, in your voice, is a saved-and-sent post.",
        question="their offer just got accepted. what happens in the next thirty days, and where do people freak out?",
        reel=[("HOOK", "you got the house. now the scary part.", True), ("BEAT 1", f"week one, what actually happens {Y}", False),
              ("BEAT 2", f"the moment people panic, and why it&#8217;s normal {Y}", False), ("BEAT 3", f"what you do so they don&#8217;t {Y}", False),
              ("CLOSE", "&#8220;i do this to protect you and your best interest.&#8221;", True)],
        carousel=[("1", "cover: day one, keys are thirty days away", False), ("2", "the keyed map: four weeks, four stops", False),
                  ("3", f"week one {Y}", False), ("4", "dark slide: the inspection day feeling", False),
                  ("5", f"the number that can move, and what you do about it {Y}", False), ("6", "what you never sign without reading", False),
                  ("7", "close: &#8220;we&#8217;re gonna do this, this, and this, and go from there.&#8221;", True)],
    ),
    dict(
        title=f'how to spot a {it("lipstick remodel.")}',
        why="your word, your eye. you can feel quality in the handles and the doors; buyers can&#8217;t. this is the tour people save.",
        question="you walk into a flip. what do you touch first, and what tells you they cut corners?",
        reel=[("HOOK", "pretty kitchen. cheap house. here&#8217;s how i know.", True), ("BEAT 1", f"the first thing you touch {Y}", False),
              ("BEAT 2", f"the thing they always skip {Y}", False), ("BEAT 3", f"what a real remodel feels like, the one you couldn&#8217;t stop thinking about {Y}", False),
              ("CLOSE", "&#8220;send me the listing before you fall in love. i&#8217;ll tell you what i see.&#8221;", True)],
        carousel=[("1", "cover: the phrase, lipstick remodel", False), ("2", "the keyed map: four places to look in the first minute", False),
                  ("3", f"the handles, the doors, the windows {Y}", False), ("4", "dark slide: what&#8217;s behind the new paint", False),
                  ("5", f"the question to ask the listing agent {Y}", False), ("6", "the one you loved: the stone, the finishes, why it felt different", False),
                  ("7", "close: her close + &#8220;my DMs are open&#8221;", True)],
    ),
]

for k, t in enumerate(topics, 1):
    (OUT / f"T{k}.dc.html").write_text(HEAD.format(body=card(k, **t)))

# forwardable text
import re
def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    return s.replace("&#8217;", "'").replace("&#8220;", "“").replace("&#8221;", "”").replace("&#183;", "·").replace("&#8202;", "")

lines = ["five voice memos, whenever you have a minute in the car. sixty seconds each, first thing that comes out, don't fix it. each one becomes a reel and a carousel in your look; you read everything before it posts.\n"]
for k, t in enumerate(topics, 1):
    lines.append(f"{k}. {plain(t['title'])}\n   {plain(t['question'])}\n")
lines.append("that's it. no scripts, no reading anything. just talk.")
(OUT / "TOPICS-for-jen.md").write_text("\n".join(lines))
print("wrote T1..T5 + TOPICS-for-jen.md")
