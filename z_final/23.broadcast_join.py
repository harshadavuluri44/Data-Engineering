'''

Explain broadcast joins in Spark. What's the default broadcast threshold?
When does broadcasting hurt performance?

------------------------------------------------------------------------------------------------------


A Broadcast join is where small table is sent(broadcast) to all worker nodes so that join can happen
locally on each partition of the larger table


    This avoids expensive shuffling of large table across cluster.
    Greatly improves performance for small * large table joins.


from pyspark.sql.functions import broadcast

df_large.join(broadcast(df_small), on='id')

------------------------------------------------------------------------------------------------------

Default broadcast threshold in Spark is 10MB

We can change the value by

    spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '50MB')

------------------------------------------------------------------------------------------------------

when does broadcast join hurt performance ?

1. Both tables are actually large (hundreds of MBs or GBs) - causes OOM

2. Too many executors - Each executor gets a copy, memory duplication across nodes.
                        (consumption of memory is high)


'''