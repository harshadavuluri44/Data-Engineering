'''

What is Data Skew?

Data Skew means when data is unevenly distributed across partitions in a cluster nodes of distributed
computing system like spark.

i.e Some partitions have huge amount of data (hot partitions) and others have little data


Data Skew causes 

* Stragglers (slow tasks that process large partitions)
* Wasted resources (most executors finish quickly, but a few keep running)
* Performance bottlenecks


Example :

If 90% of rows have country = 'US' and other countries make up rest, then:
    Partition holding US data will be huge
    That executor will take much longer time to finish spark job
------------------------------------------------------------------------------------------------

How do you debug from spark UI to detect/confirm data skew ?


1. Check the Jobs tab and note total duration and number of stages
2. Identify which stage took longest time
3. Click on the slow stage(from step 2) and open the Tasks
4. Check tasks time and input size in tasks inside slow stage
        If tasks are taking 10X longer time and
        input size per task is more compared to other

        Then we can confirm the skew.

------------------------------------------------------------------------------------------------
HANDLING DATA SKEW

1. Salting the keys : Add random prefix or suffix to skewed keys to artificially spread them across
                      partitions


Ex :-

salted_df = df.withColumn('salted_key', concat_ws('_',col('country'),(rand()*10.cast('int'))))


2. Broadcast Joins : If one side of join is small, broadcast it to all executors

This avoids shuffling the skewed big table.

df_big.join(broadcast(df_small), 'key')



3. Repartitioning : Use repartition() with a better a column that balances data



4. Increase parallelism : Increase the number of shuffle partitions

spark.conf.set('spark.sql.shuffle.partitions', 1000)

-> During wide operations as shuffle takes place, the number of partitions will become 1000 by
   default.


5. Bucketing : Pre-bucket tables on join keys -> reduce skew at runtime

6. In Spark 3.0 + AQE automatically handles data skew


'''