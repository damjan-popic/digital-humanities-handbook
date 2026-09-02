---
title: "How do I cite with Zotero in Word or LibreOffice?"
description: "Insert locator-rich citations and a refreshable bibliography while keeping Zotero metadata and word-processor fields intact."
category: "Reference management"
category_id: "reference-management"
difficulty: "beginner"
time: "45–75 min"
tags: [zotero, word, libreoffice, citations, bibliography]
---

# How do I cite with Zotero in Word or LibreOffice?

<div class="answer-meta" markdown>
<span>Reference management</span><span>beginner</span><span>45–75 min</span>
</div>

## What you are trying to do

How can a citation remain connected to corrected source metadata while a paper changes? Zotero's word-processor integration inserts active fields. The visible citation is formatted output; the editable bibliographic facts belong in the Zotero item.

Choose and audit the required citation standard before this workflow. Do not maintain the same document simultaneously with Zotero and Word's built-in citation manager: two field systems make corrections and collaboration difficult to diagnose.

## You need

- a backed-up `.docx` or `.odt` working document;
- five metadata-checked Zotero items;
- the citation style and locale required by your faculty, journal, publisher, or instructor;
- at least one source passage whose page, section, paragraph, folio, or timestamp you have verified.

Use the [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip) for a small structured document, test records, bibliography, and citation-style audit.

## Workflow

1. **Verify the integration.** Open Zotero before the word processor. In Word, look for the *Zotero* tab. In LibreOffice Writer, look for the Zotero toolbar or menu. If it is absent, close the word processor and use Zotero *Settings/Preferences → Cite → Word Processors* to install or reinstall the appropriate plugin. Labels and placement differ by platform and release.

2. **Set document preferences.** In the Zotero tab or toolbar, open *Document Preferences*. Select the required style and, where offered, the citation language or locale. Decide whether the chosen style uses in-text citations, footnotes, or endnotes; these are conventions, not quality levels. Word or Writer controls the layout of notes, while Zotero formats their citation content.

3. **Insert a source at the claim.** Put the cursor immediately after the claim or quotation and choose *Add/Edit Citation*. Search for the checked item. Open the selected citation's options and enter the verified locator and locator type, such as page `27`, section `3`, or timestamp `00:04:12`. A locator identifies the cited passage; the item's full page range belongs in the bibliographic record.

4. **Insert multiple sources in one citation.** In the same citation dialog, add a second item and arrange the order only when the style or argument requires it. Add locators to the individual sources, not as unstructured text after the field.

5. **Generate the bibliography.** Place the cursor at the document's bibliography location and choose *Add/Edit Bibliography*. Do not type a parallel manual list. The bibliography is generated from active citations according to the selected style; a disciplinary brief may separately require uncited primary sources or archival groups.

6. **Correct at the source of truth.** If a citation shows a wrong author, title, date, or DOI, open the item in Zotero, correct the metadata there, return to the document, and choose *Refresh*. Do not repair the same error in every formatted citation.

7. **Treat active fields as fragile.** Avoid typing inside a shaded citation or generated bibliography. *Add/Edit Citation* can add a locator, prefix, suffix, or suppress an author where the style permits. A manual edit may be overwritten at refresh and may stop the citation from updating reliably.

8. **Refresh and inspect.** After moving paragraphs or correcting records, choose *Refresh*. Check five cases against the authoritative style guide: a simple source, a locator, multiple sources, a repeated citation, and an unusual creator or source type. Refresh is not a substitute for an editorial audit.

9. **Collaborate in a compatible copy.** Keep the working file in one format and test round trips before a deadline. Zotero may use Word fields or bookmarks depending on collaboration needs; current Zotero guidance generally prefers fields unless LibreOffice compatibility requires bookmarks. Never assume that converting repeatedly between `.docx` and `.odt` preserves every active field.

10. **Unlink only a backed-up final copy.** *Unlink Citations* removes Zotero field codes and prevents future automatic updates. Zotero documents this as irreversible. Use it only in a separate, backed-up delivery copy when a recipient specifically requires plain text. Keep the linked working document.

## Word and LibreOffice labels

| Operation | Word | LibreOffice Writer | Durable meaning |
| --- | --- | --- | --- |
| Insert/edit citation | *Zotero → Add/Edit Citation* | Zotero toolbar/menu → *Add/Edit Citation* | Insert or modify an active citation field. |
| Document style | *Zotero → Document Preferences* | Zotero toolbar/menu → *Document Preferences* | Set the citation style and available language options. |
| Bibliography | *Zotero → Add/Edit Bibliography* | Zotero toolbar/menu → *Add/Edit Bibliography* | Generate or edit the bibliography field. |
| Recalculate | *Zotero → Refresh* | Zotero toolbar/menu → *Refresh* | Re-render active citations from library metadata. |
| Finalize | *Zotero → Unlink Citations* | Zotero toolbar/menu → *Unlink Citations* | Irreversibly convert active citations to plain text. |

## Output

Produce a linked working document containing one citation with a locator, one multi-source citation, and a generated bibliography; a five-case comparison log; and, only if requested, a separately named unlinked delivery copy.

The workflow passes when a metadata correction made once in Zotero appears after *Refresh*, all five audit cases match the chosen authoritative guide or have a documented deviation, and the linked working copy remains available.

## Check yourself

- Can you explain whether the selected style is in-text, notes-and-bibliography, or numeric?
- Does every quotation or precise claim use the right locator type?
- Do multiple-source citations preserve source-specific locators?
- Does the bibliography change after a controlled metadata correction and refresh?
- Is any unlinked file clearly marked as a final copy rather than the master?

## Common traps

- Mixing Zotero with Word's built-in citation manager in one document.
- Typing page numbers outside the active citation instead of using a locator.
- Manually repairing the bibliography while leaving the Zotero record wrong.
- Assuming a footnote is automatically a notes-and-bibliography citation.
- Clicking *Unlink Citations* to solve an ordinary formatting problem.

## Sources and interface status

Sources checked **2 September 2026**: Zotero's official [Word Processor Plugins](https://www.zotero.org/support/word_processor_integration), [Using the Zotero Word Plugin](https://www.zotero.org/support/word_processor_plugin_usage), [Cite settings](https://www.zotero.org/support/preferences/cite), and [Troubleshooting](https://www.zotero.org/support/word_processor_plugin_troubleshooting) documentation. The plugin's concepts are shared across Word and Writer, but exact labels, field storage, and compatibility behaviour vary by platform and version.

## Practice task

Insert two single-source citations, one with a page locator, and one multi-source citation. Generate a bibliography, correct one record in Zotero, and refresh. Save the linked document, then write one sentence explaining why an unlinked copy cannot replace it.
