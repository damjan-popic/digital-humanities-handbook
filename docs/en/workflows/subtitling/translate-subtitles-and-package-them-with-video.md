---
title: "How do I translate subtitles and package them with video?"
description: "You need translated subtitles and want them selectable inside a video file."
category: "Subtitling"
difficulty: "intermediate"
time: "45–90 min"
tags: [subtitles, translation, DeepL, MKVToolNix, video]
---

# How do I translate subtitles and package them with video?

<div class="answer-meta" markdown>
<span>Subtitling</span>
<span>intermediate</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You need translated subtitles and want them selectable inside a video file.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Source subtitle file such as `es.srt`
- Video file

## Tools

- [DeepL](https://www.deepl.com)
- [MKVToolNix](https://mkvtoolnix.download)

## Workflow

1. Translate subtitles with a machine-translation tool or CAT workflow.
2. Review segment by segment; subtitles have timing constraints that MT ignores.
3. Save translated subtitles as `target.srt`.
4. Use MKVToolNix to add subtitles as selectable tracks.
5. Label track language and title clearly.

## Output

MKV file with selectable subtitle track.

## Check yourself

- Does the subtitle track appear in the video player?
- Are long MT sentences shortened?
- Are cultural references handled?

## Common traps

- Machine-translating without reading-speed review.
- Burning subtitles in when a selectable track is better.
- Forgetting language metadata.

## Practice task

Have groups translate the same 30-second clip and compare how each handles condensation.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
