---
title: "How do I separate speakers with pyannote?"
description: "You have multi-speaker audio and need to know who spoke when."
category: "Audio"
difficulty: "advanced"
time: "45–120 min"
tags: [audio, speaker diarisation, pyannote, transcription]
---

# How do I separate speakers with pyannote?

<div class="answer-meta" markdown>
<span>Audio</span>
<span>advanced</span>
<span>45–120 min</span>
</div>

## What you are trying to do

You have multi-speaker audio and need to know who spoke when.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `audio.wav`
- Optional speaker labels or sample segments

## Tools

- [pyannote.audio](https://github.com/pyannote/pyannote-audio)

## Workflow

1. Prepare clean mono audio if possible.
2. Run a diarisation pipeline.
3. Export RTTM or JSON speaker turns.
4. Listen to boundary errors and overlapping speech.
5. Map anonymous speakers to names only when ethically appropriate.

## Output

Speaker-turn file such as RTTM plus notes.

## Check yourself

- Are speakers consistently separated?
- Are overlaps marked?
- Is consent/privacy handled?

## Common traps

- Assuming speaker labels identify real people.
- Ignoring background noise and crosstalk.
- Publishing sensitive speech metadata.

## Practice task

Users diarise a short interview clip manually, then compare with automatic segmentation.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
