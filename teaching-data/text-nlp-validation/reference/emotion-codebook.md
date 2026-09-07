# Contextual emotion codebook

Unit: one sentence from the synthetic contemporary teaching corpus.

- `emotion_present=true` requires explicit contextual evidence that a named or
  recoverable experiencer is represented as experiencing one of the deliberately
  coarse categories `joy`, `fear`, `anger` or `sadness`.
- A word association alone is insufficient. Negated, metalinguistic and ironic
  mentions can receive `emotion_present=false`.
- `experiencer` names who is represented as feeling; `target` names the entity,
  event or proposition toward which the emotion is directed or which stimulates
  it. Use `unresolved` when the sentence does not warrant a value.
- `voice` distinguishes narrator wording, reported speech and quoted speech.
  Quotation does not transfer the quoted emotion to the author or editor.
- `uncertain=true` preserves genuinely mixed or pragmatically underdetermined
  cases. It is not forced into the negative class for model evaluation; the
  baseline table reports it separately.

The scheme describes textual representation, not psychological state. All
examples are handbook-authored and synthetic.
