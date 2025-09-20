'''

Both repartition() and coalesce() are transformations used to change the number of partitions in 
spark.


DIFFERENCES :

    -   Can increase or decrease the number of partitions.
        Can only decrease the number of partitions.

        Always triggers a full shuffle of data to evenly redistribute it across partitions
        Avoids a full shuffle by merging existing partitions together

        Ensures partitions are balanced/ even in size.
        Causes uneven (skewed) partitions

        More expensive
        Faster & Cheaper than repartition

Doing repartition smartly before join operations 
            can reduce shuffle cost and execution time.
'''