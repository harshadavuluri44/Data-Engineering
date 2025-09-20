'''

PARTITIONING,   CLUSTERING,     BUCKETING,    Z-ORDERING,    LIQUID-CLUSTERING

-----------------------------------------------------------------------------------------------

1. PARTITIONING

Splitting large table into small physical directories/ partitions based on the value of one or more
columns.

PURPOSE : Helps prune unnecessary data during queries -> faster reads

EAMPLE: Table - sales (year, month, country, amount)

partition sales table by year   - means -> create directories:
    /sales/year=2023/
    /sales/year=2024/

Query like SELECT * FROM sales WHERE year=2023 -> only reads the 2023 partition directory

--------------------------------------------------------------------------------------------------

2. CLUSTERING

Organizing data within each partition based on the values of one or more columns by sorting or 
grouping rows together inside parquet or delta files.


* NOTE : It doesn't create new directories

PURPOSE : Makes range or filter queries faster due to sorted and grouped data

EXAMPLE : sales table Partitioned by year, clustered by country

-------------------------------------------------------------------------------------------------

3. BUCKETING

Organizing data into n buckets (.parquet files not folders) based on hash value of column

PURPOSE : Speeds up joins and aggregation by avoiding shuffles.

EXAMPLE : Table - orders(order_id, customer_id, amount)

Bucket by customer_id into 8 buckets -> rows with same customer_id go into same bucket

Join with customer table bucketed on same column (customer_id) -> more efficient

-------------------------------------------------------------------------------------------------

4. Z-ORDERING

A multi-dimensional clustering technique used in Delta lake that co-locates related data across
multiple columns in same physical blocks


PURPOSE : Optimizes filter queries with multiple predicates

EXAMPLE : Table - sales (customer_id, product_id, sale_date, amount)

OPTIMIZE sales ZORDER BY (customer_id, product_id)

-------------------------------------------------------------------------------------------------

5. LIQUID CLUSTERING

A dynamic, self-optimizing clustering method used in Databricks Delta tables.

NOTES

Automatically reorganizes data for optimal query performance without manual re-clustering

Reduces need for explicit OPTIMIZE .... ZORDER BY operations


EXAMPLE :

create Delta table and enable liquid clustering on customer_id

As data is ingested, Delta Lake continously maintains clustering on customer_id to speed up queries
'''