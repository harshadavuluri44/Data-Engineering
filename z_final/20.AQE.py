'''

AQE = Adaptive Query Execution  (Introduced in Spark 3.0)

It means Spark can optimize the query plan at runtime, after it has already started executing

Normally, Spark makes an execution plan before running (logical -> physical plan). But it cannot
predict actual data size until it runs and can't changes the plan based on data size and partitions

-> AQE solves this by adapting the plan dynamically using real-time statistics.

-----------------------------------------------------------------------------------------------

3 SITUATIONS MAINLY AQE is required


1. Dynamic Coalescing of shuffle partitions

    If spark creates 1000 shuffle partitions but only 10 have data, AQE merges them into few
    partitions to avoid overhead

    Helps avoid many small tasks

2. Dynamic Switching of Join Strategies

    If one side of join turns out to be small, AQE can switch from sort-merge join 
    -> broadcast join at runtime

3. Handling skewed joins

    AQE can detect data skew (e.g., one partition has way more rows) and split the skewed partitions
    into smaller ones for better parallelism


-----------------------------------------------------------------------------

ENABLING AQE

spark.conf.set('spark.sql.adaptive.enabled', 'true')

spark.conf.set('spark.sql.adaptive.coalescePartitions.enabled', 'true')

spark.conf.set('spark.sql.adaptive.skewJoin.enabled', 'true')
'''