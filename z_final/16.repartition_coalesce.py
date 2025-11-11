'''
Both repartition() and coalesce() are transformations used to change the number of partitions in
Spark.

--------------------------------------------------------------------------------
DIFFERENCES:

1. df_r = df.repartition(100)

        Can increase or decrease the number of partitions.
        Always triggers a full shuffle of data to evenly redistribute it across partitions.
        Ensures partitions are balanced/even in size.
        More expensive in terms of computation.

2. df_c = df.coalesce(10)

        Can only decrease the number of partitions.
        Avoids a full shuffle by merging existing partitions together.
        May cause uneven/skewed partitions.
        Faster and cheaper than repartition().

--------------------------------------------------------------------------------
TIP:

    Doing repartition smartly before join operations can reduce shuffle cost and execution time.

'''
