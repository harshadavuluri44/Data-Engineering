'''

How to peform incremental loads in a lakehouse environment?

----------------------------------------------------------------------------------------------

INCREMENTAL Concept

Instead of loading entire dataset every time, incremental load processes only new or updated records.

This saves time, reduce compute usage and avoids overwriting unchanged data.

---------------------------------------------------------------------------------------------------

Implementation in Databricks / Delta Lake:

Use MERGE INTO (Upsert) command to perform incremental updates:

MERGE DEFINITION :  Perform conditional INSERT, UPDATE or DELETE in a single statement by matching
source and target data, i.e It updates matching records, insert new records or deletes old records.


MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.col1 = s.col1, t.col2 = s.col2
WHEN NOT MATCHED THEN
    INSERT (id, col1, col2) VALUES (s.id, s.col1, s.col2)


OR

Use dataframe approach

spark.conf.set('spark.sql.sources.partitionOverwriteMode', 'dynamic')

df = spark.read.format('parquet').load('source_location_s3')

df.write.format('delta').mode('overwrite').partitionBy('date').saveAsTable('delta_table')
------------------------------------------------------------------------------------------------


mode('overwrite') + spark.sql.sources.partitionOverwriteMode = 'dynamic'

    The above config implies, only partitions present in df and delta table gets overridden,
not the whole table.
                          

'''