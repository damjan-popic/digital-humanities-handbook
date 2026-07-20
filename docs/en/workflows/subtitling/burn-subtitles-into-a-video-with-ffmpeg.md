---
title: "How do I burn subtitles into a video with FFmpeg?"
description: "You need hard subtitles that are permanently visible in the video."
category: "Subtitling"
difficulty: "intermediate"
time: "20–45 min"
tags: [FFmpeg, subtitles, video, accessibility]
---

# How do I burn subtitles into a video with FFmpeg?

<div class="answer-meta" markdown>
<span>Subtitling</span>
<span>intermediate</span>
<span>20–45 min</span>
</div>

## What you are trying to do

You need hard subtitles that are permanently visible in the video.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `video.mp4`
- Subtitle file such as `.srt` or `.ass`

## Tools

- [FFmpeg](https://ffmpeg.org)
- [Whisper](https://github.com/openai/whisper)

## Workflow

1. Create or correct the subtitle file first.
2. Test subtitle display in a player.
3. Use FFmpeg’s subtitles filter to burn in text.
4. Choose compression settings that preserve readability.
5. Watch the output from start to finish.

## Output

`out.mp4` with burned-in subtitles.

## Check yourself

- Are subtitles readable on small screens?
- Do diacritics render?
- Is the output file size reasonable?

## Common traps

- Burning in when selectable subtitles would be more accessible.
- Font or encoding problems.
- Not checking final video.

## Practice task

Compare hard subtitles, soft subtitles, and captions. Users decide which is best for three use cases.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
