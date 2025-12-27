'''

What is Data Skew?

Data Skew means when data is unevenly distributed across partitions in a cluster nodes of distributed
computing system like spark.

i.e Some partitions have huge amount of data (hot partitions) and others have little data
---------------------------------------------------------------------------------------------------

Data Skew causes 

* Stragglers (slow tasks that process large partitions)
* Wasted resources (most executors finish quickly, but a few keep running)
* Performance bottlenecks


Example :

If 90% of rows have country = 'US' and other countries make up rest, then:
    Partition holding US data will be huge
    That executor will take much longer time to finish spark job
---------------------------------------------------------------------------------------------------

How do you debug from spark UI to detect/confirm data skew ?


1. Check the Jobs tab and note total duration and number of stages
2. Identify which stage took longest time
3. Click on the slow stage(from step 2) and open the Tasks
4. Check tasks time and input size in tasks inside slow stage
        If tasks are taking 10X longer time and
        input size per task is more compared to other

        Then we can confirm the skew.

---------------------------------------------------------------------------------------------------
HANDLING DATA SKEW 

Scenario : Fact table has skew on customer_id, Please find the total amount spent for each customer.

1. Salting Technique

STEP 1: Add a salt key to spread skewed customer_ids across partitions

        from pyspark.sql.functions import col, rand, floor,

        N=50  # number of salts

        df_salted = df.withColumn('customer_id_salted', col('customer_id').cast('string') +
                                                        "_" +
                                                        floor(rand() * N))

        This breaks one skewed customer into 50 smaller distributed groups

STEP 2: Group by the salted key

        df_partial = df_salted.groupBy('customer_id_salted').agg(sum('amount').alias('partial_sum'))

STEP 3: Final groupBy on actual customer_id

        from pyspark.sql.functions import split

        df_final= df_partial.withColumn('customer_id', split('customer_id_salted', '_')[0])
                            .groupBy('customer_id')
                            .agg(sum('partial_sum').alias('total_amount_spent'))

-----------------------------------------------------------------------------------------------------

2. Broadcast Joins : If one side of join is small, broadcast it to all executors

This avoids shuffling the skewed big table.

df_big.join(broadcast(df_small), 'key')

-----------------------------------------------------------------------------------------------------

3. Repartitioning : Use repartition() with a better a column that balances data

-----------------------------------------------------------------------------------------------------

4. Increase parallelism : Increase the number of shuffle partitions

spark.conf.set('spark.sql.shuffle.partitions', 1000)

-> During wide operations as shuffle takes place, the number of partitions will become 1000 by
   default.

------------------------------------------------------------------------------------------------------

5. Bucketing : Pre-bucket tables on join keys -> reduce skew at runtime

------------------------------------------------------------------------------------------------------

6. In Spark 3.0 + AQE automatically handles data skew

'''