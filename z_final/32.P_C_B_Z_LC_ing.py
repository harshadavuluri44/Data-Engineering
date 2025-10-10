'''

PARTITIONING, CLUSTERING, BUCKETING, Z-ORDERING, LIQUID CLUSTERING
-------------------------------------------------------------------------------------------------

1. PARTITIONING
Splitting a large table into smaller physical directories/partitions based on the value of one or
more columns.

PURPOSE: Helps prune unnecessary data during queries -> faster reads

EXAMPLE: Table - sales(year, month, country, amount)
Partition by year -> creates directories:
    /sales/year=2023/
    /sales/year=2024/

Query: SELECT * FROM sales WHERE year=2023 
    only reads the /sales/year=2023/ partition

-------------------------------------------------------------------------------------------------

2. CLUSTERING
Organizing data within each partition by sorting/grouping rows on one or more columns. Happens 
inside parquet/delta files, not at directory level.

PURPOSE: Makes range and filter queries faster due to ordered/grouped data

EXAMPLE: sales table partitioned by year, clustered by country

-------------------------------------------------------------------------------------------------

3. BUCKETING
Organizing data into fixed number of buckets (files, not folders) based on hash value of a column.

PURPOSE: Speeds up joins and aggregations by reducing shuffles

EXAMPLE: orders(order_id, customer_id, amount)
Bucket by customer_id into 8 buckets -> rows with same customer_id go to same bucket
Join with customer table bucketed on customer_id -> more efficient

-------------------------------------------------------------------------------------------------

4. Z-ORDERING
A multi-dimensional clustering technique in Delta Lake that co-locates related data across multiple
columns into the same physical blocks.

PURPOSE: Optimizes queries with multiple filter conditions (multi-column predicates)

EXAMPLE: sales(customer_id, product_id, sale_date, amount)
OPTIMIZE sales ZORDER BY (customer_id, product_id)

-------------------------------------------------------------------------------------------------

5. LIQUID CLUSTERING
A dynamic, self-optimizing clustering method in Delta Lake (Databricks).

NOTES:
    Automatically reorganizes data for optimal query performance 
    Reduces need for manual OPTIMIZE ... ZORDER BY

EXAMPLE:
Create Delta table with liquid clustering on customer_id
As new data arrives, Delta automatically maintains clustering 
on customer_id for faster queries

-------------------------------------------------------------------------------------------------
'''