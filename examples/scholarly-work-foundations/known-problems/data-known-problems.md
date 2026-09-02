# Known data problems and deliberate traps

| Problem | Rows or fields | Required response | Do not do |
|---|---|---|---|
| Leading zeros | `00009`, all identifiers | import as text | convert identifiers to numbers |
| Exact duplicate | second `00105` | exclude once and log the rule | delete both occurrences |
| Non-identical duplicate candidates | same key, differing fields | apply an explicit priority/group/index or retain/exclude rule; record retained IDs and row counts | assume visible sort order determines which row remains |
| Test row | `TEST-01` | exclude through an explicit filter | delete it from the raw file |
| Locale-sensitive numbers | `1.204`, `1 125` | apply the documented source convention and test known values | trust automatic type detection |
| Mixed date precision | month, year, exact day, approximate and uncertain dates | separate display value, ISO value, precision and status | invent missing days or precision |
| Impossible date | `1914-13-40` | flag invalid; leave normalized date blank | silently coerce it |
| Missing values | creator, views, type, date | keep missingness explicit | replace blanks with zero or a guessed person |
| Category variants | `Photograph`, `photo`, `Postcard`, `postcard`, `razglednica` | document a mapping to analytical categories | overwrite the source string |
| Historical/bilingual place labels | `Laibach`, `Koper / Capodistria` | retain source form beside a reviewed grouping value | treat normalization as a neutral correction |

The cleaned layer is one defensible interpretation for the stated exercise, not a universal authority file.
