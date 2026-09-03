PRAGMA foreign_keys = ON;

CREATE TABLE entity (
  entity_id TEXT PRIMARY KEY NOT NULL,
  kind TEXT NOT NULL CHECK (kind IN ('person','place','territory')),
  label TEXT NOT NULL,
  synthetic TEXT NOT NULL CHECK (synthetic = 'true')
);
CREATE TABLE source (
  source_id TEXT PRIMARY KEY NOT NULL,
  locator TEXT NOT NULL,
  synthetic TEXT NOT NULL CHECK (synthetic = 'true')
);
CREATE TABLE assertion (
  assertion_id TEXT PRIMARY KEY NOT NULL,
  subject_id TEXT NOT NULL REFERENCES entity(entity_id),
  predicate TEXT NOT NULL CHECK (predicate IN
    ('name','status','language_assigned','language_used','language_knowledge',
     'residence','territorial_membership')),
  value_text TEXT,
  object_id TEXT REFERENCES entity(entity_id),
  context TEXT NOT NULL,
  valid_start TEXT NOT NULL,
  valid_end TEXT NOT NULL,
  date_kind TEXT NOT NULL CHECK (date_kind IN ('duration','event_window')),
  recorded_at TEXT NOT NULL,
  supersedes TEXT REFERENCES assertion(assertion_id),
  source_id TEXT NOT NULL REFERENCES source(source_id),
  source_wording TEXT NOT NULL,
  confidence TEXT NOT NULL CHECK (confidence IN ('certain','probable','possible')),
  synthetic TEXT NOT NULL CHECK (synthetic = 'true'),
  CHECK ((value_text IS NULL) != (object_id IS NULL)),
  CHECK (valid_start < valid_end),
  CHECK (supersedes IS NULL OR supersedes != assertion_id)
);
CREATE INDEX assertion_lookup ON assertion(subject_id,predicate,valid_start,valid_end);

-- Current editorial view only; old assertions remain in the underlying table.
CREATE VIEW current_assertion AS
SELECT a.* FROM assertion a
WHERE NOT EXISTS (SELECT 1 FROM assertion n WHERE n.supersedes=a.assertion_id);

-- Append-only assertion ledger. Corrections are new rows, never silent updates.
CREATE TRIGGER no_assertion_update BEFORE UPDATE ON assertion
BEGIN SELECT RAISE(ABORT,'append a superseding assertion instead'); END;
CREATE TRIGGER no_assertion_delete BEFORE DELETE ON assertion
BEGIN SELECT RAISE(ABORT,'assertions are retained for audit'); END;
CREATE TRIGGER ordered_supersession BEFORE INSERT ON assertion
WHEN NEW.supersedes IS NOT NULL
BEGIN
  SELECT CASE WHEN NOT EXISTS (
    SELECT 1 FROM assertion old
    WHERE old.assertion_id=NEW.supersedes
      AND old.subject_id=NEW.subject_id AND old.predicate=NEW.predicate
      AND old.context=NEW.context AND old.recorded_at<NEW.recorded_at
  ) THEN RAISE(ABORT,'supersession must follow the same assertion context') END;
END;
