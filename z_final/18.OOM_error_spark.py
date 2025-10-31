"""
Q: A Spark job keeps failing due to 'OutOfMemoryError'. How would you troubleshoot?


1. Identify Where the OOM Happens

   Check Spark UI / logs to see if the failure occurs in:
      Driver (common when using large `collect()` or `show()` actions)
      Executor (common during wide transformations, shuffles, joins)

-----------------------------------------------------------------------------------------------
2. Driver OOM

   Avoid using collect() on huge datasets. Instead, use:

      .limit(100)   → Returns a new DataFrame limited to 100 rows (lazy until an action)
      .show(100)   → Displays 100 rows (for viewing only; pulls data to driver)

Important: Actions like `collect()` or `show()` pull data from executors to the driver JVM heap.


Increase driver memory if needed:

      spark.driver.memory 10g

-----------------------------------------------------------------------------------------------
3. Executor OOM

   Increase executor memory and cores:

      spark.executor.memory 8g
      spark.executor.cores 5


   Check for data skew:
      If one partition/task is much larger than others → handle skew via:
         Salting keys
         Adaptive Query Execution (AQE) skew join optimization

      spark.sql.adaptive.enabled true
      spark.sql.adaptive.skewJoin.enabled true


   Increase shuffle partitions:

      spark.sql.shuffle.partitions = 400

   
   Use broadcast joins when one table is small.

-----------------------------------------------------------------------------------------------
4. Optimize Data & Code

   Use columnar formats like Parquet/ORC instead of CSV/JSON (better compression + faster reads).  
   Prefer DataFrame / Dataset API over RDDs (Catalyst optimizer can optimize queries).  
   Cache / persist only when necessary. Use `MEMORY_AND_DISK` storage level:
      Disk here refers to the machine's hard drive or SSD.

-----------------------------------------------------------------------------------------------


OOM occurs when

1. large data collections
2. data skew
3. wide transformations with excessive data shuffle
4. caching/ persisting large data

"""