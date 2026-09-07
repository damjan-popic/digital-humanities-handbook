-- :as_of is historical time; :known_at is the editorial snapshot, in UTC.
-- Inclusion of an event_window means possible occurrence, NOT continuous validity.
SELECT a.assertion_id,a.predicate,a.value_text,a.object_id,a.context,
       a.date_kind,a.source_id,a.source_wording,a.source_wording_relation,a.confidence
FROM assertion a
WHERE a.subject_id=:subject
  AND a.valid_start<=:as_of AND :as_of<a.valid_end
  AND a.recorded_at<=:known_at
  AND NOT EXISTS (
    SELECT 1 FROM assertion n
    WHERE n.supersedes=a.assertion_id AND n.recorded_at<=:known_at
  )
ORDER BY a.predicate,a.assertion_id;
