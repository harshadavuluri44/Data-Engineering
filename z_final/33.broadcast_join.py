'''

Explain broadcast joins in Spark. What's the default broadcast threshold?
When does broadcasting hurt performance?

-------------------------------------------------------------------------------------------------

A broadcast join is an optimization technique in Spark to avoid shuffle


* The smaller dataset is broadcasted(copied) to all executors.
* This avoids a shuffle of the larger dataset during a join.


from pyspark.sql.functions import broadcast

df_large.join(broadcast(df_small), 'id')

How it works?

* Spark driver broadcasts df_small to all worker nodes
* Each executor joins its partition of df_large locally with in-memory copy of df_small
* Eliminates expensive shuffle and network I/O

------------------------------------------------------------------------------------------------

Default broadcast threshold in Spark is 10MB

We can change the value by

spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '50MB')

-------------------------------------------------------------------------------------------------

when does broadcast join hurt performance ?

1. If small dataset is actually large (hundreds of MBs or GBs) - causes OOM

2. Too many executors - Each executor gets a copy, memory duplication across nodes.
                        (consumption of memory is high)

'''