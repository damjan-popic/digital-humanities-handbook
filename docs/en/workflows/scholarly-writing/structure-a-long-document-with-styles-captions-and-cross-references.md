---
title: "How do I structure a long document with styles, captions, and cross-references?"
description: "Build a revisable Word or LibreOffice Writer document whose headings, contents, captions, references, notes, and review marks remain connected."
category: "Scholarly writing"
category_id: "scholarly-writing"
difficulty: "beginner"
time: "60–100 min"
tags: [word, libreoffice-writer, styles, captions, cross-references, accessibility]
---

# How do I structure a long document with styles, captions, and cross-references?

<div class="answer-meta" markdown>
<span>Scholarly writing</span><span>beginner</span><span>60–100 min</span>
</div>

## What you are trying to do

How can a paper survive reordered sections, inserted figures, collaborative review, and a new page layout without hand-repairing every heading and reference? Word and LibreOffice Writer can store structural roles and fields. A bold line only looks like a heading; a Heading style identifies it for navigation, accessibility, and an automatic table of contents.

The current labels below are orientation points, not permanent facts. Word desktop, Word for the web, macOS, localized Office, and LibreOffice Writer expose different subsets and menus.

## You need

- a backed-up paper draft with two heading levels, one table, one figure, one note, and one internal reference;
- Word desktop or LibreOffice Writer; browser versions may not expose all field and section features;
- the [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip), containing paired `.docx` and `.odt` examples and a manual-check log.

## Workflow

1. **Reveal the structure.** Turn on non-printing marks and open Word's *Navigation Pane* or Writer's *Navigator*. List the intended title, Heading 1 sections, and Heading 2 subsections before changing appearance. Do not skip a level merely because Heading 3 looks better.

2. **Apply paragraph styles.** Use built-in *Title*, *Heading 1*, *Heading 2*, and body/Normal styles according to semantic role. Modify the style definition once if the design must change. Direct bold, font size, spacing, or color is appropriate for a small exception, not as a substitute for structure.

3. **Generate the contents page.** In Word use *References → Table of Contents*; in Writer use *Insert → Table of Contents and Index → Table of Contents, Index or Bibliography*. Generate from heading levels. Do not type titles and page numbers by hand. Update the contents after structural changes.

4. **Choose the right break.** A **page break** starts following content on a new page without changing the page setup. A **section break** in Word, or a deliberate page-style change in Writer, creates a boundary for page numbering, headers, footers, columns, margins, or orientation. Repeated blank paragraphs are neither.

5. **Set front matter and page numbers.** Keep the title page and optional abstract/contents distinct from the main text. In Word, a new section can use Roman numerals or no visible number before Arabic numbering begins; unlink its header/footer from the previous section before changing it. Writer uses page styles and page-number fields. Keep this basic and test the exported PDF.

6. **Insert real captions.** Select the table or figure and use Word *References → Insert Caption* or Writer *Insert Caption*/the object's *Caption* command. Choose the correct label and write a complete caption: identifier, descriptive title, source, relevant transformation, unit/denominator, and missing-value or rights note. The automatically numbered field—not typed `Figure 1`—supports renumbering.

7. **Insert a cross-reference.** Create the target first. In Word use *Insert/References → Cross-reference*; in Writer use *Insert → Cross-reference* or *Insert → Field → More Fields → Cross-references*. Select the caption, heading, footnote, or bookmark and the required display form. A pasted “see Table 2” is text, not a live reference.

8. **Use real footnotes or endnotes.** Insert them through *References → Insert Footnote/Endnote* in Word or *Insert → Footnote and Endnote* in Writer. Choose between footnotes and endnotes according to the governing citation system, guidelines, and genre. Do not type a superscript and a note at the bottom of the page manually.

9. **Add review evidence.** Use comments for questions or explanations and *Track Changes*/*Record Changes* for proposed textual changes. Identify reviewers. Inspect each suggestion in context and accept or reject it deliberately; “accept all” can remove necessary distinctions or import an error.

10. **Add meaningful alternative text.** Describe the purpose and relevant content of each informative image or chart. Mark a truly decorative object as decorative where supported. Do not repeat the caption verbatim when it does not explain the visual relationship. Real headings also let screen-reader users navigate the document.

11. **Update fields before submission.** Save a backup, then update the contents, captions, cross-references, page numbers, and Zotero citations/bibliography using their own update commands. In Word, selecting the document and updating fields can refresh many Word fields, but Zotero citations should be refreshed from the Zotero plugin. In Writer, update indexes and fields explicitly. Inspect rather than assuming every field updated.

12. **Test movement and export.** Insert a heading before section 2 and a figure before the first figure. Update fields. Confirm that navigation, contents, numbering, and cross-references changed correctly. Export to PDF and check page breaks, links, alternative text where the export supports it, and the reading order. Keep the editable source file.

## Output

Produce one structured working document with a two-level heading hierarchy, automatic contents, deliberate page/section or page-style boundary, numbered caption, live cross-reference, real note, page numbering, one comment, one tracked change, and meaningful alternative text.

The workflow passes when moving a section and inserting a figure followed by field updates requires no manual renumbering, the navigation view matches the intended outline, and the exported document remains readable.

## Check yourself

- Can the navigation pane or Navigator display the whole heading hierarchy?
- Does the contents page update after a heading is renamed?
- Do caption numbers and cross-references update after an insertion?
- Are page and section breaks used for different purposes?
- Have comments and tracked changes been reviewed individually?
- Can the purpose of each informative visual be understood without seeing it?

## Common traps

- Making headings with manual bold and font size.
- Typing a contents page, caption number, or “see Figure 3” by hand.
- Pressing Enter repeatedly to reach the next page.
- Using a section break for every new page or a page break where numbering must change.
- Updating Word fields but forgetting Zotero fields, or the reverse.
- Assuming a clean-looking PDF preserves the editable structure of the source document.

## Sources and interface status

Sources checked **2 September 2026**: Microsoft Support on [heading styles](https://support.microsoft.com/en-us/word/add-a-heading-in-a-word-document), [tables of contents](https://support.microsoft.com/en-us/word/format-or-customize-a-table-of-contents-in-word), [section breaks](https://support.microsoft.com/en-us/word/use-section-breaks-to-change-the-layout-or-formatting-in-one-section-of-your-word-document), [captions](https://support.microsoft.com/en-us/word/add-format-or-delete-captions-in-word), [cross-references](https://support.microsoft.com/en-us/word/create-a-cross-reference), [footnotes and endnotes](https://support.microsoft.com/en-us/word/training/insert-footnotes-and-endnotes-in-word), [field updates](https://support.microsoft.com/en-us/word/update-fields), [tracked changes](https://support.microsoft.com/en-us/word/training/track-changes-in-word), [page-number sections](https://support.microsoft.com/en-us/word/customize-page-numbers-and-their-formats-in-different-word-document-sections), and [accessible Word documents](https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities); LibreOffice Help on [Writer](https://help.libreoffice.org/latest/en-US/text/swriter/guide/main.html), [contents entries](https://help.libreoffice.org/latest/en-US/text/swriter/guide/indices_enter.html), [cross-references](https://help.libreoffice.org/latest/en-US/text/swriter/01/04090002.html), [footnotes and endnotes](https://help.libreoffice.org/latest/en-US/text/swriter/guide/footnote_usage.html), and the [Navigator](https://help.libreoffice.org/latest/en-US/text/swriter/01/02110000.html). Exact labels and feature parity remain version-dependent.

## Practice task

Repair the sample document, move one subsection, add a second figure, and update all fields. Record which actions worked in your application and which label differed from this page.
