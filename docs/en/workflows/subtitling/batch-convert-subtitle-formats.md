---
title: "How do I batch-convert subtitle formats?"
description: "You have subtitles in one format and need several delivery formats."
category: "Subtitling"
difficulty: "beginner"
time: "10–20 min"
tags: [subtitles, SRT, VTT, Subtitle Edit, accessibility]
---

# How do I batch-convert subtitle formats?

<div class="answer-meta" markdown>
<span>Subtitling</span>
<span>beginner</span>
<span>10–20 min</span>
</div>

## What you are trying to do

You have subtitles in one format and need several delivery formats.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Master subtitle file such as `.srt`

## Tools

- [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit)

## Workflow

1. Open Subtitle Edit.
2. Use batch convert or open the source subtitle.
3. Choose target formats such as SRT, VTT, ASS, or STL.
4. Preserve time codes unless you intentionally retime.
5. Export and test in the target player.

## Output

Subtitle files in multiple formats.

## Check yourself

- Do line breaks survive?
- Are timecodes valid?
- Does the target platform accept the file?

## Common traps

- Assuming all formats support the same styling.
- Forgetting WebVTT header requirements.
- Exporting without checking encoding.

## Practice task

Give each group a short subtitle file and a different target platform. They report what the platform accepts or rejects.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
