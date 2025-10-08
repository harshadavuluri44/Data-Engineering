'''

(BIGGEST NOTE :- We cant directly query s3 files using S3 path, we need to create database,
table in Athena using S3 location, then do queries. Each query writes result to configured
s3 path as CSV file)


Amazon Athena

* Serverless query service to analyze data stored in Amazon S3
* Uses standard SQL language to query the files
* Athena can query CSV, JSON, ORC, Avro, and Parquet files in S3 using SQL

* Pricing :- $5 per TB of data scanned

Commonly used for adhoc insights, reporting/dashboards.
----------------------------------------------------------------------------------------

Amazon Athena - Performance Imporvent

* Query only required columns to save cost
* Prefer querying data which of columnar format (Apache parquet, ORC)


* Querying CSV, JSON files using Athena can cost high - So instead first convert them into
  parquet or orc files using AWS ETL tool - GLUE.


* Partition the datasets in AWS S3, so query using athena can help us decrease cost and time
  Ex:- s3://athena-examples/flight/parquet/year=2024/month=6/day=11/

* Maintain larger files (>128 MB) to minimize overhead(extra cost and work)
  Indirectly do optimize
--------------------------------------------------------------------------------------------

Amazon Athena - Federated query

* Allows us to run SQL queries across data stored in relational, non-relational, and custom
  data sources (AWS or on-premises)

* Uses data source connectors that run on AWS lambda to run Federated queries. (Dynamo DB, RDS)

* And store results back in Amazon S3.

NOTE :- Athena can't directly query other databases like RDS, DynamoDB or on-prem without
some help. This can be done with help of Lambda Connector only.


EXAMPLE FLOW : Suppose we want to join S3 sales data with customer data in AURORA

SELECT c.customer_name, s.total_sales
FROM aurora.customers c
JOIN s3.sales s 
    ON c.id = s.customer_id

NOW

1) Athena sends the aurora.customers part to the Aurora Lambda connector.
2) Lambda fetches the data from Aurora and sends it back to Athena.
3) Athena joins it with S3 data

NOTE :-  Before running the query, we must register aurora db with athen 



'''