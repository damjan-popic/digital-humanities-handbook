---
title: "How do I choose, apply, and audit a citation style?"
description: "Identify the required citation system, select its concrete style, test varied source types, and document corrections and unresolved cases."
category: "Reference management"
category_id: "reference-management"
difficulty: "beginner"
time: "75–120 min"
tags: [citation-style, csl, zotero, locators, audit]
---

# How do I choose, apply, and audit a citation style?

<div class="answer-meta" markdown>
<span>Reference management</span><span>beginner</span><span>75–120 min</span>
</div>

## What you are trying to do

How can you know that an automatically formatted bibliography satisfies the rules that govern a real submission? A **citation system** establishes the basic arrangement, such as author–date, notes and bibliography, or numeric references. A **citation style** is a concrete formatting implementation, often encoded in Citation Style Language (CSL). The governing faculty, journal, publisher, or professional-association **citation guidelines** may add submission-specific requirements. These distinctions are editorial conventions, not a quality ranking.

Keep the chain explicit: a **source** is the evidence; a **bibliographic record** describes it; a **citation** points from a claim to that record; a **locator** identifies the cited passage or unit; a **bibliography** lists records according to selection rules; a **citation style** formats and orders these elements; and local or venue-specific citation guidelines may add requirements that the generic style does not encode.

## You need

- the current official or faculty-approved style guide and its version or access date;
- five corrected Zotero records representing deliberately different source types;
- Word or LibreOffice Writer with the Zotero plugin;
- the [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip), whose `citation-style-audit/` folder models the expected evidence.

## Workflow

1. **Identify the authority before the style name.** Record who requires the standard: faculty, instructor, journal, publisher, archive, or discipline. Note the guide title, edition or version, URL, access date, language, and any local supplement. “Harvard” alone is not a single authoritative specification.

2. **Classify the citation system.** An **author–date** system usually connects a parenthetical author and year to a reference list. A **notes-and-bibliography** system uses footnotes or endnotes, often with a bibliography. A **numeric** system connects numbers to an ordered list. These are different conventions and rhetorical emphases, not ascending levels of rigour.

3. **Select the corresponding Zotero CSL style.** Use the Zotero Style Repository or the exact style named by the authority. Record its title and update date where visible. Set the requested locale or document language, then preview output. CSL controls formatting and localized terms, but a style can be outdated, incorrectly selected, or unable to express a local exception.

4. **Plan appropriate locators.** Use pages for paginated works, sections or paragraphs for structured online texts, folios for manuscripts, timestamps for audiovisual material, and collection/series/box/folder or another archival signature for archival material. Do not invent a page number for an unpaginated source. Follow the chosen guide for labels, ranges, and placement.

5. **Test five varied records.** Include at least: a book or chapter with editor/translator/edition information; a journal article with DOI; a corporate-author mutable webpage with access date; a dataset or digital edition with version and stable identifier where available; and software, code, map, archival item, handbook release, or another field-specific source. The sample adds same-author/year and translated-work questions to the checklist.

6. **Stress difficult creator and repetition cases.** Check a corporate author, editor instead of author, translator, later edition, translated work, repeated citation, and multiple works by the same author in one year. Confirm how the guide disambiguates names and years. Never force all creator roles into an Author field merely to make one output look plausible.

7. **Audit identifiers and mutability.** Prefer a DOI or another maintained stable identifier when the guide requests it. A DOI and a URL have different functions; do not keep a transient database-session URL as if it were persistent. Record access dates for mutable web resources when the standard or source conditions require them.

8. **Check non-book sources without pretending one rule fits all.** Consult the chosen guide's current instructions for archival material, datasets, software, code, maps, digital editions, AI systems or outputs, and citable handbook releases. If the guide has no adequate model, record the unresolved case and seek an editor's decision. For AI, also disclose use and preserve enough prompt/output/version evidence to verify the claim; a citation alone is not methodological disclosure.

9. **Separate source function from bibliography layout.** Primary and secondary sources play different roles in an argument, but not every humanities field requires separate bibliography sections. Follow the brief and explain any grouping. Do not infer a universal primary/secondary structure from one style's example bibliography.

10. **Correct metadata, refresh, and compare.** Fix creators, titles, dates, item type, identifiers, and edition data in Zotero. Refresh the document and compare each generated citation and bibliography entry field by field with the authority. Do not patch the same output manually in every occurrence.

11. **Document justified local deviations.** A faculty brief may require a heading, primary-source division, archival convention, or capitalization not represented by the CSL style. Record the authority, exact deviation, reason, scope, and whether it must be reapplied after refresh. Escalate contradictions rather than silently choosing one rule.

## Citation-style audit matrix

| Test | Compare | Pass condition |
| --- | --- | --- |
| Creator | order, initials, corporate name, role labels | Matches authority; Zotero roles are correct. |
| Title/container | capitalization, italics, quotation marks, edition | Matches source metadata and guide. |
| Date/repetition | publication date, access date, same-year suffix, shortened repeat | Matches the system and local brief. |
| Locator | type, label, range, placement | Identifies the consulted unit without inventing pagination. |
| Identifier | DOI, URL, archive signature, dataset/software version | Uses the guide's preferred durable form. |
| Bibliography | inclusion, order, hanging indent, grouping | Matches the authority or documents a local deviation. |

## Output

```text
citation-style-audit/
├── style-and-version.md
├── five-test-records.md
├── generated-bibliography.docx-or-odt
├── comparison-and-corrections.md
└── unresolved-cases.md
```

The audit passes when five different source types have been compared against the named authority, metadata corrections are made in Zotero and survive refresh, and every remaining discrepancy has an owner or editorial decision path.

## Check yourself

- Can you name the authority and version, not only the Zotero style label?
- Have you tested the citation and the bibliography rather than only one of them?
- Are locators appropriate to each source's material form?
- Are DOI, URL, access date, version, and archival signature used for distinct purposes?
- Does each local deviation have a written reason and scope?

## Common traps

- Choosing a style because it looks familiar rather than because an authority requires it.
- Calling author–date “scientific” and notes “humanities” as universal rules.
- Confusing the source's total page range with the locator of a cited passage.
- Manually repairing generated output while leaving the underlying record wrong.
- Treating CSL output as self-validating or assuming every source type has a settled template.

## Sources and interface status

Sources checked **2 September 2026**: Zotero's official [Citation Styles](https://www.zotero.org/support/styles), [Standard Citation Styles](https://www.zotero.org/support/kb/style_standards), [Item Types and Fields](https://www.zotero.org/support/kb/item_types_and_fields), and [word-processor usage](https://www.zotero.org/support/word_processor_plugin_usage); the official [CSL primer](https://docs.citationstyles.org/en/stable/primer.html); and the [Chicago-Style Citation Quick Guide](https://www.chicagomanualofstyle.org/tools_citationguide), which explicitly distinguishes notes-and-bibliography from author–date. Always replace the example authority with the current guide governing your submission.

## Practice task

Audit the five sample records. Introduce one controlled metadata error, refresh, identify its effect, correct the Zotero record, and refresh again. Add one unresolved local case and state who must decide it.
