---
title: "How do I build and clean a Zotero library?"
description: "Collect a small set of humanities sources, correct their bibliographic metadata, and preserve attachments, notes, and rights decisions separately."
category: "Reference management"
category_id: "reference-management"
difficulty: "beginner"
time: "60–90 min"
tags: [zotero, metadata, bibliography, sources, quality-control]
---

# How do I build and clean a Zotero library?

<div class="answer-meta" markdown>
<span>Reference management</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

How can you preserve enough information about a source to find it again, cite it accurately, and explain what you actually consulted? A Zotero import is a candidate bibliographic record, not proof that the catalogue, database, DOI registry, or webpage supplied correct metadata.

This workflow creates a small, checked library. It keeps four objects distinct: the source, its Zotero item, any attached PDF or snapshot, and your reading note. The interface labels below describe Zotero's current desktop application and Connector; their position may change.

## You need

- five deliberately varied sources, including a book, article, mutable webpage, dataset, or software item;
- access to the authoritative source page, title page, colophon, catalogue, DOI record, or finding aid used for checking;
- [Zotero](https://www.zotero.org/download/) and the matching [Zotero Connector](https://www.zotero.org/download/connectors) from official sources;
- a written decision about whether attachments may be downloaded, synced, or shared.

The [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip) includes an identifier exercise, five RIS records, known metadata problems, and rights notes. It is a teaching sample, not evidence for a real historical claim.

## Workflow

1. **Install from the official site.** Install the Zotero desktop application, then the Connector for a supported browser. Restart the browser or word processor if an integration does not appear. Institutional computers may require an administrator.

2. **Create a project collection.** In *My Library*, create `Scholarly-work test`. A collection behaves more like a playlist than a file-system folder: drag the same item into `Writing`, `Data`, and `To verify` without creating duplicate library items. Use subcollections only when they answer a real retrieval need.

3. **Add records through four routes.** From a library catalogue or scholarly database, open the full record and use *Save to Zotero*. Add one verified DOI and one ISBN through *Add Item by Identifier*. Create one unusual or local source with *New Item* and the appropriate item type. Prefer the source's landing page to a direct PDF: a PDF is normally an attachment beneath a bibliographic parent item, not the item itself.

4. **Check the item type first.** An incorrectly imported webpage, book section, report, thesis, dataset, or journal article exposes the wrong fields and may render incorrectly. Compare the Zotero item with the source itself, not with another aggregator.

5. **Audit the fields that drive citation output.** Check creator roles and order; title and subtitle; publication or container title; date; volume and issue; page range; edition; publisher; DOI or ISBN; URL; and access date. Preserve corporate creators as organizations. Do not put a catalogue-record URL in the source URL field when you did not consult the work there. Store the date you actually accessed a mutable web resource.

6. **Record the correction.** Add a short child note such as `Metadata checked against title page and DOI landing page, 2026-09-02; corrected issue and page range.` Imported metadata are a starting point. A green Connector icon or a DOI does not certify every field.

7. **Organize without confusing functions.** Use collections for project membership, tags for topics or work states such as `read` and `metadata-checked`, and notes for traceable observations. In *Related*, connect a review with the reviewed book or a dataset with its documentation. Relationships support navigation; they do not merge the records.

8. **Merge genuine duplicates carefully.** Open *Duplicate Items*, compare candidates, select the best master values, and use *Merge*. Confirm that notes, tags, collections, and attachments remain. Two editions, translations, versions, or archival copies may describe related but distinct sources and should not be merged merely because their titles resemble one another.

9. **Run a five-item quality-control sample.** Choose records that stress different fields. For each, mark pass/fail for item type, creators, title, container, date, locator fields, stable identifier, URL/access date, and attachment status. Correct the Zotero record rather than planning to patch every future citation.

10. **Decide whether to sync.** Zotero can sync library data and notes; attachment storage is a separate concern. A personal sync account is useful across devices. A group library supports shared records, but membership and permissions must match the project. Do not upload copyrighted PDFs, restricted scans, personal data, or licensed database exports to a group or cloud service unless the rights and data conditions permit it. A citation record may be shareable when its attachment is not.

## Output

Produce:

```text
zotero-library-check/
├── five-item-qc.csv
├── metadata-correction-log.md
├── attachment-and-sync-decision.md
└── library-export.ris
```

The library passes when all five sampled records match an authoritative source for every applicable field, no attachment is mistaken for its parent item, and every synced file has a documented permission basis.

## Check yourself

- Does one source appear in multiple collections as one library item rather than as copies?
- Are authors, editors, translators, and corporate creators assigned the right roles and order?
- Can you identify which metadata came from import and which you verified?
- Are editions, translations, versions, and real duplicates distinguished?
- Could you share the bibliographic record without unlawfully sharing its attachment?

## Common traps

- Saving a PDF alone and citing its filename or PDF-extracted title.
- Treating imported capitalization, creator order, date, or item type as authoritative.
- Using tags, collections, related items, and duplicate merging as if they did the same job.
- Replacing a DOI with a database-session URL.
- Enabling attachment sync before checking copyright, privacy, and group permissions.

## Sources and interface status

Sources checked **2 September 2026**: Zotero's official [Basics](https://www.zotero.org/support/quick_start_guide), [Adding Items](https://www.zotero.org/support/adding_items_to_zotero), [Item Types and Fields](https://www.zotero.org/support/kb/item_types_and_fields), [Collections and Tags](https://www.zotero.org/support/collections_and_tags), [Duplicate Detection](https://www.zotero.org/support/duplicate_detection), [Syncing](https://www.zotero.org/support/sync), and [Group Libraries](https://www.zotero.org/support/groups) documentation. The conceptual checks remain valid if button placement changes; verify labels against the current official pages.

## Practice task

Import the five sample records through at least three routes. Deliberately correct one creator role, one item type, one container field, and one access date. Put one source into two collections, merge one genuine duplicate, and explain why one similar record must remain separate.
