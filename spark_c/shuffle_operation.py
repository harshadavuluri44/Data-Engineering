'''
What is a Shuffle Operation in Spark?

A shuffle operation in Spark is a mechanism for redistributing data across partitions and cluster
nodes. During a shuffle, data is reorganized so that records with same key are moved to same
partition.

When Shuffle occur
Shuffle operations are triggered by TRANSFORMATION that require data from multiple partitions to
be combined or reorganized;

* groupByKey, reduceByKey, aggregateByKey
* join 
* distinct
* repartition and coalesce
* sortBy and orderBy

Why Shuffles are expensive?
Shuffles are among the most costly operations in spark bcz

* Moving large amounts of data across cluster nodes
* Writing intermediate shuffle files and reading them back
* serialization/ Deserialization 


Optimization Strategies
* Leverage broadcast joins for small datasets
* use appropriate number of partitions through repartition and coalsece
* Used reduceByKey instead of groupByKey
'''
