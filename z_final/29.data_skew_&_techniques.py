'''

What is Data Skew?

Data Skew means when data is unevenly distributed across partitions in a cluster nodes of distributed
computing system like spark.

i.e Some partitions have huge amount of data (hot partitions)
    Others have very little data


Data Skew causes 

* Stragglers (slow tasks that process large partitions)
* Wasted resources (most executors finish quickly, but a few keep running)
* Performance bottlenecks


Example :

If 90% of rows have country = 'US' and other countries make up rest, then:
    Partition holding US data will be huge
    That executor will take much longer time to finish spark job



HANDLING DATA SKEW

1. Salting the keys : Add random prefix or suffix to skewed keys to artificially spread them across
                      partitions


Ex :-

salted_df = df.withColumn('salted_key', concat_ws('_',col('country'),(rand()*10.cast('int'))))


2. Broadcast Joins : If one side of join is small, broadcast it to all executors

This avoids shuffling the skewed big table.

df_big.join(broadcast(df_small), 'key')



3. Repartitioning : Use repartition() with a better a column that balances data



4. Incease parallelism : Increase the number of shuffle partitions

spark.conf.set('spark.sql.shuffle.partitions', 1000)

-> During wide operations as shuffle takes place, the number of partitions will become 1000 by
   default.


5. Bucketing : Pre-bucket tables on join keys -> reduce skew at runtime

6. In Spark 3.0 + AQE automatically handles data skew


'''