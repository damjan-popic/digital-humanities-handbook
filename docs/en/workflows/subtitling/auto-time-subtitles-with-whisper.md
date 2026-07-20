---
title: "How do I auto-time subtitles with Whisper?"
description: "You have speech audio or video and need a timed transcript quickly."
category: "Subtitling"
difficulty: "intermediate"
time: "30–90 min"
tags: [Whisper, subtitles, speech recognition, video]
---

# How do I auto-time subtitles with Whisper?

<div class="answer-meta" markdown>
<span>Subtitling</span>
<span>intermediate</span>
<span>30–90 min</span>
</div>

## What you are trying to do

You have speech audio or video and need a timed transcript quickly.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `video.mp4` or `audio.wav`
- Optional speaker or vocabulary notes

## Tools

- [Whisper](https://github.com/openai/whisper)
- [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit)

## Workflow

1. Convert noisy video to a clean audio file if needed.
2. Run Whisper or use Subtitle Edit’s speech-to-text function.
3. Choose a model size appropriate for your machine.
4. Export SRT or VTT.
5. Manually correct names, terminology, punctuation, and timing.

## Output

Timed subtitle file.

## Check yourself

- Are proper names correct?
- Are line lengths readable?
- Do timecodes match speech, not only sentence boundaries?

## Common traps

- Trusting automatic punctuation.
- Ignoring accessibility line length and reading speed.
- Using a giant model on a slow machine without a reason.

## Practice task

Users compare raw ASR output with a corrected version and classify error types: names, numbers, punctuation, segmentation.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
