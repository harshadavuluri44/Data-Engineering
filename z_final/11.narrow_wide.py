"""
Narrow vs Wide Transformations in Spark

Narrow Transformations:
   Each task/partition can be processed independently without requiring data from other partitions.
   Does NOT require a shuffle.

Examples: .withColumn(), .filter(), .map(), .select()

-------------------------------------------------------------------------------------------------
Wide Transformations:
   Processing a task/partition may require data from multiple partitions, triggering a shuffle.

Examples: .groupBy(), .join(), .reduceByKey(), .distinct()

--------------------------------------------------------------------------------------------------
Key Differences:

1. Shuffle:
      Narrow: No shuffle required
      Wide: Shuffle required

2. Performance:
      Narrow: Faster
      Wide: Slower due to shuffle overhead

3. Fault Tolerance:
      Narrow: Quick recovery (can recompute only affected partitions)
      Wide: Slower recovery (requires recomputing shuffled data)

4. Memory Usage:
      Narrow: Constant memory per partition
      Wide: Memory usage can vary depending on size of partition; may cause OOM, data skew, etc.

"""