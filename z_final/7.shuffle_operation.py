'''
What is a Shuffle Operation in Spark?

A shuffle operation in Spark is the process of redistributing data across partitions and cluster 
nodes by moving records, so that those with the same key end up in the same partition.


When Shuffle occurs?
Shuffle occurs when data needs to be grouped, aggregated or joined based on a key.
i.e WIDE TRANSFORMATIONS like 
                        groupBy,
                        joins, etc., 


Optimization Strategies to avoid shuffles
    - Leverage broadcast joins when one table is of small size
    - Do repartition and coalesce wisely
    - Prefer reduceByKey over groupByKey
    - Apply bucketing on both tables using the same column before performing a join

    

Why Shuffles are expensive?
Shuffles are among the most costly operations in spark bcz

* Moving large amounts of data across cluster nodes
* Writing intermediate shuffle files and reading them back
* serialization/ Deserialization


'''