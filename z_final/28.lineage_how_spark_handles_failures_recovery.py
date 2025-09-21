'''

LINEAGE in Spark

    Lineage is Spark's way of tracking the sequence of transformations applied to a rdd/DataFrame
to produce a new rdd/dataframe

It forms a logical DAG of operations, showing how each rdd/df is derived from its parent


WHY LINEAGE MATTERS : Instead of replicating intermediate data on disk for fault tolerance, Spark
can recompute lost partitions using lineage.

Example :  rdd1 -> map() -> rdd2 -> filter() -> rdd3

----------------------------------------------------------------------------------------------

HOW SPARK HANDLES FAILURE RECOVERY ?


1) If a partition of an RDD is lost due to executor failure or node crash

    a) Spark looks at the lineage DAG of that RDD
    b) It recomputes only the lost partition(s) by reapplying transformations from parent RDDs
    c) Tasks are re-executed only for the lost partitions, not entire dataset.


KEY ADVANTAGES :

    a) No need to replicate all intermediate data (saves memory/disk)
    b) Efficient and scalable recovery for large datasets

CHECKPOINTING :

    a) For very long lineage chains, recomputation can be expensive
    b) Spark allows checkpointing, which writes RDDs to stable storage (HDFS/S3), so lineage before
    that point can be discarded.

'''