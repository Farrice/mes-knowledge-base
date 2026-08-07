# Avatar Content Elevation System

Purpose: Codify the repeatable process that produced the Coach Cooz V3 avatar and content package.

## What Was Created

This system is now available as an on-demand command:

```text
/avatar-content-elevation [client/brand/project + source files or folder]
```

It was installed in three places so both Codex and the Antigravity command bridge can find it:

- `.agent/workflows/avatar-content-elevation.md`
- `.agents/skills/source-command-avatar-content-elevation/SKILL.md`
- `.claude/commands/avatar-content-elevation.md`

It was also registered in:

- `SLASH_COMMANDS.md`

## What The Workflow Produces

By default, the workflow creates a new artifact folder:

```text
brain/[client-slug]-avatar-content-v[version]/
```

With these files:

- `README.md`
- `AVATAR-ICP-BELIEF-PROFILE.md`
- `CONTENT-STRATEGY-V3.md`
- `LINKEDIN-POSTS-V3.md`
- `INSTAGRAM-YOUTUBE-BLOG-CASCADE-V3.md`
- `VOICE-MEMO-INTAKE-PROMPTS.md`

## The Core Pipeline

1. Gather source truth before writing.
2. Build one real buyer avatar before polishing copy.
3. Map the buyer's private conversation, objections, failed attempts, and belief shifts.
4. Turn the avatar into semantic content lanes and reader-value rules.
5. Rewrite primary platform content with proof, tension, insight, and practical next moves.
6. Adapt the strongest ideas into platform-native Instagram, YouTube, and blog assets.
7. Add voice memo prompts so future batches keep the client's real voice.
8. Run final reader-value, voice, proof, platform, and anti-slop gates.

## Why This Repeats The Coach Cooz Result

The workflow preserves the actual sequence that made the Coach Cooz V3 package stronger:

- buyer truth before content polish
- plain buyer language before brand poetry
- proof with transfer instead of self-proof
- practical reader value in every post
- emotional tension without manipulation
- platform-native adaptation instead of copy-paste repurposing
- voice capture prompts to prevent AI drift

## When To Use

Use it when a brand/content package is already decent but feels like a 6-7 out of 10:

- the strategy is smart but too abstract
- the content is concise but lacks reader value
- the profile is clear but not emotionally sticky
- the ICP is described but not felt
- social posts sound polished but do not create movement
- platform assets exist but feel like resized versions of the same thought

## Recommended Invocation

```text
/avatar-content-elevation "Use these source files and produce a comparison-ready V3 package for [client]. Preserve source files and create a new artifact folder."
```

## Notes

This is not a scheduled automation. It is an on-demand production workflow. That is the right shape because each run needs source files, buyer context, proof status, and current platform priorities.
