# Expected observations

These are checks, not interpretations to copy into an essay.

- The packet has one authentic historical object: one unchanged two-page
  PDF. It has eight handbook-created, source-grounded observations: one issue
  and seven features. Four teaching perturbations are explicitly synthetic.
- The raw table has nine rows because AF-SYN-004 adds one duplicate; the
  cleaned/reference table has eight stable observation IDs.
- AF-P1-002 has no supported photograph-creation date. Its
  `date_normalized` is blank and `date_status` is `unknown`; 1925-02-07 is
  stored only as `issue_context_date`.
- Relative printed dates support 1925-02-01 for AF-P1-001 and 1925-01-27 for
  AF-P1-004 under documented, reversible editorial decisions.
- Clear printed names remain local labels even when no external authority
  search was attempted. AF-P2-001 is `multiple_people`, not one unresolved
  identity. “Meker” is retained; Ezra Meeker is a `candidate_rejected`.
- `correction-log.csv` has nine source-grounded editorial decisions and four
  synthetic reversals. The ninth records selection, decoding and whitespace
  normalization from the exact dLib TXT export into the comparison excerpt.
  All carry locators, evidence, process, date, rule version, confidence and
  reversibility.
- The OCR audit covers the complete declared comparison excerpt. CER and WER
  begin after that extraction normalization and do not measure omitted
  layout-whitespace behaviour. Word-error-audit rows
  sum to the word substitutions/deletions/insertions; character operations
  are a separate whole-string alignment. CER and WER use the reference
  denominators and six-decimal round-half-even formatting.
- `output/record-summary.csv` reports inventory, record kinds, date states,
  entity structures and authority-link states. Counts describe the model;
  they do not interpret the issue's politics.
