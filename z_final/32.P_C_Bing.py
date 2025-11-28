'''

PARTITIONING, CLUSTERING, BUCKETING, LIQUID CLUSTERING
-------------------------------------------------------------------------------------------------

PARTITIONING / HIVE PARTITIONING

Splitting a large table into smaller physical directories/partitions based on the value of one or
more columns.


EXAMPLE: Table - sales(year, month, country, amount)

df.write.format('delta').partitionBy('year').saveAsTable('sales')

Now, files are stored in disk like this
        /sales/
            year=2023/
            year=2024/
            year=2025/

SELECT * FROM sales WHERE year=2023 
    only reads the /sales/year=2023/ folder

Purpose:
    Faster queries and much cheaper
    Efficient filtering based on WHERE clause

-------------------------------------------------------------------------------------------------

CLUSTERING

Organizing data within each partition by sorting/grouping rows on one or more columns. Happens 
inside parquet/delta files, not at directory level.

PURPOSE: Makes range and filter queries faster due to ordered/grouped data

EXAMPLE: sales table partitioned by year, clustered by country

-------------------------------------------------------------------------------------------------

BUCKETING

Organizing data into fixed number of files(buckets) (not folders) based on hash value of a column.

PURPOSE: Speeds up joins and aggregations by reducing shuffles

EXAMPLE: orders(order_id, customer_id, amount)

CREATE TABLE sales (
    customer_id STRING,
    amount DOUBLE
)
CLUSTERED BY (customer_id) INTO 8 BUCKETS;


Bucket by customer_id into 8 buckets -> rows with same has value of customer_id go to same bucket
Join with customer table bucketed on customer_id -> more efficient

-------------------------------------------------------------------------------------------------

'''