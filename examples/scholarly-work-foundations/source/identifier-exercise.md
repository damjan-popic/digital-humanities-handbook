# Persistent-identifier exercise

Use these deliberately mixed inputs to test Zotero's **Add Item by Identifier** command and your metadata checks.

| Input | Expected kind | Check after retrieval |
|---|---|---|
| `9780231168014` | ISBN for a scholarly book | creator order, title capitalization, publisher, place, year |
| `10.3138/jsp.46.4.BR2` | DOI for a journal review | review title, reviewed author, journal, volume, issue, pages, year |
| `https://writingcenter.fas.harvard.edu/thesis` | URL, not an identifier to paste into the identifier tool | capture from the landing page; check corporate author and access date |
| `10.0000/not-a-real-doi` | deliberately invalid DOI | record the failed lookup; do not invent a record |

Interface labels may change. The stable test is whether the identifier resolves to the intended work and whether the resulting bibliographic fields are supported by the authoritative record.
