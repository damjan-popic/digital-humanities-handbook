---
title: "User/AI transcript analysis"
description: "A transcript-analysis workflow for comparing user and AI sections with token and summary outputs."
tags: [projects, interviews, transcripts, Stanza, AI]
---

# User/AI transcript analysis

<div class="answer-meta" markdown>
<span>transcripts</span>
<span>Stanza</span>
<span>AI interaction</span>
</div>

## What this project does

This example analyses interview transcripts split into user and AI sections. It produces token-level output, section summaries, lemma summaries, transcript summaries, and optional CoNLL-U exports.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/createAI)

## Use this when

- you need to compare user and assistant language in structured transcripts.
- you want to process transcript sections separately.
- you need token-level and summary-level outputs from the same workflow.
- you want a compact example of Stanza-based transcript annotation.

## What to inspect in the code

- `scripts/` — processing scripts.
- `interview_split.tsv` — expected input structure.
- `interview_transcripts/` — transcript material; check sensitivity before reuse.
- `stanza_out/` — generated annotation outputs.
- `analysis/` — downstream summaries or analysis outputs.
- README command examples for choosing user, assistant, or both sections.

## Minimal run path

```bash
python -m pip install -U stanza pandas tqdm pyarrow openpyxl
python stanza_tag_sections.py \
  --input interview_split.tsv \
  --outdir stanza_out \
  --which both \
  --extra csv
```

Optional flag:

```bash
--conllu
```

## Relevant handbook workflows

- [How do I separate speakers with pyannote?](../workflows/audio/separate-speakers-with-pyannote.md)
- [How do I annotate a corpus with UDPipe?](../workflows/nlp/annotate-a-corpus-with-udpipe.md)
- [How do I audit AI output against source documents?](../workflows/ai/audit-ai-output-against-source-documents.md)
- [How do I package a corpus with FAIR metadata?](../workflows/publishing/package-a-corpus-with-fair-metadata.md)

## Practice use

Give users a tiny TSV with one transcript and two sections: `u_*` and `a_*`. Ask them to compute one section-level metric and one lemma-level summary, then explain what cannot be inferred from those metrics alone.

## Limits and cautions

- Interview transcripts can contain personal or sensitive data.
- Section labels must be consistent before annotation.
- Token-level annotation quality depends on language, model, and transcript cleanliness.
- Quantitative summaries should be paired with qualitative reading.
