'''

In Spark, caching and persisting are ways to store intermediate results in memory (or disk) so they
can be reused later without recomputation.
--------------------------------------------------------------------------------------------------

cache() stores data in memory only (MEMORY_ONLY storage level).
persist() stores data in memory and disk also

cache() is used for reuse of smaller dataframes that can fit in memory
persist() is used for large data that may not fit in memory
-------------------------------------------------------------------------------------------------

Storage levels

MEMORY_ONLY
MEMORY_AND_DISK
DISK_ONLY
MEMORY_ONLY_SER
MEMORY_AND_DISK_SER

df.persist(StorageLevel.MEMORY_AND_DISK)


unpersist  ->  df.unpersist()


In dbx :-    spark.databricks.io.cache.enabled true (MEMORY AND DISK both)
                                                    DISK is preferred primarily

'''