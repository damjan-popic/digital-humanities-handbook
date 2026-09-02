# Citation-style comparison and corrections

## Procedure

1. Generate one full note, one shortened repeat note and the complete bibliography in a fresh document.
2. Compare them with the current Chicago notes-and-bibliography examples, field by field.
3. Correct bibliographic metadata in Zotero, refresh the document, and rerun the comparison.
4. Record a local output correction only when the governing authority genuinely departs from the CSL result; do not hide bad metadata with word-processor edits.

## Model audit log

| Record | Observed problem | Root cause | Correction layer | Recheck |
|---|---|---|---|---|
| Hayot book | place missing after RIS import in one test installation | imported field mapping differed | Zotero item metadata | full note and bibliography regenerated |
| Gump review | reviewed-work wording needed inspection | review is not a generic research article | item type/title metadata checked against DOI record | full note compared with authority |
| Harvard page | access date displayed only if the chosen style calls for it | style rule, not missing source evidence | no manual document edit; date retained in Zotero | bibliography refreshed |
| Dataset | corporate creator initially entered as personal names | creator mode incorrect | single-field corporate creator in Zotero | note begins with corporate author |
| Workbook | source type has no perfect universal model | venue instructions may vary | case recorded for editorial decision | unresolved status carried forward |

## Audit result

The bibliography document in this pack is an illustrative static output. It demonstrates a reviewable layout but does not replace a live Zotero refresh. A learner's audit passes only when the exact installed CSL label/version, generated outputs, authoritative comparison and remaining exceptions are all preserved together.
