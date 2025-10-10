'''
LINEAGE in Spark

    Lineage is Spark's way of tracking the sequence of transformations applied to an RDD or DataFrame
    to produce a new RDD/DataFrame.
    It forms a logical DAG of operations, showing how each RDD/DataFrame is derived from its parent.

Example:
    rdd1 -> map() -> rdd2 -> filter() -> rdd3

--------------------------------------------------------------------------------------------------

WHY LINEAGE MATTERS:

    Instead of replicating intermediate data on disk for fault tolerance, Spark can recompute 
    lost partitions using lineage.
    
    Efficiently supports fault recovery without storing all intermediate results.

------------------------------------------------------------------------------------------------

HOW SPARK HANDLES FAILURE RECOVERY:

1) If a partition of an RDD is lost due to executor failure or node crash:
    a) Spark checks the lineage DAG of that RDD.
    b) It recomputes only the lost partition(s) by reapplying transformations from parent RDDs.
    c) Tasks are re-executed only for lost partitions, not the entire dataset.

------------------------------------------------------------------------------------------------

KEY ADVANTAGES:

    a) No need to replicate all intermediate data → saves memory/disk.
    b) Efficient and scalable recovery for large datasets.

------------------------------------------------------------------------------------------------

CHECKPOINTING:

    a) For very long lineage chains, recomputation can be expensive.
    b) Spark allows checkpointing, which writes RDDs to stable storage (HDFS/S3), 
       so lineage before that point can be discarded.

-------------------------------------------------------------------------------------------------

'''
