'''
Q. A SPARK JOB KEEPS FAILING DUE TO 'OutOfMemoryError'. How would you troubleshoot?

A.

1. Identify where OOM Happens

   * Check Spark UI / logs -> is it failing on:
   
   Driver (common with large collect/ show like actions)?
   Executor (common incase of wide transformations, shuffles, joins)?


2. For Driver OOM
  
   * Don't use collect() on huge datasets -> use limit, take, or write to storage

   NOTE :- .show(100) → prints 100 records (for display, not a DataFrame)

           .limit(100) → returns a new DataFrame limited to 100 rows (lazy until an action)

           .take(100) → returns a list of 100 Row objects to the driver (immediate action)

   IMP :- collect(), show() actions pull data from executors to JVM Heap

   * Incease driver memory:  spark.driver.memory 10g (use this in DBX cluster)

3. For Executor OOM
   
   * check memory configs: Increase executor memory:
      --executor-memory 8g
      --executor-cores 5

   * Check data skew
     If one task/partition is huge while others are small -> handle skew (salting, AQE skew join)

   * Increase shuffle partitions: spark.sql.shuffle.partitions 400

   * Use broadcast joins for small tables

4. Optimize Data & Code
   
    * Use parquet/ORC instead of CSV/JSON (parquet is binary formmated and columnar)

    * Use dataframe API instead of RDD's -> catalyst optimizer is smarter

    * persist/cache only when reused - use MEMORY_AND_DISK storage level

    DISK MEANS MACHINE'S HARD DRIVE OR SSD
'''