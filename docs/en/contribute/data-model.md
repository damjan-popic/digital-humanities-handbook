# Data model

Every answer page uses YAML front matter.

| Field | Meaning | Example |
|---|---|---|
| `title` | Question-style title | `How do I map places mentioned in a text?` |
| `description` | One-sentence summary | `Create a map from extracted place mentions.` |
| `category` | Human-readable category | `Mapping` |
| `difficulty` | `beginner`, `intermediate`, or `advanced` | `beginner` |
| `time` | Estimated duration | `45–90 min` |
| `tags` | Searchable labels | `[mapping, geocoding, places]` |

## Required headings

The checker expects these headings in every answer page:

- `## What you are trying to do`
- `## You need`
- `## Tools`
- `## Workflow`
- `## Output`
- `## Check yourself`
- `## Common traps`
- `## Practice task`

## Why this matters

The metadata makes search, tags, navigation, peer review, and future automation easier. It also keeps documentation usable as the collection grows.
