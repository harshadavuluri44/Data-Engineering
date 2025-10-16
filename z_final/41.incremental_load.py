'''

How to peform incremental loads in a lakehouse environment?

----------------------------------------------------------------------------------------------

INCREMENTAL Concept

Instead of loading entire dataset every time, incremental load processes only new or updated records.

This saves time, reduce compute usage and avoids overwriting unchanged data.

---------------------------------------------------------------------------------------------------

Implementation in Databricks / Delta Lake:

Use MERGE INTO (Upsert) command to perform incremental updates:


MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.col1 = s.col1, t.col2 = s.col2
WHEN NOT MATCHED THEN
    INSERT (id, col1, col2) VALUES (s.id, s.col1, s.col2)
'''