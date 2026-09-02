# Independent manual checks

These checks are intentionally separate from the transformation layer.

## Row and exclusion check

- Raw rows excluding header: **10**.
- Exact duplicate: the second occurrence of `00105` (**1** row).
- Non-collection test record: `TEST-01` (**1** row).
- Accepted cleaned rows: **8**.
- Record identifiers remain text; `00009` retains both leading zeros.

## Category check

Count the retained identifiers without using the model summary:

- photograph: `00101`, `00102`, `00105` = **3**;
- postcard: `00103`, `00104`, `00106`, `00009` = **4**;
- unknown: `00107` = **1**;
- total = **8**.

Expected shares are 37.5%, 50.0% and 12.5%. They sum to 100.0%.

## Known-value check

- `00101` views should parse from `1.204` to **1204** under the documented source convention.
- `00103` views should parse from `1 125` to **1125**.
- `00104` views remain missing rather than becoming zero.
- `00106` has an invalid date and must not receive an invented ISO date.
- `Laibach` remains visible as a source label even when its grouping value is `Ljubljana`.

## Refresh test

In a copy of the raw file, add a new non-test row with a valid identifier and an object type already present in the mapping. Refresh the query. The accepted-row count and exactly one category total should increase by one. Undo or discard the modified copy after the test.
