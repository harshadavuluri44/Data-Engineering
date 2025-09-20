'''
What is Lazy Evaluation in Spark?

* In Spark, transformations like (.filter, .select, etc) do not execute immediately.

* Instead, spark builds a logical plan (a DAG) describing the sequence of operations.

* Actual execution happens only when an action (like .collect, .count, etc) is called.

-----------

WHY IS LAZY EVALUATION IS USEFUL ?

1. Optimization (Catalyst optimizer in Spark SQL)

    Spark can look at entire chain operations and optimize execution (e.g, push filters down,
    combine operations).

2. Fault Tolerance

    Spark can recompute missing data using DAG instead of storing intermediate results.

3. Efficiency

   Unnecessary computations are skipped if their results aren't needed.

'''