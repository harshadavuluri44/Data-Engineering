'''
Partitioning :- It is dividing a large dataset into smaller, more manageable pieces (partitions)
based on value of one or more columns.

In Spark/Databricks, partitioning means physicially storing data in separate folders in storage
(e.g., S3, ADLS, DBFS)

Example :- partition sales data by country,

s3/sales/country=US/...
s3/sales/country=IN/...
s3/sales/country=UK/...

Pros:
* Improves query performance (pruning: spark reads only relevant partitions)
* Reduces I/O overhead when filtering on partition column

Cons:
* Too many partitions (high cardinality of countries) -> to many small files -> 
  performance degradation (while reading whole data)

------------------------------------------------------------------------------------------------

Bucketing :- It is dividing data into fixed number of buckets (files) based on hash value of column

Unlike partitioning, bucketing does not create folders; instead, data is evenly distributed into
bucket files

Example : If we bucket sales data into 8 buckets on customer_id, spark will hash each customer_id
and assign it to one of 8 buckets

Pros:
* Useful for joins -> spark can avoid shuffles if two datasets are bucketed on same column & number
  of buckets.
* Better control over file sizes compared to partitioning
'''