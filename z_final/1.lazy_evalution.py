'''

LAZY EVALUATION in SPARK

In Spark, transformations (like .filter(), .select(), .map()) are not executed immediately.
Instead, Spark builds a logical plan, called a DAG (Directed Acyclic Graph), that describes all 
the transformations.

Transformations are only executed when an action is called, such as .collect(), .count(), etc.

-------------------------------------------------------------------------------------------------

WHY Lazy Evaluation is Useful?

1. Optimization (via Catalyst Optimizer)

    Spark can analyze the full chain of transformations before execution.
    It can reorder, combine, or push down operations (like filters) to improve performance.

2. Fault Tolerance

    Spark can recompute lost data using the DAG instead of storing all intermediate results.
    This allows efficient recovery from node failures.

3. Efficiency

    Computations that are not needed are skipped, reducing unnecessary work, This helps save time 
    and resources.

-------------------------------------------------------------------------------------------------

'''