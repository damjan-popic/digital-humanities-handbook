# Data dictionary and modelling limits

All CSV files are UTF-8 with headers and comma delimiters. Identifiers are case
sensitive. Blank assertion fields become SQL NULL; other blank fields must be
interpreted with their documented status, not as zero. Dates use Gregorian
YYYY-MM-DD and half-open intervals [start,end). Record times use canonical UTC.

| Input | Row and important fields |
|---|---|
| `entities.csv` | person, place or territory; stable `entity_id`, display label, `synthetic` |
| `sources.csv` | the exact ten-source inventory D1–D6, N1, N2, BORDER and NAMES; source type, anchored dossier locator and content status |
| `documents.csv` | one selected network document; genre, possible event window, source ID and locator |
| `participation.csv` | one unique person–document pair; role, confidence, source ID and synthetic flag |
| `assertions.csv` | subject, predicate, text XOR entity object, context, interval kind, recorded time, superseded assertion, source wording, wording relation and confidence |
| `candidates.csv` | one mention–candidate pair; original wording, source, unresolved decision and reason |
| `toponyms.csv` | one source-qualified name variant; language, context and validity interval; all fictional |
| `places.csv` | invented point in the local engineering square; x/y metres and stipulated ±75 m positional uncertainty |
| `boundaries.csv` | one source-qualified dated divider version; west is x below divider, east includes divider |
| `landmarks.csv` | authentic-map pixel candidate and current Wikidata coordinate/revision; reported precision is not verified accuracy |
| `gcps.csv` | same landmark rows plus cached EPSG:3794 easting/northing in metres |

`source_wording_relation` says exactly whether `source_wording` is an
`exact`, `translation` or `summary`; it must not be inferred from the
wording itself. All are statements about the fictional dossier, not quotations
from an archive. A02's value contains the deliberately mistaken transcription
while its source wording retains the stipulated signature. A03 supersedes A02.
Status assertions A04 and A05 remain parallel. Prefix all shortened IDs with SYN-.

The schema checks referential consistency and append-only assertions. The importer
checks canonical dates, the exact anchored source inventory and unique
participation. A superseding row must keep the earlier assertion's subject,
predicate, context, source, interval and date kind; a row can have at most one
direct successor. It is not a complete temporal
ontology: no unknown endpoints, calendar conversions or secured transaction
timestamps are implemented. Predicate/object type compatibility still needs
domain review. The conflict query reports overlapping different status labels,
not logical contradictions. `--conflicts` reports the full current review queue;
it does not apply the entity/date filters of the ordinary query.

## Output conventions

- `assertions-*.csv`: snapshots with source and date qualification.
- `membership.csv`: four centre/possible membership rows with explicitly named
  boundary-validity fields for two places and periods.
- `candidate-places.csv`: unresolved mention candidates joined to the historical
  states of each candidate place. Mention dates, boundary dates and name dates
  remain separate; `comparison_interval_*` is the true half-open intersection of
  a boundary version and name version, not the duration of the mention. Do not
  count these rows as residents.
- `authentic-issue-cooccurrence.csv`: six pairs from the four individually labelled
  reference observations; source locators are retained. No interaction is inferred.
- `projection-evidence.csv`: one row per pair and supporting document. Projection
  weights count distinct documents, not independent historical testimonies.
- `projection-singletons.csv`: documents with exactly one participant. They remain
  in `bipartite-edges.csv` but produce no projected pair and no fractional divisor.
- `*-metrics.csv`: degree, in/out degree, raw betweenness and outgoing harmonic
  closeness divided by N−1. Undirected in/out columns both equal ordinary degree.
  Edge weights select edges, but all retained paths have unit length.
- `correspondence-edges.csv`: sender, recipient, source, interval and confidence.
  A possible event window is not a duration. Repeated events would be separate
  evidence rows; graph metrics collapse duplicate endpoint pairs.
- `fractional-weights.csv`: sum of 1/(k−1) per shared document of size k.
- `gcp-residuals.csv`: Euclidean error in target metres, including withheld checks.
  Pixel y is positive down in inputs; QGIS points export reverses its sign.
- `gcp-leave-one-out.csv`: fit to three of four controls, check the omitted one.
- `results.json`: all metrics, weak components for directed graphs and all maximum
  unweighted undirected modularity partitions at resolution 1. Community analysis
  is restricted to the six-person graphs; correspondence direction is discarded
  for communities only. Isolates can cause tied partitions.

The authentic newspaper extract is unchanged and has its original dictionary
in the archival-friction packet. Its `synthetic=false` means an editorial
observation of the authentic item, not a verified person identity.
