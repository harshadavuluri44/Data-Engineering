"""
Narrow vs Wide Transformations in Spark

Narrow Transformations:
   Each task/partition can be transformed independently without requiring data from other partitions.
   Does NOT require a shuffle.

Examples: .withColumn(), .filter(), .map(), .select()

-------------------------------------------------------------------------------------------------
Wide Transformations:
   Transforming a task/partition may require data from multiple partitions, triggering a shuffle.

Examples: .groupBy(), .join(), .reduceByKey(), .distinct()

--------------------------------------------------------------------------------------------------
Key Differences:

Aspect	        Narrow Transformation	                     Wide Transformation

Shuffle	        No shuffle required	                     Shuffle required
Performance	     Faster	                                    Slower (due to shuffle overhead)
Fault Tolerance  Quick recovery                             Slower recovery
                 (recompute only affected partitions)	      (recompute shuffled data)
Memory Usage     Constant per partition	                  Can vary; may cause OOM or data skew

"""