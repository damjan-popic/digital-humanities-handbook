-- A review queue, not an automatic finding of historical contradiction.
SELECT a.assertion_id AS assertion_a,b.assertion_id AS assertion_b,
       a.context AS context_a,b.context AS context_b,
       a.value_text AS value_a,b.value_text AS value_b,
       a.source_id AS source_a,b.source_id AS source_b
FROM current_assertion a JOIN current_assertion b
  ON a.subject_id=b.subject_id AND a.predicate=b.predicate
 AND a.assertion_id<b.assertion_id
 AND a.valid_start<b.valid_end AND b.valid_start<a.valid_end
WHERE a.predicate='status' AND a.value_text!=b.value_text
ORDER BY a.assertion_id,b.assertion_id;
