"""
What is a Shuffle Operation in Spark?

A shuffle operation in Spark is the process of redistributing data across partitions and cluster 
nodes by moving records so that those with the same key end up in the same partition.

Shuffle → (All rows with the same key, e.g., key:A, are moved into a single partition, regardless 
of how many rows exist for that key).

-----------------------------------------------------------------------------------------------
When does Shuffle occur?
Shuffle happens during wide transformations where data needs to be grouped, aggregated, or joined 
based on a key.

Examples: .groupBy(), .reduceByKey() / .groupByKey(), .join()
          .distinct(), .repartition()

-----------------------------------------------------------------------------------------------
Why are Shuffles expensive?
Shuffles are among the most costly operations in Spark because they involve:
    Moving large amounts of data across cluster nodes (network I/O)
    Writing intermediate shuffle files to disk and reading them back
    Serialization / Deserialization overhead

-----------------------------------------------------------------------------------------------
Optimization strategies to reduce shuffle cost:

    Use broadcast joins when one dataset is small
    Use reduceByKey instead of groupByKey (reduces data before shuffle)
    Repartition and coalesce wisely (avoid unnecessary shuffles)
    Apply bucketing on both tables using the same column before joining

-----------------------------------------------------------------------------------------------

Summary:
    Shuffle = Data movement across partitions/nodes.
    It's expensive and should be minimized through partitioning, bucketing, and using efficient 
    transformations.
"""
