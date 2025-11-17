"""
How do you optimize PySpark code in production pipelines?

--------------------------------------------------------------------------------------------

1) Use efficient file formats:
      Prefer Parquet/ORC over CSV/JSON for better compression and columnar storage.
   
   Example: while writing data, always choose parquet unless there is a specific reason.

2) Cache/Persist wisely:
      Use df.cache() or df.persist() only when the same DataFrame is reused multiple times.
      Avoid unnecessary caching to save cluster memory.

3) Optimize partitions:
      Check number of partitions using df.rdd.getNumPartitions().
      Use repartition() for full shuffle (expensive but balances data evenly).
      Use coalesce() to reduce partitions without shuffle.

4) Minimize shuffle operations:
      Prefer broadcast joins for small tables (<200 MB) using broadcast().

5) Use DataFrames/Datasets over RDDs:
      DataFrames benefit from Catalyst Optimizer and Tungsten execution engine.
      Provides better performance and less boilerplate code.

6) Use built-in Spark SQL functions instead of UDFs:
      Spark SQL functions are optimized and benefit from Catalyst.
      UDFs are black boxes and slower unless absolutely required.

7) Enable Predicate Pushdown and Column Pruning:
      Filter early in the pipeline to minimize scanned data.
      Read only required columns: df.select("col1", "col2").

8) Monitor and Tune jobs:
      Use Spark UI to identify slow stages, skewed partitions, and long shuffles.
      Optimize skewed joins (salting technique or skew join hints).


MORE POINTS :

* Avoid collect(), take() on huge data to driver node
* Control skew by salting, broadcast join, increase shuffle partitions
* Use proper cluster sizing, for huge datasets use more executors (more parallelism),
                                                   more memory (fewer spills)
* Enable Adaptive Query Execution (AQE)
      Auto optimizes shuffle partitions
      Auto broadcast join when possible
      Handles skew optimization


"""
