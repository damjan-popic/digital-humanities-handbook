# Known problems and bounded uncertainty

- The CLASSLA sample is purposive, small and partly selected for difficulty.
  Layer scores diagnose this sample only and have no confidence interval.
- The manual reference annotation is a reviewed scholarly intervention. Another
  qualified annotator may reasonably disagree, especially about dependency
  heads, relations and historical lemmas.
- Provider OCR and historical reference are two textual realizations of one
  source passage. Comparing their downstream annotations mixes recognition
  damage with annotation behaviour; it is not an independent corpus contrast.
- Exact-form emotion matching intentionally ignores lemmatization. The miniature
  lexicon is incomplete and its category `fear` deliberately groups concern with
  fear for teaching purposes.
- The twelve-document synthetic corpus is far below a defensible empirical topic
  study. Topic stability output demonstrates sensitivity and matching only.
- NMF topic identity is established by maximum top-word Jaccard overlap within
  one component count. Low overlap and ties remain uncertainty, not failure to
  be hidden.
- Model versions, resource files and interfaces can change. Frozen output records
  one run and ordinary CI does not re-download it.
- Slovene documentation is a machine-assisted draft pending specialist review.
