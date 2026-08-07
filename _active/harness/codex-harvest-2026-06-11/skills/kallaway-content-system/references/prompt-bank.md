# Kallaway Content System — Prompt Bank

Use these as starting prompts inside the workflows. They are not final outputs by themselves.

## Topic Mining Prompt

```text
I am uploading a report of the top 100 videos in my niche over the last [TIME WINDOW]. These were posted by top creators in my niche.

Background: I make content in [NICHE] with the goal of helping [AVATAR]. My target authority statement is: I help [X PEOPLE] with [Y THING] so they can [Z OUTCOME].

First, screen out any videos that are not on-topic for what I would cover.

With the remaining videos, run two analyses:

1. List all videos in order by outlier score. For each, give me the specific 3-5 word topic, the original link, and a 1-2 sentence pitch for why this would be a strong video for me given my authority statement.

2. Cluster the videos by topic category. Create 8-15 clear buckets, rank them by highest average outlier score, and list the individual videos inside each bucket with topic, link, and the same pitch.
```

## Format Ranking Prompt

```text
Give me a breakout of all videos by storytelling format. Rank each format bucket by highest average outlier score. Inside each bucket, list the individual videos, links, and format names. Then recommend the top 3 formats I should use for [NICHE / AVATAR / OFFER], including the constraints each format creates for the script.
```

## Evidence Partner Prompt

```text
I am making a video about [TOPIC] in [FORMAT].

My contrarian take is: [TAKE].

Help me think through what evidence would make this claim believable. Give me proof options across: visual proof, A/B contrast, story, case study, metaphor, example, psychology, and data. Do not invent my point of view. Only help me strengthen and prove it.
```

## Hook Mad Lib Prompt

```text
Analyze the hooks from the top videos in [FORMAT].

For each, extract:
- original topic
- video URL
- spoken hook
- text hook if available
- Mad Lib hook format
- why the hook works for this format

When I give you a new topic and format, generate new hooks using only the strongest Mad Lib formats from this same format bucket. If the bucket is too thin, expand to adjacent formats and label them clearly.
```

## Script Profile Prompt

```text
I am uploading 10-20 top-performing transcripts from [CREATOR].

First, clean small transcript errors. Then build a short-form scripting profile from these examples. Capture tone, rhythm, sentence length, pacing, transition habits, opening logic, proof style, and closing style.

I want to feed you a topic, format, contrarian take, evidence, and hook, and have you draft in this voice/rhythm model. Save this as a script writing skill and tell me what inputs you need for the first script.
```
